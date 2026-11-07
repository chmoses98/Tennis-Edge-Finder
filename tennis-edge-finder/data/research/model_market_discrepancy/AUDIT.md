# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-07T14:35Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 81,547): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.83 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.7%, doubles 6.8%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,688): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.5%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.2%, market_freshness 19.4%, execution 17.5%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,688 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.8% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 491.5 points vs 1732.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.025, Gen-2 0.82, Gen-1 ledger 0.864 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 902 model 0.223 vs Kalshi 0.2055; n 187 model 0.298 vs Kalshi 0.1745.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 345,616 model-market comparisons (566,318 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 115,171 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-07T14:17:28.419926+00:00'], shadow board 93,662 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-07T14:17:31.748277+00:00'], Model 4 42,561 rows, 28,759 settled tickers, 10,798 tickers with an external scan.
* By model: {"gen1_ledger": 77575, "gen1_elo": 47071, "fair_v1": 47071, "gen2": 47071, "gen1_sr": 47071, "model4_fundamental": 39920, "model4_conditioned": 39837}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 81,547 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.83 | 40.8% | 21.7% |
| MW fair_v1 | 47,071 | 12.9 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 9.9 | 13.03 | 44.4% | 24.7% |
| MW gen1_elo | 47,071 | 12.6 | 8.9 | 19.2 | 15.3 | 19.5 | 14.6 | 9.8 | 12.82 | 44.0% | 24.4% |
| MW gen1_ledger | 34,476 | 15.7 | 10.9 | 22.2 | 15.1 | 18.4 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 47,071 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.6 | 15.8 | 52.0% | 31.3% |
| MW gen2 | 47,071 | 11.0 | 7.6 | 16.6 | 13.7 | 19.6 | 17.7 | 13.7 | 15.45 | 51.0% | 31.4% |
| all families model4_conditioned | 39,837 | 22.2 | 18.0 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,920 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.61 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,958 | 28.5 | 15.7 | 27.5 | 13.5 | 10.6 | 3.6 | 0.6 | 5.77 | 14.8% | 4.2% |
| CHALLENGER | 7,053 | 16.2 | 9.7 | 20.8 | 15.3 | 16.0 | 11.3 | 10.7 | 10.89 | 38.1% | 22.1% |
| ITF_MEN | 13,349 | 9.8 | 7.4 | 17.1 | 15.1 | 21.2 | 17.2 | 12.2 | 15.23 | 50.7% | 29.4% |
| ITF_WOMEN | 18,337 | 9.6 | 7.1 | 16.0 | 14.8 | 22.2 | 18.3 | 12.0 | 15.89 | 52.6% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,041 | 16.8 | 13.2 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,958 | 26.7 | 15.9 | 26.1 | 15.4 | 11.5 | 3.7 | 0.8 | 6.02 | 15.9% | 4.5% |
| CHALLENGER | 7,053 | 14.7 | 9.1 | 18.9 | 13.8 | 18.6 | 13.4 | 11.4 | 12.42 | 43.4% | 24.8% |
| ITF_MEN | 13,349 | 8.2 | 6.1 | 15.1 | 13.7 | 20.0 | 20.5 | 16.4 | 17.94 | 56.9% | 36.9% |
| ITF_WOMEN | 18,337 | 7.9 | 5.8 | 14.1 | 12.8 | 20.8 | 21.2 | 17.5 | 19.09 | 59.4% | 38.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,041 | 14.1 | 10.2 | 21.6 | 16.2 | 22.5 | 12.9 | 2.5 | 11.28 | 37.9% | 15.5% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,958 | 22.9 | 14.2 | 25.3 | 15.5 | 14.9 | 6.1 | 1.2 | 7.1 | 22.1% | 7.2% |
| CHALLENGER | 7,053 | 15.2 | 9.5 | 20.7 | 15.7 | 16.2 | 11.8 | 10.9 | 11.33 | 38.9% | 22.7% |
| ITF_MEN | 13,349 | 9.5 | 7.3 | 17.3 | 14.2 | 21.9 | 17.2 | 12.6 | 15.64 | 51.7% | 29.8% |
| ITF_WOMEN | 18,337 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.2 | 11.4 | 15.6 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,041 | 22.8 | 17.1 | 31.8 | 15.3 | 8.7 | 3.3 | 1.1 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,359 | 26.8 | 19.8 | 29.9 | 12.2 | 8.2 | 2.6 | 0.5 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,560 | 22.5 | 14.5 | 27.4 | 14.9 | 13.4 | 5.7 | 1.5 | 7.06 | 20.6% | 7.2% |
| DOUBLES | 2,571 | 4.9 | 4.5 | 12.9 | 11.1 | 20.3 | 24.4 | 22.0 | 23.31 | 66.7% | 46.4% |
| ITF_MEN | 9,890 | 12.9 | 9.6 | 21.5 | 15.7 | 21.6 | 12.9 | 5.8 | 11.75 | 40.3% | 18.7% |
| ITF_WOMEN | 11,907 | 13.4 | 9.2 | 19.9 | 15.6 | 21.4 | 14.9 | 5.5 | 12.26 | 41.9% | 20.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,784 | 23.8 | 16.1 | 31.3 | 16.9 | 9.0 | 2.6 | 0.2 | 6.54 | 11.8% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,842 | 28.9 | 15.9 | 27.9 | 13.4 | 10.4 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,989 | 20.9 | 12.0 | 25.7 | 18.0 | 16.0 | 5.9 | 1.6 | 8.21 | 23.4% | 7.5% |
| ITF_MEN | 9,733 | 12.0 | 8.7 | 20.7 | 17.3 | 22.1 | 14.0 | 5.2 | 12.37 | 41.3% | 19.2% |
| ITF_WOMEN | 13,484 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.1 | 4.9 | 13.19 | 44.1% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,928 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.5 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,842 | 27.0 | 16.2 | 26.3 | 15.3 | 11.4 | 3.3 | 0.4 | 5.96 | 15.1% | 3.7% |
| CHALLENGER | 4,989 | 18.5 | 11.5 | 23.8 | 16.2 | 19.0 | 9.1 | 1.8 | 8.96 | 30.0% | 11.0% |
| ITF_MEN | 9,734 | 9.7 | 7.2 | 17.6 | 16.0 | 21.8 | 18.7 | 9.1 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,485 | 8.9 | 6.9 | 16.1 | 14.4 | 22.7 | 20.4 | 10.6 | 16.49 | 53.8% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,928 | 14.3 | 10.3 | 21.9 | 16.4 | 22.6 | 12.6 | 1.9 | 11.05 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,300 | 27.0 | 20.0 | 29.9 | 12.3 | 7.9 | 2.4 | 0.4 | 5.3 | 10.7% | 2.8% |
| CHALLENGER | 4,030 | 23.9 | 15.4 | 28.5 | 15.0 | 12.8 | 4.0 | 0.4 | 6.59 | 17.1% | 4.3% |
| DOUBLES | 2,409 | 4.7 | 4.5 | 13.1 | 11.1 | 20.1 | 24.4 | 22.0 | 23.23 | 66.5% | 46.4% |
| ITF_MEN | 8,496 | 13.7 | 10.2 | 23.1 | 16.2 | 21.6 | 11.4 | 3.8 | 10.79 | 36.8% | 15.2% |
| ITF_WOMEN | 10,206 | 14.0 | 9.8 | 21.0 | 16.2 | 21.6 | 13.9 | 3.6 | 11.44 | 39.1% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,722 | 24.1 | 16.6 | 31.4 | 16.9 | 9.0 | 2.0 | 0.1 | 6.43 | 11.1% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,571 | 4.9 | 4.5 | 12.9 | 11.1 | 20.3 | 24.4 | 22.0 | 23.31 | 66.7% | 46.4% |
| singles | 31,905 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 174 | 8.1 | 9.2 | 11.5 | 7.5 | 20.1 | 28.2 | 15.5 | 21.18 | 63.8% | 43.7% |
| Clay | 9,693 | 12.7 | 9.1 | 20.0 | 15.5 | 19.6 | 13.9 | 9.2 | 12.6 | 42.7% | 23.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,620 | 13.4 | 8.7 | 18.7 | 15.2 | 19.2 | 14.8 | 9.9 | 12.89 | 43.9% | 24.7% |
| UNKNOWN | 6,347 | 10.6 | 7.6 | 17.1 | 16.3 | 21.5 | 15.9 | 11.1 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,386 | 19.6 | 11.9 | 22.4 | 15.9 | 14.9 | 9.2 | 6.2 | 8.88 | 30.3% | 15.4% |
| B | 5,753 | 12.6 | 8.7 | 19.7 | 15.6 | 19.9 | 12.7 | 10.8 | 12.7 | 43.4% | 23.5% |
| C | 6,670 | 12.0 | 8.8 | 19.5 | 15.7 | 18.6 | 14.6 | 10.8 | 12.98 | 44.0% | 25.4% |
| D | 7,647 | 11.7 | 8.3 | 17.9 | 15.3 | 21.7 | 15.7 | 9.4 | 13.85 | 46.8% | 25.1% |
| F | 13,615 | 7.4 | 5.6 | 14.8 | 14.7 | 23.6 | 20.8 | 13.1 | 17.79 | 57.5% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,256 | 24.6 | 16.1 | 29.0 | 15.0 | 10.6 | 3.4 | 1.2 | 6.36 | 15.2% | 4.7% |
| B | 4,826 | 16.6 | 10.8 | 24.2 | 16.9 | 18.9 | 9.6 | 3.0 | 9.68 | 31.5% | 12.7% |
| C | 6,804 | 11.0 | 7.8 | 19.6 | 14.6 | 21.0 | 15.7 | 10.4 | 13.64 | 47.1% | 26.1% |
| D | 5,169 | 14.5 | 10.1 | 21.4 | 15.3 | 20.8 | 12.5 | 5.3 | 11.19 | 38.6% | 17.8% |
| F | 8,421 | 10.2 | 8.3 | 16.2 | 14.6 | 23.3 | 19.6 | 7.8 | 15.34 | 50.7% | 27.4% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,108 | 17.8 | 10.9 | 21.5 | 15.7 | 15.2 | 10.1 | 8.8 | 9.97 | 34.1% | 18.9% |
| LIMITED | 10,311 | 13.7 | 9.7 | 20.4 | 15.8 | 19.4 | 13.3 | 7.6 | 11.89 | 40.4% | 20.9% |
| POOR | 21,652 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.8 | 11.8 | 16.16 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,819 | 23.8 | 17.9 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.91 | 9.7% | 3.3% |
| GAME_SPREAD | 6,642 | 22.7 | 15.4 | 32.0 | 16.9 | 9.0 | 3.4 | 0.7 | 6.69 | 13.0% | 4.0% |
| MATCH_WINNER | 34,476 | 15.7 | 10.9 | 22.2 | 15.1 | 18.4 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,394 | 27.9 | 16.8 | 30.8 | 12.7 | 9.1 | 2.4 | 0.3 | 5.64 | 11.8% | 2.7% |
| TOTAL_GAMES | 11,220 | 9.8 | 10.8 | 35.6 | 25.9 | 10.7 | 4.2 | 2.9 | 9.19 | 17.8% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,102 | 24.5 | 28.8 | 33.3 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,177 | 47.0 | 16.1 | 24.6 | 7.4 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,558 | 6.6 | 9.8 | 40.2 | 30.2 | 7.4 | 3.3 | 2.4 | 9.21 | 13.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,137 | 23.9 | 16.7 | 34.7 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,186 | 20.7 | 13.6 | 28.2 | 20.0 | 11.9 | 4.4 | 1.2 | 7.58 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,597 | 10.0 | 10.8 | 36.2 | 24.2 | 11.5 | 4.5 | 2.6 | 9.04 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 47,071 | 44.4% | 24.7% | 13.03 | 35.3% | 15.0% | 10.67 |
| gen1_elo | 47,071 | 44.0% | 24.4% | 12.82 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 47,071 | 52.0% | 31.3% | 15.8 | 43.9% | 21.5% | 12.98 |
| gen2 | 47,071 | 51.0% | 31.4% | 15.45 | 43.8% | 23.0% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,000 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 27,071 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 16.9 | 14.8 | 15.41 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,944 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.88 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 81,547 | 27944 | 23472 | 30131 | 24.8 | 126.8 | 1451.1 |
| ge_15pp | 33,290 | 9602 | 8361 | 15327 | 28.2 | 433.3 | 1451.1 |
| ge_25pp | 17,688 | 4579 | 3647 | 9462 | 33.1 | 580.7 | 1431.1 |
| lt_10pp | 35,800 | 14085 | 11105 | 10610 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261107T143504Z-b707b043`: 162 priced rows, quote age at build {'median': 17.9, 'max': 17.9}, freshness {'AGING': 162}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,643 | 19.2 | 10.9 | 25.5 | 17.9 | 18.1 | 7.5 | 1.0 | 8.81 | 26.5% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 988 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,096 | 0.0 | 2.2 | 37.4 | 26.4 | 24.0 | 9.2 | 0.9 | 11.8 | 34.0% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 47,071 | 7835 (16.7%) | 26.8% | 1.0% | {"EXTERNAL_STALE": 4643, "AGREES_WITH_KALSHI": 2096, "ALL_AGREE": 988, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,889 | 1974 (9.4%) | 36.1% | 1.5% | {"EXTERNAL_STALE": 1231, "AGREES_WITH_KALSHI": 713, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,647 | 614 (5.3%) | 34.2% | 2.1% | {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,453 | 584 (10.7%) | 34.8% | 2.2% | {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,946 | 4474 (23.6%) | 18.6% | 1.0% | {"EXTERNAL_STALE": 2583, "ALL_AGREE": 988, "AGREES_WITH_KALSHI": 830, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,228 | 10.5 | 7.7 | 19.4 | 14.7 | 21.6 | 16.2 | 9.9 | 14.09 | 47.7% | 26.1% |
| 4-10x | 6,306 | 11.2 | 8.5 | 18.4 | 15.2 | 22.1 | 14.3 | 10.2 | 13.84 | 46.6% | 24.5% |
| <2x | 24,034 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.56 | 39.6% | 22.0% |
| >=10x | 7,503 | 10.4 | 6.4 | 15.0 | 14.4 | 21.7 | 18.9 | 13.2 | 16.42 | 53.8% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,344 | 12.4 | 8.6 | 19.8 | 16.2 | 19.0 | 13.6 | 10.4 | 12.77 | 43.0% | 24.0% |
| 300-1000 | 10,211 | 11.8 | 8.7 | 17.7 | 15.2 | 20.8 | 16.2 | 9.6 | 13.75 | 46.6% | 25.8% |
| <300 | 14,724 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.8 | 13.1 | 17.12 | 56.0% | 32.9% |
| >=3000 | 9,792 | 21.4 | 12.9 | 23.9 | 15.6 | 13.9 | 7.3 | 5.1 | 7.74 | 26.3% | 12.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1444 | 0.5484 | 0.4096 | 0.4868 | +0.062 | -0.077 | 0.0014 ± 0.004 |
| ratio 4-10x | 983 | 0.5774 | 0.4329 | 0.4873 | +0.090 | -0.054 | 0.0088 ± 0.0051 |
| ratio <2x | 3516 | 0.5363 | 0.4137 | 0.4366 | +0.100 | -0.023 | 0.0148 ± 0.0024 |
| ratio >=10x | 1204 | 0.5651 | 0.3926 | 0.4477 | +0.117 | -0.055 | 0.0148 ± 0.0052 |
| thinner_sample 1000-3000 | 1981 | 0.5393 | 0.412 | 0.4478 | +0.091 | -0.036 | 0.0116 ± 0.0033 |
| thinner_sample 300-1000 | 1627 | 0.5641 | 0.424 | 0.4733 | +0.091 | -0.049 | 0.005 ± 0.0038 |
| thinner_sample <300 | 2307 | 0.558 | 0.3906 | 0.4547 | +0.103 | -0.064 | 0.0131 ± 0.0037 |
| thinner_sample >=3000 | 1232 | 0.5294 | 0.436 | 0.4464 | +0.083 | -0.011 | 0.0154 ± 0.0032 |
| data_status ADEQUATE | 1978 | 0.532 | 0.4291 | 0.4403 | +0.092 | -0.011 | 0.0155 ± 0.0028 |
| data_status LIMITED | 1750 | 0.5475 | 0.4151 | 0.4669 | +0.081 | -0.052 | 0.0074 ± 0.0036 |
| data_status POOR | 3419 | 0.5602 | 0.4004 | 0.4586 | +0.102 | -0.058 | 0.0108 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1036 | 0.1971 | 0.1975 | -0.0004 ± 0.0005 | 0.5741 | 0.5749 | 0.5026 | 0.4874 | 0.5019 | -0.092 ± 0.0146 | -0.0087 (8) |
| 3-5 | 659 | 0.2056 | 0.2055 | +0.0001 ± 0.0014 | 0.5961 | 0.5941 | 0.5042 | 0.4644 | 0.4825 | -0.096 ± 0.0181 | 0.01 (2) |
| 5-10 | 1537 | 0.2016 | 0.2006 | +0.0010 ± 0.0017 | 0.5896 | 0.5846 | 0.5119 | 0.4381 | 0.4658 | -0.091 ± 0.0118 | -0.0143 (7) |
| 10-15 | 1239 | 0.219 | 0.2098 | +0.0092 ± 0.0032 | 0.63 | 0.6034 | 0.5236 | 0.4001 | 0.4237 | -0.105 ± 0.0132 | -0.048 (5) |
| 15-25 | 1587 | 0.2259 | 0.2078 | +0.0182 ± 0.0045 | 0.6471 | 0.5991 | 0.5758 | 0.3812 | 0.4316 | -0.106 ± 0.0115 | -0.0045 (11) |
| 25-40 | 902 | 0.223 | 0.2055 | +0.0175 ± 0.009 | 0.6359 | 0.592 | 0.6507 | 0.341 | 0.4678 | -0.065 ± 0.0138 | -0.06 (2) |
| 40+ | 187 | 0.298 | 0.1745 | +0.1235 ± 0.0274 | 0.8017 | 0.5219 | 0.7301 | 0.2756 | 0.3743 | -0.085 ± 0.0266 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5415 | 0.1852 | 0.1861 | -0.0009 ± 0.0002 | 0.5464 | 0.5476 | 0.4904 | 0.4752 | 0.5082 | -0.019 ± 0.0059 | -0.01 (28) |
| 3-5 | 3607 | 0.1981 | 0.1964 | +0.0017 ± 0.0006 | 0.5768 | 0.5705 | 0.4824 | 0.4426 | 0.4411 | -0.056 ± 0.0075 | 0.0 (3) |
| 5-10 | 7819 | 0.2011 | 0.1977 | +0.0034 ± 0.0008 | 0.588 | 0.5765 | 0.4846 | 0.4109 | 0.4254 | -0.044 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6457 | 0.2024 | 0.1864 | +0.0160 ± 0.0013 | 0.5915 | 0.5466 | 0.4853 | 0.3614 | 0.359 | -0.064 ± 0.0054 | -0.0281 (16) |
| 15-25 | 8185 | 0.2064 | 0.1668 | +0.0396 ± 0.0018 | 0.6047 | 0.4957 | 0.4996 | 0.3041 | 0.3014 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6295 | 0.2231 | 0.1263 | +0.0968 ± 0.0028 | 0.6405 | 0.3882 | 0.5265 | 0.213 | 0.2197 | -0.058 ± 0.0043 | -0.0733 (3) |
| 40+ | 4199 | 0.3829 | 0.0438 | +0.3392 ± 0.0037 | 0.9974 | 0.1702 | 0.6308 | 0.1015 | 0.0576 | -0.076 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 827 | 0.2042 | 0.2045 | -0.0003 ± 0.0005 | 0.589 | 0.5901 | 0.5064 | 0.4916 | 0.5139 | -0.102 ± 0.0169 | -0.0117 (6) |
| 3-5 | 590 | 0.2115 | 0.2086 | +0.0029 ± 0.0015 | 0.6062 | 0.5999 | 0.513 | 0.4735 | 0.4525 | -0.130 ± 0.0202 | 0.01 (2) |
| 5-10 | 1324 | 0.2068 | 0.2049 | +0.0019 ± 0.0019 | 0.6 | 0.5948 | 0.5404 | 0.4659 | 0.4924 | -0.089 ± 0.0128 | -0.01 (4) |
| 10-15 | 1148 | 0.2134 | 0.2077 | +0.0057 ± 0.0034 | 0.6196 | 0.6015 | 0.5631 | 0.4387 | 0.4808 | -0.098 ± 0.0141 | -0.04 (5) |
| 15-25 | 1674 | 0.2321 | 0.2123 | +0.0198 ± 0.0044 | 0.6601 | 0.609 | 0.585 | 0.3895 | 0.4379 | -0.100 ± 0.0115 | -0.0118 (11) |
| 25-40 | 1167 | 0.2665 | 0.1974 | +0.0691 ± 0.0082 | 0.7435 | 0.5749 | 0.659 | 0.3448 | 0.3942 | -0.119 ± 0.013 | -0.008 (5) |
| 40+ | 417 | 0.3731 | 0.1615 | +0.2116 ± 0.0197 | 1.0168 | 0.4889 | 0.7349 | 0.2463 | 0.2878 | -0.088 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4628 | 0.192 | 0.1922 | -0.0002 ± 0.0002 | 0.5597 | 0.5599 | 0.5074 | 0.4923 | 0.5076 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3166 | 0.1929 | 0.1918 | +0.0011 ± 0.0006 | 0.5625 | 0.559 | 0.5116 | 0.4719 | 0.4773 | -0.046 ± 0.008 | 0.01 (2) |
| 5-10 | 6974 | 0.1972 | 0.1938 | +0.0034 ± 0.0008 | 0.5794 | 0.567 | 0.5088 | 0.4347 | 0.4511 | -0.041 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5795 | 0.2028 | 0.1919 | +0.0109 ± 0.0014 | 0.5951 | 0.561 | 0.5107 | 0.3867 | 0.4055 | -0.046 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8241 | 0.2173 | 0.1815 | +0.0358 ± 0.0018 | 0.6318 | 0.5323 | 0.5254 | 0.3298 | 0.3387 | -0.059 ± 0.0047 | -0.0094 (49) |
| 25-40 | 7400 | 0.251 | 0.1371 | +0.1139 ± 0.0027 | 0.7089 | 0.4191 | 0.5598 | 0.2429 | 0.2253 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5773 | 0.4018 | 0.0583 | +0.3435 ± 0.0037 | 1.0592 | 0.2108 | 0.6541 | 0.1183 | 0.0792 | -0.075 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1007 | 0.1955 | 0.1969 | -0.0014 ± 0.0005 | 0.5707 | 0.5742 | 0.5027 | 0.4873 | 0.5333 | -0.051 ± 0.0146 | -0.012 (10) |
| 3-5 | 709 | 0.2077 | 0.2061 | +0.0016 ± 0.0014 | 0.602 | 0.5965 | 0.4973 | 0.4577 | 0.4598 | -0.111 ± 0.0178 | -0.0 (4) |
| 5-10 | 1569 | 0.2026 | 0.1991 | +0.0035 ± 0.0017 | 0.5904 | 0.5805 | 0.5127 | 0.4389 | 0.4512 | -0.104 ± 0.0116 | -0.01 (10) |
| 10-15 | 1259 | 0.2113 | 0.2022 | +0.0092 ± 0.0031 | 0.6132 | 0.5867 | 0.5368 | 0.4135 | 0.44 | -0.107 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1517 | 0.2318 | 0.2127 | +0.0191 ± 0.0046 | 0.6613 | 0.6097 | 0.5859 | 0.3919 | 0.439 | -0.109 ± 0.0119 | -0.03 (1) |
| 25-40 | 890 | 0.2125 | 0.21 | +0.0025 ± 0.009 | 0.6136 | 0.6024 | 0.6589 | 0.3481 | 0.4978 | -0.053 ± 0.0139 | -0.0267 (3) |
| 40+ | 196 | 0.3112 | 0.182 | +0.1291 ± 0.0274 | 0.8415 | 0.5381 | 0.742 | 0.2876 | 0.3827 | -0.089 ± 0.0281 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5207 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.5462 | 0.5471 | 0.4863 | 0.471 | 0.4911 | -0.031 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3718 | 0.204 | 0.2023 | +0.0017 ± 0.0006 | 0.5932 | 0.5871 | 0.4791 | 0.4396 | 0.4381 | -0.056 ± 0.0075 | -0.01 (19) |
| 5-10 | 7976 | 0.196 | 0.1907 | +0.0052 ± 0.0007 | 0.5752 | 0.5589 | 0.4876 | 0.4136 | 0.4155 | -0.055 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6418 | 0.1938 | 0.1785 | +0.0153 ± 0.0013 | 0.5723 | 0.5283 | 0.4946 | 0.3712 | 0.3708 | -0.062 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8274 | 0.2123 | 0.1724 | +0.0398 ± 0.0018 | 0.6186 | 0.5086 | 0.5125 | 0.318 | 0.3136 | -0.071 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6234 | 0.2167 | 0.1273 | +0.0894 ± 0.0028 | 0.6268 | 0.39 | 0.5289 | 0.2133 | 0.2316 | -0.048 ± 0.0044 | -0.02 (4) |
| 40+ | 4150 | 0.392 | 0.0488 | +0.3432 ± 0.0039 | 1.0216 | 0.1828 | 0.6401 | 0.1077 | 0.0646 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1436 | 0.1977 | 0.1977 | -0.0000 ± 0.0004 | 0.5738 | 0.5737 | 0.5086 | 0.4936 | 0.4979 | -0.069 ± 0.012 | -0.0213 (54) |
| 3-5 | 1041 | 0.188 | 0.188 | -0.0000 ± 0.0011 | 0.5539 | 0.5521 | 0.4972 | 0.4573 | 0.4755 | -0.055 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2092 | 0.1998 | 0.1949 | +0.0049 ± 0.0015 | 0.5895 | 0.5732 | 0.5074 | 0.4338 | 0.4383 | -0.077 ± 0.0099 | -0.005 (78) |
| 10-15 | 1441 | 0.2147 | 0.202 | +0.0127 ± 0.0029 | 0.623 | 0.5875 | 0.5425 | 0.4197 | 0.4282 | -0.090 ± 0.0122 | 0.0012 (66) |
| 15-25 | 1874 | 0.2311 | 0.2073 | +0.0238 ± 0.0041 | 0.6596 | 0.5984 | 0.591 | 0.3961 | 0.4344 | -0.089 ± 0.0106 | -0.0214 (59) |
| 25-40 | 1124 | 0.24 | 0.2102 | +0.0298 ± 0.0083 | 0.6855 | 0.6034 | 0.6887 | 0.3767 | 0.4849 | -0.087 ± 0.0129 | -0.0252 (27) |
| 40+ | 400 | 0.3299 | 0.2005 | +0.1294 ± 0.0215 | 0.9487 | 0.5846 | 0.8156 | 0.3392 | 0.4575 | -0.099 ± 0.0201 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5303 | 0.1779 | 0.178 | -0.0001 ± 0.0002 | 0.5262 | 0.526 | 0.5116 | 0.4963 | 0.5061 | -0.039 ± 0.0058 | -0.0145 (98) |
| 3-5 | 3687 | 0.1949 | 0.1942 | +0.0007 ± 0.0006 | 0.5688 | 0.5666 | 0.5017 | 0.4619 | 0.473 | -0.039 ± 0.0073 | -0.0204 (72) |
| 5-10 | 7484 | 0.1963 | 0.1898 | +0.0065 ± 0.0008 | 0.5797 | 0.5598 | 0.5011 | 0.4276 | 0.4216 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5128 | 0.2101 | 0.1936 | +0.0164 ± 0.0015 | 0.6115 | 0.568 | 0.5375 | 0.4145 | 0.4078 | -0.073 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6236 | 0.2316 | 0.1999 | +0.0316 ± 0.0022 | 0.6652 | 0.5793 | 0.5767 | 0.3813 | 0.399 | -0.067 ± 0.0057 | -0.026 (108) |
| 25-40 | 4059 | 0.2571 | 0.1901 | +0.0670 ± 0.0043 | 0.7275 | 0.5537 | 0.6403 | 0.3277 | 0.3797 | -0.066 ± 0.0067 | -0.0246 (52) |
| 40+ | 1796 | 0.3728 | 0.1586 | +0.2142 ± 0.0097 | 1.0517 | 0.473 | 0.7446 | 0.2436 | 0.2906 | -0.066 ± 0.009 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7147 | 1.025 ± 0.033 | 1.101 | 0.169 | 0.1688 | 0.215 | 0.2037 |
| gen2 | 7147 | 0.82 ± 0.03 | 1.072 | 0.1734 | 0.1692 | 0.2333 | 0.2036 |
| gen1_elo | 7147 | 1.008 ± 0.032 | 1.089 | 0.1754 | 0.1689 | 0.2141 | 0.2038 |
| gen1_sr | 7147 | 1.004 ± 0.039 | 1.129 | 0.1334 | 0.1708 | 0.2294 | 0.2033 |
| gen1_ledger | 9408 | 0.864 ± 0.024 | 1.075 | 0.1897 | 0.1758 | 0.217 | 0.2002 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,290)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,683 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,545 | 22.7% |
| BOOK_QUALITY | execution | 5,955 | 17.9% |
| POOR_DATA | data | 3,848 | 11.6% |
| LIMITED_DATA | data | 2,072 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,924 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,388 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,372 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 952 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 550 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.7%, execution 17.9%, data 17.8%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,688)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,044 | 34.2% |
| STALE_QUOTE | market_freshness | 3,425 | 19.4% |
| BOOK_QUALITY | execution | 3,093 | 17.5% |
| POOR_DATA | data | 1,621 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,025 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 771 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 624 | 3.5% |
| LIMITED_DATA | data | 608 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 341 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 135 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.2%, market_freshness 19.4%, execution 17.5%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 53.5%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.8%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14111, "IDENTITY_AMBIGUOUS": 3577}; ticker orientation: {"VERIFIED": 17688}.

Checks: discipline:AMBIGUOUS 1194, discipline:PASS 16494, identity_confidence:AMBIGUOUS 3246, identity_confidence:PASS 14442, level_mapping:NA 1206, level_mapping:PASS 16482, market_pair:AMBIGUOUS 492, market_pair:NA 395, market_pair:PASS 16801, model_complement:NA 357, model_complement:PASS 17331, namesake:AMBIGUOUS 6, namesake:PASS 17682, physical_match_id:NA 6041, physical_match_id:PASS 11647, player_ids:PASS 17688, same_pair_other_event:PASS 17688, ticker_orientation:PASS 17688

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,317 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 54, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 18} | 5.52 | 0.2256 / 0.2205 (805) | 24.7% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,613 | 16.2% | 6.1% | 10.7% | {"coverage": 1116, "market_freshness/coverage": 220, "market_freshness": 217, "data": 157, "model_calibration_or_unknown": 79, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.36 | 0.2197 / 0.2095 (2728) | 37.9% | 15.1% | 4.1% | 22.3% |
| DOUBLES | 2,571 | 46.4% | 46.4% | 6.8% | {"execution": 665, "mapping": 347, "market_freshness": 106, "market_freshness/coverage": 69, "coverage": 7} | 23.23 | 0.2982 / 0.2322 (642) | 9.1% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 23,239 | 24.9% | 17.3% | 32.7% | {"coverage": 2031, "market_freshness": 1118, "execution": 980, "data": 850, "market_freshness/coverage": 587, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.64 | 0.2176 / 0.1993 (4932) | 39.9% | 68.7% | 15.1% | 21.6% |
| ITF_WOMEN | 30,244 | 26.4% | 18.9% | 45.2% | {"coverage": 2814, "market_freshness": 1723, "execution": 1324, "data": 1121, "market_freshness/coverage": 698, "mapping": 197, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.52 | 0.2028 / 0.1937 (5848) | 41.1% | 57.1% | 9.8% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,825 | 6.0% | 5.1% | 1.7% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2297 / 0.22 (788) | 29.9% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 19.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1173 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 207 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 163 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.97, "by_level_share_of_ge_25pp": {"ATP": 0.0135, "CHALLENGER": 0.1065, "DOUBLES": 0.0675, "ITF_MEN": 0.3268, "ITF_WOMEN": 0.4519, "OTHER": 0.0007, "WTA": 0.0165, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5349, "share_primary_cause_market_settled_or_in_play": 0.4349, "share_primary_cause_stale_quote_only": 0.1936}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17688, "identity_ambiguous_share": 0.2022, "ticker_orientation": {"VERIFIED": 17688}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11647, "with_external": 614, "coverage": 0.0527, "external_status": {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 391, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.342, "share_external_supports_model": 0.0212}, "pregame_clean_ge_25pp": {"n": 5453, "with_external": 584, "coverage": 0.1071, "external_status": {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 368, "MODEL_LONE_OUTLIER": 203, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3476, "share_external_supports_model": 0.0223}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 491.5, "median_sample_ratio": 2.45, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2087, "data_status": {"POOR": 9898, "LIMITED": 4601, "ADEQUATE": 3189}, "comparison_lt_10pp": {"median_thinner_serve_points": 1732.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1444, "model_minus_observed": 0.0616, "kalshi_minus_observed": -0.0772, "brier_diff_model_minus_kalshi": 0.0014}, "4-10x": {"n": 983, "model_minus_observed": 0.0902, "kalshi_minus_observed": -0.0544, "brier_diff_model_minus_kalshi": 0.0088}, "<2x": {"n": 3516, "model_minus_observed": 0.0998, "kalshi_minus_observed": -0.0229, "brier_diff_model_minus_kalshi": 0.0148}, ">=10x": {"n": 1204, "model_minus_observed": 0.1174, "kalshi_minus_observed": -0.0551, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7147, "model": {"intercept": -0.556, "slope": 0.82, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.179, "slope": 1.072, "slope_se": 0.034}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2333, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0297, "brier_diff_se": 0.0022, "model_logloss": 0.6642, "kalshi_logloss": 0.5896}, "fair_v1": {"n": 7147, "model": {"intercept": -0.448, "slope": 1.025, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.247, "slope": 1.101, "slope_se": 0.034}, "mean_extremity_model": 0.169, "mean_extremity_kalshi": 0.1688, "model_brier": 0.215, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0112, "brier_diff_se": 0.0018, "model_logloss": 0.6191, "kalshi_logloss": 0.5898}, "gen1_elo": {"n": 7147, "model": {"intercept": -0.439, "slope": 1.008, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.246, "slope": 1.089, "slope_se": 0.033}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1689, "model_brier": 0.2141, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0103, "brier_diff_se": 0.0018, "model_logloss": 0.6176, "kalshi_logloss": 0.59}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2474, "share_ge_15": 0.4438, "median_abs_gap": 13.03, "n": 47071}, "gen1_elo": {"share_ge_25": 0.2445, "share_ge_15": 0.4399, "median_abs_gap": 12.82, "n": 47071}, "gen1_sr": {"share_ge_25": 0.313, "share_ge_15": 0.5199, "median_abs_gap": 15.8, "n": 47071}, "gen2": {"share_ge_25": 0.3136, "share_ge_15": 0.51, "median_abs_gap": 15.45, "n": 47071}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1504, "share_ge_15": 0.353, "median_abs_gap": 10.67, "n": 36260}, "gen1_elo": {"share_ge_25": 0.1483, "share_ge_15": 0.3483, "median_abs_gap": 10.49, "n": 36260}, "gen1_sr": {"share_ge_25": 0.2154, "share_ge_15": 0.4387, "median_abs_gap": 12.98, "n": 36262}, "gen2": {"share_ge_25": 0.2303, "share_ge_15": 0.4381, "median_abs_gap": 12.83, "n": 36262}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0378, "share_ge_25_pregame_clean": 0.0326}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0603, "share_ge_25_pregame_clean": 0.0512}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.439, "share_within_10pp_pregame_clean": 0.4921, "corr_model_vs_mid_pregame_clean": 0.851}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1036, "model_brier": 0.1971, "kalshi_brier": 0.1975, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1239, "model_brier": 0.219, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 1587, "model_brier": 0.2259, "kalshi_brier": 0.2078, "brier_diff_model_minus_kalshi": 0.0182}, "25-40": {"n_settled": 902, "model_brier": 0.223, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 659, "model_brier": 0.2056, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 187, "model_brier": 0.298, "kalshi_brier": 0.1745, "brier_diff_model_minus_kalshi": 0.1235}, "5-10": {"n_settled": 1537, "model_brier": 0.2016, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.82, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.179, "slope": 1.072, "slope_se": 0.034}, "n": 7147}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.487, "slope": 0.864, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.171, "slope": 1.075, "slope_se": 0.028}, "n": 9408}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 642, "model_brier": 0.2982, "kalshi_brier": 0.2322, "brier_diff_model_minus_kalshi": 0.066, "brier_diff_se": 0.0116, "corr_model_outcome": 0.0995, "corr_kalshi_outcome": 0.2822}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
