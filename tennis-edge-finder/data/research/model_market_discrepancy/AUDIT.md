# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-02T22:49Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 73,775): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.0%, 25-40 13.7%, 40+ 8.0%; median gap 11.8 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.4%, Challenger 10.9%, doubles 6.9%). Main tour: ATP 3.9% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,005): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, STALE_QUOTE 19.0%, BOOK_QUALITY 18.3%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, market_freshness 19.0%, execution 18.3%, data 12.7%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.0% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,005 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.0% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.033, Gen-2 0.82, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 787 model 0.2193 vs Kalshi 0.2072; n 162 model 0.2828 vs Kalshi 0.1868.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 317,798 model-market comparisons (517,278 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 106,419 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-02T22:30:40.500013+00:00'], shadow board 84,604 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-02T22:30:45.816875+00:00'], Model 4 40,341 rows, 25,736 settled tickers, 9,467 tickers with an external scan.
* By model: {"gen1_ledger": 72125, "gen1_elo": 42516, "fair_v1": 42516, "gen2": 42516, "gen1_sr": 42516, "model4_fundamental": 37840, "model4_conditioned": 37769}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 73,775 | 14.1 | 9.6 | 20.2 | 15.4 | 19.0 | 13.7 | 8.0 | 11.8 | 40.7% | 21.7% |
| MW fair_v1 | 42,516 | 12.9 | 8.7 | 18.8 | 15.5 | 19.5 | 14.8 | 9.8 | 12.97 | 44.1% | 24.6% |
| MW gen1_elo | 42,516 | 12.6 | 8.8 | 19.4 | 15.4 | 19.4 | 14.7 | 9.7 | 12.79 | 43.9% | 24.4% |
| MW gen1_ledger | 31,259 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.29 | 36.0% | 17.7% |
| MW gen1_sr | 42,516 | 10.2 | 7.2 | 16.9 | 13.9 | 20.6 | 18.6 | 12.6 | 15.71 | 51.8% | 31.2% |
| MW gen2 | 42,516 | 11.1 | 7.7 | 16.6 | 13.8 | 19.4 | 17.7 | 13.7 | 15.37 | 50.8% | 31.4% |
| all families model4_conditioned | 37,769 | 22.3 | 18.0 | 34.1 | 17.2 | 5.0 | 2.1 | 1.3 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 37,840 | 17.3 | 13.4 | 33.8 | 20.1 | 10.1 | 3.8 | 1.6 | 7.68 | 15.4% | 5.3% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.0%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.27pp; >=10pp 44.6%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,774 | 27.8 | 15.4 | 28.0 | 13.5 | 11.0 | 3.8 | 0.6 | 5.92 | 15.4% | 4.4% |
| CHALLENGER | 6,388 | 16.2 | 9.8 | 20.6 | 15.2 | 15.9 | 11.5 | 10.8 | 10.93 | 38.2% | 22.3% |
| ITF_MEN | 11,671 | 9.8 | 7.5 | 16.9 | 15.0 | 21.2 | 17.5 | 12.1 | 15.32 | 50.8% | 29.6% |
| ITF_WOMEN | 16,630 | 9.5 | 7.0 | 16.0 | 15.2 | 22.0 | 18.2 | 12.1 | 15.74 | 52.3% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,832 | 17.4 | 13.0 | 24.6 | 21.1 | 16.1 | 6.5 | 1.2 | 8.54 | 23.8% | 7.7% |
| WTA125 | 1,215 | 15.9 | 7.2 | 22.6 | 19.6 | 20.7 | 12.3 | 1.7 | 10.7 | 34.6% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,774 | 26.1 | 15.9 | 26.1 | 15.7 | 11.6 | 3.8 | 0.8 | 6.13 | 16.2% | 4.6% |
| CHALLENGER | 6,388 | 15.0 | 9.1 | 18.5 | 14.1 | 18.5 | 13.5 | 11.5 | 12.49 | 43.4% | 25.0% |
| ITF_MEN | 11,671 | 8.0 | 6.2 | 15.1 | 13.8 | 19.6 | 20.7 | 16.6 | 17.95 | 56.8% | 37.2% |
| ITF_WOMEN | 16,630 | 7.9 | 5.8 | 14.0 | 12.8 | 20.6 | 21.2 | 17.8 | 19.15 | 59.6% | 39.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,832 | 14.7 | 10.5 | 21.7 | 16.0 | 21.9 | 12.8 | 2.4 | 10.92 | 37.1% | 15.2% |
| WTA125 | 1,215 | 9.9 | 7.2 | 16.5 | 15.9 | 23.9 | 17.9 | 8.6 | 15.14 | 50.4% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,774 | 22.4 | 13.7 | 25.2 | 15.7 | 15.5 | 6.3 | 1.2 | 7.43 | 23.0% | 7.5% |
| CHALLENGER | 6,388 | 15.1 | 9.4 | 20.8 | 15.8 | 15.9 | 12.1 | 10.9 | 11.31 | 38.9% | 23.0% |
| ITF_MEN | 11,671 | 9.3 | 7.2 | 17.3 | 14.2 | 21.9 | 17.7 | 12.5 | 15.8 | 52.1% | 30.2% |
| ITF_WOMEN | 16,630 | 9.3 | 6.9 | 16.4 | 15.8 | 22.1 | 18.1 | 11.4 | 15.51 | 51.6% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,832 | 22.9 | 16.6 | 32.0 | 15.0 | 9.0 | 3.4 | 1.1 | 6.17 | 13.6% | 4.6% |
| WTA125 | 1,215 | 20.7 | 12.8 | 26.0 | 18.9 | 15.3 | 6.0 | 0.3 | 8.07 | 21.6% | 6.3% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,234 | 25.4 | 19.6 | 30.8 | 12.6 | 8.5 | 2.6 | 0.5 | 5.54 | 11.6% | 3.1% |
| CHALLENGER | 4,244 | 22.5 | 14.4 | 27.3 | 14.6 | 13.7 | 5.9 | 1.6 | 7.15 | 21.2% | 7.5% |
| DOUBLES | 2,298 | 5.2 | 4.3 | 12.0 | 10.4 | 20.4 | 25.4 | 22.3 | 23.85 | 68.1% | 47.7% |
| ITF_MEN | 8,792 | 13.0 | 9.4 | 21.2 | 15.9 | 21.4 | 13.2 | 5.9 | 11.89 | 40.5% | 19.1% |
| ITF_WOMEN | 10,692 | 13.3 | 9.1 | 19.9 | 15.8 | 21.2 | 15.2 | 5.5 | 12.32 | 42.0% | 20.7% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,667 | 24.2 | 16.4 | 30.5 | 17.0 | 8.9 | 2.8 | 0.2 | 6.53 | 11.9% | 3.0% |
| WTA125 | 1,183 | 24.9 | 12.9 | 21.1 | 19.4 | 13.4 | 6.8 | 1.5 | 7.85 | 21.7% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,666 | 28.2 | 15.6 | 28.4 | 13.4 | 10.8 | 3.4 | 0.3 | 5.84 | 14.5% | 3.7% |
| CHALLENGER | 4,510 | 20.8 | 12.2 | 25.5 | 17.8 | 15.9 | 6.0 | 1.7 | 8.18 | 23.6% | 7.7% |
| ITF_MEN | 8,526 | 12.1 | 8.9 | 20.5 | 17.0 | 22.1 | 14.2 | 5.3 | 12.39 | 41.5% | 19.5% |
| ITF_WOMEN | 12,348 | 11.4 | 8.4 | 18.6 | 17.4 | 24.0 | 15.1 | 5.1 | 13.27 | 44.2% | 20.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,729 | 17.7 | 13.1 | 25.0 | 21.4 | 16.2 | 6.0 | 0.7 | 8.41 | 22.8% | 6.7% |
| WTA125 | 1,173 | 16.1 | 7.2 | 22.2 | 19.9 | 21.1 | 11.9 | 1.5 | 10.77 | 34.6% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,666 | 26.5 | 16.2 | 26.3 | 15.6 | 11.6 | 3.4 | 0.4 | 6.06 | 15.4% | 3.8% |
| CHALLENGER | 4,510 | 18.9 | 11.3 | 23.1 | 16.5 | 18.8 | 9.2 | 2.0 | 9.03 | 30.0% | 11.2% |
| ITF_MEN | 8,527 | 9.5 | 7.4 | 17.5 | 16.0 | 21.4 | 18.7 | 9.5 | 14.91 | 49.6% | 28.2% |
| ITF_WOMEN | 12,349 | 8.8 | 6.8 | 15.9 | 14.3 | 22.7 | 20.6 | 10.9 | 16.58 | 54.2% | 31.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,729 | 14.9 | 10.6 | 22.0 | 16.1 | 22.1 | 12.5 | 1.7 | 10.87 | 36.4% | 14.2% |
| WTA125 | 1,173 | 9.9 | 7.3 | 16.7 | 15.9 | 23.9 | 18.1 | 8.2 | 15.02 | 50.1% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,177 | 25.6 | 19.8 | 30.7 | 12.7 | 8.2 | 2.5 | 0.4 | 5.48 | 11.1% | 2.9% |
| CHALLENGER | 3,745 | 23.9 | 15.3 | 28.4 | 14.8 | 13.1 | 4.1 | 0.4 | 6.62 | 17.6% | 4.5% |
| DOUBLES | 2,159 | 5.1 | 4.4 | 12.2 | 10.6 | 20.1 | 25.3 | 22.3 | 23.85 | 67.7% | 47.6% |
| ITF_MEN | 7,514 | 13.8 | 10.1 | 22.9 | 16.4 | 21.3 | 11.7 | 3.9 | 10.94 | 36.9% | 15.6% |
| ITF_WOMEN | 9,138 | 13.9 | 9.5 | 21.1 | 16.4 | 21.4 | 14.2 | 3.5 | 11.52 | 39.1% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,607 | 24.5 | 16.9 | 30.4 | 17.1 | 8.9 | 2.2 | 0.1 | 6.37 | 11.1% | 2.2% |
| WTA125 | 1,052 | 26.1 | 13.7 | 22.1 | 20.4 | 12.4 | 4.8 | 0.5 | 7.36 | 17.7% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,298 | 5.2 | 4.3 | 12.0 | 10.4 | 20.4 | 25.4 | 22.3 | 23.85 | 68.1% | 47.7% |
| singles | 28,961 | 16.6 | 11.4 | 22.9 | 15.6 | 18.1 | 11.2 | 4.2 | 9.76 | 33.5% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 48 | 6.2 | 10.4 | 22.9 | 10.4 | 20.8 | 22.9 | 6.2 | 17.32 | 50.0% | 29.2% |
| Clay | 8,339 | 13.0 | 9.3 | 19.9 | 15.8 | 19.3 | 13.7 | 8.9 | 12.4 | 41.9% | 22.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 28,087 | 13.4 | 8.7 | 18.8 | 15.2 | 19.1 | 14.8 | 9.9 | 12.85 | 43.8% | 24.7% |
| UNKNOWN | 5,805 | 10.5 | 7.7 | 17.0 | 16.4 | 21.3 | 16.1 | 11.2 | 14.29 | 48.5% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,096 | 19.9 | 11.9 | 22.6 | 16.0 | 14.8 | 8.9 | 6.0 | 8.65 | 29.6% | 14.9% |
| B | 5,289 | 12.9 | 8.9 | 19.3 | 15.8 | 19.6 | 12.6 | 10.9 | 12.62 | 43.1% | 23.5% |
| C | 6,053 | 11.7 | 8.8 | 19.6 | 16.1 | 18.5 | 14.6 | 10.8 | 12.93 | 43.9% | 25.3% |
| D | 6,726 | 11.8 | 8.5 | 17.6 | 15.3 | 21.6 | 15.8 | 9.4 | 13.83 | 46.9% | 25.3% |
| F | 12,352 | 7.4 | 5.6 | 15.0 | 14.7 | 23.4 | 21.0 | 12.9 | 17.71 | 57.3% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,462 | 24.4 | 16.1 | 29.2 | 15.0 | 10.7 | 3.5 | 1.2 | 6.39 | 15.4% | 4.7% |
| B | 4,430 | 16.7 | 10.7 | 23.9 | 17.0 | 18.9 | 9.7 | 3.1 | 9.71 | 31.6% | 12.8% |
| C | 6,147 | 11.4 | 7.7 | 19.2 | 14.4 | 20.9 | 15.9 | 10.4 | 13.69 | 47.3% | 26.3% |
| D | 4,578 | 14.2 | 9.8 | 21.7 | 15.6 | 20.0 | 13.3 | 5.4 | 11.27 | 38.7% | 18.7% |
| F | 7,642 | 10.1 | 8.3 | 16.0 | 14.8 | 23.2 | 19.8 | 7.8 | 15.41 | 50.8% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 13,687 | 18.1 | 10.9 | 21.7 | 15.7 | 15.2 | 9.7 | 8.7 | 9.78 | 33.6% | 18.4% |
| LIMITED | 9,364 | 13.6 | 9.8 | 20.3 | 16.2 | 19.2 | 13.3 | 7.6 | 11.84 | 40.1% | 20.9% |
| POOR | 19,465 | 9.0 | 6.6 | 16.0 | 15.0 | 22.7 | 19.0 | 11.8 | 16.15 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,423 | 23.9 | 17.8 | 33.1 | 15.8 | 6.3 | 2.7 | 0.4 | 5.92 | 9.5% | 3.1% |
| GAME_SPREAD | 6,346 | 22.2 | 15.1 | 32.6 | 17.0 | 9.1 | 3.4 | 0.6 | 6.77 | 13.1% | 4.0% |
| MATCH_WINNER | 31,259 | 15.8 | 10.8 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.29 | 36.0% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,484 | 27.7 | 16.7 | 30.6 | 12.7 | 9.4 | 2.5 | 0.3 | 5.65 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,589 | 9.8 | 10.7 | 35.3 | 26.3 | 10.6 | 4.2 | 3.0 | 9.26 | 17.8% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,493 | 24.5 | 28.9 | 33.2 | 8.2 | 4.0 | 0.9 | 0.3 | 4.79 | 5.2% | 1.2% |
| GAME_SPREAD | 8,739 | 46.7 | 16.2 | 24.9 | 7.5 | 2.2 | 1.9 | 0.6 | 3.31 | 4.7% | 2.5% |
| TOTAL_GAMES | 15,537 | 6.6 | 9.7 | 40.0 | 30.6 | 7.5 | 3.4 | 2.5 | 9.27 | 13.3% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,521 | 23.9 | 16.6 | 34.8 | 14.8 | 7.0 | 2.5 | 0.5 | 6.06 | 10.0% | 3.0% |
| GAME_SPREAD | 8,744 | 20.1 | 13.5 | 28.2 | 20.2 | 12.2 | 4.5 | 1.2 | 7.75 | 17.9% | 5.7% |
| TOTAL_GAMES | 15,575 | 10.0 | 10.5 | 36.1 | 24.8 | 11.6 | 4.4 | 2.7 | 9.15 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 42,516 | 44.1% | 24.6% | 12.97 | 35.3% | 15.1% | 10.67 |
| gen1_elo | 42,516 | 43.9% | 24.4% | 12.79 | 35.0% | 15.1% | 10.5 |
| gen1_sr | 42,516 | 51.8% | 31.2% | 15.71 | 43.8% | 21.6% | 12.93 |
| gen2 | 42,516 | 50.8% | 31.4% | 15.37 | 43.8% | 23.2% | 12.8 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,242 | 15.6 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.3 | 10.7 | 35.2% | 15.2% |
| STALE | 23,274 | 10.8 | 7.2 | 16.6 | 14.0 | 19.0 | 17.1 | 15.3 | 15.58 | 51.4% | 32.4% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 24,727 | 16.5 | 11.2 | 22.8 | 15.3 | 17.7 | 11.7 | 4.8 | 9.87 | 34.2% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 73,775 | 24727 | 22714 | 26334 | 24.4 | 124.1 | 1451.1 |
| ge_15pp | 30,011 | 8461 | 8067 | 13483 | 27.4 | 435.3 | 1451.1 |
| ge_25pp | 16,005 | 4079 | 3511 | 8415 | 32.1 | 586.7 | 1431.1 |
| lt_10pp | 32,424 | 12474 | 10760 | 9190 | 22.6 | 47.1 | 1421.1 |

Current slate `SL-20261102T224935Z-e98695a8`: 654 priced rows, quote age at build {'median': 19.2, 'max': 19.3}, freshness {'AGING': 654}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 48 | 0.0 | 0.0 | 35.4 | 6.2 | 33.3 | 20.8 | 4.2 | 19.13 | 58.3% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 26 | 65.4 | 34.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.37 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,166 | 19.5 | 10.9 | 25.3 | 18.1 | 18.0 | 7.2 | 0.9 | 8.71 | 26.2% | 8.2% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 868 | 66.2 | 33.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,897 | 0.0 | 2.3 | 36.9 | 26.5 | 24.0 | 9.5 | 0.8 | 11.88 | 34.4% | 10.3% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 42,516 | 7032 (16.5%) | 27.0% | 1.1% | {"EXTERNAL_STALE": 4166, "AGREES_WITH_KALSHI": 1897, "ALL_AGREE": 868, "SUPPORTS_MODEL_DIRECTION": 47, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 26, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,751 | 1772 (9.4%) | 36.8% | 1.7% | {"EXTERNAL_STALE": 1090, "AGREES_WITH_KALSHI": 652, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,464 | 550 (5.3%) | 35.6% | 2.4% | {"EXTERNAL_STALE": 341, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,976 | 522 (10.5%) | 36.2% | 2.5% | {"EXTERNAL_STALE": 320, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,181 | 4001 (23.3%) | 18.6% | 1.0% | {"EXTERNAL_STALE": 2324, "ALL_AGREE": 868, "AGREES_WITH_KALSHI": 743, "EXTERNAL_OUTLIER": 26, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 16, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,224 | 10.4 | 7.5 | 19.4 | 14.6 | 21.7 | 16.4 | 10.0 | 14.14 | 48.1% | 26.4% |
| 4-10x | 5,698 | 11.0 | 8.6 | 18.6 | 15.4 | 22.1 | 14.2 | 10.2 | 13.76 | 46.5% | 24.4% |
| <2x | 21,831 | 15.2 | 9.9 | 19.8 | 16.2 | 17.3 | 12.9 | 8.8 | 11.47 | 39.0% | 21.7% |
| >=10x | 6,763 | 10.5 | 6.4 | 15.1 | 14.5 | 21.7 | 19.1 | 12.8 | 16.31 | 53.6% | 31.8% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,090 | 12.6 | 8.7 | 19.6 | 16.2 | 19.2 | 13.4 | 10.3 | 12.71 | 42.8% | 23.6% |
| 300-1000 | 9,123 | 11.8 | 8.8 | 17.7 | 15.3 | 20.3 | 16.4 | 9.6 | 13.61 | 46.3% | 26.0% |
| <300 | 13,408 | 8.3 | 5.8 | 15.2 | 14.8 | 23.1 | 19.9 | 12.9 | 17.1 | 56.0% | 32.9% |
| >=3000 | 8,895 | 21.5 | 12.9 | 24.2 | 15.8 | 13.6 | 7.0 | 4.9 | 7.63 | 25.5% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1225 | 0.551 | 0.4115 | 0.4963 | +0.055 | -0.085 | -0.0027 ± 0.0044 |
| ratio 4-10x | 851 | 0.582 | 0.4354 | 0.4947 | +0.087 | -0.059 | 0.0078 ± 0.0055 |
| ratio <2x | 3037 | 0.5374 | 0.4154 | 0.4439 | +0.094 | -0.028 | 0.0125 ± 0.0026 |
| ratio >=10x | 1043 | 0.5692 | 0.395 | 0.4506 | +0.119 | -0.056 | 0.014 ± 0.0056 |
| thinner_sample 1000-3000 | 1703 | 0.5395 | 0.4131 | 0.4533 | +0.086 | -0.040 | 0.0088 ± 0.0035 |
| thinner_sample 300-1000 | 1395 | 0.5688 | 0.427 | 0.4839 | +0.085 | -0.057 | 0.0031 ± 0.0042 |
| thinner_sample <300 | 2010 | 0.5611 | 0.3931 | 0.4607 | +0.100 | -0.068 | 0.0106 ± 0.004 |
| thinner_sample >=3000 | 1048 | 0.5307 | 0.438 | 0.4523 | +0.078 | -0.014 | 0.0148 ± 0.0035 |
| data_status ADEQUATE | 1702 | 0.533 | 0.4311 | 0.4448 | +0.088 | -0.014 | 0.0134 ± 0.0029 |
| data_status LIMITED | 1518 | 0.5492 | 0.4165 | 0.471 | +0.078 | -0.055 | 0.0068 ± 0.0038 |
| data_status POOR | 2936 | 0.5638 | 0.4027 | 0.4683 | +0.095 | -0.066 | 0.0077 ± 0.0032 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 903 | 0.1998 | 0.2002 | -0.0004 ± 0.0005 | 0.58 | 0.581 | 0.503 | 0.4878 | 0.505 | -0.091 ± 0.0158 | -0.0087 (8) |
| 3-5 | 561 | 0.2056 | 0.2051 | +0.0006 ± 0.0015 | 0.5945 | 0.5913 | 0.5036 | 0.4637 | 0.4759 | -0.106 ± 0.0196 | 0.01 (2) |
| 5-10 | 1312 | 0.2007 | 0.2006 | +0.0001 ± 0.0019 | 0.5871 | 0.5847 | 0.5115 | 0.4378 | 0.4718 | -0.089 ± 0.0128 | -0.0143 (7) |
| 10-15 | 1064 | 0.2195 | 0.2103 | +0.0092 ± 0.0035 | 0.6313 | 0.6052 | 0.5289 | 0.4053 | 0.4286 | -0.109 ± 0.0142 | -0.048 (5) |
| 15-25 | 1367 | 0.2253 | 0.2099 | +0.0154 ± 0.0048 | 0.6458 | 0.6034 | 0.5769 | 0.3817 | 0.4404 | -0.104 ± 0.0124 | -0.004 (10) |
| 25-40 | 787 | 0.2193 | 0.2072 | +0.0121 ± 0.0097 | 0.6273 | 0.5963 | 0.6572 | 0.3472 | 0.4828 | -0.069 ± 0.0147 | -0.06 (2) |
| 40+ | 162 | 0.2828 | 0.1868 | +0.0960 ± 0.0297 | 0.7691 | 0.5514 | 0.7391 | 0.2898 | 0.4136 | -0.074 ± 0.0293 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4850 | 0.1851 | 0.1859 | -0.0008 ± 0.0002 | 0.5456 | 0.5464 | 0.4876 | 0.4724 | 0.5012 | -0.024 ± 0.0063 | -0.01 (28) |
| 3-5 | 3245 | 0.1948 | 0.1926 | +0.0021 ± 0.0006 | 0.5681 | 0.5607 | 0.4825 | 0.4427 | 0.4351 | -0.062 ± 0.0078 | 0.0 (3) |
| 5-10 | 6994 | 0.2007 | 0.1973 | +0.0034 ± 0.0008 | 0.5868 | 0.5753 | 0.4847 | 0.4112 | 0.4251 | -0.046 ± 0.0054 | -0.0114 (22) |
| 10-15 | 5753 | 0.2013 | 0.1855 | +0.0158 ± 0.0014 | 0.5888 | 0.5452 | 0.4849 | 0.361 | 0.3584 | -0.065 ± 0.0057 | -0.0281 (16) |
| 15-25 | 7219 | 0.2068 | 0.1679 | +0.0389 ± 0.0019 | 0.606 | 0.4982 | 0.5001 | 0.3043 | 0.3039 | -0.070 ± 0.0048 | -0.0027 (45) |
| 25-40 | 5627 | 0.2208 | 0.1257 | +0.0952 ± 0.003 | 0.6356 | 0.3863 | 0.5262 | 0.2122 | 0.222 | -0.057 ± 0.0046 | -0.0733 (3) |
| 40+ | 3714 | 0.3834 | 0.0448 | +0.3386 ± 0.004 | 0.9989 | 0.1734 | 0.6327 | 0.1042 | 0.0603 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 721 | 0.2077 | 0.2082 | -0.0006 ± 0.0006 | 0.5978 | 0.5994 | 0.5053 | 0.4905 | 0.5215 | -0.098 ± 0.0184 | -0.0117 (6) |
| 3-5 | 510 | 0.2152 | 0.2125 | +0.0027 ± 0.0016 | 0.6129 | 0.6077 | 0.5148 | 0.4751 | 0.4569 | -0.131 ± 0.0219 | 0.01 (2) |
| 5-10 | 1136 | 0.2063 | 0.204 | +0.0023 ± 0.002 | 0.599 | 0.5923 | 0.5427 | 0.468 | 0.493 | -0.096 ± 0.0138 | -0.01 (4) |
| 10-15 | 987 | 0.2147 | 0.2096 | +0.0051 ± 0.0036 | 0.6203 | 0.606 | 0.5664 | 0.4421 | 0.4873 | -0.100 ± 0.0152 | -0.04 (5) |
| 15-25 | 1431 | 0.2296 | 0.2123 | +0.0172 ± 0.0048 | 0.6535 | 0.6089 | 0.5838 | 0.3884 | 0.4444 | -0.099 ± 0.0124 | -0.012 (10) |
| 25-40 | 1004 | 0.2681 | 0.1992 | +0.0689 ± 0.0088 | 0.7484 | 0.5792 | 0.6616 | 0.3479 | 0.3974 | -0.127 ± 0.0141 | -0.008 (5) |
| 40+ | 367 | 0.3639 | 0.1656 | +0.1984 ± 0.0211 | 0.9947 | 0.4985 | 0.7326 | 0.2475 | 0.2997 | -0.082 ± 0.0204 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4172 | 0.1914 | 0.1916 | -0.0002 ± 0.0002 | 0.5586 | 0.5588 | 0.5076 | 0.4926 | 0.5096 | -0.040 ± 0.007 | -0.0154 (26) |
| 3-5 | 2860 | 0.1935 | 0.1924 | +0.0011 ± 0.0007 | 0.5632 | 0.5597 | 0.511 | 0.4713 | 0.4762 | -0.047 ± 0.0084 | 0.01 (2) |
| 5-10 | 6212 | 0.1978 | 0.1941 | +0.0037 ± 0.0008 | 0.5805 | 0.5674 | 0.5092 | 0.4352 | 0.4501 | -0.043 ± 0.0057 | -0.0117 (6) |
| 10-15 | 5161 | 0.203 | 0.1916 | +0.0114 ± 0.0015 | 0.5951 | 0.5607 | 0.5129 | 0.3891 | 0.4059 | -0.049 ± 0.0062 | -0.0189 (18) |
| 15-25 | 7224 | 0.2168 | 0.1806 | +0.0362 ± 0.002 | 0.6307 | 0.5301 | 0.5227 | 0.3274 | 0.3354 | -0.062 ± 0.005 | -0.0084 (43) |
| 25-40 | 6593 | 0.2506 | 0.1367 | +0.1139 ± 0.0029 | 0.7076 | 0.4181 | 0.5584 | 0.2417 | 0.2237 | -0.083 ± 0.0045 | -0.0095 (20) |
| 40+ | 5180 | 0.4 | 0.059 | +0.3410 ± 0.0039 | 1.0551 | 0.2126 | 0.6538 | 0.1186 | 0.0815 | -0.073 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 853 | 0.1949 | 0.1968 | -0.0020 ± 0.0005 | 0.5688 | 0.5737 | 0.5018 | 0.4864 | 0.5428 | -0.041 ± 0.0159 | -0.012 (10) |
| 3-5 | 605 | 0.2069 | 0.2048 | +0.0021 ± 0.0015 | 0.5987 | 0.5918 | 0.4977 | 0.4581 | 0.4545 | -0.122 ± 0.0192 | -0.0 (4) |
| 5-10 | 1354 | 0.2027 | 0.2001 | +0.0026 ± 0.0018 | 0.5906 | 0.5825 | 0.5116 | 0.4378 | 0.4557 | -0.101 ± 0.0125 | -0.01 (9) |
| 10-15 | 1072 | 0.2096 | 0.203 | +0.0067 ± 0.0034 | 0.6092 | 0.5891 | 0.5418 | 0.4186 | 0.4543 | -0.103 ± 0.0138 | -0.0286 (7) |
| 15-25 | 1298 | 0.2337 | 0.2156 | +0.0181 ± 0.005 | 0.6659 | 0.616 | 0.5899 | 0.3956 | 0.4461 | -0.113 ± 0.0129 | -0.03 (1) |
| 25-40 | 803 | 0.2101 | 0.2121 | -0.0020 ± 0.0095 | 0.6075 | 0.608 | 0.6648 | 0.3542 | 0.5106 | -0.055 ± 0.0145 | -0.0267 (3) |
| 40+ | 171 | 0.3004 | 0.1944 | +0.1060 ± 0.0297 | 0.8176 | 0.5688 | 0.75 | 0.2993 | 0.4152 | -0.081 ± 0.0309 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4619 | 0.1838 | 0.1844 | -0.0007 ± 0.0002 | 0.5416 | 0.5427 | 0.483 | 0.4677 | 0.4889 | -0.030 ± 0.0064 | -0.0137 (41) |
| 3-5 | 3272 | 0.2007 | 0.1985 | +0.0022 ± 0.0006 | 0.5846 | 0.5773 | 0.4804 | 0.4409 | 0.4334 | -0.063 ± 0.0079 | -0.01 (19) |
| 5-10 | 7137 | 0.194 | 0.1896 | +0.0045 ± 0.0008 | 0.5708 | 0.5562 | 0.4869 | 0.4129 | 0.4199 | -0.051 ± 0.0052 | -0.0105 (37) |
| 10-15 | 5721 | 0.1925 | 0.1789 | +0.0136 ± 0.0014 | 0.5692 | 0.5295 | 0.4957 | 0.3724 | 0.3781 | -0.057 ± 0.0056 | -0.0146 (13) |
| 15-25 | 7343 | 0.2132 | 0.1736 | +0.0396 ± 0.0019 | 0.6207 | 0.511 | 0.5142 | 0.3196 | 0.3164 | -0.072 ± 0.0049 | -0.0533 (3) |
| 25-40 | 5641 | 0.216 | 0.1282 | +0.0878 ± 0.003 | 0.6249 | 0.3922 | 0.5297 | 0.2141 | 0.2349 | -0.048 ± 0.0046 | -0.02 (4) |
| 40+ | 3669 | 0.3934 | 0.0504 | +0.3430 ± 0.0042 | 1.0258 | 0.1876 | 0.6424 | 0.1109 | 0.0673 | -0.078 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1279 | 0.1946 | 0.1947 | -0.0001 ± 0.0004 | 0.5672 | 0.5672 | 0.5062 | 0.4911 | 0.4957 | -0.069 ± 0.0126 | -0.0213 (54) |
| 3-5 | 896 | 0.1886 | 0.1884 | +0.0002 ± 0.0012 | 0.5537 | 0.552 | 0.4968 | 0.457 | 0.4732 | -0.060 ± 0.0148 | -0.0194 (34) |
| 5-10 | 1861 | 0.2011 | 0.1966 | +0.0045 ± 0.0015 | 0.5909 | 0.5763 | 0.5054 | 0.4317 | 0.4385 | -0.075 ± 0.0105 | -0.005 (78) |
| 10-15 | 1282 | 0.2169 | 0.2037 | +0.0133 ± 0.0031 | 0.6264 | 0.5912 | 0.5395 | 0.4167 | 0.4228 | -0.092 ± 0.013 | 0.0014 (65) |
| 15-25 | 1647 | 0.2306 | 0.2086 | +0.0220 ± 0.0044 | 0.6574 | 0.6014 | 0.5866 | 0.3918 | 0.4359 | -0.087 ± 0.0114 | -0.0214 (59) |
| 25-40 | 1024 | 0.2411 | 0.2114 | +0.0298 ± 0.0088 | 0.6895 | 0.6056 | 0.6886 | 0.3762 | 0.4844 | -0.091 ± 0.0134 | -0.0252 (27) |
| 40+ | 352 | 0.3241 | 0.2053 | +0.1188 ± 0.023 | 0.9418 | 0.596 | 0.8218 | 0.346 | 0.4744 | -0.097 ± 0.0215 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4806 | 0.1749 | 0.1752 | -0.0002 ± 0.0002 | 0.5188 | 0.5189 | 0.5117 | 0.4965 | 0.5096 | -0.036 ± 0.0061 | -0.0145 (98) |
| 3-5 | 3301 | 0.1943 | 0.1932 | +0.0011 ± 0.0006 | 0.5663 | 0.5637 | 0.5021 | 0.4624 | 0.4686 | -0.044 ± 0.0077 | -0.0204 (72) |
| 5-10 | 6729 | 0.1977 | 0.1912 | +0.0065 ± 0.0008 | 0.5814 | 0.5625 | 0.5009 | 0.4273 | 0.4216 | -0.063 ± 0.0054 | -0.0084 (134) |
| 10-15 | 4654 | 0.211 | 0.1951 | +0.0159 ± 0.0016 | 0.6126 | 0.5714 | 0.5378 | 0.4148 | 0.4104 | -0.070 ± 0.0065 | -0.0053 (106) |
| 15-25 | 5597 | 0.2301 | 0.2002 | +0.0299 ± 0.0024 | 0.6615 | 0.5797 | 0.5732 | 0.3777 | 0.4004 | -0.065 ± 0.006 | -0.026 (108) |
| 25-40 | 3755 | 0.2585 | 0.1893 | +0.0693 ± 0.0045 | 0.7318 | 0.5516 | 0.6385 | 0.3259 | 0.3736 | -0.072 ± 0.0069 | -0.0246 (52) |
| 40+ | 1619 | 0.3724 | 0.1576 | +0.2148 ± 0.0102 | 1.0546 | 0.4689 | 0.7453 | 0.2435 | 0.2909 | -0.068 ± 0.0093 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6156 | 1.033 ± 0.036 | 1.103 | 0.1693 | 0.1659 | 0.2142 | 0.2052 |
| gen2 | 6156 | 0.82 ± 0.032 | 1.072 | 0.172 | 0.1662 | 0.2334 | 0.205 |
| gen1_elo | 6156 | 1.008 ± 0.034 | 1.096 | 0.1762 | 0.166 | 0.2134 | 0.2053 |
| gen1_sr | 6156 | 1.009 ± 0.042 | 1.132 | 0.1322 | 0.168 | 0.2296 | 0.2047 |
| gen1_ledger | 8341 | 0.866 ± 0.026 | 1.073 | 0.1887 | 0.1746 | 0.2171 | 0.201 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 30,011)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 6,745 | 22.5% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,734 | 22.4% |
| BOOK_QUALITY | execution | 5,625 | 18.7% |
| POOR_DATA | data | 3,465 | 11.6% |
| LIMITED_DATA | data | 1,878 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,695 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,269 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,232 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 852 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 515 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 22.5%, coverage 22.4%, execution 18.7%, data 17.8%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 51.8%, STALE_KALSHI_QUOTE 44.9%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 25.0%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.3%, LOW_DISPLAYED_LIQUIDITY 8.2%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.9%, POST_SETTLEMENT_OBSERVATION 22.4%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,005)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,436 | 34.0% |
| STALE_QUOTE | market_freshness | 3,042 | 19.0% |
| BOOK_QUALITY | execution | 2,936 | 18.3% |
| POOR_DATA | data | 1,488 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 890 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 671 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 555 | 3.5% |
| LIMITED_DATA | data | 548 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 311 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 127 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, market_freshness 19.0%, execution 18.3%, data 12.7%, market_freshness/coverage 9.0%, mapping 4.2%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.0%, STALE_KALSHI_QUOTE 52.6%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.1%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, EVENT_MAPPING_RISK 9.2%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.1%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12721, "IDENTITY_AMBIGUOUS": 3284}; ticker orientation: {"VERIFIED": 16005}.

Checks: discipline:AMBIGUOUS 1096, discipline:PASS 14909, identity_confidence:AMBIGUOUS 2960, identity_confidence:PASS 13045, level_mapping:NA 1108, level_mapping:PASS 14897, market_pair:AMBIGUOUS 484, market_pair:NA 357, market_pair:PASS 15164, model_complement:NA 320, model_complement:PASS 15685, namesake:AMBIGUOUS 6, namesake:PASS 15999, physical_match_id:NA 5541, physical_match_id:PASS 10464, player_ids:PASS 16005, same_pair_other_event:PASS 16005, ticker_orientation:PASS 16005

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,008 | 3.9% | 3.4% | 1.5% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "coverage": 19, "market_freshness/coverage": 17} | 5.67 | 0.2215 / 0.2155 (727) | 23.9% | 2.6% | 3.1% | 2.8% |
| CHALLENGER | 10,632 | 16.4% | 6.3% | 10.9% | {"coverage": 1017, "market_freshness/coverage": 207, "market_freshness": 196, "data": 154, "model_calibration_or_unknown": 74, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.37 | 0.2208 / 0.2099 (2463) | 36.3% | 16.0% | 4.2% | 22.4% |
| DOUBLES | 2,298 | 47.7% | 47.6% | 6.9% | {"execution": 625, "mapping": 297, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.85 | 0.3053 / 0.2392 (546) | 10.2% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 20,463 | 25.1% | 17.6% | 32.1% | {"coverage": 1810, "market_freshness": 952, "execution": 929, "data": 754, "market_freshness/coverage": 493, "mapping": 188, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.71 | 0.2169 / 0.2003 (4214) | 38.4% | 69.0% | 16.2% | 21.6% |
| ITF_WOMEN | 27,322 | 26.5% | 19.1% | 45.3% | {"coverage": 2531, "market_freshness": 1553, "execution": 1259, "data": 1030, "market_freshness/coverage": 612, "mapping": 163, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.56 | 0.202 / 0.1948 (5104) | 40.1% | 57.2% | 9.8% | 21.4% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,499 | 6.0% | 5.0% | 1.7% | {"market_freshness": 97, "model_calibration_or_unknown": 47, "coverage": 37, "execution": 29, "data": 24, "model_calibration": 20, "market_freshness/coverage": 13, "mapping": 1} | 7.63 | 0.2297 / 0.2229 (691) | 28.8% | 1.9% | 1.4% | 3.6% |
| WTA125 | 2,398 | 11.2% | 9.6% | 1.7% | {"market_freshness": 79, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 38, "execution": 24, "model_calibration": 17, "coverage": 14, "mapping": 4} | 9.26 | 0.2098 / 0.1927 (710) | 27.2% | 10.9% | 4.5% | 7.2% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 769 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 547 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
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
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9685, "by_level_share_of_ge_25pp": {"ATP": 0.0146, "CHALLENGER": 0.1088, "DOUBLES": 0.0685, "ITF_MEN": 0.3208, "ITF_WOMEN": 0.453, "OTHER": 0.0007, "WTA": 0.0167, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5258, "share_primary_cause_market_settled_or_in_play": 0.4299, "share_primary_cause_stale_quote_only": 0.1901}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16005, "identity_ambiguous_share": 0.2052, "ticker_orientation": {"VERIFIED": 16005}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10464, "with_external": 550, "coverage": 0.0526, "external_status": {"EXTERNAL_STALE": 341, "AGREES_WITH_KALSHI": 196, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 341, "MODEL_LONE_OUTLIER": 196, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3564, "share_external_supports_model": 0.0236}, "pregame_clean_ge_25pp": {"n": 4976, "with_external": 522, "coverage": 0.1049, "external_status": {"EXTERNAL_STALE": 320, "AGREES_WITH_KALSHI": 189, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 320, "MODEL_LONE_OUTLIER": 189, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3621, "share_external_supports_model": 0.0249}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2066, "data_status": {"POOR": 8987, "LIMITED": 4195, "ADEQUATE": 2823}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.69, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1225, "model_minus_observed": 0.0547, "kalshi_minus_observed": -0.0848, "brier_diff_model_minus_kalshi": -0.0027}, "4-10x": {"n": 851, "model_minus_observed": 0.0872, "kalshi_minus_observed": -0.0593, "brier_diff_model_minus_kalshi": 0.0078}, "<2x": {"n": 3037, "model_minus_observed": 0.0936, "kalshi_minus_observed": -0.0284, "brier_diff_model_minus_kalshi": 0.0125}, ">=10x": {"n": 1043, "model_minus_observed": 0.1186, "kalshi_minus_observed": -0.0557, "brier_diff_model_minus_kalshi": 0.014}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6156, "model": {"intercept": -0.539, "slope": 0.82, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.194, "slope": 1.072, "slope_se": 0.036}, "mean_extremity_model": 0.172, "mean_extremity_kalshi": 0.1662, "model_brier": 0.2334, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0285, "brier_diff_se": 0.0024, "model_logloss": 0.6641, "kalshi_logloss": 0.5927}, "fair_v1": {"n": 6156, "model": {"intercept": -0.431, "slope": 1.033, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.269, "slope": 1.103, "slope_se": 0.037}, "mean_extremity_model": 0.1693, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2142, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0091, "brier_diff_se": 0.002, "model_logloss": 0.6173, "kalshi_logloss": 0.5931}, "gen1_elo": {"n": 6156, "model": {"intercept": -0.414, "slope": 1.008, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.28, "slope": 1.096, "slope_se": 0.036}, "mean_extremity_model": 0.1762, "mean_extremity_kalshi": 0.166, "model_brier": 0.2134, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0082, "brier_diff_se": 0.002, "model_logloss": 0.616, "kalshi_logloss": 0.5934}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2461, "share_ge_15": 0.441, "median_abs_gap": 12.97, "n": 42516}, "gen1_elo": {"share_ge_25": 0.2442, "share_ge_15": 0.4387, "median_abs_gap": 12.79, "n": 42516}, "gen1_sr": {"share_ge_25": 0.3119, "share_ge_15": 0.5176, "median_abs_gap": 15.71, "n": 42516}, "gen2": {"share_ge_25": 0.3141, "share_ge_15": 0.5079, "median_abs_gap": 15.37, "n": 42516}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.151, "share_ge_15": 0.3529, "median_abs_gap": 10.67, "n": 32958}, "gen1_elo": {"share_ge_25": 0.1506, "share_ge_15": 0.3496, "median_abs_gap": 10.5, "n": 32957}, "gen1_sr": {"share_ge_25": 0.2162, "share_ge_15": 0.4375, "median_abs_gap": 12.93, "n": 32960}, "gen2": {"share_ge_25": 0.2318, "share_ge_15": 0.4378, "median_abs_gap": 12.8, "n": 32960}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.67, "share_ge_25_all": 0.0389, "share_ge_25_pregame_clean": 0.0339}, "WTA": {"median_abs_gap_pregame_clean": 7.63, "share_ge_25_all": 0.0596, "share_ge_25_pregame_clean": 0.0503}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2375, "share_within_10pp_all": 0.4395, "share_within_10pp_pregame_clean": 0.4918, "corr_model_vs_mid_pregame_clean": 0.8503}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 903, "model_brier": 0.1998, "kalshi_brier": 0.2002, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1064, "model_brier": 0.2195, "kalshi_brier": 0.2103, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 1367, "model_brier": 0.2253, "kalshi_brier": 0.2099, "brier_diff_model_minus_kalshi": 0.0154}, "25-40": {"n_settled": 787, "model_brier": 0.2193, "kalshi_brier": 0.2072, "brier_diff_model_minus_kalshi": 0.0121}, "3-5": {"n_settled": 561, "model_brier": 0.2056, "kalshi_brier": 0.2051, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 162, "model_brier": 0.2828, "kalshi_brier": 0.1868, "brier_diff_model_minus_kalshi": 0.096}, "5-10": {"n_settled": 1312, "model_brier": 0.2007, "kalshi_brier": 0.2006, "brier_diff_model_minus_kalshi": 0.0001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.539, "slope": 0.82, "slope_se": 0.032}, "kalshi_slope": {"intercept": 0.194, "slope": 1.072, "slope_se": 0.036}, "n": 6156}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.484, "slope": 0.866, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.177, "slope": 1.073, "slope_se": 0.03}, "n": 8341}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 546, "model_brier": 0.3053, "kalshi_brier": 0.2392, "brier_diff_model_minus_kalshi": 0.0661, "brier_diff_se": 0.0128, "corr_model_outcome": 0.0647, "corr_kalshi_outcome": 0.2269}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
