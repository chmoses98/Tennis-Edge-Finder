# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-01T05:47Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 8,456): 0-3 12.9%, 3-5 9.5%, 5-10 19.7%, 10-15 14.6%, 15-25 19.6%, 25-40 14.3%, 40+ 9.4%; median gap 12.54 pp.
* **Where the extremes live**: 97.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.3%, Challenger 11.7%, doubles 8.1%). Main tour: ATP 1.7% and WTA 7.3% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,006): MARKET_ALREADY_SETTLED_WHEN_PRICED 44.0%, STALE_QUOTE 22.4%, POOR_DATA 7.1%, POSSIBLY_IN_PLAY_QUOTE 6.3%, BOOK_QUALITY 6.2%, IN_PLAY_QUOTE 6.0%, LIMITED_DATA 3.6%, IDENTITY_AMBIGUOUS 2.8%, UNEXPLAINED_MODEL_DISAGREEMENT 1.7%. By class: coverage 44.0%, market_freshness 22.4%, market_freshness/coverage 12.3%, data 10.7%, execution 6.2%, mapping 2.8%, model_calibration_or_unknown 1.7%.
* **Stale / settled / in-play**: 66.0% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,006 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 16.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 9.0% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 664.0 points vs 2045.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.212, Gen-2 0.951, Gen-1 ledger 0.9 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 68 model 0.2385 vs Kalshi 0.1851; n 15 model 0.3032 vs Kalshi 0.1389.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%). Not implemented here.

## 1. Observations

* 25,068 model-market comparisons (42,829 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 14,906 rows ['2026-09-11T13:47:52.094820+00:00', '2026-09-30T23:03:37.532882+00:00'], shadow board 6,307 rows ['2026-09-28T03:33:22.503933+00:00', '2026-09-30T23:03:41.938238+00:00'], Model 4 1,800 rows, 7,536 settled tickers, 1,667 tickers with an external scan.
* By model: {"gen1_ledger": 8832, "gen1_elo": 3173, "fair_v1": 3173, "gen2": 3173, "gen1_sr": 3173, "model4_fundamental": 1773, "model4_conditioned": 1771}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 8,456 | 12.9 | 9.5 | 19.7 | 14.6 | 19.6 | 14.3 | 9.4 | 12.54 | 43.4% | 23.7% |
| MW fair_v1 | 3,173 | 12.7 | 9.3 | 18.8 | 14.6 | 18.9 | 14.9 | 10.8 | 13.06 | 44.6% | 25.8% |
| MW gen1_elo | 3,173 | 13.8 | 7.9 | 19.6 | 14.8 | 18.7 | 15.2 | 9.9 | 12.73 | 43.8% | 25.1% |
| MW gen1_ledger | 5,283 | 12.9 | 9.6 | 20.2 | 14.6 | 20.1 | 13.9 | 8.6 | 12.23 | 42.6% | 22.5% |
| MW gen1_sr | 3,173 | 9.5 | 6.1 | 17.3 | 13.9 | 20.7 | 19.2 | 13.3 | 16.3 | 53.2% | 32.5% |
| MW gen2 | 3,173 | 10.1 | 6.2 | 16.3 | 16.1 | 19.4 | 17.4 | 14.6 | 15.49 | 51.4% | 32.0% |
| all families model4_conditioned | 1,771 | 21.1 | 15.9 | 30.0 | 20.4 | 8.9 | 1.7 | 2.0 | 6.75 | 12.5% | 3.7% |
| all families model4_fundamental | 1,773 | 14.9 | 10.9 | 31.6 | 21.7 | 13.3 | 5.0 | 2.6 | 8.67 | 20.9% | 7.6% |

Configurable thresholds (primary): >=5pp 77.6%, >=10pp 58.0%, >=15pp 43.4%, >=20pp 32.6%, >=25pp 23.7%, >=30pp 17.8%, >=40pp 9.4%, >=50pp 4.2%
Executable gap (model outside the book, before fees): median 10.0pp; >=10pp 50.0%, >=25pp 21.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 172 | 22.7 | 22.1 | 23.8 | 10.5 | 18.6 | 1.7 | 0.6 | 5.86 | 20.9% | 2.3% |
| CHALLENGER | 614 | 15.8 | 9.9 | 14.8 | 16.6 | 15.6 | 13.4 | 13.8 | 13.33 | 42.8% | 27.2% |
| ITF_MEN | 979 | 10.5 | 8.9 | 19.3 | 12.9 | 18.5 | 17.2 | 12.8 | 13.99 | 48.4% | 29.9% |
| ITF_WOMEN | 1,119 | 10.5 | 6.9 | 16.4 | 15.1 | 21.1 | 18.5 | 11.6 | 15.78 | 51.2% | 30.1% |
| WTA | 229 | 17.9 | 12.7 | 35.8 | 11.8 | 18.3 | 3.5 | 0.0 | 7.39 | 21.8% | 3.5% |
| WTA125 | 60 | 11.7 | 6.7 | 15.0 | 33.3 | 20.0 | 10.0 | 3.3 | 11.83 | 33.3% | 13.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 172 | 23.8 | 14.5 | 24.4 | 15.7 | 18.0 | 2.3 | 1.2 | 6.52 | 21.5% | 3.5% |
| CHALLENGER | 614 | 9.9 | 6.3 | 18.9 | 17.3 | 16.4 | 17.3 | 13.8 | 14.68 | 47.6% | 31.1% |
| ITF_MEN | 979 | 9.3 | 5.0 | 15.7 | 17.1 | 18.8 | 18.3 | 15.8 | 15.88 | 52.9% | 34.1% |
| ITF_WOMEN | 1,119 | 8.0 | 6.1 | 13.1 | 13.9 | 19.5 | 20.5 | 18.9 | 18.8 | 58.9% | 39.4% |
| WTA | 229 | 14.8 | 6.1 | 20.5 | 17.0 | 27.9 | 13.1 | 0.4 | 13.18 | 41.5% | 13.5% |
| WTA125 | 60 | 5.0 | 3.3 | 18.3 | 25.0 | 28.3 | 8.3 | 11.7 | 13.92 | 48.3% | 20.0% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 172 | 35.5 | 11.6 | 25.0 | 10.5 | 9.9 | 7.0 | 0.6 | 5.46 | 17.4% | 7.6% |
| CHALLENGER | 614 | 16.4 | 6.3 | 19.5 | 16.9 | 15.3 | 13.7 | 11.7 | 11.99 | 40.7% | 25.4% |
| ITF_MEN | 979 | 8.9 | 9.5 | 18.3 | 14.6 | 18.3 | 17.9 | 12.6 | 14.06 | 48.7% | 30.4% |
| ITF_WOMEN | 1,119 | 10.3 | 6.6 | 17.2 | 13.8 | 23.5 | 18.2 | 10.5 | 16.38 | 52.2% | 28.7% |
| WTA | 229 | 27.9 | 10.5 | 31.4 | 14.8 | 13.1 | 2.2 | 0.0 | 6.49 | 15.3% | 2.2% |
| WTA125 | 60 | 18.3 | 3.3 | 26.7 | 30.0 | 16.7 | 5.0 | 0.0 | 10.37 | 21.7% | 5.0% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 71 | 23.9 | 22.5 | 35.2 | 11.3 | 7.0 | 0.0 | 0.0 | 6.19 | 7.0% | 0.0% |
| CHALLENGER | 736 | 21.5 | 13.6 | 26.9 | 15.1 | 13.7 | 6.5 | 2.7 | 7.41 | 23.0% | 9.2% |
| DOUBLES | 337 | 5.9 | 3.9 | 9.8 | 10.1 | 22.0 | 19.9 | 28.5 | 24.11 | 70.3% | 48.4% |
| ITF_MEN | 1,724 | 13.1 | 9.1 | 18.8 | 13.8 | 20.6 | 14.7 | 9.9 | 13.0 | 45.3% | 24.6% |
| ITF_WOMEN | 1,580 | 8.5 | 8.8 | 17.5 | 14.5 | 23.1 | 18.4 | 9.2 | 15.23 | 50.7% | 27.6% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 323 | 13.9 | 9.9 | 20.4 | 16.4 | 23.8 | 11.5 | 4.0 | 11.35 | 39.3% | 15.5% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 171 | 22.2 | 22.2 | 24.0 | 10.5 | 18.7 | 1.8 | 0.6 | 5.87 | 21.1% | 2.3% |
| CHALLENGER | 444 | 20.1 | 13.1 | 17.6 | 20.1 | 16.0 | 7.7 | 5.6 | 9.8 | 29.3% | 13.3% |
| ITF_MEN | 659 | 14.6 | 11.7 | 24.1 | 14.6 | 18.5 | 12.1 | 4.4 | 9.95 | 35.0% | 16.5% |
| ITF_WOMEN | 774 | 14.3 | 8.5 | 19.2 | 18.1 | 22.1 | 13.1 | 4.7 | 12.38 | 39.8% | 17.7% |
| WTA | 228 | 18.0 | 12.7 | 36.0 | 11.8 | 18.4 | 3.1 | 0.0 | 7.39 | 21.5% | 3.1% |
| WTA125 | 59 | 11.9 | 6.8 | 15.2 | 33.9 | 20.3 | 8.5 | 3.4 | 11.65 | 32.2% | 11.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 171 | 24.0 | 14.0 | 24.6 | 15.8 | 18.1 | 2.3 | 1.2 | 6.54 | 21.6% | 3.5% |
| CHALLENGER | 444 | 12.2 | 8.1 | 23.9 | 21.2 | 18.0 | 12.2 | 4.5 | 11.2 | 34.7% | 16.7% |
| ITF_MEN | 659 | 11.8 | 6.4 | 19.4 | 20.0 | 20.6 | 14.4 | 7.3 | 12.83 | 42.3% | 21.7% |
| ITF_WOMEN | 774 | 9.4 | 8.0 | 15.0 | 14.6 | 22.2 | 18.6 | 12.1 | 16.09 | 53.0% | 30.8% |
| WTA | 228 | 14.9 | 6.1 | 20.6 | 17.1 | 28.1 | 12.7 | 0.4 | 13.18 | 41.2% | 13.2% |
| WTA125 | 59 | 5.1 | 3.4 | 18.6 | 25.4 | 28.8 | 8.5 | 10.2 | 13.01 | 47.5% | 18.6% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 59 | 25.4 | 25.4 | 35.6 | 11.9 | 1.7 | 0.0 | 0.0 | 4.87 | 1.7% | 0.0% |
| CHALLENGER | 600 | 24.0 | 16.0 | 30.0 | 14.3 | 12.8 | 2.7 | 0.2 | 6.62 | 15.7% | 2.8% |
| DOUBLES | 256 | 6.6 | 3.5 | 9.8 | 10.2 | 22.3 | 20.7 | 26.9 | 24.02 | 69.9% | 47.7% |
| ITF_MEN | 1,206 | 16.0 | 10.9 | 22.6 | 14.8 | 20.2 | 11.7 | 3.8 | 10.17 | 35.7% | 15.5% |
| ITF_WOMEN | 1,059 | 10.3 | 10.3 | 21.3 | 16.6 | 24.1 | 14.9 | 2.5 | 12.14 | 41.4% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 255 | 15.3 | 9.0 | 25.5 | 23.5 | 19.6 | 7.1 | 0.0 | 10.01 | 26.7% | 7.1% |
| WTA125 | 244 | 16.8 | 11.1 | 24.6 | 18.9 | 21.7 | 6.6 | 0.4 | 9.32 | 28.7% | 7.0% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 337 | 5.9 | 3.9 | 9.8 | 10.1 | 22.0 | 19.9 | 28.5 | 24.11 | 70.3% | 48.4% |
| singles | 4,946 | 13.4 | 10.0 | 20.9 | 14.9 | 20.0 | 13.5 | 7.2 | 11.78 | 40.7% | 20.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 714 | 15.1 | 8.5 | 17.6 | 14.0 | 17.9 | 13.9 | 12.9 | 12.71 | 44.7% | 26.8% |
| Hard | 2,258 | 11.8 | 9.8 | 19.5 | 14.5 | 19.3 | 14.9 | 10.2 | 13.12 | 44.4% | 25.1% |
| UNKNOWN | 201 | 14.4 | 7.0 | 13.9 | 17.4 | 17.9 | 19.4 | 9.9 | 14.1 | 47.3% | 29.3% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 892 | 17.3 | 13.0 | 21.6 | 15.2 | 16.4 | 9.9 | 6.6 | 9.7 | 32.9% | 16.5% |
| B | 392 | 12.8 | 9.9 | 16.8 | 18.9 | 17.4 | 10.7 | 13.5 | 12.8 | 41.6% | 24.2% |
| C | 536 | 14.2 | 8.6 | 24.1 | 12.5 | 14.7 | 14.7 | 11.2 | 11.95 | 40.7% | 25.9% |
| D | 615 | 10.9 | 8.8 | 15.8 | 13.8 | 22.6 | 15.1 | 13.0 | 15.62 | 50.7% | 28.1% |
| F | 738 | 7.7 | 5.6 | 14.9 | 13.6 | 22.6 | 23.3 | 12.3 | 18.89 | 58.3% | 35.6% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,654 | 18.7 | 11.9 | 26.9 | 16.6 | 16.6 | 6.6 | 2.7 | 8.48 | 25.9% | 9.2% |
| B | 869 | 13.0 | 9.1 | 21.4 | 17.5 | 18.4 | 12.9 | 7.7 | 11.75 | 39.0% | 20.6% |
| C | 1,072 | 10.9 | 8.9 | 15.6 | 13.4 | 21.8 | 15.7 | 13.7 | 15.44 | 51.2% | 29.4% |
| D | 809 | 11.0 | 8.3 | 19.3 | 12.1 | 24.5 | 15.7 | 9.2 | 14.62 | 49.3% | 24.9% |
| F | 879 | 6.3 | 8.0 | 13.0 | 11.9 | 22.1 | 24.9 | 13.9 | 19.89 | 60.9% | 38.8% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,116 | 15.1 | 11.8 | 20.3 | 16.4 | 17.0 | 10.1 | 9.2 | 10.64 | 36.4% | 19.4% |
| LIMITED | 693 | 15.9 | 10.0 | 23.1 | 13.6 | 14.0 | 13.6 | 10.0 | 10.36 | 37.5% | 23.5% |
| POOR | 1,364 | 9.2 | 7.0 | 15.2 | 13.6 | 22.9 | 19.6 | 12.5 | 17.41 | 55.0% | 32.1% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 325 | 34.8 | 23.1 | 32.9 | 5.8 | 2.5 | 0.9 | 0.0 | 4.14 | 3.4% | 0.9% |
| GAME_SPREAD | 394 | 20.3 | 16.5 | 36.3 | 16.0 | 9.1 | 1.3 | 0.5 | 6.5 | 10.9% | 1.8% |
| MATCH_WINNER | 5,283 | 12.9 | 9.6 | 20.2 | 14.6 | 20.1 | 13.9 | 8.6 | 12.23 | 42.6% | 22.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,686 | 21.9 | 13.5 | 29.9 | 17.4 | 13.8 | 2.8 | 0.7 | 7.06 | 17.2% | 3.4% |
| TOTAL_GAMES | 1,120 | 9.9 | 9.0 | 26.2 | 25.2 | 17.1 | 8.0 | 4.5 | 10.68 | 29.6% | 12.5% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 658 | 29.6 | 31.3 | 27.7 | 0.9 | 8.7 | 1.7 | 0.1 | 4.29 | 10.5% | 1.8% |
| GAME_SPREAD | 396 | 37.9 | 12.1 | 23.7 | 21.2 | 3.0 | 1.5 | 0.5 | 4.95 | 5.1% | 2.0% |
| TOTAL_GAMES | 717 | 4.0 | 3.9 | 35.7 | 37.8 | 12.3 | 1.8 | 4.5 | 10.51 | 18.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 658 | 24.0 | 18.1 | 34.0 | 8.7 | 10.3 | 4.0 | 0.9 | 5.79 | 15.2% | 4.9% |
| GAME_SPREAD | 396 | 17.7 | 11.4 | 24.0 | 22.2 | 17.2 | 5.8 | 1.8 | 9.62 | 24.8% | 7.6% |
| TOTAL_GAMES | 719 | 5.0 | 4.2 | 33.5 | 33.2 | 13.9 | 5.4 | 4.7 | 10.91 | 24.1% | 10.2% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 3,173 | 44.6% | 25.8% | 13.06 | 33.1% | 13.8% | 9.98 |
| gen1_elo | 3,173 | 43.8% | 25.1% | 12.73 | 32.0% | 14.1% | 9.6 |
| gen1_sr | 3,173 | 53.2% | 32.5% | 16.3 | 43.9% | 20.9% | 13.19 |
| gen2 | 3,173 | 51.4% | 32.0% | 15.49 | 42.9% | 21.5% | 13.07 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,343 | 16.5 | 12.8 | 23.0 | 15.5 | 19.2 | 9.8 | 3.3 | 9.49 | 32.2% | 13.0% |
| STALE | 1,830 | 10.0 | 6.8 | 15.6 | 13.9 | 18.6 | 18.7 | 16.3 | 16.92 | 53.7% | 35.1% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 2,958 | 14.8 | 10.3 | 21.8 | 15.8 | 20.1 | 12.4 | 4.7 | 10.85 | 37.2% | 17.1% |
| STALE | 2,325 | 10.6 | 8.7 | 18.1 | 13.2 | 20.0 | 15.8 | 13.5 | 14.76 | 49.4% | 29.3% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 8,456 | 0 | 4301 | 4155 | 29.1 | 142.2 | 1400.4 |
| ge_15pp | 3,666 | 0 | 1535 | 2131 | 34.1 | 418.5 | 1380.4 |
| ge_25pp | 2,006 | 0 | 682 | 1324 | 44.0 | 597.1 | 1380.4 |
| lt_10pp | 3,555 | 0 | 2092 | 1463 | 27.8 | 53.8 | 1102.2 |

Current slate `SL-20260930T230839Z-f33aa325`: 306 priced rows, quote age at build {'median': 39.4, 'max': 57.9}, freshness {'STALE': 306}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 102 | 19.6 | 12.8 | 21.6 | 22.6 | 21.6 | 2.0 | 0.0 | 7.76 | 23.5% | 2.0% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 11 | 0.0 | 0.0 | 9.1 | 45.5 | 45.5 | 0.0 | 0.0 | 13.64 | 45.5% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 3,173 | 122 (3.8%) | 9.0% | 0.0% | {"EXTERNAL_STALE": 102, "AGREES_WITH_KALSHI": 11, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 1,416 | 29 (2.1%) | 17.2% | 0.0% | {"EXTERNAL_STALE": 24, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 817 | 2 (0.2%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 2} |
| fair_v1_ge_25pp_pregame_clean | 323 | 2 (0.6%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 2} |
| fair_v1_lt_10pp | 1,295 | 65 (5.0%) | 1.5% | 0.0% | {"EXTERNAL_STALE": 55, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 638 | 13.2 | 7.7 | 16.9 | 15.5 | 21.3 | 15.4 | 10.0 | 13.77 | 46.7% | 25.4% |
| 4-10x | 468 | 12.8 | 9.4 | 17.7 | 14.5 | 18.8 | 14.1 | 12.6 | 13.36 | 45.5% | 26.7% |
| <2x | 1,668 | 13.6 | 10.6 | 20.4 | 14.9 | 17.3 | 13.2 | 10.1 | 11.67 | 40.6% | 23.3% |
| >=10x | 399 | 8.5 | 6.8 | 16.0 | 11.5 | 21.8 | 22.6 | 12.8 | 18.88 | 57.1% | 35.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 761 | 12.9 | 8.5 | 21.8 | 15.5 | 17.9 | 12.1 | 11.3 | 12.12 | 41.3% | 23.4% |
| 300-1000 | 786 | 14.1 | 8.5 | 17.7 | 15.5 | 19.2 | 15.3 | 9.7 | 13.44 | 44.1% | 24.9% |
| <300 | 900 | 8.2 | 6.6 | 14.9 | 11.8 | 22.3 | 21.9 | 14.3 | 18.98 | 58.6% | 36.2% |
| >=3000 | 726 | 16.7 | 14.5 | 21.5 | 16.0 | 15.3 | 8.9 | 7.2 | 9.46 | 31.4% | 16.1% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 131 | 0.5245 | 0.3921 | 0.4427 | +0.082 | -0.051 | 0.012 ± 0.0131 |
| ratio 4-10x | 102 | 0.5789 | 0.445 | 0.5 | +0.079 | -0.055 | 0.0086 ± 0.0144 |
| ratio <2x | 254 | 0.536 | 0.4174 | 0.4803 | +0.056 | -0.063 | 0.0068 ± 0.0081 |
| ratio >=10x | 94 | 0.5328 | 0.3615 | 0.4468 | +0.086 | -0.085 | 0.0173 ± 0.0198 |
| thinner_sample 1000-3000 | 131 | 0.5585 | 0.4427 | 0.4885 | +0.070 | -0.046 | -0.0024 ± 0.0113 |
| thinner_sample 300-1000 | 163 | 0.5515 | 0.4254 | 0.5153 | +0.036 | -0.090 | -0.0037 ± 0.011 |
| thinner_sample <300 | 217 | 0.5327 | 0.3712 | 0.4378 | +0.095 | -0.067 | 0.0245 ± 0.0118 |
| thinner_sample >=3000 | 70 | 0.5046 | 0.4124 | 0.4286 | +0.076 | -0.016 | 0.0197 ± 0.0122 |
| data_status ADEQUATE | 135 | 0.527 | 0.4227 | 0.4593 | +0.068 | -0.037 | 0.0059 ± 0.0099 |
| data_status LIMITED | 127 | 0.567 | 0.4531 | 0.5354 | +0.032 | -0.082 | -0.0052 ± 0.012 |
| data_status POOR | 319 | 0.5355 | 0.3829 | 0.4483 | +0.087 | -0.065 | 0.0177 ± 0.0092 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 97 | 0.1825 | 0.1845 | -0.0019 ± 0.0016 | 0.5414 | 0.5464 | 0.4946 | 0.4796 | 0.5155 | -0.090 ± 0.0477 | -0.01 (3) |
| 3-5 | 64 | 0.1673 | 0.1663 | +0.0009 ± 0.0043 | 0.5107 | 0.5054 | 0.5401 | 0.4991 | 0.5 | -0.096 ± 0.0546 | 0.02 (1) |
| 5-10 | 119 | 0.1985 | 0.205 | -0.0065 ± 0.0063 | 0.5796 | 0.5916 | 0.5257 | 0.4506 | 0.5378 | -0.043 ± 0.0423 | -0.02 (1) |
| 10-15 | 96 | 0.2176 | 0.2141 | +0.0035 ± 0.0119 | 0.6218 | 0.6119 | 0.5222 | 0.3973 | 0.4479 | -0.071 ± 0.0475 | -0.0633 (3) |
| 15-25 | 122 | 0.2088 | 0.2066 | +0.0022 ± 0.0159 | 0.6025 | 0.5908 | 0.5542 | 0.3588 | 0.459 | -0.018 ± 0.0391 | -0.015 (2) |
| 25-40 | 68 | 0.2385 | 0.1851 | +0.0533 ± 0.0328 | 0.6675 | 0.5431 | 0.6053 | 0.2866 | 0.3529 | -0.073 ± 0.05 | -0.01 (1) |
| 40+ | 15 | 0.3032 | 0.1389 | +0.1644 ± 0.0887 | 0.789 | 0.4359 | 0.6646 | 0.2177 | 0.2667 | -0.071 ± 0.086 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 233 | 0.177 | 0.178 | -0.0010 ± 0.001 | 0.5271 | 0.529 | 0.5129 | 0.4977 | 0.5365 | -0.039 ± 0.029 | -0.0188 (8) |
| 3-5 | 170 | 0.1764 | 0.1748 | +0.0016 ± 0.0026 | 0.5305 | 0.5208 | 0.4925 | 0.4522 | 0.4471 | -0.066 ± 0.0334 | 0.02 (1) |
| 5-10 | 340 | 0.1817 | 0.1885 | -0.0068 ± 0.0035 | 0.5396 | 0.5503 | 0.482 | 0.4082 | 0.4971 | +0.015 ± 0.0236 | -0.015 (2) |
| 10-15 | 272 | 0.1831 | 0.1712 | +0.0119 ± 0.0063 | 0.5439 | 0.5036 | 0.463 | 0.3383 | 0.3529 | -0.054 ± 0.025 | -0.0633 (3) |
| 15-25 | 401 | 0.1861 | 0.1548 | +0.0312 ± 0.0078 | 0.5569 | 0.4601 | 0.4655 | 0.2685 | 0.2893 | -0.040 ± 0.0192 | -0.02 (3) |
| 25-40 | 405 | 0.2138 | 0.0853 | +0.1285 ± 0.0092 | 0.6199 | 0.2854 | 0.4903 | 0.1698 | 0.1309 | -0.084 ± 0.014 | -0.01 (1) |
| 40+ | 288 | 0.3573 | 0.0337 | +0.3236 ± 0.0113 | 0.9236 | 0.1447 | 0.6054 | 0.0926 | 0.0417 | -0.076 ± 0.01 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 56 | 0.1669 | 0.1695 | -0.0027 ± 0.0017 | 0.5056 | 0.5115 | 0.4925 | 0.4781 | 0.5714 | -0.021 ± 0.0534 | -0.01 (1) |
| 3-5 | 39 | 0.2377 | 0.2363 | +0.0013 ± 0.0064 | 0.6549 | 0.6558 | 0.5009 | 0.4615 | 0.4615 | -0.093 ± 0.0842 | 0.02 (1) |
| 5-10 | 111 | 0.1872 | 0.1834 | +0.0038 ± 0.0062 | 0.5583 | 0.5458 | 0.563 | 0.487 | 0.4865 | -0.120 ± 0.0417 | -0.01 (3) |
| 10-15 | 109 | 0.2033 | 0.1977 | +0.0055 ± 0.0107 | 0.5871 | 0.5762 | 0.5826 | 0.4583 | 0.5046 | -0.060 ± 0.0445 | -0.0667 (3) |
| 15-25 | 144 | 0.2241 | 0.2107 | +0.0134 ± 0.0151 | 0.6372 | 0.5984 | 0.578 | 0.3804 | 0.4514 | -0.060 ± 0.0392 | -0.01 (1) |
| 25-40 | 84 | 0.2689 | 0.1749 | +0.0939 ± 0.0285 | 0.7401 | 0.5181 | 0.6439 | 0.3326 | 0.3333 | -0.165 ± 0.0467 | -0.02 (1) |
| 40+ | 38 | 0.3579 | 0.2157 | +0.1421 ± 0.0757 | 0.9912 | 0.6263 | 0.747 | 0.2555 | 0.3684 | +0.007 ± 0.0695 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 180 | 0.1392 | 0.1413 | -0.0021 ± 0.001 | 0.4327 | 0.4381 | 0.524 | 0.5094 | 0.5722 | +0.003 ± 0.0273 | -0.0217 (6) |
| 3-5 | 95 | 0.1736 | 0.1737 | -0.0001 ± 0.0035 | 0.5079 | 0.5105 | 0.5465 | 0.5062 | 0.5263 | -0.040 ± 0.0443 | 0.02 (1) |
| 5-10 | 314 | 0.1946 | 0.1974 | -0.0027 ± 0.0038 | 0.5739 | 0.5726 | 0.5253 | 0.45 | 0.5032 | -0.013 ± 0.0253 | -0.01 (4) |
| 10-15 | 324 | 0.1789 | 0.172 | +0.0069 ± 0.0057 | 0.5331 | 0.5086 | 0.5142 | 0.3899 | 0.4321 | -0.021 ± 0.0236 | -0.0575 (4) |
| 15-25 | 393 | 0.197 | 0.1632 | +0.0338 ± 0.0081 | 0.5802 | 0.4827 | 0.5004 | 0.305 | 0.3257 | -0.053 ± 0.0205 | -0.01 (1) |
| 25-40 | 414 | 0.2275 | 0.1021 | +0.1254 ± 0.01 | 0.6549 | 0.3262 | 0.5258 | 0.209 | 0.1739 | -0.094 ± 0.016 | -0.02 (1) |
| 40+ | 389 | 0.395 | 0.0602 | +0.3348 ± 0.0144 | 1.0388 | 0.2159 | 0.6522 | 0.1165 | 0.0823 | -0.064 ± 0.0119 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 90 | 0.1615 | 0.1641 | -0.0026 ± 0.0015 | 0.4907 | 0.497 | 0.531 | 0.5171 | 0.5556 | -0.062 ± 0.0424 | 0.0 (3) |
| 3-5 | 60 | 0.1689 | 0.1676 | +0.0013 ± 0.0043 | 0.5095 | 0.5061 | 0.5382 | 0.4992 | 0.5 | -0.130 ± 0.0584 | -- (0) |
| 5-10 | 114 | 0.2013 | 0.204 | -0.0028 ± 0.0062 | 0.5899 | 0.591 | 0.5243 | 0.4538 | 0.5175 | -0.043 ± 0.0425 | -0.01 (2) |
| 10-15 | 112 | 0.2235 | 0.2256 | -0.0021 ± 0.0112 | 0.6391 | 0.6377 | 0.551 | 0.4263 | 0.5089 | -0.051 ± 0.0449 | -0.05 (4) |
| 15-25 | 119 | 0.2061 | 0.2057 | +0.0003 ± 0.0157 | 0.6032 | 0.5902 | 0.5739 | 0.3812 | 0.479 | -0.029 ± 0.0396 | -0.03 (1) |
| 25-40 | 73 | 0.2399 | 0.1836 | +0.0563 ± 0.0319 | 0.6754 | 0.5397 | 0.5957 | 0.279 | 0.3425 | -0.074 ± 0.0485 | 0.0 (1) |
| 40+ | 13 | 0.3177 | 0.1578 | +0.1599 ± 0.1041 | 0.8214 | 0.4818 | 0.6902 | 0.2304 | 0.3077 | -0.055 ± 0.0988 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 218 | 0.1647 | 0.1653 | -0.0006 ± 0.001 | 0.499 | 0.4999 | 0.5378 | 0.5233 | 0.5321 | -0.063 ± 0.0278 | -0.015 (8) |
| 3-5 | 150 | 0.1891 | 0.1875 | +0.0015 ± 0.0028 | 0.5545 | 0.5504 | 0.5204 | 0.4813 | 0.48 | -0.082 ± 0.0366 | -- (0) |
| 5-10 | 343 | 0.1783 | 0.1765 | +0.0018 ± 0.0034 | 0.5359 | 0.5182 | 0.477 | 0.4046 | 0.4344 | -0.028 ± 0.0228 | -0.01 (2) |
| 10-15 | 298 | 0.196 | 0.1829 | +0.0132 ± 0.0062 | 0.5759 | 0.5325 | 0.4861 | 0.362 | 0.3758 | -0.061 ± 0.0247 | -0.042 (5) |
| 15-25 | 433 | 0.1749 | 0.1444 | +0.0306 ± 0.0072 | 0.5344 | 0.4367 | 0.4719 | 0.2747 | 0.2979 | -0.038 ± 0.0178 | -0.03 (2) |
| 25-40 | 399 | 0.2167 | 0.0932 | +0.1235 ± 0.0098 | 0.6275 | 0.3029 | 0.4925 | 0.171 | 0.1404 | -0.077 ± 0.0149 | 0.0 (1) |
| 40+ | 268 | 0.3736 | 0.034 | +0.3396 ± 0.0125 | 0.9734 | 0.1461 | 0.6097 | 0.0915 | 0.0336 | -0.083 ± 0.0102 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 370 | 0.2067 | 0.2066 | +0.0001 ± 0.0008 | 0.5956 | 0.5956 | 0.5076 | 0.4929 | 0.4865 | -0.051 ± 0.0237 | -0.0226 (46) |
| 3-5 | 273 | 0.1934 | 0.1938 | -0.0004 ± 0.0021 | 0.5676 | 0.5652 | 0.4657 | 0.4258 | 0.4542 | -0.024 ± 0.0265 | -0.0059 (32) |
| 5-10 | 581 | 0.1876 | 0.1829 | +0.0047 ± 0.0027 | 0.5584 | 0.5453 | 0.4649 | 0.3917 | 0.3976 | -0.041 ± 0.0178 | -0.0049 (70) |
| 10-15 | 381 | 0.2019 | 0.1885 | +0.0134 ± 0.0056 | 0.5919 | 0.5551 | 0.4519 | 0.3284 | 0.336 | -0.045 ± 0.0221 | 0.002 (61) |
| 15-25 | 512 | 0.2342 | 0.2096 | +0.0246 ± 0.0079 | 0.6614 | 0.6054 | 0.5308 | 0.3374 | 0.3711 | -0.031 ± 0.0202 | -0.0216 (58) |
| 25-40 | 251 | 0.2624 | 0.1673 | +0.0951 ± 0.0162 | 0.7248 | 0.5043 | 0.5678 | 0.2561 | 0.259 | -0.061 ± 0.0256 | -0.0216 (25) |
| 40+ | 90 | 0.4349 | 0.1592 | +0.2757 ± 0.0452 | 1.223 | 0.4921 | 0.7344 | 0.2252 | 0.2333 | -0.065 ± 0.044 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 672 | 0.1982 | 0.1976 | +0.0005 ± 0.0006 | 0.5761 | 0.5744 | 0.501 | 0.4862 | 0.4673 | -0.062 ± 0.0171 | -0.0155 (82) |
| 3-5 | 496 | 0.1992 | 0.1986 | +0.0006 ± 0.0016 | 0.5786 | 0.5743 | 0.4729 | 0.4329 | 0.4456 | -0.034 ± 0.02 | -0.018 (54) |
| 5-10 | 1042 | 0.1857 | 0.1794 | +0.0062 ± 0.002 | 0.5544 | 0.5352 | 0.4497 | 0.3759 | 0.3752 | -0.043 ± 0.0133 | -0.0089 (119) |
| 10-15 | 759 | 0.1963 | 0.1815 | +0.0149 ± 0.0039 | 0.5774 | 0.5366 | 0.4445 | 0.3208 | 0.3228 | -0.044 ± 0.0153 | -0.0051 (95) |
| 15-25 | 1048 | 0.2227 | 0.1879 | +0.0347 ± 0.0053 | 0.6411 | 0.551 | 0.5054 | 0.3095 | 0.3187 | -0.043 ± 0.0134 | -0.0255 (106) |
| 25-40 | 731 | 0.2454 | 0.129 | +0.1164 ± 0.0084 | 0.6918 | 0.403 | 0.5279 | 0.2122 | 0.1874 | -0.070 ± 0.0132 | -0.0206 (47) |
| 40+ | 442 | 0.3936 | 0.0836 | +0.3100 ± 0.0149 | 1.0765 | 0.2789 | 0.656 | 0.1407 | 0.1086 | -0.076 ± 0.0141 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 581 | 1.212 ± 0.127 | 1.285 | 0.1641 | 0.1814 | 0.2051 | 0.1951 |
| gen2 | 581 | 0.951 ± 0.108 | 1.195 | 0.1828 | 0.1801 | 0.2238 | 0.1959 |
| gen1_elo | 581 | 1.174 ± 0.123 | 1.248 | 0.1717 | 0.1815 | 0.2045 | 0.195 |
| gen1_sr | 581 | 1.186 ± 0.141 | 1.229 | 0.1402 | 0.1822 | 0.2216 | 0.1952 |
| gen1_ledger | 2458 | 0.9 ± 0.055 | 1.075 | 0.161 | 0.1996 | 0.2197 | 0.1916 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 3,666)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,123 | 30.6% |
| STALE_QUOTE | market_freshness | 977 | 26.7% |
| POOR_DATA | data | 325 | 8.9% |
| BOOK_QUALITY | execution | 273 | 7.4% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 255 | 7.0% |
| LIMITED_DATA | data | 245 | 6.7% |
| IN_PLAY_QUOTE | market_freshness/coverage | 206 | 5.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 184 | 5.0% |
| IDENTITY_AMBIGUOUS | mapping | 75 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 30.6%, market_freshness 26.7%, data 15.6%, market_freshness/coverage 12.6%, execution 7.4%, model_calibration_or_unknown 5.0%, mapping 2.1%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.8%, LOW_DATA_QUALITY 66.6%, STALE_KALSHI_QUOTE 58.1%, STALE_PLAYER_DATA 57.6%, THIN_PLAYER_HISTORY 53.8%, MODEL_INTERNAL_DISAGREEMENT 32.5%, ASYMMETRIC_SAMPLE_SIZE 29.8%, WIDE_SPREAD 16.4%, PLAYER_IDENTITY_RISK 12.1%, MODEL_HIGH_UNCERTAINTY 10.0%, LEVEL_TRANSFER_RISK 9.6%, EVENT_MAPPING_RISK 7.8%, LOW_DISPLAYED_LIQUIDITY 4.4%, MODEL_CALIBRATION_OUTLIER 2.0%, UNKNOWN 0.9%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 33.8%, POST_SETTLEMENT_OBSERVATION 30.6%, POSSIBLE_IN_PLAY_QUOTE 7.9%, CONFIRMED_IN_PLAY_QUOTE 3.0%

### >= ge_25 pp (N = 2,006)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 882 | 44.0% |
| STALE_QUOTE | market_freshness | 449 | 22.4% |
| POOR_DATA | data | 142 | 7.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 126 | 6.3% |
| BOOK_QUALITY | execution | 125 | 6.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 120 | 6.0% |
| LIMITED_DATA | data | 72 | 3.6% |
| IDENTITY_AMBIGUOUS | mapping | 56 | 2.8% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 34 | 1.7% |

Cause class: coverage 44.0%, market_freshness 22.4%, market_freshness/coverage 12.3%, data 10.7%, execution 6.2%, mapping 2.8%, model_calibration_or_unknown 1.7%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 97.7%, LOW_DATA_QUALITY 71.4%, STALE_KALSHI_QUOTE 66.0%, THIN_PLAYER_HISTORY 56.9%, STALE_PLAYER_DATA 56.6%, MODEL_INTERNAL_DISAGREEMENT 33.1%, ASYMMETRIC_SAMPLE_SIZE 32.3%, PLAYER_IDENTITY_RISK 15.3%, WIDE_SPREAD 14.3%, MODEL_HIGH_UNCERTAINTY 11.1%, EVENT_MAPPING_RISK 9.5%, LEVEL_TRANSFER_RISK 9.3%, LOW_DISPLAYED_LIQUIDITY 4.3%, MODEL_CALIBRATION_OUTLIER 2.7%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 47.4%, POST_SETTLEMENT_OBSERVATION 44.0%, POSSIBLE_IN_PLAY_QUOTE 7.3%, CONFIRMED_IN_PLAY_QUOTE 3.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 1671, "IDENTITY_AMBIGUOUS": 335}; ticker orientation: {"VERIFIED": 2006}.

Checks: discipline:AMBIGUOUS 163, discipline:PASS 1843, identity_confidence:AMBIGUOUS 308, identity_confidence:PASS 1698, level_mapping:NA 175, level_mapping:PASS 1831, market_pair:AMBIGUOUS 55, market_pair:NA 52, market_pair:PASS 1899, model_complement:NA 28, model_complement:PASS 1978, namesake:PASS 2006, physical_match_id:NA 1189, physical_match_id:PASS 817, player_ids:PASS 2006, same_pair_other_event:PASS 2006, ticker_orientation:PASS 2006

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 243 | 1.7% | 1.7% | 0.2% | {"market_freshness": 4} | 5.86 | 0.1838 / 0.1834 (45) | 33.7% | 0.0% | 0.8% | 5.3% |
| CHALLENGER | 1,350 | 17.4% | 7.3% | 11.7% | {"coverage": 127, "market_freshness": 49, "market_freshness/coverage": 32, "data": 13, "model_calibration_or_unknown": 11, "execution": 3} | 7.35 | 0.2197 / 0.1998 (482) | 50.1% | 4.5% | 0.8% | 22.7% |
| DOUBLES | 337 | 48.4% | 47.7% | 8.1% | {"market_freshness": 77, "market_freshness/coverage": 36, "execution": 25, "mapping": 20, "coverage": 5} | 24.02 | 0.3236 / 0.2197 (143) | 58.8% | 0.0% | 100.0% | 24.0% |
| ITF_MEN | 2,703 | 26.6% | 15.9% | 35.8% | {"coverage": 356, "market_freshness": 145, "data": 82, "market_freshness/coverage": 66, "execution": 60, "mapping": 8, "model_calibration_or_unknown": 1} | 10.03 | 0.2129 / 0.1849 (1061) | 51.2% | 53.1% | 6.0% | 31.0% |
| ITF_WOMEN | 2,699 | 28.6% | 17.5% | 38.5% | {"coverage": 382, "market_freshness": 156, "data": 102, "market_freshness/coverage": 70, "execution": 28, "mapping": 26, "model_calibration_or_unknown": 9} | 12.21 | 0.2078 / 0.1915 (950) | 54.1% | 56.5% | 7.3% | 32.1% |
| OTHER | 149 | 8.1% | 7.3% | 0.6% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 592 | 7.3% | 5.2% | 2.1% | {"market_freshness/coverage": 14, "data": 9, "market_freshness": 8, "execution": 4, "coverage": 4, "model_calibration_or_unknown": 3, "mapping": 1} | 8.47 | 0.1995 / 0.1973 (113) | 31.4% | 3.5% | 2.0% | 18.4% |
| WTA125 | 383 | 15.1% | 7.9% | 2.9% | {"market_freshness/coverage": 27, "model_calibration_or_unknown": 8, "market_freshness": 8, "data": 8, "coverage": 7} | 10.36 | 0.2317 / 0.2049 (203) | 33.4% | 9.9% | 0.5% | 20.9% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 2 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 3 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 4 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 5 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 596 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 6 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 7 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 8 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 9 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 11 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 12 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 13 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 14 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 15 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 16 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 17 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 18 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 19 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 20 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 21 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 22 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 23 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 24 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 25 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 26 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 27 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 28 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 29 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 30 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 31 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 32 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 33 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 34 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 35 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 36 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 37 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 220 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 38 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |
| 39 | `KXATPCHALLENGERDOUBLES-26SEP17ARESTEBLASCH-BLASCH` | DOUBLES | gen1_ledger | 95% / 28% | +67 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 79 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 40 | `KXITFWMATCH-26SEP24BOUKUR-BOU` | ITF_WOMEN | gen1_ledger | 76% / 8% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 1497.0, ratio 2.48); no external reference |
| 41 | `KXATPCHALLENGERMATCH-26SEP28TABSAN-SAN` | CHALLENGER | gen1_ledger | 70% / 4% | +67 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 48 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26SEP22SHCPAS-PAS` | ITF_WOMEN | gen1_ledger | 69% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 199 min (STALE); data POOR (grade F, thinner serve sample 239.0, ratio 5.93); no external reference |
| 43 | `KXWTADOUBLES-26SEP20DETKHRPRETAR-PRETAR` | DOUBLES | gen1_ledger | 84% / 18% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | first-ball truth shows the match under way at the quote time; quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 44 | `KXITFWMATCH-26SEP29KRURAY-KRU` | ITF_WOMEN | fair_v1 | 78% / 12% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 126 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 223.0); no external reference |
| 45 | `KXITFWMATCH-26SEP30BIOKRO-KRO` | ITF_WOMEN | fair_v1 | 68% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 743 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 3.24); no external reference |
| 46 | `KXITFMATCH-26SEP12EFSMOR-MOR` | ITF_MEN | gen1_ledger | 67% / 2% | +66 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 36 min (STALE); data LIMITED (grade B, thinner serve sample 3783.0, ratio 1.33); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26SEP17TROUCHBAYKAD-TROUCH` | DOUBLES | gen1_ledger | 87% / 21% | +66 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 38 min before settlement (in-play print); quote age at model time 21 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26SEP30BRAKUH-BRA` | ITF_WOMEN | fair_v1 | 82% / 16% | +65 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 49 | `KXITFMATCH-26SEP23BAKBAL-BAK` | ITF_MEN | gen1_ledger | 69% / 4% | +65 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 29 min (AGING); data POOR (grade F, thinner serve sample 89.0, ratio 20.62); no external reference |
| 50 | `KXITFMATCH-26SEP16BASTAB-BAS` | ITF_MEN | gen1_ledger | 86% / 20% | +65 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 115 min (STALE); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9765, "by_level_share_of_ge_25pp": {"ATP": 0.002, "CHALLENGER": 0.1171, "DOUBLES": 0.0813, "ITF_MEN": 0.3579, "ITF_WOMEN": 0.3853, "OTHER": 0.006, "WTA": 0.0214, "WTA125": 0.0289}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.66, "share_primary_cause_market_settled_or_in_play": 0.5623, "share_primary_cause_stale_quote_only": 0.2238}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2006, "identity_ambiguous_share": 0.167, "ticker_orientation": {"VERIFIED": 2006}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 817, "with_external": 2, "coverage": 0.0024, "external_status": {"EXTERNAL_STALE": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 2}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 323, "with_external": 2, "coverage": 0.0062, "external_status": {"EXTERNAL_STALE": 2}, "triangulation": {"INSUFFICIENT_INPUTS": 2}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 664.0, "median_sample_ratio": 2.49, "median_min_matches": 24.0, "median_max_days_since_last": 173.0, "share_severe_asymmetry": 0.1765, "data_status": {"POOR": 991, "LIMITED": 710, "ADEQUATE": 305}, "comparison_lt_10pp": {"median_thinner_serve_points": 2045.0, "median_sample_ratio": 1.7, "median_min_matches": 81.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 131, "model_minus_observed": 0.0818, "kalshi_minus_observed": -0.0506, "brier_diff_model_minus_kalshi": 0.012}, "4-10x": {"n": 102, "model_minus_observed": 0.0789, "kalshi_minus_observed": -0.055, "brier_diff_model_minus_kalshi": 0.0086}, "<2x": {"n": 254, "model_minus_observed": 0.0557, "kalshi_minus_observed": -0.063, "brier_diff_model_minus_kalshi": 0.0068}, ">=10x": {"n": 94, "model_minus_observed": 0.086, "kalshi_minus_observed": -0.0853, "brier_diff_model_minus_kalshi": 0.0173}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 581, "model": {"intercept": -0.589, "slope": 0.951, "slope_se": 0.108}, "kalshi_mid_same_rows": {"intercept": 0.276, "slope": 1.195, "slope_se": 0.119}, "mean_extremity_model": 0.1828, "mean_extremity_kalshi": 0.1801, "model_brier": 0.2238, "kalshi_brier": 0.1959, "brier_diff_model_minus_kalshi": 0.0278, "brier_diff_se": 0.008, "model_logloss": 0.6393, "kalshi_logloss": 0.5699}, "fair_v1": {"n": 581, "model": {"intercept": -0.371, "slope": 1.212, "slope_se": 0.127}, "kalshi_mid_same_rows": {"intercept": 0.427, "slope": 1.285, "slope_se": 0.124}, "mean_extremity_model": 0.1641, "mean_extremity_kalshi": 0.1814, "model_brier": 0.2051, "kalshi_brier": 0.1951, "brier_diff_model_minus_kalshi": 0.01, "brier_diff_se": 0.0062, "model_logloss": 0.5931, "kalshi_logloss": 0.5681}, "gen1_elo": {"n": 581, "model": {"intercept": -0.375, "slope": 1.174, "slope_se": 0.123}, "kalshi_mid_same_rows": {"intercept": 0.407, "slope": 1.248, "slope_se": 0.12}, "mean_extremity_model": 0.1717, "mean_extremity_kalshi": 0.1815, "model_brier": 0.2045, "kalshi_brier": 0.195, "brier_diff_model_minus_kalshi": 0.0095, "brier_diff_se": 0.0062, "model_logloss": 0.5944, "kalshi_logloss": 0.5676}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2575, "share_ge_15": 0.4463, "median_abs_gap": 13.06, "n": 3173}, "gen1_elo": {"share_ge_25": 0.2509, "share_ge_15": 0.4378, "median_abs_gap": 12.73, "n": 3173}, "gen1_sr": {"share_ge_25": 0.3249, "share_ge_15": 0.5323, "median_abs_gap": 16.3, "n": 3173}, "gen2": {"share_ge_25": 0.3199, "share_ge_15": 0.5137, "median_abs_gap": 15.49, "n": 3173}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1383, "share_ge_15": 0.331, "median_abs_gap": 9.98, "n": 2335}, "gen1_elo": {"share_ge_25": 0.1405, "share_ge_15": 0.3203, "median_abs_gap": 9.6, "n": 2335}, "gen1_sr": {"share_ge_25": 0.2086, "share_ge_15": 0.4385, "median_abs_gap": 13.19, "n": 2335}, "gen2": {"share_ge_25": 0.215, "share_ge_15": 0.4291, "median_abs_gap": 13.07, "n": 2335}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.86, "share_ge_25_all": 0.0165, "share_ge_25_pregame_clean": 0.0174}, "WTA": {"median_abs_gap_pregame_clean": 8.47, "share_ge_25_all": 0.0726, "share_ge_25_pregame_clean": 0.0518}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2237, "share_within_10pp_all": 0.4204, "share_within_10pp_pregame_clean": 0.5006, "corr_model_vs_mid_pregame_clean": 0.8282}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 97, "model_brier": 0.1825, "kalshi_brier": 0.1845, "brier_diff_model_minus_kalshi": -0.0019}, "10-15": {"n_settled": 96, "model_brier": 0.2176, "kalshi_brier": 0.2141, "brier_diff_model_minus_kalshi": 0.0035}, "15-25": {"n_settled": 122, "model_brier": 0.2088, "kalshi_brier": 0.2066, "brier_diff_model_minus_kalshi": 0.0022}, "25-40": {"n_settled": 68, "model_brier": 0.2385, "kalshi_brier": 0.1851, "brier_diff_model_minus_kalshi": 0.0533}, "3-5": {"n_settled": 64, "model_brier": 0.1673, "kalshi_brier": 0.1663, "brier_diff_model_minus_kalshi": 0.0009}, "40+": {"n_settled": 15, "model_brier": 0.3032, "kalshi_brier": 0.1389, "brier_diff_model_minus_kalshi": 0.1644}, "5-10": {"n_settled": 119, "model_brier": 0.1985, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": -0.0065}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%)
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap).
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 143, "model_brier": 0.3236, "kalshi_brier": 0.2197, "brier_diff_model_minus_kalshi": 0.1038, "brier_diff_se": 0.0277, "corr_model_outcome": -0.059, "corr_kalshi_outcome": 0.3814}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
