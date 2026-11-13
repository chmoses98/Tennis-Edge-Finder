# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-13T19:23Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 92,124): 0-3 13.9%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.8%, 40+ 8.4%; median gap 11.94 pp.
* **Where the extremes live**: 97.4% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.3%, Challenger 11.1%, doubles 6.5%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 20,391): MARKET_ALREADY_SETTLED_WHEN_PRICED 35.6%, STALE_QUOTE 19.9%, BOOK_QUALITY 16.2%, POOR_DATA 9.0%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 35.6%, market_freshness 19.9%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.9% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 20,391 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.8%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 0.9%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 489.0 points vs 1672.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.021, Gen-2 0.818, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 1043 model 0.2256 vs Kalshi 0.2037; n 214 model 0.307 vs Kalshi 0.1666.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 381,444 model-market comparisons (632,267 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 125,414 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-13T19:09:10.921048+00:00'], shadow board 106,786 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-13T19:09:14.122673+00:00'], Model 4 44,286 rows, 31,711 settled tickers, 11,931 tickers with an external scan.
* By model: {"gen1_ledger": 83730, "gen1_elo": 53661, "fair_v1": 53661, "gen2": 53661, "gen1_sr": 53661, "model4_fundamental": 41577, "model4_conditioned": 41493}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 92,124 | 13.9 | 9.5 | 20.1 | 15.2 | 19.2 | 13.8 | 8.4 | 11.94 | 41.3% | 22.1% |
| MW fair_v1 | 53,661 | 12.5 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.4 | 13.24 | 45.1% | 25.5% |
| MW gen1_elo | 53,661 | 12.3 | 8.7 | 19.1 | 15.3 | 19.4 | 15.0 | 10.2 | 13.02 | 44.6% | 25.2% |
| MW gen1_ledger | 38,463 | 15.8 | 10.8 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 53,661 | 9.9 | 7.1 | 16.5 | 13.9 | 20.9 | 18.8 | 12.9 | 16.02 | 52.6% | 31.7% |
| MW gen2 | 53,661 | 10.8 | 7.5 | 16.6 | 13.7 | 19.7 | 17.7 | 14.0 | 15.56 | 51.4% | 31.7% |
| all families model4_conditioned | 41,493 | 22.2 | 17.9 | 34.6 | 16.9 | 5.0 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 41,577 | 17.3 | 13.5 | 34.0 | 19.9 | 9.9 | 3.8 | 1.5 | 7.6 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.6%, >=10pp 56.5%, >=15pp 41.3%, >=20pp 30.5%, >=25pp 22.1%, >=30pp 16.1%, >=40pp 8.4%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.61pp; >=10pp 45.8%, >=25pp 17.6%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,132 | 27.9 | 16.0 | 28.0 | 13.2 | 10.7 | 3.5 | 0.6 | 5.77 | 14.9% | 4.1% |
| CHALLENGER | 8,422 | 16.4 | 9.6 | 20.6 | 15.2 | 15.7 | 11.3 | 11.2 | 10.93 | 38.3% | 22.6% |
| ITF_MEN | 15,905 | 9.6 | 7.3 | 17.0 | 14.9 | 21.0 | 17.1 | 12.9 | 15.45 | 51.1% | 30.1% |
| ITF_WOMEN | 20,757 | 9.3 | 7.0 | 16.1 | 14.6 | 22.2 | 18.6 | 12.1 | 16.04 | 52.9% | 30.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,112 | 16.6 | 13.2 | 24.9 | 20.7 | 16.8 | 6.7 | 1.1 | 8.65 | 24.6% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,132 | 26.3 | 15.7 | 26.4 | 15.7 | 11.3 | 3.9 | 0.8 | 6.09 | 16.0% | 4.7% |
| CHALLENGER | 8,422 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.6 | 11.7 | 12.54 | 43.7% | 25.3% |
| ITF_MEN | 15,905 | 8.2 | 6.2 | 15.2 | 13.8 | 20.4 | 19.9 | 16.4 | 17.84 | 56.6% | 36.2% |
| ITF_WOMEN | 20,757 | 7.8 | 5.8 | 14.1 | 12.7 | 20.7 | 21.2 | 17.8 | 19.21 | 59.7% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,112 | 14.1 | 10.3 | 21.5 | 16.3 | 22.6 | 12.8 | 2.5 | 11.28 | 37.8% | 15.3% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,132 | 23.4 | 14.1 | 25.6 | 15.5 | 14.3 | 5.9 | 1.1 | 7.03 | 21.3% | 7.0% |
| CHALLENGER | 8,422 | 15.2 | 9.6 | 20.8 | 15.6 | 16.0 | 11.9 | 11.0 | 11.16 | 39.0% | 22.9% |
| ITF_MEN | 15,905 | 9.3 | 7.3 | 17.2 | 14.3 | 21.4 | 17.3 | 13.2 | 15.75 | 51.9% | 30.5% |
| ITF_WOMEN | 20,757 | 9.2 | 6.8 | 16.2 | 15.5 | 22.1 | 18.7 | 11.5 | 15.83 | 52.2% | 30.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,112 | 22.4 | 17.2 | 31.8 | 15.2 | 9.1 | 3.3 | 1.0 | 6.12 | 13.4% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,501 | 28.1 | 19.6 | 29.1 | 12.2 | 8.1 | 2.5 | 0.4 | 5.24 | 11.0% | 3.0% |
| CHALLENGER | 5,100 | 23.2 | 14.7 | 27.6 | 14.7 | 12.9 | 5.4 | 1.5 | 6.97 | 19.8% | 6.9% |
| DOUBLES | 2,839 | 4.8 | 4.4 | 12.9 | 10.9 | 20.5 | 24.9 | 21.6 | 23.31 | 67.0% | 46.4% |
| ITF_MEN | 11,455 | 12.8 | 9.6 | 21.5 | 15.7 | 21.6 | 12.8 | 6.0 | 11.77 | 40.4% | 18.8% |
| ITF_WOMEN | 13,329 | 13.4 | 9.3 | 19.9 | 15.8 | 21.6 | 14.6 | 5.4 | 12.15 | 41.5% | 19.9% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,834 | 23.8 | 15.9 | 31.9 | 16.8 | 8.8 | 2.5 | 0.2 | 6.57 | 11.6% | 2.7% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,003 | 28.4 | 16.2 | 28.4 | 13.2 | 10.5 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,905 | 21.2 | 12.0 | 25.7 | 18.0 | 15.7 | 5.6 | 1.8 | 8.18 | 23.1% | 7.4% |
| ITF_MEN | 11,471 | 11.9 | 8.8 | 20.6 | 17.2 | 22.1 | 14.0 | 5.4 | 12.43 | 41.5% | 19.4% |
| ITF_WOMEN | 15,033 | 11.3 | 8.6 | 19.1 | 17.0 | 24.1 | 15.3 | 4.5 | 13.12 | 43.9% | 19.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,998 | 16.8 | 13.3 | 25.2 | 21.1 | 16.8 | 6.2 | 0.6 | 8.48 | 23.6% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,003 | 26.6 | 16.1 | 26.7 | 15.7 | 11.2 | 3.4 | 0.4 | 6.02 | 15.0% | 3.8% |
| CHALLENGER | 5,905 | 18.1 | 11.8 | 23.9 | 16.2 | 19.0 | 8.9 | 2.1 | 8.97 | 30.0% | 11.0% |
| ITF_MEN | 11,473 | 9.7 | 7.4 | 17.8 | 16.0 | 22.3 | 17.9 | 8.9 | 14.67 | 49.1% | 26.8% |
| ITF_WOMEN | 15,035 | 8.9 | 7.0 | 16.1 | 14.2 | 22.6 | 20.6 | 10.6 | 16.51 | 53.8% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,998 | 14.3 | 10.4 | 21.8 | 16.4 | 22.7 | 12.5 | 1.9 | 11.05 | 37.1% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,431 | 28.4 | 19.8 | 29.1 | 12.3 | 7.7 | 2.3 | 0.3 | 5.17 | 10.4% | 2.6% |
| CHALLENGER | 4,511 | 24.6 | 15.5 | 28.8 | 14.8 | 12.2 | 3.7 | 0.4 | 6.48 | 16.4% | 4.1% |
| DOUBLES | 2,658 | 4.7 | 4.5 | 13.1 | 10.9 | 20.4 | 24.8 | 21.7 | 23.23 | 66.8% | 46.5% |
| ITF_MEN | 9,892 | 13.6 | 10.1 | 22.9 | 16.3 | 21.7 | 11.4 | 4.1 | 10.94 | 37.2% | 15.5% |
| ITF_WOMEN | 11,474 | 14.1 | 9.8 | 21.0 | 16.4 | 21.8 | 13.4 | 3.6 | 11.38 | 38.8% | 17.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,771 | 24.2 | 16.3 | 32.0 | 16.8 | 8.8 | 2.0 | 0.1 | 6.43 | 10.8% | 2.0% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,839 | 4.8 | 4.4 | 12.9 | 10.9 | 20.5 | 24.9 | 21.6 | 23.31 | 67.0% | 46.4% |
| singles | 35,624 | 16.6 | 11.4 | 22.9 | 15.5 | 18.4 | 10.9 | 4.2 | 9.75 | 33.6% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 11,706 | 12.6 | 9.0 | 19.2 | 14.9 | 19.7 | 14.3 | 10.3 | 13.03 | 44.3% | 24.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 34,883 | 12.9 | 8.6 | 18.8 | 15.1 | 19.2 | 15.1 | 10.4 | 13.05 | 44.6% | 25.4% |
| UNKNOWN | 6,659 | 10.4 | 7.5 | 17.1 | 16.6 | 21.5 | 15.8 | 11.1 | 14.3 | 48.4% | 26.9% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,895 | 19.0 | 11.8 | 22.4 | 15.7 | 14.9 | 9.5 | 6.6 | 9.05 | 31.1% | 16.2% |
| B | 6,370 | 12.9 | 8.5 | 19.5 | 15.2 | 19.8 | 12.4 | 11.7 | 12.86 | 43.9% | 24.1% |
| C | 7,678 | 11.9 | 8.5 | 19.2 | 15.9 | 19.2 | 14.7 | 10.5 | 13.07 | 44.4% | 25.2% |
| D | 8,886 | 11.2 | 8.3 | 17.8 | 15.2 | 21.6 | 15.7 | 10.1 | 14.09 | 47.4% | 25.8% |
| F | 15,832 | 7.3 | 5.7 | 15.1 | 14.2 | 23.0 | 21.1 | 13.7 | 18.05 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,096 | 25.0 | 15.9 | 29.0 | 14.9 | 10.5 | 3.4 | 1.2 | 6.35 | 15.2% | 4.7% |
| B | 5,231 | 16.7 | 11.0 | 24.1 | 17.1 | 18.9 | 9.4 | 2.9 | 9.61 | 31.2% | 12.3% |
| C | 7,613 | 11.0 | 7.8 | 19.5 | 14.9 | 20.9 | 15.7 | 10.1 | 13.49 | 46.7% | 25.8% |
| D | 5,888 | 14.4 | 9.9 | 21.0 | 15.5 | 21.1 | 12.8 | 5.3 | 11.42 | 39.2% | 18.1% |
| F | 9,635 | 10.2 | 8.4 | 16.7 | 14.5 | 23.4 | 18.8 | 7.9 | 15.07 | 50.2% | 26.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,874 | 17.5 | 10.9 | 21.3 | 15.5 | 15.2 | 10.2 | 9.4 | 10.04 | 34.9% | 19.7% |
| LIMITED | 11,669 | 13.4 | 9.4 | 20.4 | 15.9 | 19.8 | 13.4 | 7.7 | 12.0 | 40.9% | 21.1% |
| POOR | 25,118 | 8.8 | 6.7 | 16.1 | 14.6 | 22.4 | 19.0 | 12.4 | 16.37 | 53.8% | 31.4% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,354 | 23.8 | 18.0 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.89 | 9.8% | 3.4% |
| GAME_SPREAD | 6,980 | 22.8 | 15.3 | 32.0 | 16.8 | 9.1 | 3.3 | 0.7 | 6.69 | 13.0% | 3.9% |
| MATCH_WINNER | 38,463 | 15.8 | 10.8 | 22.1 | 15.2 | 18.6 | 11.9 | 5.5 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,203 | 28.4 | 16.8 | 30.7 | 12.7 | 8.8 | 2.3 | 0.3 | 5.57 | 11.4% | 2.6% |
| TOTAL_GAMES | 11,706 | 9.7 | 10.8 | 36.5 | 25.6 | 10.4 | 4.2 | 2.8 | 9.12 | 17.4% | 7.0% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,754 | 24.5 | 28.8 | 33.3 | 8.1 | 3.9 | 1.2 | 0.3 | 4.79 | 5.4% | 1.5% |
| GAME_SPREAD | 9,596 | 46.6 | 15.8 | 25.2 | 7.4 | 2.4 | 1.9 | 0.6 | 3.33 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,143 | 6.5 | 9.8 | 41.0 | 29.8 | 7.2 | 3.3 | 2.3 | 9.14 | 12.9% | 5.6% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,790 | 23.9 | 16.6 | 34.7 | 14.7 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,605 | 20.3 | 13.4 | 28.5 | 20.2 | 12.2 | 4.3 | 1.1 | 7.71 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,182 | 10.1 | 10.9 | 36.5 | 24.3 | 11.3 | 4.4 | 2.6 | 9.0 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 53,661 | 45.1% | 25.5% | 13.24 | 35.5% | 15.1% | 10.71 |
| gen1_elo | 53,661 | 44.6% | 25.2% | 13.02 | 34.9% | 15.0% | 10.51 |
| gen1_sr | 53,661 | 52.6% | 31.7% | 16.02 | 43.9% | 21.4% | 12.98 |
| gen2 | 53,661 | 51.4% | 31.7% | 15.56 | 43.9% | 22.9% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,577 | 15.4 | 10.5 | 21.3 | 17.3 | 20.1 | 11.9 | 3.5 | 10.72 | 35.4% | 15.4% |
| STALE | 33,084 | 10.7 | 7.4 | 17.0 | 13.9 | 19.3 | 17.0 | 14.8 | 15.43 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 31,931 | 16.3 | 11.1 | 22.6 | 15.2 | 18.2 | 11.5 | 5.0 | 9.97 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 92,124 | 31931 | 24049 | 36144 | 25.3 | 152.9 | 1451.1 |
| ge_15pp | 38,055 | 11070 | 8582 | 18403 | 29.2 | 454.4 | 1451.1 |
| ge_25pp | 20,391 | 5259 | 3754 | 11378 | 35.0 | 596.0 | 1431.1 |
| lt_10pp | 40,088 | 15991 | 11364 | 12733 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261113T192346Z-3c0e45ce`: 154 priced rows, quote age at build {'median': 14.8, 'max': 14.9}, freshness {'AGING': 154}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 5,106 | 19.2 | 11.1 | 25.7 | 18.3 | 17.7 | 7.1 | 1.0 | 8.77 | 25.8% | 8.1% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,104 | 66.1 | 33.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,342 | 0.0 | 2.2 | 38.4 | 26.0 | 23.9 | 8.7 | 0.9 | 11.66 | 33.5% | 9.6% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 53,661 | 8665 (16.2%) | 27.0% | 0.9% | {"EXTERNAL_STALE": 5106, "AGREES_WITH_KALSHI": 2342, "ALL_AGREE": 1104, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 24,186 | 2131 (8.8%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 1316, "AGREES_WITH_KALSHI": 784, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,670 | 649 (4.8%) | 34.5% | 2.0% | {"EXTERNAL_STALE": 412, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 6,157 | 617 (10.0%) | 35.2% | 2.1% | {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 21,328 | 4986 (23.4%) | 19.1% | 0.9% | {"EXTERNAL_STALE": 2857, "ALL_AGREE": 1104, "AGREES_WITH_KALSHI": 950, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,533 | 10.6 | 7.7 | 18.9 | 14.3 | 21.7 | 16.4 | 10.4 | 14.4 | 48.6% | 26.8% |
| 4-10x | 7,267 | 10.9 | 8.7 | 18.1 | 14.9 | 21.5 | 14.7 | 11.4 | 14.1 | 47.5% | 26.1% |
| <2x | 27,288 | 14.5 | 9.6 | 19.8 | 15.9 | 17.6 | 13.4 | 9.3 | 11.75 | 40.2% | 22.7% |
| >=10x | 8,573 | 10.2 | 6.4 | 15.2 | 14.2 | 21.8 | 18.9 | 13.3 | 16.52 | 54.0% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 14,167 | 12.3 | 8.6 | 19.6 | 16.1 | 19.2 | 13.7 | 10.6 | 12.87 | 43.5% | 24.3% |
| 300-1000 | 11,703 | 11.4 | 8.6 | 17.8 | 15.1 | 20.5 | 16.4 | 10.1 | 13.94 | 47.0% | 26.5% |
| <300 | 16,966 | 8.1 | 5.9 | 15.1 | 14.4 | 22.9 | 20.0 | 13.6 | 17.46 | 56.5% | 33.6% |
| >=3000 | 10,825 | 20.9 | 12.8 | 23.9 | 15.3 | 14.1 | 7.5 | 5.5 | 7.92 | 27.1% | 13.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1670 | 0.5471 | 0.4082 | 0.4766 | +0.070 | -0.069 | 0.0041 ± 0.0038 |
| ratio 4-10x | 1141 | 0.5712 | 0.4271 | 0.4855 | +0.086 | -0.059 | 0.0094 ± 0.0048 |
| ratio <2x | 4071 | 0.5343 | 0.4115 | 0.4309 | +0.103 | -0.019 | 0.0149 ± 0.0022 |
| ratio >=10x | 1402 | 0.5581 | 0.3868 | 0.4301 | +0.128 | -0.043 | 0.0185 ± 0.0047 |
| thinner_sample 1000-3000 | 2290 | 0.5396 | 0.4127 | 0.4424 | +0.097 | -0.030 | 0.0129 ± 0.003 |
| thinner_sample 300-1000 | 1891 | 0.5593 | 0.4191 | 0.468 | +0.091 | -0.049 | 0.0068 ± 0.0036 |
| thinner_sample <300 | 2699 | 0.5519 | 0.3853 | 0.4398 | +0.112 | -0.054 | 0.0157 ± 0.0034 |
| thinner_sample >=3000 | 1404 | 0.5272 | 0.4337 | 0.443 | +0.084 | -0.009 | 0.0137 ± 0.003 |
| data_status ADEQUATE | 2235 | 0.5317 | 0.4294 | 0.4394 | +0.092 | -0.010 | 0.0148 ± 0.0026 |
| data_status LIMITED | 2027 | 0.5461 | 0.4133 | 0.4608 | +0.085 | -0.048 | 0.0079 ± 0.0034 |
| data_status POOR | 4022 | 0.5539 | 0.3951 | 0.4453 | +0.109 | -0.050 | 0.0137 ± 0.0027 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1188 | 0.1962 | 0.1962 | +0.0000 ± 0.0004 | 0.5717 | 0.5719 | 0.5025 | 0.4873 | 0.4916 | -0.100 ± 0.0136 | -0.0087 (8) |
| 3-5 | 775 | 0.2084 | 0.2079 | +0.0005 ± 0.0013 | 0.6028 | 0.6003 | 0.5004 | 0.4606 | 0.4735 | -0.097 ± 0.0168 | 0.01 (3) |
| 5-10 | 1784 | 0.2022 | 0.2003 | +0.0019 ± 0.0016 | 0.5906 | 0.5841 | 0.5093 | 0.4353 | 0.4585 | -0.091 ± 0.0109 | -0.0143 (7) |
| 10-15 | 1442 | 0.2202 | 0.2105 | +0.0096 ± 0.003 | 0.633 | 0.6048 | 0.524 | 0.4007 | 0.4223 | -0.103 ± 0.0123 | -0.055 (6) |
| 15-25 | 1838 | 0.2257 | 0.2074 | +0.0183 ± 0.0041 | 0.6464 | 0.5983 | 0.5705 | 0.3761 | 0.426 | -0.098 ± 0.0107 | -0.0045 (11) |
| 25-40 | 1043 | 0.2256 | 0.2037 | +0.0219 ± 0.0084 | 0.6416 | 0.5879 | 0.6428 | 0.3333 | 0.4516 | -0.065 ± 0.013 | -0.06 (2) |
| 40+ | 214 | 0.307 | 0.1666 | +0.1404 ± 0.0253 | 0.8206 | 0.5019 | 0.7244 | 0.2671 | 0.3505 | -0.089 ± 0.0244 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5997 | 0.1871 | 0.1879 | -0.0008 ± 0.0002 | 0.5506 | 0.5516 | 0.4918 | 0.4765 | 0.5054 | -0.023 ± 0.0057 | -0.01 (28) |
| 3-5 | 4086 | 0.1993 | 0.1975 | +0.0018 ± 0.0006 | 0.5797 | 0.5736 | 0.4805 | 0.4407 | 0.4381 | -0.056 ± 0.007 | 0.005 (6) |
| 5-10 | 8945 | 0.2003 | 0.196 | +0.0043 ± 0.0007 | 0.5863 | 0.5725 | 0.482 | 0.4082 | 0.4161 | -0.049 ± 0.0047 | -0.0114 (22) |
| 10-15 | 7299 | 0.2022 | 0.1861 | +0.0161 ± 0.0013 | 0.5914 | 0.5458 | 0.484 | 0.3601 | 0.3573 | -0.064 ± 0.0051 | -0.0379 (19) |
| 15-25 | 9398 | 0.2063 | 0.1672 | +0.0391 ± 0.0017 | 0.6045 | 0.4969 | 0.4977 | 0.3022 | 0.3008 | -0.067 ± 0.0042 | -0.0043 (51) |
| 25-40 | 7349 | 0.2225 | 0.1236 | +0.0989 ± 0.0026 | 0.6391 | 0.3813 | 0.5232 | 0.2089 | 0.2124 | -0.058 ± 0.004 | -0.0733 (3) |
| 40+ | 5089 | 0.3795 | 0.0439 | +0.3356 ± 0.0033 | 0.989 | 0.1707 | 0.6274 | 0.1018 | 0.057 | -0.076 ± 0.0028 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 952 | 0.2022 | 0.2025 | -0.0003 ± 0.0005 | 0.5845 | 0.5854 | 0.5081 | 0.4931 | 0.5168 | -0.095 ± 0.0156 | -0.0117 (6) |
| 3-5 | 696 | 0.2116 | 0.2087 | +0.0029 ± 0.0014 | 0.6069 | 0.6004 | 0.5184 | 0.4788 | 0.4598 | -0.124 ± 0.0186 | 0.01 (3) |
| 5-10 | 1542 | 0.2044 | 0.2027 | +0.0016 ± 0.0017 | 0.594 | 0.59 | 0.5385 | 0.464 | 0.4916 | -0.083 ± 0.0118 | -0.01 (4) |
| 10-15 | 1338 | 0.2153 | 0.2073 | +0.0080 ± 0.0031 | 0.6231 | 0.6003 | 0.5573 | 0.4329 | 0.4656 | -0.102 ± 0.0129 | -0.04 (5) |
| 15-25 | 1935 | 0.2333 | 0.2124 | +0.0209 ± 0.0041 | 0.6645 | 0.6091 | 0.584 | 0.3883 | 0.4346 | -0.097 ± 0.0107 | -0.0183 (12) |
| 25-40 | 1335 | 0.2663 | 0.2001 | +0.0662 ± 0.0077 | 0.7429 | 0.5807 | 0.6581 | 0.3444 | 0.3978 | -0.108 ± 0.0123 | -0.008 (5) |
| 40+ | 486 | 0.3749 | 0.1598 | +0.2151 ± 0.0182 | 1.0178 | 0.4849 | 0.7318 | 0.2426 | 0.2798 | -0.088 ± 0.0175 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5158 | 0.1901 | 0.1903 | -0.0002 ± 0.0002 | 0.5554 | 0.5557 | 0.5058 | 0.4907 | 0.5056 | -0.039 ± 0.0062 | -0.0154 (26) |
| 3-5 | 3585 | 0.1937 | 0.1927 | +0.0010 ± 0.0006 | 0.5646 | 0.5617 | 0.5107 | 0.471 | 0.4775 | -0.044 ± 0.0075 | 0.01 (5) |
| 5-10 | 7996 | 0.1954 | 0.1921 | +0.0033 ± 0.0007 | 0.5749 | 0.5625 | 0.5066 | 0.4323 | 0.4495 | -0.038 ± 0.005 | -0.0117 (6) |
| 10-15 | 6616 | 0.2018 | 0.1896 | +0.0122 ± 0.0013 | 0.5928 | 0.5553 | 0.5056 | 0.3817 | 0.3954 | -0.049 ± 0.0054 | -0.0189 (18) |
| 15-25 | 9489 | 0.2164 | 0.1804 | +0.0360 ± 0.0017 | 0.6305 | 0.5294 | 0.5237 | 0.3282 | 0.3364 | -0.058 ± 0.0044 | -0.014 (52) |
| 25-40 | 8519 | 0.2497 | 0.1377 | +0.1121 ± 0.0026 | 0.7057 | 0.4202 | 0.5587 | 0.2414 | 0.227 | -0.075 ± 0.004 | -0.0095 (20) |
| 40+ | 6800 | 0.4019 | 0.0592 | +0.3427 ± 0.0034 | 1.0589 | 0.2128 | 0.6544 | 0.1189 | 0.08 | -0.074 ± 0.0029 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1165 | 0.1962 | 0.1974 | -0.0011 ± 0.0005 | 0.5723 | 0.5749 | 0.5017 | 0.4863 | 0.5227 | -0.060 ± 0.0136 | -0.0191 (11) |
| 3-5 | 841 | 0.209 | 0.2075 | +0.0016 ± 0.0013 | 0.6055 | 0.6003 | 0.4956 | 0.4561 | 0.4578 | -0.108 ± 0.0164 | 0.002 (5) |
| 5-10 | 1793 | 0.2032 | 0.1991 | +0.0041 ± 0.0016 | 0.5919 | 0.5806 | 0.5097 | 0.4359 | 0.4445 | -0.103 ± 0.0108 | -0.01 (10) |
| 10-15 | 1488 | 0.2124 | 0.2029 | +0.0095 ± 0.0029 | 0.6157 | 0.5884 | 0.5371 | 0.4138 | 0.4388 | -0.103 ± 0.0118 | -0.0286 (7) |
| 15-25 | 1740 | 0.2313 | 0.212 | +0.0193 ± 0.0043 | 0.6598 | 0.6081 | 0.5796 | 0.3857 | 0.4328 | -0.102 ± 0.0111 | -0.03 (1) |
| 25-40 | 1028 | 0.2177 | 0.2059 | +0.0118 ± 0.0084 | 0.6253 | 0.5928 | 0.6509 | 0.3414 | 0.4747 | -0.058 ± 0.0131 | -0.0267 (3) |
| 40+ | 229 | 0.3093 | 0.1804 | +0.1289 ± 0.0253 | 0.8338 | 0.5323 | 0.7372 | 0.2806 | 0.3799 | -0.075 ± 0.0258 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5826 | 0.1867 | 0.1872 | -0.0005 ± 0.0002 | 0.5493 | 0.5497 | 0.487 | 0.4716 | 0.4858 | -0.037 ± 0.0057 | -0.0189 (44) |
| 3-5 | 4185 | 0.2046 | 0.2029 | +0.0017 ± 0.0006 | 0.5944 | 0.5887 | 0.4802 | 0.4407 | 0.4392 | -0.056 ± 0.0071 | -0.0073 (22) |
| 5-10 | 9082 | 0.1963 | 0.1908 | +0.0055 ± 0.0007 | 0.5763 | 0.559 | 0.4849 | 0.4109 | 0.4102 | -0.057 ± 0.0046 | -0.0117 (42) |
| 10-15 | 7308 | 0.1953 | 0.1796 | +0.0157 ± 0.0012 | 0.5761 | 0.5319 | 0.4946 | 0.3713 | 0.3695 | -0.063 ± 0.005 | -0.0136 (14) |
| 15-25 | 9411 | 0.211 | 0.1719 | +0.0391 ± 0.0017 | 0.6154 | 0.507 | 0.5094 | 0.3146 | 0.3125 | -0.067 ± 0.0043 | -0.0533 (3) |
| 25-40 | 7348 | 0.2165 | 0.1234 | +0.0931 ± 0.0026 | 0.626 | 0.38 | 0.5247 | 0.2092 | 0.221 | -0.051 ± 0.004 | -0.02 (4) |
| 40+ | 5003 | 0.388 | 0.0479 | +0.3402 ± 0.0035 | 1.0116 | 0.1808 | 0.6363 | 0.1072 | 0.063 | -0.077 ± 0.003 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1645 | 0.196 | 0.1956 | +0.0004 ± 0.0004 | 0.5702 | 0.5692 | 0.5063 | 0.4912 | 0.4875 | -0.075 ± 0.0111 | -0.0221 (56) |
| 3-5 | 1161 | 0.1895 | 0.1896 | -0.0001 ± 0.001 | 0.5571 | 0.5564 | 0.4986 | 0.4587 | 0.478 | -0.053 ± 0.0131 | -0.0194 (34) |
| 5-10 | 2358 | 0.1987 | 0.1936 | +0.0051 ± 0.0014 | 0.5863 | 0.57 | 0.51 | 0.4363 | 0.4389 | -0.077 ± 0.0093 | -0.005 (78) |
| 10-15 | 1625 | 0.2157 | 0.2035 | +0.0123 ± 0.0028 | 0.6261 | 0.5906 | 0.5445 | 0.4217 | 0.432 | -0.087 ± 0.0115 | 0.0015 (67) |
| 15-25 | 2118 | 0.2325 | 0.2076 | +0.0249 ± 0.0039 | 0.6632 | 0.5989 | 0.5924 | 0.3974 | 0.4325 | -0.090 ± 0.01 | -0.0214 (59) |
| 25-40 | 1234 | 0.2419 | 0.2121 | +0.0298 ± 0.008 | 0.6904 | 0.6075 | 0.6884 | 0.3768 | 0.4854 | -0.081 ± 0.0124 | -0.0243 (28) |
| 40+ | 457 | 0.3282 | 0.1985 | +0.1298 ± 0.02 | 0.937 | 0.5788 | 0.8071 | 0.3305 | 0.4486 | -0.089 ± 0.0188 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5928 | 0.1772 | 0.1772 | +0.0000 ± 0.0002 | 0.5248 | 0.5242 | 0.5088 | 0.4936 | 0.4997 | -0.042 ± 0.0055 | -0.0154 (103) |
| 3-5 | 4069 | 0.1943 | 0.1935 | +0.0008 ± 0.0006 | 0.5672 | 0.5653 | 0.502 | 0.4622 | 0.4724 | -0.039 ± 0.007 | -0.0212 (73) |
| 5-10 | 8321 | 0.1969 | 0.1904 | +0.0065 ± 0.0007 | 0.5809 | 0.5614 | 0.5032 | 0.4295 | 0.4233 | -0.061 ± 0.0048 | -0.0084 (134) |
| 10-15 | 5722 | 0.211 | 0.1949 | +0.0161 ± 0.0014 | 0.6143 | 0.5708 | 0.5378 | 0.4148 | 0.4095 | -0.070 ± 0.0059 | -0.0054 (112) |
| 15-25 | 7008 | 0.2318 | 0.1993 | +0.0325 ± 0.0021 | 0.6664 | 0.5778 | 0.5769 | 0.3815 | 0.3964 | -0.068 ± 0.0054 | -0.024 (112) |
| 25-40 | 4514 | 0.2576 | 0.1912 | +0.0664 ± 0.0041 | 0.7282 | 0.556 | 0.6408 | 0.3287 | 0.3813 | -0.060 ± 0.0064 | -0.0267 (58) |
| 40+ | 2023 | 0.37 | 0.1595 | +0.2105 ± 0.0091 | 1.0389 | 0.4753 | 0.7407 | 0.2412 | 0.2907 | -0.058 ± 0.0085 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 8284 | 1.021 ± 0.031 | 1.08 | 0.1677 | 0.1712 | 0.2159 | 0.2033 |
| gen2 | 8284 | 0.818 ± 0.028 | 1.06 | 0.174 | 0.1714 | 0.2332 | 0.2033 |
| gen1_elo | 8284 | 1.003 ± 0.03 | 1.072 | 0.1741 | 0.1714 | 0.2151 | 0.2034 |
| gen1_sr | 8284 | 1.004 ± 0.036 | 1.107 | 0.1336 | 0.1729 | 0.2293 | 0.203 |
| gen1_ledger | 10598 | 0.866 ± 0.023 | 1.061 | 0.1904 | 0.1772 | 0.2172 | 0.2001 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 38,055)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 9,167 | 24.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 9,004 | 23.7% |
| BOOK_QUALITY | execution | 6,389 | 16.8% |
| POOR_DATA | data | 4,333 | 11.4% |
| LIMITED_DATA | data | 2,279 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,232 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 1,564 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,434 | 3.8% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,069 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 583 | 1.5% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.1%, coverage 23.7%, data 17.4%, execution 16.8%, market_freshness/coverage 8.7%, mapping 4.1%, model_calibration_or_unknown 3.8%, model_calibration 1.5%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.7%, START_UNVERIFIABLE 95.1%, LOW_DATA_QUALITY 72.2%, THIN_PLAYER_HISTORY 60.1%, STALE_PLAYER_DATA 51.9%, STALE_KALSHI_QUOTE 48.4%, MODEL_INTERNAL_DISAGREEMENT 41.7%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 23.2%, MODEL_HIGH_UNCERTAINTY 18.8%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.7%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.1%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 26.0%, POST_SETTLEMENT_OBSERVATION 23.7%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 20,391)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,255 | 35.6% |
| STALE_QUOTE | market_freshness | 4,066 | 19.9% |
| BOOK_QUALITY | execution | 3,298 | 16.2% |
| POOR_DATA | data | 1,834 | 9.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,204 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 867 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 703 | 3.5% |
| LIMITED_DATA | data | 673 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 350 | 1.7% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 140 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 35.6%, market_freshness 19.9%, execution 16.2%, data 12.3%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.7%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.2%, START_UNVERIFIABLE 97.4%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 62.1%, STALE_KALSHI_QUOTE 55.8%, STALE_PLAYER_DATA 45.1%, MODEL_INTERNAL_DISAGREEMENT 41.7%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 22.4%, MODEL_HIGH_UNCERTAINTY 19.5%, PLAYER_IDENTITY_RISK 17.8%, LOW_DISPLAYED_LIQUIDITY 8.6%, EVENT_MAPPING_RISK 8.5%, LEVEL_TRANSFER_RISK 8.1%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.7%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 38.5%, POST_SETTLEMENT_OBSERVATION 35.6%, POSSIBLE_IN_PLAY_QUOTE 6.4%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 16412, "IDENTITY_AMBIGUOUS": 3979}; ticker orientation: {"VERIFIED": 20391}.

Checks: discipline:AMBIGUOUS 1318, discipline:PASS 19073, identity_confidence:AMBIGUOUS 3626, identity_confidence:PASS 16765, level_mapping:NA 1330, level_mapping:PASS 19061, market_pair:AMBIGUOUS 518, market_pair:NA 433, market_pair:PASS 19440, model_complement:NA 395, model_complement:PASS 19996, namesake:AMBIGUOUS 6, namesake:PASS 20385, physical_match_id:NA 6721, physical_match_id:PASS 13670, player_ids:PASS 20391, same_pair_other_event:PASS 20391, ticker_orientation:PASS 20391

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,633 | 3.7% | 3.1% | 1.2% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.222 / 0.2184 (873) | 25.7% | 2.4% | 3.2% | 3.0% |
| CHALLENGER | 13,522 | 16.7% | 6.0% | 11.1% | {"coverage": 1388, "market_freshness": 274, "market_freshness/coverage": 245, "data": 164, "model_calibration_or_unknown": 84, "execution": 41, "model_calibration": 41, "mapping": 17, "possible_market_error": 1} | 7.3 | 0.2214 / 0.2113 (3148) | 41.8% | 13.5% | 4.0% | 23.0% |
| DOUBLES | 2,839 | 46.4% | 46.5% | 6.5% | {"execution": 728, "mapping": 401, "market_freshness": 106, "market_freshness/coverage": 76, "coverage": 7} | 23.23 | 0.2968 / 0.2315 (717) | 8.2% | 0.0% | 100.0% | 6.4% |
| ITF_MEN | 27,360 | 25.4% | 17.6% | 34.0% | {"coverage": 2469, "market_freshness": 1439, "execution": 1055, "data": 1023, "market_freshness/coverage": 708, "mapping": 233, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.73 | 0.2183 / 0.1979 (5837) | 42.4% | 69.7% | 14.3% | 21.9% |
| ITF_WOMEN | 34,086 | 26.5% | 18.6% | 44.3% | {"coverage": 3312, "market_freshness": 1986, "execution": 1391, "data": 1219, "market_freshness/coverage": 799, "mapping": 210, "model_calibration_or_unknown": 98, "model_calibration": 23} | 12.43 | 0.2035 / 0.1941 (6679) | 43.0% | 57.2% | 10.1% | 22.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,946 | 5.9% | 5.0% | 1.4% | {"market_freshness": 111, "model_calibration_or_unknown": 52, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2311 / 0.2208 (816) | 30.3% | 2.0% | 1.2% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.4% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFMATCH-26NOV12VALRAT-RAT` | ITF_MEN | gen1_ledger | 92% / 4% | +88 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 10 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 1333.0, ratio 3.64); no external reference |
| 6 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 7 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 8 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 9 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 172 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 10 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 11 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 12 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.1h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 493 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 13 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 14 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 658 min (STALE); no external reference |
| 17 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 18 | `KXITFMATCH-26NOV13ALMJAD-ALM` | ITF_MEN | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 68 min (STALE); data LIMITED (grade C, thinner serve sample 691.0, ratio 3.98); no external reference |
| 19 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 20 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 21 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 22 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 23 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 24 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 25 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 26 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 27 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 28 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 29 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 30 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 31 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 32 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 33 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 34 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 35 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 36 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 37 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 38 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 39 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 40 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 41 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 42 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 43 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 44 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 45 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 46 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 47 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 48 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 49 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 649 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 50 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9736, "by_level_share_of_ge_25pp": {"ATP": 0.012, "CHALLENGER": 0.1106, "DOUBLES": 0.0646, "ITF_MEN": 0.3402, "ITF_WOMEN": 0.4432, "OTHER": 0.0006, "WTA": 0.0143, "WTA125": 0.0144}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.558, "share_primary_cause_market_settled_or_in_play": 0.4493, "share_primary_cause_stale_quote_only": 0.1994}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 20391, "identity_ambiguous_share": 0.1951, "ticker_orientation": {"VERIFIED": 20391}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13670, "with_external": 649, "coverage": 0.0475, "external_status": {"EXTERNAL_STALE": 412, "AGREES_WITH_KALSHI": 224, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 412, "MODEL_LONE_OUTLIER": 224, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3451, "share_external_supports_model": 0.02}, "pregame_clean_ge_25pp": {"n": 6157, "with_external": 617, "coverage": 0.1002, "external_status": {"EXTERNAL_STALE": 387, "AGREES_WITH_KALSHI": 217, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 387, "MODEL_LONE_OUTLIER": 217, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3517, "share_external_supports_model": 0.0211}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 489.0, "median_sample_ratio": 2.43, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2055, "data_status": {"POOR": 11570, "LIMITED": 5146, "ADEQUATE": 3675}, "comparison_lt_10pp": {"median_thinner_serve_points": 1672.0, "median_sample_ratio": 1.71, "median_min_matches": 86.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1670, "model_minus_observed": 0.0704, "kalshi_minus_observed": -0.0685, "brier_diff_model_minus_kalshi": 0.0041}, "4-10x": {"n": 1141, "model_minus_observed": 0.0857, "kalshi_minus_observed": -0.0585, "brier_diff_model_minus_kalshi": 0.0094}, "<2x": {"n": 4071, "model_minus_observed": 0.1035, "kalshi_minus_observed": -0.0194, "brier_diff_model_minus_kalshi": 0.0149}, ">=10x": {"n": 1402, "model_minus_observed": 0.128, "kalshi_minus_observed": -0.0433, "brier_diff_model_minus_kalshi": 0.0185}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 8284, "model": {"intercept": -0.561, "slope": 0.818, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.167, "slope": 1.06, "slope_se": 0.031}, "mean_extremity_model": 0.174, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2332, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.03, "brier_diff_se": 0.0021, "model_logloss": 0.664, "kalshi_logloss": 0.5888}, "fair_v1": {"n": 8284, "model": {"intercept": -0.471, "slope": 1.021, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.211, "slope": 1.08, "slope_se": 0.031}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1712, "model_brier": 0.2159, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0126, "brier_diff_se": 0.0017, "model_logloss": 0.6212, "kalshi_logloss": 0.589}, "gen1_elo": {"n": 8284, "model": {"intercept": -0.458, "slope": 1.003, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.215, "slope": 1.072, "slope_se": 0.031}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1714, "model_brier": 0.2151, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0117, "brier_diff_se": 0.0017, "model_logloss": 0.6199, "kalshi_logloss": 0.5891}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2547, "share_ge_15": 0.4507, "median_abs_gap": 13.24, "n": 53661}, "gen1_elo": {"share_ge_25": 0.2525, "share_ge_15": 0.4463, "median_abs_gap": 13.02, "n": 53661}, "gen1_sr": {"share_ge_25": 0.317, "share_ge_15": 0.5258, "median_abs_gap": 16.02, "n": 53661}, "gen2": {"share_ge_25": 0.317, "share_ge_15": 0.514, "median_abs_gap": 15.56, "n": 53661}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1513, "share_ge_15": 0.3548, "median_abs_gap": 10.71, "n": 40694}, "gen1_elo": {"share_ge_25": 0.1496, "share_ge_15": 0.3489, "median_abs_gap": 10.51, "n": 40694}, "gen1_sr": {"share_ge_25": 0.2143, "share_ge_15": 0.4393, "median_abs_gap": 12.98, "n": 40697}, "gen2": {"share_ge_25": 0.2294, "share_ge_15": 0.4388, "median_abs_gap": 12.83, "n": 40698}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0369, "share_ge_25_pregame_clean": 0.0309}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.059, "share_ge_25_pregame_clean": 0.0501}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.234, "share_within_10pp_all": 0.4352, "share_within_10pp_pregame_clean": 0.4906, "corr_model_vs_mid_pregame_clean": 0.85}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1188, "model_brier": 0.1962, "kalshi_brier": 0.1962, "brier_diff_model_minus_kalshi": 0.0}, "10-15": {"n_settled": 1442, "model_brier": 0.2202, "kalshi_brier": 0.2105, "brier_diff_model_minus_kalshi": 0.0096}, "15-25": {"n_settled": 1838, "model_brier": 0.2257, "kalshi_brier": 0.2074, "brier_diff_model_minus_kalshi": 0.0183}, "25-40": {"n_settled": 1043, "model_brier": 0.2256, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0219}, "3-5": {"n_settled": 775, "model_brier": 0.2084, "kalshi_brier": 0.2079, "brier_diff_model_minus_kalshi": 0.0005}, "40+": {"n_settled": 214, "model_brier": 0.307, "kalshi_brier": 0.1666, "brier_diff_model_minus_kalshi": 0.1404}, "5-10": {"n_settled": 1784, "model_brier": 0.2022, "kalshi_brier": 0.2003, "brier_diff_model_minus_kalshi": 0.0019}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.561, "slope": 0.818, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.167, "slope": 1.06, "slope_se": 0.031}, "n": 8284}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.5, "slope": 0.866, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.15, "slope": 1.061, "slope_se": 0.026}, "n": 10598}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 717, "model_brier": 0.2968, "kalshi_brier": 0.2315, "brier_diff_model_minus_kalshi": 0.0653, "brier_diff_se": 0.0109, "corr_model_outcome": 0.1186, "corr_kalshi_outcome": 0.2835}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
