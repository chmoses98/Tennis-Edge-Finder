# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-06T19:57Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 80,996): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.81 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.8%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,530): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.1%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.5%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.5%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.1%, market_freshness 19.4%, execution 17.5%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.4% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,530 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1724.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.031, Gen-2 0.824, Gen-1 ledger 0.868 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 899 model 0.2226 vs Kalshi 0.2053; n 186 model 0.2966 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 343,509 model-market comparisons (562,740 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 114,414 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-06T19:42:51.321733+00:00'], shadow board 93,037 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-06T19:42:54.505632+00:00'], Model 4 42,393 rows, 28,581 settled tickers, 10,740 tickers with an external scan.
* By model: {"gen1_ledger": 77056, "gen1_elo": 46755, "fair_v1": 46755, "gen2": 46755, "gen1_sr": 46755, "model4_fundamental": 39758, "model4_conditioned": 39675}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 80,996 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.0 | 11.81 | 40.8% | 21.6% |
| MW fair_v1 | 46,755 | 12.9 | 8.7 | 18.8 | 15.4 | 19.6 | 14.8 | 9.9 | 13.02 | 44.3% | 24.7% |
| MW gen1_elo | 46,755 | 12.6 | 8.8 | 19.3 | 15.4 | 19.6 | 14.6 | 9.8 | 12.8 | 43.9% | 24.4% |
| MW gen1_ledger | 34,241 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| MW gen1_sr | 46,755 | 10.1 | 7.3 | 16.7 | 14.0 | 20.7 | 18.7 | 12.6 | 15.78 | 52.0% | 31.3% |
| MW gen2 | 46,755 | 11.0 | 7.6 | 16.7 | 13.8 | 19.7 | 17.7 | 13.6 | 15.44 | 51.0% | 31.3% |
| all families model4_conditioned | 39,675 | 22.2 | 18.0 | 34.1 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,758 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.38pp; >=10pp 45.0%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,935 | 28.6 | 15.6 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.8% | 4.2% |
| CHALLENGER | 7,005 | 16.2 | 9.8 | 20.7 | 15.3 | 16.1 | 11.3 | 10.7 | 10.91 | 38.1% | 22.0% |
| ITF_MEN | 13,245 | 9.8 | 7.3 | 17.1 | 15.2 | 21.3 | 17.2 | 12.1 | 15.21 | 50.6% | 29.3% |
| ITF_WOMEN | 18,206 | 9.6 | 7.1 | 16.1 | 14.8 | 22.1 | 18.3 | 12.1 | 15.82 | 52.5% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,031 | 16.8 | 13.2 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.6% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,935 | 26.9 | 15.8 | 26.1 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.8% | 4.5% |
| CHALLENGER | 7,005 | 14.7 | 9.1 | 18.9 | 13.9 | 18.6 | 13.4 | 11.3 | 12.47 | 43.4% | 24.8% |
| ITF_MEN | 13,245 | 8.2 | 6.1 | 15.1 | 13.8 | 20.0 | 20.5 | 16.3 | 17.91 | 56.8% | 36.8% |
| ITF_WOMEN | 18,206 | 7.8 | 5.8 | 14.1 | 12.8 | 20.8 | 21.1 | 17.5 | 19.09 | 59.4% | 38.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,031 | 14.1 | 10.2 | 21.7 | 16.1 | 22.4 | 12.9 | 2.5 | 11.28 | 37.9% | 15.5% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,935 | 22.9 | 14.0 | 25.3 | 15.6 | 14.9 | 6.1 | 1.2 | 7.15 | 22.2% | 7.3% |
| CHALLENGER | 7,005 | 15.2 | 9.5 | 20.8 | 15.7 | 16.2 | 11.8 | 10.8 | 11.3 | 38.8% | 22.6% |
| ITF_MEN | 13,245 | 9.5 | 7.3 | 17.3 | 14.2 | 22.0 | 17.2 | 12.5 | 15.61 | 51.7% | 29.7% |
| ITF_WOMEN | 18,206 | 9.3 | 6.9 | 16.3 | 15.7 | 22.2 | 18.2 | 11.4 | 15.57 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,031 | 22.7 | 17.1 | 31.9 | 15.2 | 8.7 | 3.3 | 1.1 | 6.12 | 13.1% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,336 | 26.8 | 19.8 | 30.0 | 12.2 | 8.2 | 2.6 | 0.4 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,530 | 22.4 | 14.6 | 27.6 | 14.9 | 13.4 | 5.7 | 1.6 | 7.08 | 20.6% | 7.2% |
| DOUBLES | 2,547 | 4.9 | 4.5 | 13.0 | 11.1 | 20.1 | 24.5 | 22.0 | 23.31 | 66.6% | 46.5% |
| ITF_MEN | 9,825 | 12.9 | 9.6 | 21.4 | 15.7 | 21.7 | 12.9 | 5.8 | 11.77 | 40.3% | 18.7% |
| ITF_WOMEN | 11,823 | 13.4 | 9.3 | 20.0 | 15.7 | 21.4 | 14.9 | 5.4 | 12.22 | 41.7% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,775 | 23.8 | 16.0 | 31.3 | 17.0 | 9.1 | 2.6 | 0.2 | 6.57 | 11.9% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,820 | 29.0 | 15.8 | 28.0 | 13.3 | 10.3 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,961 | 20.8 | 12.0 | 25.6 | 18.0 | 16.0 | 5.9 | 1.6 | 8.23 | 23.5% | 7.5% |
| ITF_MEN | 9,674 | 12.0 | 8.6 | 20.7 | 17.4 | 22.1 | 14.0 | 5.2 | 12.39 | 41.3% | 19.2% |
| ITF_WOMEN | 13,401 | 11.4 | 8.6 | 18.9 | 17.1 | 24.0 | 15.1 | 4.9 | 13.16 | 44.0% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,918 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.51 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,820 | 27.2 | 16.2 | 26.3 | 15.3 | 11.3 | 3.3 | 0.4 | 5.95 | 15.0% | 3.7% |
| CHALLENGER | 4,961 | 18.4 | 11.4 | 23.8 | 16.2 | 19.1 | 9.2 | 1.9 | 8.99 | 30.1% | 11.1% |
| ITF_MEN | 9,675 | 9.7 | 7.2 | 17.6 | 16.0 | 21.8 | 18.7 | 9.1 | 14.87 | 49.5% | 27.8% |
| ITF_WOMEN | 13,402 | 8.8 | 6.9 | 16.1 | 14.4 | 22.7 | 20.4 | 10.7 | 16.5 | 53.8% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,918 | 14.3 | 10.3 | 21.9 | 16.3 | 22.6 | 12.6 | 1.9 | 11.03 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,279 | 27.0 | 20.0 | 29.9 | 12.4 | 7.9 | 2.5 | 0.3 | 5.3 | 10.7% | 2.8% |
| CHALLENGER | 4,005 | 23.8 | 15.5 | 28.6 | 15.0 | 12.7 | 4.0 | 0.4 | 6.6 | 17.1% | 4.4% |
| DOUBLES | 2,391 | 4.8 | 4.6 | 13.2 | 11.1 | 19.9 | 24.4 | 22.0 | 23.23 | 66.4% | 46.4% |
| ITF_MEN | 8,441 | 13.7 | 10.2 | 23.0 | 16.2 | 21.7 | 11.4 | 3.8 | 10.83 | 36.8% | 15.2% |
| ITF_WOMEN | 10,125 | 14.0 | 9.8 | 21.1 | 16.2 | 21.5 | 13.8 | 3.5 | 11.41 | 38.9% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,713 | 24.2 | 16.4 | 31.4 | 16.9 | 9.1 | 2.0 | 0.1 | 6.43 | 11.2% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,547 | 4.9 | 4.5 | 13.0 | 11.1 | 20.1 | 24.5 | 22.0 | 23.31 | 66.6% | 46.5% |
| singles | 31,694 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 165 | 7.9 | 9.1 | 12.1 | 7.9 | 19.4 | 29.1 | 14.6 | 21.33 | 63.0% | 43.6% |
| Clay | 9,604 | 12.8 | 9.1 | 19.9 | 15.6 | 19.7 | 13.8 | 9.1 | 12.59 | 42.6% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,434 | 13.4 | 8.7 | 18.8 | 15.2 | 19.2 | 14.8 | 9.9 | 12.86 | 43.9% | 24.7% |
| UNKNOWN | 6,315 | 10.6 | 7.6 | 17.0 | 16.3 | 21.5 | 16.0 | 11.0 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,266 | 19.6 | 11.9 | 22.4 | 15.8 | 14.9 | 9.2 | 6.2 | 8.88 | 30.3% | 15.4% |
| B | 5,715 | 12.7 | 8.7 | 19.7 | 15.7 | 19.7 | 12.7 | 10.7 | 12.64 | 43.2% | 23.4% |
| C | 6,628 | 12.0 | 8.9 | 19.5 | 15.7 | 18.6 | 14.6 | 10.6 | 12.91 | 43.8% | 25.3% |
| D | 7,599 | 11.7 | 8.3 | 17.9 | 15.4 | 21.7 | 15.7 | 9.4 | 13.83 | 46.7% | 25.1% |
| F | 13,547 | 7.4 | 5.6 | 14.8 | 14.7 | 23.6 | 20.8 | 13.1 | 17.74 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,164 | 24.5 | 16.1 | 29.2 | 15.0 | 10.6 | 3.4 | 1.2 | 6.37 | 15.2% | 4.6% |
| B | 4,805 | 16.6 | 10.8 | 24.2 | 16.9 | 18.8 | 9.6 | 3.1 | 9.68 | 31.5% | 12.7% |
| C | 6,759 | 11.1 | 7.8 | 19.6 | 14.7 | 20.9 | 15.6 | 10.4 | 13.56 | 46.9% | 26.0% |
| D | 5,137 | 14.5 | 10.1 | 21.4 | 15.3 | 20.8 | 12.5 | 5.3 | 11.19 | 38.6% | 17.8% |
| F | 8,376 | 10.2 | 8.4 | 16.2 | 14.6 | 23.4 | 19.5 | 7.8 | 15.33 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,984 | 17.8 | 10.9 | 21.5 | 15.7 | 15.3 | 10.0 | 8.8 | 9.96 | 34.1% | 18.8% |
| LIMITED | 10,235 | 13.7 | 9.8 | 20.4 | 15.9 | 19.3 | 13.3 | 7.6 | 11.83 | 40.2% | 20.9% |
| POOR | 21,536 | 9.0 | 6.6 | 16.0 | 15.0 | 22.8 | 18.8 | 11.8 | 16.14 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,730 | 23.8 | 17.9 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.9 | 9.7% | 3.3% |
| GAME_SPREAD | 6,621 | 22.6 | 15.4 | 32.1 | 16.9 | 9.0 | 3.4 | 0.7 | 6.71 | 13.0% | 4.1% |
| MATCH_WINNER | 34,241 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,268 | 27.9 | 16.7 | 30.8 | 12.7 | 9.2 | 2.4 | 0.3 | 5.64 | 11.9% | 2.7% |
| TOTAL_GAMES | 11,172 | 9.8 | 10.8 | 35.6 | 26.0 | 10.7 | 4.2 | 2.9 | 9.2 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,012 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,156 | 47.0 | 16.1 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,507 | 6.6 | 9.8 | 40.2 | 30.2 | 7.5 | 3.3 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,047 | 23.9 | 16.7 | 34.8 | 14.6 | 6.9 | 2.6 | 0.5 | 6.04 | 10.0% | 3.1% |
| GAME_SPREAD | 9,165 | 20.6 | 13.6 | 28.2 | 20.0 | 11.9 | 4.4 | 1.2 | 7.6 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,546 | 10.0 | 10.8 | 36.2 | 24.3 | 11.6 | 4.5 | 2.6 | 9.06 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 46,755 | 44.3% | 24.7% | 13.02 | 35.3% | 15.0% | 10.67 |
| gen1_elo | 46,755 | 43.9% | 24.4% | 12.8 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 46,755 | 52.0% | 31.3% | 15.78 | 43.9% | 21.6% | 12.98 |
| gen2 | 46,755 | 51.0% | 31.3% | 15.44 | 43.8% | 23.0% | 12.84 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,974 | 15.6 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,781 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 16.9 | 14.8 | 15.39 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,709 | 16.3 | 11.3 | 22.8 | 15.3 | 18.0 | 11.5 | 4.8 | 9.87 | 34.3% | 16.3% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 80,996 | 27709 | 23446 | 29841 | 24.8 | 125.6 | 1451.1 |
| ge_15pp | 33,020 | 9500 | 8353 | 15167 | 28.1 | 431.5 | 1451.1 |
| ge_25pp | 17,530 | 4524 | 3645 | 9361 | 33.1 | 579.6 | 1431.1 |
| lt_10pp | 35,584 | 13977 | 11092 | 10515 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261106T195738Z-b84b2fbd`: 131 priced rows, quote age at build {'median': 15.0, 'max': 15.1}, freshness {'AGING': 131}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,630 | 19.3 | 10.9 | 25.4 | 17.8 | 18.1 | 7.5 | 1.0 | 8.8 | 26.5% | 8.5% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 972 | 66.7 | 33.3 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,079 | 0.0 | 2.3 | 37.4 | 26.3 | 24.1 | 9.1 | 0.9 | 11.77 | 34.1% | 10.0% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 46,755 | 7789 (16.7%) | 26.7% | 1.0% | {"EXTERNAL_STALE": 4630, "AGREES_WITH_KALSHI": 2079, "ALL_AGREE": 972, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,721 | 1968 (9.5%) | 36.0% | 1.5% | {"EXTERNAL_STALE": 1229, "AGREES_WITH_KALSHI": 709, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,544 | 613 (5.3%) | 33.9% | 2.1% | {"EXTERNAL_STALE": 392, "AGREES_WITH_KALSHI": 208, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,429 | 583 (10.7%) | 34.5% | 2.2% | {"EXTERNAL_STALE": 369, "AGREES_WITH_KALSHI": 201, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,838 | 4445 (23.6%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2576, "ALL_AGREE": 972, "AGREES_WITH_KALSHI": 824, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,176 | 10.5 | 7.7 | 19.5 | 14.7 | 21.6 | 16.2 | 9.8 | 14.05 | 47.7% | 26.1% |
| 4-10x | 6,270 | 11.3 | 8.5 | 18.4 | 15.2 | 22.1 | 14.3 | 10.2 | 13.76 | 46.5% | 24.4% |
| <2x | 23,851 | 15.0 | 9.8 | 19.8 | 16.0 | 17.6 | 13.1 | 8.8 | 11.55 | 39.5% | 21.9% |
| >=10x | 7,458 | 10.4 | 6.4 | 15.0 | 14.4 | 21.8 | 18.9 | 13.1 | 16.37 | 53.7% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,259 | 12.4 | 8.7 | 19.9 | 16.2 | 19.0 | 13.5 | 10.3 | 12.69 | 42.9% | 23.8% |
| 300-1000 | 10,139 | 11.8 | 8.8 | 17.7 | 15.2 | 20.7 | 16.3 | 9.5 | 13.72 | 46.5% | 25.8% |
| <300 | 14,655 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.8 | 13.1 | 17.11 | 56.0% | 32.9% |
| >=3000 | 9,702 | 21.4 | 12.8 | 23.9 | 15.6 | 13.9 | 7.3 | 5.0 | 7.75 | 26.2% | 12.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1436 | 0.5479 | 0.409 | 0.4861 | +0.062 | -0.077 | 0.0013 ± 0.004 |
| ratio 4-10x | 976 | 0.5767 | 0.432 | 0.4887 | +0.088 | -0.057 | 0.0084 ± 0.0051 |
| ratio <2x | 3482 | 0.5365 | 0.4137 | 0.438 | +0.099 | -0.024 | 0.0144 ± 0.0024 |
| ratio >=10x | 1200 | 0.5641 | 0.3914 | 0.4483 | +0.116 | -0.057 | 0.0146 ± 0.0052 |
| thinner_sample 1000-3000 | 1966 | 0.539 | 0.4119 | 0.4481 | +0.091 | -0.036 | 0.0114 ± 0.0033 |
| thinner_sample 300-1000 | 1616 | 0.5637 | 0.4234 | 0.474 | +0.090 | -0.051 | 0.0048 ± 0.0039 |
| thinner_sample <300 | 2300 | 0.5574 | 0.3898 | 0.4552 | +0.102 | -0.065 | 0.013 ± 0.0037 |
| thinner_sample >=3000 | 1212 | 0.5297 | 0.4359 | 0.4488 | +0.081 | -0.013 | 0.0147 ± 0.0033 |
| data_status ADEQUATE | 1958 | 0.5324 | 0.4291 | 0.4423 | +0.090 | -0.013 | 0.0151 ± 0.0028 |
| data_status LIMITED | 1732 | 0.5471 | 0.4148 | 0.4671 | +0.080 | -0.052 | 0.0071 ± 0.0036 |
| data_status POOR | 3404 | 0.5596 | 0.3997 | 0.4592 | +0.100 | -0.059 | 0.0106 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1021 | 0.1973 | 0.1977 | -0.0004 ± 0.0005 | 0.5743 | 0.5752 | 0.5027 | 0.4876 | 0.5024 | -0.093 ± 0.0147 | -0.0087 (8) |
| 3-5 | 657 | 0.2039 | 0.2041 | -0.0001 ± 0.0014 | 0.5917 | 0.5906 | 0.5031 | 0.4633 | 0.484 | -0.093 ± 0.0181 | 0.01 (2) |
| 5-10 | 1527 | 0.201 | 0.2002 | +0.0008 ± 0.0017 | 0.5881 | 0.5838 | 0.5114 | 0.4376 | 0.4669 | -0.090 ± 0.0119 | -0.0143 (7) |
| 10-15 | 1229 | 0.2187 | 0.2096 | +0.0091 ± 0.0032 | 0.6294 | 0.6025 | 0.5234 | 0.3999 | 0.4239 | -0.105 ± 0.0133 | -0.048 (5) |
| 15-25 | 1575 | 0.2253 | 0.2077 | +0.0175 ± 0.0045 | 0.6457 | 0.5989 | 0.5753 | 0.3807 | 0.433 | -0.104 ± 0.0115 | -0.0045 (11) |
| 25-40 | 899 | 0.2226 | 0.2053 | +0.0173 ± 0.009 | 0.6351 | 0.5916 | 0.6508 | 0.3409 | 0.4683 | -0.065 ± 0.0139 | -0.06 (2) |
| 40+ | 186 | 0.2966 | 0.1748 | +0.1217 ± 0.0275 | 0.7985 | 0.5224 | 0.73 | 0.2752 | 0.3763 | -0.084 ± 0.0267 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5366 | 0.1853 | 0.1862 | -0.0009 ± 0.0002 | 0.5465 | 0.5476 | 0.4903 | 0.4751 | 0.5073 | -0.020 ± 0.006 | -0.01 (28) |
| 3-5 | 3591 | 0.1972 | 0.1957 | +0.0016 ± 0.0006 | 0.5746 | 0.5687 | 0.4817 | 0.4419 | 0.4414 | -0.055 ± 0.0075 | 0.0 (3) |
| 5-10 | 7772 | 0.2005 | 0.1974 | +0.0031 ± 0.0008 | 0.5867 | 0.5758 | 0.4842 | 0.4105 | 0.4265 | -0.043 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6427 | 0.2021 | 0.1862 | +0.0159 ± 0.0013 | 0.5908 | 0.546 | 0.4852 | 0.3612 | 0.3594 | -0.063 ± 0.0054 | -0.0281 (16) |
| 15-25 | 8128 | 0.2062 | 0.167 | +0.0393 ± 0.0018 | 0.6044 | 0.4961 | 0.4995 | 0.304 | 0.3022 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6256 | 0.2229 | 0.1267 | +0.0963 ± 0.0028 | 0.6401 | 0.389 | 0.5268 | 0.2132 | 0.2207 | -0.057 ± 0.0044 | -0.0733 (3) |
| 40+ | 4148 | 0.3823 | 0.0441 | +0.3382 ± 0.0037 | 0.996 | 0.1711 | 0.6306 | 0.1017 | 0.0583 | -0.076 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 819 | 0.204 | 0.2045 | -0.0004 ± 0.0005 | 0.5885 | 0.5899 | 0.5068 | 0.492 | 0.5153 | -0.102 ± 0.017 | -0.0117 (6) |
| 3-5 | 585 | 0.2107 | 0.2079 | +0.0028 ± 0.0015 | 0.6038 | 0.5979 | 0.5117 | 0.4721 | 0.453 | -0.129 ± 0.0203 | 0.01 (2) |
| 5-10 | 1313 | 0.2064 | 0.2047 | +0.0017 ± 0.0019 | 0.5989 | 0.5942 | 0.5396 | 0.4651 | 0.4935 | -0.087 ± 0.0129 | -0.01 (4) |
| 10-15 | 1139 | 0.212 | 0.2067 | +0.0054 ± 0.0034 | 0.6163 | 0.599 | 0.5631 | 0.4388 | 0.482 | -0.098 ± 0.0141 | -0.04 (5) |
| 15-25 | 1665 | 0.2316 | 0.2124 | +0.0192 ± 0.0044 | 0.6592 | 0.6093 | 0.5846 | 0.3891 | 0.439 | -0.099 ± 0.0116 | -0.0118 (11) |
| 25-40 | 1157 | 0.2663 | 0.1971 | +0.0692 ± 0.0082 | 0.7431 | 0.5741 | 0.6582 | 0.344 | 0.3933 | -0.119 ± 0.0131 | -0.008 (5) |
| 40+ | 416 | 0.3729 | 0.1618 | +0.2111 ± 0.0197 | 1.0165 | 0.4896 | 0.7351 | 0.2464 | 0.2885 | -0.088 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4599 | 0.1917 | 0.1919 | -0.0002 ± 0.0002 | 0.5588 | 0.5591 | 0.5071 | 0.492 | 0.5086 | -0.039 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3140 | 0.1926 | 0.1916 | +0.0010 ± 0.0006 | 0.5615 | 0.5583 | 0.5113 | 0.4716 | 0.4783 | -0.045 ± 0.008 | 0.01 (2) |
| 5-10 | 6931 | 0.197 | 0.1937 | +0.0033 ± 0.0008 | 0.5789 | 0.5668 | 0.5086 | 0.4345 | 0.4519 | -0.040 ± 0.0054 | -0.0117 (6) |
| 10-15 | 5766 | 0.202 | 0.1914 | +0.0107 ± 0.0014 | 0.5932 | 0.5597 | 0.5104 | 0.3864 | 0.4062 | -0.045 ± 0.0059 | -0.0189 (18) |
| 15-25 | 8190 | 0.2171 | 0.1817 | +0.0354 ± 0.0019 | 0.6314 | 0.5327 | 0.525 | 0.3294 | 0.3393 | -0.059 ± 0.0048 | -0.0094 (49) |
| 25-40 | 7350 | 0.251 | 0.1371 | +0.1139 ± 0.0027 | 0.709 | 0.4192 | 0.5596 | 0.2426 | 0.225 | -0.081 ± 0.0043 | -0.0095 (20) |
| 40+ | 5712 | 0.4014 | 0.0588 | +0.3427 ± 0.0037 | 1.0584 | 0.212 | 0.6541 | 0.1186 | 0.08 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1000 | 0.1958 | 0.1973 | -0.0015 ± 0.0005 | 0.5713 | 0.5749 | 0.503 | 0.4875 | 0.535 | -0.050 ± 0.0147 | -0.012 (10) |
| 3-5 | 699 | 0.2061 | 0.2048 | +0.0014 ± 0.0014 | 0.5978 | 0.5931 | 0.4957 | 0.4562 | 0.4607 | -0.109 ± 0.0179 | -0.0 (4) |
| 5-10 | 1558 | 0.2022 | 0.1989 | +0.0034 ± 0.0017 | 0.5895 | 0.5799 | 0.512 | 0.4383 | 0.4519 | -0.103 ± 0.0117 | -0.01 (10) |
| 10-15 | 1248 | 0.2111 | 0.2015 | +0.0095 ± 0.0032 | 0.6127 | 0.585 | 0.5365 | 0.4132 | 0.4383 | -0.109 ± 0.0128 | -0.0286 (7) |
| 15-25 | 1505 | 0.2312 | 0.2126 | +0.0187 ± 0.0046 | 0.6601 | 0.6094 | 0.5855 | 0.3914 | 0.4399 | -0.108 ± 0.0119 | -0.03 (1) |
| 25-40 | 889 | 0.2123 | 0.2101 | +0.0022 ± 0.009 | 0.6133 | 0.6026 | 0.659 | 0.3481 | 0.4983 | -0.052 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5183 | 0.1855 | 0.1862 | -0.0007 ± 0.0002 | 0.5466 | 0.5475 | 0.4861 | 0.4707 | 0.491 | -0.031 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3687 | 0.2032 | 0.2016 | +0.0016 ± 0.0006 | 0.591 | 0.5853 | 0.478 | 0.4386 | 0.4386 | -0.054 ± 0.0075 | -0.01 (19) |
| 5-10 | 7929 | 0.1955 | 0.1905 | +0.0050 ± 0.0007 | 0.5742 | 0.5583 | 0.4871 | 0.4131 | 0.4166 | -0.054 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6371 | 0.1937 | 0.1783 | +0.0155 ± 0.0013 | 0.5722 | 0.5277 | 0.4942 | 0.3709 | 0.3698 | -0.063 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8224 | 0.2119 | 0.1723 | +0.0396 ± 0.0018 | 0.6178 | 0.5083 | 0.5123 | 0.3178 | 0.3142 | -0.071 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6195 | 0.2167 | 0.1278 | +0.0888 ± 0.0029 | 0.6266 | 0.3912 | 0.5293 | 0.2136 | 0.2329 | -0.047 ± 0.0044 | -0.02 (4) |
| 40+ | 4099 | 0.3916 | 0.0492 | +0.3424 ± 0.0039 | 1.0208 | 0.1838 | 0.6401 | 0.1079 | 0.0654 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1429 | 0.1978 | 0.1978 | -0.0000 ± 0.0004 | 0.574 | 0.5739 | 0.5086 | 0.4936 | 0.4976 | -0.069 ± 0.012 | -0.0213 (54) |
| 3-5 | 1028 | 0.1882 | 0.188 | +0.0002 ± 0.0011 | 0.5543 | 0.5519 | 0.4963 | 0.4564 | 0.4718 | -0.059 ± 0.0138 | -0.0194 (34) |
| 5-10 | 2078 | 0.1987 | 0.1942 | +0.0045 ± 0.0015 | 0.5866 | 0.5712 | 0.507 | 0.4334 | 0.4398 | -0.075 ± 0.0099 | -0.005 (78) |
| 10-15 | 1436 | 0.2142 | 0.2017 | +0.0124 ± 0.0029 | 0.6216 | 0.587 | 0.5424 | 0.4196 | 0.429 | -0.090 ± 0.0122 | 0.0012 (66) |
| 15-25 | 1855 | 0.2307 | 0.2071 | +0.0237 ± 0.0042 | 0.6589 | 0.5979 | 0.5904 | 0.3954 | 0.4345 | -0.089 ± 0.0107 | -0.0214 (59) |
| 25-40 | 1123 | 0.2402 | 0.2102 | +0.0300 ± 0.0083 | 0.686 | 0.6034 | 0.6886 | 0.3765 | 0.4844 | -0.087 ± 0.0129 | -0.0252 (27) |
| 40+ | 396 | 0.3271 | 0.2018 | +0.1252 ± 0.0216 | 0.9416 | 0.5873 | 0.816 | 0.3399 | 0.4621 | -0.097 ± 0.0202 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5271 | 0.1778 | 0.1779 | -0.0001 ± 0.0002 | 0.5259 | 0.5257 | 0.5115 | 0.4963 | 0.5065 | -0.039 ± 0.0059 | -0.0145 (98) |
| 3-5 | 3651 | 0.1952 | 0.1942 | +0.0009 ± 0.0006 | 0.5691 | 0.5664 | 0.5009 | 0.4612 | 0.47 | -0.041 ± 0.0074 | -0.0204 (72) |
| 5-10 | 7436 | 0.1959 | 0.1896 | +0.0063 ± 0.0008 | 0.5785 | 0.559 | 0.5007 | 0.4272 | 0.4221 | -0.061 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5104 | 0.2086 | 0.1927 | +0.0159 ± 0.0015 | 0.6077 | 0.5659 | 0.5367 | 0.4138 | 0.4091 | -0.071 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6186 | 0.2312 | 0.1999 | +0.0314 ± 0.0022 | 0.6646 | 0.5791 | 0.5763 | 0.3809 | 0.3993 | -0.067 ± 0.0057 | -0.026 (108) |
| 25-40 | 4046 | 0.257 | 0.1903 | +0.0667 ± 0.0043 | 0.7274 | 0.5541 | 0.6402 | 0.3276 | 0.3799 | -0.066 ± 0.0067 | -0.0246 (52) |
| 40+ | 1779 | 0.3706 | 0.1596 | +0.2110 ± 0.0098 | 1.0454 | 0.475 | 0.7444 | 0.2437 | 0.2934 | -0.064 ± 0.009 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7094 | 1.031 ± 0.033 | 1.107 | 0.1691 | 0.1691 | 0.2144 | 0.2035 |
| gen2 | 7094 | 0.824 ± 0.03 | 1.078 | 0.1734 | 0.1694 | 0.2328 | 0.2033 |
| gen1_elo | 7094 | 1.012 ± 0.032 | 1.095 | 0.1755 | 0.1692 | 0.2136 | 0.2036 |
| gen1_sr | 7094 | 1.01 ± 0.039 | 1.136 | 0.1334 | 0.1711 | 0.2291 | 0.203 |
| gen1_ledger | 9345 | 0.868 ± 0.024 | 1.078 | 0.1899 | 0.1761 | 0.2166 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,020)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,615 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,453 | 22.6% |
| BOOK_QUALITY | execution | 5,920 | 17.9% |
| POOR_DATA | data | 3,839 | 11.6% |
| LIMITED_DATA | data | 2,056 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,910 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,369 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,368 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 943 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 546 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.6%, execution 17.9%, data 17.8%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.1%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.0%, POST_SETTLEMENT_OBSERVATION 22.6%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,530)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,970 | 34.1% |
| STALE_QUOTE | market_freshness | 3,398 | 19.4% |
| BOOK_QUALITY | execution | 3,069 | 17.5% |
| POOR_DATA | data | 1,617 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,016 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 762 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 617 | 3.5% |
| LIMITED_DATA | data | 604 | 3.5% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 342 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 134 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.1%, market_freshness 19.4%, execution 17.5%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.9%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 53.4%, STALE_PLAYER_DATA 45.8%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.4%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.1%, POST_SETTLEMENT_OBSERVATION 34.1%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13978, "IDENTITY_AMBIGUOUS": 3552}; ticker orientation: {"VERIFIED": 17530}.

Checks: discipline:AMBIGUOUS 1184, discipline:PASS 16346, identity_confidence:AMBIGUOUS 3222, identity_confidence:PASS 14308, level_mapping:NA 1196, level_mapping:PASS 16334, market_pair:AMBIGUOUS 491, market_pair:NA 388, market_pair:PASS 16651, model_complement:NA 350, model_complement:PASS 17180, namesake:AMBIGUOUS 6, namesake:PASS 17524, physical_match_id:NA 5986, physical_match_id:PASS 11544, player_ids:PASS 17530, same_pair_other_event:PASS 17530, ticker_orientation:PASS 17530

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,271 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.52 | 0.2264 / 0.2216 (797) | 24.6% | 2.5% | 3.1% | 2.7% |
| CHALLENGER | 11,535 | 16.2% | 6.1% | 10.7% | {"coverage": 1101, "market_freshness/coverage": 218, "market_freshness": 217, "data": 157, "model_calibration_or_unknown": 81, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.37 | 0.2196 / 0.2096 (2704) | 37.8% | 15.2% | 4.1% | 22.3% |
| DOUBLES | 2,547 | 46.5% | 46.4% | 6.8% | {"execution": 663, "mapping": 341, "market_freshness": 106, "market_freshness/coverage": 67, "coverage": 7} | 23.23 | 0.2978 / 0.2332 (632) | 9.2% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 23,070 | 24.8% | 17.3% | 32.6% | {"coverage": 1996, "market_freshness": 1107, "execution": 977, "data": 845, "market_freshness/coverage": 578, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 4} | 11.67 | 0.2162 / 0.1987 (4896) | 39.8% | 68.8% | 15.2% | 21.5% |
| ITF_WOMEN | 30,029 | 26.4% | 18.9% | 45.2% | {"coverage": 2790, "market_freshness": 1708, "execution": 1305, "data": 1118, "market_freshness/coverage": 696, "mapping": 194, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.49 | 0.2028 / 0.1935 (5814) | 41.0% | 57.1% | 9.8% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,806 | 6.0% | 5.1% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 52, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2292 / 0.22 (784) | 29.8% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 2.8h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 176 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 14.3h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 869 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 15.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 928 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 12.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 768 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 747 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 873 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.2h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 82 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9699, "by_level_share_of_ge_25pp": {"ATP": 0.0135, "CHALLENGER": 0.1066, "DOUBLES": 0.0675, "ITF_MEN": 0.3261, "ITF_WOMEN": 0.4523, "OTHER": 0.0007, "WTA": 0.0165, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.534, "share_primary_cause_market_settled_or_in_play": 0.4338, "share_primary_cause_stale_quote_only": 0.1938}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17530, "identity_ambiguous_share": 0.2026, "ticker_orientation": {"VERIFIED": 17530}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11544, "with_external": 613, "coverage": 0.0531, "external_status": {"EXTERNAL_STALE": 392, "AGREES_WITH_KALSHI": 208, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 392, "MODEL_LONE_OUTLIER": 208, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3393, "share_external_supports_model": 0.0212}, "pregame_clean_ge_25pp": {"n": 5429, "with_external": 583, "coverage": 0.1074, "external_status": {"EXTERNAL_STALE": 369, "AGREES_WITH_KALSHI": 201, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 369, "MODEL_LONE_OUTLIER": 201, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3448, "share_external_supports_model": 0.0223}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2084, "data_status": {"POOR": 9828, "LIMITED": 4557, "ADEQUATE": 3145}, "comparison_lt_10pp": {"median_thinner_serve_points": 1724.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1436, "model_minus_observed": 0.0618, "kalshi_minus_observed": -0.0771, "brier_diff_model_minus_kalshi": 0.0013}, "4-10x": {"n": 976, "model_minus_observed": 0.088, "kalshi_minus_observed": -0.0567, "brier_diff_model_minus_kalshi": 0.0084}, "<2x": {"n": 3482, "model_minus_observed": 0.0986, "kalshi_minus_observed": -0.0243, "brier_diff_model_minus_kalshi": 0.0144}, ">=10x": {"n": 1200, "model_minus_observed": 0.1158, "kalshi_minus_observed": -0.057, "brier_diff_model_minus_kalshi": 0.0146}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7094, "model": {"intercept": -0.553, "slope": 0.824, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.187, "slope": 1.078, "slope_se": 0.034}, "mean_extremity_model": 0.1734, "mean_extremity_kalshi": 0.1694, "model_brier": 0.2328, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0295, "brier_diff_se": 0.0022, "model_logloss": 0.6631, "kalshi_logloss": 0.5889}, "fair_v1": {"n": 7094, "model": {"intercept": -0.445, "slope": 1.031, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.256, "slope": 1.107, "slope_se": 0.034}, "mean_extremity_model": 0.1691, "mean_extremity_kalshi": 0.1691, "model_brier": 0.2144, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.011, "brier_diff_se": 0.0018, "model_logloss": 0.6179, "kalshi_logloss": 0.5892}, "gen1_elo": {"n": 7094, "model": {"intercept": -0.437, "slope": 1.012, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.253, "slope": 1.095, "slope_se": 0.033}, "mean_extremity_model": 0.1755, "mean_extremity_kalshi": 0.1692, "model_brier": 0.2136, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0101, "brier_diff_se": 0.0018, "model_logloss": 0.6166, "kalshi_logloss": 0.5894}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2469, "share_ge_15": 0.4432, "median_abs_gap": 13.02, "n": 46755}, "gen1_elo": {"share_ge_25": 0.2438, "share_ge_15": 0.4393, "median_abs_gap": 12.8, "n": 46755}, "gen1_sr": {"share_ge_25": 0.3128, "share_ge_15": 0.5196, "median_abs_gap": 15.78, "n": 46755}, "gen2": {"share_ge_25": 0.3131, "share_ge_15": 0.5097, "median_abs_gap": 15.44, "n": 46755}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1505, "share_ge_15": 0.353, "median_abs_gap": 10.67, "n": 36058}, "gen1_elo": {"share_ge_25": 0.1483, "share_ge_15": 0.3482, "median_abs_gap": 10.49, "n": 36058}, "gen1_sr": {"share_ge_25": 0.2159, "share_ge_15": 0.439, "median_abs_gap": 12.98, "n": 36060}, "gen2": {"share_ge_25": 0.2303, "share_ge_15": 0.4383, "median_abs_gap": 12.84, "n": 36060}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0378, "share_ge_25_pregame_clean": 0.0326}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0603, "share_ge_25_pregame_clean": 0.0512}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.4393, "share_within_10pp_pregame_clean": 0.4922, "corr_model_vs_mid_pregame_clean": 0.8512}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1021, "model_brier": 0.1973, "kalshi_brier": 0.1977, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1229, "model_brier": 0.2187, "kalshi_brier": 0.2096, "brier_diff_model_minus_kalshi": 0.0091}, "15-25": {"n_settled": 1575, "model_brier": 0.2253, "kalshi_brier": 0.2077, "brier_diff_model_minus_kalshi": 0.0175}, "25-40": {"n_settled": 899, "model_brier": 0.2226, "kalshi_brier": 0.2053, "brier_diff_model_minus_kalshi": 0.0173}, "3-5": {"n_settled": 657, "model_brier": 0.2039, "kalshi_brier": 0.2041, "brier_diff_model_minus_kalshi": -0.0001}, "40+": {"n_settled": 186, "model_brier": 0.2966, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1217}, "5-10": {"n_settled": 1527, "model_brier": 0.201, "kalshi_brier": 0.2002, "brier_diff_model_minus_kalshi": 0.0008}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.553, "slope": 0.824, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.187, "slope": 1.078, "slope_se": 0.034}, "n": 7094}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.486, "slope": 0.868, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.175, "slope": 1.078, "slope_se": 0.029}, "n": 9345}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 632, "model_brier": 0.2978, "kalshi_brier": 0.2332, "brier_diff_model_minus_kalshi": 0.0646, "brier_diff_se": 0.0116, "corr_model_outcome": 0.0987, "corr_kalshi_outcome": 0.2744}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
