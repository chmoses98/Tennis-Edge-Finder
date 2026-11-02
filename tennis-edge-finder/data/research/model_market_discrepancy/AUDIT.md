# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-02T07:24Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 73,189): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 18.9%, 25-40 13.7%, 40+ 8.0%; median gap 11.78 pp.
* **Where the extremes live**: 96.9% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.4%, Challenger 10.9%, doubles 6.9%). Main tour: ATP 3.9% and WTA 5.9% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 15,879): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, STALE_QUOTE 18.8%, BOOK_QUALITY 18.4%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.6%, IDENTITY_AMBIGUOUS 4.2%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 2.0%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, market_freshness 18.8%, execution 18.4%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 52.4% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.1% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 15,879 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.5% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.7% of the time and with the model 1.1%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1754.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.03, Gen-2 0.819, Gen-1 ledger 0.863 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 776 model 0.2204 vs Kalshi 0.2082; n 159 model 0.2822 vs Kalshi 0.1885.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 314,479 model-market comparisons (512,060 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 105,871 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-02T07:05:39.835324+00:00'], shadow board 83,722 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-02T07:05:44.814952+00:00'], Model 4 39,707 rows, 25,401 settled tickers, 9,365 tickers with an external scan.
* By model: {"gen1_ledger": 71725, "gen1_elo": 42073, "fair_v1": 42073, "gen2": 42073, "gen1_sr": 42073, "model4_fundamental": 37257, "model4_conditioned": 37205}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 73,189 | 14.1 | 9.6 | 20.2 | 15.3 | 18.9 | 13.7 | 8.0 | 11.78 | 40.6% | 21.7% |
| MW fair_v1 | 42,073 | 12.9 | 8.7 | 18.8 | 15.4 | 19.4 | 14.8 | 9.9 | 12.96 | 44.1% | 24.6% |
| MW gen1_elo | 42,073 | 12.6 | 8.8 | 19.4 | 15.4 | 19.4 | 14.7 | 9.7 | 12.8 | 43.9% | 24.4% |
| MW gen1_ledger | 31,116 | 15.8 | 10.9 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.28 | 36.0% | 17.7% |
| MW gen1_sr | 42,073 | 10.2 | 7.2 | 16.9 | 13.9 | 20.6 | 18.5 | 12.6 | 15.72 | 51.8% | 31.1% |
| MW gen2 | 42,073 | 11.1 | 7.7 | 16.6 | 13.8 | 19.4 | 17.7 | 13.7 | 15.37 | 50.8% | 31.4% |
| all families model4_conditioned | 37,205 | 22.3 | 18.1 | 34.1 | 17.2 | 5.0 | 2.1 | 1.2 | 6.05 | 8.4% | 3.4% |
| all families model4_fundamental | 37,257 | 17.3 | 13.3 | 33.8 | 20.2 | 10.1 | 3.7 | 1.5 | 7.67 | 15.3% | 5.2% |

Configurable thresholds (primary): >=5pp 76.2%, >=10pp 56.0%, >=15pp 40.6%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.7%
Executable gap (model outside the book, before fees): median 8.25pp; >=10pp 44.6%, >=25pp 16.9%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,732 | 27.6 | 15.3 | 28.2 | 13.4 | 11.1 | 3.8 | 0.6 | 5.92 | 15.4% | 4.4% |
| CHALLENGER | 6,299 | 16.2 | 9.8 | 20.7 | 15.2 | 15.8 | 11.5 | 10.8 | 10.91 | 38.1% | 22.3% |
| ITF_MEN | 11,590 | 9.8 | 7.4 | 17.0 | 14.9 | 21.2 | 17.6 | 12.1 | 15.3 | 50.8% | 29.6% |
| ITF_WOMEN | 16,473 | 9.6 | 7.1 | 16.0 | 15.1 | 22.0 | 18.1 | 12.1 | 15.69 | 52.2% | 30.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,777 | 17.6 | 13.1 | 24.7 | 20.9 | 16.0 | 6.5 | 1.1 | 8.44 | 23.7% | 7.7% |
| WTA125 | 1,196 | 16.1 | 7.2 | 22.7 | 19.6 | 20.6 | 12.1 | 1.8 | 10.7 | 34.5% | 13.9% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,732 | 26.1 | 15.8 | 26.2 | 15.7 | 11.6 | 3.8 | 0.8 | 6.19 | 16.2% | 4.6% |
| CHALLENGER | 6,299 | 15.1 | 9.1 | 18.4 | 14.1 | 18.4 | 13.4 | 11.6 | 12.49 | 43.4% | 25.0% |
| ITF_MEN | 11,590 | 8.1 | 6.2 | 15.1 | 13.8 | 19.6 | 20.7 | 16.6 | 17.94 | 56.8% | 37.3% |
| ITF_WOMEN | 16,473 | 7.9 | 5.8 | 14.0 | 12.8 | 20.6 | 21.2 | 17.7 | 19.13 | 59.5% | 38.9% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,777 | 14.9 | 10.7 | 21.9 | 15.7 | 21.9 | 12.8 | 2.3 | 10.87 | 36.9% | 15.0% |
| WTA125 | 1,196 | 9.9 | 7.0 | 16.8 | 15.9 | 24.0 | 17.8 | 8.6 | 15.14 | 50.4% | 26.4% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,732 | 22.3 | 13.7 | 25.1 | 15.8 | 15.5 | 6.3 | 1.2 | 7.47 | 23.0% | 7.5% |
| CHALLENGER | 6,299 | 15.1 | 9.4 | 20.8 | 15.8 | 15.8 | 12.1 | 11.0 | 11.33 | 38.9% | 23.1% |
| ITF_MEN | 11,590 | 9.3 | 7.2 | 17.3 | 14.2 | 21.8 | 17.7 | 12.5 | 15.8 | 52.1% | 30.2% |
| ITF_WOMEN | 16,473 | 9.3 | 6.9 | 16.4 | 15.8 | 22.1 | 18.0 | 11.4 | 15.5 | 51.5% | 29.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 2,777 | 22.8 | 16.5 | 32.0 | 14.9 | 9.1 | 3.5 | 1.1 | 6.18 | 13.7% | 4.6% |
| WTA125 | 1,196 | 20.8 | 12.9 | 26.3 | 18.5 | 15.4 | 5.8 | 0.3 | 8.06 | 21.5% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,224 | 25.4 | 19.6 | 30.9 | 12.6 | 8.5 | 2.6 | 0.5 | 5.54 | 11.7% | 3.1% |
| CHALLENGER | 4,228 | 22.5 | 14.4 | 27.3 | 14.6 | 13.7 | 6.0 | 1.6 | 7.13 | 21.2% | 7.5% |
| DOUBLES | 2,284 | 5.2 | 4.3 | 11.9 | 10.5 | 20.4 | 25.5 | 22.2 | 23.86 | 68.2% | 47.7% |
| ITF_MEN | 8,731 | 13.0 | 9.5 | 21.2 | 15.8 | 21.3 | 13.2 | 5.9 | 11.88 | 40.5% | 19.1% |
| ITF_WOMEN | 10,650 | 13.2 | 9.1 | 19.9 | 15.8 | 21.2 | 15.2 | 5.5 | 12.32 | 42.0% | 20.8% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,667 | 24.2 | 16.4 | 30.5 | 17.0 | 8.9 | 2.8 | 0.2 | 6.53 | 11.9% | 3.0% |
| WTA125 | 1,183 | 24.9 | 12.9 | 21.1 | 19.4 | 13.4 | 6.8 | 1.5 | 7.85 | 21.7% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,627 | 28.0 | 15.5 | 28.5 | 13.3 | 10.9 | 3.4 | 0.3 | 5.84 | 14.6% | 3.7% |
| CHALLENGER | 4,430 | 20.9 | 12.2 | 25.7 | 17.8 | 15.7 | 5.9 | 1.7 | 8.11 | 23.3% | 7.6% |
| ITF_MEN | 8,449 | 12.1 | 8.8 | 20.6 | 17.0 | 22.0 | 14.2 | 5.2 | 12.35 | 41.4% | 19.5% |
| ITF_WOMEN | 12,229 | 11.4 | 8.5 | 18.6 | 17.3 | 24.0 | 15.1 | 5.0 | 13.25 | 44.2% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,675 | 17.9 | 13.2 | 25.1 | 21.2 | 16.0 | 6.0 | 0.7 | 8.32 | 22.7% | 6.7% |
| WTA125 | 1,154 | 16.3 | 7.1 | 22.3 | 19.8 | 21.1 | 11.8 | 1.6 | 10.73 | 34.5% | 13.3% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,627 | 26.4 | 16.1 | 26.4 | 15.7 | 11.6 | 3.5 | 0.4 | 6.07 | 15.4% | 3.9% |
| CHALLENGER | 4,430 | 19.0 | 11.4 | 23.1 | 16.7 | 18.7 | 9.1 | 2.0 | 9.02 | 29.8% | 11.1% |
| ITF_MEN | 8,450 | 9.5 | 7.3 | 17.5 | 16.0 | 21.4 | 18.7 | 9.5 | 14.91 | 49.6% | 28.2% |
| ITF_WOMEN | 12,230 | 8.8 | 6.8 | 15.9 | 14.3 | 22.7 | 20.6 | 10.9 | 16.58 | 54.2% | 31.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,675 | 15.1 | 10.8 | 22.1 | 15.8 | 22.1 | 12.5 | 1.6 | 10.64 | 36.2% | 14.1% |
| WTA125 | 1,154 | 9.9 | 7.1 | 17.0 | 15.9 | 24.0 | 17.9 | 8.2 | 15.01 | 50.1% | 26.1% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,167 | 25.5 | 19.8 | 30.8 | 12.7 | 8.3 | 2.5 | 0.4 | 5.5 | 11.2% | 2.9% |
| CHALLENGER | 3,729 | 23.9 | 15.3 | 28.4 | 14.8 | 13.0 | 4.1 | 0.4 | 6.61 | 17.6% | 4.6% |
| DOUBLES | 2,145 | 5.1 | 4.4 | 12.1 | 10.6 | 20.2 | 25.4 | 22.2 | 23.85 | 67.8% | 47.6% |
| ITF_MEN | 7,453 | 13.8 | 10.1 | 22.9 | 16.4 | 21.2 | 11.7 | 3.8 | 10.88 | 36.8% | 15.5% |
| ITF_WOMEN | 9,104 | 13.9 | 9.6 | 21.1 | 16.4 | 21.4 | 14.2 | 3.5 | 11.52 | 39.1% | 17.7% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,607 | 24.5 | 16.9 | 30.4 | 17.1 | 8.9 | 2.2 | 0.1 | 6.37 | 11.1% | 2.2% |
| WTA125 | 1,052 | 26.1 | 13.7 | 22.1 | 20.4 | 12.4 | 4.8 | 0.5 | 7.36 | 17.7% | 5.2% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,284 | 5.2 | 4.3 | 11.9 | 10.5 | 20.4 | 25.5 | 22.2 | 23.86 | 68.2% | 47.7% |
| singles | 28,832 | 16.6 | 11.4 | 23.0 | 15.6 | 18.1 | 11.2 | 4.2 | 9.76 | 33.5% | 15.3% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 34 | 5.9 | 14.7 | 29.4 | 8.8 | 17.6 | 20.6 | 2.9 | 9.75 | 41.2% | 23.5% |
| Clay | 8,231 | 13.1 | 9.3 | 20.1 | 15.8 | 19.2 | 13.7 | 8.9 | 12.34 | 41.8% | 22.6% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 27,796 | 13.5 | 8.7 | 18.8 | 15.2 | 19.1 | 14.8 | 9.9 | 12.85 | 43.8% | 24.7% |
| UNKNOWN | 5,775 | 10.4 | 7.7 | 17.1 | 16.4 | 21.2 | 16.1 | 11.2 | 14.29 | 48.5% | 27.2% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 11,945 | 19.9 | 11.9 | 22.6 | 15.8 | 14.7 | 8.9 | 6.0 | 8.59 | 29.6% | 14.9% |
| B | 5,245 | 12.8 | 8.9 | 19.4 | 15.8 | 19.6 | 12.6 | 10.9 | 12.6 | 43.0% | 23.5% |
| C | 5,999 | 11.7 | 8.8 | 19.7 | 15.9 | 18.5 | 14.5 | 10.8 | 12.91 | 43.9% | 25.3% |
| D | 6,658 | 11.8 | 8.5 | 17.6 | 15.2 | 21.5 | 15.8 | 9.4 | 13.78 | 46.8% | 25.3% |
| F | 12,226 | 7.4 | 5.5 | 15.1 | 14.8 | 23.3 | 21.0 | 12.9 | 17.68 | 57.2% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 8,432 | 24.4 | 16.1 | 29.1 | 15.0 | 10.7 | 3.5 | 1.2 | 6.39 | 15.4% | 4.7% |
| B | 4,419 | 16.7 | 10.8 | 24.0 | 16.9 | 18.9 | 9.7 | 3.1 | 9.71 | 31.7% | 12.8% |
| C | 6,114 | 11.3 | 7.8 | 19.1 | 14.5 | 20.9 | 15.9 | 10.4 | 13.74 | 47.3% | 26.4% |
| D | 4,557 | 14.2 | 9.8 | 21.7 | 15.6 | 19.9 | 13.3 | 5.4 | 11.26 | 38.7% | 18.7% |
| F | 7,594 | 10.1 | 8.3 | 16.0 | 14.8 | 23.2 | 19.8 | 7.7 | 15.4 | 50.7% | 27.5% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 13,504 | 18.2 | 10.9 | 21.7 | 15.6 | 15.1 | 9.8 | 8.7 | 9.74 | 33.6% | 18.5% |
| LIMITED | 9,300 | 13.6 | 9.9 | 20.3 | 16.2 | 19.2 | 13.3 | 7.6 | 11.82 | 40.1% | 20.8% |
| POOR | 19,269 | 9.0 | 6.6 | 16.1 | 15.0 | 22.6 | 19.0 | 11.8 | 16.1 | 53.4% | 30.8% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,383 | 23.9 | 17.8 | 33.1 | 15.7 | 6.4 | 2.7 | 0.4 | 5.91 | 9.4% | 3.1% |
| GAME_SPREAD | 6,304 | 22.2 | 15.1 | 32.6 | 17.0 | 9.1 | 3.4 | 0.6 | 6.76 | 13.1% | 4.0% |
| MATCH_WINNER | 31,116 | 15.8 | 10.9 | 22.1 | 15.2 | 18.3 | 12.2 | 5.5 | 10.28 | 36.0% | 17.7% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 15,382 | 27.7 | 16.7 | 30.7 | 12.8 | 9.4 | 2.5 | 0.3 | 5.66 | 12.2% | 2.8% |
| TOTAL_GAMES | 10,516 | 9.8 | 10.7 | 35.4 | 26.4 | 10.6 | 4.2 | 3.0 | 9.27 | 17.8% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,331 | 24.4 | 29.0 | 33.2 | 8.1 | 4.0 | 0.9 | 0.3 | 4.79 | 5.2% | 1.2% |
| GAME_SPREAD | 8,619 | 46.7 | 16.1 | 25.1 | 7.4 | 2.2 | 1.8 | 0.6 | 3.31 | 4.7% | 2.5% |
| TOTAL_GAMES | 15,255 | 6.6 | 9.6 | 40.0 | 30.6 | 7.4 | 3.3 | 2.4 | 9.28 | 13.2% | 5.8% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 13,350 | 23.9 | 16.6 | 34.8 | 14.8 | 6.9 | 2.5 | 0.4 | 6.06 | 9.9% | 3.0% |
| GAME_SPREAD | 8,622 | 20.1 | 13.5 | 28.2 | 20.2 | 12.2 | 4.5 | 1.1 | 7.75 | 17.9% | 5.7% |
| TOTAL_GAMES | 15,285 | 10.0 | 10.4 | 36.1 | 24.9 | 11.6 | 4.4 | 2.6 | 9.16 | 18.6% | 7.0% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 42,073 | 44.1% | 24.6% | 12.96 | 35.2% | 15.1% | 10.65 |
| gen1_elo | 42,073 | 43.9% | 24.4% | 12.8 | 34.9% | 15.1% | 10.5 |
| gen1_sr | 42,073 | 51.8% | 31.1% | 15.72 | 43.7% | 21.5% | 12.92 |
| gen2 | 42,073 | 50.8% | 31.4% | 15.37 | 43.7% | 23.1% | 12.79 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,120 | 15.6 | 10.5 | 21.4 | 17.3 | 20.0 | 11.9 | 3.3 | 10.68 | 35.2% | 15.2% |
| STALE | 22,953 | 10.8 | 7.2 | 16.7 | 13.9 | 19.0 | 17.2 | 15.3 | 15.58 | 51.4% | 32.5% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 24,584 | 16.5 | 11.2 | 22.8 | 15.3 | 17.7 | 11.7 | 4.8 | 9.86 | 34.2% | 16.5% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 73,189 | 24584 | 22592 | 26013 | 24.4 | 123.5 | 1451.1 |
| ge_15pp | 29,750 | 8405 | 8025 | 13320 | 27.2 | 435.1 | 1451.1 |
| ge_25pp | 15,879 | 4055 | 3496 | 8328 | 31.9 | 586.7 | 1431.1 |
| lt_10pp | 32,210 | 12409 | 10712 | 9089 | 22.6 | 46.9 | 1421.1 |

Current slate `SL-20261102T072359Z-7b5daa51`: 817 priced rows, quote age at build {'median': 18.7, 'max': 18.8}, freshness {'AGING': 817}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 48 | 0.0 | 0.0 | 35.4 | 6.2 | 33.3 | 20.8 | 4.2 | 19.13 | 58.3% | 25.0% |
| EXTERNAL_LONE_OUTLIER | 25 | 64.0 | 36.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.43 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,148 | 19.5 | 10.9 | 25.3 | 18.2 | 17.9 | 7.2 | 0.9 | 8.71 | 26.1% | 8.2% |
| KALSHI_LONE_OUTLIER | 27 | 3.7 | 3.7 | 77.8 | 7.4 | 3.7 | 3.7 | 0.0 | 6.42 | 7.4% | 3.7% |
| MARKETS_AGREE | 860 | 66.4 | 33.6 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.2 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 1,862 | 0.0 | 2.3 | 37.1 | 26.0 | 24.2 | 9.6 | 0.9 | 11.87 | 34.6% | 10.4% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 42,073 | 6970 (16.6%) | 26.7% | 1.1% | {"EXTERNAL_STALE": 4148, "AGREES_WITH_KALSHI": 1862, "ALL_AGREE": 860, "SUPPORTS_MODEL_DIRECTION": 47, "AGREES_WITH_MODEL": 27, "EXTERNAL_OUTLIER": 25, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 18,546 | 1756 (9.5%) | 36.7% | 1.7% | {"EXTERNAL_STALE": 1082, "AGREES_WITH_KALSHI": 644, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 10,362 | 545 (5.3%) | 35.6% | 2.4% | {"EXTERNAL_STALE": 338, "AGREES_WITH_KALSHI": 194, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 4,912 | 518 (10.5%) | 36.1% | 2.5% | {"EXTERNAL_STALE": 318, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 17,032 | 3970 (23.3%) | 18.5% | 1.0% | {"EXTERNAL_STALE": 2311, "ALL_AGREE": 860, "AGREES_WITH_KALSHI": 734, "EXTERNAL_OUTLIER": 25, "AGREES_WITH_MODEL": 23, "SUPPORTS_MODEL_DIRECTION": 16, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 8,147 | 10.4 | 7.6 | 19.4 | 14.5 | 21.6 | 16.4 | 10.0 | 14.11 | 48.1% | 26.5% |
| 4-10x | 5,637 | 11.1 | 8.6 | 18.7 | 15.4 | 22.0 | 14.2 | 10.1 | 13.67 | 46.3% | 24.3% |
| <2x | 21,576 | 15.2 | 9.9 | 19.8 | 16.1 | 17.3 | 12.9 | 8.8 | 11.47 | 39.1% | 21.8% |
| >=10x | 6,713 | 10.5 | 6.4 | 15.1 | 14.5 | 21.7 | 19.1 | 12.8 | 16.29 | 53.5% | 31.9% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 10,986 | 12.6 | 8.8 | 19.7 | 16.1 | 19.1 | 13.4 | 10.3 | 12.7 | 42.9% | 23.7% |
| 300-1000 | 9,031 | 11.9 | 8.8 | 17.8 | 15.3 | 20.3 | 16.4 | 9.6 | 13.6 | 46.3% | 26.0% |
| <300 | 13,269 | 8.2 | 5.8 | 15.2 | 14.8 | 23.1 | 19.9 | 12.9 | 17.06 | 55.9% | 32.9% |
| >=3000 | 8,787 | 21.6 | 12.9 | 24.2 | 15.7 | 13.6 | 7.0 | 5.0 | 7.59 | 25.5% | 11.9% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1217 | 0.5513 | 0.4121 | 0.4979 | +0.053 | -0.086 | -0.0029 ± 0.0044 |
| ratio 4-10x | 838 | 0.5838 | 0.4377 | 0.4988 | +0.085 | -0.061 | 0.0072 ± 0.0055 |
| ratio <2x | 2991 | 0.5376 | 0.4157 | 0.4443 | +0.093 | -0.029 | 0.0126 ± 0.0026 |
| ratio >=10x | 1035 | 0.5691 | 0.3951 | 0.4522 | +0.117 | -0.057 | 0.0134 ± 0.0056 |
| thinner_sample 1000-3000 | 1695 | 0.5393 | 0.4129 | 0.4525 | +0.087 | -0.040 | 0.0089 ± 0.0035 |
| thinner_sample 300-1000 | 1373 | 0.5694 | 0.4279 | 0.4858 | +0.084 | -0.058 | 0.0031 ± 0.0043 |
| thinner_sample <300 | 1983 | 0.5617 | 0.394 | 0.4624 | +0.099 | -0.068 | 0.01 ± 0.004 |
| thinner_sample >=3000 | 1030 | 0.5314 | 0.4386 | 0.4563 | +0.075 | -0.018 | 0.0142 ± 0.0035 |
| data_status ADEQUATE | 1684 | 0.5334 | 0.4314 | 0.4471 | +0.086 | -0.016 | 0.013 ± 0.003 |
| data_status LIMITED | 1498 | 0.5497 | 0.4171 | 0.472 | +0.078 | -0.055 | 0.0068 ± 0.0039 |
| data_status POOR | 2899 | 0.5641 | 0.4033 | 0.4695 | +0.095 | -0.066 | 0.0075 ± 0.0032 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 891 | 0.2004 | 0.2008 | -0.0004 ± 0.0005 | 0.5812 | 0.5824 | 0.5042 | 0.489 | 0.5084 | -0.088 ± 0.0159 | -0.0087 (8) |
| 3-5 | 555 | 0.2052 | 0.2048 | +0.0004 ± 0.0016 | 0.5939 | 0.591 | 0.5049 | 0.4651 | 0.4793 | -0.105 ± 0.0197 | 0.01 (2) |
| 5-10 | 1300 | 0.2005 | 0.2003 | +0.0002 ± 0.0019 | 0.5868 | 0.5841 | 0.5111 | 0.4373 | 0.4708 | -0.088 ± 0.0129 | -0.0143 (7) |
| 10-15 | 1051 | 0.2194 | 0.2107 | +0.0086 ± 0.0035 | 0.6308 | 0.6064 | 0.529 | 0.4055 | 0.431 | -0.106 ± 0.0143 | -0.048 (5) |
| 15-25 | 1349 | 0.2249 | 0.2098 | +0.0151 ± 0.0049 | 0.645 | 0.6032 | 0.5776 | 0.3823 | 0.4418 | -0.102 ± 0.0125 | -0.004 (10) |
| 25-40 | 776 | 0.2204 | 0.2082 | +0.0123 ± 0.0098 | 0.6298 | 0.5988 | 0.6581 | 0.3479 | 0.4832 | -0.069 ± 0.0149 | -0.06 (2) |
| 40+ | 159 | 0.2822 | 0.1885 | +0.0938 ± 0.03 | 0.7687 | 0.5556 | 0.7384 | 0.2904 | 0.4151 | -0.073 ± 0.0297 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4800 | 0.1853 | 0.1862 | -0.0009 ± 0.0002 | 0.5461 | 0.547 | 0.4879 | 0.4727 | 0.5031 | -0.022 ± 0.0063 | -0.01 (28) |
| 3-5 | 3214 | 0.1948 | 0.1928 | +0.0020 ± 0.0006 | 0.5682 | 0.561 | 0.4824 | 0.4426 | 0.4362 | -0.061 ± 0.0078 | 0.0 (3) |
| 5-10 | 6928 | 0.2008 | 0.1973 | +0.0035 ± 0.0008 | 0.5871 | 0.5754 | 0.4849 | 0.4114 | 0.4249 | -0.046 ± 0.0054 | -0.0114 (22) |
| 10-15 | 5695 | 0.2013 | 0.1855 | +0.0158 ± 0.0014 | 0.5887 | 0.5454 | 0.4851 | 0.3612 | 0.3587 | -0.065 ± 0.0057 | -0.0281 (16) |
| 15-25 | 7140 | 0.2066 | 0.1679 | +0.0387 ± 0.0019 | 0.6057 | 0.4983 | 0.5003 | 0.3046 | 0.3045 | -0.070 ± 0.0048 | -0.0027 (45) |
| 25-40 | 5554 | 0.2212 | 0.1258 | +0.0954 ± 0.003 | 0.6365 | 0.3868 | 0.5264 | 0.2123 | 0.2218 | -0.058 ± 0.0046 | -0.0733 (3) |
| 40+ | 3684 | 0.3836 | 0.045 | +0.3386 ± 0.004 | 0.9995 | 0.1737 | 0.6328 | 0.104 | 0.0605 | -0.077 ± 0.0033 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 708 | 0.2079 | 0.2084 | -0.0006 ± 0.0006 | 0.5983 | 0.5999 | 0.5058 | 0.491 | 0.5212 | -0.099 ± 0.0186 | -0.0117 (6) |
| 3-5 | 502 | 0.216 | 0.2135 | +0.0025 ± 0.0016 | 0.6147 | 0.61 | 0.5156 | 0.476 | 0.4602 | -0.127 ± 0.0222 | 0.01 (2) |
| 5-10 | 1127 | 0.2067 | 0.2043 | +0.0024 ± 0.002 | 0.6 | 0.593 | 0.5424 | 0.4676 | 0.4916 | -0.096 ± 0.0139 | -0.01 (4) |
| 10-15 | 976 | 0.2145 | 0.2097 | +0.0048 ± 0.0037 | 0.6194 | 0.6061 | 0.5657 | 0.4414 | 0.4877 | -0.098 ± 0.0153 | -0.04 (5) |
| 15-25 | 1415 | 0.2287 | 0.2123 | +0.0165 ± 0.0048 | 0.6517 | 0.6089 | 0.5835 | 0.3882 | 0.4459 | -0.096 ± 0.0124 | -0.012 (10) |
| 25-40 | 995 | 0.2679 | 0.1998 | +0.0681 ± 0.0089 | 0.748 | 0.5807 | 0.6621 | 0.3485 | 0.399 | -0.127 ± 0.0141 | -0.008 (5) |
| 40+ | 358 | 0.3652 | 0.1654 | +0.1998 ± 0.0213 | 0.9991 | 0.4981 | 0.7333 | 0.2486 | 0.2989 | -0.084 ± 0.0208 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4123 | 0.1918 | 0.192 | -0.0002 ± 0.0002 | 0.5595 | 0.5596 | 0.5078 | 0.4927 | 0.5096 | -0.040 ± 0.0071 | -0.0154 (26) |
| 3-5 | 2814 | 0.194 | 0.1928 | +0.0012 ± 0.0007 | 0.5643 | 0.5606 | 0.5111 | 0.4714 | 0.4748 | -0.049 ± 0.0085 | 0.01 (2) |
| 5-10 | 6151 | 0.198 | 0.1944 | +0.0036 ± 0.0008 | 0.581 | 0.5679 | 0.5094 | 0.4354 | 0.4508 | -0.043 ± 0.0057 | -0.0117 (6) |
| 10-15 | 5113 | 0.2029 | 0.1915 | +0.0113 ± 0.0015 | 0.5948 | 0.5606 | 0.5122 | 0.3884 | 0.4056 | -0.049 ± 0.0062 | -0.0189 (18) |
| 15-25 | 7170 | 0.2166 | 0.1805 | +0.0361 ± 0.002 | 0.6302 | 0.5299 | 0.5227 | 0.3274 | 0.3357 | -0.062 ± 0.005 | -0.0084 (43) |
| 25-40 | 6532 | 0.2508 | 0.1368 | +0.1141 ± 0.0029 | 0.7081 | 0.4185 | 0.5586 | 0.242 | 0.2238 | -0.083 ± 0.0046 | -0.0095 (20) |
| 40+ | 5112 | 0.3998 | 0.0588 | +0.3410 ± 0.0039 | 1.0548 | 0.2118 | 0.6536 | 0.1182 | 0.0812 | -0.073 ± 0.0033 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 847 | 0.1953 | 0.1973 | -0.0020 ± 0.0005 | 0.5699 | 0.575 | 0.5022 | 0.4868 | 0.5443 | -0.040 ± 0.0159 | -0.012 (10) |
| 3-5 | 596 | 0.2071 | 0.205 | +0.0021 ± 0.0015 | 0.5993 | 0.5922 | 0.4976 | 0.4579 | 0.453 | -0.121 ± 0.0193 | -0.0 (4) |
| 5-10 | 1337 | 0.2023 | 0.1993 | +0.0030 ± 0.0018 | 0.5897 | 0.5808 | 0.5112 | 0.4375 | 0.4533 | -0.102 ± 0.0126 | -0.01 (9) |
| 10-15 | 1062 | 0.2088 | 0.2031 | +0.0057 ± 0.0034 | 0.6072 | 0.5894 | 0.5422 | 0.4188 | 0.4586 | -0.099 ± 0.0138 | -0.0286 (7) |
| 15-25 | 1278 | 0.2343 | 0.2161 | +0.0183 ± 0.0051 | 0.6674 | 0.617 | 0.591 | 0.3966 | 0.4468 | -0.112 ± 0.013 | -0.03 (1) |
| 25-40 | 793 | 0.2111 | 0.2134 | -0.0024 ± 0.0096 | 0.6097 | 0.6113 | 0.6656 | 0.3551 | 0.512 | -0.055 ± 0.0147 | -0.0267 (3) |
| 40+ | 168 | 0.3002 | 0.1961 | +0.1040 ± 0.0301 | 0.8181 | 0.5732 | 0.7497 | 0.3001 | 0.4167 | -0.080 ± 0.0314 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4590 | 0.184 | 0.1847 | -0.0007 ± 0.0002 | 0.5421 | 0.5433 | 0.483 | 0.4677 | 0.4891 | -0.030 ± 0.0064 | -0.0137 (41) |
| 3-5 | 3216 | 0.2019 | 0.1996 | +0.0023 ± 0.0006 | 0.5871 | 0.5795 | 0.4799 | 0.4404 | 0.4316 | -0.064 ± 0.008 | -0.01 (19) |
| 5-10 | 7070 | 0.1936 | 0.189 | +0.0046 ± 0.0008 | 0.5699 | 0.555 | 0.4871 | 0.4131 | 0.4198 | -0.051 ± 0.0052 | -0.0105 (37) |
| 10-15 | 5661 | 0.1922 | 0.1787 | +0.0135 ± 0.0014 | 0.5686 | 0.5292 | 0.496 | 0.3726 | 0.3787 | -0.057 ± 0.0056 | -0.0146 (13) |
| 15-25 | 7272 | 0.2135 | 0.1738 | +0.0397 ± 0.0019 | 0.6213 | 0.5116 | 0.5148 | 0.3202 | 0.317 | -0.072 ± 0.0049 | -0.0533 (3) |
| 25-40 | 5564 | 0.2163 | 0.1286 | +0.0878 ± 0.003 | 0.6258 | 0.3931 | 0.5297 | 0.2141 | 0.2351 | -0.048 ± 0.0046 | -0.02 (4) |
| 40+ | 3642 | 0.3936 | 0.0506 | +0.3430 ± 0.0042 | 1.0264 | 0.188 | 0.6426 | 0.1108 | 0.0675 | -0.077 ± 0.0036 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1265 | 0.195 | 0.195 | -0.0000 ± 0.0004 | 0.5681 | 0.5681 | 0.506 | 0.4909 | 0.4941 | -0.070 ± 0.0127 | -0.0213 (54) |
| 3-5 | 894 | 0.1887 | 0.1885 | +0.0002 ± 0.0012 | 0.5538 | 0.5521 | 0.4969 | 0.4571 | 0.4732 | -0.060 ± 0.0148 | -0.0194 (34) |
| 5-10 | 1851 | 0.2013 | 0.1967 | +0.0047 ± 0.0016 | 0.5916 | 0.5767 | 0.505 | 0.4313 | 0.4371 | -0.076 ± 0.0106 | -0.005 (78) |
| 10-15 | 1262 | 0.2166 | 0.2035 | +0.0131 ± 0.0032 | 0.6253 | 0.591 | 0.5399 | 0.4171 | 0.4239 | -0.090 ± 0.0131 | 0.0014 (65) |
| 15-25 | 1631 | 0.2304 | 0.2089 | +0.0215 ± 0.0044 | 0.657 | 0.6022 | 0.5864 | 0.3916 | 0.4365 | -0.085 ± 0.0114 | -0.0214 (59) |
| 25-40 | 1017 | 0.2415 | 0.2114 | +0.0302 ± 0.0088 | 0.6907 | 0.6057 | 0.6883 | 0.3761 | 0.4838 | -0.091 ± 0.0135 | -0.0252 (27) |
| 40+ | 343 | 0.3302 | 0.2055 | +0.1247 ± 0.0235 | 0.9594 | 0.5968 | 0.8206 | 0.344 | 0.4665 | -0.099 ± 0.022 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4750 | 0.1753 | 0.1756 | -0.0002 ± 0.0002 | 0.5198 | 0.5199 | 0.5107 | 0.4955 | 0.508 | -0.037 ± 0.0061 | -0.0145 (98) |
| 3-5 | 3275 | 0.1943 | 0.1933 | +0.0010 ± 0.0006 | 0.5664 | 0.5641 | 0.503 | 0.4633 | 0.4708 | -0.043 ± 0.0078 | -0.0204 (72) |
| 5-10 | 6692 | 0.198 | 0.1914 | +0.0066 ± 0.0008 | 0.5822 | 0.563 | 0.5008 | 0.4271 | 0.421 | -0.063 ± 0.0054 | -0.0084 (134) |
| 10-15 | 4611 | 0.2111 | 0.1952 | +0.0158 ± 0.0016 | 0.6127 | 0.5719 | 0.5378 | 0.4149 | 0.4108 | -0.070 ± 0.0066 | -0.0053 (106) |
| 15-25 | 5556 | 0.2299 | 0.2004 | +0.0295 ± 0.0024 | 0.6611 | 0.5803 | 0.5732 | 0.3778 | 0.4014 | -0.064 ± 0.0061 | -0.026 (108) |
| 25-40 | 3722 | 0.2591 | 0.1887 | +0.0703 ± 0.0045 | 0.7331 | 0.5504 | 0.6383 | 0.3257 | 0.3718 | -0.074 ± 0.007 | -0.0246 (52) |
| 40+ | 1601 | 0.3746 | 0.1577 | +0.2169 ± 0.0103 | 1.0613 | 0.4692 | 0.7448 | 0.2425 | 0.2879 | -0.069 ± 0.0094 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6081 | 1.03 ± 0.036 | 1.101 | 0.1695 | 0.1659 | 0.2143 | 0.2054 |
| gen2 | 6081 | 0.819 ± 0.033 | 1.07 | 0.172 | 0.1663 | 0.2333 | 0.2052 |
| gen1_elo | 6081 | 1.005 ± 0.035 | 1.093 | 0.1764 | 0.166 | 0.2135 | 0.2055 |
| gen1_sr | 6081 | 1.007 ± 0.043 | 1.13 | 0.1322 | 0.1681 | 0.2295 | 0.2049 |
| gen1_ledger | 8263 | 0.863 ± 0.026 | 1.069 | 0.1886 | 0.1749 | 0.2174 | 0.2012 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 29,750)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 6,689 | 22.5% |
| STALE_QUOTE | market_freshness | 6,624 | 22.3% |
| BOOK_QUALITY | execution | 5,595 | 18.8% |
| POOR_DATA | data | 3,441 | 11.6% |
| LIMITED_DATA | data | 1,868 | 6.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,689 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,263 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,221 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 851 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 508 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 22.5%, market_freshness 22.3%, execution 18.8%, data 17.8%, market_freshness/coverage 8.5%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.4%, START_UNVERIFIABLE 94.3%, LOW_DATA_QUALITY 71.4%, THIN_PLAYER_HISTORY 59.8%, STALE_PLAYER_DATA 52.0%, STALE_KALSHI_QUOTE 44.8%, MODEL_INTERNAL_DISAGREEMENT 42.1%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.9%, MODEL_HIGH_UNCERTAINTY 18.4%, PLAYER_IDENTITY_RISK 15.6%, LEVEL_TRANSFER_RISK 10.3%, LOW_DISPLAYED_LIQUIDITY 8.1%, EVENT_MAPPING_RISK 7.5%, MODEL_CALIBRATION_OUTLIER 3.8%, EXTERNAL_MARKET_REJECTION 3.4%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.9%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 15,879)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,400 | 34.0% |
| STALE_QUOTE | market_freshness | 2,988 | 18.8% |
| BOOK_QUALITY | execution | 2,925 | 18.4% |
| POOR_DATA | data | 1,476 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 887 | 5.6% |
| IDENTITY_AMBIGUOUS | mapping | 664 | 4.2% |
| IN_PLAY_QUOTE | market_freshness/coverage | 554 | 3.5% |
| LIMITED_DATA | data | 546 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 313 | 2.0% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 125 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, market_freshness 18.8%, execution 18.4%, data 12.7%, market_freshness/coverage 9.1%, mapping 4.2%, model_calibration_or_unknown 2.0%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 97.9%, START_UNVERIFIABLE 96.9%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 52.4%, STALE_PLAYER_DATA 46.0%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.1%, WIDE_SPREAD 24.4%, MODEL_HIGH_UNCERTAINTY 19.1%, PLAYER_IDENTITY_RISK 18.5%, EVENT_MAPPING_RISK 9.2%, LEVEL_TRANSFER_RISK 9.2%, LOW_DISPLAYED_LIQUIDITY 8.0%, MODEL_CALIBRATION_OUTLIER 5.1%, EXTERNAL_MARKET_REJECTION 2.0%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 6.0%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 12616, "IDENTITY_AMBIGUOUS": 3263}; ticker orientation: {"VERIFIED": 15879}.

Checks: discipline:AMBIGUOUS 1090, discipline:PASS 14789, identity_confidence:AMBIGUOUS 2939, identity_confidence:PASS 12940, level_mapping:NA 1102, level_mapping:PASS 14777, market_pair:AMBIGUOUS 483, market_pair:NA 354, market_pair:PASS 15042, model_complement:NA 317, model_complement:PASS 15562, namesake:AMBIGUOUS 6, namesake:PASS 15873, physical_match_id:NA 5517, physical_match_id:PASS 10362, player_ids:PASS 15879, same_pair_other_event:PASS 15879, ticker_orientation:PASS 15879

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 5,956 | 3.9% | 3.4% | 1.5% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 24, "market_freshness/coverage": 17, "coverage": 17} | 5.67 | 0.2219 / 0.216 (705) | 23.7% | 2.6% | 3.1% | 2.7% |
| CHALLENGER | 10,527 | 16.4% | 6.2% | 10.9% | {"coverage": 1011, "market_freshness/coverage": 207, "market_freshness": 183, "data": 154, "model_calibration_or_unknown": 75, "execution": 42, "model_calibration": 35, "mapping": 17, "possible_market_error": 1} | 7.33 | 0.2204 / 0.2095 (2449) | 36.1% | 16.0% | 4.2% | 22.5% |
| DOUBLES | 2,284 | 47.7% | 47.6% | 6.9% | {"execution": 621, "mapping": 295, "market_freshness": 106, "market_freshness/coverage": 61, "coverage": 7} | 23.85 | 0.3069 / 0.2391 (543) | 10.2% | 0.0% | 100.0% | 6.1% |
| ITF_MEN | 20,321 | 25.1% | 17.6% | 32.1% | {"coverage": 1807, "market_freshness": 938, "execution": 924, "data": 748, "market_freshness/coverage": 493, "mapping": 184, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.68 | 0.2163 / 0.2004 (4196) | 38.3% | 68.9% | 16.2% | 21.8% |
| ITF_WOMEN | 27,123 | 26.5% | 19.1% | 45.3% | {"coverage": 2506, "market_freshness": 1533, "execution": 1256, "data": 1022, "market_freshness/coverage": 609, "mapping": 162, "model_calibration_or_unknown": 82, "model_calibration": 21} | 12.54 | 0.2026 / 0.1951 (5020) | 40.0% | 57.1% | 9.9% | 21.3% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,444 | 5.9% | 5.0% | 1.7% | {"market_freshness": 94, "model_calibration_or_unknown": 47, "coverage": 37, "execution": 29, "data": 24, "model_calibration": 19, "market_freshness/coverage": 12, "mapping": 1} | 7.59 | 0.2296 / 0.2241 (681) | 28.5% | 1.8% | 1.4% | 3.6% |
| WTA125 | 2,379 | 11.1% | 9.5% | 1.7% | {"market_freshness": 75, "model_calibration_or_unknown": 52, "market_freshness/coverage": 41, "data": 38, "execution": 24, "model_calibration": 16, "coverage": 14, "mapping": 4} | 9.21 | 0.2104 / 0.1933 (708) | 27.1% | 10.8% | 4.5% | 7.3% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.4h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 509 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 3 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 4 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 590 min (STALE); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 5 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 11.0h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 667 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 6 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 228 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 7 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 8 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 572 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 9 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 10 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 11 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 12 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 14.9h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 899 min (STALE); no external reference |
| 13 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 14 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 15 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 16 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 17.1h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 1037 min (STALE); no external reference |
| 17 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 18 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.1h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 250 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 19 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 20 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 21 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.8h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 56 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 22 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 23 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 24 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 25 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 26 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 126 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 27 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 28 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 29 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 30 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 31 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 34 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 32 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 33 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 34 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 35 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.2h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 315 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 36 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 37 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 38 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 39 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 40 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 41 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 42 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 43 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 44 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.0h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 379 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 45 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.7h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 589 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 46 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |
| 47 | `KXATPDOUBLES-26OCT09DARETCCASGLA-DARETC` | DOUBLES | gen1_ledger | 96% / 18% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFMATCH-26OCT15SURREJ-SUR` | ITF_MEN | fair_v1 | 86% / 8% | +78 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 155 min (STALE); data POOR (grade D, thinner serve sample 131.0, ratio 9.45); no external reference |
| 49 | `KXATPCHALLENGERDOUBLES-26OCT07REYWATKASMAE-KASMAE` | DOUBLES | gen1_ledger | 91% / 12% | +78 | IDENTITY_AMBIGUOUS | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 50 | `KXITFWMATCH-26OCT31KUHDEK-KUH` | ITF_WOMEN | fair_v1 | 84% / 6% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 224 min (STALE); data LIMITED (grade C, thinner serve sample 1253.0, ratio 1.41); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9688, "by_level_share_of_ge_25pp": {"ATP": 0.0146, "CHALLENGER": 0.1086, "DOUBLES": 0.0686, "ITF_MEN": 0.3213, "ITF_WOMEN": 0.4529, "OTHER": 0.0008, "WTA": 0.0166, "WTA125": 0.0166}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5245, "share_primary_cause_market_settled_or_in_play": 0.4309, "share_primary_cause_stale_quote_only": 0.1882}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 15879, "identity_ambiguous_share": 0.2055, "ticker_orientation": {"VERIFIED": 15879}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 10362, "with_external": 545, "coverage": 0.0526, "external_status": {"EXTERNAL_STALE": 338, "AGREES_WITH_KALSHI": 194, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 338, "MODEL_LONE_OUTLIER": 194, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.356, "share_external_supports_model": 0.0239}, "pregame_clean_ge_25pp": {"n": 4912, "with_external": 518, "coverage": 0.1055, "external_status": {"EXTERNAL_STALE": 318, "AGREES_WITH_KALSHI": 187, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 318, "MODEL_LONE_OUTLIER": 187, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.361, "share_external_supports_model": 0.0251}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.47, "median_min_matches": 19.0, "median_max_days_since_last": 238.0, "share_severe_asymmetry": 0.2069, "data_status": {"POOR": 8907, "LIMITED": 4171, "ADEQUATE": 2801}, "comparison_lt_10pp": {"median_thinner_serve_points": 1754.0, "median_sample_ratio": 1.69, "median_min_matches": 92.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1217, "model_minus_observed": 0.0533, "kalshi_minus_observed": -0.0859, "brier_diff_model_minus_kalshi": -0.0029}, "4-10x": {"n": 838, "model_minus_observed": 0.085, "kalshi_minus_observed": -0.0612, "brier_diff_model_minus_kalshi": 0.0072}, "<2x": {"n": 2991, "model_minus_observed": 0.0933, "kalshi_minus_observed": -0.0287, "brier_diff_model_minus_kalshi": 0.0126}, ">=10x": {"n": 1035, "model_minus_observed": 0.1169, "kalshi_minus_observed": -0.0571, "brier_diff_model_minus_kalshi": 0.0134}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6081, "model": {"intercept": -0.534, "slope": 0.819, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.196, "slope": 1.07, "slope_se": 0.037}, "mean_extremity_model": 0.172, "mean_extremity_kalshi": 0.1663, "model_brier": 0.2333, "kalshi_brier": 0.2052, "brier_diff_model_minus_kalshi": 0.0281, "brier_diff_se": 0.0024, "model_logloss": 0.6639, "kalshi_logloss": 0.5934}, "fair_v1": {"n": 6081, "model": {"intercept": -0.425, "slope": 1.03, "slope_se": 0.036}, "kalshi_mid_same_rows": {"intercept": 0.272, "slope": 1.101, "slope_se": 0.037}, "mean_extremity_model": 0.1695, "mean_extremity_kalshi": 0.1659, "model_brier": 0.2143, "kalshi_brier": 0.2054, "brier_diff_model_minus_kalshi": 0.0089, "brier_diff_se": 0.002, "model_logloss": 0.6174, "kalshi_logloss": 0.5937}, "gen1_elo": {"n": 6081, "model": {"intercept": -0.411, "slope": 1.005, "slope_se": 0.035}, "kalshi_mid_same_rows": {"intercept": 0.28, "slope": 1.093, "slope_se": 0.036}, "mean_extremity_model": 0.1764, "mean_extremity_kalshi": 0.166, "model_brier": 0.2135, "kalshi_brier": 0.2055, "brier_diff_model_minus_kalshi": 0.008, "brier_diff_se": 0.002, "model_logloss": 0.6162, "kalshi_logloss": 0.594}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2463, "share_ge_15": 0.4408, "median_abs_gap": 12.96, "n": 42073}, "gen1_elo": {"share_ge_25": 0.2445, "share_ge_15": 0.439, "median_abs_gap": 12.8, "n": 42073}, "gen1_sr": {"share_ge_25": 0.3114, "share_ge_15": 0.5176, "median_abs_gap": 15.72, "n": 42073}, "gen2": {"share_ge_25": 0.314, "share_ge_15": 0.5077, "median_abs_gap": 15.37, "n": 42073}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.1508, "share_ge_15": 0.3523, "median_abs_gap": 10.65, "n": 32570}, "gen1_elo": {"share_ge_25": 0.1506, "share_ge_15": 0.3495, "median_abs_gap": 10.5, "n": 32569}, "gen1_sr": {"share_ge_25": 0.2153, "share_ge_15": 0.4373, "median_abs_gap": 12.92, "n": 32572}, "gen2": {"share_ge_25": 0.2314, "share_ge_15": 0.4373, "median_abs_gap": 12.79, "n": 32572}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.67, "share_ge_25_all": 0.039, "share_ge_25_pregame_clean": 0.0342}, "WTA": {"median_abs_gap_pregame_clean": 7.59, "share_ge_25_all": 0.0592, "share_ge_25_pregame_clean": 0.05}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2377, "share_within_10pp_all": 0.4401, "share_within_10pp_pregame_clean": 0.4927, "corr_model_vs_mid_pregame_clean": 0.8507}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 891, "model_brier": 0.2004, "kalshi_brier": 0.2008, "brier_diff_model_minus_kalshi": -0.0004}, "10-15": {"n_settled": 1051, "model_brier": 0.2194, "kalshi_brier": 0.2107, "brier_diff_model_minus_kalshi": 0.0086}, "15-25": {"n_settled": 1349, "model_brier": 0.2249, "kalshi_brier": 0.2098, "brier_diff_model_minus_kalshi": 0.0151}, "25-40": {"n_settled": 776, "model_brier": 0.2204, "kalshi_brier": 0.2082, "brier_diff_model_minus_kalshi": 0.0123}, "3-5": {"n_settled": 555, "model_brier": 0.2052, "kalshi_brier": 0.2048, "brier_diff_model_minus_kalshi": 0.0004}, "40+": {"n_settled": 159, "model_brier": 0.2822, "kalshi_brier": 0.1885, "brier_diff_model_minus_kalshi": 0.0938}, "5-10": {"n_settled": 1300, "model_brier": 0.2005, "kalshi_brier": 0.2003, "brier_diff_model_minus_kalshi": 0.0002}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.534, "slope": 0.819, "slope_se": 0.033}, "kalshi_slope": {"intercept": 0.196, "slope": 1.07, "slope_se": 0.037}, "n": 6081}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.485, "slope": 0.863, "slope_se": 0.026}, "kalshi_slope": {"intercept": 0.173, "slope": 1.069, "slope_se": 0.03}, "n": 8263}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 543, "model_brier": 0.3069, "kalshi_brier": 0.2391, "brier_diff_model_minus_kalshi": 0.0678, "brier_diff_se": 0.0129, "corr_model_outcome": 0.0592, "corr_kalshi_outcome": 0.226}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
