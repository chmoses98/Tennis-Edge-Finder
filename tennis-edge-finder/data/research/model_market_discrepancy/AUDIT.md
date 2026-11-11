# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-11T16:29Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 88,697): 0-3 14.0%, 3-5 9.5%, 5-10 20.1%, 10-15 15.2%, 15-25 19.2%, 25-40 13.7%, 40+ 8.3%; median gap 11.89 pp.
* **Where the extremes live**: 97.2% of >=25 pp gaps are off the ATP/WTA main tour (ITF 78.1%, Challenger 11.2%, doubles 6.4%). Main tour: ATP 3.7% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 19,518): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.9%, STALE_QUOTE 20.2%, BOOK_QUALITY 16.5%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.9%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.4%, LIMITED_DATA 3.3%, UNEXPLAINED_MODEL_DISAGREEMENT 1.8%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.7%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.9%, market_freshness 20.2%, execution 16.5%, data 12.4%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 55.2% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 44.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 19,518 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 19.7% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 4.9%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 27.2% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 477.0 points vs 1686.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.022, Gen-2 0.818, Gen-1 ledger 0.869 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 999 model 0.2253 vs Kalshi 0.2029; n 207 model 0.3061 vs Kalshi 0.1699.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 370,617 model-market comparisons (611,766 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 122,261 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-11T16:15:26.688139+00:00'], shadow board 102,593 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-11T16:15:31.079945+00:00'], Model 4 43,956 rows, 30,637 settled tickers, 11,623 tickers with an external scan.
* By model: {"gen1_ledger": 81939, "gen1_elo": 51556, "fair_v1": 51556, "gen2": 51556, "gen1_sr": 51556, "model4_fundamental": 41269, "model4_conditioned": 41185}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 88,697 | 14.0 | 9.5 | 20.1 | 15.2 | 19.2 | 13.7 | 8.3 | 11.89 | 41.2% | 22.0% |
| MW fair_v1 | 51,556 | 12.7 | 8.6 | 18.7 | 15.2 | 19.6 | 15.0 | 10.2 | 13.14 | 44.8% | 25.2% |
| MW gen1_elo | 51,556 | 12.4 | 8.7 | 19.2 | 15.3 | 19.4 | 14.9 | 10.1 | 12.99 | 44.4% | 25.0% |
| MW gen1_ledger | 37,141 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| MW gen1_sr | 51,556 | 9.9 | 7.2 | 16.6 | 13.9 | 20.8 | 18.7 | 12.8 | 15.95 | 52.4% | 31.5% |
| MW gen2 | 51,556 | 10.9 | 7.5 | 16.6 | 13.8 | 19.7 | 17.7 | 13.8 | 15.49 | 51.2% | 31.5% |
| all families model4_conditioned | 41,185 | 22.2 | 17.9 | 34.5 | 16.9 | 5.0 | 2.2 | 1.2 | 6.07 | 8.4% | 3.4% |
| all families model4_fundamental | 41,269 | 17.3 | 13.5 | 34.0 | 20.0 | 9.9 | 3.8 | 1.5 | 7.61 | 15.2% | 5.3% |

Configurable thresholds (primary): >=5pp 76.5%, >=10pp 56.4%, >=15pp 41.2%, >=20pp 30.4%, >=25pp 22.0%, >=30pp 15.9%, >=40pp 8.3%, >=50pp 3.9%
Executable gap (model outside the book, before fees): median 8.53pp; >=10pp 45.5%, >=25pp 17.5%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,102 | 28.0 | 15.8 | 28.0 | 13.3 | 10.7 | 3.6 | 0.6 | 5.77 | 14.9% | 4.2% |
| CHALLENGER | 8,162 | 16.4 | 9.6 | 20.5 | 15.2 | 15.8 | 11.4 | 11.0 | 10.93 | 38.3% | 22.4% |
| ITF_MEN | 14,913 | 9.6 | 7.3 | 17.0 | 14.9 | 21.1 | 17.2 | 12.8 | 15.45 | 51.1% | 30.0% |
| ITF_WOMEN | 19,956 | 9.4 | 7.0 | 16.1 | 14.7 | 22.1 | 18.6 | 11.9 | 15.98 | 52.7% | 30.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,090 | 16.7 | 13.3 | 25.1 | 20.6 | 16.5 | 6.7 | 1.1 | 8.56 | 24.3% | 7.8% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,102 | 26.4 | 15.6 | 26.3 | 15.7 | 11.2 | 3.9 | 0.8 | 6.09 | 15.9% | 4.7% |
| CHALLENGER | 8,162 | 14.4 | 9.1 | 19.0 | 13.8 | 18.4 | 13.7 | 11.5 | 12.5 | 43.6% | 25.2% |
| ITF_MEN | 14,913 | 8.1 | 6.1 | 15.0 | 14.0 | 20.3 | 20.0 | 16.5 | 17.87 | 56.8% | 36.5% |
| ITF_WOMEN | 19,956 | 7.8 | 5.9 | 14.2 | 12.7 | 20.6 | 21.2 | 17.6 | 19.09 | 59.4% | 38.8% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,090 | 14.1 | 10.4 | 21.7 | 16.2 | 22.4 | 12.7 | 2.5 | 11.18 | 37.6% | 15.2% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 4,102 | 23.4 | 14.1 | 25.6 | 15.5 | 14.4 | 6.0 | 1.1 | 7.04 | 21.5% | 7.1% |
| CHALLENGER | 8,162 | 15.0 | 9.6 | 20.8 | 15.6 | 16.2 | 12.0 | 10.9 | 11.29 | 39.0% | 22.9% |
| ITF_MEN | 14,913 | 9.4 | 7.2 | 17.1 | 14.2 | 21.6 | 17.4 | 13.1 | 15.82 | 52.0% | 30.5% |
| ITF_WOMEN | 19,956 | 9.2 | 6.8 | 16.3 | 15.6 | 22.1 | 18.6 | 11.3 | 15.67 | 52.0% | 29.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,090 | 22.5 | 17.2 | 31.9 | 15.3 | 8.8 | 3.3 | 1.0 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,475 | 28.2 | 19.5 | 29.1 | 12.1 | 8.1 | 2.5 | 0.4 | 5.24 | 11.1% | 3.0% |
| CHALLENGER | 4,957 | 22.7 | 14.5 | 28.0 | 14.7 | 13.1 | 5.5 | 1.5 | 7.03 | 20.1% | 7.0% |
| DOUBLES | 2,715 | 4.9 | 4.5 | 13.0 | 11.0 | 20.6 | 24.5 | 21.6 | 23.06 | 66.7% | 46.1% |
| ITF_MEN | 10,867 | 12.7 | 9.4 | 21.4 | 15.6 | 21.8 | 12.9 | 6.1 | 11.86 | 40.9% | 19.0% |
| ITF_WOMEN | 12,907 | 13.6 | 9.3 | 19.7 | 15.7 | 21.6 | 14.7 | 5.5 | 12.2 | 41.7% | 20.1% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,815 | 24.1 | 16.0 | 31.5 | 16.9 | 8.9 | 2.5 | 0.2 | 6.44 | 11.6% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,973 | 28.5 | 16.1 | 28.4 | 13.2 | 10.4 | 3.1 | 0.3 | 5.64 | 13.8% | 3.4% |
| CHALLENGER | 5,732 | 21.1 | 12.0 | 25.7 | 17.9 | 15.9 | 5.7 | 1.7 | 8.2 | 23.2% | 7.3% |
| ITF_MEN | 10,880 | 11.8 | 8.6 | 20.6 | 17.2 | 22.2 | 14.0 | 5.5 | 12.49 | 41.8% | 19.6% |
| ITF_WOMEN | 14,596 | 11.3 | 8.6 | 19.0 | 17.1 | 24.0 | 15.4 | 4.7 | 13.15 | 44.0% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,976 | 17.0 | 13.3 | 25.4 | 21.0 | 16.5 | 6.2 | 0.6 | 8.42 | 23.3% | 6.8% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,973 | 26.7 | 16.0 | 26.6 | 15.7 | 11.2 | 3.5 | 0.4 | 6.01 | 15.0% | 3.8% |
| CHALLENGER | 5,732 | 18.2 | 11.6 | 23.9 | 16.3 | 19.0 | 9.1 | 1.9 | 8.97 | 29.9% | 11.0% |
| ITF_MEN | 10,881 | 9.6 | 7.3 | 17.5 | 16.1 | 22.2 | 18.2 | 9.1 | 14.86 | 49.5% | 27.3% |
| ITF_WOMEN | 14,597 | 8.9 | 7.0 | 16.0 | 14.3 | 22.5 | 20.6 | 10.7 | 16.51 | 53.8% | 31.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,976 | 14.4 | 10.5 | 21.9 | 16.4 | 22.6 | 12.4 | 1.9 | 11.03 | 36.8% | 14.3% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,405 | 28.5 | 19.7 | 29.1 | 12.3 | 7.8 | 2.3 | 0.3 | 5.2 | 10.4% | 2.7% |
| CHALLENGER | 4,384 | 24.0 | 15.4 | 29.2 | 14.8 | 12.4 | 3.8 | 0.4 | 6.58 | 16.6% | 4.2% |
| DOUBLES | 2,544 | 4.8 | 4.5 | 13.2 | 11.1 | 20.4 | 24.4 | 21.6 | 22.95 | 66.5% | 46.0% |
| ITF_MEN | 9,385 | 13.5 | 9.9 | 22.9 | 16.1 | 21.9 | 11.5 | 4.2 | 11.03 | 37.5% | 15.7% |
| ITF_WOMEN | 11,106 | 14.2 | 9.8 | 20.8 | 16.2 | 21.8 | 13.6 | 3.6 | 11.43 | 39.0% | 17.2% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,752 | 24.4 | 16.4 | 31.4 | 16.8 | 8.8 | 2.0 | 0.1 | 6.42 | 10.9% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,715 | 4.9 | 4.5 | 13.0 | 11.0 | 20.6 | 24.5 | 21.6 | 23.06 | 66.7% | 46.1% |
| singles | 34,426 | 16.7 | 11.3 | 22.9 | 15.4 | 18.5 | 11.0 | 4.3 | 9.77 | 33.7% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 10,962 | 12.7 | 8.9 | 19.4 | 15.2 | 19.6 | 14.3 | 9.7 | 12.88 | 43.7% | 24.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 33,615 | 13.1 | 8.7 | 18.9 | 15.0 | 19.1 | 15.0 | 10.2 | 12.98 | 44.3% | 25.2% |
| UNKNOWN | 6,566 | 10.4 | 7.5 | 17.0 | 16.5 | 21.5 | 15.9 | 11.2 | 14.41 | 48.6% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 14,444 | 19.2 | 11.8 | 22.4 | 15.8 | 14.8 | 9.5 | 6.4 | 9.0 | 30.7% | 15.9% |
| B | 6,204 | 12.9 | 8.5 | 19.6 | 15.3 | 19.6 | 12.4 | 11.5 | 12.75 | 43.6% | 24.0% |
| C | 7,277 | 12.0 | 8.6 | 19.5 | 16.1 | 18.9 | 14.6 | 10.4 | 12.9 | 43.8% | 25.0% |
| D | 8,404 | 11.5 | 8.3 | 17.9 | 15.0 | 21.9 | 15.7 | 9.7 | 14.01 | 47.3% | 25.4% |
| F | 15,227 | 7.3 | 5.7 | 14.9 | 14.4 | 23.1 | 21.1 | 13.6 | 18.01 | 57.7% | 34.7% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,804 | 25.0 | 15.9 | 28.9 | 14.8 | 10.7 | 3.5 | 1.2 | 6.35 | 15.3% | 4.7% |
| B | 5,070 | 16.7 | 10.9 | 24.3 | 16.9 | 18.9 | 9.4 | 3.0 | 9.6 | 31.3% | 12.4% |
| C | 7,292 | 11.0 | 7.8 | 19.6 | 14.9 | 21.1 | 15.5 | 10.1 | 13.46 | 46.7% | 25.6% |
| D | 5,631 | 14.5 | 10.0 | 21.1 | 15.3 | 20.9 | 12.7 | 5.5 | 11.32 | 39.1% | 18.2% |
| F | 9,344 | 10.2 | 8.3 | 16.5 | 14.5 | 23.5 | 19.0 | 8.0 | 15.27 | 50.5% | 27.0% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 16,376 | 17.7 | 10.9 | 21.4 | 15.5 | 15.1 | 10.2 | 9.2 | 10.0 | 34.5% | 19.3% |
| LIMITED | 11,152 | 13.5 | 9.5 | 20.5 | 16.1 | 19.6 | 13.3 | 7.6 | 11.91 | 40.5% | 20.9% |
| POOR | 24,028 | 8.8 | 6.6 | 16.0 | 14.6 | 22.6 | 19.1 | 12.2 | 16.36 | 53.8% | 31.3% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 9,254 | 23.7 | 18.1 | 33.0 | 15.4 | 6.4 | 3.0 | 0.4 | 5.9 | 9.8% | 3.4% |
| GAME_SPREAD | 6,921 | 22.8 | 15.3 | 32.1 | 16.7 | 9.1 | 3.3 | 0.7 | 6.69 | 13.1% | 4.0% |
| MATCH_WINNER | 37,141 | 15.8 | 10.8 | 22.1 | 15.1 | 18.6 | 11.9 | 5.6 | 10.29 | 36.1% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 17,016 | 28.4 | 16.8 | 30.6 | 12.7 | 8.9 | 2.3 | 0.3 | 5.58 | 11.5% | 2.6% |
| TOTAL_GAMES | 11,583 | 9.7 | 10.8 | 36.2 | 25.7 | 10.4 | 4.2 | 2.9 | 9.14 | 17.5% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,649 | 24.5 | 28.7 | 33.3 | 8.1 | 4.0 | 1.2 | 0.3 | 4.8 | 5.4% | 1.5% |
| GAME_SPREAD | 9,528 | 46.7 | 15.9 | 25.1 | 7.4 | 2.4 | 1.9 | 0.6 | 3.32 | 4.9% | 2.5% |
| TOTAL_GAMES | 17,008 | 6.6 | 9.8 | 40.8 | 29.9 | 7.3 | 3.3 | 2.4 | 9.16 | 13.0% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,685 | 23.8 | 16.6 | 34.6 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,537 | 20.4 | 13.4 | 28.4 | 20.2 | 12.1 | 4.4 | 1.1 | 7.69 | 17.6% | 5.5% |
| TOTAL_GAMES | 17,047 | 10.0 | 10.8 | 36.6 | 24.3 | 11.3 | 4.4 | 2.6 | 9.02 | 18.3% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 51,556 | 44.8% | 25.2% | 13.14 | 35.5% | 15.2% | 10.71 |
| gen1_elo | 51,556 | 44.4% | 25.0% | 12.99 | 35.0% | 15.0% | 10.51 |
| gen1_sr | 51,556 | 52.4% | 31.5% | 15.95 | 44.0% | 21.6% | 13.0 |
| gen2 | 51,556 | 51.2% | 31.5% | 15.49 | 43.9% | 23.0% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,229 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 31,327 | 10.8 | 7.4 | 17.0 | 13.9 | 19.2 | 17.0 | 14.6 | 15.36 | 50.9% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 30,609 | 16.4 | 11.1 | 22.7 | 15.2 | 18.2 | 11.5 | 5.0 | 9.96 | 34.7% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 88,697 | 30609 | 23701 | 34387 | 25.1 | 138.0 | 1451.1 |
| ge_15pp | 36,516 | 10619 | 8447 | 17450 | 29.0 | 443.3 | 1451.1 |
| ge_25pp | 19,518 | 5042 | 3694 | 10782 | 34.5 | 592.1 | 1431.1 |
| lt_10pp | 38,718 | 15342 | 11206 | 12170 | 22.8 | 49.7 | 1421.7 |

Current slate `SL-20261111T162944Z-02639086`: 346 priced rows, quote age at build {'median': 14.5, 'max': 14.6}, freshness {'AGING': 346}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 52 | 0.0 | 0.0 | 34.6 | 9.6 | 32.7 | 19.2 | 3.9 | 18.34 | 55.8% | 23.1% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,949 | 19.2 | 11.1 | 25.5 | 18.2 | 17.8 | 7.2 | 0.9 | 8.8 | 26.0% | 8.2% |
| KALSHI_LONE_OUTLIER | 32 | 6.2 | 6.2 | 75.0 | 6.2 | 3.1 | 3.1 | 0.0 | 6.16 | 6.2% | 3.1% |
| MARKETS_AGREE | 1,081 | 66.3 | 33.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,295 | 0.0 | 2.2 | 38.5 | 25.9 | 23.8 | 8.8 | 0.9 | 11.65 | 33.4% | 9.7% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 51,556 | 8438 (16.4%) | 27.2% | 1.0% | {"EXTERNAL_STALE": 4949, "AGREES_WITH_KALSHI": 2295, "ALL_AGREE": 1081, "SUPPORTS_MODEL_DIRECTION": 50, "AGREES_WITH_MODEL": 32, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 2} |
| fair_v1_ge_15pp | 23,098 | 2084 (9.0%) | 36.8% | 1.5% | {"EXTERNAL_STALE": 1286, "AGREES_WITH_KALSHI": 767, "SUPPORTS_MODEL_DIRECTION": 29, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 13,014 | 640 (4.9%) | 34.7% | 2.0% | {"EXTERNAL_STALE": 405, "AGREES_WITH_KALSHI": 222, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,986 | 609 (10.2%) | 35.3% | 2.1% | {"EXTERNAL_STALE": 381, "AGREES_WITH_KALSHI": 215, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 20,607 | 4849 (23.5%) | 19.2% | 0.9% | {"EXTERNAL_STALE": 2760, "ALL_AGREE": 1081, "AGREES_WITH_KALSHI": 933, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 28, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 10,100 | 10.7 | 7.5 | 19.1 | 14.3 | 21.7 | 16.4 | 10.2 | 14.32 | 48.4% | 26.6% |
| 4-10x | 6,912 | 11.1 | 8.7 | 17.9 | 14.8 | 21.8 | 14.7 | 11.0 | 14.07 | 47.5% | 25.8% |
| <2x | 26,303 | 14.6 | 9.6 | 19.9 | 16.0 | 17.5 | 13.3 | 9.1 | 11.61 | 39.8% | 22.4% |
| >=10x | 8,241 | 10.2 | 6.5 | 15.1 | 14.3 | 21.7 | 19.0 | 13.3 | 16.52 | 54.0% | 32.3% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 13,534 | 12.4 | 8.5 | 19.8 | 16.1 | 19.0 | 13.6 | 10.5 | 12.78 | 43.2% | 24.1% |
| 300-1000 | 11,145 | 11.7 | 8.7 | 17.9 | 15.0 | 20.7 | 16.3 | 9.7 | 13.81 | 46.8% | 26.0% |
| <300 | 16,345 | 8.1 | 5.9 | 15.0 | 14.5 | 22.8 | 20.1 | 13.5 | 17.47 | 56.5% | 33.7% |
| >=3000 | 10,532 | 21.1 | 12.8 | 24.0 | 15.4 | 13.9 | 7.4 | 5.3 | 7.84 | 26.7% | 12.7% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1583 | 0.5479 | 0.4081 | 0.4782 | +0.070 | -0.070 | 0.0036 ± 0.0039 |
| ratio 4-10x | 1080 | 0.5736 | 0.4286 | 0.4824 | +0.091 | -0.054 | 0.0106 ± 0.0049 |
| ratio <2x | 3874 | 0.5354 | 0.4129 | 0.4329 | +0.103 | -0.020 | 0.015 ± 0.0023 |
| ratio >=10x | 1329 | 0.5609 | 0.3876 | 0.4342 | +0.127 | -0.046 | 0.0189 ± 0.0049 |
| thinner_sample 1000-3000 | 2169 | 0.5392 | 0.412 | 0.4435 | +0.096 | -0.032 | 0.0128 ± 0.0031 |
| thinner_sample 300-1000 | 1775 | 0.5621 | 0.422 | 0.4682 | +0.094 | -0.046 | 0.0064 ± 0.0037 |
| thinner_sample <300 | 2573 | 0.5549 | 0.3869 | 0.4442 | +0.111 | -0.057 | 0.0158 ± 0.0035 |
| thinner_sample >=3000 | 1349 | 0.5274 | 0.4341 | 0.4418 | +0.086 | -0.008 | 0.0151 ± 0.0031 |
| data_status ADEQUATE | 2148 | 0.5312 | 0.4288 | 0.4372 | +0.094 | -0.008 | 0.0159 ± 0.0026 |
| data_status LIMITED | 1915 | 0.5475 | 0.4145 | 0.4621 | +0.085 | -0.048 | 0.0084 ± 0.0034 |
| data_status POOR | 3803 | 0.5567 | 0.3968 | 0.4491 | +0.108 | -0.052 | 0.0131 ± 0.0028 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1139 | 0.1973 | 0.1973 | -0.0001 ± 0.0005 | 0.5744 | 0.5746 | 0.5027 | 0.4875 | 0.4952 | -0.098 ± 0.014 | -0.0087 (8) |
| 3-5 | 725 | 0.2071 | 0.2065 | +0.0006 ± 0.0014 | 0.5999 | 0.5967 | 0.5011 | 0.4614 | 0.4731 | -0.102 ± 0.0173 | 0.01 (3) |
| 5-10 | 1685 | 0.2039 | 0.2022 | +0.0017 ± 0.0017 | 0.5945 | 0.5882 | 0.5102 | 0.4362 | 0.4605 | -0.093 ± 0.0113 | -0.0143 (7) |
| 10-15 | 1367 | 0.2184 | 0.2089 | +0.0095 ± 0.0031 | 0.6284 | 0.6012 | 0.5244 | 0.401 | 0.4228 | -0.107 ± 0.0126 | -0.055 (6) |
| 15-25 | 1744 | 0.2255 | 0.2064 | +0.0191 ± 0.0042 | 0.6461 | 0.5956 | 0.5727 | 0.3781 | 0.426 | -0.105 ± 0.011 | -0.0045 (11) |
| 25-40 | 999 | 0.2253 | 0.2029 | +0.0224 ± 0.0085 | 0.6411 | 0.5857 | 0.6456 | 0.3361 | 0.4545 | -0.069 ± 0.0133 | -0.06 (2) |
| 40+ | 207 | 0.3061 | 0.1699 | +0.1362 ± 0.026 | 0.819 | 0.5099 | 0.7265 | 0.2687 | 0.3575 | -0.086 ± 0.0252 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5814 | 0.1871 | 0.1879 | -0.0009 ± 0.0002 | 0.5506 | 0.5517 | 0.4913 | 0.476 | 0.5084 | -0.020 ± 0.0058 | -0.01 (28) |
| 3-5 | 3896 | 0.1995 | 0.1975 | +0.0020 ± 0.0006 | 0.5801 | 0.5733 | 0.4813 | 0.4415 | 0.4358 | -0.060 ± 0.0072 | 0.005 (6) |
| 5-10 | 8538 | 0.2016 | 0.1973 | +0.0043 ± 0.0007 | 0.5892 | 0.5754 | 0.483 | 0.4092 | 0.4172 | -0.050 ± 0.0049 | -0.0114 (22) |
| 10-15 | 6975 | 0.2018 | 0.1857 | +0.0161 ± 0.0013 | 0.5902 | 0.5453 | 0.4854 | 0.3615 | 0.3586 | -0.065 ± 0.0052 | -0.0379 (19) |
| 15-25 | 8933 | 0.2059 | 0.1663 | +0.0396 ± 0.0017 | 0.6037 | 0.4947 | 0.4981 | 0.3024 | 0.2997 | -0.069 ± 0.0043 | -0.0043 (51) |
| 25-40 | 7015 | 0.2235 | 0.124 | +0.0995 ± 0.0026 | 0.6413 | 0.3824 | 0.5248 | 0.2109 | 0.2133 | -0.060 ± 0.0041 | -0.0733 (3) |
| 40+ | 4771 | 0.381 | 0.044 | +0.3370 ± 0.0034 | 0.9923 | 0.1707 | 0.6289 | 0.1013 | 0.0574 | -0.075 ± 0.0029 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 910 | 0.2036 | 0.2039 | -0.0003 ± 0.0005 | 0.5875 | 0.5886 | 0.5078 | 0.4929 | 0.5187 | -0.096 ± 0.016 | -0.0117 (6) |
| 3-5 | 654 | 0.213 | 0.2101 | +0.0029 ± 0.0014 | 0.6098 | 0.6035 | 0.5156 | 0.476 | 0.4572 | -0.128 ± 0.0193 | 0.01 (3) |
| 5-10 | 1459 | 0.2058 | 0.204 | +0.0017 ± 0.0018 | 0.5974 | 0.5928 | 0.5391 | 0.4646 | 0.4921 | -0.087 ± 0.0122 | -0.01 (4) |
| 10-15 | 1267 | 0.2145 | 0.2069 | +0.0076 ± 0.0032 | 0.6219 | 0.5993 | 0.5587 | 0.4343 | 0.4688 | -0.104 ± 0.0133 | -0.04 (5) |
| 15-25 | 1832 | 0.2317 | 0.2106 | +0.0211 ± 0.0042 | 0.6595 | 0.6049 | 0.5852 | 0.3895 | 0.435 | -0.102 ± 0.011 | -0.0183 (12) |
| 25-40 | 1277 | 0.2671 | 0.2 | +0.0671 ± 0.0079 | 0.7448 | 0.5805 | 0.6595 | 0.3456 | 0.3978 | -0.112 ± 0.0126 | -0.008 (5) |
| 40+ | 467 | 0.3745 | 0.1587 | +0.2158 ± 0.0185 | 1.018 | 0.4818 | 0.7321 | 0.2434 | 0.2805 | -0.090 ± 0.0178 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4973 | 0.1904 | 0.1905 | -0.0002 ± 0.0002 | 0.5559 | 0.556 | 0.5077 | 0.4926 | 0.5069 | -0.041 ± 0.0064 | -0.0154 (26) |
| 3-5 | 3431 | 0.1948 | 0.1939 | +0.0009 ± 0.0006 | 0.5671 | 0.5643 | 0.5108 | 0.4711 | 0.4789 | -0.044 ± 0.0077 | 0.01 (5) |
| 5-10 | 7621 | 0.1964 | 0.193 | +0.0034 ± 0.0008 | 0.5774 | 0.5647 | 0.5073 | 0.4331 | 0.4501 | -0.039 ± 0.0051 | -0.0117 (6) |
| 10-15 | 6334 | 0.2027 | 0.1906 | +0.0121 ± 0.0014 | 0.5952 | 0.5581 | 0.5082 | 0.3842 | 0.3983 | -0.050 ± 0.0056 | -0.0189 (18) |
| 15-25 | 9015 | 0.2156 | 0.1787 | +0.0369 ± 0.0018 | 0.628 | 0.5256 | 0.5241 | 0.3286 | 0.3342 | -0.062 ± 0.0045 | -0.014 (52) |
| 25-40 | 8126 | 0.2511 | 0.1379 | +0.1132 ± 0.0026 | 0.7089 | 0.4208 | 0.56 | 0.2426 | 0.2267 | -0.077 ± 0.0041 | -0.0095 (20) |
| 40+ | 6442 | 0.4023 | 0.0593 | +0.3430 ± 0.0035 | 1.0601 | 0.2132 | 0.6547 | 0.1188 | 0.0803 | -0.073 ± 0.003 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1113 | 0.1954 | 0.1965 | -0.0011 ± 0.0005 | 0.5702 | 0.5729 | 0.5008 | 0.4854 | 0.5238 | -0.060 ± 0.0139 | -0.0191 (11) |
| 3-5 | 790 | 0.2094 | 0.2077 | +0.0016 ± 0.0013 | 0.6058 | 0.6004 | 0.4972 | 0.4577 | 0.4582 | -0.113 ± 0.0169 | 0.002 (5) |
| 5-10 | 1694 | 0.2039 | 0.1997 | +0.0042 ± 0.0016 | 0.5934 | 0.5818 | 0.5114 | 0.4376 | 0.4457 | -0.107 ± 0.0112 | -0.01 (10) |
| 10-15 | 1408 | 0.2119 | 0.2024 | +0.0095 ± 0.003 | 0.6141 | 0.5871 | 0.5382 | 0.415 | 0.4396 | -0.107 ± 0.0121 | -0.0286 (7) |
| 15-25 | 1660 | 0.2309 | 0.2117 | +0.0192 ± 0.0044 | 0.659 | 0.6072 | 0.5822 | 0.388 | 0.4349 | -0.106 ± 0.0113 | -0.03 (1) |
| 25-40 | 983 | 0.2171 | 0.2067 | +0.0104 ± 0.0086 | 0.6242 | 0.5945 | 0.6539 | 0.3438 | 0.4802 | -0.061 ± 0.0134 | -0.0267 (3) |
| 40+ | 218 | 0.314 | 0.1776 | +0.1364 ± 0.0258 | 0.8455 | 0.5261 | 0.7381 | 0.2805 | 0.3716 | -0.084 ± 0.0263 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5606 | 0.1856 | 0.1861 | -0.0005 ± 0.0002 | 0.5469 | 0.5473 | 0.4863 | 0.4709 | 0.4856 | -0.037 ± 0.0058 | -0.0189 (44) |
| 3-5 | 4011 | 0.2056 | 0.2037 | +0.0019 ± 0.0006 | 0.5967 | 0.5903 | 0.4813 | 0.4418 | 0.4378 | -0.059 ± 0.0072 | -0.0073 (22) |
| 5-10 | 8680 | 0.1964 | 0.1911 | +0.0054 ± 0.0007 | 0.5765 | 0.5597 | 0.4861 | 0.4121 | 0.4126 | -0.056 ± 0.0047 | -0.0117 (42) |
| 10-15 | 6987 | 0.195 | 0.1796 | +0.0154 ± 0.0013 | 0.5752 | 0.5313 | 0.4962 | 0.373 | 0.3718 | -0.063 ± 0.0051 | -0.0136 (14) |
| 15-25 | 8973 | 0.211 | 0.1718 | +0.0392 ± 0.0017 | 0.6156 | 0.5071 | 0.5099 | 0.3153 | 0.3125 | -0.069 ± 0.0044 | -0.0533 (3) |
| 25-40 | 6988 | 0.2179 | 0.124 | +0.0939 ± 0.0027 | 0.6293 | 0.3818 | 0.5266 | 0.2111 | 0.2217 | -0.053 ± 0.0041 | -0.02 (4) |
| 40+ | 4697 | 0.3893 | 0.0481 | +0.3413 ± 0.0036 | 1.0145 | 0.1809 | 0.6376 | 0.1068 | 0.0634 | -0.076 ± 0.0031 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1583 | 0.1963 | 0.196 | +0.0003 ± 0.0004 | 0.5708 | 0.5699 | 0.5081 | 0.493 | 0.4908 | -0.075 ± 0.0114 | -0.0221 (56) |
| 3-5 | 1108 | 0.1889 | 0.1889 | +0.0000 ± 0.0011 | 0.5555 | 0.5538 | 0.4985 | 0.4586 | 0.4765 | -0.056 ± 0.0134 | -0.0194 (34) |
| 5-10 | 2238 | 0.1997 | 0.1946 | +0.0051 ± 0.0014 | 0.5889 | 0.5725 | 0.5076 | 0.434 | 0.4366 | -0.078 ± 0.0096 | -0.005 (78) |
| 10-15 | 1556 | 0.2154 | 0.2022 | +0.0132 ± 0.0028 | 0.625 | 0.5876 | 0.5439 | 0.4212 | 0.4274 | -0.093 ± 0.0117 | 0.0012 (66) |
| 15-25 | 2030 | 0.2317 | 0.2076 | +0.0241 ± 0.004 | 0.6612 | 0.5991 | 0.5911 | 0.3961 | 0.433 | -0.090 ± 0.0102 | -0.0214 (59) |
| 25-40 | 1198 | 0.2412 | 0.2108 | +0.0304 ± 0.0081 | 0.6886 | 0.6044 | 0.6884 | 0.3768 | 0.4841 | -0.085 ± 0.0125 | -0.0252 (27) |
| 40+ | 438 | 0.326 | 0.198 | +0.1280 ± 0.0203 | 0.9337 | 0.5773 | 0.8108 | 0.3348 | 0.4543 | -0.094 ± 0.019 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5731 | 0.1767 | 0.1767 | +0.0000 ± 0.0002 | 0.5235 | 0.5229 | 0.5102 | 0.4949 | 0.5013 | -0.042 ± 0.0056 | -0.0154 (103) |
| 3-5 | 3928 | 0.1941 | 0.1933 | +0.0009 ± 0.0006 | 0.5667 | 0.5642 | 0.5024 | 0.4626 | 0.4717 | -0.041 ± 0.0071 | -0.0212 (73) |
| 5-10 | 8004 | 0.1972 | 0.1907 | +0.0065 ± 0.0007 | 0.5817 | 0.5619 | 0.5024 | 0.4288 | 0.4225 | -0.062 ± 0.0049 | -0.0084 (134) |
| 10-15 | 5493 | 0.2105 | 0.1937 | +0.0168 ± 0.0015 | 0.6129 | 0.5682 | 0.5367 | 0.4138 | 0.4054 | -0.074 ± 0.006 | -0.0057 (111) |
| 15-25 | 6765 | 0.2313 | 0.1991 | +0.0322 ± 0.0021 | 0.665 | 0.5775 | 0.5759 | 0.3805 | 0.396 | -0.068 ± 0.0055 | -0.026 (108) |
| 25-40 | 4367 | 0.2572 | 0.1904 | +0.0668 ± 0.0041 | 0.7272 | 0.5543 | 0.6397 | 0.3276 | 0.3799 | -0.062 ± 0.0065 | -0.0277 (53) |
| 40+ | 1968 | 0.368 | 0.1597 | +0.2084 ± 0.0093 | 1.0359 | 0.4754 | 0.7412 | 0.2419 | 0.2932 | -0.058 ± 0.0086 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7866 | 1.022 ± 0.031 | 1.095 | 0.1677 | 0.1696 | 0.216 | 0.2032 |
| gen2 | 7866 | 0.818 ± 0.028 | 1.072 | 0.1737 | 0.1699 | 0.2335 | 0.2032 |
| gen1_elo | 7866 | 1.006 ± 0.031 | 1.084 | 0.1741 | 0.1697 | 0.2151 | 0.2033 |
| gen1_sr | 7866 | 1.003 ± 0.037 | 1.12 | 0.1335 | 0.1714 | 0.2297 | 0.2029 |
| gen1_ledger | 10151 | 0.869 ± 0.023 | 1.07 | 0.1897 | 0.1762 | 0.2171 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 36,516)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 8,822 | 24.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 8,441 | 23.1% |
| BOOK_QUALITY | execution | 6,251 | 17.1% |
| POOR_DATA | data | 4,187 | 11.5% |
| LIMITED_DATA | data | 2,200 | 6.0% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 2,123 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,490 | 4.1% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,406 | 3.9% |
| IN_PLAY_QUOTE | market_freshness/coverage | 1,022 | 2.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 573 | 1.6% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 24.2%, coverage 23.1%, data 17.5%, execution 17.1%, market_freshness/coverage 8.6%, mapping 4.1%, model_calibration_or_unknown 3.9%, model_calibration 1.6%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.6%, START_UNVERIFIABLE 94.9%, LOW_DATA_QUALITY 72.0%, THIN_PLAYER_HISTORY 60.2%, STALE_PLAYER_DATA 52.2%, STALE_KALSHI_QUOTE 47.8%, MODEL_INTERNAL_DISAGREEMENT 41.8%, ASYMMETRIC_SAMPLE_SIZE 33.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 18.5%, PLAYER_IDENTITY_RISK 15.0%, LEVEL_TRANSFER_RISK 9.5%, LOW_DISPLAYED_LIQUIDITY 8.5%, EVENT_MAPPING_RISK 7.0%, MODEL_CALIBRATION_OUTLIER 3.6%, EXTERNAL_MARKET_REJECTION 3.2%, UNKNOWN 0.7%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.5%, POST_SETTLEMENT_OBSERVATION 23.1%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 19,518)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,807 | 34.9% |
| STALE_QUOTE | market_freshness | 3,935 | 20.2% |
| BOOK_QUALITY | execution | 3,222 | 16.5% |
| POOR_DATA | data | 1,779 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,148 | 5.9% |
| IDENTITY_AMBIGUOUS | mapping | 829 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 668 | 3.4% |
| LIMITED_DATA | data | 646 | 3.3% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 344 | 1.8% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 139 | 0.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.9%, market_freshness 20.2%, execution 16.5%, data 12.4%, market_freshness/coverage 9.3%, mapping 4.2%, model_calibration_or_unknown 1.8%, model_calibration 0.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.1%, START_UNVERIFIABLE 97.2%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 62.2%, STALE_KALSHI_QUOTE 55.2%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 41.9%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 22.7%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.0%, EVENT_MAPPING_RISK 8.4%, LOW_DISPLAYED_LIQUIDITY 8.4%, LEVEL_TRANSFER_RISK 8.4%, MODEL_CALIBRATION_OUTLIER 4.6%, EXTERNAL_MARKET_REJECTION 1.8%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.8%, POST_SETTLEMENT_OBSERVATION 34.9%, POSSIBLE_IN_PLAY_QUOTE 6.3%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 15665, "IDENTITY_AMBIGUOUS": 3853}; ticker orientation: {"VERIFIED": 19518}.

Checks: discipline:AMBIGUOUS 1251, discipline:PASS 18267, identity_confidence:AMBIGUOUS 3513, identity_confidence:PASS 16005, level_mapping:NA 1263, level_mapping:PASS 18255, market_pair:AMBIGUOUS 504, market_pair:NA 420, market_pair:PASS 18594, model_complement:NA 382, model_complement:PASS 19136, namesake:AMBIGUOUS 6, namesake:PASS 19512, physical_match_id:NA 6504, physical_match_id:PASS 13014, player_ids:PASS 19518, same_pair_other_event:PASS 19518, ticker_orientation:PASS 19518

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,577 | 3.7% | 3.1% | 1.3% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 24, "market_freshness/coverage": 22} | 5.47 | 0.2217 / 0.2176 (855) | 25.6% | 2.4% | 3.1% | 3.0% |
| CHALLENGER | 13,119 | 16.6% | 6.0% | 11.2% | {"coverage": 1334, "market_freshness": 262, "market_freshness/coverage": 238, "data": 164, "model_calibration_or_unknown": 80, "execution": 41, "model_calibration": 40, "mapping": 17, "possible_market_error": 1} | 7.34 | 0.2213 / 0.2106 (3051) | 41.5% | 13.9% | 4.0% | 22.9% |
| DOUBLES | 2,715 | 46.1% | 46.0% | 6.4% | {"execution": 691, "mapping": 374, "market_freshness": 106, "market_freshness/coverage": 73, "coverage": 7} | 22.95 | 0.2983 / 0.2329 (678) | 8.6% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 25,780 | 25.4% | 17.7% | 33.5% | {"coverage": 2288, "market_freshness": 1363, "execution": 1032, "data": 966, "market_freshness/coverage": 661, "mapping": 224, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.78 | 0.2189 / 0.1987 (5431) | 41.8% | 70.1% | 14.8% | 21.4% |
| ITF_WOMEN | 32,863 | 26.5% | 18.8% | 44.6% | {"coverage": 3099, "market_freshness": 1943, "execution": 1375, "data": 1194, "market_freshness/coverage": 765, "mapping": 208, "model_calibration_or_unknown": 97, "model_calibration": 23} | 12.48 | 0.2029 / 0.1932 (6382) | 42.5% | 57.4% | 10.0% | 21.8% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,905 | 5.9% | 5.0% | 1.5% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.64 | 0.2308 / 0.2206 (808) | 30.3% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.5% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 17.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1025 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 117 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFMATCH-26NOV10KOUPOR-POR` | ITF_MEN | fair_v1 | 87% / 2% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.9h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 305 min (STALE); data POOR (grade D, thinner serve sample 1554.0, ratio 1.02); no external reference |
| 12 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 13 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 15 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 10.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 658 min (STALE); no external reference |
| 16 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 17 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 18 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 19 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 151 min (STALE); no external reference |
| 20 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 21 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 22 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 23 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 24 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 25 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 26 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 27 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 28 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 29 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 30 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 31 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 34 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 13.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 814 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 35 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 36 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 37 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 38 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 39 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 40 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 41 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 43 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 44 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 45 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 46 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 47 | `KXITFWMATCH-26NOV11CORROJ-ROJ` | ITF_WOMEN | fair_v1 | 87% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 375 min (STALE); data POOR (grade D, thinner serve sample 531.0, ratio 1.04); no external reference |
| 48 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9724, "by_level_share_of_ge_25pp": {"ATP": 0.0126, "CHALLENGER": 0.1115, "DOUBLES": 0.0641, "ITF_MEN": 0.3353, "ITF_WOMEN": 0.4459, "OTHER": 0.0006, "WTA": 0.0149, "WTA125": 0.015}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5524, "share_primary_cause_market_settled_or_in_play": 0.4418, "share_primary_cause_stale_quote_only": 0.2016}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 19518, "identity_ambiguous_share": 0.1974, "ticker_orientation": {"VERIFIED": 19518}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 13014, "with_external": 640, "coverage": 0.0492, "external_status": {"EXTERNAL_STALE": 405, "AGREES_WITH_KALSHI": 222, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 405, "MODEL_LONE_OUTLIER": 222, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3469, "share_external_supports_model": 0.0203}, "pregame_clean_ge_25pp": {"n": 5986, "with_external": 609, "coverage": 0.1017, "external_status": {"EXTERNAL_STALE": 381, "AGREES_WITH_KALSHI": 215, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 381, "MODEL_LONE_OUTLIER": 215, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.353, "share_external_supports_model": 0.0213}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 477.0, "median_sample_ratio": 2.45, "median_min_matches": 18.0, "median_max_days_since_last": 246.0, "share_severe_asymmetry": 0.2076, "data_status": {"POOR": 11097, "LIMITED": 4904, "ADEQUATE": 3517}, "comparison_lt_10pp": {"median_thinner_serve_points": 1686.0, "median_sample_ratio": 1.71, "median_min_matches": 87.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1583, "model_minus_observed": 0.0697, "kalshi_minus_observed": -0.0701, "brier_diff_model_minus_kalshi": 0.0036}, "4-10x": {"n": 1080, "model_minus_observed": 0.0912, "kalshi_minus_observed": -0.0538, "brier_diff_model_minus_kalshi": 0.0106}, "<2x": {"n": 3874, "model_minus_observed": 0.1026, "kalshi_minus_observed": -0.02, "brier_diff_model_minus_kalshi": 0.015}, ">=10x": {"n": 1329, "model_minus_observed": 0.1267, "kalshi_minus_observed": -0.0465, "brier_diff_model_minus_kalshi": 0.0189}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7866, "model": {"intercept": -0.559, "slope": 0.818, "slope_se": 0.028}, "kalshi_mid_same_rows": {"intercept": 0.172, "slope": 1.072, "slope_se": 0.032}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2335, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0304, "brier_diff_se": 0.0021, "model_logloss": 0.6646, "kalshi_logloss": 0.5885}, "fair_v1": {"n": 7866, "model": {"intercept": -0.468, "slope": 1.022, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.221, "slope": 1.095, "slope_se": 0.032}, "mean_extremity_model": 0.1677, "mean_extremity_kalshi": 0.1696, "model_brier": 0.216, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0127, "brier_diff_se": 0.0017, "model_logloss": 0.6212, "kalshi_logloss": 0.5885}, "gen1_elo": {"n": 7866, "model": {"intercept": -0.457, "slope": 1.006, "slope_se": 0.031}, "kalshi_mid_same_rows": {"intercept": 0.222, "slope": 1.084, "slope_se": 0.032}, "mean_extremity_model": 0.1741, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2151, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0118, "brier_diff_se": 0.0017, "model_logloss": 0.6198, "kalshi_logloss": 0.5887}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2524, "share_ge_15": 0.448, "median_abs_gap": 13.14, "n": 51556}, "gen1_elo": {"share_ge_25": 0.2501, "share_ge_15": 0.444, "median_abs_gap": 12.99, "n": 51556}, "gen1_sr": {"share_ge_25": 0.3152, "share_ge_15": 0.5236, "median_abs_gap": 15.95, "n": 51556}, "gen2": {"share_ge_25": 0.3153, "share_ge_15": 0.5119, "median_abs_gap": 15.49, "n": 51556}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1517, "share_ge_15": 0.3547, "median_abs_gap": 10.71, "n": 39441}, "gen1_elo": {"share_ge_25": 0.1502, "share_ge_15": 0.3497, "median_abs_gap": 10.51, "n": 39441}, "gen1_sr": {"share_ge_25": 0.2155, "share_ge_15": 0.4398, "median_abs_gap": 13.0, "n": 39443}, "gen2": {"share_ge_25": 0.2303, "share_ge_15": 0.4385, "median_abs_gap": 12.83, "n": 39443}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.47, "share_ge_25_all": 0.0373, "share_ge_25_pregame_clean": 0.0312}, "WTA": {"median_abs_gap_pregame_clean": 7.64, "share_ge_25_all": 0.0593, "share_ge_25_pregame_clean": 0.0503}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.235, "share_within_10pp_all": 0.4365, "share_within_10pp_pregame_clean": 0.4907, "corr_model_vs_mid_pregame_clean": 0.8497}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1139, "model_brier": 0.1973, "kalshi_brier": 0.1973, "brier_diff_model_minus_kalshi": -0.0001}, "10-15": {"n_settled": 1367, "model_brier": 0.2184, "kalshi_brier": 0.2089, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1744, "model_brier": 0.2255, "kalshi_brier": 0.2064, "brier_diff_model_minus_kalshi": 0.0191}, "25-40": {"n_settled": 999, "model_brier": 0.2253, "kalshi_brier": 0.2029, "brier_diff_model_minus_kalshi": 0.0224}, "3-5": {"n_settled": 725, "model_brier": 0.2071, "kalshi_brier": 0.2065, "brier_diff_model_minus_kalshi": 0.0006}, "40+": {"n_settled": 207, "model_brier": 0.3061, "kalshi_brier": 0.1699, "brier_diff_model_minus_kalshi": 0.1362}, "5-10": {"n_settled": 1685, "model_brier": 0.2039, "kalshi_brier": 0.2022, "brier_diff_model_minus_kalshi": 0.0017}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.559, "slope": 0.818, "slope_se": 0.028}, "kalshi_slope": {"intercept": 0.172, "slope": 1.072, "slope_se": 0.032}, "n": 7866}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.502, "slope": 0.869, "slope_se": 0.023}, "kalshi_slope": {"intercept": 0.154, "slope": 1.07, "slope_se": 0.027}, "n": 10151}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 678, "model_brier": 0.2983, "kalshi_brier": 0.2329, "brier_diff_model_minus_kalshi": 0.0654, "brier_diff_se": 0.0112, "corr_model_outcome": 0.1027, "corr_kalshi_outcome": 0.274}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
