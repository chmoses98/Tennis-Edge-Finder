# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-24T21:37Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 52,135): 0-3 13.9%, 3-5 9.4%, 5-10 19.7%, 10-15 15.3%, 15-25 19.2%, 25-40 14.1%, 40+ 8.3%; median gap 12.12 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 76.8%, Challenger 11.9%, doubles 6.6%). Main tour: ATP 4.6% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 11,661): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.8%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.0%, POOR_DATA 8.6%, POSSIBLY_IN_PLAY_QUOTE 5.5%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.2%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.8%, market_freshness 18.8%, execution 18.0%, data 12.1%, market_freshness/coverage 9.0%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 11,661 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 22.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.0%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.1% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 498.0 points vs 1712.5 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.03, Gen-2 0.835, Gen-1 ledger 0.859 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 567 model 0.2232 vs Kalshi 0.2095; n 114 model 0.2782 vs Kalshi 0.1979.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 225,890 model-market comparisons (367,566 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 75,386 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-24T21:23:19.761938+00:00'], shadow board 60,358 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-24T21:23:23.943244+00:00'], Model 4 28,347 rows, 20,139 settled tickers, 7,081 tickers with an external scan.
* By model: {"gen1_ledger": 51279, "gen1_elo": 30354, "fair_v1": 30354, "gen2": 30354, "gen1_sr": 30354, "model4_fundamental": 26615, "model4_conditioned": 26580}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 52,135 | 13.9 | 9.4 | 19.7 | 15.3 | 19.2 | 14.1 | 8.3 | 12.12 | 41.6% | 22.4% |
| MW fair_v1 | 30,354 | 12.8 | 8.5 | 18.5 | 15.5 | 19.7 | 15.1 | 10.0 | 13.21 | 44.8% | 25.1% |
| MW gen1_elo | 30,354 | 12.7 | 8.5 | 18.9 | 15.2 | 19.9 | 15.0 | 9.7 | 13.02 | 44.6% | 24.8% |
| MW gen1_ledger | 21,781 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.8 | 10.55 | 37.2% | 18.6% |
| MW gen1_sr | 30,354 | 10.2 | 7.0 | 16.5 | 13.6 | 20.8 | 18.8 | 13.1 | 16.07 | 52.6% | 31.8% |
| MW gen2 | 30,354 | 10.9 | 7.3 | 16.2 | 14.0 | 19.4 | 18.0 | 14.2 | 15.66 | 51.6% | 32.2% |
| all families model4_conditioned | 26,580 | 21.9 | 18.9 | 34.8 | 17.5 | 4.4 | 1.5 | 1.0 | 5.97 | 7.0% | 2.5% |
| all families model4_fundamental | 26,615 | 16.8 | 13.3 | 34.1 | 20.4 | 10.6 | 3.5 | 1.3 | 7.75 | 15.3% | 4.8% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.9%, >=15pp 41.6%, >=20pp 31.0%, >=25pp 22.4%, >=30pp 16.2%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.49pp; >=10pp 45.5%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,672 | 28.1 | 14.2 | 24.9 | 15.5 | 11.9 | 4.6 | 0.8 | 6.17 | 17.2% | 5.3% |
| CHALLENGER | 4,695 | 15.7 | 9.9 | 20.4 | 15.4 | 14.9 | 12.5 | 11.1 | 11.12 | 38.5% | 23.6% |
| ITF_MEN | 8,394 | 10.1 | 7.3 | 16.8 | 14.6 | 21.6 | 17.4 | 12.2 | 15.46 | 51.2% | 29.6% |
| ITF_WOMEN | 12,023 | 9.4 | 6.8 | 15.9 | 15.3 | 22.3 | 18.2 | 12.1 | 15.82 | 52.5% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,904 | 17.5 | 12.9 | 26.2 | 19.2 | 17.5 | 6.0 | 0.7 | 8.25 | 24.3% | 6.7% |
| WTA125 | 660 | 13.3 | 7.4 | 23.5 | 20.4 | 19.9 | 13.5 | 2.0 | 11.31 | 35.3% | 15.4% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,672 | 24.0 | 15.1 | 24.7 | 17.7 | 13.0 | 4.6 | 1.0 | 6.63 | 18.6% | 5.6% |
| CHALLENGER | 4,695 | 15.0 | 8.7 | 18.4 | 14.6 | 17.4 | 14.0 | 11.9 | 12.54 | 43.4% | 25.9% |
| ITF_MEN | 8,394 | 8.2 | 5.9 | 14.4 | 13.0 | 19.7 | 21.1 | 17.9 | 18.77 | 58.6% | 38.9% |
| ITF_WOMEN | 12,023 | 8.1 | 5.6 | 13.7 | 13.2 | 20.6 | 21.0 | 17.8 | 19.13 | 59.3% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,904 | 14.0 | 10.2 | 22.2 | 16.3 | 22.5 | 13.4 | 1.3 | 10.94 | 37.3% | 14.8% |
| WTA125 | 660 | 6.8 | 4.7 | 17.0 | 17.4 | 26.1 | 19.2 | 8.8 | 16.84 | 54.1% | 28.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,672 | 23.7 | 12.6 | 23.9 | 16.5 | 15.1 | 7.0 | 1.2 | 7.49 | 23.2% | 8.2% |
| CHALLENGER | 4,695 | 14.3 | 9.1 | 20.4 | 15.5 | 16.2 | 13.1 | 11.2 | 11.5 | 40.6% | 24.4% |
| ITF_MEN | 8,394 | 9.7 | 7.3 | 16.9 | 13.8 | 22.1 | 17.8 | 12.3 | 15.84 | 52.3% | 30.2% |
| ITF_WOMEN | 12,023 | 9.4 | 6.6 | 16.3 | 15.8 | 22.7 | 18.1 | 11.2 | 15.62 | 52.0% | 29.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 1,904 | 23.8 | 17.4 | 30.4 | 15.1 | 10.2 | 2.7 | 0.5 | 6.04 | 13.3% | 3.1% |
| WTA125 | 660 | 23.0 | 12.1 | 29.1 | 15.9 | 13.8 | 5.8 | 0.3 | 7.72 | 19.9% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,626 | 25.4 | 19.2 | 30.0 | 12.7 | 9.4 | 3.0 | 0.3 | 5.62 | 12.7% | 3.3% |
| CHALLENGER | 3,218 | 21.6 | 14.4 | 26.4 | 14.4 | 14.7 | 6.7 | 1.8 | 7.31 | 23.2% | 8.5% |
| DOUBLES | 1,651 | 5.3 | 4.7 | 11.8 | 10.4 | 21.0 | 26.0 | 20.8 | 23.73 | 67.9% | 46.9% |
| ITF_MEN | 6,195 | 13.8 | 9.1 | 20.0 | 16.1 | 21.2 | 13.3 | 6.5 | 12.14 | 41.0% | 19.8% |
| ITF_WOMEN | 7,122 | 12.6 | 9.0 | 19.2 | 15.2 | 21.6 | 16.3 | 6.1 | 12.87 | 44.0% | 22.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,088 | 22.7 | 15.8 | 30.0 | 17.7 | 9.8 | 3.6 | 0.4 | 6.83 | 13.8% | 4.0% |
| WTA125 | 732 | 21.6 | 14.1 | 22.0 | 18.2 | 14.3 | 7.8 | 2.0 | 8.12 | 24.2% | 9.8% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,597 | 28.5 | 14.4 | 25.4 | 15.4 | 11.7 | 4.2 | 0.5 | 6.01 | 16.4% | 4.7% |
| CHALLENGER | 3,303 | 20.7 | 12.4 | 25.1 | 17.8 | 15.3 | 6.8 | 1.9 | 8.34 | 24.0% | 8.7% |
| ITF_MEN | 6,138 | 12.2 | 8.8 | 20.3 | 16.6 | 22.7 | 14.3 | 5.1 | 12.53 | 42.1% | 19.4% |
| ITF_WOMEN | 8,971 | 11.1 | 8.2 | 18.2 | 17.4 | 24.2 | 15.3 | 5.5 | 13.52 | 45.1% | 20.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 1,849 | 17.8 | 12.8 | 26.1 | 19.4 | 17.5 | 5.7 | 0.7 | 8.25 | 23.9% | 6.4% |
| WTA125 | 634 | 13.7 | 7.3 | 23.0 | 20.8 | 20.5 | 13.1 | 1.6 | 11.31 | 35.2% | 14.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,597 | 24.3 | 15.4 | 24.9 | 17.6 | 13.0 | 4.2 | 0.6 | 6.48 | 17.8% | 4.8% |
| CHALLENGER | 3,303 | 19.0 | 11.2 | 22.9 | 17.4 | 17.8 | 9.5 | 2.1 | 9.14 | 29.4% | 11.7% |
| ITF_MEN | 6,139 | 9.8 | 7.1 | 16.8 | 15.0 | 21.6 | 19.2 | 10.5 | 15.48 | 51.3% | 29.7% |
| ITF_WOMEN | 8,972 | 9.2 | 6.5 | 15.2 | 14.7 | 22.6 | 20.5 | 11.3 | 16.67 | 54.4% | 31.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 1,849 | 14.1 | 10.2 | 22.2 | 16.3 | 22.6 | 13.2 | 1.4 | 10.93 | 37.2% | 14.6% |
| WTA125 | 634 | 6.6 | 4.9 | 17.0 | 17.8 | 26.0 | 19.7 | 7.9 | 16.74 | 53.6% | 27.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,576 | 25.6 | 19.5 | 30.1 | 12.9 | 9.0 | 2.8 | 0.2 | 5.54 | 12.0% | 3.0% |
| CHALLENGER | 2,805 | 23.0 | 15.5 | 27.8 | 14.4 | 14.1 | 4.5 | 0.5 | 6.72 | 19.1% | 5.1% |
| DOUBLES | 1,532 | 5.2 | 4.8 | 12.1 | 10.5 | 20.9 | 26.0 | 20.5 | 23.61 | 67.4% | 46.5% |
| ITF_MEN | 5,191 | 14.9 | 9.8 | 21.7 | 16.9 | 21.1 | 11.6 | 4.0 | 11.15 | 36.7% | 15.6% |
| ITF_WOMEN | 5,895 | 13.5 | 9.5 | 20.7 | 16.0 | 21.9 | 15.0 | 3.4 | 11.71 | 40.3% | 18.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,038 | 23.2 | 16.3 | 30.0 | 17.7 | 9.8 | 2.9 | 0.1 | 6.71 | 12.8% | 3.0% |
| WTA125 | 621 | 23.7 | 15.6 | 23.5 | 19.6 | 12.6 | 4.7 | 0.3 | 6.95 | 17.5% | 5.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 1,651 | 5.3 | 4.7 | 11.8 | 10.4 | 21.0 | 26.0 | 20.8 | 23.73 | 67.9% | 46.9% |
| singles | 20,130 | 16.3 | 11.3 | 22.3 | 15.4 | 18.4 | 11.7 | 4.6 | 10.02 | 34.7% | 16.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 5 | 20.0 | 40.0 | 20.0 | 0.0 | 20.0 | 0.0 | 0.0 | 4.01 | 20.0% | 0.0% |
| Clay | 6,691 | 13.0 | 9.0 | 19.2 | 15.6 | 18.7 | 14.5 | 10.0 | 12.83 | 43.2% | 24.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 18,809 | 13.3 | 8.5 | 18.6 | 15.2 | 19.8 | 14.9 | 9.8 | 13.1 | 44.5% | 24.7% |
| UNKNOWN | 4,612 | 10.7 | 7.5 | 17.0 | 16.8 | 20.6 | 16.3 | 11.1 | 14.16 | 48.0% | 27.4% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,620 | 19.5 | 11.9 | 21.4 | 16.5 | 15.0 | 9.3 | 6.4 | 9.16 | 30.7% | 15.7% |
| B | 3,766 | 12.4 | 8.7 | 19.6 | 16.1 | 19.3 | 12.7 | 11.2 | 12.66 | 43.2% | 23.9% |
| C | 4,247 | 11.4 | 8.7 | 19.8 | 15.2 | 19.5 | 14.7 | 10.8 | 13.23 | 45.0% | 25.5% |
| D | 4,713 | 12.1 | 7.7 | 17.4 | 15.4 | 21.4 | 15.8 | 10.2 | 14.0 | 47.4% | 26.0% |
| F | 9,008 | 7.6 | 5.5 | 15.1 | 14.5 | 23.5 | 21.2 | 12.6 | 17.82 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 6,201 | 23.2 | 15.8 | 28.8 | 15.1 | 11.6 | 4.0 | 1.4 | 6.64 | 17.1% | 5.5% |
| B | 2,965 | 16.2 | 10.3 | 23.1 | 16.2 | 19.5 | 10.7 | 3.9 | 10.06 | 34.1% | 14.6% |
| C | 4,273 | 11.2 | 7.4 | 18.2 | 14.3 | 21.5 | 16.8 | 10.6 | 14.42 | 48.9% | 27.4% |
| D | 3,021 | 14.3 | 9.8 | 19.9 | 14.5 | 21.0 | 14.5 | 6.1 | 12.06 | 41.6% | 20.6% |
| F | 5,321 | 10.3 | 8.5 | 15.7 | 15.0 | 22.6 | 19.9 | 8.1 | 15.27 | 50.6% | 28.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 9,895 | 17.8 | 10.6 | 20.7 | 16.2 | 15.6 | 10.2 | 8.9 | 10.25 | 34.7% | 19.1% |
| LIMITED | 6,400 | 13.2 | 10.0 | 20.3 | 15.7 | 19.4 | 13.5 | 7.9 | 12.0 | 40.7% | 21.4% |
| POOR | 14,059 | 9.1 | 6.3 | 16.0 | 14.9 | 22.7 | 19.2 | 11.8 | 16.27 | 53.7% | 31.0% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 6,132 | 25.6 | 19.6 | 33.8 | 12.8 | 5.6 | 2.2 | 0.3 | 5.48 | 8.1% | 2.5% |
| GAME_SPREAD | 4,835 | 22.2 | 15.2 | 33.4 | 17.2 | 9.2 | 2.4 | 0.3 | 6.74 | 11.9% | 2.7% |
| MATCH_WINNER | 21,781 | 15.5 | 10.8 | 21.5 | 15.0 | 18.6 | 12.8 | 5.8 | 10.55 | 37.2% | 18.6% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 10,851 | 28.8 | 17.1 | 30.9 | 12.5 | 8.2 | 2.2 | 0.4 | 5.52 | 10.7% | 2.5% |
| TOTAL_GAMES | 7,656 | 9.1 | 9.8 | 36.5 | 28.4 | 10.3 | 3.2 | 2.7 | 9.39 | 16.2% | 5.9% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,461 | 25.2 | 32.9 | 32.6 | 5.0 | 3.3 | 0.8 | 0.2 | 4.51 | 4.4% | 1.0% |
| GAME_SPREAD | 6,318 | 45.6 | 16.7 | 26.8 | 7.9 | 1.7 | 0.9 | 0.3 | 3.47 | 3.0% | 1.2% |
| TOTAL_GAMES | 10,801 | 5.1 | 7.9 | 41.3 | 34.1 | 6.9 | 2.5 | 2.2 | 9.53 | 11.6% | 4.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,472 | 24.1 | 17.4 | 35.4 | 12.8 | 7.2 | 2.6 | 0.4 | 5.9 | 10.3% | 3.0% |
| GAME_SPREAD | 6,321 | 19.6 | 13.4 | 27.8 | 20.8 | 13.2 | 4.3 | 0.9 | 7.96 | 18.5% | 5.2% |
| TOTAL_GAMES | 10,822 | 8.7 | 9.7 | 36.7 | 26.9 | 12.0 | 3.6 | 2.3 | 9.41 | 18.0% | 6.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 30,354 | 44.8% | 25.1% | 13.21 | 36.3% | 15.7% | 10.96 |
| gen1_elo | 30,354 | 44.6% | 24.8% | 13.02 | 36.0% | 15.7% | 10.77 |
| gen1_sr | 30,354 | 52.6% | 31.8% | 16.07 | 44.8% | 22.4% | 13.17 |
| gen2 | 30,354 | 51.6% | 32.2% | 15.66 | 44.7% | 24.0% | 13.11 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 15,321 | 15.7 | 10.3 | 21.3 | 17.2 | 20.2 | 12.0 | 3.3 | 10.73 | 35.4% | 15.3% |
| STALE | 15,033 | 9.9 | 6.6 | 15.5 | 13.7 | 19.2 | 18.2 | 16.9 | 17.06 | 54.3% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 15,249 | 16.5 | 11.3 | 22.2 | 15.1 | 17.9 | 12.2 | 4.8 | 9.99 | 34.8% | 17.0% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 52,135 | 15249 | 18793 | 18093 | 24.2 | 151.1 | 1400.4 |
| ge_15pp | 21,694 | 5310 | 6717 | 9667 | 26.7 | 445.1 | 1380.4 |
| ge_25pp | 11,661 | 2588 | 2931 | 6142 | 32.9 | 589.9 | 1380.4 |
| lt_10pp | 22,465 | 7633 | 8885 | 5947 | 22.4 | 47.9 | 1341.5 |

Current slate `SL-20261024T213734Z-a42f4c8a`: 628 priced rows, quote age at build {'median': 14.8, 'max': 14.8}, freshness {'AGING': 628}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 24 | 0.0 | 0.0 | 25.0 | 4.2 | 37.5 | 33.3 | 0.0 | 20.48 | 70.8% | 33.3% |
| EXTERNAL_LONE_OUTLIER | 16 | 75.0 | 25.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 2,887 | 19.3 | 11.2 | 24.9 | 18.8 | 18.0 | 7.2 | 0.7 | 8.83 | 25.8% | 7.8% |
| KALSHI_LONE_OUTLIER | 18 | 5.6 | 5.6 | 72.2 | 5.6 | 5.6 | 5.6 | 0.0 | 6.16 | 11.1% | 5.6% |
| MARKETS_AGREE | 588 | 65.0 | 35.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.26 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,248 | 0.0 | 2.3 | 35.9 | 25.7 | 24.7 | 10.7 | 0.7 | 12.08 | 36.1% | 11.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 30,354 | 4781 (15.8%) | 26.1% | 0.9% | {"EXTERNAL_STALE": 2887, "AGREES_WITH_KALSHI": 1248, "ALL_AGREE": 588, "SUPPORTS_MODEL_DIRECTION": 23, "AGREES_WITH_MODEL": 18, "EXTERNAL_OUTLIER": 16, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 13,585 | 1215 (8.9%) | 37.0% | 1.6% | {"EXTERNAL_STALE": 746, "AGREES_WITH_KALSHI": 450, "SUPPORTS_MODEL_DIRECTION": 17, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 7,611 | 377 (5.0%) | 37.7% | 2.4% | {"EXTERNAL_STALE": 226, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 3,685 | 354 (9.6%) | 38.1% | 2.5% | {"EXTERNAL_STALE": 210, "AGREES_WITH_KALSHI": 135, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 12,063 | 2700 (22.4%) | 17.7% | 0.7% | {"EXTERNAL_STALE": 1598, "ALL_AGREE": 588, "AGREES_WITH_KALSHI": 477, "EXTERNAL_OUTLIER": 16, "AGREES_WITH_MODEL": 15, "SUPPORTS_MODEL_DIRECTION": 5, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 5,790 | 10.2 | 7.5 | 19.5 | 14.3 | 22.2 | 16.1 | 10.1 | 14.26 | 48.5% | 26.3% |
| 4-10x | 3,959 | 10.9 | 8.2 | 19.1 | 15.3 | 21.4 | 14.9 | 10.2 | 13.77 | 46.5% | 25.1% |
| <2x | 15,386 | 14.9 | 9.7 | 19.0 | 16.4 | 17.5 | 13.1 | 9.3 | 11.88 | 40.0% | 22.4% |
| >=10x | 5,219 | 10.8 | 6.2 | 15.3 | 14.2 | 21.8 | 19.6 | 12.1 | 16.42 | 53.5% | 31.6% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 7,759 | 12.4 | 8.5 | 19.4 | 15.9 | 19.1 | 13.8 | 10.9 | 12.99 | 43.8% | 24.7% |
| 300-1000 | 6,460 | 11.6 | 8.5 | 17.3 | 15.3 | 20.5 | 16.4 | 10.3 | 13.97 | 47.2% | 26.7% |
| <300 | 9,928 | 8.6 | 5.6 | 15.5 | 14.7 | 23.1 | 20.1 | 12.4 | 17.02 | 55.6% | 32.5% |
| >=3000 | 6,207 | 21.3 | 12.9 | 23.2 | 16.5 | 14.1 | 7.1 | 4.8 | 7.97 | 26.1% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 863 | 0.55 | 0.4116 | 0.4994 | +0.051 | -0.088 | -0.0035 ± 0.0052 |
| ratio 4-10x | 593 | 0.5889 | 0.4423 | 0.4958 | +0.093 | -0.053 | 0.0115 ± 0.0066 |
| ratio <2x | 2145 | 0.5382 | 0.4154 | 0.4457 | +0.092 | -0.030 | 0.0127 ± 0.0031 |
| ratio >=10x | 791 | 0.572 | 0.3967 | 0.4627 | +0.109 | -0.066 | 0.0077 ± 0.0065 |
| thinner_sample 1000-3000 | 1189 | 0.5426 | 0.4159 | 0.4449 | +0.098 | -0.029 | 0.0108 ± 0.0041 |
| thinner_sample 300-1000 | 997 | 0.5674 | 0.4235 | 0.4925 | +0.075 | -0.069 | 0.0008 ± 0.0051 |
| thinner_sample <300 | 1474 | 0.5615 | 0.3949 | 0.464 | +0.097 | -0.069 | 0.0097 ± 0.0046 |
| thinner_sample >=3000 | 732 | 0.5361 | 0.4418 | 0.4686 | +0.068 | -0.027 | 0.0126 ± 0.0043 |
| data_status ADEQUATE | 1279 | 0.5386 | 0.4344 | 0.4519 | +0.087 | -0.018 | 0.012 ± 0.0035 |
| data_status LIMITED | 1002 | 0.5514 | 0.4172 | 0.481 | +0.070 | -0.064 | 0.0043 ± 0.0047 |
| data_status POOR | 2111 | 0.5635 | 0.402 | 0.4676 | +0.096 | -0.066 | 0.0083 ± 0.0038 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 641 | 0.2024 | 0.2033 | -0.0009 ± 0.0006 | 0.5859 | 0.5879 | 0.5031 | 0.4883 | 0.5242 | -0.071 ± 0.0188 | -0.01 (5) |
| 3-5 | 408 | 0.2043 | 0.2039 | +0.0004 ± 0.0018 | 0.5921 | 0.5895 | 0.5026 | 0.4625 | 0.4755 | -0.099 ± 0.023 | 0.02 (1) |
| 5-10 | 909 | 0.2034 | 0.2028 | +0.0005 ± 0.0023 | 0.5936 | 0.5891 | 0.5117 | 0.4377 | 0.4664 | -0.091 ± 0.0155 | -0.0167 (6) |
| 10-15 | 759 | 0.215 | 0.205 | +0.0100 ± 0.0041 | 0.6206 | 0.5918 | 0.5304 | 0.4062 | 0.4269 | -0.106 ± 0.0164 | -0.048 (5) |
| 15-25 | 994 | 0.2247 | 0.2121 | +0.0126 ± 0.0057 | 0.644 | 0.6077 | 0.5787 | 0.3831 | 0.4487 | -0.095 ± 0.0145 | -0.0033 (9) |
| 25-40 | 567 | 0.2232 | 0.2095 | +0.0137 ± 0.0115 | 0.6363 | 0.6023 | 0.6596 | 0.3495 | 0.4797 | -0.075 ± 0.0176 | -0.01 (1) |
| 40+ | 114 | 0.2782 | 0.1979 | +0.0803 ± 0.0361 | 0.7617 | 0.5807 | 0.7579 | 0.3106 | 0.4474 | -0.079 ± 0.0353 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3314 | 0.1857 | 0.1867 | -0.0010 ± 0.0003 | 0.5472 | 0.5483 | 0.4932 | 0.4781 | 0.5118 | -0.021 ± 0.0076 | -0.0129 (17) |
| 3-5 | 2194 | 0.1995 | 0.1983 | +0.0012 ± 0.0008 | 0.58 | 0.5747 | 0.4858 | 0.4458 | 0.4499 | -0.052 ± 0.0097 | 0.0 (2) |
| 5-10 | 4759 | 0.1985 | 0.1952 | +0.0033 ± 0.001 | 0.581 | 0.5698 | 0.4824 | 0.4086 | 0.4224 | -0.047 ± 0.0065 | -0.0119 (21) |
| 10-15 | 4029 | 0.198 | 0.1799 | +0.0181 ± 0.0017 | 0.5816 | 0.5308 | 0.4872 | 0.3627 | 0.3517 | -0.074 ± 0.0067 | -0.0281 (16) |
| 15-25 | 5056 | 0.2091 | 0.1695 | +0.0395 ± 0.0023 | 0.6119 | 0.5016 | 0.5064 | 0.31 | 0.3085 | -0.075 ± 0.0057 | -0.0025 (44) |
| 25-40 | 3982 | 0.2227 | 0.1284 | +0.0942 ± 0.0036 | 0.6395 | 0.3936 | 0.5316 | 0.2182 | 0.2283 | -0.060 ± 0.0055 | -0.01 (1) |
| 40+ | 2600 | 0.3803 | 0.0453 | +0.3350 ± 0.0047 | 0.9907 | 0.1741 | 0.633 | 0.1065 | 0.0642 | -0.077 ± 0.0039 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 503 | 0.2077 | 0.2085 | -0.0009 ± 0.0007 | 0.5976 | 0.5995 | 0.5073 | 0.4921 | 0.5189 | -0.100 ± 0.0219 | -0.01 (3) |
| 3-5 | 365 | 0.2256 | 0.223 | +0.0027 ± 0.002 | 0.6379 | 0.6324 | 0.516 | 0.4761 | 0.4575 | -0.128 ± 0.0264 | 0.02 (1) |
| 5-10 | 793 | 0.2064 | 0.2065 | -0.0001 ± 0.0024 | 0.5993 | 0.5986 | 0.5467 | 0.4718 | 0.5132 | -0.078 ± 0.0166 | -0.01 (4) |
| 10-15 | 725 | 0.218 | 0.2099 | +0.0081 ± 0.0043 | 0.6257 | 0.6057 | 0.5658 | 0.4415 | 0.4731 | -0.113 ± 0.0177 | -0.04 (5) |
| 15-25 | 1017 | 0.2302 | 0.2103 | +0.0199 ± 0.0057 | 0.6534 | 0.6033 | 0.5879 | 0.3922 | 0.4435 | -0.102 ± 0.0147 | -0.0133 (9) |
| 25-40 | 715 | 0.2625 | 0.1975 | +0.0649 ± 0.0105 | 0.7319 | 0.5754 | 0.6535 | 0.3379 | 0.3944 | -0.115 ± 0.0163 | -0.0075 (4) |
| 40+ | 274 | 0.3572 | 0.1714 | +0.1858 ± 0.0247 | 0.9817 | 0.513 | 0.733 | 0.2492 | 0.3139 | -0.072 ± 0.0239 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 2822 | 0.1948 | 0.1951 | -0.0003 ± 0.0003 | 0.5665 | 0.567 | 0.5113 | 0.4963 | 0.5113 | -0.043 ± 0.0086 | -0.0133 (15) |
| 3-5 | 1891 | 0.2003 | 0.1994 | +0.0009 ± 0.0008 | 0.5788 | 0.5763 | 0.5153 | 0.4754 | 0.4833 | -0.046 ± 0.0105 | 0.02 (1) |
| 5-10 | 4199 | 0.1964 | 0.1945 | +0.0019 ± 0.001 | 0.5778 | 0.5685 | 0.5101 | 0.4361 | 0.4627 | -0.034 ± 0.0069 | -0.0117 (6) |
| 10-15 | 3654 | 0.2022 | 0.1899 | +0.0123 ± 0.0018 | 0.5913 | 0.5532 | 0.5135 | 0.3895 | 0.4028 | -0.056 ± 0.0073 | -0.0189 (18) |
| 15-25 | 5021 | 0.2163 | 0.178 | +0.0382 ± 0.0024 | 0.6281 | 0.5238 | 0.5252 | 0.3292 | 0.3336 | -0.069 ± 0.006 | -0.0086 (42) |
| 25-40 | 4644 | 0.2513 | 0.1366 | +0.1147 ± 0.0035 | 0.707 | 0.4198 | 0.5575 | 0.2403 | 0.2207 | -0.085 ± 0.0054 | -0.0044 (18) |
| 40+ | 3703 | 0.3938 | 0.0604 | +0.3334 ± 0.0046 | 1.0364 | 0.216 | 0.6505 | 0.1186 | 0.084 | -0.072 ± 0.0039 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 614 | 0.2001 | 0.2021 | -0.0021 ± 0.0006 | 0.5809 | 0.5861 | 0.5015 | 0.4862 | 0.5456 | -0.036 ± 0.0189 | -0.0137 (8) |
| 3-5 | 436 | 0.2035 | 0.202 | +0.0016 ± 0.0017 | 0.5905 | 0.5852 | 0.506 | 0.4663 | 0.4679 | -0.116 ± 0.0224 | 0.0067 (3) |
| 5-10 | 926 | 0.2025 | 0.199 | +0.0035 ± 0.0022 | 0.5917 | 0.5796 | 0.5079 | 0.4339 | 0.4449 | -0.105 ± 0.015 | -0.0071 (7) |
| 10-15 | 762 | 0.2094 | 0.2058 | +0.0036 ± 0.0041 | 0.6079 | 0.594 | 0.5402 | 0.4166 | 0.4659 | -0.084 ± 0.0163 | -0.0317 (6) |
| 15-25 | 943 | 0.2307 | 0.2121 | +0.0186 ± 0.0058 | 0.6592 | 0.6072 | 0.5898 | 0.3953 | 0.4443 | -0.110 ± 0.0149 | -0.03 (1) |
| 25-40 | 591 | 0.2138 | 0.2175 | -0.0037 ± 0.0112 | 0.6172 | 0.6208 | 0.6704 | 0.3592 | 0.5178 | -0.055 ± 0.0173 | 0.015 (2) |
| 40+ | 120 | 0.2938 | 0.2096 | +0.0842 ± 0.0365 | 0.8102 | 0.6066 | 0.7684 | 0.3189 | 0.4583 | -0.076 ± 0.0382 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3244 | 0.1855 | 0.186 | -0.0005 ± 0.0003 | 0.5456 | 0.5464 | 0.4896 | 0.4744 | 0.4886 | -0.038 ± 0.0076 | -0.0163 (35) |
| 3-5 | 2197 | 0.1952 | 0.1932 | +0.0020 ± 0.0008 | 0.5729 | 0.5664 | 0.4871 | 0.4474 | 0.4429 | -0.064 ± 0.0096 | -0.0094 (18) |
| 5-10 | 4811 | 0.196 | 0.1902 | +0.0058 ± 0.0009 | 0.5759 | 0.557 | 0.4834 | 0.4095 | 0.4078 | -0.061 ± 0.0063 | -0.01 (31) |
| 10-15 | 3922 | 0.1923 | 0.177 | +0.0152 ± 0.0017 | 0.5683 | 0.5228 | 0.4999 | 0.3765 | 0.3761 | -0.064 ± 0.0067 | -0.015 (12) |
| 15-25 | 5242 | 0.2112 | 0.1722 | +0.0390 ± 0.0022 | 0.6168 | 0.5078 | 0.5157 | 0.3207 | 0.3186 | -0.073 ± 0.0057 | -0.03 (2) |
| 25-40 | 3998 | 0.2195 | 0.1325 | +0.0869 ± 0.0036 | 0.6332 | 0.4024 | 0.5377 | 0.2214 | 0.2439 | -0.050 ± 0.0055 | 0.01 (3) |
| 40+ | 2520 | 0.3951 | 0.0498 | +0.3453 ± 0.0051 | 1.0325 | 0.1861 | 0.6452 | 0.1129 | 0.0687 | -0.081 ± 0.0042 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1002 | 0.1953 | 0.1955 | -0.0002 ± 0.0005 | 0.5699 | 0.57 | 0.5031 | 0.488 | 0.496 | -0.057 ± 0.0141 | -0.0224 (49) |
| 3-5 | 698 | 0.193 | 0.1922 | +0.0007 ± 0.0013 | 0.5636 | 0.5605 | 0.4906 | 0.4508 | 0.4585 | -0.060 ± 0.017 | -0.0194 (34) |
| 5-10 | 1450 | 0.2024 | 0.1963 | +0.0061 ± 0.0018 | 0.5942 | 0.5752 | 0.4966 | 0.4233 | 0.4193 | -0.074 ± 0.0118 | -0.005 (78) |
| 10-15 | 969 | 0.2109 | 0.1987 | +0.0122 ± 0.0036 | 0.6113 | 0.5796 | 0.523 | 0.3999 | 0.4097 | -0.072 ± 0.0147 | 0.0014 (64) |
| 15-25 | 1298 | 0.2316 | 0.2103 | +0.0213 ± 0.005 | 0.6615 | 0.6052 | 0.5784 | 0.3836 | 0.4276 | -0.074 ± 0.0127 | -0.0214 (59) |
| 25-40 | 787 | 0.2479 | 0.2074 | +0.0405 ± 0.01 | 0.7042 | 0.5961 | 0.6738 | 0.3611 | 0.4524 | -0.087 ± 0.0152 | -0.0219 (26) |
| 40+ | 260 | 0.3514 | 0.1975 | +0.1539 ± 0.0272 | 1.0146 | 0.5768 | 0.8089 | 0.3265 | 0.4269 | -0.095 ± 0.0248 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3276 | 0.1833 | 0.1836 | -0.0002 ± 0.0003 | 0.5399 | 0.5396 | 0.505 | 0.4896 | 0.5006 | -0.038 ± 0.0075 | -0.0157 (88) |
| 3-5 | 2276 | 0.1955 | 0.1936 | +0.0019 ± 0.0007 | 0.5701 | 0.5658 | 0.4969 | 0.4571 | 0.453 | -0.055 ± 0.0094 | -0.0209 (69) |
| 5-10 | 4513 | 0.1975 | 0.1891 | +0.0084 ± 0.001 | 0.5808 | 0.5561 | 0.4914 | 0.4178 | 0.4004 | -0.072 ± 0.0065 | -0.0082 (132) |
| 10-15 | 3171 | 0.2073 | 0.1908 | +0.0164 ± 0.0019 | 0.6033 | 0.5602 | 0.5298 | 0.4067 | 0.4008 | -0.068 ± 0.0078 | -0.0053 (105) |
| 15-25 | 3937 | 0.2302 | 0.1996 | +0.0305 ± 0.0028 | 0.6638 | 0.5785 | 0.5701 | 0.3746 | 0.3955 | -0.067 ± 0.0071 | -0.0253 (107) |
| 25-40 | 2717 | 0.2588 | 0.1843 | +0.0745 ± 0.0052 | 0.7334 | 0.5377 | 0.6329 | 0.3189 | 0.3596 | -0.077 ± 0.008 | -0.0229 (51) |
| 40+ | 1200 | 0.378 | 0.1445 | +0.2334 ± 0.0115 | 1.0706 | 0.4354 | 0.73 | 0.2264 | 0.2592 | -0.071 ± 0.0103 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 4392 | 1.03 ± 0.042 | 1.12 | 0.1686 | 0.1635 | 0.2147 | 0.2062 |
| gen2 | 4392 | 0.835 ± 0.039 | 1.088 | 0.1681 | 0.1642 | 0.2341 | 0.2059 |
| gen1_elo | 4392 | 1.003 ± 0.041 | 1.114 | 0.1755 | 0.1636 | 0.2135 | 0.2065 |
| gen1_sr | 4392 | 1.017 ± 0.051 | 1.161 | 0.1293 | 0.1661 | 0.2302 | 0.2055 |
| gen1_ledger | 6464 | 0.859 ± 0.03 | 1.069 | 0.1836 | 0.178 | 0.2189 | 0.2003 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 21,694)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,031 | 23.2% |
| STALE_QUOTE | market_freshness | 4,723 | 21.8% |
| BOOK_QUALITY | execution | 4,045 | 18.6% |
| POOR_DATA | data | 2,431 | 11.2% |
| LIMITED_DATA | data | 1,332 | 6.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,183 | 5.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,023 | 4.7% |
| IDENTITY_AMBIGUOUS | mapping | 911 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 648 | 3.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 366 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 23.2%, market_freshness 21.8%, execution 18.6%, data 17.3%, market_freshness/coverage 8.4%, model_calibration_or_unknown 4.7%, mapping 4.2%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.1%, LOW_DATA_QUALITY 70.8%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 49.3%, STALE_KALSHI_QUOTE 44.6%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 24.8%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 16.4%, LEVEL_TRANSFER_RISK 11.0%, EVENT_MAPPING_RISK 8.0%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.9%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.8%, POST_SETTLEMENT_OBSERVATION 23.2%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 11,661)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,060 | 34.8% |
| STALE_QUOTE | market_freshness | 2,190 | 18.8% |
| BOOK_QUALITY | execution | 2,100 | 18.0% |
| POOR_DATA | data | 1,006 | 8.6% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 635 | 5.5% |
| IDENTITY_AMBIGUOUS | mapping | 515 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 413 | 3.5% |
| LIMITED_DATA | data | 404 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 256 | 2.2% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 81 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.8%, market_freshness 18.8%, execution 18.0%, data 12.1%, market_freshness/coverage 9.0%, mapping 4.4%, model_calibration_or_unknown 2.2%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 74.1%, THIN_PLAYER_HISTORY 61.8%, STALE_KALSHI_QUOTE 52.7%, STALE_PLAYER_DATA 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.8%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 23.8%, PLAYER_IDENTITY_RISK 19.7%, MODEL_HIGH_UNCERTAINTY 18.4%, LEVEL_TRANSFER_RISK 9.7%, EVENT_MAPPING_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.9%, POST_SETTLEMENT_OBSERVATION 34.8%, POSSIBLE_IN_PLAY_QUOTE 5.8%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 9075, "IDENTITY_AMBIGUOUS": 2586}; ticker orientation: {"VERIFIED": 11661}.

Checks: discipline:AMBIGUOUS 774, discipline:PASS 10887, identity_confidence:AMBIGUOUS 2296, identity_confidence:PASS 9365, level_mapping:NA 786, level_mapping:PASS 10875, market_pair:AMBIGUOUS 407, market_pair:NA 295, market_pair:PASS 10959, model_complement:NA 262, model_complement:PASS 11399, namesake:AMBIGUOUS 6, namesake:PASS 11655, physical_match_id:NA 4050, physical_match_id:PASS 7611, player_ids:PASS 11661, same_pair_other_event:PASS 11661, ticker_orientation:PASS 11661

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,298 | 4.6% | 4.0% | 1.7% | {"market_freshness": 53, "model_calibration_or_unknown": 44, "data": 35, "execution": 23, "market_freshness/coverage": 15, "model_calibration": 13, "coverage": 13} | 5.9 | 0.2224 / 0.2181 (519) | 18.9% | 3.6% | 3.3% | 2.9% |
| CHALLENGER | 7,913 | 17.5% | 7.0% | 11.9% | {"coverage": 786, "market_freshness/coverage": 168, "market_freshness": 151, "data": 139, "model_calibration_or_unknown": 64, "execution": 31, "model_calibration": 28, "mapping": 15, "possible_market_error": 1} | 7.46 | 0.2202 / 0.2089 (1892) | 35.0% | 17.7% | 3.9% | 22.8% |
| DOUBLES | 1,651 | 46.9% | 46.5% | 6.6% | {"execution": 406, "mapping": 200, "market_freshness": 106, "market_freshness/coverage": 55, "coverage": 7} | 23.61 | 0.3096 / 0.2358 (432) | 14.2% | 0.0% | 100.0% | 7.2% |
| ITF_MEN | 14,589 | 25.5% | 17.7% | 31.9% | {"coverage": 1394, "execution": 704, "market_freshness": 633, "data": 487, "market_freshness/coverage": 322, "mapping": 173, "model_calibration_or_unknown": 2, "model_calibration": 2} | 11.89 | 0.2156 / 0.1974 (3276) | 37.6% | 69.9% | 19.9% | 22.4% |
| ITF_WOMEN | 19,145 | 27.3% | 19.9% | 44.9% | {"coverage": 1835, "market_freshness": 1148, "execution": 896, "data": 715, "market_freshness/coverage": 439, "mapping": 121, "model_calibration_or_unknown": 69, "model_calibration": 11} | 12.88 | 0.2038 / 0.1946 (3712) | 40.1% | 55.9% | 9.9% | 22.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 2,992 | 5.7% | 5.2% | 1.5% | {"market_freshness": 59, "model_calibration_or_unknown": 36, "execution": 26, "model_calibration": 16, "coverage": 12, "data": 11, "market_freshness/coverage": 10, "mapping": 1} | 7.65 | 0.2353 / 0.2301 (495) | 25.0% | 1.4% | 1.7% | 3.5% |
| WTA125 | 1,392 | 12.5% | 9.9% | 1.5% | {"model_calibration_or_unknown": 39, "market_freshness": 38, "market_freshness/coverage": 38, "data": 23, "coverage": 12, "model_calibration": 11, "execution": 9, "mapping": 4} | 9.09 | 0.219 / 0.2065 (488) | 22.8% | 7.3% | 5.2% | 9.8% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 3 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 4 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 5 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 6 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 7 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 8 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 9 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 10 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 13 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 14 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 15 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 16 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 17 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 18 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 19 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 20 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 21 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 22 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 23 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 24 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 25 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 26 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 27 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 28 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 29 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 30 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 31 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 32 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 33 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 34 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 35 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 36 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 37 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 38 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 752 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 12.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 768 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 41 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 42 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 43 | `KXITFMATCH-26OCT20TAGVAN-TAG` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 151.0, ratio 2.71); no external reference |
| 44 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 45 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 46 | `KXITFMATCH-26OCT16BLAJUH-BLA` | ITF_MEN | fair_v1 | 79% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 468 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 3140.69); no external reference |
| 47 | `KXITFMATCH-26OCT21TORPON-PON` | ITF_MEN | gen1_ledger | 84% / 8% | +77 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 91.53); no external reference |
| 48 | `KXITFWMATCH-26OCT07GIZPIG-PIG` | ITF_WOMEN | gen1_ledger | 91% / 14% | +77 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 52 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 6.39); no external reference |
| 49 | `KXITFMATCH-26OCT05CHIHAO-HAO` | ITF_MEN | fair_v1 | 78% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 874 min (STALE); data POOR (grade F, thinner serve sample 54.0, ratio 7.45); no external reference |
| 50 | `KXITFWMATCH-26OCT06ABADUN-ABA` | ITF_WOMEN | fair_v1 | 89% / 12% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 134 min (STALE); data POOR (grade F, thinner serve sample 200.0, ratio 4.51); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9685, "by_level_share_of_ge_25pp": {"ATP": 0.0168, "CHALLENGER": 0.1186, "DOUBLES": 0.0664, "ITF_MEN": 0.3188, "ITF_WOMEN": 0.4488, "OTHER": 0.001, "WTA": 0.0147, "WTA125": 0.0149}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5267, "share_primary_cause_market_settled_or_in_play": 0.4381, "share_primary_cause_stale_quote_only": 0.1878}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 11661, "identity_ambiguous_share": 0.2218, "ticker_orientation": {"VERIFIED": 11661}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 7611, "with_external": 377, "coverage": 0.0495, "external_status": {"EXTERNAL_STALE": 226, "AGREES_WITH_KALSHI": 142, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 226, "MODEL_LONE_OUTLIER": 142, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3767, "share_external_supports_model": 0.0239}, "pregame_clean_ge_25pp": {"n": 3685, "with_external": 354, "coverage": 0.0961, "external_status": {"EXTERNAL_STALE": 210, "AGREES_WITH_KALSHI": 135, "SUPPORTS_MODEL_DIRECTION": 8, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 210, "MODEL_LONE_OUTLIER": 135, "ALL_THREE_DISAGREE": 8, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3814, "share_external_supports_model": 0.0254}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 498.0, "median_sample_ratio": 2.43, "median_min_matches": 21.0, "median_max_days_since_last": 225.0, "share_severe_asymmetry": 0.2147, "data_status": {"POOR": 6481, "LIMITED": 3039, "ADEQUATE": 2141}, "comparison_lt_10pp": {"median_thinner_serve_points": 1712.5, "median_sample_ratio": 1.7, "median_min_matches": 95.5}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 863, "model_minus_observed": 0.0506, "kalshi_minus_observed": -0.0879, "brier_diff_model_minus_kalshi": -0.0035}, "4-10x": {"n": 593, "model_minus_observed": 0.0931, "kalshi_minus_observed": -0.0534, "brier_diff_model_minus_kalshi": 0.0115}, "<2x": {"n": 2145, "model_minus_observed": 0.0925, "kalshi_minus_observed": -0.0303, "brier_diff_model_minus_kalshi": 0.0127}, ">=10x": {"n": 791, "model_minus_observed": 0.1093, "kalshi_minus_observed": -0.066, "brier_diff_model_minus_kalshi": 0.0077}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 4392, "model": {"intercept": -0.537, "slope": 0.835, "slope_se": 0.039}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.088, "slope_se": 0.044}, "mean_extremity_model": 0.1681, "mean_extremity_kalshi": 0.1642, "model_brier": 0.2341, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0282, "brier_diff_se": 0.0029, "model_logloss": 0.6646, "kalshi_logloss": 0.5947}, "fair_v1": {"n": 4392, "model": {"intercept": -0.421, "slope": 1.03, "slope_se": 0.042}, "kalshi_mid_same_rows": {"intercept": 0.286, "slope": 1.12, "slope_se": 0.044}, "mean_extremity_model": 0.1686, "mean_extremity_kalshi": 0.1635, "model_brier": 0.2147, "kalshi_brier": 0.2062, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0023, "model_logloss": 0.6183, "kalshi_logloss": 0.5951}, "gen1_elo": {"n": 4392, "model": {"intercept": -0.398, "slope": 1.003, "slope_se": 0.041}, "kalshi_mid_same_rows": {"intercept": 0.305, "slope": 1.114, "slope_se": 0.044}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1636, "model_brier": 0.2135, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.0024, "model_logloss": 0.6168, "kalshi_logloss": 0.5958}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2507, "share_ge_15": 0.4476, "median_abs_gap": 13.21, "n": 30354}, "gen1_elo": {"share_ge_25": 0.2476, "share_ge_15": 0.4465, "median_abs_gap": 13.02, "n": 30354}, "gen1_sr": {"share_ge_25": 0.3184, "share_ge_15": 0.5264, "median_abs_gap": 16.07, "n": 30354}, "gen2": {"share_ge_25": 0.3216, "share_ge_15": 0.5157, "median_abs_gap": 15.66, "n": 30354}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1568, "share_ge_15": 0.3627, "median_abs_gap": 10.96, "n": 23498}, "gen1_elo": {"share_ge_25": 0.1572, "share_ge_15": 0.3603, "median_abs_gap": 10.77, "n": 23495}, "gen1_sr": {"share_ge_25": 0.2236, "share_ge_15": 0.4477, "median_abs_gap": 13.17, "n": 23499}, "gen2": {"share_ge_25": 0.2397, "share_ge_15": 0.4466, "median_abs_gap": 13.11, "n": 23500}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.9, "share_ge_25_all": 0.0456, "share_ge_25_pregame_clean": 0.0403}, "WTA": {"median_abs_gap_pregame_clean": 7.65, "share_ge_25_all": 0.0572, "share_ge_25_pregame_clean": 0.0516}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2337, "share_within_10pp_all": 0.4309, "share_within_10pp_pregame_clean": 0.4845, "corr_model_vs_mid_pregame_clean": 0.8429}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 641, "model_brier": 0.2024, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": -0.0009}, "10-15": {"n_settled": 759, "model_brier": 0.215, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.01}, "15-25": {"n_settled": 994, "model_brier": 0.2247, "kalshi_brier": 0.2121, "brier_diff_model_minus_kalshi": 0.0126}, "25-40": {"n_settled": 567, "model_brier": 0.2232, "kalshi_brier": 0.2095, "brier_diff_model_minus_kalshi": 0.0137}, "3-5": {"n_settled": 408, "model_brier": 0.2043, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 114, "model_brier": 0.2782, "kalshi_brier": 0.1979, "brier_diff_model_minus_kalshi": 0.0803}, "5-10": {"n_settled": 909, "model_brier": 0.2034, "kalshi_brier": 0.2028, "brier_diff_model_minus_kalshi": 0.0005}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.537, "slope": 0.835, "slope_se": 0.039}, "kalshi_slope": {"intercept": 0.211, "slope": 1.088, "slope_se": 0.044}, "n": 4392}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.508, "slope": 0.859, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.15, "slope": 1.069, "slope_se": 0.034}, "n": 6464}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 432, "model_brier": 0.3096, "kalshi_brier": 0.2358, "brier_diff_model_minus_kalshi": 0.0738, "brier_diff_se": 0.0146, "corr_model_outcome": 0.0434, "corr_kalshi_outcome": 0.2537}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
