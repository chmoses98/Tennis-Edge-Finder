# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-07T07:28Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 81,280): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.1%; median gap 11.82 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.8%). Main tour: ATP 3.8% and WTA 6.0% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,596): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.2%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.5%, POOR_DATA 9.2%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.2%, market_freshness 19.4%, execution 17.5%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.5% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.5% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,596 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.2% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 491.0 points vs 1729.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.029, Gen-2 0.823, Gen-1 ledger 0.866 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 900 model 0.2227 vs Kalshi 0.2052; n 186 model 0.2966 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 344,593 model-market comparisons (564,586 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 114,797 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-07T07:09:56.069916+00:00'], shadow board 93,364 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-07T07:09:59.629783+00:00'], Model 4 42,472 rows, 28,665 settled tickers, 10,763 tickers with an external scan.
* By model: {"gen1_ledger": 77320, "gen1_elo": 46921, "fair_v1": 46921, "gen2": 46921, "gen1_sr": 46921, "model4_fundamental": 39836, "model4_conditioned": 39753}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 81,280 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.1 | 11.82 | 40.8% | 21.6% |
| MW fair_v1 | 46,921 | 12.9 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 9.9 | 13.03 | 44.4% | 24.7% |
| MW gen1_elo | 46,921 | 12.6 | 8.8 | 19.2 | 15.4 | 19.5 | 14.6 | 9.8 | 12.81 | 44.0% | 24.4% |
| MW gen1_ledger | 34,359 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| MW gen1_sr | 46,921 | 10.1 | 7.3 | 16.7 | 14.0 | 20.7 | 18.7 | 12.6 | 15.8 | 52.0% | 31.3% |
| MW gen2 | 46,921 | 11.0 | 7.6 | 16.6 | 13.7 | 19.7 | 17.7 | 13.7 | 15.45 | 51.0% | 31.3% |
| all families model4_conditioned | 39,753 | 22.2 | 18.0 | 34.1 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,836 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.4% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.6%, >=30pp 15.6%, >=40pp 8.1%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.39pp; >=10pp 45.0%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,945 | 28.6 | 15.7 | 27.5 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.8% | 4.2% |
| CHALLENGER | 7,030 | 16.2 | 9.7 | 20.7 | 15.2 | 16.1 | 11.3 | 10.7 | 10.91 | 38.1% | 22.1% |
| ITF_MEN | 13,308 | 9.8 | 7.4 | 17.1 | 15.1 | 21.3 | 17.2 | 12.2 | 15.23 | 50.7% | 29.4% |
| ITF_WOMEN | 18,267 | 9.6 | 7.1 | 16.1 | 14.8 | 22.2 | 18.3 | 12.0 | 15.85 | 52.5% | 30.3% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,038 | 16.8 | 13.1 | 24.7 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,945 | 26.8 | 15.8 | 26.1 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.9% | 4.5% |
| CHALLENGER | 7,030 | 14.7 | 9.1 | 18.9 | 13.9 | 18.6 | 13.4 | 11.4 | 12.47 | 43.4% | 24.8% |
| ITF_MEN | 13,308 | 8.2 | 6.1 | 15.1 | 13.8 | 20.0 | 20.5 | 16.4 | 17.93 | 56.8% | 36.8% |
| ITF_WOMEN | 18,267 | 7.8 | 5.9 | 14.1 | 12.8 | 20.8 | 21.1 | 17.5 | 19.08 | 59.4% | 38.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,038 | 14.1 | 10.2 | 21.6 | 16.2 | 22.4 | 12.9 | 2.5 | 11.28 | 37.9% | 15.5% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,945 | 22.8 | 14.1 | 25.3 | 15.6 | 14.9 | 6.1 | 1.2 | 7.11 | 22.1% | 7.2% |
| CHALLENGER | 7,030 | 15.2 | 9.5 | 20.7 | 15.7 | 16.2 | 11.8 | 10.9 | 11.32 | 38.9% | 22.7% |
| ITF_MEN | 13,308 | 9.5 | 7.3 | 17.3 | 14.2 | 21.9 | 17.2 | 12.6 | 15.64 | 51.7% | 29.8% |
| ITF_WOMEN | 18,267 | 9.3 | 6.9 | 16.3 | 15.7 | 22.2 | 18.2 | 11.4 | 15.57 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,038 | 22.8 | 17.1 | 31.8 | 15.2 | 8.7 | 3.3 | 1.1 | 6.12 | 13.0% | 4.3% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,346 | 26.9 | 19.8 | 30.0 | 12.2 | 8.2 | 2.6 | 0.4 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,542 | 22.4 | 14.6 | 27.5 | 14.9 | 13.4 | 5.7 | 1.5 | 7.08 | 20.6% | 7.2% |
| DOUBLES | 2,562 | 4.8 | 4.5 | 12.9 | 11.1 | 20.3 | 24.4 | 22.0 | 23.27 | 66.7% | 46.4% |
| ITF_MEN | 9,863 | 12.9 | 9.6 | 21.4 | 15.7 | 21.6 | 12.9 | 5.8 | 11.76 | 40.3% | 18.7% |
| ITF_WOMEN | 11,859 | 13.4 | 9.3 | 20.0 | 15.7 | 21.4 | 14.9 | 5.4 | 12.22 | 41.7% | 20.3% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,782 | 23.8 | 16.1 | 31.3 | 16.9 | 9.0 | 2.6 | 0.2 | 6.56 | 11.8% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,830 | 29.0 | 15.8 | 27.9 | 13.3 | 10.4 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,971 | 20.9 | 12.0 | 25.6 | 18.0 | 16.0 | 5.9 | 1.6 | 8.23 | 23.5% | 7.5% |
| ITF_MEN | 9,711 | 12.0 | 8.7 | 20.7 | 17.4 | 22.1 | 14.0 | 5.2 | 12.38 | 41.3% | 19.2% |
| ITF_WOMEN | 13,436 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.1 | 4.9 | 13.16 | 44.0% | 20.0% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,925 | 17.1 | 13.2 | 25.0 | 21.2 | 16.6 | 6.3 | 0.6 | 8.5 | 23.5% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,830 | 27.1 | 16.2 | 26.4 | 15.3 | 11.3 | 3.3 | 0.4 | 5.95 | 15.0% | 3.7% |
| CHALLENGER | 4,971 | 18.4 | 11.5 | 23.8 | 16.2 | 19.1 | 9.2 | 1.8 | 8.98 | 30.1% | 11.0% |
| ITF_MEN | 9,712 | 9.7 | 7.2 | 17.6 | 16.0 | 21.7 | 18.7 | 9.1 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,437 | 8.9 | 6.9 | 16.1 | 14.4 | 22.7 | 20.4 | 10.7 | 16.5 | 53.8% | 31.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,925 | 14.4 | 10.3 | 21.9 | 16.3 | 22.6 | 12.6 | 1.9 | 11.03 | 37.1% | 14.5% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,289 | 27.0 | 20.0 | 29.9 | 12.4 | 7.9 | 2.5 | 0.3 | 5.3 | 10.7% | 2.8% |
| CHALLENGER | 4,013 | 23.7 | 15.5 | 28.6 | 15.1 | 12.8 | 4.0 | 0.4 | 6.6 | 17.1% | 4.4% |
| DOUBLES | 2,405 | 4.7 | 4.5 | 13.1 | 11.1 | 20.2 | 24.3 | 22.0 | 23.2 | 66.5% | 46.3% |
| ITF_MEN | 8,475 | 13.7 | 10.2 | 23.0 | 16.2 | 21.6 | 11.4 | 3.8 | 10.81 | 36.8% | 15.2% |
| ITF_WOMEN | 10,161 | 14.0 | 9.8 | 21.1 | 16.2 | 21.6 | 13.8 | 3.5 | 11.41 | 38.9% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,720 | 24.1 | 16.5 | 31.3 | 16.9 | 9.0 | 2.0 | 0.1 | 6.43 | 11.1% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,562 | 4.8 | 4.5 | 12.9 | 11.1 | 20.3 | 24.4 | 22.0 | 23.27 | 66.7% | 46.4% |
| singles | 31,797 | 16.6 | 11.5 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.72 | 33.4% | 15.1% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 170 | 8.2 | 9.4 | 11.8 | 7.7 | 19.4 | 28.8 | 14.7 | 21.18 | 62.9% | 43.5% |
| Clay | 9,654 | 12.7 | 9.1 | 19.9 | 15.6 | 19.7 | 13.8 | 9.2 | 12.59 | 42.7% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,528 | 13.4 | 8.7 | 18.8 | 15.2 | 19.2 | 14.8 | 9.9 | 12.87 | 43.9% | 24.7% |
| UNKNOWN | 6,332 | 10.6 | 7.6 | 17.0 | 16.3 | 21.5 | 16.0 | 11.1 | 14.32 | 48.5% | 27.0% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,329 | 19.6 | 11.9 | 22.4 | 15.9 | 14.9 | 9.2 | 6.2 | 8.88 | 30.3% | 15.4% |
| B | 5,741 | 12.7 | 8.7 | 19.7 | 15.7 | 19.8 | 12.7 | 10.8 | 12.67 | 43.3% | 23.4% |
| C | 6,650 | 12.0 | 8.9 | 19.5 | 15.7 | 18.6 | 14.6 | 10.7 | 12.93 | 43.9% | 25.3% |
| D | 7,623 | 11.7 | 8.3 | 18.0 | 15.3 | 21.7 | 15.7 | 9.4 | 13.84 | 46.8% | 25.1% |
| F | 13,578 | 7.4 | 5.6 | 14.8 | 14.7 | 23.6 | 20.8 | 13.1 | 17.75 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,210 | 24.5 | 16.1 | 29.1 | 15.0 | 10.6 | 3.4 | 1.2 | 6.37 | 15.2% | 4.6% |
| B | 4,821 | 16.6 | 10.8 | 24.2 | 16.9 | 18.8 | 9.6 | 3.0 | 9.67 | 31.5% | 12.7% |
| C | 6,783 | 11.0 | 7.8 | 19.6 | 14.6 | 21.0 | 15.6 | 10.4 | 13.6 | 47.0% | 26.0% |
| D | 5,152 | 14.5 | 10.1 | 21.4 | 15.4 | 20.8 | 12.5 | 5.3 | 11.18 | 38.5% | 17.7% |
| F | 8,393 | 10.2 | 8.4 | 16.2 | 14.6 | 23.4 | 19.5 | 7.7 | 15.33 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 15,050 | 17.8 | 10.9 | 21.5 | 15.7 | 15.3 | 10.0 | 8.8 | 9.97 | 34.1% | 18.9% |
| LIMITED | 10,280 | 13.7 | 9.8 | 20.4 | 15.8 | 19.4 | 13.3 | 7.6 | 11.86 | 40.3% | 20.9% |
| POOR | 21,591 | 9.0 | 6.6 | 16.0 | 14.9 | 22.8 | 18.8 | 11.8 | 16.15 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,769 | 23.7 | 17.9 | 33.1 | 15.6 | 6.4 | 2.9 | 0.4 | 5.91 | 9.7% | 3.3% |
| GAME_SPREAD | 6,630 | 22.6 | 15.4 | 32.1 | 16.9 | 9.0 | 3.4 | 0.7 | 6.7 | 13.0% | 4.1% |
| MATCH_WINNER | 34,359 | 15.7 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,336 | 27.9 | 16.7 | 30.8 | 12.7 | 9.1 | 2.4 | 0.3 | 5.64 | 11.8% | 2.7% |
| TOTAL_GAMES | 11,202 | 9.8 | 10.8 | 35.6 | 26.0 | 10.7 | 4.2 | 2.9 | 9.19 | 17.8% | 7.1% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,051 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,165 | 47.0 | 16.1 | 24.7 | 7.5 | 2.3 | 1.9 | 0.6 | 3.29 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,537 | 6.6 | 9.9 | 40.2 | 30.2 | 7.4 | 3.3 | 2.4 | 9.21 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,086 | 23.9 | 16.7 | 34.7 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,174 | 20.6 | 13.6 | 28.2 | 20.0 | 11.9 | 4.4 | 1.2 | 7.6 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,576 | 10.0 | 10.8 | 36.2 | 24.3 | 11.5 | 4.5 | 2.6 | 9.06 | 18.6% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 46,921 | 44.4% | 24.7% | 13.03 | 35.3% | 15.0% | 10.67 |
| gen1_elo | 46,921 | 44.0% | 24.4% | 12.81 | 34.8% | 14.8% | 10.49 |
| gen1_sr | 46,921 | 52.0% | 31.3% | 15.8 | 43.9% | 21.6% | 12.97 |
| gen2 | 46,921 | 51.0% | 31.3% | 15.45 | 43.8% | 23.0% | 12.83 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,974 | 15.6 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,947 | 10.9 | 7.3 | 16.8 | 14.0 | 19.3 | 16.9 | 14.8 | 15.39 | 51.0% | 31.7% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,827 | 16.3 | 11.3 | 22.8 | 15.3 | 18.0 | 11.5 | 4.8 | 9.87 | 34.3% | 16.3% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 81,280 | 27827 | 23446 | 30007 | 24.8 | 126.7 | 1451.1 |
| ge_15pp | 33,151 | 9543 | 8353 | 15255 | 28.2 | 433.5 | 1451.1 |
| ge_25pp | 17,596 | 4540 | 3645 | 9411 | 33.1 | 581.3 | 1431.1 |
| lt_10pp | 35,700 | 14035 | 11092 | 10573 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261107T072855Z-9c92854f`: 210 priced rows, quote age at build {'median': 19.3, 'max': 19.4}, freshness {'AGING': 210}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,633 | 19.2 | 10.9 | 25.4 | 17.8 | 18.1 | 7.5 | 1.0 | 8.81 | 26.6% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 978 | 66.8 | 33.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.17 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,085 | 0.0 | 2.2 | 37.4 | 26.3 | 24.0 | 9.2 | 0.9 | 11.8 | 34.1% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 46,921 | 7804 (16.6%) | 26.7% | 1.0% | {"EXTERNAL_STALE": 4633, "AGREES_WITH_KALSHI": 2085, "ALL_AGREE": 978, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,809 | 1971 (9.5%) | 36.1% | 1.5% | {"EXTERNAL_STALE": 1230, "AGREES_WITH_KALSHI": 711, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,594 | 614 (5.3%) | 34.2% | 2.1% | {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,434 | 584 (10.8%) | 34.8% | 2.2% | {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,896 | 4454 (23.6%) | 18.6% | 1.0% | {"EXTERNAL_STALE": 2577, "ALL_AGREE": 978, "AGREES_WITH_KALSHI": 826, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,204 | 10.5 | 7.7 | 19.4 | 14.6 | 21.6 | 16.2 | 9.9 | 14.08 | 47.7% | 26.1% |
| 4-10x | 6,291 | 11.3 | 8.5 | 18.4 | 15.2 | 22.1 | 14.2 | 10.2 | 13.79 | 46.6% | 24.4% |
| <2x | 23,951 | 14.9 | 9.8 | 19.7 | 16.0 | 17.6 | 13.1 | 8.9 | 11.56 | 39.5% | 22.0% |
| >=10x | 7,475 | 10.4 | 6.4 | 15.0 | 14.4 | 21.7 | 18.8 | 13.1 | 16.38 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,309 | 12.4 | 8.6 | 19.9 | 16.2 | 19.1 | 13.5 | 10.3 | 12.73 | 42.9% | 23.9% |
| 300-1000 | 10,177 | 11.8 | 8.7 | 17.7 | 15.2 | 20.8 | 16.2 | 9.5 | 13.73 | 46.6% | 25.8% |
| <300 | 14,685 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.8 | 13.1 | 17.11 | 56.0% | 32.9% |
| >=3000 | 9,750 | 21.4 | 12.9 | 23.9 | 15.6 | 13.9 | 7.3 | 5.0 | 7.75 | 26.3% | 12.3% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1441 | 0.5481 | 0.4093 | 0.4858 | +0.062 | -0.076 | 0.0016 ± 0.004 |
| ratio 4-10x | 980 | 0.5769 | 0.4323 | 0.4878 | +0.089 | -0.056 | 0.0087 ± 0.0051 |
| ratio <2x | 3499 | 0.5362 | 0.4136 | 0.4373 | +0.099 | -0.024 | 0.0145 ± 0.0024 |
| ratio >=10x | 1202 | 0.5645 | 0.392 | 0.4476 | +0.117 | -0.056 | 0.0148 ± 0.0052 |
| thinner_sample 1000-3000 | 1972 | 0.5391 | 0.412 | 0.4473 | +0.092 | -0.035 | 0.0116 ± 0.0033 |
| thinner_sample 300-1000 | 1623 | 0.5638 | 0.4236 | 0.4732 | +0.091 | -0.050 | 0.0049 ± 0.0038 |
| thinner_sample <300 | 2303 | 0.5576 | 0.3901 | 0.4546 | +0.103 | -0.065 | 0.0131 ± 0.0037 |
| thinner_sample >=3000 | 1224 | 0.5292 | 0.4358 | 0.4485 | +0.081 | -0.013 | 0.0148 ± 0.0032 |
| data_status ADEQUATE | 1971 | 0.532 | 0.429 | 0.4414 | +0.091 | -0.012 | 0.0152 ± 0.0028 |
| data_status LIMITED | 1740 | 0.5472 | 0.415 | 0.4667 | +0.081 | -0.052 | 0.0073 ± 0.0036 |
| data_status POOR | 3411 | 0.5597 | 0.3999 | 0.4585 | +0.101 | -0.059 | 0.0107 ± 0.0029 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1031 | 0.1972 | 0.1976 | -0.0004 ± 0.0005 | 0.5742 | 0.575 | 0.5027 | 0.4876 | 0.5024 | -0.092 ± 0.0147 | -0.0087 (8) |
| 3-5 | 658 | 0.2047 | 0.2047 | -0.0000 ± 0.0014 | 0.5936 | 0.5921 | 0.5036 | 0.4638 | 0.4833 | -0.094 ± 0.0181 | 0.01 (2) |
| 5-10 | 1533 | 0.2014 | 0.2004 | +0.0010 ± 0.0017 | 0.5891 | 0.5843 | 0.5114 | 0.4376 | 0.4658 | -0.090 ± 0.0119 | -0.0143 (7) |
| 10-15 | 1234 | 0.2185 | 0.2094 | +0.0091 ± 0.0032 | 0.629 | 0.6022 | 0.5234 | 0.4 | 0.4238 | -0.105 ± 0.0132 | -0.048 (5) |
| 15-25 | 1580 | 0.2257 | 0.2077 | +0.0180 ± 0.0045 | 0.6465 | 0.5988 | 0.5753 | 0.3808 | 0.4316 | -0.106 ± 0.0115 | -0.0045 (11) |
| 25-40 | 900 | 0.2227 | 0.2052 | +0.0175 ± 0.009 | 0.6353 | 0.5914 | 0.6507 | 0.3409 | 0.4678 | -0.066 ± 0.0138 | -0.06 (2) |
| 40+ | 186 | 0.2966 | 0.1748 | +0.1217 ± 0.0275 | 0.7985 | 0.5224 | 0.73 | 0.2752 | 0.3763 | -0.084 ± 0.0267 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5401 | 0.1852 | 0.1861 | -0.0009 ± 0.0002 | 0.5463 | 0.5475 | 0.4904 | 0.4751 | 0.5079 | -0.020 ± 0.006 | -0.01 (28) |
| 3-5 | 3599 | 0.1976 | 0.196 | +0.0016 ± 0.0006 | 0.5754 | 0.5694 | 0.482 | 0.4422 | 0.4415 | -0.055 ± 0.0075 | 0.0 (3) |
| 5-10 | 7807 | 0.201 | 0.1977 | +0.0033 ± 0.0008 | 0.5878 | 0.5764 | 0.4843 | 0.4106 | 0.4253 | -0.044 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6441 | 0.202 | 0.1861 | +0.0160 ± 0.0013 | 0.5907 | 0.5457 | 0.4851 | 0.3612 | 0.359 | -0.064 ± 0.0054 | -0.0281 (16) |
| 15-25 | 8159 | 0.2063 | 0.1667 | +0.0396 ± 0.0018 | 0.6046 | 0.4955 | 0.4993 | 0.3038 | 0.301 | -0.070 ± 0.0045 | -0.0043 (51) |
| 25-40 | 6277 | 0.2229 | 0.1263 | +0.0966 ± 0.0028 | 0.6402 | 0.3883 | 0.5266 | 0.213 | 0.22 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 4176 | 0.3823 | 0.0439 | +0.3384 ± 0.0037 | 0.9959 | 0.1704 | 0.6304 | 0.1014 | 0.058 | -0.076 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 824 | 0.2042 | 0.2046 | -0.0004 ± 0.0005 | 0.5889 | 0.5902 | 0.5065 | 0.4916 | 0.5146 | -0.102 ± 0.0169 | -0.0117 (6) |
| 3-5 | 587 | 0.2109 | 0.208 | +0.0029 ± 0.0015 | 0.6043 | 0.5982 | 0.5118 | 0.4722 | 0.4514 | -0.130 ± 0.0202 | 0.01 (2) |
| 5-10 | 1320 | 0.2067 | 0.2048 | +0.0019 ± 0.0019 | 0.5996 | 0.5945 | 0.54 | 0.4654 | 0.4924 | -0.088 ± 0.0129 | -0.01 (4) |
| 10-15 | 1144 | 0.2128 | 0.2071 | +0.0058 ± 0.0034 | 0.6184 | 0.5998 | 0.5635 | 0.4391 | 0.4808 | -0.099 ± 0.0141 | -0.04 (5) |
| 15-25 | 1670 | 0.2316 | 0.2123 | +0.0194 ± 0.0044 | 0.6591 | 0.6089 | 0.5848 | 0.3893 | 0.4389 | -0.099 ± 0.0115 | -0.0118 (11) |
| 25-40 | 1160 | 0.2664 | 0.1971 | +0.0693 ± 0.0082 | 0.7434 | 0.5742 | 0.6583 | 0.3442 | 0.3931 | -0.120 ± 0.013 | -0.008 (5) |
| 40+ | 417 | 0.3731 | 0.1615 | +0.2116 ± 0.0197 | 1.0168 | 0.4889 | 0.7349 | 0.2463 | 0.2878 | -0.088 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4615 | 0.1919 | 0.1921 | -0.0002 ± 0.0002 | 0.5593 | 0.5595 | 0.5072 | 0.4922 | 0.5079 | -0.040 ± 0.0066 | -0.0154 (26) |
| 3-5 | 3152 | 0.1928 | 0.1917 | +0.0011 ± 0.0006 | 0.5622 | 0.5587 | 0.5111 | 0.4714 | 0.4765 | -0.046 ± 0.008 | 0.01 (2) |
| 5-10 | 6961 | 0.197 | 0.1936 | +0.0034 ± 0.0008 | 0.579 | 0.5667 | 0.5087 | 0.4346 | 0.4512 | -0.040 ± 0.0053 | -0.0117 (6) |
| 10-15 | 5785 | 0.2025 | 0.1916 | +0.0110 ± 0.0014 | 0.5945 | 0.5602 | 0.5107 | 0.3868 | 0.4054 | -0.046 ± 0.0058 | -0.0189 (18) |
| 15-25 | 8222 | 0.217 | 0.1815 | +0.0355 ± 0.0019 | 0.6311 | 0.5323 | 0.5253 | 0.3297 | 0.3393 | -0.059 ± 0.0047 | -0.0094 (49) |
| 25-40 | 7374 | 0.2511 | 0.1369 | +0.1142 ± 0.0027 | 0.7092 | 0.4188 | 0.5595 | 0.2425 | 0.2244 | -0.081 ± 0.0043 | -0.0095 (20) |
| 40+ | 5751 | 0.4014 | 0.0585 | +0.3429 ± 0.0037 | 1.0582 | 0.2112 | 0.6539 | 0.1184 | 0.0795 | -0.074 ± 0.0031 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1004 | 0.1955 | 0.197 | -0.0015 ± 0.0005 | 0.5707 | 0.5742 | 0.5029 | 0.4875 | 0.5339 | -0.051 ± 0.0146 | -0.012 (10) |
| 3-5 | 704 | 0.2067 | 0.2051 | +0.0016 ± 0.0014 | 0.5993 | 0.594 | 0.4965 | 0.457 | 0.4588 | -0.112 ± 0.0178 | -0.0 (4) |
| 5-10 | 1563 | 0.2024 | 0.199 | +0.0035 ± 0.0017 | 0.59 | 0.5801 | 0.5121 | 0.4383 | 0.4511 | -0.104 ± 0.0117 | -0.01 (10) |
| 10-15 | 1255 | 0.2112 | 0.2018 | +0.0094 ± 0.0031 | 0.6129 | 0.5855 | 0.5366 | 0.4134 | 0.439 | -0.108 ± 0.0127 | -0.0286 (7) |
| 15-25 | 1511 | 0.2316 | 0.2125 | +0.0191 ± 0.0046 | 0.6609 | 0.6093 | 0.5857 | 0.3916 | 0.4388 | -0.109 ± 0.0119 | -0.03 (1) |
| 25-40 | 890 | 0.2125 | 0.21 | +0.0025 ± 0.009 | 0.6136 | 0.6024 | 0.6589 | 0.3481 | 0.4978 | -0.053 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5197 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.5461 | 0.547 | 0.4863 | 0.4709 | 0.4912 | -0.031 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3705 | 0.2034 | 0.2017 | +0.0018 ± 0.0006 | 0.5916 | 0.5856 | 0.4786 | 0.4391 | 0.4375 | -0.056 ± 0.0075 | -0.01 (19) |
| 5-10 | 7955 | 0.1959 | 0.1907 | +0.0052 ± 0.0007 | 0.5751 | 0.5588 | 0.4873 | 0.4133 | 0.4155 | -0.055 ± 0.0049 | -0.0117 (42) |
| 10-15 | 6402 | 0.1937 | 0.1783 | +0.0154 ± 0.0013 | 0.5722 | 0.5278 | 0.4943 | 0.371 | 0.3702 | -0.063 ± 0.0053 | -0.0136 (14) |
| 15-25 | 8256 | 0.2121 | 0.1722 | +0.0399 ± 0.0018 | 0.6182 | 0.508 | 0.5123 | 0.3177 | 0.3132 | -0.071 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6221 | 0.2167 | 0.1274 | +0.0893 ± 0.0028 | 0.6267 | 0.3903 | 0.529 | 0.2134 | 0.232 | -0.048 ± 0.0044 | -0.02 (4) |
| 40+ | 4124 | 0.3915 | 0.0489 | +0.3426 ± 0.0039 | 1.0205 | 0.1831 | 0.6399 | 0.1077 | 0.065 | -0.076 ± 0.0033 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1434 | 0.1976 | 0.1977 | -0.0000 ± 0.0004 | 0.5737 | 0.5736 | 0.5086 | 0.4936 | 0.4979 | -0.068 ± 0.012 | -0.0213 (54) |
| 3-5 | 1036 | 0.188 | 0.188 | +0.0000 ± 0.0011 | 0.554 | 0.5521 | 0.4969 | 0.457 | 0.4749 | -0.056 ± 0.0137 | -0.0194 (34) |
| 5-10 | 2085 | 0.1991 | 0.1943 | +0.0048 ± 0.0015 | 0.5874 | 0.5715 | 0.5071 | 0.4335 | 0.4384 | -0.076 ± 0.0099 | -0.005 (78) |
| 10-15 | 1438 | 0.2145 | 0.2019 | +0.0126 ± 0.0029 | 0.6226 | 0.5873 | 0.5426 | 0.4197 | 0.4284 | -0.090 ± 0.0122 | 0.0012 (66) |
| 15-25 | 1862 | 0.231 | 0.207 | +0.0240 ± 0.0042 | 0.6595 | 0.5978 | 0.5904 | 0.3955 | 0.4334 | -0.090 ± 0.0107 | -0.0214 (59) |
| 25-40 | 1123 | 0.2402 | 0.2102 | +0.0300 ± 0.0083 | 0.686 | 0.6034 | 0.6886 | 0.3765 | 0.4844 | -0.087 ± 0.0129 | -0.0252 (27) |
| 40+ | 399 | 0.3293 | 0.2007 | +0.1286 ± 0.0215 | 0.9476 | 0.585 | 0.8158 | 0.3392 | 0.4586 | -0.099 ± 0.0201 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5297 | 0.1777 | 0.1778 | -0.0002 ± 0.0002 | 0.5258 | 0.5256 | 0.5115 | 0.4963 | 0.5063 | -0.039 ± 0.0058 | -0.0145 (98) |
| 3-5 | 3672 | 0.1948 | 0.1941 | +0.0008 ± 0.0006 | 0.5685 | 0.5661 | 0.5015 | 0.4617 | 0.4722 | -0.040 ± 0.0073 | -0.0204 (72) |
| 5-10 | 7465 | 0.196 | 0.1895 | +0.0065 ± 0.0008 | 0.5787 | 0.5589 | 0.5008 | 0.4272 | 0.4213 | -0.062 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5118 | 0.2097 | 0.1934 | +0.0164 ± 0.0015 | 0.6107 | 0.5675 | 0.5373 | 0.4144 | 0.408 | -0.072 ± 0.0062 | -0.0057 (111) |
| 15-25 | 6204 | 0.2315 | 0.1997 | +0.0317 ± 0.0022 | 0.6651 | 0.5789 | 0.5763 | 0.3809 | 0.3983 | -0.068 ± 0.0057 | -0.026 (108) |
| 25-40 | 4049 | 0.2572 | 0.1902 | +0.0669 ± 0.0043 | 0.7277 | 0.554 | 0.6402 | 0.3276 | 0.3796 | -0.066 ± 0.0067 | -0.0246 (52) |
| 40+ | 1794 | 0.3728 | 0.1587 | +0.2141 ± 0.0097 | 1.0516 | 0.4732 | 0.7447 | 0.2436 | 0.291 | -0.065 ± 0.009 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 7122 | 1.029 ± 0.033 | 1.105 | 0.1689 | 0.169 | 0.2146 | 0.2035 |
| gen2 | 7122 | 0.823 ± 0.03 | 1.076 | 0.1733 | 0.1693 | 0.2331 | 0.2034 |
| gen1_elo | 7122 | 1.011 ± 0.032 | 1.093 | 0.1754 | 0.1691 | 0.2138 | 0.2036 |
| gen1_sr | 7122 | 1.008 ± 0.039 | 1.134 | 0.1333 | 0.171 | 0.2293 | 0.203 |
| gen1_ledger | 9377 | 0.866 ± 0.024 | 1.078 | 0.1898 | 0.176 | 0.2168 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 33,151)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,650 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,508 | 22.7% |
| BOOK_QUALITY | execution | 5,926 | 17.9% |
| POOR_DATA | data | 3,843 | 11.6% |
| LIMITED_DATA | data | 2,065 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,916 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 1,382 | 4.2% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,365 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 947 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 548 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.7%, execution 17.9%, data 17.8%, market_freshness/coverage 8.6%, mapping 4.2%, model_calibration_or_unknown 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.6%, LOW_DATA_QUALITY 71.5%, THIN_PLAYER_HISTORY 59.7%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.0%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.3%, EVENT_MAPPING_RISK 7.3%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 25.1%, POST_SETTLEMENT_OBSERVATION 22.7%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,596)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,011 | 34.2% |
| STALE_QUOTE | market_freshness | 3,408 | 19.4% |
| BOOK_QUALITY | execution | 3,073 | 17.5% |
| POOR_DATA | data | 1,617 | 9.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,022 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 765 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 621 | 3.5% |
| LIMITED_DATA | data | 606 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 337 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 135 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.2%, market_freshness 19.4%, execution 17.5%, data 12.6%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 74.8%, THIN_PLAYER_HISTORY 61.7%, STALE_KALSHI_QUOTE 53.5%, STALE_PLAYER_DATA 45.7%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 34.2%, WIDE_SPREAD 23.5%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, EVENT_MAPPING_RISK 8.9%, LEVEL_TRANSFER_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.1%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.2%, POST_SETTLEMENT_OBSERVATION 34.2%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 14036, "IDENTITY_AMBIGUOUS": 3560}; ticker orientation: {"VERIFIED": 17596}.

Checks: discipline:AMBIGUOUS 1189, discipline:PASS 16407, identity_confidence:AMBIGUOUS 3229, identity_confidence:PASS 14367, level_mapping:NA 1201, level_mapping:PASS 16395, market_pair:AMBIGUOUS 492, market_pair:NA 393, market_pair:PASS 16711, model_complement:NA 355, model_complement:PASS 17241, namesake:AMBIGUOUS 6, namesake:PASS 17590, physical_match_id:NA 6002, physical_match_id:PASS 11594, player_ids:PASS 17596, same_pair_other_event:PASS 17596, ticker_orientation:PASS 17596

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,291 | 3.8% | 3.2% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.52 | 0.2259 / 0.2209 (801) | 24.7% | 2.5% | 3.1% | 2.7% |
| CHALLENGER | 11,572 | 16.2% | 6.1% | 10.7% | {"coverage": 1111, "market_freshness/coverage": 220, "market_freshness": 218, "data": 157, "model_calibration_or_unknown": 78, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.37 | 0.2195 / 0.2095 (2724) | 37.9% | 15.2% | 4.1% | 22.4% |
| DOUBLES | 2,562 | 46.4% | 46.3% | 6.8% | {"execution": 665, "mapping": 343, "market_freshness": 106, "market_freshness/coverage": 68, "coverage": 7} | 23.2 | 0.2993 / 0.2322 (636) | 9.1% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 23,171 | 24.8% | 17.3% | 32.7% | {"coverage": 2016, "market_freshness": 1115, "execution": 979, "data": 844, "market_freshness/coverage": 585, "mapping": 204, "model_calibration": 6, "model_calibration_or_unknown": 3} | 11.66 | 0.2168 / 0.1989 (4910) | 39.9% | 68.8% | 15.1% | 21.5% |
| ITF_WOMEN | 30,126 | 26.4% | 18.8% | 45.1% | {"coverage": 2801, "market_freshness": 1708, "execution": 1305, "data": 1121, "market_freshness/coverage": 696, "mapping": 195, "model_calibration_or_unknown": 94, "model_calibration": 23} | 12.49 | 0.2028 / 0.1934 (5832) | 41.0% | 57.1% | 9.8% | 21.7% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,820 | 6.0% | 5.1% | 1.7% | {"market_freshness": 111, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 22, "market_freshness/coverage": 13, "mapping": 1} | 7.68 | 0.2292 / 0.22 (784) | 29.9% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.7h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 404 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 21.5h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 1296 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 311 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 14.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 852 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 20.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 1252 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 20.0h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 1203 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 5.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 344 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 902 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 2.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 163 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 439 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 32 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 7.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 463 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 11.7h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 720 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.3h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 748 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9701, "by_level_share_of_ge_25pp": {"ATP": 0.0135, "CHALLENGER": 0.1068, "DOUBLES": 0.0676, "ITF_MEN": 0.3269, "ITF_WOMEN": 0.4514, "OTHER": 0.0007, "WTA": 0.0165, "WTA125": 0.0167}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5348, "share_primary_cause_market_settled_or_in_play": 0.435, "share_primary_cause_stale_quote_only": 0.1937}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17596, "identity_ambiguous_share": 0.2023, "ticker_orientation": {"VERIFIED": 17596}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11594, "with_external": 614, "coverage": 0.053, "external_status": {"EXTERNAL_STALE": 391, "AGREES_WITH_KALSHI": 210, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 391, "MODEL_LONE_OUTLIER": 210, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.342, "share_external_supports_model": 0.0212}, "pregame_clean_ge_25pp": {"n": 5434, "with_external": 584, "coverage": 0.1075, "external_status": {"EXTERNAL_STALE": 368, "AGREES_WITH_KALSHI": 203, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 368, "MODEL_LONE_OUTLIER": 203, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3476, "share_external_supports_model": 0.0223}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 491.0, "median_sample_ratio": 2.45, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2081, "data_status": {"POOR": 9850, "LIMITED": 4577, "ADEQUATE": 3169}, "comparison_lt_10pp": {"median_thinner_serve_points": 1729.0, "median_sample_ratio": 1.7, "median_min_matches": 90.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1441, "model_minus_observed": 0.0623, "kalshi_minus_observed": -0.0765, "brier_diff_model_minus_kalshi": 0.0016}, "4-10x": {"n": 980, "model_minus_observed": 0.0891, "kalshi_minus_observed": -0.0555, "brier_diff_model_minus_kalshi": 0.0087}, "<2x": {"n": 3499, "model_minus_observed": 0.099, "kalshi_minus_observed": -0.0236, "brier_diff_model_minus_kalshi": 0.0145}, ">=10x": {"n": 1202, "model_minus_observed": 0.117, "kalshi_minus_observed": -0.0556, "brier_diff_model_minus_kalshi": 0.0148}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 7122, "model": {"intercept": -0.556, "slope": 0.823, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.182, "slope": 1.076, "slope_se": 0.034}, "mean_extremity_model": 0.1733, "mean_extremity_kalshi": 0.1693, "model_brier": 0.2331, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0297, "brier_diff_se": 0.0022, "model_logloss": 0.6636, "kalshi_logloss": 0.5891}, "fair_v1": {"n": 7122, "model": {"intercept": -0.447, "slope": 1.029, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.251, "slope": 1.105, "slope_se": 0.034}, "mean_extremity_model": 0.1689, "mean_extremity_kalshi": 0.169, "model_brier": 0.2146, "kalshi_brier": 0.2035, "brier_diff_model_minus_kalshi": 0.0111, "brier_diff_se": 0.0018, "model_logloss": 0.6183, "kalshi_logloss": 0.5893}, "gen1_elo": {"n": 7122, "model": {"intercept": -0.44, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.248, "slope": 1.093, "slope_se": 0.033}, "mean_extremity_model": 0.1754, "mean_extremity_kalshi": 0.1691, "model_brier": 0.2138, "kalshi_brier": 0.2036, "brier_diff_model_minus_kalshi": 0.0102, "brier_diff_se": 0.0018, "model_logloss": 0.617, "kalshi_logloss": 0.5895}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2471, "share_ge_15": 0.4435, "median_abs_gap": 13.03, "n": 46921}, "gen1_elo": {"share_ge_25": 0.2441, "share_ge_15": 0.4395, "median_abs_gap": 12.81, "n": 46921}, "gen1_sr": {"share_ge_25": 0.313, "share_ge_15": 0.5197, "median_abs_gap": 15.8, "n": 46921}, "gen2": {"share_ge_25": 0.3134, "share_ge_15": 0.51, "median_abs_gap": 15.45, "n": 46921}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1503, "share_ge_15": 0.3529, "median_abs_gap": 10.67, "n": 36157}, "gen1_elo": {"share_ge_25": 0.1481, "share_ge_15": 0.348, "median_abs_gap": 10.49, "n": 36157}, "gen1_sr": {"share_ge_25": 0.2156, "share_ge_15": 0.4387, "median_abs_gap": 12.97, "n": 36159}, "gen2": {"share_ge_25": 0.2302, "share_ge_15": 0.4381, "median_abs_gap": 12.83, "n": 36159}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.52, "share_ge_25_all": 0.0377, "share_ge_25_pregame_clean": 0.0325}, "WTA": {"median_abs_gap_pregame_clean": 7.68, "share_ge_25_all": 0.0604, "share_ge_25_pregame_clean": 0.0512}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.237, "share_within_10pp_all": 0.4392, "share_within_10pp_pregame_clean": 0.4923, "corr_model_vs_mid_pregame_clean": 0.8513}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1031, "model_brier": 0.1972, "kalshi_brier": 0.1976, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1234, "model_brier": 0.2185, "kalshi_brier": 0.2094, "brier_diff_model_minus_kalshi": 0.0091}, "15-25": {"n_settled": 1580, "model_brier": 0.2257, "kalshi_brier": 0.2077, "brier_diff_model_minus_kalshi": 0.018}, "25-40": {"n_settled": 900, "model_brier": 0.2227, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0175}, "3-5": {"n_settled": 658, "model_brier": 0.2047, "kalshi_brier": 0.2047, "brier_diff_model_minus_kalshi": -0.0}, "40+": {"n_settled": 186, "model_brier": 0.2966, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1217}, "5-10": {"n_settled": 1533, "model_brier": 0.2014, "kalshi_brier": 0.2004, "brier_diff_model_minus_kalshi": 0.001}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.823, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.182, "slope": 1.076, "slope_se": 0.034}, "n": 7122}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.488, "slope": 0.866, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.172, "slope": 1.078, "slope_se": 0.028}, "n": 9377}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 636, "model_brier": 0.2993, "kalshi_brier": 0.2322, "brier_diff_model_minus_kalshi": 0.0671, "brier_diff_se": 0.0117, "corr_model_outcome": 0.0975, "corr_kalshi_outcome": 0.2812}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
