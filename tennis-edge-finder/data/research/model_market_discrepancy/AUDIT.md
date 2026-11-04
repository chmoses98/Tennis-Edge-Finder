# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-04T16:06Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 77,144): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.4%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.6%, Challenger 10.8%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 16,688): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.3%, STALE_QUOTE 19.6%, BOOK_QUALITY 18.0%, POOR_DATA 9.5%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.3%, market_freshness 19.6%, execution 18.0%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.7% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 16,688 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.4% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 476.0 points vs 1733.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.043, Gen-2 0.835, Gen-1 ledger 0.872 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 840 model 0.2205 vs Kalshi 0.2048; n 179 model 0.2922 vs Kalshi 0.1802.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 330,606 model-market comparisons (539,472 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 110,091 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-04T15:46:26.291209+00:00'], shadow board 88,650 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-04T15:46:30.981730+00:00'], Model 4 41,660 rows, 27,129 settled tickers, 10,236 tickers with an external scan.
* By model: {"gen1_ledger": 74399, "gen1_elo": 44549, "fair_v1": 44549, "gen2": 44549, "gen1_sr": 44549, "model4_fundamental": 39047, "model4_conditioned": 38964}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 77,144 | 14.1 | 9.6 | 20.2 | 15.4 | 19.1 | 13.6 | 8.0 | 11.81 | 40.7% | 21.6% |
| MW fair_v1 | 44,549 | 12.9 | 8.7 | 18.8 | 15.5 | 19.6 | 14.8 | 9.8 | 12.98 | 44.1% | 24.5% |
| MW gen1_elo | 44,549 | 12.6 | 8.8 | 19.4 | 15.4 | 19.5 | 14.6 | 9.7 | 12.74 | 43.8% | 24.3% |
| MW gen1_ledger | 32,595 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.28 | 36.1% | 17.7% |
| MW gen1_sr | 44,549 | 10.2 | 7.3 | 16.8 | 13.9 | 20.6 | 18.6 | 12.5 | 15.71 | 51.8% | 31.1% |
| MW gen2 | 44,549 | 11.1 | 7.6 | 16.7 | 13.8 | 19.5 | 17.7 | 13.6 | 15.37 | 50.8% | 31.3% |
| all families model4_conditioned | 38,964 | 22.2 | 18.1 | 34.2 | 17.1 | 5.0 | 2.2 | 1.2 | 6.06 | 8.4% | 3.4% |
| all families model4_fundamental | 39,047 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.33pp; >=10pp 44.8%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,877 | 28.3 | 15.5 | 27.7 | 13.4 | 10.7 | 3.7 | 0.6 | 5.84 | 15.0% | 4.3% |
| CHALLENGER | 6,725 | 16.1 | 9.9 | 20.8 | 15.3 | 16.0 | 11.3 | 10.6 | 10.85 | 38.0% | 22.0% |
| ITF_MEN | 12,392 | 9.9 | 7.3 | 16.9 | 15.1 | 21.4 | 17.4 | 12.0 | 15.27 | 50.8% | 29.4% |
| ITF_WOMEN | 17,304 | 9.5 | 7.1 | 16.0 | 15.1 | 22.1 | 18.2 | 12.0 | 15.75 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,945 | 16.9 | 13.0 | 24.7 | 21.1 | 16.3 | 6.8 | 1.1 | 8.68 | 24.2% | 7.9% |
| WTA125 | 1,300 | 15.8 | 7.0 | 22.7 | 20.0 | 20.5 | 12.2 | 1.8 | 10.67 | 34.5% | 14.0% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,877 | 26.8 | 15.7 | 26.1 | 15.4 | 11.5 | 3.7 | 0.8 | 6.06 | 16.0% | 4.5% |
| CHALLENGER | 6,725 | 15.0 | 9.0 | 18.6 | 14.1 | 18.5 | 13.4 | 11.3 | 12.42 | 43.3% | 24.8% |
| ITF_MEN | 12,392 | 8.1 | 6.2 | 15.2 | 13.7 | 19.8 | 20.7 | 16.4 | 17.94 | 56.9% | 37.0% |
| ITF_WOMEN | 17,304 | 7.8 | 5.8 | 14.1 | 12.8 | 20.6 | 21.2 | 17.6 | 19.08 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,945 | 14.3 | 10.2 | 21.9 | 16.0 | 22.1 | 12.9 | 2.6 | 11.07 | 37.6% | 15.6% |
| WTA125 | 1,300 | 10.2 | 7.2 | 16.5 | 15.5 | 24.2 | 17.4 | 8.9 | 15.18 | 50.5% | 26.3% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,877 | 22.8 | 13.9 | 25.1 | 15.6 | 15.2 | 6.2 | 1.2 | 7.3 | 22.5% | 7.4% |
| CHALLENGER | 6,725 | 15.2 | 9.5 | 20.9 | 15.7 | 16.0 | 11.9 | 10.8 | 11.18 | 38.7% | 22.7% |
| ITF_MEN | 12,392 | 9.3 | 7.2 | 17.3 | 14.3 | 22.0 | 17.4 | 12.5 | 15.72 | 51.9% | 29.9% |
| ITF_WOMEN | 17,304 | 9.3 | 6.9 | 16.4 | 15.9 | 22.2 | 18.1 | 11.3 | 15.52 | 51.6% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,945 | 22.9 | 16.8 | 31.9 | 15.0 | 9.0 | 3.3 | 1.1 | 6.12 | 13.4% | 4.4% |
| WTA125 | 1,300 | 21.3 | 13.2 | 25.8 | 18.5 | 15.1 | 5.8 | 0.3 | 8.01 | 21.1% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,287 | 26.3 | 19.7 | 30.2 | 12.4 | 8.3 | 2.6 | 0.4 | 5.4 | 11.4% | 3.1% |
| CHALLENGER | 4,342 | 22.4 | 14.6 | 27.4 | 14.6 | 13.7 | 5.8 | 1.6 | 7.09 | 21.1% | 7.4% |
| DOUBLES | 2,384 | 5.1 | 4.4 | 12.5 | 10.6 | 20.5 | 24.9 | 22.1 | 23.62 | 67.5% | 47.0% |
| ITF_MEN | 9,257 | 12.9 | 9.5 | 21.1 | 15.8 | 21.5 | 13.2 | 6.0 | 11.89 | 40.7% | 19.1% |
| ITF_WOMEN | 11,244 | 13.4 | 9.2 | 19.9 | 15.7 | 21.3 | 15.1 | 5.5 | 12.28 | 41.9% | 20.5% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,705 | 24.2 | 16.1 | 30.9 | 16.8 | 9.2 | 2.7 | 0.2 | 6.57 | 12.1% | 2.9% |
| WTA125 | 1,227 | 25.4 | 13.0 | 21.4 | 19.0 | 13.1 | 6.7 | 1.5 | 7.67 | 21.3% | 8.2% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,764 | 28.7 | 15.7 | 28.1 | 13.4 | 10.5 | 3.3 | 0.3 | 5.69 | 14.1% | 3.6% |
| CHALLENGER | 4,775 | 20.6 | 12.2 | 25.6 | 17.9 | 16.0 | 6.0 | 1.6 | 8.21 | 23.6% | 7.6% |
| ITF_MEN | 9,156 | 12.0 | 8.6 | 20.4 | 17.2 | 22.2 | 14.1 | 5.5 | 12.5 | 41.8% | 19.6% |
| ITF_WOMEN | 12,891 | 11.3 | 8.5 | 18.7 | 17.2 | 24.0 | 15.2 | 5.1 | 13.28 | 44.3% | 20.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,838 | 17.2 | 13.1 | 25.0 | 21.5 | 16.4 | 6.3 | 0.6 | 8.52 | 23.3% | 6.9% |
| WTA125 | 1,256 | 16.1 | 6.9 | 22.4 | 20.2 | 20.9 | 11.9 | 1.6 | 10.67 | 34.4% | 13.5% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,764 | 27.1 | 16.1 | 26.3 | 15.4 | 11.4 | 3.3 | 0.4 | 5.98 | 15.1% | 3.7% |
| CHALLENGER | 4,775 | 18.8 | 11.3 | 23.2 | 16.5 | 18.9 | 9.3 | 1.9 | 9.06 | 30.1% | 11.2% |
| ITF_MEN | 9,157 | 9.5 | 7.3 | 17.6 | 15.8 | 21.5 | 18.8 | 9.5 | 14.96 | 49.9% | 28.4% |
| ITF_WOMEN | 12,892 | 8.8 | 6.7 | 16.0 | 14.4 | 22.7 | 20.5 | 10.9 | 16.58 | 54.1% | 31.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,838 | 14.5 | 10.4 | 22.1 | 16.1 | 22.3 | 12.7 | 2.0 | 10.96 | 36.9% | 14.7% |
| WTA125 | 1,256 | 10.3 | 7.3 | 16.6 | 15.6 | 24.2 | 17.5 | 8.4 | 15.02 | 50.2% | 26.0% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,230 | 26.5 | 19.9 | 30.2 | 12.6 | 8.1 | 2.5 | 0.4 | 5.37 | 10.9% | 2.9% |
| CHALLENGER | 3,833 | 23.7 | 15.5 | 28.4 | 14.7 | 13.1 | 4.1 | 0.4 | 6.61 | 17.6% | 4.5% |
| DOUBLES | 2,241 | 5.0 | 4.5 | 12.7 | 10.8 | 20.3 | 24.8 | 22.0 | 23.54 | 67.1% | 46.8% |
| ITF_MEN | 7,953 | 13.7 | 10.1 | 22.7 | 16.3 | 21.5 | 11.7 | 4.0 | 11.01 | 37.2% | 15.7% |
| ITF_WOMEN | 9,631 | 14.1 | 9.7 | 21.0 | 16.2 | 21.5 | 14.0 | 3.5 | 11.46 | 39.1% | 17.6% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,644 | 24.5 | 16.6 | 30.8 | 16.8 | 9.1 | 2.1 | 0.1 | 6.43 | 11.3% | 2.2% |
| WTA125 | 1,092 | 26.5 | 13.8 | 22.3 | 20.0 | 12.2 | 4.8 | 0.5 | 7.2 | 17.4% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,384 | 5.1 | 4.4 | 12.5 | 10.6 | 20.5 | 24.9 | 22.1 | 23.62 | 67.5% | 47.0% |
| singles | 30,211 | 16.6 | 11.4 | 22.9 | 15.5 | 18.2 | 11.1 | 4.2 | 9.76 | 33.6% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 96 | 8.3 | 9.4 | 16.7 | 9.4 | 19.8 | 24.0 | 12.5 | 17.12 | 56.2% | 36.5% |
| Clay | 8,950 | 12.9 | 9.3 | 19.8 | 15.9 | 19.6 | 13.7 | 8.8 | 12.44 | 42.1% | 22.5% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 29,228 | 13.4 | 8.7 | 18.8 | 15.3 | 19.1 | 14.8 | 9.8 | 12.84 | 43.8% | 24.6% |
| UNKNOWN | 6,038 | 10.4 | 7.6 | 17.0 | 16.4 | 21.5 | 15.8 | 11.1 | 14.3 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 12,658 | 19.7 | 11.9 | 22.6 | 16.0 | 14.8 | 8.9 | 6.0 | 8.75 | 29.7% | 14.9% |
| B | 5,494 | 12.9 | 8.8 | 19.5 | 15.8 | 19.6 | 12.6 | 10.7 | 12.59 | 42.9% | 23.3% |
| C | 6,288 | 11.9 | 8.9 | 19.5 | 16.1 | 18.5 | 14.6 | 10.5 | 12.89 | 43.6% | 25.1% |
| D | 7,110 | 11.7 | 8.3 | 17.9 | 15.5 | 21.7 | 15.7 | 9.2 | 13.75 | 46.6% | 24.9% |
| F | 12,999 | 7.4 | 5.5 | 14.9 | 14.7 | 23.5 | 20.9 | 13.1 | 17.71 | 57.5% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,711 | 24.6 | 16.1 | 29.0 | 14.9 | 10.7 | 3.4 | 1.2 | 6.36 | 15.4% | 4.7% |
| B | 4,592 | 16.7 | 10.8 | 24.1 | 16.9 | 18.9 | 9.6 | 3.1 | 9.68 | 31.6% | 12.7% |
| C | 6,403 | 11.3 | 7.8 | 19.4 | 14.6 | 21.0 | 15.7 | 10.3 | 13.6 | 47.0% | 26.0% |
| D | 4,836 | 14.3 | 9.9 | 21.4 | 15.6 | 20.4 | 13.0 | 5.4 | 11.27 | 38.8% | 18.4% |
| F | 8,053 | 10.2 | 8.4 | 16.1 | 14.6 | 23.2 | 19.7 | 7.8 | 15.37 | 50.7% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,335 | 18.0 | 10.9 | 21.7 | 15.8 | 15.2 | 9.8 | 8.5 | 9.82 | 33.5% | 18.3% |
| LIMITED | 9,715 | 13.6 | 9.9 | 20.3 | 16.2 | 19.2 | 13.3 | 7.5 | 11.8 | 40.0% | 20.8% |
| POOR | 20,499 | 9.0 | 6.5 | 16.0 | 15.0 | 22.8 | 18.9 | 11.8 | 16.15 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,597 | 23.9 | 17.8 | 33.1 | 15.7 | 6.4 | 2.8 | 0.4 | 5.91 | 9.6% | 3.2% |
| GAME_SPREAD | 6,492 | 22.5 | 15.1 | 32.3 | 17.1 | 9.0 | 3.4 | 0.6 | 6.74 | 13.0% | 4.0% |
| MATCH_WINNER | 32,595 | 15.8 | 10.9 | 22.1 | 15.2 | 18.4 | 12.1 | 5.5 | 10.28 | 36.1% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,852 | 27.9 | 16.8 | 30.5 | 12.7 | 9.4 | 2.5 | 0.3 | 5.64 | 12.1% | 2.8% |
| TOTAL_GAMES | 10,839 | 9.9 | 10.9 | 35.4 | 26.1 | 10.5 | 4.3 | 3.0 | 9.22 | 17.8% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,836 | 24.5 | 28.9 | 33.3 | 8.1 | 4.0 | 1.0 | 0.3 | 4.79 | 5.2% | 1.3% |
| GAME_SPREAD | 9,008 | 46.7 | 16.2 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.31 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,120 | 6.6 | 9.8 | 40.2 | 30.2 | 7.4 | 3.4 | 2.4 | 9.23 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,871 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.5 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,017 | 20.5 | 13.5 | 28.2 | 20.1 | 12.0 | 4.5 | 1.2 | 7.64 | 17.7% | 5.7% |
| TOTAL_GAMES | 16,159 | 10.0 | 10.7 | 36.2 | 24.4 | 11.6 | 4.5 | 2.6 | 9.08 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 44,549 | 44.1% | 24.5% | 12.98 | 35.4% | 15.2% | 10.71 |
| gen1_elo | 44,549 | 43.8% | 24.3% | 12.74 | 35.0% | 15.1% | 10.5 |
| gen1_sr | 44,549 | 51.8% | 31.1% | 15.71 | 44.0% | 21.8% | 13.0 |
| gen2 | 44,549 | 50.8% | 31.3% | 15.37 | 43.9% | 23.3% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,722 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.3% | 15.3% |
| STALE | 24,827 | 10.8 | 7.3 | 16.8 | 14.1 | 19.2 | 17.0 | 14.9 | 15.42 | 51.1% | 31.9% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 26,063 | 16.4 | 11.2 | 22.7 | 15.2 | 17.9 | 11.6 | 4.8 | 9.89 | 34.4% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 77,144 | 26063 | 23194 | 27887 | 24.6 | 114.7 | 1451.1 |
| ge_15pp | 31,404 | 8957 | 8257 | 14190 | 27.8 | 420.6 | 1451.1 |
| ge_25pp | 16,688 | 4293 | 3603 | 8792 | 32.4 | 576.9 | 1431.1 |
| lt_10pp | 33,884 | 13131 | 10970 | 9783 | 22.6 | 47.3 | 1421.1 |

Current slate `SL-20261104T160618Z-648f4c64`: 545 priced rows, quote age at build {'median': 55.8, 'max': 75.8}, freshness {'STALE': 545}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,405 | 19.3 | 10.9 | 25.5 | 18.0 | 17.9 | 7.4 | 0.9 | 8.77 | 26.2% | 8.3% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 904 | 66.0 | 34.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,965 | 0.0 | 2.3 | 37.1 | 26.2 | 24.2 | 9.3 | 0.9 | 11.81 | 34.3% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 44,549 | 7379 (16.6%) | 26.6% | 1.0% | {"EXTERNAL_STALE": 4405, "AGREES_WITH_KALSHI": 1965, "ALL_AGREE": 904, "SUPPORTS_MODEL_DIRECTION": 48, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 27, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 19,648 | 1860 (9.5%) | 36.2% | 1.6% | {"EXTERNAL_STALE": 1156, "AGREES_WITH_KALSHI": 674, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,933 | 580 (5.3%) | 34.3% | 2.2% | {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,278 | 551 (10.4%) | 34.8% | 2.4% | {"EXTERNAL_STALE": 346, "AGREES_WITH_KALSHI": 192, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,984 | 4205 (23.4%) | 18.4% | 0.9% | {"EXTERNAL_STALE": 2455, "ALL_AGREE": 904, "AGREES_WITH_KALSHI": 776, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,665 | 10.4 | 7.7 | 19.4 | 14.8 | 21.7 | 16.1 | 9.9 | 14.01 | 47.6% | 25.9% |
| 4-10x | 5,941 | 11.1 | 8.5 | 18.6 | 15.4 | 22.1 | 14.2 | 10.0 | 13.71 | 46.3% | 24.2% |
| <2x | 22,844 | 15.1 | 9.8 | 19.8 | 16.2 | 17.5 | 13.0 | 8.7 | 11.5 | 39.2% | 21.7% |
| >=10x | 7,099 | 10.4 | 6.3 | 15.0 | 14.5 | 21.6 | 19.1 | 13.0 | 16.42 | 53.8% | 32.2% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 11,594 | 12.6 | 8.7 | 19.8 | 16.3 | 19.0 | 13.4 | 10.1 | 12.64 | 42.5% | 23.5% |
| 300-1000 | 9,588 | 11.8 | 8.8 | 17.8 | 15.5 | 20.6 | 16.2 | 9.4 | 13.61 | 46.2% | 25.5% |
| <300 | 14,063 | 8.3 | 5.8 | 15.1 | 14.8 | 23.1 | 20.0 | 13.0 | 17.12 | 56.1% | 33.0% |
| >=3000 | 9,304 | 21.4 | 13.0 | 24.1 | 15.7 | 13.8 | 7.1 | 5.0 | 7.68 | 25.8% | 12.0% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1328 | 0.5487 | 0.4097 | 0.4925 | +0.056 | -0.083 | -0.0009 ± 0.0042 |
| ratio 4-10x | 914 | 0.5807 | 0.4342 | 0.4891 | +0.092 | -0.055 | 0.0096 ± 0.0053 |
| ratio <2x | 3257 | 0.5371 | 0.4141 | 0.4406 | +0.097 | -0.026 | 0.0134 ± 0.0025 |
| ratio >=10x | 1108 | 0.5669 | 0.3932 | 0.4468 | +0.120 | -0.053 | 0.0152 ± 0.0054 |
| thinner_sample 1000-3000 | 1832 | 0.5393 | 0.4126 | 0.452 | +0.087 | -0.039 | 0.0091 ± 0.0034 |
| thinner_sample 300-1000 | 1502 | 0.5665 | 0.4257 | 0.482 | +0.085 | -0.056 | 0.0032 ± 0.004 |
| thinner_sample <300 | 2156 | 0.5597 | 0.391 | 0.4536 | +0.106 | -0.063 | 0.0137 ± 0.0038 |
| thinner_sample >=3000 | 1117 | 0.5294 | 0.4362 | 0.4485 | +0.081 | -0.012 | 0.0154 ± 0.0034 |
| data_status ADEQUATE | 1832 | 0.5311 | 0.4285 | 0.4416 | +0.089 | -0.013 | 0.0146 ± 0.0029 |
| data_status LIMITED | 1611 | 0.5493 | 0.4164 | 0.4724 | +0.077 | -0.056 | 0.0055 ± 0.0037 |
| data_status POOR | 3164 | 0.5622 | 0.4012 | 0.4618 | +0.100 | -0.060 | 0.0103 ± 0.0031 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 962 | 0.1985 | 0.199 | -0.0005 ± 0.0005 | 0.5771 | 0.5783 | 0.5019 | 0.4868 | 0.5031 | -0.093 ± 0.0152 | -0.0087 (8) |
| 3-5 | 602 | 0.2022 | 0.2019 | +0.0004 ± 0.0015 | 0.5867 | 0.5838 | 0.5033 | 0.4634 | 0.4784 | -0.102 ± 0.0188 | 0.01 (2) |
| 5-10 | 1416 | 0.1999 | 0.1995 | +0.0004 ± 0.0018 | 0.585 | 0.5817 | 0.5121 | 0.4383 | 0.4696 | -0.089 ± 0.0123 | -0.0143 (7) |
| 10-15 | 1148 | 0.2191 | 0.2096 | +0.0095 ± 0.0034 | 0.6307 | 0.603 | 0.5263 | 0.4027 | 0.4251 | -0.110 ± 0.0137 | -0.048 (5) |
| 15-25 | 1460 | 0.2244 | 0.2082 | +0.0162 ± 0.0047 | 0.6437 | 0.5998 | 0.5765 | 0.3814 | 0.4377 | -0.105 ± 0.012 | -0.004 (10) |
| 25-40 | 840 | 0.2205 | 0.2048 | +0.0157 ± 0.0093 | 0.6298 | 0.5907 | 0.6531 | 0.3432 | 0.4726 | -0.070 ± 0.0142 | -0.06 (2) |
| 40+ | 179 | 0.2922 | 0.1802 | +0.1120 ± 0.0283 | 0.7896 | 0.5357 | 0.7337 | 0.2796 | 0.3911 | -0.079 ± 0.0277 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5065 | 0.1854 | 0.1863 | -0.0009 ± 0.0002 | 0.5462 | 0.5472 | 0.4873 | 0.4721 | 0.5023 | -0.023 ± 0.0062 | -0.01 (28) |
| 3-5 | 3383 | 0.1959 | 0.1943 | +0.0016 ± 0.0006 | 0.5703 | 0.5643 | 0.4805 | 0.4407 | 0.4401 | -0.055 ± 0.0077 | 0.0 (3) |
| 5-10 | 7326 | 0.2004 | 0.1973 | +0.0030 ± 0.0008 | 0.5859 | 0.5753 | 0.4853 | 0.4117 | 0.4281 | -0.043 ± 0.0053 | -0.0114 (22) |
| 10-15 | 6075 | 0.202 | 0.1861 | +0.0159 ± 0.0014 | 0.5907 | 0.5464 | 0.4861 | 0.3623 | 0.36 | -0.064 ± 0.0056 | -0.0281 (16) |
| 15-25 | 7587 | 0.2062 | 0.1672 | +0.0390 ± 0.0018 | 0.6045 | 0.4968 | 0.4999 | 0.3044 | 0.3033 | -0.070 ± 0.0047 | -0.0027 (45) |
| 25-40 | 5860 | 0.2221 | 0.1266 | +0.0955 ± 0.0029 | 0.6383 | 0.3887 | 0.5269 | 0.2132 | 0.2222 | -0.058 ± 0.0045 | -0.0733 (3) |
| 40+ | 3866 | 0.3825 | 0.0457 | +0.3368 ± 0.0039 | 0.9964 | 0.1758 | 0.6321 | 0.1039 | 0.0613 | -0.076 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 771 | 0.2058 | 0.2063 | -0.0005 ± 0.0006 | 0.593 | 0.5946 | 0.5073 | 0.4926 | 0.5201 | -0.100 ± 0.0177 | -0.0117 (6) |
| 3-5 | 544 | 0.2115 | 0.2085 | +0.0030 ± 0.0016 | 0.6054 | 0.5993 | 0.5119 | 0.4723 | 0.4504 | -0.133 ± 0.021 | 0.01 (2) |
| 5-10 | 1213 | 0.2047 | 0.2024 | +0.0024 ± 0.002 | 0.5949 | 0.5877 | 0.5405 | 0.4659 | 0.4905 | -0.095 ± 0.0133 | -0.01 (4) |
| 10-15 | 1065 | 0.2119 | 0.2067 | +0.0052 ± 0.0035 | 0.6149 | 0.5991 | 0.5632 | 0.4389 | 0.4836 | -0.099 ± 0.0145 | -0.04 (5) |
| 15-25 | 1540 | 0.2308 | 0.2111 | +0.0197 ± 0.0046 | 0.6563 | 0.6062 | 0.5855 | 0.39 | 0.4396 | -0.103 ± 0.012 | -0.012 (10) |
| 25-40 | 1082 | 0.2675 | 0.1986 | +0.0688 ± 0.0085 | 0.746 | 0.5777 | 0.66 | 0.3461 | 0.3956 | -0.125 ± 0.0136 | -0.008 (5) |
| 40+ | 392 | 0.366 | 0.1661 | +0.1999 ± 0.0205 | 0.9979 | 0.4996 | 0.7357 | 0.2473 | 0.301 | -0.080 ± 0.0198 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4371 | 0.1922 | 0.1926 | -0.0004 ± 0.0002 | 0.5601 | 0.5607 | 0.5082 | 0.4931 | 0.5122 | -0.037 ± 0.0068 | -0.0154 (26) |
| 3-5 | 2967 | 0.1926 | 0.1916 | +0.0010 ± 0.0006 | 0.5612 | 0.558 | 0.5098 | 0.4701 | 0.4766 | -0.045 ± 0.0082 | 0.01 (2) |
| 5-10 | 6531 | 0.1972 | 0.1936 | +0.0036 ± 0.0008 | 0.5788 | 0.5658 | 0.5077 | 0.4336 | 0.4488 | -0.043 ± 0.0055 | -0.0117 (6) |
| 10-15 | 5439 | 0.202 | 0.1913 | +0.0107 ± 0.0015 | 0.5933 | 0.5598 | 0.5124 | 0.3885 | 0.408 | -0.046 ± 0.006 | -0.0189 (18) |
| 15-25 | 7584 | 0.2172 | 0.1806 | +0.0366 ± 0.0019 | 0.6313 | 0.53 | 0.5243 | 0.3291 | 0.3362 | -0.063 ± 0.0049 | -0.0084 (43) |
| 25-40 | 6898 | 0.251 | 0.1378 | +0.1132 ± 0.0028 | 0.708 | 0.421 | 0.56 | 0.2434 | 0.2263 | -0.082 ± 0.0045 | -0.0095 (20) |
| 40+ | 5372 | 0.4002 | 0.0606 | +0.3396 ± 0.0039 | 1.0551 | 0.2169 | 0.6546 | 0.1196 | 0.0836 | -0.072 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 928 | 0.1958 | 0.1973 | -0.0016 ± 0.0005 | 0.5709 | 0.5748 | 0.5003 | 0.4849 | 0.5323 | -0.051 ± 0.0152 | -0.012 (10) |
| 3-5 | 648 | 0.2066 | 0.2051 | +0.0015 ± 0.0014 | 0.5975 | 0.5919 | 0.4974 | 0.4578 | 0.4614 | -0.113 ± 0.0186 | -0.0 (4) |
| 5-10 | 1447 | 0.2011 | 0.1977 | +0.0034 ± 0.0018 | 0.5867 | 0.5766 | 0.5119 | 0.4382 | 0.4499 | -0.106 ± 0.0121 | -0.01 (9) |
| 10-15 | 1160 | 0.2106 | 0.2028 | +0.0078 ± 0.0033 | 0.6113 | 0.5885 | 0.5398 | 0.4167 | 0.4483 | -0.106 ± 0.0133 | -0.0286 (7) |
| 15-25 | 1394 | 0.2306 | 0.2126 | +0.0180 ± 0.0048 | 0.6587 | 0.6092 | 0.588 | 0.3935 | 0.444 | -0.111 ± 0.0124 | -0.03 (1) |
| 25-40 | 841 | 0.2123 | 0.21 | +0.0024 ± 0.0093 | 0.6125 | 0.6029 | 0.6619 | 0.351 | 0.5006 | -0.058 ± 0.0142 | -0.0267 (3) |
| 40+ | 189 | 0.3109 | 0.1834 | +0.1275 ± 0.028 | 0.8418 | 0.542 | 0.7436 | 0.2896 | 0.3862 | -0.093 ± 0.0286 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4864 | 0.1832 | 0.1839 | -0.0007 ± 0.0002 | 0.5402 | 0.5413 | 0.4822 | 0.4668 | 0.487 | -0.031 ± 0.0062 | -0.0137 (41) |
| 3-5 | 3447 | 0.2048 | 0.2031 | +0.0017 ± 0.0006 | 0.5935 | 0.5875 | 0.4808 | 0.4413 | 0.4407 | -0.056 ± 0.0078 | -0.01 (19) |
| 5-10 | 7506 | 0.1952 | 0.1904 | +0.0048 ± 0.0008 | 0.5733 | 0.5578 | 0.4875 | 0.4136 | 0.4178 | -0.054 ± 0.0051 | -0.0105 (37) |
| 10-15 | 5985 | 0.1934 | 0.1791 | +0.0143 ± 0.0014 | 0.5713 | 0.5299 | 0.4955 | 0.3723 | 0.3753 | -0.060 ± 0.0055 | -0.0146 (13) |
| 15-25 | 7702 | 0.2119 | 0.1725 | +0.0394 ± 0.0019 | 0.6181 | 0.5088 | 0.5141 | 0.3195 | 0.3165 | -0.072 ± 0.0047 | -0.0533 (3) |
| 25-40 | 5835 | 0.2171 | 0.1279 | +0.0892 ± 0.0029 | 0.6274 | 0.3917 | 0.5301 | 0.2145 | 0.2331 | -0.049 ± 0.0045 | -0.02 (4) |
| 40+ | 3823 | 0.3924 | 0.0508 | +0.3416 ± 0.0041 | 1.023 | 0.1888 | 0.6416 | 0.1103 | 0.0677 | -0.077 ± 0.0035 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1352 | 0.1954 | 0.1955 | -0.0001 ± 0.0004 | 0.5685 | 0.5684 | 0.5067 | 0.4917 | 0.4956 | -0.069 ± 0.0123 | -0.0213 (54) |
| 3-5 | 960 | 0.188 | 0.1876 | +0.0004 ± 0.0011 | 0.5535 | 0.5511 | 0.495 | 0.4552 | 0.4688 | -0.062 ± 0.0143 | -0.0194 (34) |
| 5-10 | 1957 | 0.1993 | 0.1947 | +0.0046 ± 0.0015 | 0.5865 | 0.5718 | 0.5069 | 0.4333 | 0.4389 | -0.076 ± 0.0102 | -0.005 (78) |
| 10-15 | 1346 | 0.2149 | 0.202 | +0.0129 ± 0.003 | 0.6222 | 0.5876 | 0.5406 | 0.4178 | 0.425 | -0.091 ± 0.0126 | 0.0014 (65) |
| 15-25 | 1741 | 0.2303 | 0.2072 | +0.0232 ± 0.0043 | 0.6577 | 0.5982 | 0.589 | 0.394 | 0.4348 | -0.089 ± 0.011 | -0.0214 (59) |
| 25-40 | 1068 | 0.2406 | 0.2099 | +0.0307 ± 0.0086 | 0.6875 | 0.6027 | 0.6862 | 0.3741 | 0.4813 | -0.089 ± 0.0131 | -0.0252 (27) |
| 40+ | 377 | 0.3284 | 0.2027 | +0.1257 ± 0.0222 | 0.949 | 0.5895 | 0.8158 | 0.3389 | 0.4615 | -0.098 ± 0.0209 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4977 | 0.1764 | 0.1766 | -0.0002 ± 0.0002 | 0.522 | 0.5219 | 0.5123 | 0.497 | 0.5075 | -0.039 ± 0.006 | -0.0145 (98) |
| 3-5 | 3414 | 0.1938 | 0.1928 | +0.0010 ± 0.0006 | 0.5653 | 0.5628 | 0.5011 | 0.4613 | 0.469 | -0.043 ± 0.0076 | -0.0204 (72) |
| 5-10 | 6947 | 0.1965 | 0.19 | +0.0065 ± 0.0008 | 0.5787 | 0.5599 | 0.5009 | 0.4273 | 0.4213 | -0.063 ± 0.0053 | -0.0084 (134) |
| 10-15 | 4790 | 0.21 | 0.1938 | +0.0162 ± 0.0016 | 0.6103 | 0.5685 | 0.5375 | 0.4146 | 0.409 | -0.072 ± 0.0064 | -0.0053 (106) |
| 15-25 | 5783 | 0.23 | 0.1995 | +0.0305 ± 0.0023 | 0.6614 | 0.5782 | 0.5747 | 0.3793 | 0.4003 | -0.066 ± 0.0059 | -0.026 (108) |
| 25-40 | 3864 | 0.2575 | 0.1893 | +0.0682 ± 0.0044 | 0.729 | 0.5519 | 0.6379 | 0.3253 | 0.3753 | -0.069 ± 0.0068 | -0.0246 (52) |
| 40+ | 1689 | 0.3729 | 0.1584 | +0.2144 ± 0.01 | 1.0544 | 0.4724 | 0.744 | 0.2428 | 0.2901 | -0.068 ± 0.0092 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6607 | 1.043 ± 0.034 | 1.118 | 0.1693 | 0.1678 | 0.2138 | 0.2035 |
| gen2 | 6607 | 0.835 ± 0.031 | 1.087 | 0.1733 | 0.1682 | 0.2325 | 0.2033 |
| gen1_elo | 6607 | 1.017 ± 0.033 | 1.107 | 0.176 | 0.1679 | 0.2133 | 0.2036 |
| gen1_sr | 6607 | 1.023 ± 0.041 | 1.147 | 0.1333 | 0.1699 | 0.2288 | 0.203 |
| gen1_ledger | 8801 | 0.872 ± 0.025 | 1.081 | 0.1894 | 0.1761 | 0.2165 | 0.1998 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 31,404)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,243 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,910 | 22.0% |
| BOOK_QUALITY | execution | 5,783 | 18.4% |
| POOR_DATA | data | 3,694 | 11.8% |
| LIMITED_DATA | data | 1,972 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,773 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,321 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,296 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 885 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 526 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.0%, execution 18.4%, data 18.0%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 60.0%, STALE_PLAYER_DATA 52.3%, STALE_KALSHI_QUOTE 45.2%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.6%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.5%, LEVEL_TRANSFER_RISK 10.2%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.4%, POST_SETTLEMENT_OBSERVATION 22.0%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 16,688)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,562 | 33.3% |
| STALE_QUOTE | market_freshness | 3,274 | 19.6% |
| BOOK_QUALITY | execution | 3,006 | 18.0% |
| POOR_DATA | data | 1,585 | 9.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 939 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 712 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 581 | 3.5% |
| LIMITED_DATA | data | 574 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 323 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 131 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.3%, market_freshness 19.6%, execution 18.0%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.1%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 52.7%, STALE_PLAYER_DATA 46.3%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.1%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.4%, POST_SETTLEMENT_OBSERVATION 33.3%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13275, "IDENTITY_AMBIGUOUS": 3413}; ticker orientation: {"VERIFIED": 16688}.

Checks: discipline:AMBIGUOUS 1120, discipline:PASS 15568, identity_confidence:AMBIGUOUS 3089, identity_confidence:PASS 13599, level_mapping:NA 1132, level_mapping:PASS 15556, market_pair:AMBIGUOUS 485, market_pair:NA 367, market_pair:PASS 15836, model_complement:NA 330, model_complement:PASS 16358, namesake:AMBIGUOUS 6, namesake:PASS 16682, physical_match_id:NA 5755, physical_match_id:PASS 10933, player_ids:PASS 16688, same_pair_other_event:PASS 16688, ticker_orientation:PASS 16688

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,164 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.56 | 0.2237 / 0.2187 (761) | 24.3% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,067 | 16.3% | 6.2% | 10.8% | {"coverage": 1051, "market_freshness/coverage": 213, "market_freshness": 209, "data": 157, "model_calibration_or_unknown": 76, "execution": 41, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.38 | 0.2207 / 0.2101 (2580) | 37.2% | 15.8% | 4.2% | 22.2% |
| DOUBLES | 2,384 | 47.0% | 46.8% | 6.7% | {"execution": 641, "mapping": 302, "market_freshness": 106, "market_freshness/coverage": 64, "coverage": 7} | 23.54 | 0.3031 / 0.2367 (574) | 9.8% | 0.0% | 100.0% | 6.0% |
| ITF_MEN | 21,649 | 25.0% | 17.8% | 32.4% | {"coverage": 1846, "market_freshness": 1052, "execution": 958, "data": 821, "market_freshness/coverage": 524, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.8 | 0.2152 / 0.1978 (4543) | 38.9% | 69.3% | 15.8% | 21.0% |
| ITF_WOMEN | 28,548 | 26.4% | 19.1% | 45.2% | {"coverage": 2584, "market_freshness": 1655, "execution": 1283, "data": 1082, "market_freshness/coverage": 646, "mapping": 183, "model_calibration_or_unknown": 86, "model_calibration": 22} | 12.55 | 0.2022 / 0.193 (5424) | 40.3% | 57.4% | 9.8% | 21.1% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,650 | 6.1% | 5.2% | 1.7% | {"market_freshness": 106, "model_calibration_or_unknown": 51, "coverage": 38, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.7 | 0.231 / 0.2233 (748) | 29.3% | 2.1% | 1.3% | 3.6% |
| WTA125 | 2,527 | 11.2% | 9.6% | 1.7% | {"market_freshness": 87, "model_calibration_or_unknown": 53, "market_freshness/coverage": 42, "data": 39, "execution": 24, "model_calibration": 19, "coverage": 14, "mapping": 4} | 9.17 | 0.2064 / 0.1905 (736) | 28.6% | 10.7% | 4.3% | 7.1% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 21.3h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1282 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 109 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 29 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 32 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 365 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXATPCHALLENGERMATCH-26NOV02TOBSTO-TOB` | CHALLENGER | fair_v1 | 80% / 2% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 165 min (STALE); data POOR (grade F, thinner serve sample 159.0, ratio 20.58); no external reference |
| 49 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 480 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 50 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9689, "by_level_share_of_ge_25pp": {"ATP": 0.0142, "CHALLENGER": 0.1079, "DOUBLES": 0.0671, "ITF_MEN": 0.3244, "ITF_WOMEN": 0.4519, "OTHER": 0.0007, "WTA": 0.017, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5268, "share_primary_cause_market_settled_or_in_play": 0.4244, "share_primary_cause_stale_quote_only": 0.1962}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 16688, "identity_ambiguous_share": 0.2045, "ticker_orientation": {"VERIFIED": 16688}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10933, "with_external": 580, "coverage": 0.0531, "external_status": {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 368, "MODEL_LONE_OUTLIER": 199, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3431, "share_external_supports_model": 0.0224}, "pregame_clean_ge_25pp": {"n": 5278, "with_external": 551, "coverage": 0.1044, "external_status": {"EXTERNAL_STALE": 346, "AGREES_WITH_KALSHI": 192, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 346, "MODEL_LONE_OUTLIER": 192, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3485, "share_external_supports_model": 0.0236}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 476.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2098, "data_status": {"POOR": 9425, "LIMITED": 4321, "ADEQUATE": 2942}, "comparison_lt_10pp": {"median_thinner_serve_points": 1733.0, "median_sample_ratio": 1.69, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1328, "model_minus_observed": 0.0562, "kalshi_minus_observed": -0.0828, "brier_diff_model_minus_kalshi": -0.0009}, "4-10x": {"n": 914, "model_minus_observed": 0.0916, "kalshi_minus_observed": -0.0549, "brier_diff_model_minus_kalshi": 0.0096}, "<2x": {"n": 3257, "model_minus_observed": 0.0965, "kalshi_minus_observed": -0.0264, "brier_diff_model_minus_kalshi": 0.0134}, ">=10x": {"n": 1108, "model_minus_observed": 0.1202, "kalshi_minus_observed": -0.0535, "brier_diff_model_minus_kalshi": 0.0152}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6607, "model": {"intercept": -0.557, "slope": 0.835, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.19, "slope": 1.087, "slope_se": 0.035}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1682, "model_brier": 0.2325, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0292, "brier_diff_se": 0.0023, "model_logloss": 0.6617, "kalshi_logloss": 0.5887}, "fair_v1": {"n": 6607, "model": {"intercept": -0.444, "slope": 1.043, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.265, "slope": 1.118, "slope_se": 0.036}, "mean_extremity_model": 0.1693, "mean_extremity_kalshi": 0.1678, "model_brier": 0.2138, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0103, "brier_diff_se": 0.0019, "model_logloss": 0.6162, "kalshi_logloss": 0.589}, "gen1_elo": {"n": 6607, "model": {"intercept": -0.433, "slope": 1.017, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.265, "slope": 1.107, "slope_se": 0.035}, "mean_extremity_model": 0.176, "mean_extremity_kalshi": 0.1679, "model_brier": 0.2133, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0098, "brier_diff_se": 0.0019, "model_logloss": 0.6156, "kalshi_logloss": 0.5892}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2454, "share_ge_15": 0.441, "median_abs_gap": 12.98, "n": 44549}, "gen1_elo": {"share_ge_25": 0.2429, "share_ge_15": 0.4379, "median_abs_gap": 12.74, "n": 44549}, "gen1_sr": {"share_ge_25": 0.3115, "share_ge_15": 0.5179, "median_abs_gap": 15.71, "n": 44549}, "gen2": {"share_ge_25": 0.3133, "share_ge_15": 0.5079, "median_abs_gap": 15.37, "n": 44549}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1521, "share_ge_15": 0.3543, "median_abs_gap": 10.71, "n": 34686}, "gen1_elo": {"share_ge_25": 0.1509, "share_ge_15": 0.35, "median_abs_gap": 10.5, "n": 34686}, "gen1_sr": {"share_ge_25": 0.2178, "share_ge_15": 0.4397, "median_abs_gap": 13.0, "n": 34688}, "gen2": {"share_ge_25": 0.2328, "share_ge_15": 0.4392, "median_abs_gap": 12.85, "n": 34688}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.56, "share_ge_25_all": 0.0384, "share_ge_25_pregame_clean": 0.0332}, "WTA": {"median_abs_gap_pregame_clean": 7.7, "share_ge_25_all": 0.0609, "share_ge_25_pregame_clean": 0.0518}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2374, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.4906, "corr_model_vs_mid_pregame_clean": 0.8499}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 962, "model_brier": 0.1985, "kalshi_brier": 0.199, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 1148, "model_brier": 0.2191, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1460, "model_brier": 0.2244, "kalshi_brier": 0.2082, "brier_diff_model_minus_kalshi": 0.0162}, "25-40": {"n_settled": 840, "model_brier": 0.2205, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0157}, "3-5": {"n_settled": 602, "model_brier": 0.2022, "kalshi_brier": 0.2019, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 179, "model_brier": 0.2922, "kalshi_brier": 0.1802, "brier_diff_model_minus_kalshi": 0.112}, "5-10": {"n_settled": 1416, "model_brier": 0.1999, "kalshi_brier": 0.1995, "brier_diff_model_minus_kalshi": 0.0004}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.557, "slope": 0.835, "slope_se": 0.031}, "kalshi_slope": {"intercept": 0.19, "slope": 1.087, "slope_se": 0.035}, "n": 6607}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.491, "slope": 0.872, "slope_se": 0.025}, "kalshi_slope": {"intercept": 0.174, "slope": 1.081, "slope_se": 0.029}, "n": 8801}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 574, "model_brier": 0.3031, "kalshi_brier": 0.2367, "brier_diff_model_minus_kalshi": 0.0664, "brier_diff_se": 0.0125, "corr_model_outcome": 0.0788, "corr_kalshi_outcome": 0.2466}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
