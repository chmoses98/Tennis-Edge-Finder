# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-10-29T14:09Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 67,966): 0-3 14.1%, 3-5 9.6%, 5-10 20.1%, 10-15 15.3%, 15-25 19.1%, 25-40 13.9%, 40+ 8.0%; median gap 11.87 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.9%, doubles 6.5%). Main tour: ATP 4.2% and WTA 5.7% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 14,848): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.7%, STALE_QUOTE 18.7%, BOOK_QUALITY 18.6%, POOR_DATA 9.5%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.1%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 2.1%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.7%, market_freshness 18.7%, execution 18.6%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 51.8% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 42.7% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 14,848 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.6% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 25.9% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 458.0 points vs 1651.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.018, Gen-2 0.809, Gen-1 ledger 0.859 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 715 model 0.2236 vs Kalshi 0.2068; n 150 model 0.2801 vs Kalshi 0.1888.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 290,042 model-market comparisons (473,312 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 97,211 rows ['2026-09-11T13:47:52.094820+00:00', '2026-10-29T13:52:15.859934+00:00'], shadow board 77,648 rows ['2026-09-28T03:33:22.503933+00:00', '2026-10-29T13:52:20.091541+00:00'], Model 4 36,459 rows, 23,502 settled tickers, 8,621 tickers with an external scan.
* By model: {"gen1_ledger": 65538, "gen1_elo": 39032, "fair_v1": 39032, "gen2": 39032, "gen1_sr": 39032, "model4_fundamental": 34210, "model4_conditioned": 34166}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 67,966 | 14.1 | 9.6 | 20.1 | 15.3 | 19.1 | 13.9 | 8.0 | 11.87 | 40.9% | 21.9% |
| MW fair_v1 | 39,032 | 12.9 | 8.7 | 18.6 | 15.4 | 19.5 | 14.9 | 9.8 | 13.02 | 44.3% | 24.8% |
| MW gen1_elo | 39,032 | 12.6 | 8.6 | 19.3 | 15.4 | 19.5 | 14.9 | 9.7 | 12.93 | 44.1% | 24.6% |
| MW gen1_ledger | 28,934 | 15.6 | 10.8 | 22.0 | 15.2 | 18.5 | 12.4 | 5.5 | 10.4 | 36.4% | 17.9% |
| MW gen1_sr | 39,032 | 10.1 | 7.2 | 16.9 | 13.8 | 20.7 | 18.6 | 12.8 | 15.85 | 52.0% | 31.3% |
| MW gen2 | 39,032 | 11.2 | 7.6 | 16.5 | 13.8 | 19.4 | 17.8 | 13.8 | 15.47 | 51.0% | 31.6% |
| all families model4_conditioned | 34,166 | 22.4 | 18.2 | 34.2 | 17.2 | 4.9 | 1.9 | 1.1 | 6.0 | 7.9% | 3.0% |
| all families model4_fundamental | 34,210 | 17.3 | 13.4 | 33.8 | 20.3 | 10.2 | 3.6 | 1.4 | 7.7 | 15.2% | 5.0% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.2%, >=15pp 40.9%, >=20pp 30.3%, >=25pp 21.9%, >=30pp 15.7%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.28pp; >=10pp 44.7%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,394 | 27.2 | 15.5 | 27.5 | 13.5 | 11.7 | 4.1 | 0.6 | 5.93 | 16.3% | 4.7% |
| CHALLENGER | 5,853 | 16.2 | 9.8 | 20.8 | 15.2 | 15.4 | 11.8 | 10.7 | 10.91 | 37.9% | 22.5% |
| ITF_MEN | 10,890 | 9.8 | 7.4 | 17.0 | 15.1 | 21.2 | 17.6 | 11.9 | 15.21 | 50.6% | 29.5% |
| ITF_WOMEN | 15,390 | 9.7 | 7.1 | 15.8 | 15.1 | 22.1 | 18.2 | 12.0 | 15.69 | 52.3% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,429 | 18.3 | 13.7 | 24.5 | 20.1 | 16.1 | 6.4 | 0.9 | 8.25 | 23.5% | 7.3% |
| WTA125 | 1,070 | 16.1 | 7.8 | 22.5 | 19.2 | 20.2 | 12.5 | 1.8 | 10.7 | 34.5% | 14.3% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,394 | 26.0 | 15.4 | 25.4 | 16.3 | 12.0 | 4.1 | 0.8 | 6.23 | 16.9% | 4.9% |
| CHALLENGER | 5,853 | 15.1 | 9.0 | 18.3 | 14.3 | 18.1 | 13.7 | 11.6 | 12.55 | 43.3% | 25.2% |
| ITF_MEN | 10,890 | 8.0 | 6.2 | 15.0 | 13.7 | 19.6 | 20.6 | 16.9 | 18.02 | 57.0% | 37.5% |
| ITF_WOMEN | 15,390 | 8.1 | 5.8 | 14.0 | 12.6 | 20.6 | 21.3 | 17.5 | 19.21 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,429 | 15.2 | 11.0 | 21.9 | 15.5 | 22.0 | 12.6 | 1.8 | 10.59 | 36.4% | 14.4% |
| WTA125 | 1,070 | 9.6 | 6.4 | 16.4 | 16.6 | 24.4 | 17.5 | 9.1 | 15.34 | 50.9% | 26.5% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,394 | 22.3 | 13.0 | 24.4 | 16.0 | 16.2 | 6.7 | 1.3 | 7.58 | 24.2% | 8.0% |
| CHALLENGER | 5,853 | 15.0 | 9.3 | 21.1 | 16.0 | 15.6 | 12.2 | 10.9 | 11.29 | 38.6% | 23.1% |
| ITF_MEN | 10,890 | 9.2 | 7.1 | 17.5 | 14.4 | 21.6 | 17.9 | 12.2 | 15.67 | 51.8% | 30.1% |
| ITF_WOMEN | 15,390 | 9.5 | 6.8 | 16.3 | 15.8 | 22.1 | 18.1 | 11.3 | 15.49 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,429 | 23.6 | 16.6 | 31.7 | 14.6 | 9.3 | 2.8 | 1.3 | 6.08 | 13.5% | 4.1% |
| WTA125 | 1,070 | 22.1 | 13.0 | 26.6 | 16.8 | 14.9 | 6.2 | 0.4 | 7.99 | 21.5% | 6.5% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,975 | 24.4 | 18.9 | 31.3 | 12.9 | 9.0 | 3.0 | 0.5 | 5.82 | 12.5% | 3.5% |
| CHALLENGER | 3,969 | 22.4 | 14.6 | 27.1 | 14.6 | 13.7 | 6.0 | 1.6 | 7.12 | 21.3% | 7.6% |
| DOUBLES | 2,075 | 5.2 | 4.5 | 12.2 | 10.8 | 20.9 | 25.1 | 21.4 | 23.54 | 67.4% | 46.5% |
| ITF_MEN | 8,321 | 13.0 | 9.4 | 21.1 | 15.8 | 21.3 | 13.3 | 6.0 | 11.91 | 40.6% | 19.2% |
| ITF_WOMEN | 9,922 | 13.1 | 9.2 | 19.6 | 15.6 | 21.4 | 15.4 | 5.7 | 12.44 | 42.5% | 21.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,439 | 24.2 | 15.4 | 30.1 | 17.9 | 9.2 | 2.8 | 0.3 | 6.8 | 12.3% | 3.1% |
| WTA125 | 1,084 | 24.8 | 12.6 | 21.1 | 18.9 | 13.6 | 7.3 | 1.7 | 7.92 | 22.5% | 8.9% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,296 | 27.6 | 15.6 | 27.9 | 13.4 | 11.4 | 3.7 | 0.4 | 5.9 | 15.5% | 4.1% |
| CHALLENGER | 4,108 | 21.2 | 12.3 | 25.9 | 17.7 | 15.1 | 6.1 | 1.5 | 8.01 | 22.8% | 7.6% |
| ITF_MEN | 8,006 | 12.0 | 8.8 | 20.6 | 17.1 | 22.0 | 14.3 | 5.2 | 12.41 | 41.5% | 19.6% |
| ITF_WOMEN | 11,501 | 11.6 | 8.4 | 18.3 | 17.3 | 24.0 | 15.2 | 5.2 | 13.34 | 44.4% | 20.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,350 | 18.6 | 13.7 | 24.7 | 20.3 | 16.2 | 6.0 | 0.6 | 8.18 | 22.7% | 6.5% |
| WTA125 | 1,034 | 16.3 | 7.6 | 22.1 | 19.4 | 20.7 | 12.3 | 1.6 | 10.97 | 34.5% | 13.8% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,296 | 26.3 | 15.8 | 25.6 | 16.2 | 11.9 | 3.8 | 0.5 | 6.2 | 16.1% | 4.2% |
| CHALLENGER | 4,108 | 19.2 | 11.5 | 23.0 | 16.8 | 18.4 | 9.2 | 1.9 | 9.02 | 29.5% | 11.0% |
| ITF_MEN | 8,007 | 9.4 | 7.3 | 17.4 | 16.0 | 21.3 | 18.8 | 9.8 | 14.99 | 50.0% | 28.6% |
| ITF_WOMEN | 11,503 | 8.9 | 6.7 | 15.8 | 14.1 | 22.8 | 20.8 | 10.8 | 16.71 | 54.4% | 31.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,350 | 15.4 | 11.1 | 22.0 | 15.6 | 22.2 | 12.5 | 1.2 | 10.53 | 35.9% | 13.7% |
| WTA125 | 1,034 | 9.7 | 6.4 | 16.5 | 16.8 | 24.3 | 17.8 | 8.5 | 15.16 | 50.6% | 26.3% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 1,921 | 24.5 | 19.1 | 31.3 | 13.1 | 8.7 | 2.9 | 0.4 | 5.73 | 12.0% | 3.3% |
| CHALLENGER | 3,500 | 23.9 | 15.6 | 28.2 | 14.7 | 13.0 | 4.1 | 0.5 | 6.59 | 17.5% | 4.5% |
| DOUBLES | 1,947 | 5.1 | 4.6 | 12.4 | 10.9 | 20.8 | 25.0 | 21.2 | 23.41 | 67.0% | 46.2% |
| ITF_MEN | 7,110 | 13.9 | 9.9 | 22.8 | 16.4 | 21.3 | 11.8 | 3.9 | 10.99 | 37.0% | 15.7% |
| ITF_WOMEN | 8,446 | 13.7 | 9.7 | 20.9 | 16.3 | 21.5 | 14.4 | 3.5 | 11.62 | 39.5% | 18.0% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,385 | 24.6 | 15.8 | 30.1 | 18.0 | 9.2 | 2.2 | 0.1 | 6.68 | 11.5% | 2.2% |
| WTA125 | 960 | 26.1 | 13.4 | 22.2 | 20.1 | 12.5 | 5.1 | 0.5 | 7.36 | 18.1% | 5.6% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,075 | 5.2 | 4.5 | 12.2 | 10.8 | 20.9 | 25.1 | 21.4 | 23.54 | 67.4% | 46.5% |
| singles | 26,859 | 16.4 | 11.3 | 22.8 | 15.6 | 18.3 | 11.4 | 4.3 | 9.89 | 34.0% | 15.7% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 12 | 8.3 | 16.7 | 41.7 | 0.0 | 8.3 | 25.0 | 0.0 | 8.48 | 33.3% | 25.0% |
| Clay | 7,821 | 13.1 | 9.3 | 20.1 | 15.6 | 19.1 | 13.8 | 9.0 | 12.35 | 41.8% | 22.8% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 25,541 | 13.4 | 8.7 | 18.5 | 15.1 | 19.3 | 15.1 | 9.8 | 12.99 | 44.2% | 24.9% |
| UNKNOWN | 5,421 | 10.4 | 7.8 | 17.3 | 16.6 | 20.9 | 16.0 | 11.1 | 14.11 | 47.9% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 10,801 | 20.0 | 12.2 | 22.4 | 15.7 | 14.7 | 9.2 | 5.8 | 8.54 | 29.8% | 15.1% |
| B | 4,780 | 12.8 | 8.9 | 19.1 | 16.1 | 19.4 | 12.7 | 10.9 | 12.59 | 43.0% | 23.6% |
| C | 5,577 | 12.1 | 8.9 | 19.9 | 15.8 | 18.6 | 14.3 | 10.4 | 12.77 | 43.4% | 24.7% |
| D | 6,165 | 12.0 | 8.3 | 17.6 | 15.4 | 21.6 | 15.8 | 9.3 | 13.73 | 46.6% | 25.1% |
| F | 11,709 | 7.4 | 5.6 | 15.0 | 14.7 | 23.3 | 21.0 | 13.0 | 17.71 | 57.3% | 34.0% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 7,675 | 24.0 | 15.7 | 28.8 | 15.3 | 11.1 | 3.8 | 1.3 | 6.54 | 16.1% | 5.1% |
| B | 4,049 | 17.0 | 10.6 | 24.1 | 16.3 | 19.0 | 9.8 | 3.2 | 9.66 | 32.0% | 13.0% |
| C | 5,645 | 11.2 | 7.9 | 19.5 | 14.7 | 21.0 | 15.6 | 10.0 | 13.46 | 46.7% | 25.7% |
| D | 4,241 | 14.5 | 10.0 | 21.6 | 15.3 | 20.0 | 13.1 | 5.5 | 11.24 | 38.6% | 18.6% |
| F | 7,324 | 9.9 | 8.4 | 16.0 | 14.9 | 23.2 | 19.9 | 7.8 | 15.44 | 50.8% | 27.7% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 12,239 | 18.3 | 11.1 | 21.4 | 15.4 | 15.2 | 10.0 | 8.6 | 9.74 | 33.8% | 18.6% |
| LIMITED | 8,552 | 13.6 | 10.0 | 20.3 | 16.3 | 19.0 | 13.3 | 7.5 | 11.73 | 39.8% | 20.8% |
| POOR | 18,241 | 9.1 | 6.5 | 16.0 | 15.0 | 22.6 | 19.0 | 11.7 | 16.14 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 7,481 | 24.1 | 18.2 | 33.1 | 15.0 | 6.6 | 2.7 | 0.4 | 5.85 | 9.6% | 3.1% |
| GAME_SPREAD | 5,862 | 22.2 | 15.2 | 33.0 | 17.2 | 9.0 | 2.9 | 0.6 | 6.73 | 12.4% | 3.4% |
| MATCH_WINNER | 28,934 | 15.6 | 10.8 | 22.0 | 15.2 | 18.5 | 12.4 | 5.5 | 10.4 | 36.4% | 17.9% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 13,514 | 27.4 | 16.7 | 31.2 | 12.5 | 9.5 | 2.4 | 0.3 | 5.69 | 12.2% | 2.7% |
| TOTAL_GAMES | 9,723 | 9.6 | 10.4 | 36.0 | 26.7 | 10.5 | 4.0 | 2.8 | 9.29 | 17.3% | 6.8% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,099 | 24.5 | 30.1 | 32.9 | 7.3 | 4.0 | 0.9 | 0.2 | 4.7 | 5.1% | 1.1% |
| GAME_SPREAD | 8,002 | 47.3 | 16.0 | 25.4 | 7.3 | 2.2 | 1.2 | 0.6 | 3.27 | 4.0% | 1.8% |
| TOTAL_GAMES | 14,065 | 6.4 | 9.2 | 40.4 | 31.4 | 7.2 | 3.1 | 2.2 | 9.31 | 12.5% | 5.3% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 12,110 | 23.9 | 16.9 | 34.8 | 14.4 | 7.1 | 2.6 | 0.4 | 6.01 | 10.1% | 3.0% |
| GAME_SPREAD | 8,005 | 20.2 | 13.6 | 28.0 | 20.5 | 12.5 | 4.2 | 1.1 | 7.77 | 17.8% | 5.3% |
| TOTAL_GAMES | 14,095 | 10.0 | 10.2 | 36.3 | 25.3 | 11.5 | 4.2 | 2.4 | 9.19 | 18.1% | 6.6% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 39,032 | 44.3% | 24.8% | 13.02 | 35.6% | 15.4% | 10.74 |
| gen1_elo | 39,032 | 44.1% | 24.6% | 12.93 | 35.3% | 15.4% | 10.56 |
| gen1_sr | 39,032 | 52.0% | 31.3% | 15.85 | 44.2% | 21.9% | 13.03 |
| gen2 | 39,032 | 51.0% | 31.6% | 15.47 | 44.1% | 23.5% | 12.93 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 18,552 | 15.6 | 10.6 | 21.3 | 17.1 | 20.1 | 12.0 | 3.3 | 10.71 | 35.4% | 15.3% |
| STALE | 20,480 | 10.6 | 7.1 | 16.2 | 13.8 | 19.0 | 17.6 | 15.7 | 15.99 | 52.3% | 33.3% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 22,402 | 16.3 | 11.1 | 22.7 | 15.4 | 17.9 | 11.9 | 4.7 | 9.97 | 34.5% | 16.6% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 67,966 | 22402 | 22024 | 23540 | 24.3 | 121.4 | 1451.1 |
| ge_15pp | 27,812 | 7734 | 7857 | 12221 | 26.8 | 431.5 | 1451.1 |
| ge_25pp | 14,848 | 3720 | 3436 | 7692 | 31.6 | 581.5 | 1431.1 |
| lt_10pp | 29,733 | 11223 | 10435 | 8075 | 22.4 | 47.0 | 1421.1 |

Current slate `SL-20261029T140930Z-3ceea296`: 460 priced rows, quote age at build {'median': 17.6, 'max': 17.7}, freshness {'AGING': 460}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 44 | 0.0 | 0.0 | 31.8 | 6.8 | 34.1 | 22.7 | 4.5 | 20.33 | 61.4% | 27.3% |
| EXTERNAL_LONE_OUTLIER | 23 | 69.6 | 30.4 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.3 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 3,842 | 19.7 | 11.3 | 25.1 | 18.0 | 17.9 | 7.2 | 0.9 | 8.64 | 26.0% | 8.2% |
| KALSHI_LONE_OUTLIER | 26 | 3.9 | 3.9 | 76.9 | 7.7 | 3.9 | 3.9 | 0.0 | 6.31 | 7.7% | 3.9% |
| MARKETS_AGREE | 759 | 65.1 | 34.9 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.27 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,643 | 0.0 | 2.4 | 36.3 | 25.6 | 24.6 | 10.2 | 0.9 | 12.0 | 35.7% | 11.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 39,032 | 6337 (16.2%) | 25.9% | 1.1% | {"EXTERNAL_STALE": 3842, "AGREES_WITH_KALSHI": 1643, "ALL_AGREE": 759, "SUPPORTS_MODEL_DIRECTION": 43, "AGREES_WITH_MODEL": 26, "EXTERNAL_OUTLIER": 23, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 17,279 | 1616 (9.3%) | 36.3% | 1.8% | {"EXTERNAL_STALE": 1000, "AGREES_WITH_KALSHI": 587, "SUPPORTS_MODEL_DIRECTION": 27, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 9,666 | 509 (5.3%) | 35.9% | 2.5% | {"EXTERNAL_STALE": 313, "AGREES_WITH_KALSHI": 183, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,655 | 484 (10.4%) | 36.4% | 2.7% | {"EXTERNAL_STALE": 295, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 15,741 | 3606 (22.9%) | 17.6% | 1.0% | {"EXTERNAL_STALE": 2152, "ALL_AGREE": 759, "AGREES_WITH_KALSHI": 636, "EXTERNAL_OUTLIER": 23, "AGREES_WITH_MODEL": 22, "SUPPORTS_MODEL_DIRECTION": 13, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 7,651 | 10.4 | 7.4 | 19.8 | 14.4 | 21.6 | 16.5 | 9.9 | 14.1 | 48.1% | 26.5% |
| 4-10x | 5,269 | 11.1 | 8.6 | 18.5 | 15.6 | 21.9 | 14.4 | 9.9 | 13.65 | 46.2% | 24.3% |
| <2x | 19,696 | 15.2 | 10.0 | 19.4 | 16.1 | 17.4 | 13.1 | 8.8 | 11.57 | 39.3% | 21.9% |
| >=10x | 6,416 | 10.6 | 6.5 | 15.2 | 14.4 | 21.5 | 19.2 | 12.7 | 16.2 | 53.4% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 9,929 | 12.7 | 8.8 | 19.6 | 16.1 | 19.0 | 13.5 | 10.3 | 12.69 | 42.9% | 23.9% |
| 300-1000 | 8,429 | 12.1 | 8.7 | 17.8 | 15.3 | 20.3 | 16.3 | 9.5 | 13.57 | 46.1% | 25.8% |
| <300 | 12,700 | 8.3 | 5.9 | 15.2 | 14.8 | 23.0 | 20.0 | 12.9 | 17.05 | 55.9% | 32.9% |
| >=3000 | 7,974 | 21.6 | 13.3 | 23.9 | 15.6 | 13.8 | 7.2 | 4.7 | 7.53 | 25.6% | 11.8% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1125 | 0.5492 | 0.4104 | 0.496 | +0.053 | -0.086 | -0.0018 ± 0.0046 |
| ratio 4-10x | 766 | 0.5779 | 0.4319 | 0.4935 | +0.085 | -0.062 | 0.0077 ± 0.0057 |
| ratio <2x | 2669 | 0.5375 | 0.4141 | 0.45 | +0.087 | -0.036 | 0.0111 ± 0.0028 |
| ratio >=10x | 973 | 0.5671 | 0.3926 | 0.4491 | +0.118 | -0.057 | 0.014 ± 0.0058 |
| thinner_sample 1000-3000 | 1492 | 0.5391 | 0.4122 | 0.4544 | +0.085 | -0.042 | 0.0083 ± 0.0037 |
| thinner_sample 300-1000 | 1262 | 0.5666 | 0.4246 | 0.4857 | +0.081 | -0.061 | 0.0027 ± 0.0045 |
| thinner_sample <300 | 1873 | 0.5582 | 0.3907 | 0.4608 | +0.098 | -0.070 | 0.0104 ± 0.0041 |
| thinner_sample >=3000 | 906 | 0.532 | 0.4381 | 0.4636 | +0.069 | -0.025 | 0.013 ± 0.0038 |
| data_status ADEQUATE | 1504 | 0.5341 | 0.4312 | 0.4508 | +0.083 | -0.020 | 0.0124 ± 0.0032 |
| data_status LIMITED | 1332 | 0.5488 | 0.4155 | 0.4782 | +0.071 | -0.063 | 0.0048 ± 0.0041 |
| data_status POOR | 2697 | 0.5608 | 0.3996 | 0.4668 | +0.094 | -0.067 | 0.0081 ± 0.0033 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 811 | 0.1988 | 0.1993 | -0.0005 ± 0.0005 | 0.577 | 0.5784 | 0.5031 | 0.488 | 0.5105 | -0.086 ± 0.0166 | -0.01 (5) |
| 3-5 | 501 | 0.2053 | 0.2057 | -0.0004 ± 0.0016 | 0.5936 | 0.593 | 0.5015 | 0.4616 | 0.485 | -0.095 ± 0.0207 | 0.02 (1) |
| 5-10 | 1159 | 0.2007 | 0.2014 | -0.0006 ± 0.002 | 0.5871 | 0.5856 | 0.5102 | 0.4365 | 0.4754 | -0.086 ± 0.0136 | -0.0167 (6) |
| 10-15 | 968 | 0.2213 | 0.2123 | +0.0089 ± 0.0037 | 0.6353 | 0.6102 | 0.5259 | 0.4022 | 0.4267 | -0.109 ± 0.0149 | -0.048 (5) |
| 15-25 | 1229 | 0.2234 | 0.2121 | +0.0114 ± 0.0051 | 0.6422 | 0.6084 | 0.5757 | 0.3801 | 0.4491 | -0.097 ± 0.0131 | -0.0033 (9) |
| 25-40 | 715 | 0.2236 | 0.2068 | +0.0169 ± 0.0102 | 0.6371 | 0.5954 | 0.6554 | 0.3447 | 0.4727 | -0.074 ± 0.0156 | -0.01 (1) |
| 40+ | 150 | 0.2801 | 0.1888 | +0.0913 ± 0.0309 | 0.7644 | 0.5567 | 0.7409 | 0.2923 | 0.42 | -0.075 ± 0.0306 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4405 | 0.1836 | 0.1845 | -0.0009 ± 0.0002 | 0.5415 | 0.5427 | 0.4872 | 0.4719 | 0.5031 | -0.022 ± 0.0066 | -0.0129 (17) |
| 3-5 | 2958 | 0.1954 | 0.1933 | +0.0021 ± 0.0007 | 0.5698 | 0.5625 | 0.4811 | 0.4413 | 0.4344 | -0.062 ± 0.0082 | 0.0 (2) |
| 5-10 | 6260 | 0.2012 | 0.198 | +0.0032 ± 0.0008 | 0.5877 | 0.5763 | 0.4832 | 0.4096 | 0.4265 | -0.044 ± 0.0057 | -0.0119 (21) |
| 10-15 | 5238 | 0.2024 | 0.1864 | +0.0160 ± 0.0015 | 0.5911 | 0.5474 | 0.4828 | 0.3587 | 0.3559 | -0.067 ± 0.006 | -0.0281 (16) |
| 15-25 | 6548 | 0.2059 | 0.1681 | +0.0378 ± 0.002 | 0.6042 | 0.4989 | 0.4995 | 0.3033 | 0.3057 | -0.069 ± 0.005 | -0.0025 (44) |
| 25-40 | 5193 | 0.2223 | 0.126 | +0.0963 ± 0.0031 | 0.6389 | 0.387 | 0.5264 | 0.2121 | 0.2203 | -0.059 ± 0.0048 | -0.01 (1) |
| 40+ | 3369 | 0.3831 | 0.045 | +0.3381 ± 0.0042 | 0.9982 | 0.1738 | 0.6322 | 0.104 | 0.0606 | -0.078 ± 0.0035 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 636 | 0.2047 | 0.2053 | -0.0006 ± 0.0006 | 0.5907 | 0.5925 | 0.5096 | 0.4946 | 0.5204 | -0.104 ± 0.0195 | -0.01 (3) |
| 3-5 | 450 | 0.2226 | 0.22 | +0.0026 ± 0.0018 | 0.63 | 0.6249 | 0.5145 | 0.4748 | 0.4578 | -0.129 ± 0.0236 | 0.02 (1) |
| 5-10 | 1009 | 0.2086 | 0.2081 | +0.0005 ± 0.0022 | 0.6034 | 0.6012 | 0.5443 | 0.4694 | 0.5055 | -0.087 ± 0.0148 | -0.01 (4) |
| 10-15 | 904 | 0.2166 | 0.2091 | +0.0074 ± 0.0038 | 0.6242 | 0.6048 | 0.5643 | 0.44 | 0.4746 | -0.112 ± 0.0159 | -0.04 (5) |
| 15-25 | 1283 | 0.2291 | 0.2143 | +0.0148 ± 0.005 | 0.6525 | 0.6128 | 0.5827 | 0.3874 | 0.4497 | -0.094 ± 0.0131 | -0.0133 (9) |
| 25-40 | 912 | 0.267 | 0.1962 | +0.0708 ± 0.0092 | 0.7458 | 0.5728 | 0.656 | 0.3419 | 0.3893 | -0.130 ± 0.0146 | -0.0075 (4) |
| 40+ | 339 | 0.3604 | 0.1681 | +0.1924 ± 0.0221 | 0.9903 | 0.5041 | 0.7333 | 0.2483 | 0.3068 | -0.079 ± 0.0215 | -0.01 (1) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 3785 | 0.1886 | 0.1889 | -0.0003 ± 0.0002 | 0.5517 | 0.5521 | 0.5093 | 0.4942 | 0.5091 | -0.042 ± 0.0073 | -0.0133 (15) |
| 3-5 | 2547 | 0.1974 | 0.196 | +0.0014 ± 0.0007 | 0.5721 | 0.5679 | 0.513 | 0.4733 | 0.4743 | -0.052 ± 0.009 | 0.02 (1) |
| 5-10 | 5564 | 0.1992 | 0.1957 | +0.0035 ± 0.0009 | 0.5839 | 0.5708 | 0.511 | 0.4369 | 0.4533 | -0.043 ± 0.006 | -0.0117 (6) |
| 10-15 | 4700 | 0.2053 | 0.1923 | +0.0130 ± 0.0016 | 0.6003 | 0.5616 | 0.5124 | 0.3885 | 0.3989 | -0.057 ± 0.0065 | -0.0189 (18) |
| 15-25 | 6577 | 0.2168 | 0.1816 | +0.0352 ± 0.0021 | 0.6308 | 0.5324 | 0.5231 | 0.3277 | 0.3388 | -0.060 ± 0.0053 | -0.0086 (42) |
| 25-40 | 6039 | 0.251 | 0.1359 | +0.1152 ± 0.003 | 0.7082 | 0.4171 | 0.5566 | 0.2399 | 0.2199 | -0.085 ± 0.0047 | -0.0044 (18) |
| 40+ | 4759 | 0.3967 | 0.0592 | +0.3375 ± 0.0041 | 1.0467 | 0.2127 | 0.651 | 0.1172 | 0.0815 | -0.073 ± 0.0035 | -0.01 (1) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 778 | 0.1956 | 0.1978 | -0.0022 ± 0.0006 | 0.5698 | 0.5755 | 0.5005 | 0.4851 | 0.5463 | -0.037 ± 0.0167 | -0.0137 (8) |
| 3-5 | 536 | 0.2053 | 0.2035 | +0.0018 ± 0.0016 | 0.5939 | 0.5876 | 0.4948 | 0.4552 | 0.4534 | -0.122 ± 0.0202 | 0.0067 (3) |
| 5-10 | 1202 | 0.2028 | 0.2011 | +0.0016 ± 0.0019 | 0.5913 | 0.5848 | 0.5088 | 0.435 | 0.4601 | -0.095 ± 0.0133 | -0.0071 (7) |
| 10-15 | 962 | 0.2092 | 0.2049 | +0.0042 ± 0.0036 | 0.6081 | 0.5937 | 0.5386 | 0.4153 | 0.4605 | -0.096 ± 0.0146 | -0.0317 (6) |
| 15-25 | 1166 | 0.2315 | 0.2162 | +0.0154 ± 0.0053 | 0.6608 | 0.6175 | 0.5864 | 0.3921 | 0.4503 | -0.107 ± 0.0136 | -0.03 (1) |
| 25-40 | 730 | 0.2135 | 0.2137 | -0.0002 ± 0.01 | 0.6159 | 0.6114 | 0.6641 | 0.3532 | 0.5068 | -0.059 ± 0.0155 | 0.015 (2) |
| 40+ | 159 | 0.2959 | 0.197 | +0.0989 ± 0.031 | 0.8067 | 0.5752 | 0.7484 | 0.2975 | 0.4214 | -0.073 ± 0.0322 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4254 | 0.1831 | 0.1837 | -0.0006 ± 0.0002 | 0.5393 | 0.5404 | 0.483 | 0.4677 | 0.4852 | -0.034 ± 0.0067 | -0.0163 (35) |
| 3-5 | 2904 | 0.2018 | 0.1997 | +0.0021 ± 0.0007 | 0.5866 | 0.5792 | 0.482 | 0.4426 | 0.4366 | -0.063 ± 0.0084 | -0.0094 (18) |
| 5-10 | 6431 | 0.1943 | 0.1906 | +0.0037 ± 0.0008 | 0.5719 | 0.5584 | 0.4833 | 0.4093 | 0.4217 | -0.047 ± 0.0055 | -0.01 (31) |
| 10-15 | 5185 | 0.1916 | 0.1787 | +0.0129 ± 0.0015 | 0.5666 | 0.5292 | 0.4929 | 0.3695 | 0.3784 | -0.055 ± 0.0059 | -0.015 (12) |
| 15-25 | 6683 | 0.2118 | 0.1729 | +0.0389 ± 0.002 | 0.6171 | 0.51 | 0.5118 | 0.317 | 0.3162 | -0.071 ± 0.0051 | -0.03 (2) |
| 25-40 | 5170 | 0.2161 | 0.1296 | +0.0865 ± 0.0031 | 0.6256 | 0.3948 | 0.5297 | 0.2141 | 0.2371 | -0.046 ± 0.0048 | 0.01 (3) |
| 40+ | 3344 | 0.3944 | 0.0504 | +0.3440 ± 0.0044 | 1.0286 | 0.1881 | 0.6426 | 0.1111 | 0.0667 | -0.079 ± 0.0037 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1169 | 0.1961 | 0.1962 | -0.0002 ± 0.0005 | 0.5708 | 0.571 | 0.5053 | 0.4902 | 0.497 | -0.066 ± 0.0132 | -0.0224 (49) |
| 3-5 | 829 | 0.1868 | 0.1859 | +0.0009 ± 0.0012 | 0.5477 | 0.5449 | 0.498 | 0.4581 | 0.4644 | -0.068 ± 0.0154 | -0.0194 (34) |
| 5-10 | 1714 | 0.2011 | 0.1962 | +0.0049 ± 0.0016 | 0.5912 | 0.5755 | 0.5012 | 0.4276 | 0.4317 | -0.076 ± 0.0109 | -0.005 (78) |
| 10-15 | 1175 | 0.2156 | 0.2038 | +0.0118 ± 0.0033 | 0.6231 | 0.5916 | 0.5356 | 0.4128 | 0.4247 | -0.084 ± 0.0135 | 0.0014 (64) |
| 15-25 | 1520 | 0.2311 | 0.2109 | +0.0202 ± 0.0046 | 0.6589 | 0.6068 | 0.581 | 0.3864 | 0.4342 | -0.081 ± 0.0119 | -0.0214 (59) |
| 25-40 | 947 | 0.2448 | 0.2104 | +0.0344 ± 0.0091 | 0.6996 | 0.6028 | 0.683 | 0.3711 | 0.472 | -0.095 ± 0.014 | -0.0219 (26) |
| 40+ | 317 | 0.3359 | 0.2018 | +0.1341 ± 0.0243 | 0.9701 | 0.589 | 0.814 | 0.3373 | 0.4511 | -0.100 ± 0.0227 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4349 | 0.1753 | 0.1756 | -0.0003 ± 0.0002 | 0.5193 | 0.5196 | 0.5094 | 0.4942 | 0.5068 | -0.037 ± 0.0064 | -0.0157 (88) |
| 3-5 | 2967 | 0.1934 | 0.192 | +0.0014 ± 0.0006 | 0.5629 | 0.5602 | 0.5051 | 0.4653 | 0.4671 | -0.049 ± 0.0082 | -0.0209 (69) |
| 5-10 | 6036 | 0.1983 | 0.191 | +0.0072 ± 0.0008 | 0.5834 | 0.5623 | 0.4962 | 0.4225 | 0.412 | -0.068 ± 0.0057 | -0.0082 (132) |
| 10-15 | 4236 | 0.211 | 0.1959 | +0.0151 ± 0.0017 | 0.6128 | 0.5732 | 0.5337 | 0.4108 | 0.4101 | -0.067 ± 0.0069 | -0.0053 (105) |
| 15-25 | 5149 | 0.2291 | 0.2013 | +0.0279 ± 0.0025 | 0.6596 | 0.582 | 0.5671 | 0.3718 | 0.3985 | -0.061 ± 0.0063 | -0.0253 (107) |
| 25-40 | 3465 | 0.2606 | 0.1871 | +0.0736 ± 0.0046 | 0.7375 | 0.5456 | 0.6355 | 0.3227 | 0.3642 | -0.080 ± 0.0072 | -0.0229 (51) |
| 40+ | 1490 | 0.3786 | 0.1511 | +0.2275 ± 0.0104 | 1.0685 | 0.4538 | 0.7373 | 0.2369 | 0.2711 | -0.078 ± 0.0095 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 5533 | 1.018 ± 0.037 | 1.094 | 0.1692 | 0.1665 | 0.2146 | 0.2061 |
| gen2 | 5533 | 0.809 ± 0.034 | 1.054 | 0.1711 | 0.1669 | 0.2343 | 0.2059 |
| gen1_elo | 5533 | 0.999 ± 0.036 | 1.092 | 0.1756 | 0.1667 | 0.2133 | 0.2063 |
| gen1_sr | 5533 | 0.991 ± 0.045 | 1.116 | 0.1314 | 0.1689 | 0.2302 | 0.2056 |
| gen1_ledger | 7671 | 0.859 ± 0.027 | 1.059 | 0.1874 | 0.1766 | 0.2179 | 0.2011 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 27,812)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,185 | 22.2% |
| STALE_QUOTE | market_freshness | 6,067 | 21.8% |
| BOOK_QUALITY | execution | 5,314 | 19.1% |
| POOR_DATA | data | 3,289 | 11.8% |
| LIMITED_DATA | data | 1,741 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,577 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,223 | 4.4% |
| IDENTITY_AMBIGUOUS | mapping | 1,135 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 803 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 477 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.2%, market_freshness 21.8%, execution 19.1%, data 18.1%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.4%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.4%, LOW_DATA_QUALITY 71.9%, THIN_PLAYER_HISTORY 60.7%, STALE_PLAYER_DATA 52.6%, STALE_KALSHI_QUOTE 43.9%, MODEL_INTERNAL_DISAGREEMENT 42.4%, ASYMMETRIC_SAMPLE_SIZE 33.5%, WIDE_SPREAD 25.1%, MODEL_HIGH_UNCERTAINTY 18.0%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.4%, LOW_DISPLAYED_LIQUIDITY 8.0%, EVENT_MAPPING_RISK 7.4%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.8%, POST_SETTLEMENT_OBSERVATION 22.2%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.4%

### >= ge_25 pp (N = 14,848)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 4,998 | 33.7% |
| STALE_QUOTE | market_freshness | 2,778 | 18.7% |
| BOOK_QUALITY | execution | 2,768 | 18.6% |
| POOR_DATA | data | 1,405 | 9.5% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 830 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 605 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 518 | 3.5% |
| LIMITED_DATA | data | 516 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 307 | 2.1% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 122 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.7%, market_freshness 18.7%, execution 18.6%, data 12.9%, market_freshness/coverage 9.1%, mapping 4.1%, model_calibration_or_unknown 2.1%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.8%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.2%, THIN_PLAYER_HISTORY 63.0%, STALE_KALSHI_QUOTE 51.8%, STALE_PLAYER_DATA 46.7%, MODEL_INTERNAL_DISAGREEMENT 42.7%, ASYMMETRIC_SAMPLE_SIZE 34.6%, WIDE_SPREAD 24.5%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 18.5%, LEVEL_TRANSFER_RISK 9.2%, EVENT_MAPPING_RISK 9.0%, LOW_DISPLAYED_LIQUIDITY 7.8%, MODEL_CALIBRATION_OUTLIER 4.8%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 36.7%, POST_SETTLEMENT_OBSERVATION 33.7%, POSSIBLE_IN_PLAY_QUOTE 5.9%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 11787, "IDENTITY_AMBIGUOUS": 3061}; ticker orientation: {"VERIFIED": 14848}.

Checks: discipline:AMBIGUOUS 964, discipline:PASS 13884, identity_confidence:AMBIGUOUS 2742, identity_confidence:PASS 12106, level_mapping:NA 976, level_mapping:PASS 13872, market_pair:AMBIGUOUS 478, market_pair:NA 347, market_pair:PASS 14023, model_complement:NA 311, model_complement:PASS 14537, namesake:AMBIGUOUS 6, namesake:PASS 14842, physical_match_id:NA 5182, physical_match_id:PASS 9666, player_ids:PASS 14848, same_pair_other_event:PASS 14848, ticker_orientation:PASS 14848

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,369 | 4.2% | 3.8% | 1.5% | {"market_freshness": 56, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 13} | 5.85 | 0.22 / 0.2173 (611) | 21.5% | 2.9% | 3.3% | 2.8% |
| CHALLENGER | 9,822 | 16.5% | 6.2% | 10.9% | {"coverage": 951, "market_freshness/coverage": 195, "market_freshness": 165, "data": 144, "model_calibration_or_unknown": 74, "execution": 37, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.25 | 0.2197 / 0.2107 (2247) | 35.2% | 15.7% | 4.1% | 22.5% |
| DOUBLES | 2,075 | 46.5% | 46.2% | 6.5% | {"execution": 547, "mapping": 246, "market_freshness": 106, "market_freshness/coverage": 58, "coverage": 7} | 23.41 | 0.308 / 0.2377 (497) | 11.3% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 19,211 | 25.1% | 17.7% | 32.4% | {"coverage": 1677, "execution": 900, "market_freshness": 871, "data": 717, "market_freshness/coverage": 456, "mapping": 183, "model_calibration": 6, "model_calibration_or_unknown": 3} | 11.72 | 0.2158 / 0.1992 (3956) | 37.3% | 70.1% | 16.8% | 21.3% |
| ITF_WOMEN | 25,312 | 26.6% | 19.4% | 45.4% | {"coverage": 2310, "market_freshness": 1434, "execution": 1207, "data": 966, "market_freshness/coverage": 569, "mapping": 153, "model_calibration_or_unknown": 81, "model_calibration": 21} | 12.64 | 0.2042 / 0.1959 (4614) | 39.2% | 57.6% | 10.0% | 21.2% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 3,868 | 5.7% | 4.9% | 1.5% | {"market_freshness": 76, "model_calibration_or_unknown": 43, "execution": 27, "coverage": 27, "data": 19, "model_calibration": 18, "market_freshness/coverage": 11, "mapping": 1} | 7.54 | 0.2373 / 0.2306 (605) | 26.1% | 1.1% | 1.4% | 3.4% |
| WTA125 | 2,154 | 11.6% | 9.9% | 1.7% | {"market_freshness": 68, "model_calibration_or_unknown": 51, "market_freshness/coverage": 41, "data": 39, "execution": 21, "model_calibration": 14, "coverage": 12, "mapping": 4} | 9.21 | 0.2094 / 0.192 (632) | 25.4% | 11.4% | 5.0% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 413 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 19.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1173 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.0h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 549 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 41 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 42 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 43 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 44 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 45 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 46 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT07SCOREE-REE` | ITF_WOMEN | fair_v1 | 20% / 98% | -78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | YES | Kalshi had settled this market 9.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 553 min (STALE); data POOR (grade D, thinner serve sample 144.0, ratio 15.33); no external reference |
| 49 | `KXITFMATCH-26OCT13RIHLOU-LOU` | ITF_MEN | fair_v1 | 79% / 2% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 466 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 152.45); no external reference |
| 50 | `KXATPDOUBLES-26OCT29MICVANARROLI-MICVAN` | DOUBLES | gen1_ledger | 98% / 20% | +77 | BOOK_QUALITY | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9697, "by_level_share_of_ge_25pp": {"ATP": 0.0153, "CHALLENGER": 0.109, "DOUBLES": 0.0649, "ITF_MEN": 0.3242, "ITF_WOMEN": 0.454, "OTHER": 0.0008, "WTA": 0.015, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.518, "share_primary_cause_market_settled_or_in_play": 0.4274, "share_primary_cause_stale_quote_only": 0.1871}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 14848, "identity_ambiguous_share": 0.2062, "ticker_orientation": {"VERIFIED": 14848}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 9666, "with_external": 509, "coverage": 0.0527, "external_status": {"EXTERNAL_STALE": 313, "AGREES_WITH_KALSHI": 183, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 313, "MODEL_LONE_OUTLIER": 183, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3595, "share_external_supports_model": 0.0255}, "pregame_clean_ge_25pp": {"n": 4655, "with_external": 484, "coverage": 0.104, "external_status": {"EXTERNAL_STALE": 295, "AGREES_WITH_KALSHI": 176, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 295, "MODEL_LONE_OUTLIER": 176, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3636, "share_external_supports_model": 0.0269}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 458.0, "median_sample_ratio": 2.51, "median_min_matches": 18.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2119, "data_status": {"POOR": 8460, "LIMITED": 3815, "ADEQUATE": 2573}, "comparison_lt_10pp": {"median_thinner_serve_points": 1651.0, "median_sample_ratio": 1.73, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1125, "model_minus_observed": 0.0532, "kalshi_minus_observed": -0.0856, "brier_diff_model_minus_kalshi": -0.0018}, "4-10x": {"n": 766, "model_minus_observed": 0.0845, "kalshi_minus_observed": -0.0616, "brier_diff_model_minus_kalshi": 0.0077}, "<2x": {"n": 2669, "model_minus_observed": 0.0875, "kalshi_minus_observed": -0.0359, "brier_diff_model_minus_kalshi": 0.0111}, ">=10x": {"n": 973, "model_minus_observed": 0.118, "kalshi_minus_observed": -0.0565, "brier_diff_model_minus_kalshi": 0.014}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 5533, "model": {"intercept": -0.533, "slope": 0.809, "slope_se": 0.034}, "kalshi_mid_same_rows": {"intercept": 0.196, "slope": 1.054, "slope_se": 0.038}, "mean_extremity_model": 0.1711, "mean_extremity_kalshi": 0.1669, "model_brier": 0.2343, "kalshi_brier": 0.2059, "brier_diff_model_minus_kalshi": 0.0283, "brier_diff_se": 0.0025, "model_logloss": 0.6661, "kalshi_logloss": 0.5948}, "fair_v1": {"n": 5533, "model": {"intercept": -0.409, "slope": 1.018, "slope_se": 0.037}, "kalshi_mid_same_rows": {"intercept": 0.289, "slope": 1.094, "slope_se": 0.038}, "mean_extremity_model": 0.1692, "mean_extremity_kalshi": 0.1665, "model_brier": 0.2146, "kalshi_brier": 0.2061, "brier_diff_model_minus_kalshi": 0.0085, "brier_diff_se": 0.0021, "model_logloss": 0.6181, "kalshi_logloss": 0.5951}, "gen1_elo": {"n": 5533, "model": {"intercept": -0.385, "slope": 0.999, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.31, "slope": 1.092, "slope_se": 0.038}, "mean_extremity_model": 0.1756, "mean_extremity_kalshi": 0.1667, "model_brier": 0.2133, "kalshi_brier": 0.2063, "brier_diff_model_minus_kalshi": 0.007, "brier_diff_se": 0.0021, "model_logloss": 0.6155, "kalshi_logloss": 0.5954}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2476, "share_ge_15": 0.4427, "median_abs_gap": 13.02, "n": 39032}, "gen1_elo": {"share_ge_25": 0.2461, "share_ge_15": 0.4409, "median_abs_gap": 12.93, "n": 39032}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5202, "median_abs_gap": 15.85, "n": 39032}, "gen2": {"share_ge_25": 0.3162, "share_ge_15": 0.5102, "median_abs_gap": 15.47, "n": 39032}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1536, "share_ge_15": 0.3557, "median_abs_gap": 10.74, "n": 30301}, "gen1_elo": {"share_ge_25": 0.1539, "share_ge_15": 0.3529, "median_abs_gap": 10.56, "n": 30300}, "gen1_sr": {"share_ge_25": 0.219, "share_ge_15": 0.4422, "median_abs_gap": 13.03, "n": 30303}, "gen2": {"share_ge_25": 0.2351, "share_ge_15": 0.4414, "median_abs_gap": 12.93, "n": 30304}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.85, "share_ge_25_all": 0.0423, "share_ge_25_pregame_clean": 0.0378}, "WTA": {"median_abs_gap_pregame_clean": 7.54, "share_ge_25_all": 0.0574, "share_ge_25_pregame_clean": 0.0493}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2367, "share_within_10pp_all": 0.4375, "share_within_10pp_pregame_clean": 0.4894, "corr_model_vs_mid_pregame_clean": 0.8504}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 811, "model_brier": 0.1988, "kalshi_brier": 0.1993, "brier_diff_model_minus_kalshi": -0.0005}, "10-15": {"n_settled": 968, "model_brier": 0.2213, "kalshi_brier": 0.2123, "brier_diff_model_minus_kalshi": 0.0089}, "15-25": {"n_settled": 1229, "model_brier": 0.2234, "kalshi_brier": 0.2121, "brier_diff_model_minus_kalshi": 0.0114}, "25-40": {"n_settled": 715, "model_brier": 0.2236, "kalshi_brier": 0.2068, "brier_diff_model_minus_kalshi": 0.0169}, "3-5": {"n_settled": 501, "model_brier": 0.2053, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": -0.0004}, "40+": {"n_settled": 150, "model_brier": 0.2801, "kalshi_brier": 0.1888, "brier_diff_model_minus_kalshi": 0.0913}, "5-10": {"n_settled": 1159, "model_brier": 0.2007, "kalshi_brier": 0.2014, "brier_diff_model_minus_kalshi": -0.0006}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.533, "slope": 0.809, "slope_se": 0.034}, "kalshi_slope": {"intercept": 0.196, "slope": 1.054, "slope_se": 0.038}, "n": 5533}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.49, "slope": 0.859, "slope_se": 0.027}, "kalshi_slope": {"intercept": 0.166, "slope": 1.059, "slope_se": 0.031}, "n": 7671}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 497, "model_brier": 0.308, "kalshi_brier": 0.2377, "brier_diff_model_minus_kalshi": 0.0703, "brier_diff_se": 0.0134, "corr_model_outcome": 0.0616, "corr_kalshi_outcome": 0.2343}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
