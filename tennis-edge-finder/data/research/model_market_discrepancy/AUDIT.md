# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-08T00:02Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 81,726): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.83 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.9%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,734): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.3%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.4%, POOR_DATA 9.1%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.4%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.6% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.6% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,734 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.2%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 492.0 points vs 1729.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.028, Gen-2 0.823, Gen-1 ledger 0.865 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 904 model 0.2232 vs Kalshi 0.2057; n 188 model 0.2966 vs Kalshi 0.1763.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 346,302 model-market comparisons (567,494 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 115,412 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-07T23:42:12.246281+00:00'], shadow board 93,871 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-07T23:42:16.270478+00:00'], Model 4 42,614 rows, 28,911 settled tickers, 10,824 tickers with an external scan.
* By model: {"gen1_ledger": 77742, "gen1_elo": 47176, "fair_v1": 47176, "gen2": 47176, "gen1_sr": 47176, "model4_fundamental": 39970, "model4_conditioned": 39886}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 81,726 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.83 | 40.8% | 21.7% |
| MW fair_v1 | 47,176 | 12.9 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 10.0 | 13.04 | 44.4% | 24.8% |
| MW gen1_elo | 47,176 | 12.6 | 8.9 | 19.2 | 15.3 | 19.5 | 14.6 | 9.8 | 12.83 | 44.0% | 24.5% |
| MW gen1_ledger | 34,550 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| MW gen1_sr | 47,176 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.6 | 15.82 | 52.0% | 31.3% |
| MW gen2 | 47,176 | 11.0 | 7.6 | 16.6 | 13.7 | 19.6 | 17.7 | 13.7 | 15.46 | 51.0% | 31.4% |
| all families model4_conditioned | 39,886 | 22.2 | 18.0 | 34.1 | 17.1 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.5% |
| all families model4_fundamental | 39,970 | 17.4 | 13.5 | 33.8 | 19.9 | 10.0 | 3.8 | 1.5 | 7.61 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.1%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.0%, >=25pp 17.1%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,965 | 28.5 | 15.7 | 27.4 | 13.5 | 10.7 | 3.6 | 0.6 | 5.77 | 14.9% | 4.2% |
| CHALLENGER | 7,071 | 16.2 | 9.7 | 20.7 | 15.2 | 16.0 | 11.4 | 10.8 | 10.91 | 38.2% | 22.1% |
| ITF_MEN | 13,377 | 9.8 | 7.3 | 17.1 | 15.1 | 21.2 | 17.2 | 12.3 | 15.24 | 50.7% | 29.5% |
| ITF_WOMEN | 18,387 | 9.6 | 7.1 | 16.0 | 14.8 | 22.2 | 18.3 | 12.0 | 15.89 | 52.6% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,043 | 16.8 | 13.2 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.66 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,965 | 26.8 | 15.8 | 26.0 | 15.4 | 11.5 | 3.7 | 0.8 | 6.02 | 16.0% | 4.5% |
| CHALLENGER | 7,071 | 14.7 | 9.1 | 18.9 | 13.8 | 18.6 | 13.4 | 11.4 | 12.47 | 43.5% | 24.9% |
| ITF_MEN | 13,377 | 8.2 | 6.1 | 15.1 | 13.7 | 20.0 | 20.5 | 16.4 | 17.94 | 56.9% | 36.9% |
| ITF_WOMEN | 18,387 | 7.9 | 5.8 | 14.1 | 12.8 | 20.7 | 21.2 | 17.5 | 19.09 | 59.4% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,043 | 14.1 | 10.2 | 21.6 | 16.2 | 22.4 | 12.9 | 2.5 | 11.28 | 37.9% | 15.4% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,965 | 22.9 | 14.2 | 25.3 | 15.6 | 14.8 | 6.1 | 1.2 | 7.1 | 22.1% | 7.2% |
| CHALLENGER | 7,071 | 15.2 | 9.5 | 20.7 | 15.6 | 16.3 | 11.8 | 10.9 | 11.34 | 39.0% | 22.7% |
| ITF_MEN | 13,377 | 9.5 | 7.3 | 17.2 | 14.2 | 21.9 | 17.2 | 12.6 | 15.65 | 51.7% | 29.8% |
| ITF_WOMEN | 18,387 | 9.3 | 6.9 | 16.2 | 15.7 | 22.2 | 18.2 | 11.4 | 15.6 | 51.9% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,043 | 22.8 | 17.1 | 31.8 | 15.3 | 8.7 | 3.3 | 1.1 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,366 | 26.9 | 19.8 | 29.8 | 12.3 | 8.2 | 2.6 | 0.5 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,571 | 22.5 | 14.5 | 27.4 | 14.8 | 13.5 | 5.7 | 1.5 | 7.07 | 20.7% | 7.2% |
| DOUBLES | 2,575 | 4.8 | 4.5 | 12.8 | 11.0 | 20.3 | 24.4 | 22.0 | 23.31 | 66.8% | 46.5% |
| ITF_MEN | 9,905 | 12.9 | 9.6 | 21.5 | 15.7 | 21.6 | 12.9 | 5.8 | 11.75 | 40.3% | 18.7% |
| ITF_WOMEN | 11,940 | 13.4 | 9.2 | 19.9 | 15.6 | 21.5 | 14.9 | 5.5 | 12.24 | 41.8% | 20.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,788 | 23.8 | 16.1 | 31.4 | 16.9 | 9.0 | 2.6 | 0.2 | 6.54 | 11.8% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,846 | 28.9 | 15.9 | 27.8 | 13.4 | 10.4 | 3.2 | 0.3 | 5.64 | 14.0% | 3.5% |
| CHALLENGER | 4,998 | 20.9 | 11.9 | 25.7 | 18.0 | 16.0 | 5.9 | 1.6 | 8.23 | 23.5% | 7.5% |
| ITF_MEN | 9,747 | 12.0 | 8.7 | 20.7 | 17.4 | 22.0 | 14.0 | 5.2 | 12.35 | 41.2% | 19.2% |
| ITF_WOMEN | 13,515 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.1 | 4.9 | 13.19 | 44.1% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,929 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.49 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,846 | 27.1 | 16.2 | 26.3 | 15.3 | 11.4 | 3.4 | 0.4 | 5.96 | 15.1% | 3.7% |
| CHALLENGER | 4,998 | 18.4 | 11.5 | 23.8 | 16.2 | 19.1 | 9.2 | 1.8 | 8.98 | 30.1% | 11.0% |
| ITF_MEN | 9,748 | 9.6 | 7.2 | 17.6 | 16.0 | 21.8 | 18.7 | 9.1 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,516 | 8.9 | 6.9 | 16.1 | 14.4 | 22.6 | 20.4 | 10.7 | 16.49 | 53.8% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,929 | 14.4 | 10.3 | 21.9 | 16.4 | 22.6 | 12.6 | 1.9 | 11.03 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,304 | 27.1 | 20.0 | 29.8 | 12.5 | 7.9 | 2.4 | 0.3 | 5.3 | 10.7% | 2.8% |
| CHALLENGER | 4,039 | 23.8 | 15.4 | 28.6 | 15.0 | 12.8 | 4.0 | 0.4 | 6.59 | 17.2% | 4.4% |
| DOUBLES | 2,413 | 4.7 | 4.6 | 13.1 | 11.1 | 20.1 | 24.4 | 22.1 | 23.23 | 66.6% | 46.4% |
| ITF_MEN | 8,509 | 13.7 | 10.2 | 23.1 | 16.2 | 21.6 | 11.4 | 3.8 | 10.78 | 36.8% | 15.2% |
| ITF_WOMEN | 10,237 | 14.1 | 9.8 | 21.0 | 16.1 | 21.6 | 13.8 | 3.6 | 11.43 | 39.0% | 17.5% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,725 | 24.1 | 16.5 | 31.4 | 16.9 | 9.0 | 2.0 | 0.1 | 6.43 | 11.1% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,575 | 4.8 | 4.5 | 12.8 | 11.0 | 20.3 | 24.4 | 22.0 | 23.31 | 66.8% | 46.5% |
| singles | 31,975 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 176 | 8.0 | 9.1 | 11.4 | 7.4 | 20.4 | 27.8 | 15.9 | 21.18 | 64.2% | 43.8% |
| Clay | 9,725 | 12.7 | 9.1 | 20.0 | 15.5 | 19.6 | 13.9 | 9.2 | 12.6 | 42.7% | 23.1% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,683 | 13.4 | 8.7 | 18.7 | 15.2 | 19.2 | 14.8 | 9.9 | 12.9 | 44.0% | 24.7% |
| UNKNOWN | 6,355 | 10.5 | 7.6 | 17.1 | 16.3 | 21.5 | 16.0 | 11.1 | 14.32 | 48.6% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,418 | 19.6 | 11.9 | 22.4 | 15.9 | 14.9 | 9.2 | 6.3 | 8.89 | 30.3% | 15.5% |
| B | 5,766 | 12.6 | 8.7 | 19.7 | 15.6 | 19.8 | 12.8 | 10.8 | 12.71 | 43.4% | 23.6% |
| C | 6,683 | 12.0 | 8.8 | 19.5 | 15.6 | 18.7 | 14.6 | 10.8 | 13.0 | 44.1% | 25.4% |
| D | 7,658 | 11.7 | 8.3 | 17.9 | 15.3 | 21.7 | 15.7 | 9.4 | 13.85 | 46.8% | 25.1% |
| F | 13,651 | 7.4 | 5.6 | 14.8 | 14.7 | 23.5 | 20.8 | 13.1 | 17.78 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,279 | 24.6 | 16.1 | 29.0 | 15.0 | 10.6 | 3.4 | 1.2 | 6.36 | 15.3% | 4.6% |
| B | 4,834 | 16.6 | 10.8 | 24.2 | 16.8 | 18.9 | 9.6 | 3.0 | 9.67 | 31.5% | 12.7% |
| C | 6,813 | 11.0 | 7.8 | 19.6 | 14.6 | 21.0 | 15.7 | 10.4 | 13.63 | 47.1% | 26.1% |
| D | 5,176 | 14.5 | 10.1 | 21.4 | 15.3 | 20.8 | 12.5 | 5.3 | 11.19 | 38.6% | 17.8% |
| F | 8,448 | 10.2 | 8.3 | 16.2 | 14.6 | 23.4 | 19.5 | 7.8 | 15.34 | 50.7% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,144 | 17.8 | 10.9 | 21.4 | 15.7 | 15.2 | 10.1 | 8.9 | 9.98 | 34.2% | 18.9% |
| LIMITED | 10,333 | 13.6 | 9.7 | 20.4 | 15.8 | 19.5 | 13.3 | 7.7 | 11.89 | 40.4% | 20.9% |
| POOR | 21,699 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.8 | 11.8 | 16.16 | 53.4% | 30.7% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,847 | 23.7 | 17.9 | 33.0 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.8% | 3.4% |
| GAME_SPREAD | 6,651 | 22.7 | 15.4 | 32.1 | 16.8 | 9.0 | 3.4 | 0.7 | 6.69 | 13.0% | 4.0% |
| MATCH_WINNER | 34,550 | 15.8 | 10.9 | 22.2 | 15.1 | 18.5 | 12.0 | 5.5 | 10.26 | 36.0% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,438 | 27.9 | 16.8 | 30.8 | 12.7 | 9.1 | 2.4 | 0.3 | 5.63 | 11.8% | 2.7% |
| TOTAL_GAMES | 11,232 | 9.8 | 10.8 | 35.6 | 25.9 | 10.7 | 4.2 | 2.9 | 9.18 | 17.8% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,130 | 24.5 | 28.8 | 33.2 | 8.2 | 4.0 | 1.1 | 0.3 | 4.79 | 5.4% | 1.4% |
| GAME_SPREAD | 9,186 | 47.0 | 16.1 | 24.7 | 7.4 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,570 | 6.6 | 9.9 | 40.2 | 30.2 | 7.4 | 3.3 | 2.4 | 9.21 | 13.1% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,166 | 23.8 | 16.6 | 34.7 | 14.8 | 6.9 | 2.7 | 0.5 | 6.05 | 10.1% | 3.2% |
| GAME_SPREAD | 9,195 | 20.7 | 13.6 | 28.2 | 20.0 | 11.9 | 4.4 | 1.2 | 7.59 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,609 | 10.1 | 10.8 | 36.3 | 24.2 | 11.5 | 4.5 | 2.6 | 9.04 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 47,176 | 44.4% | 24.8% | 13.04 | 35.3% | 15.0% | 10.67 |
| gen1_elo | 47,176 | 44.0% | 24.5% | 12.83 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 47,176 | 52.0% | 31.3% | 15.82 | 43.9% | 21.5% | 12.98 |
| gen2 | 47,176 | 51.0% | 31.4% | 15.46 | 43.8% | 23.0% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 20,000 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 27,176 | 10.9 | 7.3 | 16.8 | 13.9 | 19.3 | 17.0 | 14.8 | 15.42 | 51.1% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 28,018 | 16.4 | 11.2 | 22.8 | 15.2 | 18.0 | 11.5 | 4.9 | 9.88 | 34.4% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 81,726 | 28018 | 23472 | 30236 | 24.8 | 127.1 | 1451.1 |
| ge_15pp | 33,373 | 9626 | 8361 | 15386 | 28.3 | 435.2 | 1451.1 |
| ge_25pp | 17,734 | 4585 | 3647 | 9502 | 33.1 | 582.0 | 1431.1 |
| lt_10pp | 35,876 | 14126 | 11105 | 10645 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261108T000220Z-b688cae3`: 219 priced rows, quote age at build {'median': 53.7, 'max': 83.7}, freshness {'STALE': 219}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,652 | 19.2 | 10.9 | 25.4 | 17.9 | 18.1 | 7.4 | 1.0 | 8.81 | 26.5% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 988 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,096 | 0.0 | 2.2 | 37.4 | 26.4 | 24.0 | 9.2 | 0.9 | 11.8 | 34.0% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 47,176 | 7844 (16.6%) | 26.7% | 1.0% | {"EXTERNAL_STALE": 4652, "AGREES_WITH_KALSHI": 2096, "ALL_AGREE": 988, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,948 | 1975 (9.4%) | 36.1% | 1.5% | {"EXTERNAL_STALE": 1232, "AGREES_WITH_KALSHI": 713, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,687 | 614 (5.2%) | 34.2% | 2.1% | {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,460 | 584 (10.7%) | 34.8% | 2.2% | {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,981 | 4479 (23.6%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2588, "ALL_AGREE": 988, "AGREES_WITH_KALSHI": 830, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,248 | 10.5 | 7.7 | 19.4 | 14.6 | 21.6 | 16.2 | 9.9 | 14.09 | 47.8% | 26.1% |
| 4-10x | 6,318 | 11.2 | 8.5 | 18.4 | 15.2 | 22.1 | 14.3 | 10.2 | 13.84 | 46.6% | 24.5% |
| <2x | 24,085 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.57 | 39.6% | 22.0% |
| >=10x | 7,525 | 10.4 | 6.5 | 15.0 | 14.4 | 21.7 | 18.9 | 13.2 | 16.42 | 53.8% | 32.1% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,373 | 12.4 | 8.6 | 19.8 | 16.1 | 19.0 | 13.6 | 10.4 | 12.78 | 43.0% | 24.0% |
| 300-1000 | 10,229 | 11.8 | 8.7 | 17.7 | 15.1 | 20.8 | 16.2 | 9.6 | 13.75 | 46.6% | 25.9% |
| <300 | 14,761 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.8 | 13.1 | 17.12 | 56.0% | 32.9% |
| >=3000 | 9,813 | 21.4 | 12.9 | 23.9 | 15.6 | 13.9 | 7.3 | 5.1 | 7.75 | 26.3% | 12.4% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1448 | 0.5483 | 0.4096 | 0.4862 | +0.062 | -0.077 | 0.0014 ± 0.004 |
| ratio 4-10x | 984 | 0.5771 | 0.4326 | 0.4868 | +0.090 | -0.054 | 0.0088 ± 0.0051 |
| ratio <2x | 3545 | 0.5362 | 0.4136 | 0.4367 | +0.100 | -0.023 | 0.0144 ± 0.0024 |
| ratio >=10x | 1208 | 0.5649 | 0.3926 | 0.4462 | +0.119 | -0.054 | 0.0151 ± 0.0051 |
| thinner_sample 1000-3000 | 1989 | 0.5395 | 0.412 | 0.4485 | +0.091 | -0.036 | 0.0112 ± 0.0033 |
| thinner_sample 300-1000 | 1632 | 0.5637 | 0.4237 | 0.4724 | +0.091 | -0.049 | 0.0051 ± 0.0038 |
| thinner_sample <300 | 2313 | 0.5579 | 0.3905 | 0.454 | +0.104 | -0.063 | 0.0132 ± 0.0037 |
| thinner_sample >=3000 | 1251 | 0.5289 | 0.4356 | 0.4452 | +0.084 | -0.010 | 0.0153 ± 0.0032 |
| data_status ADEQUATE | 1999 | 0.5316 | 0.4287 | 0.4397 | +0.092 | -0.011 | 0.0154 ± 0.0027 |
| data_status LIMITED | 1758 | 0.5478 | 0.4152 | 0.4676 | +0.080 | -0.052 | 0.007 ± 0.0036 |
| data_status POOR | 3428 | 0.5599 | 0.4003 | 0.4577 | +0.102 | -0.057 | 0.0108 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1042 | 0.1975 | 0.1978 | -0.0003 ± 0.0005 | 0.5751 | 0.5758 | 0.5021 | 0.4869 | 0.5 | -0.093 ± 0.0146 | -0.0087 (8) |
| 3-5 | 663 | 0.205 | 0.2049 | +0.0001 ± 0.0014 | 0.5948 | 0.5927 | 0.5049 | 0.4651 | 0.4827 | -0.096 ± 0.018 | 0.01 (3) |
| 5-10 | 1547 | 0.2019 | 0.2007 | +0.0012 ± 0.0017 | 0.5902 | 0.585 | 0.5118 | 0.4381 | 0.4648 | -0.091 ± 0.0118 | -0.0143 (7) |
| 10-15 | 1247 | 0.2184 | 0.2092 | +0.0092 ± 0.0032 | 0.6287 | 0.6019 | 0.5231 | 0.3997 | 0.4234 | -0.104 ± 0.0131 | -0.055 (6) |
| 15-25 | 1594 | 0.2259 | 0.208 | +0.0180 ± 0.0045 | 0.647 | 0.5994 | 0.5755 | 0.3809 | 0.4316 | -0.105 ± 0.0115 | -0.0045 (11) |
| 25-40 | 904 | 0.2232 | 0.2057 | +0.0175 ± 0.009 | 0.6365 | 0.5925 | 0.6509 | 0.3412 | 0.4679 | -0.066 ± 0.0139 | -0.06 (2) |
| 40+ | 188 | 0.2966 | 0.1763 | +0.1203 ± 0.0274 | 0.7985 | 0.5258 | 0.7306 | 0.2756 | 0.3777 | -0.082 ± 0.0266 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5436 | 0.1853 | 0.1862 | -0.0009 ± 0.0002 | 0.5467 | 0.5478 | 0.4903 | 0.475 | 0.5074 | -0.020 ± 0.0059 | -0.01 (28) |
| 3-5 | 3624 | 0.1978 | 0.1961 | +0.0017 ± 0.0006 | 0.5762 | 0.5699 | 0.4828 | 0.443 | 0.4412 | -0.056 ± 0.0074 | 0.005 (6) |
| 5-10 | 7854 | 0.2013 | 0.1978 | +0.0035 ± 0.0007 | 0.5885 | 0.5768 | 0.4848 | 0.4111 | 0.4248 | -0.045 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6478 | 0.2021 | 0.1862 | +0.0160 ± 0.0013 | 0.5909 | 0.5461 | 0.4852 | 0.3613 | 0.3592 | -0.063 ± 0.0054 | -0.0379 (19) |
| 15-25 | 8212 | 0.2064 | 0.1669 | +0.0395 ± 0.0018 | 0.6047 | 0.4961 | 0.4995 | 0.304 | 0.3015 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6316 | 0.2229 | 0.1263 | +0.0966 ± 0.0028 | 0.6401 | 0.3882 | 0.5267 | 0.213 | 0.2201 | -0.058 ± 0.0043 | -0.0733 (3) |
| 40+ | 4219 | 0.3831 | 0.0437 | +0.3394 ± 0.0037 | 0.9977 | 0.17 | 0.6309 | 0.1014 | 0.0576 | -0.076 ± 0.003 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 834 | 0.205 | 0.2053 | -0.0003 ± 0.0005 | 0.5907 | 0.5918 | 0.5068 | 0.492 | 0.5132 | -0.103 ± 0.0168 | -0.0117 (6) |
| 3-5 | 594 | 0.2116 | 0.2086 | +0.0029 ± 0.0015 | 0.6062 | 0.5998 | 0.5138 | 0.4743 | 0.4529 | -0.130 ± 0.0201 | 0.01 (3) |
| 5-10 | 1331 | 0.2066 | 0.2047 | +0.0019 ± 0.0019 | 0.5995 | 0.5943 | 0.5405 | 0.466 | 0.4929 | -0.088 ± 0.0128 | -0.01 (4) |
| 10-15 | 1155 | 0.2132 | 0.2071 | +0.0060 ± 0.0034 | 0.6191 | 0.6003 | 0.5625 | 0.4381 | 0.4788 | -0.099 ± 0.014 | -0.04 (5) |
| 15-25 | 1681 | 0.232 | 0.2119 | +0.0201 ± 0.0044 | 0.6597 | 0.6082 | 0.585 | 0.3895 | 0.4372 | -0.100 ± 0.0115 | -0.0183 (12) |
| 25-40 | 1172 | 0.2662 | 0.1982 | +0.0680 ± 0.0082 | 0.7427 | 0.5764 | 0.659 | 0.3448 | 0.3959 | -0.116 ± 0.013 | -0.008 (5) |
| 40+ | 418 | 0.3723 | 0.1623 | +0.2099 ± 0.0197 | 1.0148 | 0.4907 | 0.7352 | 0.2464 | 0.2895 | -0.087 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4651 | 0.192 | 0.1921 | -0.0002 ± 0.0002 | 0.5597 | 0.5598 | 0.5075 | 0.4925 | 0.5074 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3179 | 0.1928 | 0.1917 | +0.0011 ± 0.0006 | 0.5624 | 0.5588 | 0.5117 | 0.4721 | 0.4769 | -0.047 ± 0.008 | 0.01 (5) |
| 5-10 | 7005 | 0.197 | 0.1936 | +0.0034 ± 0.0008 | 0.579 | 0.5666 | 0.5091 | 0.435 | 0.4515 | -0.040 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5813 | 0.2029 | 0.1918 | +0.0111 ± 0.0014 | 0.5953 | 0.5607 | 0.5105 | 0.3866 | 0.4044 | -0.047 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8269 | 0.2172 | 0.1814 | +0.0358 ± 0.0018 | 0.6315 | 0.532 | 0.5255 | 0.3299 | 0.3386 | -0.060 ± 0.0047 | -0.014 (52) |
| 25-40 | 7424 | 0.2507 | 0.1376 | +0.1131 ± 0.0027 | 0.7083 | 0.4204 | 0.56 | 0.243 | 0.2267 | -0.079 ± 0.0043 | -0.0095 (20) |
| 40+ | 5798 | 0.4018 | 0.0582 | +0.3436 ± 0.0037 | 1.059 | 0.2106 | 0.6542 | 0.1182 | 0.0792 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1016 | 0.1957 | 0.1971 | -0.0014 ± 0.0005 | 0.5712 | 0.5746 | 0.5027 | 0.4873 | 0.5325 | -0.051 ± 0.0145 | -0.0191 (11) |
| 3-5 | 714 | 0.2071 | 0.2056 | +0.0015 ± 0.0014 | 0.6006 | 0.5953 | 0.4976 | 0.4581 | 0.4608 | -0.110 ± 0.0177 | 0.002 (5) |
| 5-10 | 1578 | 0.2026 | 0.199 | +0.0036 ± 0.0017 | 0.5903 | 0.5802 | 0.5124 | 0.4387 | 0.4506 | -0.104 ± 0.0116 | -0.01 (10) |
| 10-15 | 1262 | 0.2114 | 0.2023 | +0.0091 ± 0.0031 | 0.6133 | 0.5871 | 0.5369 | 0.4136 | 0.4406 | -0.106 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1525 | 0.2321 | 0.2126 | +0.0195 ± 0.0046 | 0.6618 | 0.6095 | 0.5858 | 0.3917 | 0.438 | -0.109 ± 0.0118 | -0.03 (1) |
| 25-40 | 893 | 0.2127 | 0.21 | +0.0027 ± 0.009 | 0.6142 | 0.6023 | 0.6589 | 0.348 | 0.4972 | -0.053 ± 0.0139 | -0.0267 (3) |
| 40+ | 197 | 0.3098 | 0.1837 | +0.1261 ± 0.0274 | 0.8383 | 0.5418 | 0.7423 | 0.2875 | 0.3858 | -0.086 ± 0.0281 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5237 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.5463 | 0.5471 | 0.486 | 0.4707 | 0.4904 | -0.032 ± 0.006 | -0.0189 (44) |
| 3-5 | 3742 | 0.2038 | 0.202 | +0.0018 ± 0.0006 | 0.5926 | 0.5865 | 0.4797 | 0.4402 | 0.4383 | -0.056 ± 0.0075 | -0.0073 (22) |
| 5-10 | 7997 | 0.196 | 0.1907 | +0.0052 ± 0.0007 | 0.5752 | 0.5589 | 0.4875 | 0.4135 | 0.4154 | -0.056 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6432 | 0.1938 | 0.1787 | +0.0152 ± 0.0013 | 0.5725 | 0.5287 | 0.4946 | 0.3713 | 0.3714 | -0.062 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8297 | 0.2124 | 0.1726 | +0.0398 ± 0.0018 | 0.6188 | 0.5089 | 0.5125 | 0.318 | 0.3137 | -0.071 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6262 | 0.2167 | 0.1273 | +0.0894 ± 0.0028 | 0.6267 | 0.3898 | 0.5289 | 0.2133 | 0.2316 | -0.048 ± 0.0044 | -0.02 (4) |
| 40+ | 4172 | 0.3919 | 0.0487 | +0.3432 ± 0.0039 | 1.0213 | 0.1826 | 0.64 | 0.1076 | 0.0645 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1450 | 0.1976 | 0.1976 | -0.0000 ± 0.0004 | 0.5736 | 0.5735 | 0.5079 | 0.4929 | 0.4972 | -0.068 ± 0.0119 | -0.0221 (56) |
| 3-5 | 1043 | 0.1881 | 0.1881 | +0.0000 ± 0.0011 | 0.5542 | 0.5524 | 0.4971 | 0.4572 | 0.4756 | -0.055 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2098 | 0.1996 | 0.1948 | +0.0048 ± 0.0015 | 0.5891 | 0.573 | 0.5076 | 0.434 | 0.439 | -0.076 ± 0.0099 | -0.005 (78) |
| 10-15 | 1448 | 0.2144 | 0.2019 | +0.0125 ± 0.0029 | 0.6223 | 0.5873 | 0.5424 | 0.4195 | 0.4289 | -0.089 ± 0.0121 | 0.0012 (66) |
| 15-25 | 1878 | 0.2313 | 0.2073 | +0.0240 ± 0.0041 | 0.6599 | 0.5984 | 0.591 | 0.3961 | 0.434 | -0.089 ± 0.0106 | -0.0214 (59) |
| 25-40 | 1130 | 0.2403 | 0.2106 | +0.0298 ± 0.0083 | 0.6863 | 0.6041 | 0.6887 | 0.3766 | 0.485 | -0.086 ± 0.0129 | -0.0252 (27) |
| 40+ | 401 | 0.3291 | 0.2007 | +0.1285 ± 0.0214 | 0.9466 | 0.5849 | 0.8159 | 0.3396 | 0.4589 | -0.099 ± 0.02 | -0.1137 (8) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5340 | 0.1778 | 0.178 | -0.0001 ± 0.0002 | 0.5261 | 0.5259 | 0.5112 | 0.4959 | 0.5054 | -0.039 ± 0.0058 | -0.0154 (103) |
| 3-5 | 3700 | 0.1948 | 0.1941 | +0.0007 ± 0.0006 | 0.5686 | 0.5663 | 0.5014 | 0.4617 | 0.473 | -0.039 ± 0.0073 | -0.0212 (73) |
| 5-10 | 7510 | 0.1963 | 0.1899 | +0.0064 ± 0.0008 | 0.5799 | 0.56 | 0.5015 | 0.4279 | 0.4222 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5142 | 0.2099 | 0.1935 | +0.0163 ± 0.0015 | 0.611 | 0.5677 | 0.5373 | 0.4143 | 0.408 | -0.072 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6249 | 0.2317 | 0.1999 | +0.0318 ± 0.0022 | 0.6654 | 0.5791 | 0.5766 | 0.3813 | 0.3985 | -0.068 ± 0.0057 | -0.026 (108) |
| 25-40 | 4077 | 0.2571 | 0.1906 | +0.0664 ± 0.0043 | 0.7274 | 0.5549 | 0.6406 | 0.3281 | 0.3809 | -0.065 ± 0.0067 | -0.0277 (53) |
| 40+ | 1800 | 0.3721 | 0.1589 | +0.2133 ± 0.0097 | 1.0499 | 0.4736 | 0.7448 | 0.2437 | 0.2917 | -0.065 ± 0.009 | -0.054 (15) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7185 | 1.028 ± 0.033 | 1.099 | 0.1689 | 0.1688 | 0.2149 | 0.2037 |
| gen2 | 7185 | 0.823 ± 0.03 | 1.071 | 0.1733 | 0.1691 | 0.2332 | 0.2036 |
| gen1_elo | 7185 | 1.009 ± 0.032 | 1.09 | 0.1753 | 0.1689 | 0.2141 | 0.2038 |
| gen1_sr | 7185 | 1.008 ± 0.039 | 1.128 | 0.1334 | 0.1708 | 0.2293 | 0.2033 |
| gen1_ledger | 9448 | 0.865 ± 0.024 | 1.077 | 0.1896 | 0.1757 | 0.217 | 0.2002 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,373)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,706 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,582 | 22.7% |
| BOOK_QUALITY | execution | 5,967 | 17.9% |
| POOR_DATA | data | 3,847 | 11.5% |
| LIMITED_DATA | data | 2,076 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,928 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,392 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,370 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 954 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 550 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.7%, execution 17.9%, data 17.8%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 46.1%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.0%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.2%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,734)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,077 | 34.3% |
| STALE_QUOTE | market_freshness | 3,433 | 19.4% |
| BOOK_QUALITY | execution | 3,095 | 17.4% |
| POOR_DATA | data | 1,619 | 9.1% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,027 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 773 | 4.4% |
| IN_PLAY_QUOTE | market_freshness/coverage | 625 | 3.5% |
| LIMITED_DATA | data | 610 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 339 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 135 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.3%, market_freshness 19.4%, execution 17.4%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.4%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 61.6%, STALE_KALSHI_QUOTE 53.6%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.8%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.3%, POST_SETTLEMENT_OBSERVATION 34.3%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14148, "IDENTITY_AMBIGUOUS": 3586}; ticker orientation: {"VERIFIED": 17734}.

Checks: discipline:AMBIGUOUS 1196, discipline:PASS 16538, identity_confidence:AMBIGUOUS 3255, identity_confidence:PASS 14479, level_mapping:NA 1208, level_mapping:PASS 16526, market_pair:AMBIGUOUS 492, market_pair:NA 396, market_pair:PASS 16846, model_complement:NA 358, model_complement:PASS 17376, namesake:AMBIGUOUS 6, namesake:PASS 17728, physical_match_id:NA 6047, physical_match_id:PASS 11687, player_ids:PASS 17734, same_pair_other_event:PASS 17734, ticker_orientation:PASS 17734

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,331 | 3.8% | 3.2% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 19} | 5.52 | 0.2235 / 0.2186 (817) | 24.8% | 2.5% | 3.1% | 2.9% |
| CHALLENGER | 11,642 | 16.3% | 6.1% | 10.7% | {"coverage": 1124, "market_freshness/coverage": 220, "market_freshness": 219, "data": 158, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.36 | 0.2201 / 0.2098 (2748) | 37.9% | 15.1% | 4.1% | 22.4% |
| DOUBLES | 2,575 | 46.5% | 46.4% | 6.7% | {"execution": 665, "mapping": 349, "market_freshness": 106, "market_freshness/coverage": 69, "coverage": 7} | 23.23 | 0.298 / 0.2322 (644) | 9.1% | 0.0% | 100.0% | 6.3% |
| ITF_MEN | 23,282 | 24.9% | 17.3% | 32.7% | {"coverage": 2043, "market_freshness": 1119, "execution": 980, "data": 848, "market_freshness/coverage": 589, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 5} | 11.63 | 0.2175 / 0.1996 (4954) | 40.0% | 68.7% | 15.1% | 21.6% |
| ITF_WOMEN | 30,327 | 26.4% | 18.9% | 45.2% | {"coverage": 2827, "market_freshness": 1728, "execution": 1326, "data": 1122, "market_freshness/coverage": 698, "mapping": 197, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.51 | 0.2028 / 0.1937 (5866) | 41.1% | 57.1% | 9.9% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,831 | 6.0% | 5.1% | 1.6% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2296 / 0.2199 (792) | 29.9% | 2.0% | 1.3% | 3.7% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 519 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 164 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 409 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 454 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
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
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.8h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 9.9h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 603 min (STALE); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 248 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 77 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9701, "by_level_share_of_ge_25pp": {"ATP": 0.0135, "CHALLENGER": 0.1068, "DOUBLES": 0.0674, "ITF_MEN": 0.3267, "ITF_WOMEN": 0.452, "OTHER": 0.0007, "WTA": 0.0164, "WTA125": 0.0165}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5358, "share_primary_cause_market_settled_or_in_play": 0.4358, "share_primary_cause_stale_quote_only": 0.1936}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17734, "identity_ambiguous_share": 0.2022, "ticker_orientation": {"VERIFIED": 17734}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11687, "with_external": 614, "coverage": 0.0525, "external_status": {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 391, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.342, "share_external_supports_model": 0.0212}, "pregame_clean_ge_25pp": {"n": 5460, "with_external": 584, "coverage": 0.107, "external_status": {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 368, "MODEL_LONE_OUTLIER": 203, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3476, "share_external_supports_model": 0.0223}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 492.0, "median_sample_ratio": 2.45, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2088, "data_status": {"POOR": 9916, "LIMITED": 4612, "ADEQUATE": 3206}, "comparison_lt_10pp": {"median_thinner_serve_points": 1729.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1448, "model_minus_observed": 0.0621, "kalshi_minus_observed": -0.0766, "brier_diff_model_minus_kalshi": 0.0014}, "4-10x": {"n": 984, "model_minus_observed": 0.0903, "kalshi_minus_observed": -0.0542, "brier_diff_model_minus_kalshi": 0.0088}, "<2x": {"n": 3545, "model_minus_observed": 0.0996, "kalshi_minus_observed": -0.0231, "brier_diff_model_minus_kalshi": 0.0144}, ">=10x": {"n": 1208, "model_minus_observed": 0.1187, "kalshi_minus_observed": -0.0536, "brier_diff_model_minus_kalshi": 0.0151}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7185, "model": {"intercept": -0.557, "slope": 0.823, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.178, "slope": 1.071, "slope_se": 0.033}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1691, "model_brier": 0.2332, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0295, "brier_diff_se": 0.0022, "model_logloss": 0.6638, "kalshi_logloss": 0.5897}, "fair_v1": {"n": 7185, "model": {"intercept": -0.451, "slope": 1.028, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.243, "slope": 1.099, "slope_se": 0.034}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.1688, "model_brier": 0.2149, "kalshi_brier": 0.2037, "brier_diff_model_minus_kalshi": 0.0112, "brier_diff_se": 0.0018, "model_logloss": 0.619, "kalshi_logloss": 0.5899}, "gen1_elo": {"n": 7185, "model": {"intercept": -0.44, "slope": 1.009, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.245, "slope": 1.09, "slope_se": 0.033}, "mean_extremity_model": 0.1753, "mean_extremity_kalshi": 0.1689, "model_brier": 0.2141, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0103, "brier_diff_se": 0.0018, "model_logloss": 0.6176, "kalshi_logloss": 0.59}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2477, "share_ge_15": 0.444, "median_abs_gap": 13.04, "n": 47176}, "gen1_elo": {"share_ge_25": 0.2448, "share_ge_15": 0.4401, "median_abs_gap": 12.83, "n": 47176}, "gen1_sr": {"share_ge_25": 0.3132, "share_ge_15": 0.5201, "median_abs_gap": 15.82, "n": 47176}, "gen2": {"share_ge_25": 0.3139, "share_ge_15": 0.5103, "median_abs_gap": 15.46, "n": 47176}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1503, "share_ge_15": 0.353, "median_abs_gap": 10.67, "n": 36319}, "gen1_elo": {"share_ge_25": 0.1482, "share_ge_15": 0.3482, "median_abs_gap": 10.49, "n": 36319}, "gen1_sr": {"share_ge_25": 0.2154, "share_ge_15": 0.4388, "median_abs_gap": 12.98, "n": 36321}, "gen2": {"share_ge_25": 0.2304, "share_ge_15": 0.4382, "median_abs_gap": 12.83, "n": 36321}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0378, "share_ge_25_pregame_clean": 0.0324}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0602, "share_ge_25_pregame_clean": 0.0511}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.439, "share_within_10pp_pregame_clean": 0.4922, "corr_model_vs_mid_pregame_clean": 0.8511}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1042, "model_brier": 0.1975, "kalshi_brier": 0.1978, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1247, "model_brier": 0.2184, "kalshi_brier": 0.2092, "brier_diff_model_minus_kalshi": 0.0092}, "15-25": {"n_settled": 1594, "model_brier": 0.2259, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.018}, "25-40": {"n_settled": 904, "model_brier": 0.2232, "kalshi_brier": 0.2057, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 663, "model_brier": 0.205, "kalshi_brier": 0.2049, "brier_diff_model_minus_kalshi": 0.0001}, "40+": {"n_settled": 188, "model_brier": 0.2966, "kalshi_brier": 0.1763, "brier_diff_model_minus_kalshi": 0.1203}, "5-10": {"n_settled": 1547, "model_brier": 0.2019, "kalshi_brier": 0.2007, "brier_diff_model_minus_kalshi": 0.0012}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.557, "slope": 0.823, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.178, "slope": 1.071, "slope_se": 0.033}, "n": 7185}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.865, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.172, "slope": 1.077, "slope_se": 0.028}, "n": 9448}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 644, "model_brier": 0.298, "kalshi_brier": 0.2322, "brier_diff_model_minus_kalshi": 0.0658, "brier_diff_se": 0.0115, "corr_model_outcome": 0.1011, "corr_kalshi_outcome": 0.2821}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
