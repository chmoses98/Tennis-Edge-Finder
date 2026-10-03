# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-03T21:50Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 11,235): 0-3 13.2%, 3-5 8.9%, 5-10 19.3%, 10-15 14.9%, 15-25 19.6%, 25-40 14.4%, 40+ 9.6%; median gap 12.69 pp.
* **Where the extremes live**: 96.7% of >=25 pp gaps are off the ATP/WTA main tour (ITF 74.7%, Challenger 12.2%, doubles 6.8%). Main tour: ATP 4.1% and WTA 9.4% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 2,705): MARKET_ALREADY_SETTLED_WHEN_PRICED 47.6%, STALE_QUOTE 23.3%, POOR_DATA 6.2%, BOOK_QUALITY 6.0%, POSSIBLY_IN_PLAY_QUOTE 5.4%, IN_PLAY_QUOTE 3.8%, LIMITED_DATA 3.0%, IDENTITY_AMBIGUOUS 2.6%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%. By class: coverage 47.6%, market_freshness 23.3%, data 9.2%, market_freshness/coverage 9.2%, execution 6.0%, mapping 2.6%, model_calibration_or_unknown 2.1%.
* **Stale / settled / in-play**: 69.9% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 56.8% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 2,705 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 14.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 0.6%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 7.6% of the time and with the model 0.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 827.0 points vs 1967.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.105, Gen-2 0.927, Gen-1 ledger 0.885 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 91 model 0.2376 vs Kalshi 0.1801; n 26 model 0.3509 vs Kalshi 0.1453.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 35,994 model-market comparisons (62,412 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 16,658 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-03T21:45:53.831770+00:00'], shadow board 10,279 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-03T21:45:57.637322+00:00'], Model 4 2,930 rows, 8,292 settled tickers, 1,795 tickers with an external scan.
* By model: {"gen1_ledger": 9669, "gen1_elo": 5171, "fair_v1": 5171, "gen2": 5171, "gen1_sr": 5171, "model4_fundamental": 2825, "model4_conditioned": 2816}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 11,235 | 13.2 | 8.9 | 19.3 | 14.9 | 19.6 | 14.4 | 9.6 | 12.69 | 43.7% | 24.1% |
| MW fair_v1 | 5,171 | 13.3 | 8.3 | 18.4 | 15.2 | 18.6 | 15.2 | 11.1 | 13.14 | 44.9% | 26.3% |
| MW gen1_elo | 5,171 | 13.0 | 8.6 | 19.7 | 15.0 | 18.2 | 15.2 | 10.2 | 12.62 | 43.7% | 25.5% |
| MW gen1_ledger | 6,064 | 13.2 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.2% |
| MW gen1_sr | 5,171 | 9.5 | 7.0 | 16.6 | 13.4 | 22.3 | 18.5 | 12.7 | 16.46 | 53.5% | 31.2% |
| MW gen2 | 5,171 | 11.2 | 6.3 | 16.5 | 14.6 | 20.3 | 17.2 | 14.0 | 15.59 | 51.5% | 31.2% |
| all families model4_conditioned | 2,816 | 18.6 | 15.4 | 29.6 | 23.8 | 8.4 | 2.4 | 1.9 | 7.37 | 12.6% | 4.3% |
| all families model4_fundamental | 2,825 | 14.6 | 10.7 | 29.9 | 21.7 | 14.6 | 5.5 | 3.0 | 9.1 | 23.1% | 8.5% |

Configurable thresholds (primary): >=5pp 77.9%, >=10pp 58.6%, >=15pp 43.7%, >=20pp 33.2%, >=25pp 24.1%, >=30pp 17.7%, >=40pp 9.6%, >=50pp 4.4%
Executable gap (model outside the book, before fees): median 10.31pp; >=10pp 50.8%, >=25pp 21.3%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 22.3 | 17.4 | 27.3 | 12.8 | 14.9 | 1.6 | 3.7 | 6.19 | 20.2% | 5.4% |
| CHALLENGER | 906 | 14.7 | 9.5 | 15.9 | 16.0 | 15.6 | 15.3 | 13.0 | 13.33 | 43.9% | 28.4% |
| ITF_MEN | 1,657 | 11.8 | 8.3 | 19.9 | 15.1 | 17.6 | 14.8 | 12.7 | 12.81 | 45.0% | 27.5% |
| ITF_WOMEN | 1,845 | 10.4 | 6.1 | 15.5 | 15.3 | 21.5 | 19.4 | 11.9 | 16.12 | 52.7% | 31.3% |
| WTA | 435 | 23.0 | 10.6 | 25.8 | 12.6 | 18.9 | 6.7 | 2.5 | 8.16 | 28.1% | 9.2% |
| WTA125 | 86 | 13.9 | 4.7 | 18.6 | 24.4 | 19.8 | 13.9 | 4.7 | 12.4 | 38.4% | 18.6% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 23.1 | 12.8 | 24.8 | 16.1 | 17.4 | 1.6 | 4.1 | 7.29 | 23.1% | 5.8% |
| CHALLENGER | 906 | 11.4 | 5.0 | 18.0 | 16.1 | 19.1 | 17.6 | 12.9 | 14.92 | 49.6% | 30.5% |
| ITF_MEN | 1,657 | 9.8 | 6.5 | 17.4 | 15.3 | 20.3 | 16.7 | 14.1 | 15.45 | 51.1% | 30.8% |
| ITF_WOMEN | 1,845 | 8.7 | 6.1 | 13.8 | 12.5 | 20.6 | 19.8 | 18.4 | 18.84 | 58.9% | 38.3% |
| WTA | 435 | 20.5 | 5.5 | 16.8 | 15.6 | 22.3 | 16.8 | 2.5 | 12.98 | 41.6% | 19.3% |
| WTA125 | 86 | 5.8 | 5.8 | 16.3 | 20.9 | 23.3 | 15.1 | 12.8 | 15.56 | 51.2% | 27.9% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 242 | 28.1 | 12.8 | 28.5 | 10.7 | 9.1 | 7.0 | 3.7 | 6.53 | 19.8% | 10.7% |
| CHALLENGER | 906 | 15.4 | 8.2 | 21.5 | 13.4 | 13.5 | 14.6 | 13.5 | 11.48 | 41.5% | 28.0% |
| ITF_MEN | 1,657 | 10.1 | 9.4 | 18.6 | 15.9 | 18.3 | 15.4 | 12.2 | 13.33 | 46.0% | 27.7% |
| ITF_WOMEN | 1,845 | 9.8 | 6.3 | 16.3 | 14.6 | 23.6 | 19.2 | 10.2 | 16.62 | 53.0% | 29.4% |
| WTA | 435 | 23.4 | 14.0 | 29.4 | 15.6 | 11.5 | 4.4 | 1.6 | 6.99 | 17.5% | 6.0% |
| WTA125 | 86 | 17.4 | 5.8 | 22.1 | 30.2 | 12.8 | 10.5 | 1.2 | 10.92 | 24.4% | 11.6% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 72 | 23.6 | 22.2 | 34.7 | 12.5 | 6.9 | 0.0 | 0.0 | 6.26 | 6.9% | 0.0% |
| CHALLENGER | 813 | 21.2 | 13.9 | 26.6 | 16.0 | 13.3 | 6.5 | 2.6 | 7.45 | 22.4% | 9.1% |
| DOUBLES | 383 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.6 | 27.4 | 24.04 | 70.0% | 48.0% |
| ITF_MEN | 2,056 | 14.2 | 9.1 | 18.9 | 14.0 | 20.8 | 13.5 | 9.5 | 12.43 | 43.8% | 23.0% |
| ITF_WOMEN | 1,891 | 8.9 | 8.3 | 17.4 | 14.1 | 24.0 | 18.4 | 8.9 | 15.55 | 51.3% | 27.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 363 | 15.4 | 9.4 | 25.6 | 22.3 | 17.6 | 8.8 | 0.8 | 9.8 | 27.3% | 9.6% |
| WTA125 | 337 | 13.3 | 9.5 | 21.7 | 16.9 | 22.9 | 11.9 | 3.9 | 11.35 | 38.6% | 15.7% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 22.0 | 17.4 | 27.4 | 12.9 | 14.9 | 1.7 | 3.7 | 6.21 | 20.3% | 5.4% |
| CHALLENGER | 664 | 18.7 | 11.9 | 19.4 | 19.3 | 16.9 | 8.7 | 5.1 | 10.05 | 30.7% | 13.9% |
| ITF_MEN | 1,035 | 15.8 | 11.8 | 25.0 | 16.9 | 17.3 | 9.5 | 3.8 | 9.46 | 30.5% | 13.2% |
| ITF_WOMEN | 1,234 | 14.2 | 8.0 | 18.5 | 17.7 | 22.9 | 14.1 | 4.7 | 12.75 | 41.6% | 18.8% |
| WTA | 434 | 23.0 | 10.6 | 25.8 | 12.7 | 18.9 | 6.5 | 2.5 | 8.16 | 27.9% | 9.0% |
| WTA125 | 83 | 14.5 | 4.8 | 19.3 | 25.3 | 19.3 | 12.1 | 4.8 | 11.65 | 36.1% | 16.9% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 241 | 23.2 | 12.4 | 24.9 | 16.2 | 17.4 | 1.7 | 4.2 | 7.5 | 23.2% | 5.8% |
| CHALLENGER | 664 | 14.3 | 6.3 | 22.7 | 19.7 | 20.3 | 12.5 | 4.1 | 11.79 | 36.9% | 16.6% |
| ITF_MEN | 1,035 | 13.4 | 7.9 | 21.9 | 17.7 | 21.4 | 12.5 | 5.2 | 11.66 | 39.0% | 17.7% |
| ITF_WOMEN | 1,234 | 10.4 | 8.1 | 15.7 | 12.2 | 23.7 | 17.8 | 12.1 | 16.3 | 53.6% | 29.9% |
| WTA | 434 | 20.5 | 5.5 | 16.8 | 15.7 | 22.4 | 16.6 | 2.5 | 12.96 | 41.5% | 19.1% |
| WTA125 | 83 | 6.0 | 6.0 | 15.7 | 21.7 | 24.1 | 15.7 | 10.8 | 15.33 | 50.6% | 26.5% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 62 | 24.2 | 25.8 | 35.5 | 12.9 | 1.6 | 0.0 | 0.0 | 5.45 | 1.6% | 0.0% |
| CHALLENGER | 662 | 23.6 | 16.3 | 29.5 | 15.7 | 12.4 | 2.4 | 0.1 | 6.68 | 14.9% | 2.6% |
| DOUBLES | 344 | 5.8 | 3.8 | 10.2 | 10.5 | 21.8 | 20.9 | 27.0 | 24.02 | 69.8% | 48.0% |
| ITF_MEN | 1,458 | 17.3 | 11.1 | 22.1 | 15.2 | 20.8 | 9.9 | 3.5 | 9.87 | 34.2% | 13.4% |
| ITF_WOMEN | 1,277 | 11.0 | 9.9 | 21.1 | 16.2 | 25.1 | 14.6 | 2.1 | 12.17 | 41.8% | 16.8% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 334 | 15.6 | 9.9 | 26.4 | 23.1 | 18.3 | 6.9 | 0.0 | 9.55 | 25.1% | 6.9% |
| WTA125 | 259 | 15.8 | 10.4 | 25.9 | 20.1 | 21.2 | 6.2 | 0.4 | 9.54 | 27.8% | 6.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 383 | 5.7 | 3.9 | 9.9 | 10.4 | 21.9 | 20.6 | 27.4 | 24.04 | 70.0% | 48.0% |
| singles | 5,681 | 13.7 | 9.8 | 20.7 | 15.0 | 20.3 | 13.3 | 7.2 | 11.81 | 40.8% | 20.5% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Clay | 1,112 | 15.2 | 8.5 | 18.8 | 14.6 | 15.7 | 13.8 | 13.4 | 12.47 | 42.9% | 27.2% |
| Hard | 3,700 | 12.6 | 8.4 | 18.7 | 14.9 | 19.4 | 15.6 | 10.3 | 13.36 | 45.4% | 25.9% |
| UNKNOWN | 359 | 14.5 | 5.8 | 14.2 | 19.2 | 19.2 | 15.9 | 11.1 | 13.77 | 46.2% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,596 | 17.1 | 10.1 | 20.7 | 14.7 | 17.2 | 11.6 | 8.7 | 10.46 | 37.4% | 20.2% |
| B | 756 | 16.7 | 10.6 | 17.2 | 16.8 | 16.1 | 10.8 | 11.8 | 11.51 | 38.8% | 22.6% |
| C | 847 | 12.0 | 8.3 | 22.6 | 13.1 | 16.5 | 15.7 | 11.8 | 12.93 | 44.0% | 27.5% |
| D | 956 | 11.1 | 7.4 | 17.1 | 14.8 | 20.7 | 16.1 | 12.8 | 14.75 | 49.6% | 28.9% |
| F | 1,016 | 7.8 | 4.4 | 13.6 | 16.7 | 22.5 | 22.8 | 12.1 | 18.33 | 57.5% | 34.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 1,869 | 18.7 | 12.0 | 26.1 | 16.7 | 16.4 | 7.0 | 3.2 | 8.65 | 26.5% | 10.1% |
| B | 1,003 | 13.7 | 9.6 | 21.3 | 16.1 | 19.4 | 12.6 | 7.4 | 11.65 | 39.4% | 19.9% |
| C | 1,250 | 11.2 | 8.4 | 15.8 | 13.8 | 22.2 | 15.4 | 13.2 | 15.33 | 50.8% | 28.6% |
| D | 931 | 11.1 | 8.1 | 20.5 | 11.9 | 24.3 | 15.4 | 8.8 | 14.28 | 48.4% | 24.2% |
| F | 1,011 | 7.0 | 7.1 | 12.2 | 13.3 | 23.1 | 24.2 | 13.0 | 18.91 | 60.3% | 37.2% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 1,998 | 16.4 | 9.5 | 19.7 | 15.8 | 16.8 | 11.8 | 10.1 | 11.07 | 38.6% | 21.9% |
| LIMITED | 1,183 | 14.4 | 10.2 | 21.6 | 13.1 | 16.3 | 13.8 | 10.6 | 11.67 | 40.7% | 24.3% |
| POOR | 1,990 | 9.5 | 5.8 | 15.2 | 15.8 | 21.9 | 19.5 | 12.3 | 16.59 | 53.7% | 31.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 341 | 34.3 | 22.9 | 33.1 | 6.5 | 2.4 | 0.9 | 0.0 | 4.16 | 3.2% | 0.9% |
| GAME_SPREAD | 406 | 19.9 | 16.5 | 37.0 | 16.0 | 8.9 | 1.2 | 0.5 | 6.59 | 10.6% | 1.7% |
| MATCH_WINNER | 6,064 | 13.2 | 9.4 | 20.0 | 14.7 | 20.4 | 13.8 | 8.4 | 12.23 | 42.6% | 22.2% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 1,702 | 21.7 | 13.4 | 30.6 | 17.2 | 13.6 | 2.8 | 0.7 | 7.04 | 17.0% | 3.4% |
| TOTAL_GAMES | 1,132 | 9.9 | 9.4 | 26.5 | 24.9 | 17.0 | 8.0 | 4.4 | 10.66 | 29.3% | 12.4% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 887 | 28.6 | 32.6 | 26.8 | 0.7 | 9.1 | 1.7 | 0.5 | 4.28 | 11.3% | 2.1% |
| GAME_SPREAD | 565 | 36.6 | 15.0 | 25.3 | 17.9 | 2.5 | 1.9 | 0.7 | 4.55 | 5.1% | 2.6% |
| TOTAL_GAMES | 1,364 | 4.5 | 4.5 | 33.1 | 41.3 | 10.3 | 3.1 | 3.2 | 10.72 | 16.6% | 6.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 887 | 26.2 | 16.7 | 33.6 | 8.1 | 9.9 | 4.5 | 1.0 | 5.79 | 15.4% | 5.5% |
| GAME_SPREAD | 565 | 17.5 | 10.3 | 25.5 | 23.2 | 15.9 | 5.1 | 2.5 | 9.56 | 23.5% | 7.6% |
| TOTAL_GAMES | 1,373 | 5.8 | 7.0 | 29.4 | 29.9 | 17.0 | 6.3 | 4.4 | 10.91 | 27.8% | 10.8% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5,171 | 44.9% | 26.3% | 13.14 | 33.4% | 14.3% | 10.09 |
| gen1_elo | 5,171 | 43.7% | 25.5% | 12.62 | 31.6% | 14.3% | 9.53 |
| gen1_sr | 5,171 | 53.5% | 31.2% | 16.46 | 43.4% | 19.6% | 12.86 |
| gen2 | 5,171 | 51.5% | 31.2% | 15.59 | 43.0% | 21.2% | 12.93 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 1,989 | 17.6 | 11.9 | 22.9 | 15.8 | 18.4 | 10.1 | 3.3 | 9.53 | 31.8% | 13.4% |
| STALE | 3,182 | 10.6 | 6.0 | 15.7 | 14.7 | 18.7 | 18.4 | 15.9 | 16.86 | 53.0% | 34.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,284 | 15.2 | 10.4 | 21.9 | 15.9 | 19.9 | 12.0 | 4.6 | 10.71 | 36.5% | 16.7% |
| STALE | 2,780 | 10.9 | 8.3 | 17.7 | 13.2 | 21.1 | 15.9 | 12.9 | 14.89 | 49.9% | 28.8% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 11,235 | 0 | 5273 | 5962 | 31.1 | 228.9 | 1400.4 |
| ge_15pp | 4,907 | 0 | 1833 | 3074 | 39.7 | 519.4 | 1380.4 |
| ge_25pp | 2,705 | 0 | 813 | 1892 | 54.4 | 637.8 | 1380.4 |
| lt_10pp | 4,653 | 0 | 2602 | 2051 | 28.4 | 54.9 | 1201.9 |

Current slate `SL-20261003T215023Z-7a3e14cf`: 146 priced rows, quote age at build {'median': 30.1, 'max': 30.2}, freshness {'STALE': 146}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXTERNAL_LONE_OUTLIER | 1 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.56 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 137 | 22.6 | 10.9 | 20.4 | 20.4 | 19.7 | 5.1 | 0.7 | 7.82 | 25.6% | 5.8% |
| MARKETS_AGREE | 8 | 50.0 | 50.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.96 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 12 | 0.0 | 0.0 | 8.3 | 50.0 | 41.7 | 0.0 | 0.0 | 14.32 | 41.7% | 0.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 5,171 | 158 (3.1%) | 7.6% | 0.0% | {"EXTERNAL_STALE": 137, "AGREES_WITH_KALSHI": 12, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1} |
| fair_v1_ge_15pp | 2,321 | 40 (1.7%) | 12.5% | 0.0% | {"EXTERNAL_STALE": 35, "AGREES_WITH_KALSHI": 5} |
| fair_v1_ge_25pp | 1,358 | 8 (0.6%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_ge_25pp_pregame_clean | 527 | 8 (1.5%) | 0.0% | 0.0% | {"EXTERNAL_STALE": 8} |
| fair_v1_lt_10pp | 2,066 | 84 (4.1%) | 1.2% | 0.0% | {"EXTERNAL_STALE": 74, "ALL_AGREE": 8, "EXTERNAL_OUTLIER": 1, "AGREES_WITH_KALSHI": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 1,018 | 11.9 | 7.1 | 18.9 | 15.8 | 19.8 | 16.2 | 10.3 | 13.54 | 46.4% | 26.5% |
| 4-10x | 687 | 12.1 | 8.6 | 17.9 | 15.6 | 17.5 | 16.4 | 11.9 | 13.92 | 45.9% | 28.4% |
| <2x | 2,843 | 14.6 | 9.2 | 19.1 | 14.8 | 18.1 | 13.2 | 11.0 | 12.15 | 42.4% | 24.2% |
| >=10x | 623 | 10.8 | 5.5 | 15.4 | 15.4 | 20.2 | 21.2 | 11.6 | 16.44 | 53.0% | 32.7% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 1,412 | 14.2 | 8.8 | 20.1 | 15.2 | 17.2 | 12.5 | 12.0 | 12.01 | 41.7% | 24.5% |
| 300-1000 | 1,245 | 12.8 | 7.3 | 17.0 | 15.7 | 20.1 | 16.2 | 10.8 | 14.14 | 47.1% | 27.1% |
| <300 | 1,226 | 8.6 | 5.6 | 14.8 | 14.8 | 21.4 | 21.9 | 12.9 | 17.89 | 56.1% | 34.8% |
| >=3000 | 1,288 | 17.2 | 11.1 | 21.4 | 14.8 | 16.1 | 10.9 | 8.5 | 10.07 | 35.5% | 19.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 199 | 0.5165 | 0.3843 | 0.4221 | +0.094 | -0.038 | 0.0121 ± 0.0103 |
| ratio 4-10x | 142 | 0.5839 | 0.4465 | 0.4789 | +0.105 | -0.032 | 0.0147 ± 0.0125 |
| ratio <2x | 410 | 0.5337 | 0.4151 | 0.4659 | +0.068 | -0.051 | 0.0103 ± 0.0068 |
| ratio >=10x | 138 | 0.5484 | 0.3885 | 0.4493 | +0.099 | -0.061 | 0.02 ± 0.0154 |
| thinner_sample 1000-3000 | 238 | 0.539 | 0.4194 | 0.458 | +0.081 | -0.039 | 0.009 ± 0.0089 |
| thinner_sample 300-1000 | 253 | 0.5553 | 0.4266 | 0.4704 | +0.085 | -0.044 | 0.0052 ± 0.0091 |
| thinner_sample <300 | 276 | 0.5366 | 0.3781 | 0.442 | +0.095 | -0.064 | 0.0226 ± 0.0104 |
| thinner_sample >=3000 | 122 | 0.5191 | 0.4227 | 0.4508 | +0.068 | -0.028 | 0.0148 ± 0.01 |
| data_status ADEQUATE | 259 | 0.5284 | 0.4207 | 0.4556 | +0.073 | -0.035 | 0.0079 ± 0.0076 |
| data_status LIMITED | 194 | 0.5575 | 0.4354 | 0.5 | +0.058 | -0.065 | 0.0021 ± 0.0106 |
| data_status POOR | 436 | 0.5394 | 0.3905 | 0.4358 | +0.104 | -0.045 | 0.0208 ± 0.0077 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 148 | 0.1761 | 0.1768 | -0.0007 ± 0.0012 | 0.5249 | 0.5268 | 0.4957 | 0.4813 | 0.4932 | -0.093 ± 0.0376 | -0.01 (3) |
| 3-5 | 92 | 0.1755 | 0.1747 | +0.0009 ± 0.0036 | 0.5322 | 0.5255 | 0.5215 | 0.4805 | 0.4891 | -0.084 ± 0.0466 | 0.02 (1) |
| 5-10 | 188 | 0.2021 | 0.2055 | -0.0034 ± 0.005 | 0.5903 | 0.5982 | 0.5149 | 0.4403 | 0.4947 | -0.046 ± 0.0335 | -0.0167 (3) |
| 10-15 | 153 | 0.2161 | 0.2105 | +0.0056 ± 0.0093 | 0.6157 | 0.6032 | 0.5212 | 0.3971 | 0.4379 | -0.065 ± 0.0366 | -0.0633 (3) |
| 15-25 | 191 | 0.2128 | 0.209 | +0.0038 ± 0.0129 | 0.613 | 0.599 | 0.562 | 0.3657 | 0.4555 | -0.023 ± 0.0322 | -0.02 (4) |
| 25-40 | 91 | 0.2376 | 0.1801 | +0.0574 ± 0.0276 | 0.6642 | 0.5322 | 0.618 | 0.3043 | 0.3626 | -0.080 ± 0.042 | -0.01 (1) |
| 40+ | 26 | 0.3509 | 0.1453 | +0.2057 ± 0.0675 | 0.9495 | 0.453 | 0.7195 | 0.2762 | 0.2692 | -0.176 ± 0.0753 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 451 | 0.165 | 0.166 | -0.0011 ± 0.0006 | 0.4963 | 0.499 | 0.5079 | 0.4932 | 0.5322 | -0.023 ± 0.0201 | -0.0188 (8) |
| 3-5 | 277 | 0.1778 | 0.1779 | -0.0001 ± 0.0021 | 0.537 | 0.5306 | 0.4977 | 0.4575 | 0.4801 | -0.036 ± 0.0261 | 0.02 (1) |
| 5-10 | 656 | 0.1858 | 0.1843 | +0.0015 ± 0.0025 | 0.5522 | 0.5467 | 0.474 | 0.4001 | 0.4284 | -0.029 ± 0.0169 | -0.0129 (7) |
| 10-15 | 544 | 0.1947 | 0.1789 | +0.0158 ± 0.0045 | 0.5712 | 0.5234 | 0.4743 | 0.3504 | 0.3493 | -0.062 ± 0.018 | -0.0633 (3) |
| 15-25 | 712 | 0.1928 | 0.1587 | +0.0341 ± 0.0059 | 0.5733 | 0.4712 | 0.4814 | 0.2836 | 0.2935 | -0.047 ± 0.0147 | -0.017 (10) |
| 25-40 | 644 | 0.2127 | 0.0933 | +0.1194 ± 0.0075 | 0.6178 | 0.3068 | 0.5017 | 0.1872 | 0.1568 | -0.076 ± 0.0117 | -0.01 (1) |
| 40+ | 480 | 0.3734 | 0.0342 | +0.3392 ± 0.0092 | 0.972 | 0.1479 | 0.6186 | 0.1027 | 0.0417 | -0.092 ± 0.0078 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 90 | 0.1786 | 0.1803 | -0.0017 ± 0.0015 | 0.5306 | 0.5331 | 0.5293 | 0.5147 | 0.5667 | -0.038 ± 0.0436 | -0.01 (1) |
| 3-5 | 69 | 0.2103 | 0.2079 | +0.0025 ± 0.0044 | 0.6015 | 0.6024 | 0.4928 | 0.4536 | 0.4348 | -0.091 ± 0.0576 | 0.02 (1) |
| 5-10 | 176 | 0.1862 | 0.1829 | +0.0033 ± 0.0049 | 0.5545 | 0.545 | 0.573 | 0.4974 | 0.5057 | -0.095 ± 0.0328 | -0.01 (4) |
| 10-15 | 155 | 0.2236 | 0.2113 | +0.0123 ± 0.0094 | 0.6363 | 0.6093 | 0.5757 | 0.451 | 0.471 | -0.080 ± 0.0379 | -0.0667 (3) |
| 15-25 | 217 | 0.2236 | 0.1964 | +0.0272 ± 0.0119 | 0.6329 | 0.5686 | 0.5845 | 0.3879 | 0.424 | -0.083 ± 0.0307 | -0.0167 (3) |
| 25-40 | 127 | 0.2527 | 0.1944 | +0.0582 ± 0.0242 | 0.7058 | 0.5642 | 0.6555 | 0.345 | 0.4016 | -0.090 ± 0.0401 | -0.025 (2) |
| 40+ | 55 | 0.3882 | 0.1943 | +0.1940 ± 0.0603 | 1.0783 | 0.5734 | 0.7552 | 0.262 | 0.3273 | -0.061 ± 0.0589 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 363 | 0.1582 | 0.16 | -0.0019 ± 0.0007 | 0.4775 | 0.4825 | 0.5457 | 0.531 | 0.5813 | -0.001 ± 0.0211 | -0.0217 (6) |
| 3-5 | 223 | 0.1774 | 0.1741 | +0.0033 ± 0.0022 | 0.5254 | 0.5229 | 0.5417 | 0.5024 | 0.4798 | -0.071 ± 0.028 | 0.02 (1) |
| 5-10 | 588 | 0.1785 | 0.1776 | +0.0008 ± 0.0027 | 0.5335 | 0.527 | 0.5206 | 0.4453 | 0.4745 | -0.027 ± 0.0175 | -0.01 (5) |
| 10-15 | 533 | 0.1906 | 0.1778 | +0.0128 ± 0.0046 | 0.5648 | 0.5238 | 0.5146 | 0.3905 | 0.409 | -0.039 ± 0.0185 | -0.0575 (4) |
| 15-25 | 761 | 0.2066 | 0.1583 | +0.0482 ± 0.0057 | 0.6017 | 0.4732 | 0.5139 | 0.3177 | 0.2983 | -0.084 ± 0.0144 | -0.0143 (7) |
| 25-40 | 692 | 0.2247 | 0.1168 | +0.1079 ± 0.0083 | 0.6518 | 0.3631 | 0.5444 | 0.229 | 0.2168 | -0.067 ± 0.0131 | -0.015 (6) |
| 40+ | 604 | 0.4065 | 0.059 | +0.3475 ± 0.0115 | 1.0681 | 0.2157 | 0.6626 | 0.1232 | 0.0844 | -0.072 ± 0.0095 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 142 | 0.1838 | 0.1854 | -0.0016 ± 0.0013 | 0.5394 | 0.5437 | 0.5148 | 0.5004 | 0.5282 | -0.055 ± 0.0364 | -0.01 (5) |
| 3-5 | 101 | 0.1706 | 0.1683 | +0.0022 ± 0.0033 | 0.5148 | 0.5094 | 0.5008 | 0.4614 | 0.4554 | -0.108 ± 0.0433 | -- (0) |
| 5-10 | 182 | 0.2066 | 0.2066 | +0.0000 ± 0.005 | 0.605 | 0.5992 | 0.5053 | 0.4326 | 0.467 | -0.059 ± 0.034 | -0.01 (3) |
| 10-15 | 156 | 0.2085 | 0.2049 | +0.0036 ± 0.009 | 0.6028 | 0.591 | 0.5486 | 0.425 | 0.4808 | -0.064 ± 0.0365 | -0.044 (5) |
| 15-25 | 187 | 0.2105 | 0.2013 | +0.0092 ± 0.0127 | 0.612 | 0.583 | 0.5758 | 0.3829 | 0.4545 | -0.042 ± 0.0316 | -0.03 (1) |
| 25-40 | 100 | 0.2346 | 0.1926 | +0.0420 ± 0.0271 | 0.6609 | 0.5634 | 0.608 | 0.2954 | 0.38 | -0.060 ± 0.0408 | 0.0 (1) |
| 40+ | 21 | 0.3707 | 0.1604 | +0.2102 ± 0.0791 | 0.9917 | 0.4892 | 0.7365 | 0.2879 | 0.2857 | -0.191 ± 0.0908 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 435 | 0.174 | 0.1741 | -0.0001 ± 0.0007 | 0.5181 | 0.5189 | 0.5097 | 0.4954 | 0.5034 | -0.050 ± 0.0201 | -0.0162 (13) |
| 3-5 | 301 | 0.1792 | 0.1746 | +0.0046 ± 0.0019 | 0.5342 | 0.5214 | 0.4874 | 0.4482 | 0.4153 | -0.092 ± 0.0243 | -0.01 (2) |
| 5-10 | 642 | 0.1917 | 0.1858 | +0.0059 ± 0.0026 | 0.5678 | 0.544 | 0.4682 | 0.3945 | 0.3941 | -0.054 ± 0.0171 | -0.01 (3) |
| 10-15 | 554 | 0.1894 | 0.1753 | +0.0141 ± 0.0044 | 0.5608 | 0.5192 | 0.4834 | 0.3601 | 0.3664 | -0.056 ± 0.0178 | -0.03 (9) |
| 15-25 | 754 | 0.1841 | 0.1485 | +0.0356 ± 0.0056 | 0.5558 | 0.4482 | 0.4892 | 0.2906 | 0.2997 | -0.047 ± 0.0137 | -0.03 (2) |
| 25-40 | 627 | 0.2135 | 0.0961 | +0.1173 ± 0.0078 | 0.6194 | 0.3114 | 0.4965 | 0.1791 | 0.1547 | -0.074 ± 0.0119 | 0.0 (1) |
| 40+ | 451 | 0.3919 | 0.034 | +0.3579 ± 0.0096 | 1.0217 | 0.1491 | 0.6262 | 0.1031 | 0.0333 | -0.100 ± 0.008 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 425 | 0.2044 | 0.2045 | -0.0000 ± 0.0007 | 0.5913 | 0.5917 | 0.4995 | 0.4848 | 0.4871 | -0.041 ± 0.022 | -0.0226 (46) |
| 3-5 | 310 | 0.1942 | 0.193 | +0.0012 ± 0.002 | 0.5701 | 0.5637 | 0.4628 | 0.423 | 0.4323 | -0.040 ± 0.0248 | -0.0059 (32) |
| 5-10 | 649 | 0.1888 | 0.1841 | +0.0046 ± 0.0025 | 0.5612 | 0.5484 | 0.4612 | 0.3878 | 0.3945 | -0.038 ± 0.0169 | -0.005 (72) |
| 10-15 | 432 | 0.2045 | 0.1928 | +0.0117 ± 0.0053 | 0.5985 | 0.5653 | 0.4587 | 0.3352 | 0.3495 | -0.036 ± 0.021 | 0.0016 (63) |
| 15-25 | 580 | 0.233 | 0.2088 | +0.0242 ± 0.0074 | 0.659 | 0.6039 | 0.5296 | 0.3367 | 0.3707 | -0.029 ± 0.0189 | -0.0216 (58) |
| 25-40 | 275 | 0.2693 | 0.1705 | +0.0988 ± 0.0156 | 0.7437 | 0.5114 | 0.5771 | 0.2659 | 0.2618 | -0.069 ± 0.0245 | -0.0216 (25) |
| 40+ | 94 | 0.4254 | 0.1611 | +0.2643 ± 0.0443 | 1.1952 | 0.4956 | 0.7368 | 0.2289 | 0.2447 | -0.060 ± 0.0429 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 787 | 0.1933 | 0.1927 | +0.0006 ± 0.0005 | 0.5648 | 0.5632 | 0.4929 | 0.4784 | 0.4651 | -0.054 ± 0.0156 | -0.0155 (82) |
| 3-5 | 559 | 0.1975 | 0.1957 | +0.0018 ± 0.0015 | 0.5752 | 0.5679 | 0.4687 | 0.4289 | 0.4275 | -0.046 ± 0.0187 | -0.018 (54) |
| 5-10 | 1188 | 0.1876 | 0.1812 | +0.0064 ± 0.0019 | 0.5582 | 0.5391 | 0.4463 | 0.3723 | 0.3704 | -0.043 ± 0.0124 | -0.0089 (122) |
| 10-15 | 872 | 0.199 | 0.1853 | +0.0136 ± 0.0036 | 0.5847 | 0.5459 | 0.4494 | 0.3259 | 0.3326 | -0.038 ± 0.0145 | -0.0053 (99) |
| 15-25 | 1218 | 0.2205 | 0.1865 | +0.0340 ± 0.0049 | 0.6362 | 0.5476 | 0.5036 | 0.3079 | 0.3186 | -0.040 ± 0.0124 | -0.0255 (106) |
| 25-40 | 832 | 0.2452 | 0.1279 | +0.1173 ± 0.0078 | 0.6918 | 0.4001 | 0.5285 | 0.2133 | 0.1863 | -0.073 ± 0.0122 | -0.0206 (47) |
| 40+ | 493 | 0.3885 | 0.0786 | +0.3098 ± 0.0138 | 1.0614 | 0.2646 | 0.6521 | 0.1365 | 0.1055 | -0.075 ± 0.0129 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 889 | 1.105 ± 0.095 | 1.217 | 0.1715 | 0.1838 | 0.2077 | 0.1948 |
| gen2 | 889 | 0.927 ± 0.084 | 1.144 | 0.1884 | 0.1829 | 0.225 | 0.1952 |
| gen1_elo | 889 | 1.085 ± 0.093 | 1.196 | 0.1765 | 0.1841 | 0.2071 | 0.1948 |
| gen1_sr | 889 | 1.127 ± 0.109 | 1.213 | 0.1438 | 0.1853 | 0.2206 | 0.1947 |
| gen1_ledger | 2765 | 0.885 ± 0.051 | 1.059 | 0.1624 | 0.1993 | 0.2196 | 0.1926 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 4,907)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,655 | 33.7% |
| STALE_QUOTE | market_freshness | 1,419 | 28.9% |
| POOR_DATA | data | 389 | 7.9% |
| BOOK_QUALITY | execution | 333 | 6.8% |
| LIMITED_DATA | data | 303 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 289 | 5.9% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 245 | 5.0% |
| IN_PLAY_QUOTE | market_freshness/coverage | 173 | 3.5% |
| IDENTITY_AMBIGUOUS | mapping | 98 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 3 | 0.1% |

Cause class: coverage 33.7%, market_freshness 28.9%, data 14.1%, market_freshness/coverage 9.4%, execution 6.8%, model_calibration_or_unknown 5.0%, mapping 2.0%, model_calibration 0.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 99.9%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 63.7%, STALE_KALSHI_QUOTE 62.6%, STALE_PLAYER_DATA 53.2%, THIN_PLAYER_HISTORY 51.5%, MODEL_INTERNAL_DISAGREEMENT 33.2%, ASYMMETRIC_SAMPLE_SIZE 28.1%, WIDE_SPREAD 14.8%, MODEL_HIGH_UNCERTAINTY 14.2%, PLAYER_IDENTITY_RISK 10.7%, LEVEL_TRANSFER_RISK 8.2%, EVENT_MAPPING_RISK 6.6%, LOW_DISPLAYED_LIQUIDITY 5.0%, MODEL_CALIBRATION_OUTLIER 2.2%, UNKNOWN 0.8%, EXTERNAL_MARKET_REJECTION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.4%, POST_SETTLEMENT_OBSERVATION 33.7%, POSSIBLE_IN_PLAY_QUOTE 6.7%, CONFIRMED_IN_PLAY_QUOTE 1.2%

### >= ge_25 pp (N = 2,705)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 1,288 | 47.6% |
| STALE_QUOTE | market_freshness | 630 | 23.3% |
| POOR_DATA | data | 167 | 6.2% |
| BOOK_QUALITY | execution | 162 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 146 | 5.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 102 | 3.8% |
| LIMITED_DATA | data | 81 | 3.0% |
| IDENTITY_AMBIGUOUS | mapping | 71 | 2.6% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 58 | 2.1% |

Cause class: coverage 47.6%, market_freshness 23.3%, data 9.2%, market_freshness/coverage 9.2%, execution 6.0%, mapping 2.6%, model_calibration_or_unknown 2.1%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 100.0%, START_UNVERIFIABLE 96.8%, STALE_KALSHI_QUOTE 69.9%, LOW_DATA_QUALITY 67.4%, THIN_PLAYER_HISTORY 53.7%, STALE_PLAYER_DATA 50.6%, MODEL_INTERNAL_DISAGREEMENT 34.1%, ASYMMETRIC_SAMPLE_SIZE 30.4%, MODEL_HIGH_UNCERTAINTY 15.7%, WIDE_SPREAD 13.4%, PLAYER_IDENTITY_RISK 13.3%, EVENT_MAPPING_RISK 8.0%, LEVEL_TRANSFER_RISK 7.6%, LOW_DISPLAYED_LIQUIDITY 5.5%, MODEL_CALIBRATION_OUTLIER 3.1%, UNKNOWN 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 50.4%, POST_SETTLEMENT_OBSERVATION 47.6%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 1.4%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 2314, "IDENTITY_AMBIGUOUS": 391}; ticker orientation: {"VERIFIED": 2705}.

Checks: discipline:AMBIGUOUS 184, discipline:PASS 2521, identity_confidence:AMBIGUOUS 359, identity_confidence:PASS 2346, level_mapping:NA 196, level_mapping:PASS 2509, market_pair:AMBIGUOUS 62, market_pair:NA 77, market_pair:PASS 2566, model_complement:NA 48, model_complement:PASS 2657, namesake:PASS 2705, physical_match_id:NA 1347, physical_match_id:PASS 1358, player_ids:PASS 2705, same_pair_other_event:PASS 2705, ticker_orientation:PASS 2705

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 314 | 4.1% | 4.3% | 0.5% | {"market_freshness": 12, "execution": 1} | 6.16 | 0.1791 / 0.1823 (49) | 39.2% | 0.0% | 0.6% | 3.5% |
| CHALLENGER | 1,719 | 19.3% | 8.2% | 12.2% | {"coverage": 183, "market_freshness": 74, "market_freshness/coverage": 39, "data": 18, "model_calibration_or_unknown": 13, "execution": 4} | 7.83 | 0.2253 / 0.2085 (548) | 51.7% | 3.9% | 0.7% | 22.9% |
| DOUBLES | 383 | 48.0% | 48.0% | 6.8% | {"market_freshness": 106, "execution": 32, "mapping": 27, "market_freshness/coverage": 12, "coverage": 7} | 24.02 | 0.3217 / 0.2283 (162) | 61.1% | 0.0% | 100.0% | 10.2% |
| ITF_MEN | 3,713 | 25.0% | 13.4% | 34.3% | {"coverage": 522, "market_freshness": 163, "data": 87, "market_freshness/coverage": 72, "execution": 72, "mapping": 10, "model_calibration_or_unknown": 1} | 9.7 | 0.2133 / 0.1884 (1327) | 55.3% | 49.0% | 5.2% | 32.9% |
| ITF_WOMEN | 3,736 | 29.3% | 17.8% | 40.4% | {"coverage": 563, "market_freshness": 228, "data": 124, "market_freshness/coverage": 85, "execution": 44, "mapping": 32, "model_calibration_or_unknown": 18} | 12.49 | 0.2063 / 0.1862 (1178) | 57.6% | 54.1% | 6.6% | 32.8% |
| OTHER | 149 | 8.1% | 7.3% | 0.4% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 7.41 | 0.1411 / 0.1522 (42) | 28.2% | 4.0% | 4.0% | 8.1% |
| WTA | 798 | 9.4% | 8.1% | 2.8% | {"market_freshness": 34, "model_calibration_or_unknown": 12, "data": 11, "market_freshness/coverage": 9, "execution": 4, "coverage": 4, "mapping": 1} | 8.66 | 0.2006 / 0.1964 (129) | 40.5% | 2.6% | 1.5% | 3.8% |
| WTA125 | 423 | 16.3% | 9.1% | 2.5% | {"market_freshness/coverage": 30, "model_calibration_or_unknown": 12, "market_freshness": 11, "data": 8, "coverage": 8} | 10.39 | 0.2261 / 0.2035 (219) | 34.3% | 9.0% | 0.5% | 19.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 2 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 3 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 4 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 5 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 6 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 7 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 8 | `KXITFWMATCH-26SEP30BARGAR-BAR` | ITF_WOMEN | fair_v1 | 80% / 2% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 571 min (STALE); data POOR (grade F, thinner serve sample 149.0, ratio 14.2); no external reference |
| 9 | `KXWTADOUBLES-26SEP18DABSTEQUESAL-QUESAL` | DOUBLES | gen1_ledger | 86% / 9% | +77 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 48 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 10 | `KXITFMATCH-26SEP17TIUBES-TIU` | ITF_MEN | gen1_ledger | 87% / 10% | +77 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.5h before the model priced it (a finished match); the quote was captured 13 min before settlement (in-play print); quote age at model time 105 min (STALE); data LIMITED (grade B, thinner serve sample 1868.0, ratio 1.45); no external reference |
| 11 | `KXITFWMATCH-26SEP17HUAKHO-KHO` | ITF_WOMEN | gen1_ledger | 82% / 6% | +76 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 2526.0, ratio 2.48); no external reference |
| 12 | `KXATPDOUBLES-26SEP23GALGORMANMUL-MANMUL` | DOUBLES | gen1_ledger | 97% / 21% | +76 | BOOK_QUALITY | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 29 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXITFMATCH-26SEP20BATMIN-MIN` | ITF_MEN | gen1_ledger | 81% / 6% | +75 | POSSIBLY_IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 87 min before settlement (in-play print); quote age at model time 23 min (AGING); data POOR (grade F, thinner serve sample 76.0, ratio 26.82); no external reference |
| 14 | `KXITFWMATCH-26SEP30CABLAM-LAM` | ITF_WOMEN | fair_v1 | 77% / 2% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.5h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 406 min (STALE); data POOR (grade F, thinner serve sample 74.0, ratio 16.35); no external reference |
| 15 | `KXITFWMATCH-26SEP23PETOKU-OKU` | ITF_WOMEN | gen1_ledger | 83% / 8% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.7h before the model priced it (a finished match); the quote was captured 24 min before settlement (in-play print); quote age at model time 186 min (STALE); data LIMITED (grade C, thinner serve sample 2197.0, ratio 1.62); no external reference |
| 16 | `KXITFMATCH-26OCT01BRACOQ-BRA` | ITF_MEN | fair_v1 | 78% / 4% | +75 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 328 min (STALE); data POOR (grade D, thinner serve sample 446.0, ratio 4.88); no external reference |
| 17 | `KXITFWMATCH-26SEP25KHOWAN-KHO` | ITF_WOMEN | gen1_ledger | 87% / 12% | +75 | LIMITED_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 17 min (AGING); data LIMITED (grade C, thinner serve sample 3118.0, ratio 2.01); no external reference |
| 18 | `KXITFWMATCH-26SEP22SAMMES-SAM` | ITF_WOMEN | gen1_ledger | 82% / 8% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 33 min before settlement (in-play print); quote age at model time 204 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 3.53); no external reference |
| 19 | `KXITFMATCH-26OCT03HOULOC-HOU` | ITF_MEN | fair_v1 | 78% / 4% | +74 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 408 min (STALE); data POOR (grade F, thinner serve sample 4430.0, ratio 1.14); no external reference |
| 20 | `KXWTADOUBLES-26SEP24CHAFANBACJAN-BACJAN` | DOUBLES | gen1_ledger | 95% / 21% | +74 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 43 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 21 | `KXITFMATCH-26SEP16KOLGRI-KOL` | ITF_MEN | gen1_ledger | 77% / 4% | +73 | IN_PLAY_QUOTE | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 34 min before settlement (in-play print); quote age at model time 26 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1395.78); no external reference |
| 22 | `KXITFWMATCH-26SEP23KAMABB-ABB` | ITF_WOMEN | gen1_ledger | 76% / 2% | +73 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 75 min (STALE); data POOR (grade D, thinner serve sample 1000.0, ratio 2.78); no external reference |
| 23 | `KXATPCHALLENGERMATCH-26OCT01NAKSMI-SMI` | CHALLENGER | fair_v1 | 86% / 12% | +73 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 22 min (AGING); data POOR (grade D, thinner serve sample 451.0, ratio 12.18); no external reference |
| 24 | `KXITFWMATCH-26SEP13HADLUK-LUK` | ITF_WOMEN | gen1_ledger | 76% / 3% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 109 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 3326.68); no external reference |
| 25 | `KXITFMATCH-26SEP12NAWBRO-NAW` | ITF_MEN | gen1_ledger | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 46 min (STALE); data POOR (grade D, thinner serve sample 802.0, ratio 5.29); no external reference |
| 26 | `KXITFWMATCH-26OCT03ZELSUS-ZEL` | ITF_WOMEN | fair_v1 | 76% / 4% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 527 min (STALE); data POOR (grade D, thinner serve sample 527.0, ratio 4.73); no external reference |
| 27 | `KXITFMATCH-26OCT02ZGOPAP-PAP` | ITF_MEN | fair_v1 | 94% / 22% | +72 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 114 min (STALE); data POOR (grade D, thinner serve sample 63.0, ratio 48.25); no external reference |
| 28 | `KXITFWMATCH-26SEP25GALGAR-GAR` | ITF_WOMEN | gen1_ledger | 73% / 2% | +72 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 23 min before settlement (in-play print); quote age at model time 18 min (AGING); data LIMITED (grade C, thinner serve sample 576.0, ratio 4.5); no external reference |
| 29 | `KXITFMATCH-26SEP24PIEDAR-PIE` | ITF_MEN | gen1_ledger | 86% / 14% | +72 | POOR_DATA | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | quote age at model time 18 min (AGING); data POOR (grade F, thinner serve sample 300.0, ratio 13.88); no external reference |
| 30 | `KXATPCHALLENGERDOUBLES-26SEP30REYSANDOMTOR-DOMTOR` | DOUBLES | gen1_ledger | 86% / 15% | +71 | IDENTITY_AMBIGUOUS | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 31 | `KXATPCHALLENGERMATCH-26SEP28MARLAN-LAN` | CHALLENGER | fair_v1 | 74% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 66 min (STALE); data LIMITED (grade C, thinner serve sample 897.0, ratio 5.46); no external reference |
| 32 | `KXITFWMATCH-26SEP26KRODAN-KRO` | ITF_WOMEN | gen1_ledger | 86% / 14% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 100 min (STALE); data LIMITED (grade C, thinner serve sample 851.0, ratio 5.62); no external reference |
| 33 | `KXATPCHALLENGERMATCH-26SEP28BONHOL-BON` | CHALLENGER | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 73 min (STALE); no external reference |
| 34 | `KXITFMATCH-26SEP28SUSCHE-CHE` | ITF_MEN | gen1_ledger | 72% / 2% | +71 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 159 min (STALE); data POOR (grade F, thinner serve sample 126.0, ratio 9.06); no external reference |
| 35 | `KXWTADOUBLES-26SEP20GARHSIMIHNIC-GARHSI` | DOUBLES | gen1_ledger | 96% / 25% | +71 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 36 | `KXITFWMATCH-26SEP29LOLANS-ANS` | ITF_WOMEN | fair_v1 | 77% / 6% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 16 min before settlement (in-play print); quote age at model time 114 min (STALE); data LIMITED (grade B, thinner serve sample 2163.0, ratio 2.0); no external reference |
| 37 | `KXITFMATCH-26OCT01KROKUP-KUP` | ITF_MEN | fair_v1 | 74% / 4% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 183 min (STALE); data POOR (grade D, thinner serve sample 442.0, ratio 3.44); no external reference |
| 38 | `KXWTAMATCH-26OCT01YASCHW-CHW` | WTA | fair_v1 | 73% / 2% | +70 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 51 min (STALE); no external reference |
| 39 | `KXITFMATCH-26SEP22OVCPOR-OVC` | ITF_MEN | gen1_ledger | 72% / 2% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 85 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 441.42); no external reference |
| 40 | `KXATPCHALLENGERMATCH-26SEP28FERREM-FER` | CHALLENGER | fair_v1 | 77% / 8% | +70 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.9h before the model priced it (a finished match); the quote was captured 3 min before settlement (in-play print); quote age at model time 476 min (STALE); no external reference |
| 41 | `KXWTADOUBLES-26SEP20CHAFANCHARAK-CHARAK` | DOUBLES | gen1_ledger | 98% / 29% | +70 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 40 min (STALE); identity AMBIGUOUS (identity_confidence, market_pair, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 42 | `KXITFMATCH-26SEP23BIDGRI-BID` | ITF_MEN | gen1_ledger | 71% / 2% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade D, thinner serve sample 351.0, ratio 3.98); no external reference |
| 43 | `KXITFWMATCH-26SEP30KOKUEM-KOK` | ITF_WOMEN | fair_v1 | 79% / 10% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 15 min before settlement (in-play print); quote age at model time 776 min (STALE); data LIMITED (grade C, thinner serve sample 824.0, ratio 2.35); no external reference |
| 44 | `KXITFMATCH-26SEP20WILRAH-RAH` | ITF_MEN | gen1_ledger | 72% / 4% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 83 min (STALE); data LIMITED (grade B, thinner serve sample 2782.0, ratio 1.84); no external reference |
| 45 | `KXITFMATCH-26SEP26NAGTHO-NAG` | ITF_MEN | gen1_ledger | 76% / 7% | +69 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 89 min (STALE); data LIMITED (grade C, thinner serve sample 1323.0, ratio 4.45); no external reference |
| 46 | `KXITFWMATCH-26SEP26PERPRE-PER` | ITF_WOMEN | gen1_ledger | 78% / 10% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 102 min (STALE); data POOR (grade D, thinner serve sample 1020.0, ratio 2.77); no external reference |
| 47 | `KXITFMATCH-26SEP22YILAGA-AGA` | ITF_MEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 203 min (STALE); data LIMITED (grade B, thinner serve sample 2786.0, ratio 2.08); no external reference |
| 48 | `KXITFMATCH-26SEP30DIMURA-URA` | ITF_MEN | fair_v1 | 71% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 819 min (STALE); data POOR (grade F, thinner serve sample 174.0, ratio 2.63); no external reference |
| 49 | `KXITFWMATCH-26OCT01TANVED-TAN` | ITF_WOMEN | fair_v1 | 76% / 8% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 8.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 492 min (STALE); no external reference |
| 50 | `KXITFWMATCH-26SEP20LLIBON-BON` | ITF_WOMEN | gen1_ledger | 70% / 2% | +68 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 69 min (STALE); data POOR (grade D, thinner serve sample 1210.0, ratio 3.0); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9674, "by_level_share_of_ge_25pp": {"ATP": 0.0048, "CHALLENGER": 0.1224, "DOUBLES": 0.068, "ITF_MEN": 0.3427, "ITF_WOMEN": 0.4044, "OTHER": 0.0044, "WTA": 0.0277, "WTA125": 0.0255}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.6994, "share_primary_cause_market_settled_or_in_play": 0.5679, "share_primary_cause_stale_quote_only": 0.2329}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 2705, "identity_ambiguous_share": 0.1445, "ticker_orientation": {"VERIFIED": 2705}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 1358, "with_external": 8, "coverage": 0.0059, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}, "pregame_clean_ge_25pp": {"n": 527, "with_external": 8, "coverage": 0.0152, "external_status": {"EXTERNAL_STALE": 8}, "triangulation": {"INSUFFICIENT_INPUTS": 8}, "share_external_agrees_with_kalshi": 0.0, "share_external_supports_model": 0.0}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 827.0, "median_sample_ratio": 2.25, "median_min_matches": 28.0, "median_max_days_since_last": 172.0, "share_severe_asymmetry": 0.1649, "data_status": {"POOR": 1245, "LIMITED": 912, "ADEQUATE": 548}, "comparison_lt_10pp": {"median_thinner_serve_points": 1967.0, "median_sample_ratio": 1.71, "median_min_matches": 80.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 199, "model_minus_observed": 0.0944, "kalshi_minus_observed": -0.0378, "brier_diff_model_minus_kalshi": 0.0121}, "4-10x": {"n": 142, "model_minus_observed": 0.105, "kalshi_minus_observed": -0.0324, "brier_diff_model_minus_kalshi": 0.0147}, "<2x": {"n": 410, "model_minus_observed": 0.0678, "kalshi_minus_observed": -0.0508, "brier_diff_model_minus_kalshi": 0.0103}, ">=10x": {"n": 138, "model_minus_observed": 0.0991, "kalshi_minus_observed": -0.0608, "brier_diff_model_minus_kalshi": 0.02}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 889, "model": {"intercept": -0.63, "slope": 0.927, "slope_se": 0.084}, "kalshi_mid_same_rows": {"intercept": 0.188, "slope": 1.144, "slope_se": 0.093}, "mean_extremity_model": 0.1884, "mean_extremity_kalshi": 0.1829, "model_brier": 0.225, "kalshi_brier": 0.1952, "brier_diff_model_minus_kalshi": 0.0298, "brier_diff_se": 0.0063, "model_logloss": 0.6431, "kalshi_logloss": 0.5697}, "fair_v1": {"n": 889, "model": {"intercept": -0.423, "slope": 1.105, "slope_se": 0.095}, "kalshi_mid_same_rows": {"intercept": 0.318, "slope": 1.217, "slope_se": 0.097}, "mean_extremity_model": 0.1715, "mean_extremity_kalshi": 0.1838, "model_brier": 0.2077, "kalshi_brier": 0.1948, "brier_diff_model_minus_kalshi": 0.0129, "brier_diff_se": 0.005, "model_logloss": 0.6007, "kalshi_logloss": 0.5688}, "gen1_elo": {"n": 889, "model": {"intercept": -0.423, "slope": 1.085, "slope_se": 0.093}, "kalshi_mid_same_rows": {"intercept": 0.3, "slope": 1.196, "slope_se": 0.095}, "mean_extremity_model": 0.1765, "mean_extremity_kalshi": 0.1841, "model_brier": 0.2071, "kalshi_brier": 0.1948, "brier_diff_model_minus_kalshi": 0.0123, "brier_diff_se": 0.005, "model_logloss": 0.6008, "kalshi_logloss": 0.5687}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2626, "share_ge_15": 0.4488, "median_abs_gap": 13.14, "n": 5171}, "gen1_elo": {"share_ge_25": 0.2549, "share_ge_15": 0.4372, "median_abs_gap": 12.62, "n": 5171}, "gen1_sr": {"share_ge_25": 0.3117, "share_ge_15": 0.5349, "median_abs_gap": 16.46, "n": 5171}, "gen2": {"share_ge_25": 0.3121, "share_ge_15": 0.515, "median_abs_gap": 15.59, "n": 5171}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1428, "share_ge_15": 0.3343, "median_abs_gap": 10.09, "n": 3691}, "gen1_elo": {"share_ge_25": 0.1428, "share_ge_15": 0.3164, "median_abs_gap": 9.53, "n": 3691}, "gen1_sr": {"share_ge_25": 0.1959, "share_ge_15": 0.434, "median_abs_gap": 12.86, "n": 3691}, "gen2": {"share_ge_25": 0.2116, "share_ge_15": 0.4302, "median_abs_gap": 12.93, "n": 3691}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 6.16, "share_ge_25_all": 0.0414, "share_ge_25_pregame_clean": 0.0429}, "WTA": {"median_abs_gap_pregame_clean": 8.66, "share_ge_25_all": 0.094, "share_ge_25_pregame_clean": 0.0807}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2213, "share_within_10pp_all": 0.4142, "share_within_10pp_pregame_clean": 0.4961, "corr_model_vs_mid_pregame_clean": 0.8285}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 148, "model_brier": 0.1761, "kalshi_brier": 0.1768, "brier_diff_model_minus_kalshi": -0.0007}, "10-15": {"n_settled": 153, "model_brier": 0.2161, "kalshi_brier": 0.2105, "brier_diff_model_minus_kalshi": 0.0056}, "15-25": {"n_settled": 191, "model_brier": 0.2128, "kalshi_brier": 0.209, "brier_diff_model_minus_kalshi": 0.0038}, "25-40": {"n_settled": 91, "model_brier": 0.2376, "kalshi_brier": 0.1801, "brier_diff_model_minus_kalshi": 0.0574}, "3-5": {"n_settled": 92, "model_brier": 0.1755, "kalshi_brier": 0.1747, "brier_diff_model_minus_kalshi": 0.0009}, "40+": {"n_settled": 26, "model_brier": 0.3509, "kalshi_brier": 0.1453, "brier_diff_model_minus_kalshi": 0.2057}, "5-10": {"n_settled": 188, "model_brier": 0.2021, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": -0.0034}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.555, "slope": 0.885, "slope_se": 0.051}, "kalshi_slope": {"intercept": 0.092, "slope": 1.059, "slope_se": 0.053}, "n": 2765}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 162, "model_brier": 0.3217, "kalshi_brier": 0.2283, "brier_diff_model_minus_kalshi": 0.0934, "brier_diff_se": 0.0257, "corr_model_outcome": -0.0972, "corr_kalshi_outcome": 0.3367}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
