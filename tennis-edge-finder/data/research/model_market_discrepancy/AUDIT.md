# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-06T09:35Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 80,694): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.6%, doubles 6.8%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,448): MARKET_ALREADY_SETTLED_WHEN_PRICED 33.9%, STALE_QUOTE 19.5%, BOOK_QUALITY 17.6%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 33.9%, market_freshness 19.5%, execution 17.6%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,448 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.6% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1722.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.032, Gen-2 0.826, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 892 model 0.2228 vs Kalshi 0.2039; n 186 model 0.2966 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 342,510 model-market comparisons (560,903 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 114,131 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-06T09:15:48.408505+00:00'], shadow board 92,668 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-06T09:15:52.124656+00:00'], Model 4 42,353 rows, 28,317 settled tickers, 10,718 tickers with an external scan.
* By model: {"gen1_ledger": 76889, "gen1_elo": 46567, "fair_v1": 46567, "gen2": 46567, "gen1_sr": 46567, "model4_fundamental": 39718, "model4_conditioned": 39635}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 80,694 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.0 | 11.81 | 40.7% | 21.6% |
| MW fair_v1 | 46,567 | 12.9 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.8 | 13.01 | 44.3% | 24.6% |
| MW gen1_elo | 46,567 | 12.6 | 8.8 | 19.3 | 15.4 | 19.6 | 14.6 | 9.7 | 12.77 | 43.9% | 24.3% |
| MW gen1_ledger | 34,127 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| MW gen1_sr | 46,567 | 10.1 | 7.3 | 16.7 | 14.0 | 20.7 | 18.7 | 12.5 | 15.77 | 51.9% | 31.2% |
| MW gen2 | 46,567 | 11.0 | 7.6 | 16.7 | 13.8 | 19.7 | 17.7 | 13.6 | 15.43 | 50.9% | 31.3% |
| all families model4_conditioned | 39,635 | 22.2 | 18.0 | 34.1 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,718 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.7%, >=20pp 30.0%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.37pp; >=10pp 45.0%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,931 | 28.6 | 15.6 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.8% | 4.2% |
| CHALLENGER | 6,967 | 16.0 | 9.8 | 20.8 | 15.3 | 16.2 | 11.3 | 10.7 | 10.91 | 38.1% | 22.0% |
| ITF_MEN | 13,173 | 9.8 | 7.4 | 17.1 | 15.2 | 21.3 | 17.3 | 11.9 | 15.18 | 50.5% | 29.2% |
| ITF_WOMEN | 18,136 | 9.6 | 7.1 | 16.1 | 14.8 | 22.1 | 18.3 | 12.1 | 15.82 | 52.5% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,027 | 16.8 | 13.2 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,931 | 26.9 | 15.8 | 26.0 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.8% | 4.5% |
| CHALLENGER | 6,967 | 14.7 | 9.1 | 18.9 | 13.9 | 18.7 | 13.5 | 11.3 | 12.47 | 43.4% | 24.8% |
| ITF_MEN | 13,173 | 8.2 | 6.1 | 15.2 | 13.8 | 20.1 | 20.5 | 16.1 | 17.85 | 56.7% | 36.6% |
| ITF_WOMEN | 18,136 | 7.8 | 5.8 | 14.1 | 12.8 | 20.8 | 21.1 | 17.5 | 19.09 | 59.4% | 38.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,027 | 14.1 | 10.2 | 21.7 | 16.1 | 22.4 | 12.9 | 2.5 | 11.23 | 37.9% | 15.5% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,931 | 22.9 | 14.0 | 25.3 | 15.6 | 15.0 | 6.1 | 1.2 | 7.2 | 22.2% | 7.3% |
| CHALLENGER | 6,967 | 15.2 | 9.5 | 20.8 | 15.7 | 16.1 | 11.8 | 10.8 | 11.21 | 38.8% | 22.6% |
| ITF_MEN | 13,173 | 9.6 | 7.3 | 17.3 | 14.3 | 22.0 | 17.2 | 12.4 | 15.57 | 51.6% | 29.6% |
| ITF_WOMEN | 18,136 | 9.3 | 6.9 | 16.3 | 15.7 | 22.2 | 18.1 | 11.4 | 15.57 | 51.8% | 29.5% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,027 | 22.7 | 17.1 | 31.9 | 15.2 | 8.7 | 3.3 | 1.1 | 6.12 | 13.1% | 4.4% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,332 | 26.9 | 19.7 | 29.9 | 12.3 | 8.2 | 2.6 | 0.4 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,506 | 22.3 | 14.6 | 27.6 | 14.8 | 13.4 | 5.7 | 1.5 | 7.09 | 20.7% | 7.3% |
| DOUBLES | 2,539 | 4.9 | 4.5 | 13.0 | 11.1 | 20.1 | 24.5 | 21.9 | 23.31 | 66.5% | 46.4% |
| ITF_MEN | 9,787 | 13.0 | 9.6 | 21.4 | 15.8 | 21.6 | 12.9 | 5.8 | 11.76 | 40.3% | 18.7% |
| ITF_WOMEN | 11,786 | 13.3 | 9.2 | 20.0 | 15.7 | 21.4 | 14.9 | 5.5 | 12.23 | 41.7% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,772 | 23.9 | 15.9 | 31.4 | 17.0 | 9.0 | 2.6 | 0.2 | 6.57 | 11.8% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,816 | 29.0 | 15.8 | 28.0 | 13.3 | 10.3 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,935 | 20.6 | 12.1 | 25.6 | 18.0 | 16.1 | 5.9 | 1.6 | 8.27 | 23.6% | 7.5% |
| ITF_MEN | 9,653 | 12.0 | 8.6 | 20.6 | 17.4 | 22.1 | 14.1 | 5.2 | 12.39 | 41.3% | 19.3% |
| ITF_WOMEN | 13,368 | 11.4 | 8.5 | 18.9 | 17.0 | 24.0 | 15.2 | 4.9 | 13.18 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,915 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.2 | 0.6 | 8.49 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,816 | 27.2 | 16.2 | 26.3 | 15.3 | 11.3 | 3.3 | 0.4 | 5.95 | 15.0% | 3.7% |
| CHALLENGER | 4,935 | 18.4 | 11.4 | 23.7 | 16.3 | 19.1 | 9.2 | 1.8 | 9.0 | 30.2% | 11.1% |
| ITF_MEN | 9,654 | 9.7 | 7.2 | 17.6 | 16.0 | 21.8 | 18.6 | 9.1 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,369 | 8.9 | 6.8 | 16.1 | 14.4 | 22.8 | 20.4 | 10.7 | 16.51 | 53.9% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,915 | 14.3 | 10.3 | 22.0 | 16.3 | 22.6 | 12.6 | 1.9 | 11.03 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,275 | 27.1 | 19.9 | 29.9 | 12.4 | 7.9 | 2.5 | 0.3 | 5.3 | 10.7% | 2.8% |
| CHALLENGER | 3,982 | 23.7 | 15.4 | 28.7 | 15.0 | 12.8 | 4.0 | 0.4 | 6.61 | 17.2% | 4.4% |
| DOUBLES | 2,383 | 4.8 | 4.6 | 13.2 | 11.2 | 19.9 | 24.5 | 21.9 | 23.22 | 66.3% | 46.4% |
| ITF_MEN | 8,424 | 13.8 | 10.2 | 22.9 | 16.3 | 21.7 | 11.4 | 3.8 | 10.84 | 36.9% | 15.2% |
| ITF_WOMEN | 10,100 | 14.0 | 9.8 | 21.1 | 16.2 | 21.5 | 13.8 | 3.6 | 11.42 | 39.0% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,711 | 24.2 | 16.3 | 31.4 | 17.0 | 9.0 | 2.0 | 0.1 | 6.43 | 11.1% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,539 | 4.9 | 4.5 | 13.0 | 11.1 | 20.1 | 24.5 | 21.9 | 23.31 | 66.5% | 46.4% |
| singles | 31,588 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.73 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 159 | 7.5 | 8.2 | 12.6 | 7.5 | 20.1 | 28.9 | 15.1 | 21.5 | 64.1% | 44.0% |
| Clay | 9,551 | 12.7 | 9.1 | 19.9 | 15.7 | 19.7 | 13.8 | 9.1 | 12.59 | 42.6% | 22.9% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,331 | 13.4 | 8.7 | 18.8 | 15.2 | 19.2 | 14.8 | 9.8 | 12.85 | 43.8% | 24.6% |
| UNKNOWN | 6,289 | 10.6 | 7.6 | 17.0 | 16.4 | 21.4 | 16.0 | 11.0 | 14.3 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,200 | 19.5 | 11.9 | 22.5 | 15.9 | 15.0 | 9.1 | 6.1 | 8.88 | 30.2% | 15.3% |
| B | 5,686 | 12.8 | 8.7 | 19.8 | 15.7 | 19.6 | 12.7 | 10.7 | 12.61 | 43.0% | 23.4% |
| C | 6,603 | 12.0 | 8.9 | 19.5 | 15.7 | 18.6 | 14.7 | 10.6 | 12.91 | 43.8% | 25.2% |
| D | 7,567 | 11.7 | 8.3 | 17.9 | 15.4 | 21.6 | 15.7 | 9.3 | 13.8 | 46.6% | 25.0% |
| F | 13,511 | 7.5 | 5.6 | 14.8 | 14.7 | 23.6 | 20.8 | 13.1 | 17.73 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,120 | 24.5 | 16.1 | 29.1 | 15.1 | 10.6 | 3.4 | 1.2 | 6.37 | 15.2% | 4.6% |
| B | 4,786 | 16.6 | 10.8 | 24.2 | 16.9 | 18.8 | 9.6 | 3.1 | 9.68 | 31.5% | 12.6% |
| C | 6,743 | 11.1 | 7.8 | 19.6 | 14.7 | 20.9 | 15.6 | 10.3 | 13.49 | 46.8% | 25.9% |
| D | 5,120 | 14.5 | 10.1 | 21.5 | 15.3 | 20.7 | 12.6 | 5.3 | 11.19 | 38.6% | 17.8% |
| F | 8,358 | 10.2 | 8.4 | 16.2 | 14.6 | 23.3 | 19.5 | 7.8 | 15.32 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,907 | 17.8 | 10.9 | 21.6 | 15.7 | 15.3 | 10.0 | 8.7 | 9.95 | 34.0% | 18.7% |
| LIMITED | 10,192 | 13.7 | 9.8 | 20.4 | 15.9 | 19.3 | 13.3 | 7.5 | 11.82 | 40.2% | 20.9% |
| POOR | 21,468 | 9.0 | 6.6 | 16.0 | 15.0 | 22.8 | 18.8 | 11.8 | 16.1 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,726 | 23.8 | 17.9 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.9 | 9.7% | 3.3% |
| GAME_SPREAD | 6,609 | 22.6 | 15.4 | 32.1 | 16.9 | 9.0 | 3.4 | 0.7 | 6.71 | 13.0% | 4.1% |
| MATCH_WINNER | 34,127 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,252 | 27.9 | 16.7 | 30.8 | 12.7 | 9.2 | 2.4 | 0.3 | 5.64 | 11.9% | 2.7% |
| TOTAL_GAMES | 11,151 | 9.8 | 10.8 | 35.6 | 25.9 | 10.7 | 4.2 | 2.9 | 9.2 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,008 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,144 | 47.0 | 16.1 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,483 | 6.6 | 9.8 | 40.2 | 30.2 | 7.5 | 3.3 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,043 | 23.9 | 16.7 | 34.8 | 14.6 | 6.9 | 2.6 | 0.5 | 6.04 | 10.0% | 3.1% |
| GAME_SPREAD | 9,153 | 20.6 | 13.6 | 28.2 | 20.0 | 11.9 | 4.5 | 1.2 | 7.61 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,522 | 10.0 | 10.8 | 36.2 | 24.3 | 11.6 | 4.5 | 2.6 | 9.06 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 46,567 | 44.3% | 24.6% | 13.01 | 35.3% | 15.1% | 10.68 |
| gen1_elo | 46,567 | 43.9% | 24.3% | 12.77 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 46,567 | 51.9% | 31.2% | 15.77 | 43.9% | 21.6% | 13.0 |
| gen2 | 46,567 | 50.9% | 31.3% | 15.43 | 43.9% | 23.0% | 12.85 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,896 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,671 | 10.9 | 7.3 | 16.9 | 14.0 | 19.3 | 16.9 | 14.7 | 15.36 | 50.9% | 31.6% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,595 | 16.4 | 11.2 | 22.8 | 15.3 | 17.9 | 11.5 | 4.8 | 9.87 | 34.3% | 16.3% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 80,694 | 27595 | 23368 | 29731 | 24.7 | 124.2 | 1451.1 |
| ge_15pp | 32,872 | 9457 | 8324 | 15091 | 28.1 | 429.9 | 1451.1 |
| ge_25pp | 17,448 | 4507 | 3632 | 9309 | 33.1 | 577.5 | 1431.1 |
| lt_10pp | 35,458 | 13917 | 11051 | 10490 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261106T093544Z-a157249a`: 297 priced rows, quote age at build {'median': 52.4, 'max': 72.4}, freshness {'STALE': 297}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,632 | 19.3 | 10.9 | 25.5 | 17.8 | 18.1 | 7.5 | 1.0 | 8.79 | 26.5% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 957 | 66.2 | 33.8 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,063 | 0.0 | 2.3 | 37.2 | 26.4 | 24.1 | 9.2 | 0.9 | 11.81 | 34.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 46,567 | 7760 (16.7%) | 26.6% | 1.0% | {"EXTERNAL_STALE": 4632, "AGREES_WITH_KALSHI": 2063, "ALL_AGREE": 957, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,616 | 1963 (9.5%) | 35.9% | 1.5% | {"EXTERNAL_STALE": 1229, "AGREES_WITH_KALSHI": 704, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,479 | 610 (5.3%) | 33.9% | 2.1% | {"EXTERNAL_STALE": 390, "AGREES_WITH_KALSHI": 207, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,422 | 580 (10.7%) | 34.5% | 2.2% | {"EXTERNAL_STALE": 367, "AGREES_WITH_KALSHI": 200, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,772 | 4423 (23.6%) | 18.4% | 1.0% | {"EXTERNAL_STALE": 2579, "ALL_AGREE": 957, "AGREES_WITH_KALSHI": 814, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,142 | 10.5 | 7.7 | 19.5 | 14.7 | 21.6 | 16.2 | 9.8 | 14.02 | 47.6% | 26.1% |
| 4-10x | 6,243 | 11.4 | 8.6 | 18.4 | 15.2 | 22.0 | 14.3 | 10.1 | 13.75 | 46.5% | 24.4% |
| <2x | 23,745 | 14.9 | 9.8 | 19.8 | 16.1 | 17.6 | 13.1 | 8.8 | 11.55 | 39.5% | 21.9% |
| >=10x | 7,437 | 10.5 | 6.4 | 15.0 | 14.4 | 21.8 | 18.9 | 13.0 | 16.35 | 53.7% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,200 | 12.5 | 8.7 | 19.9 | 16.2 | 19.0 | 13.5 | 10.2 | 12.68 | 42.8% | 23.8% |
| 300-1000 | 10,093 | 11.8 | 8.8 | 17.7 | 15.2 | 20.7 | 16.3 | 9.4 | 13.72 | 46.5% | 25.8% |
| <300 | 14,619 | 8.3 | 5.8 | 15.2 | 14.7 | 23.1 | 19.8 | 13.0 | 17.1 | 56.0% | 32.8% |
| >=3000 | 9,655 | 21.4 | 12.9 | 23.9 | 15.7 | 14.0 | 7.2 | 5.0 | 7.75 | 26.2% | 12.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1414 | 0.5477 | 0.4083 | 0.4901 | +0.058 | -0.082 | 0.0004 ± 0.0041 |
| ratio 4-10x | 968 | 0.5764 | 0.4318 | 0.4876 | +0.089 | -0.056 | 0.009 ± 0.0051 |
| ratio <2x | 3436 | 0.5368 | 0.4137 | 0.4363 | +0.101 | -0.023 | 0.0147 ± 0.0024 |
| ratio >=10x | 1188 | 0.5639 | 0.3907 | 0.447 | +0.117 | -0.056 | 0.0148 ± 0.0052 |
| thinner_sample 1000-3000 | 1940 | 0.5393 | 0.4119 | 0.4474 | +0.092 | -0.035 | 0.0114 ± 0.0033 |
| thinner_sample 300-1000 | 1594 | 0.5633 | 0.4226 | 0.4755 | +0.088 | -0.053 | 0.0043 ± 0.0039 |
| thinner_sample <300 | 2282 | 0.5573 | 0.3895 | 0.4549 | +0.102 | -0.065 | 0.0131 ± 0.0037 |
| thinner_sample >=3000 | 1190 | 0.53 | 0.4363 | 0.4462 | +0.084 | -0.010 | 0.0153 ± 0.0033 |
| data_status ADEQUATE | 1934 | 0.5322 | 0.4288 | 0.44 | +0.092 | -0.011 | 0.0155 ± 0.0028 |
| data_status LIMITED | 1704 | 0.5476 | 0.415 | 0.4665 | +0.081 | -0.052 | 0.007 ± 0.0036 |
| data_status POOR | 3368 | 0.5594 | 0.3991 | 0.4599 | +0.100 | -0.061 | 0.0105 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1005 | 0.197 | 0.1974 | -0.0003 ± 0.0005 | 0.5738 | 0.5746 | 0.5024 | 0.4873 | 0.4995 | -0.096 ± 0.0148 | -0.0087 (8) |
| 3-5 | 646 | 0.2049 | 0.205 | -0.0001 ± 0.0014 | 0.5937 | 0.5925 | 0.5029 | 0.463 | 0.483 | -0.095 ± 0.0183 | 0.01 (2) |
| 5-10 | 1508 | 0.201 | 0.2003 | +0.0007 ± 0.0017 | 0.5882 | 0.584 | 0.5115 | 0.4377 | 0.4675 | -0.089 ± 0.0119 | -0.0143 (7) |
| 10-15 | 1216 | 0.2186 | 0.2091 | +0.0095 ± 0.0033 | 0.6292 | 0.6014 | 0.5229 | 0.3994 | 0.4219 | -0.106 ± 0.0133 | -0.048 (5) |
| 15-25 | 1553 | 0.2244 | 0.208 | +0.0164 ± 0.0045 | 0.6433 | 0.5995 | 0.5748 | 0.3801 | 0.4359 | -0.101 ± 0.0116 | -0.004 (10) |
| 25-40 | 892 | 0.2228 | 0.2039 | +0.0189 ± 0.009 | 0.6355 | 0.5882 | 0.6514 | 0.3415 | 0.4664 | -0.069 ± 0.0138 | -0.06 (2) |
| 40+ | 186 | 0.2966 | 0.1748 | +0.1217 ± 0.0275 | 0.7985 | 0.5224 | 0.73 | 0.2752 | 0.3763 | -0.084 ± 0.0267 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5278 | 0.1854 | 0.1862 | -0.0009 ± 0.0002 | 0.5467 | 0.5476 | 0.4887 | 0.4735 | 0.504 | -0.022 ± 0.006 | -0.01 (28) |
| 3-5 | 3560 | 0.1976 | 0.196 | +0.0016 ± 0.0006 | 0.5755 | 0.5694 | 0.4808 | 0.441 | 0.4396 | -0.056 ± 0.0075 | 0.0 (3) |
| 5-10 | 7671 | 0.2007 | 0.1976 | +0.0031 ± 0.0008 | 0.587 | 0.5763 | 0.4844 | 0.4107 | 0.4272 | -0.042 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6360 | 0.2018 | 0.1859 | +0.0159 ± 0.0013 | 0.59 | 0.5454 | 0.485 | 0.361 | 0.3591 | -0.063 ± 0.0054 | -0.0281 (16) |
| 15-25 | 8021 | 0.2056 | 0.167 | +0.0386 ± 0.0018 | 0.6028 | 0.4962 | 0.4989 | 0.3035 | 0.3035 | -0.068 ± 0.0045 | -0.0027 (45) |
| 25-40 | 6200 | 0.2231 | 0.1261 | +0.0970 ± 0.0028 | 0.6405 | 0.3877 | 0.5269 | 0.2132 | 0.2198 | -0.059 ± 0.0044 | -0.0733 (3) |
| 40+ | 4110 | 0.3827 | 0.0443 | +0.3384 ± 0.0037 | 0.9971 | 0.1718 | 0.6311 | 0.1022 | 0.0586 | -0.076 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 808 | 0.2043 | 0.2047 | -0.0003 ± 0.0005 | 0.5892 | 0.5904 | 0.5064 | 0.4915 | 0.5136 | -0.103 ± 0.0171 | -0.0117 (6) |
| 3-5 | 577 | 0.2105 | 0.2075 | +0.0030 ± 0.0015 | 0.6033 | 0.5969 | 0.5118 | 0.4722 | 0.4506 | -0.132 ± 0.0204 | 0.01 (2) |
| 5-10 | 1291 | 0.2069 | 0.2049 | +0.0020 ± 0.0019 | 0.6001 | 0.5946 | 0.5391 | 0.4645 | 0.4911 | -0.090 ± 0.013 | -0.01 (4) |
| 10-15 | 1124 | 0.2113 | 0.2062 | +0.0052 ± 0.0034 | 0.6149 | 0.5979 | 0.5633 | 0.4389 | 0.4831 | -0.096 ± 0.0141 | -0.04 (5) |
| 15-25 | 1642 | 0.2305 | 0.2124 | +0.0182 ± 0.0045 | 0.6554 | 0.6092 | 0.5843 | 0.3888 | 0.4415 | -0.097 ± 0.0116 | -0.012 (10) |
| 25-40 | 1149 | 0.2665 | 0.1967 | +0.0698 ± 0.0082 | 0.7439 | 0.5731 | 0.6583 | 0.3441 | 0.3925 | -0.120 ± 0.0131 | -0.008 (5) |
| 40+ | 415 | 0.3727 | 0.162 | +0.2107 ± 0.0198 | 1.0163 | 0.4901 | 0.7352 | 0.2464 | 0.2892 | -0.087 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4540 | 0.1916 | 0.1919 | -0.0003 ± 0.0002 | 0.5586 | 0.559 | 0.5074 | 0.4923 | 0.5099 | -0.038 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3095 | 0.1926 | 0.1916 | +0.0010 ± 0.0006 | 0.5616 | 0.5582 | 0.5103 | 0.4707 | 0.4766 | -0.046 ± 0.0081 | 0.01 (2) |
| 5-10 | 6837 | 0.1973 | 0.1939 | +0.0035 ± 0.0008 | 0.5795 | 0.5671 | 0.5081 | 0.434 | 0.4503 | -0.041 ± 0.0054 | -0.0117 (6) |
| 10-15 | 5708 | 0.2018 | 0.1914 | +0.0104 ± 0.0014 | 0.5928 | 0.5599 | 0.5103 | 0.3864 | 0.4073 | -0.044 ± 0.0059 | -0.0189 (18) |
| 15-25 | 8072 | 0.2165 | 0.1814 | +0.0351 ± 0.0019 | 0.6291 | 0.5319 | 0.5243 | 0.3287 | 0.3393 | -0.058 ± 0.0048 | -0.0084 (43) |
| 25-40 | 7275 | 0.2508 | 0.1372 | +0.1136 ± 0.0028 | 0.7085 | 0.4193 | 0.5598 | 0.2429 | 0.2257 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5673 | 0.4017 | 0.0591 | +0.3425 ± 0.0037 | 1.0592 | 0.2131 | 0.6546 | 0.1191 | 0.0806 | -0.074 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 985 | 0.1959 | 0.1974 | -0.0015 ± 0.0005 | 0.5716 | 0.5752 | 0.5028 | 0.4873 | 0.536 | -0.048 ± 0.0148 | -0.012 (10) |
| 3-5 | 687 | 0.2069 | 0.2054 | +0.0015 ± 0.0014 | 0.5994 | 0.5944 | 0.4947 | 0.4552 | 0.4585 | -0.110 ± 0.0181 | -0.0 (4) |
| 5-10 | 1539 | 0.2022 | 0.1988 | +0.0035 ± 0.0017 | 0.5893 | 0.5797 | 0.5125 | 0.4387 | 0.4516 | -0.104 ± 0.0117 | -0.01 (9) |
| 10-15 | 1231 | 0.2107 | 0.2014 | +0.0093 ± 0.0032 | 0.612 | 0.5847 | 0.5362 | 0.413 | 0.4387 | -0.108 ± 0.0128 | -0.0286 (7) |
| 15-25 | 1485 | 0.2304 | 0.2125 | +0.0179 ± 0.0047 | 0.658 | 0.6093 | 0.5853 | 0.3911 | 0.4418 | -0.107 ± 0.012 | -0.03 (1) |
| 25-40 | 884 | 0.2126 | 0.2085 | +0.0041 ± 0.009 | 0.6139 | 0.599 | 0.6592 | 0.3483 | 0.4955 | -0.056 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5112 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.5461 | 0.547 | 0.4859 | 0.4706 | 0.4908 | -0.031 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3629 | 0.2041 | 0.2024 | +0.0017 ± 0.0006 | 0.5928 | 0.5871 | 0.4775 | 0.438 | 0.4376 | -0.055 ± 0.0076 | -0.01 (19) |
| 5-10 | 7840 | 0.1957 | 0.1907 | +0.0050 ± 0.0007 | 0.5745 | 0.5587 | 0.487 | 0.413 | 0.4165 | -0.054 ± 0.005 | -0.0105 (37) |
| 10-15 | 6296 | 0.1933 | 0.1781 | +0.0152 ± 0.0013 | 0.5711 | 0.5273 | 0.4937 | 0.3704 | 0.3702 | -0.062 ± 0.0053 | -0.0146 (13) |
| 15-25 | 8114 | 0.2113 | 0.1723 | +0.0390 ± 0.0018 | 0.6165 | 0.5082 | 0.5122 | 0.3177 | 0.3156 | -0.070 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6142 | 0.2171 | 0.1274 | +0.0897 ± 0.0029 | 0.6275 | 0.3902 | 0.5293 | 0.2138 | 0.2317 | -0.049 ± 0.0044 | -0.02 (4) |
| 40+ | 4067 | 0.3919 | 0.0493 | +0.3426 ± 0.0039 | 1.0217 | 0.1844 | 0.6405 | 0.1084 | 0.0657 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1417 | 0.1973 | 0.1974 | -0.0001 ± 0.0004 | 0.573 | 0.573 | 0.5084 | 0.4934 | 0.4996 | -0.067 ± 0.0121 | -0.0213 (54) |
| 3-5 | 1016 | 0.1885 | 0.1883 | +0.0003 ± 0.0011 | 0.5551 | 0.5525 | 0.4951 | 0.4552 | 0.4705 | -0.059 ± 0.0139 | -0.0194 (34) |
| 5-10 | 2055 | 0.1991 | 0.1946 | +0.0045 ± 0.0015 | 0.5873 | 0.5721 | 0.5071 | 0.4335 | 0.4404 | -0.074 ± 0.01 | -0.005 (78) |
| 10-15 | 1416 | 0.2136 | 0.2014 | +0.0121 ± 0.003 | 0.6203 | 0.5864 | 0.5423 | 0.4195 | 0.4301 | -0.088 ± 0.0123 | 0.0014 (65) |
| 15-25 | 1834 | 0.2303 | 0.2069 | +0.0234 ± 0.0042 | 0.6573 | 0.5974 | 0.5892 | 0.3942 | 0.434 | -0.088 ± 0.0107 | -0.0214 (59) |
| 25-40 | 1114 | 0.2403 | 0.2097 | +0.0306 ± 0.0084 | 0.6861 | 0.6021 | 0.6882 | 0.376 | 0.4829 | -0.088 ± 0.0129 | -0.0252 (27) |
| 40+ | 394 | 0.3272 | 0.2019 | +0.1254 ± 0.0216 | 0.9427 | 0.5874 | 0.8158 | 0.3398 | 0.4619 | -0.098 ± 0.0203 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5218 | 0.1775 | 0.1777 | -0.0002 ± 0.0002 | 0.5254 | 0.5253 | 0.5121 | 0.4969 | 0.5094 | -0.036 ± 0.0059 | -0.0145 (98) |
| 3-5 | 3601 | 0.1955 | 0.1947 | +0.0008 ± 0.0006 | 0.5698 | 0.5673 | 0.5002 | 0.4605 | 0.471 | -0.040 ± 0.0074 | -0.0204 (72) |
| 5-10 | 7324 | 0.196 | 0.1898 | +0.0062 ± 0.0008 | 0.5788 | 0.5596 | 0.5007 | 0.4271 | 0.4227 | -0.061 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5027 | 0.2084 | 0.1928 | +0.0156 ± 0.0015 | 0.6074 | 0.5662 | 0.5371 | 0.4142 | 0.4108 | -0.070 ± 0.0063 | -0.0053 (106) |
| 15-25 | 6097 | 0.2301 | 0.1992 | +0.0310 ± 0.0023 | 0.6615 | 0.5774 | 0.575 | 0.3797 | 0.399 | -0.066 ± 0.0058 | -0.026 (108) |
| 25-40 | 4008 | 0.257 | 0.1894 | +0.0676 ± 0.0043 | 0.7273 | 0.5521 | 0.6395 | 0.3269 | 0.3775 | -0.067 ± 0.0067 | -0.0246 (52) |
| 40+ | 1765 | 0.3706 | 0.1596 | +0.2111 ± 0.0098 | 1.0464 | 0.475 | 0.7438 | 0.2431 | 0.2929 | -0.064 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7006 | 1.032 ± 0.033 | 1.107 | 0.1694 | 0.1694 | 0.2143 | 0.2033 |
| gen2 | 7006 | 0.826 ± 0.03 | 1.078 | 0.1737 | 0.1697 | 0.2328 | 0.2032 |
| gen1_elo | 7006 | 1.011 ± 0.032 | 1.097 | 0.1759 | 0.1694 | 0.2136 | 0.2034 |
| gen1_sr | 7006 | 1.01 ± 0.039 | 1.138 | 0.1336 | 0.1714 | 0.2291 | 0.2028 |
| gen1_ledger | 9246 | 0.867 ± 0.024 | 1.078 | 0.1901 | 0.1765 | 0.2165 | 0.1999 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 32,872)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,616 | 23.2% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,387 | 22.5% |
| BOOK_QUALITY | execution | 5,911 | 18.0% |
| POOR_DATA | data | 3,834 | 11.7% |
| LIMITED_DATA | data | 2,048 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,880 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,358 | 4.1% |
| IDENTITY_AMBIGUOUS | mapping | 1,357 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 936 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 544 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.2%, coverage 22.5%, execution 18.0%, data 17.9%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.1%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.2%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.9%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,448)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,919 | 33.9% |
| STALE_QUOTE | market_freshness | 3,402 | 19.5% |
| BOOK_QUALITY | execution | 3,068 | 17.6% |
| POOR_DATA | data | 1,616 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,004 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 756 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 613 | 3.5% |
| LIMITED_DATA | data | 601 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 335 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 133 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 33.9%, market_freshness 19.5%, execution 17.6%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 53.3%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.6%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 33.9%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13903, "IDENTITY_AMBIGUOUS": 3545}; ticker orientation: {"VERIFIED": 17448}.

Checks: discipline:AMBIGUOUS 1179, discipline:PASS 16269, identity_confidence:AMBIGUOUS 3215, identity_confidence:PASS 14233, level_mapping:NA 1191, level_mapping:PASS 16257, market_pair:AMBIGUOUS 491, market_pair:NA 381, market_pair:PASS 16576, model_complement:NA 343, model_complement:PASS 17105, namesake:AMBIGUOUS 6, namesake:PASS 17442, physical_match_id:NA 5969, physical_match_id:PASS 11479, player_ids:PASS 17448, same_pair_other_event:PASS 17448, ticker_orientation:PASS 17448

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,263 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.52 | 0.2264 / 0.2215 (793) | 24.6% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,473 | 16.2% | 6.1% | 10.6% | {"coverage": 1093, "market_freshness/coverage": 218, "market_freshness": 216, "data": 157, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.38 | 0.2195 / 0.2095 (2682) | 37.9% | 15.3% | 4.1% | 22.3% |
| DOUBLES | 2,539 | 46.4% | 46.4% | 6.8% | {"execution": 663, "mapping": 336, "market_freshness": 106, "market_freshness/coverage": 67, "coverage": 7} | 23.22 | 0.2976 / 0.2337 (620) | 9.2% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 22,960 | 24.7% | 17.4% | 32.5% | {"coverage": 1968, "market_freshness": 1111, "execution": 977, "data": 840, "market_freshness/coverage": 568, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.68 | 0.2156 / 0.1983 (4823) | 39.8% | 68.9% | 15.2% | 21.3% |
| ITF_WOMEN | 29,922 | 26.4% | 18.9% | 45.3% | {"coverage": 2775, "market_freshness": 1709, "execution": 1304, "data": 1119, "market_freshness/coverage": 690, "mapping": 193, "model_calibration_or_unknown": 93, "model_calibration": 22} | 12.5 | 0.2031 / 0.1934 (5752) | 40.9% | 57.2% | 9.8% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,799 | 6.0% | 5.1% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2302 / 0.2207 (770) | 29.9% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 12.0h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 725 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 6.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 405 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 194 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 235 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 681 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 271 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.5h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 278 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 11.6h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 700 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9699, "by_level_share_of_ge_25pp": {"ATP": 0.0136, "CHALLENGER": 0.1064, "DOUBLES": 0.0676, "ITF_MEN": 0.3253, "ITF_WOMEN": 0.4531, "OTHER": 0.0007, "WTA": 0.0166, "WTA125": 0.0168}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5335, "share_primary_cause_market_settled_or_in_play": 0.4318, "share_primary_cause_stale_quote_only": 0.195}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17448, "identity_ambiguous_share": 0.2032, "ticker_orientation": {"VERIFIED": 17448}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11479, "with_external": 610, "coverage": 0.0531, "external_status": {"EXTERNAL_STALE": 390, "AGREES_WITH_KALSHI": 207, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 390, "MODEL_LONE_OUTLIER": 207, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3393, "share_external_supports_model": 0.0213}, "pregame_clean_ge_25pp": {"n": 5422, "with_external": 580, "coverage": 0.107, "external_status": {"EXTERNAL_STALE": 367, "AGREES_WITH_KALSHI": 200, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 367, "MODEL_LONE_OUTLIER": 200, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3448, "share_external_supports_model": 0.0224}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2086, "data_status": {"POOR": 9799, "LIMITED": 4537, "ADEQUATE": 3112}, "comparison_lt_10pp": {"median_thinner_serve_points": 1722.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1414, "model_minus_observed": 0.0576, "kalshi_minus_observed": -0.0818, "brier_diff_model_minus_kalshi": 0.0004}, "4-10x": {"n": 968, "model_minus_observed": 0.0888, "kalshi_minus_observed": -0.0558, "brier_diff_model_minus_kalshi": 0.009}, "<2x": {"n": 3436, "model_minus_observed": 0.1005, "kalshi_minus_observed": -0.0226, "brier_diff_model_minus_kalshi": 0.0147}, ">=10x": {"n": 1188, "model_minus_observed": 0.1169, "kalshi_minus_observed": -0.0563, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7006, "model": {"intercept": -0.556, "slope": 0.826, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.187, "slope": 1.078, "slope_se": 0.034}, "mean_extremity_model": 0.1737, "mean_extremity_kalshi": 0.1697, "model_brier": 0.2328, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0296, "brier_diff_se": 0.0023, "model_logloss": 0.6627, "kalshi_logloss": 0.5885}, "fair_v1": {"n": 7006, "model": {"intercept": -0.447, "slope": 1.032, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.255, "slope": 1.107, "slope_se": 0.034}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2143, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6176, "kalshi_logloss": 0.5888}, "gen1_elo": {"n": 7006, "model": {"intercept": -0.435, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.257, "slope": 1.097, "slope_se": 0.034}, "mean_extremity_model": 0.1759, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2136, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0102, "brier_diff_se": 0.0018, "model_logloss": 0.6164, "kalshi_logloss": 0.5889}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2465, "share_ge_15": 0.4427, "median_abs_gap": 13.01, "n": 46567}, "gen1_elo": {"share_ge_25": 0.2433, "share_ge_15": 0.4388, "median_abs_gap": 12.77, "n": 46567}, "gen1_sr": {"share_ge_25": 0.3124, "share_ge_15": 0.5194, "median_abs_gap": 15.77, "n": 46567}, "gen2": {"share_ge_25": 0.3126, "share_ge_15": 0.5093, "median_abs_gap": 15.43, "n": 46567}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1507, "share_ge_15": 0.3532, "median_abs_gap": 10.68, "n": 35971}, "gen1_elo": {"share_ge_25": 0.1484, "share_ge_15": 0.3484, "median_abs_gap": 10.49, "n": 35971}, "gen1_sr": {"share_ge_25": 0.2162, "share_ge_15": 0.4394, "median_abs_gap": 13.0, "n": 35973}, "gen2": {"share_ge_25": 0.2304, "share_ge_15": 0.4385, "median_abs_gap": 12.85, "n": 35973}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0378, "share_ge_25_pregame_clean": 0.0327}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0602, "share_ge_25_pregame_clean": 0.051}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.4394, "share_within_10pp_pregame_clean": 0.4919, "corr_model_vs_mid_pregame_clean": 0.8513}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1005, "model_brier": 0.197, "kalshi_brier": 0.1974, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1216, "model_brier": 0.2186, "kalshi_brier": 0.2091, "brier_diff_model_minus_kalshi": 0.0095}, "15-25": {"n_settled": 1553, "model_brier": 0.2244, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0164}, "25-40": {"n_settled": 892, "model_brier": 0.2228, "kalshi_brier": 0.2039, "brier_diff_model_minus_kalshi": 0.0189}, "3-5": {"n_settled": 646, "model_brier": 0.2049, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": -0.0001}, "40+": {"n_settled": 186, "model_brier": 0.2966, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1217}, "5-10": {"n_settled": 1508, "model_brier": 0.201, "kalshi_brier": 0.2003, "brier_diff_model_minus_kalshi": 0.0007}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.826, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.187, "slope": 1.078, "slope_se": 0.034}, "n": 7006}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.483, "slope": 0.867, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.178, "slope": 1.078, "slope_se": 0.029}, "n": 9246}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 620, "model_brier": 0.2976, "kalshi_brier": 0.2337, "brier_diff_model_minus_kalshi": 0.0639, "brier_diff_se": 0.0118, "corr_model_outcome": 0.0972, "corr_kalshi_outcome": 0.2717}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
