# Model-vs-market discrepancy audit

`model_market_discrepancy_audit_v1` · config `discrepancy_sanity_v1` · generated 2026-11-06T05:33Z · **AUTONOMOUS_REAL_MONEY_AUTHORITY = OFF** · no model probability was changed or reconstructed.

> DIAGNOSTIC / DESCRIPTIVE. No probability reconstructed; outcomes, settlement times and first-ball truth are used only to score and diagnose (hindsight), never as model inputs; nothing here is a betting strategy or an optimised threshold.

## Executive summary

* **Distribution** (primary match-winner comparisons, N = 80,234): 0-3 14.1%, 3-5 9.6%, 5-10 20.2%, 10-15 15.3%, 15-25 19.1%, 25-40 13.6%, 40+ 8.0%; median gap 11.82 pp.
* **Where the extremes live**: 97.0% of >=25 pp gaps are off the ATP/WTA main tour (ITF 77.8%, Challenger 10.7%, doubles 6.7%). Main tour: ATP 3.8% and WTA 6.1% of comparisons are >=25 pp.
* **Why >=25 pp gaps happen** (primary cause, N = 17,380): MARKET_ALREADY_SETTLED_WHEN_PRICED 34.0%, STALE_QUOTE 19.4%, BOOK_QUALITY 17.6%, POOR_DATA 9.3%, POSSIBLY_IN_PLAY_QUOTE 5.8%, IDENTITY_AMBIGUOUS 4.3%, IN_PLAY_QUOTE 3.5%, LIMITED_DATA 3.4%, UNEXPLAINED_MODEL_DISAGREEMENT 1.9%, MODEL_LONE_OUTLIER_VS_EXTERNAL 0.8%, EXTERNAL_SUPPORTS_MODEL 0.0%. By class: coverage 34.0%, market_freshness 19.4%, execution 17.6%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%.
* **Stale / settled / in-play**: 53.3% of >=25 pp comparisons used a Kalshi quote over 30 min old at the model's own timestamp; 43.2% were priced after the market settled or on an in-play print. No quote in the producer rows was FRESH (<=10 min) at model time: the pipeline lag alone is 11+ minutes.
* **Identity / ticker**: 0 of 17,380 >=25 pp comparisons failed identity or orientation; ticker orientation verified on all of them; 20.3% ambiguous (doubles, missing producer identity confidence).
* **External triangulation**: external coverage of >=25 pp gaps is 5.3%; the agreement question cannot be answered for extremes. Across all fair_v1 rows with an external price, it sided with Kalshi 26.4% of the time and with the model 1.0%.
* **Thin samples**: >=25 pp gaps have a median thinner-player serve sample of 490.0 points vs 1719.0 for <10 pp gaps.
* **Calibration (pregame-clean, first observation)**: fair_v1 slope 1.032, Gen-2 0.826, Gen-1 ledger 0.867 (1 = calibrated, <1 = too extreme). In the >=25 pp buckets Kalshi's Brier is far better: n 890 model 0.2225 vs Kalshi 0.2038; n 186 model 0.2966 vs Kalshi 0.1748.
* **MODEL_CHANGE_RECOMMENDED = TRUE**: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence. Not implemented here.

## 1. Observations

* 340,991 model-market comparisons (558,236 producer rows before the mirrored match-winner pair was collapsed). one comparison per match-winner event per model per producer run (model-favoured side kept; the two YES contracts mirror each other); every listed derivative contract kept.
* Inputs: Gen-1 ledger 113,528 rows ['2026-09-11T13:47:52.094820+00:00', '2026-11-06T05:18:07.297773+00:00'], shadow board 92,201 rows ['2026-09-28T03:33:22.503933+00:00', '2026-11-06T05:18:10.321229+00:00'], Model 4 42,255 rows, 28,280 settled tickers, 10,706 tickers with an external scan.
* By model: {"gen1_ledger": 76510, "gen1_elo": 46331, "fair_v1": 46331, "gen2": 46331, "gen1_sr": 46331, "model4_fundamental": 39620, "model4_conditioned": 39537}
* Pregame-clean (diagnostic, hindsight): hindsight filter for DIAGNOSIS ONLY: not priced after the market settled, quote not inside a first-ball bracket, quote not within 120 min of settlement, identity not FAILED.

## 2. Discrepancy histogram (% of comparisons per |model - Kalshi mid| bucket, pp)

### Primary match-winner models and every model

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| PRIMARY (fair_v1 + Gen-1 ledger) | 80,234 | 14.1 | 9.6 | 20.2 | 15.3 | 19.1 | 13.6 | 8.0 | 11.82 | 40.8% | 21.7% |
| MW fair_v1 | 46,331 | 12.8 | 8.7 | 18.7 | 15.4 | 19.6 | 14.8 | 9.9 | 13.02 | 44.3% | 24.7% |
| MW gen1_elo | 46,331 | 12.6 | 8.8 | 19.3 | 15.4 | 19.5 | 14.6 | 9.8 | 12.79 | 43.9% | 24.4% |
| MW gen1_ledger | 33,903 | 15.8 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| MW gen1_sr | 46,331 | 10.1 | 7.3 | 16.7 | 13.9 | 20.7 | 18.7 | 12.6 | 15.8 | 52.0% | 31.3% |
| MW gen2 | 46,331 | 11.0 | 7.6 | 16.6 | 13.8 | 19.6 | 17.7 | 13.6 | 15.44 | 50.9% | 31.3% |
| all families model4_conditioned | 39,537 | 22.2 | 18.0 | 34.2 | 17.2 | 5.0 | 2.2 | 1.2 | 6.07 | 8.5% | 3.4% |
| all families model4_fundamental | 39,620 | 17.4 | 13.5 | 33.9 | 19.9 | 10.0 | 3.8 | 1.5 | 7.62 | 15.3% | 5.3% |

Configurable thresholds (primary): >=5pp 76.3%, >=10pp 56.1%, >=15pp 40.8%, >=20pp 30.0%, >=25pp 21.7%, >=30pp 15.6%, >=40pp 8.0%, >=50pp 3.8%
Executable gap (model outside the book, before fees): median 8.36pp; >=10pp 45.0%, >=25pp 17.0%.

## 3. Discrepancy by level

### fair_v1 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,923 | 28.5 | 15.7 | 27.6 | 13.4 | 10.6 | 3.6 | 0.6 | 5.77 | 14.9% | 4.3% |
| CHALLENGER | 6,927 | 15.9 | 9.8 | 20.7 | 15.4 | 16.2 | 11.3 | 10.7 | 10.93 | 38.2% | 22.0% |
| ITF_MEN | 13,085 | 9.8 | 7.4 | 17.1 | 15.2 | 21.2 | 17.3 | 12.0 | 15.18 | 50.5% | 29.2% |
| ITF_WOMEN | 18,050 | 9.5 | 7.1 | 16.0 | 14.8 | 22.1 | 18.3 | 12.1 | 15.86 | 52.5% | 30.4% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 3,013 | 16.8 | 13.2 | 24.6 | 20.9 | 16.6 | 6.8 | 1.1 | 8.68 | 24.5% | 7.9% |
| WTA125 | 1,327 | 15.9 | 6.9 | 22.6 | 20.0 | 20.4 | 12.2 | 2.0 | 10.7 | 34.7% | 14.2% |

### gen2 -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,923 | 26.9 | 15.8 | 26.0 | 15.4 | 11.4 | 3.7 | 0.8 | 6.02 | 15.9% | 4.5% |
| CHALLENGER | 6,927 | 14.7 | 9.1 | 18.7 | 14.0 | 18.7 | 13.5 | 11.3 | 12.49 | 43.5% | 24.8% |
| ITF_MEN | 13,085 | 8.2 | 6.1 | 15.2 | 13.8 | 20.0 | 20.4 | 16.2 | 17.86 | 56.7% | 36.7% |
| ITF_WOMEN | 18,050 | 7.8 | 5.8 | 14.1 | 12.9 | 20.7 | 21.1 | 17.6 | 19.11 | 59.5% | 38.7% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 3,013 | 14.1 | 10.2 | 21.8 | 16.1 | 22.3 | 13.0 | 2.6 | 11.22 | 37.8% | 15.5% |
| WTA125 | 1,327 | 10.2 | 7.2 | 16.3 | 15.4 | 24.3 | 17.4 | 9.2 | 15.22 | 50.9% | 26.6% |

### gen1_elo -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,923 | 22.9 | 14.0 | 25.2 | 15.6 | 15.0 | 6.1 | 1.2 | 7.2 | 22.3% | 7.3% |
| CHALLENGER | 6,927 | 15.2 | 9.5 | 20.9 | 15.6 | 16.1 | 11.9 | 10.8 | 11.2 | 38.8% | 22.7% |
| ITF_MEN | 13,085 | 9.5 | 7.3 | 17.3 | 14.3 | 21.9 | 17.3 | 12.4 | 15.59 | 51.6% | 29.7% |
| ITF_WOMEN | 18,050 | 9.3 | 6.9 | 16.3 | 15.8 | 22.2 | 18.1 | 11.5 | 15.58 | 51.8% | 29.6% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 50.0 | 50.0 | 0.0 | 0.0 | 17.4 | 50.0% | 0.0% |
| WTA | 3,013 | 22.7 | 17.1 | 31.9 | 15.2 | 8.8 | 3.3 | 1.1 | 6.12 | 13.1% | 4.4% |
| WTA125 | 1,327 | 21.1 | 13.3 | 25.6 | 19.1 | 14.9 | 5.8 | 0.3 | 8.02 | 21.0% | 6.1% |

### gen1_ledger -- all observations

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,324 | 26.8 | 19.7 | 29.9 | 12.3 | 8.2 | 2.6 | 0.4 | 5.34 | 11.2% | 3.0% |
| CHALLENGER | 4,470 | 22.2 | 14.5 | 27.7 | 14.7 | 13.6 | 5.8 | 1.5 | 7.09 | 20.9% | 7.3% |
| DOUBLES | 2,515 | 4.9 | 4.6 | 12.8 | 11.0 | 20.1 | 24.7 | 21.8 | 23.41 | 66.6% | 46.5% |
| ITF_MEN | 9,716 | 13.0 | 9.6 | 21.3 | 15.8 | 21.6 | 12.9 | 5.8 | 11.77 | 40.3% | 18.8% |
| ITF_WOMEN | 11,714 | 13.3 | 9.2 | 20.0 | 15.7 | 21.4 | 14.9 | 5.5 | 12.23 | 41.7% | 20.4% |
| OTHER | 149 | 18.8 | 12.1 | 34.9 | 13.4 | 12.8 | 4.7 | 3.4 | 7.31 | 20.8% | 8.1% |
| WTA | 1,759 | 24.1 | 15.9 | 31.3 | 16.8 | 9.1 | 2.6 | 0.2 | 6.57 | 11.9% | 2.8% |
| WTA125 | 1,256 | 25.3 | 13.1 | 21.2 | 18.9 | 13.1 | 6.8 | 1.4 | 7.69 | 21.4% | 8.3% |

### fair_v1 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,808 | 28.9 | 15.9 | 28.0 | 13.3 | 10.4 | 3.2 | 0.3 | 5.64 | 13.9% | 3.5% |
| CHALLENGER | 4,900 | 20.5 | 12.2 | 25.6 | 18.1 | 16.1 | 5.9 | 1.6 | 8.27 | 23.6% | 7.5% |
| ITF_MEN | 9,575 | 12.0 | 8.7 | 20.6 | 17.4 | 22.0 | 14.1 | 5.2 | 12.37 | 41.3% | 19.3% |
| ITF_WOMEN | 13,300 | 11.4 | 8.6 | 18.9 | 17.1 | 24.1 | 15.2 | 4.9 | 13.21 | 44.1% | 20.1% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 100.0 | 0.0 | 0.0 | 21.09 | 100.0% | 0.0% |
| WTA | 2,901 | 17.1 | 13.2 | 25.0 | 21.3 | 16.6 | 6.3 | 0.6 | 8.52 | 23.4% | 6.9% |
| WTA125 | 1,278 | 16.1 | 6.8 | 22.4 | 20.2 | 20.8 | 11.8 | 1.9 | 10.7 | 34.5% | 13.7% |

### gen2 -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 3,808 | 27.2 | 16.1 | 26.2 | 15.4 | 11.3 | 3.3 | 0.4 | 5.96 | 15.0% | 3.7% |
| CHALLENGER | 4,900 | 18.5 | 11.4 | 23.5 | 16.4 | 19.1 | 9.2 | 1.9 | 9.03 | 30.2% | 11.1% |
| ITF_MEN | 9,576 | 9.7 | 7.2 | 17.6 | 16.0 | 21.7 | 18.6 | 9.2 | 14.86 | 49.5% | 27.8% |
| ITF_WOMEN | 13,301 | 8.8 | 6.8 | 16.0 | 14.4 | 22.7 | 20.5 | 10.7 | 16.54 | 54.0% | 31.2% |
| OTHER | 6 | 0.0 | 0.0 | 0.0 | 0.0 | 50.0 | 0.0 | 50.0 | 47.47 | 100.0% | 50.0% |
| WTA | 2,901 | 14.3 | 10.3 | 22.1 | 16.3 | 22.5 | 12.7 | 1.9 | 11.03 | 37.1% | 14.6% |
| WTA125 | 1,278 | 10.2 | 7.4 | 16.4 | 15.5 | 24.3 | 17.5 | 8.7 | 15.16 | 50.5% | 26.2% |

### gen1_ledger -- pregame-clean (hindsight-filtered)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 2,267 | 27.0 | 19.9 | 29.9 | 12.4 | 7.9 | 2.5 | 0.3 | 5.31 | 10.8% | 2.8% |
| CHALLENGER | 3,947 | 23.6 | 15.3 | 28.9 | 14.8 | 12.9 | 4.0 | 0.4 | 6.61 | 17.4% | 4.5% |
| DOUBLES | 2,359 | 4.8 | 4.6 | 13.1 | 11.1 | 20.0 | 24.6 | 21.8 | 23.31 | 66.4% | 46.5% |
| ITF_MEN | 8,355 | 13.8 | 10.2 | 22.9 | 16.2 | 21.6 | 11.4 | 3.8 | 10.84 | 36.9% | 15.3% |
| ITF_WOMEN | 10,031 | 14.0 | 9.8 | 21.1 | 16.2 | 21.5 | 13.8 | 3.6 | 11.42 | 38.9% | 17.4% |
| OTHER | 137 | 18.2 | 13.1 | 34.3 | 14.6 | 12.4 | 4.4 | 2.9 | 7.41 | 19.7% | 7.3% |
| WTA | 1,698 | 24.4 | 16.2 | 31.3 | 16.8 | 9.1 | 2.1 | 0.1 | 6.43 | 11.2% | 2.1% |
| WTA125 | 1,115 | 26.5 | 14.0 | 22.1 | 19.7 | 12.2 | 5.0 | 0.5 | 7.2 | 17.7% | 5.5% |

### Gen-1 ledger by discipline (doubles where a model exists)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| doubles | 2,515 | 4.9 | 4.6 | 12.8 | 11.0 | 20.1 | 24.7 | 21.8 | 23.41 | 66.6% | 46.5% |
| singles | 31,388 | 16.6 | 11.4 | 23.0 | 15.5 | 18.3 | 11.0 | 4.2 | 9.74 | 33.5% | 15.2% |

### fair_v1 by surface

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Carpet | 157 | 7.6 | 8.3 | 12.7 | 7.6 | 20.4 | 28.0 | 15.3 | 21.33 | 63.7% | 43.3% |
| Clay | 9,477 | 12.7 | 9.1 | 19.8 | 15.7 | 19.7 | 13.8 | 9.1 | 12.6 | 42.7% | 23.0% |
| Grass | 237 | 11.8 | 11.0 | 17.7 | 13.5 | 23.6 | 14.8 | 7.6 | 14.16 | 46.0% | 22.4% |
| Hard | 30,203 | 13.4 | 8.8 | 18.8 | 15.2 | 19.2 | 14.8 | 9.8 | 12.85 | 43.8% | 24.6% |
| UNKNOWN | 6,257 | 10.5 | 7.6 | 17.0 | 16.4 | 21.5 | 16.0 | 11.1 | 14.32 | 48.5% | 27.1% |

## 4. Discrepancy by data quality

### fair_v1 by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 13,112 | 19.4 | 12.0 | 22.4 | 15.9 | 15.0 | 9.1 | 6.1 | 8.89 | 30.3% | 15.2% |
| B | 5,658 | 12.8 | 8.8 | 19.8 | 15.7 | 19.6 | 12.7 | 10.8 | 12.59 | 43.0% | 23.4% |
| C | 6,574 | 11.9 | 8.9 | 19.5 | 15.8 | 18.6 | 14.7 | 10.6 | 12.95 | 43.9% | 25.3% |
| D | 7,520 | 11.7 | 8.3 | 17.9 | 15.4 | 21.6 | 15.7 | 9.4 | 13.78 | 46.6% | 25.1% |
| F | 13,467 | 7.5 | 5.6 | 14.8 | 14.7 | 23.5 | 20.8 | 13.1 | 17.72 | 57.4% | 33.9% |

### gen1_ledger by grade

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| A | 9,038 | 24.5 | 16.0 | 29.2 | 15.0 | 10.7 | 3.4 | 1.2 | 6.38 | 15.3% | 4.6% |
| B | 4,759 | 16.6 | 10.8 | 24.2 | 16.9 | 18.8 | 9.6 | 3.1 | 9.67 | 31.5% | 12.7% |
| C | 6,700 | 11.1 | 7.8 | 19.5 | 14.7 | 20.9 | 15.6 | 10.3 | 13.48 | 46.8% | 25.9% |
| D | 5,086 | 14.6 | 10.1 | 21.4 | 15.4 | 20.7 | 12.6 | 5.3 | 11.19 | 38.6% | 17.9% |
| F | 8,320 | 10.2 | 8.4 | 16.2 | 14.6 | 23.3 | 19.5 | 7.8 | 15.32 | 50.6% | 27.3% |

### fair_v1 by sanity data-quality status

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ADEQUATE | 14,825 | 17.7 | 10.9 | 21.5 | 15.8 | 15.3 | 10.0 | 8.7 | 9.96 | 34.0% | 18.7% |
| LIMITED | 10,129 | 13.6 | 9.8 | 20.4 | 15.9 | 19.3 | 13.4 | 7.5 | 11.84 | 40.2% | 20.9% |
| POOR | 21,377 | 9.1 | 6.6 | 16.0 | 15.0 | 22.7 | 18.9 | 11.8 | 16.1 | 53.4% | 30.6% |

## 5. Discrepancy by model and family

### Gen-1 ledger by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 8,718 | 23.8 | 17.8 | 33.2 | 15.6 | 6.4 | 2.9 | 0.4 | 5.92 | 9.7% | 3.3% |
| GAME_SPREAD | 6,585 | 22.5 | 15.3 | 32.2 | 16.9 | 9.0 | 3.4 | 0.6 | 6.71 | 13.0% | 4.0% |
| MATCH_WINNER | 33,903 | 15.8 | 10.9 | 22.2 | 15.2 | 18.4 | 12.0 | 5.5 | 10.26 | 35.9% | 17.5% |
| SET_SPREAD | 20 | 15.0 | 20.0 | 30.0 | 30.0 | 5.0 | 0.0 | 0.0 | 6.43 | 5.0% | 0.0% |
| SET_WINNER | 16,192 | 27.9 | 16.7 | 30.7 | 12.7 | 9.2 | 2.5 | 0.3 | 5.64 | 11.9% | 2.7% |
| TOTAL_GAMES | 11,088 | 9.8 | 10.8 | 35.6 | 26.0 | 10.7 | 4.3 | 3.0 | 9.21 | 17.9% | 7.2% |
| TOTAL_SETS | 4 | 100.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.79 | 0.0% | 0.0% |

### model4_conditioned by family (market-conditioned by construction: NOT an independent estimate)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,000 | 24.4 | 28.9 | 33.2 | 8.1 | 4.0 | 1.1 | 0.3 | 4.79 | 5.3% | 1.4% |
| GAME_SPREAD | 9,120 | 46.9 | 16.1 | 24.8 | 7.5 | 2.3 | 1.9 | 0.6 | 3.3 | 4.8% | 2.5% |
| TOTAL_GAMES | 16,417 | 6.5 | 9.8 | 40.2 | 30.2 | 7.5 | 3.3 | 2.4 | 9.22 | 13.2% | 5.7% |

### model4_fundamental by family

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| EXACT_SET_SCORE | 14,035 | 23.9 | 16.6 | 34.8 | 14.7 | 6.9 | 2.6 | 0.5 | 6.05 | 10.0% | 3.1% |
| GAME_SPREAD | 9,129 | 20.6 | 13.6 | 28.2 | 20.1 | 11.9 | 4.5 | 1.1 | 7.62 | 17.5% | 5.6% |
| TOTAL_GAMES | 16,456 | 10.0 | 10.8 | 36.2 | 24.3 | 11.6 | 4.5 | 2.6 | 9.06 | 18.7% | 7.1% |

### Same shadow-board rows, model by model

| model | N | >=15 all | >=25 all | median all | >=15 clean | >=25 clean | median clean |
|---|---|---|---|---|---|---|---|
| fair_v1 | 46,331 | 44.3% | 24.7% | 13.02 | 35.3% | 15.1% | 10.71 |
| gen1_elo | 46,331 | 43.9% | 24.4% | 12.79 | 34.8% | 14.9% | 10.49 |
| gen1_sr | 46,331 | 52.0% | 31.3% | 15.8 | 44.0% | 21.6% | 13.0 |
| gen2 | 46,331 | 50.9% | 31.3% | 15.44 | 43.9% | 23.1% | 12.86 |

## 6. Discrepancy by quote freshness (at the model's own timestamp)

### fair_v1

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 19,896 | 15.5 | 10.5 | 21.4 | 17.3 | 20.1 | 11.9 | 3.4 | 10.71 | 35.4% | 15.3% |
| STALE | 26,435 | 10.8 | 7.3 | 16.8 | 14.0 | 19.3 | 17.0 | 14.8 | 15.4 | 51.0% | 31.8% |

### gen1_ledger

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| AGING | 3,472 | 14.9 | 10.4 | 21.6 | 15.9 | 20.1 | 12.4 | 4.6 | 10.85 | 37.1% | 17.0% |
| FRESH | 27,371 | 16.4 | 11.2 | 22.8 | 15.3 | 17.9 | 11.5 | 4.8 | 9.87 | 34.3% | 16.4% |
| STALE | 3,060 | 11.1 | 8.6 | 17.6 | 13.5 | 20.9 | 16.1 | 12.4 | 14.75 | 49.4% | 28.5% |

| set | N | FRESH | AGING | STALE | median age (min) | p90 | max |
|---|---|---|---|---|---|---|---|
| all_primary | 80,234 | 27371 | 23368 | 29495 | 24.7 | 125.6 | 1451.1 |
| ge_15pp | 32,715 | 9390 | 8324 | 15001 | 28.1 | 431.1 | 1451.1 |
| ge_25pp | 17,380 | 4481 | 3632 | 9267 | 33.1 | 579.9 | 1431.1 |
| lt_10pp | 35,229 | 13804 | 11051 | 10374 | 22.6 | 47.9 | 1421.1 |

Current slate `SL-20261106T053338Z-20bdfc76`: 296 priced rows, quote age at build {'median': 15.8, 'max': 15.9}, freshness {'AGING': 296}. Quote age at assisted decision time: no decisions recorded yet.

## 7. Discrepancy by external triangulation

### fair_v1 rows with an external price, by triangulation

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ALL_THREE_DISAGREE | 49 | 0.0 | 0.0 | 36.7 | 6.1 | 32.6 | 20.4 | 4.1 | 18.34 | 57.1% | 24.5% |
| EXTERNAL_LONE_OUTLIER | 29 | 69.0 | 31.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.24 | 0.0% | 0.0% |
| INSUFFICIENT_INPUTS | 4,624 | 19.2 | 10.9 | 25.4 | 17.9 | 18.1 | 7.4 | 1.0 | 8.82 | 26.6% | 8.4% |
| KALSHI_LONE_OUTLIER | 30 | 6.7 | 6.7 | 73.3 | 6.7 | 3.3 | 3.3 | 0.0 | 6.16 | 6.7% | 3.3% |
| MARKETS_AGREE | 941 | 65.8 | 34.2 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 2.19 | 0.0% | 0.0% |
| MODEL_LONE_OUTLIER | 2,036 | 0.0 | 2.3 | 36.8 | 26.5 | 24.2 | 9.2 | 0.9 | 11.86 | 34.3% | 10.1% |

| set | N | with external | AGREES_WITH_KALSHI | supports model | statuses |
|---|---|---|---|---|---|
| fair_v1_all | 46,331 | 7709 (16.6%) | 26.4% | 1.0% | {"EXTERNAL_STALE": 4624, "AGREES_WITH_KALSHI": 2036, "ALL_AGREE": 941, "SUPPORTS_MODEL_DIRECTION": 48, "AGREES_WITH_MODEL": 30, "EXTERNAL_OUTLIER": 29, "ALL_DISAGREE": 1} |
| fair_v1_ge_15pp | 20,526 | 1957 (9.5%) | 35.7% | 1.5% | {"EXTERNAL_STALE": 1228, "AGREES_WITH_KALSHI": 699, "SUPPORTS_MODEL_DIRECTION": 28, "AGREES_WITH_MODEL": 2} |
| fair_v1_ge_25pp | 11,437 | 608 (5.3%) | 33.9% | 2.1% | {"EXTERNAL_STALE": 389, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_ge_25pp_pregame_clean | 5,401 | 578 (10.7%) | 34.4% | 2.2% | {"EXTERNAL_STALE": 366, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1} |
| fair_v1_lt_10pp | 18,656 | 4381 (23.5%) | 18.2% | 1.0% | {"EXTERNAL_STALE": 2570, "ALL_AGREE": 941, "AGREES_WITH_KALSHI": 797, "EXTERNAL_OUTLIER": 29, "AGREES_WITH_MODEL": 26, "SUPPORTS_MODEL_DIRECTION": 17, "ALL_DISAGREE": 1} |

## 8. Discrepancy by player sample asymmetry

### fair_v1 by serve-sample ratio (deeper / thinner)

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2-4x | 9,086 | 10.5 | 7.7 | 19.5 | 14.7 | 21.6 | 16.2 | 9.9 | 14.07 | 47.7% | 26.1% |
| 4-10x | 6,217 | 11.3 | 8.6 | 18.4 | 15.2 | 22.0 | 14.3 | 10.1 | 13.75 | 46.4% | 24.4% |
| <2x | 23,619 | 14.9 | 9.8 | 19.7 | 16.1 | 17.6 | 13.1 | 8.8 | 11.56 | 39.5% | 21.9% |
| >=10x | 7,409 | 10.5 | 6.4 | 15.0 | 14.4 | 21.7 | 18.9 | 13.1 | 16.35 | 53.7% | 32.0% |

### fair_v1 by thinner player's serve points

| slice | N | 0-3 | 3-5 | 5-10 | 10-15 | 15-25 | 25-40 | 40+ | median | >=15 | >=25 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1000-3000 | 12,128 | 12.4 | 8.7 | 19.9 | 16.2 | 19.0 | 13.5 | 10.2 | 12.68 | 42.8% | 23.8% |
| 300-1000 | 10,037 | 11.8 | 8.8 | 17.7 | 15.2 | 20.7 | 16.4 | 9.5 | 13.7 | 46.5% | 25.8% |
| <300 | 14,573 | 8.3 | 5.8 | 15.1 | 14.7 | 23.1 | 19.8 | 13.1 | 17.1 | 56.0% | 32.9% |
| >=3000 | 9,593 | 21.2 | 13.0 | 23.9 | 15.7 | 14.0 | 7.3 | 5.0 | 7.75 | 26.2% | 12.2% |

fair_v1 match winners, pregame-clean, first observation per match. 'model_minus_observed' > 0 on the model-favoured side means the model over-stated that side (overconfidence in the disagreement)

| slice | N settled | model side prob | Kalshi side prob | observed | model - obs | Kalshi - obs | Brier diff (model - Kalshi) |
|---|---|---|---|---|---|---|---|
| ratio 2-4x | 1411 | 0.5475 | 0.4083 | 0.4897 | +0.058 | -0.081 | 0.0007 ± 0.0041 |
| ratio 4-10x | 964 | 0.576 | 0.4312 | 0.4865 | +0.089 | -0.055 | 0.0091 ± 0.0051 |
| ratio <2x | 3430 | 0.5366 | 0.4135 | 0.4367 | +0.100 | -0.023 | 0.0145 ± 0.0024 |
| ratio >=10x | 1186 | 0.5641 | 0.3909 | 0.4477 | +0.116 | -0.057 | 0.0146 ± 0.0052 |
| thinner_sample 1000-3000 | 1935 | 0.5391 | 0.4118 | 0.4481 | +0.091 | -0.036 | 0.0111 ± 0.0033 |
| thinner_sample 300-1000 | 1590 | 0.5629 | 0.4224 | 0.4748 | +0.088 | -0.052 | 0.0046 ± 0.0039 |
| thinner_sample <300 | 2278 | 0.5574 | 0.3894 | 0.4548 | +0.103 | -0.065 | 0.0131 ± 0.0037 |
| thinner_sample >=3000 | 1188 | 0.53 | 0.4363 | 0.447 | +0.083 | -0.011 | 0.0151 ± 0.0033 |
| data_status ADEQUATE | 1930 | 0.5321 | 0.4287 | 0.4409 | +0.091 | -0.012 | 0.0153 ± 0.0028 |
| data_status LIMITED | 1701 | 0.5476 | 0.415 | 0.4668 | +0.081 | -0.052 | 0.0068 ± 0.0036 |
| data_status POOR | 3360 | 0.5593 | 0.399 | 0.4595 | +0.100 | -0.061 | 0.0105 ± 0.003 |

Surface-specific sample: UNAVAILABLE historically: producer rows carry no as-of surface sample; reading today's ratings would leak later matches.

## 9. Predictive performance by discrepancy bucket (diagnostic; never a strategy)

Model-favoured side = the side the model rates above the Kalshi mid. Hypothetical economics: one contract on that side at the observed ask with the taker fee -- descriptive only, never an optimised threshold.

### fair_v1 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1005 | 0.197 | 0.1974 | -0.0003 ± 0.0005 | 0.5738 | 0.5746 | 0.5024 | 0.4873 | 0.4995 | -0.096 ± 0.0148 | -0.0087 (8) |
| 3-5 | 644 | 0.2051 | 0.205 | +0.0000 ± 0.0014 | 0.594 | 0.5926 | 0.5025 | 0.4627 | 0.4814 | -0.095 ± 0.0183 | 0.01 (2) |
| 5-10 | 1505 | 0.2009 | 0.2002 | +0.0007 ± 0.0017 | 0.588 | 0.5839 | 0.5115 | 0.4377 | 0.4678 | -0.088 ± 0.012 | -0.0143 (7) |
| 10-15 | 1211 | 0.2183 | 0.2092 | +0.0091 ± 0.0033 | 0.6287 | 0.6018 | 0.523 | 0.3995 | 0.4236 | -0.104 ± 0.0133 | -0.048 (5) |
| 15-25 | 1550 | 0.2244 | 0.208 | +0.0164 ± 0.0045 | 0.6434 | 0.5994 | 0.5745 | 0.3798 | 0.4355 | -0.101 ± 0.0116 | -0.004 (10) |
| 25-40 | 890 | 0.2225 | 0.2038 | +0.0187 ± 0.0091 | 0.6349 | 0.588 | 0.6511 | 0.3412 | 0.4663 | -0.068 ± 0.0139 | -0.06 (2) |
| 40+ | 186 | 0.2966 | 0.1748 | +0.1217 ± 0.0275 | 0.7985 | 0.5224 | 0.73 | 0.2752 | 0.3763 | -0.084 ± 0.0267 | -- (0) |

### fair_v1 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5274 | 0.1855 | 0.1863 | -0.0008 ± 0.0002 | 0.5469 | 0.5478 | 0.4887 | 0.4734 | 0.5038 | -0.022 ± 0.006 | -0.01 (28) |
| 3-5 | 3554 | 0.1978 | 0.1962 | +0.0016 ± 0.0006 | 0.576 | 0.5699 | 0.4811 | 0.4413 | 0.4398 | -0.056 ± 0.0075 | 0.0 (3) |
| 5-10 | 7658 | 0.2007 | 0.1977 | +0.0031 ± 0.0008 | 0.587 | 0.5763 | 0.4844 | 0.4108 | 0.4273 | -0.042 ± 0.0051 | -0.0114 (22) |
| 10-15 | 6345 | 0.2016 | 0.1858 | +0.0158 ± 0.0013 | 0.5896 | 0.5452 | 0.4849 | 0.361 | 0.3593 | -0.063 ± 0.0054 | -0.0281 (16) |
| 15-25 | 8008 | 0.2056 | 0.167 | +0.0386 ± 0.0018 | 0.6029 | 0.4963 | 0.4989 | 0.3035 | 0.3033 | -0.068 ± 0.0046 | -0.0027 (45) |
| 25-40 | 6187 | 0.2229 | 0.1261 | +0.0967 ± 0.0028 | 0.64 | 0.3877 | 0.5268 | 0.213 | 0.2201 | -0.058 ± 0.0044 | -0.0733 (3) |
| 40+ | 4093 | 0.3827 | 0.0445 | +0.3382 ± 0.0038 | 0.9971 | 0.1723 | 0.6311 | 0.1025 | 0.0589 | -0.076 ± 0.0031 | -- (0) |

### gen2 -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 808 | 0.2043 | 0.2047 | -0.0003 ± 0.0005 | 0.5892 | 0.5904 | 0.5064 | 0.4915 | 0.5136 | -0.103 ± 0.0171 | -0.0117 (6) |
| 3-5 | 576 | 0.2101 | 0.2072 | +0.0029 ± 0.0015 | 0.6026 | 0.5963 | 0.5115 | 0.472 | 0.4514 | -0.131 ± 0.0204 | 0.01 (2) |
| 5-10 | 1288 | 0.2069 | 0.205 | +0.0020 ± 0.0019 | 0.6002 | 0.5948 | 0.539 | 0.4644 | 0.4915 | -0.089 ± 0.013 | -0.01 (4) |
| 10-15 | 1121 | 0.2113 | 0.2062 | +0.0051 ± 0.0034 | 0.615 | 0.5981 | 0.5635 | 0.4392 | 0.4835 | -0.096 ± 0.0142 | -0.04 (5) |
| 15-25 | 1636 | 0.2308 | 0.2124 | +0.0183 ± 0.0045 | 0.6559 | 0.6093 | 0.584 | 0.3886 | 0.4407 | -0.097 ± 0.0117 | -0.012 (10) |
| 25-40 | 1147 | 0.2659 | 0.1967 | +0.0692 ± 0.0082 | 0.7422 | 0.573 | 0.658 | 0.3439 | 0.3932 | -0.119 ± 0.0131 | -0.008 (5) |
| 40+ | 415 | 0.3727 | 0.162 | +0.2107 ± 0.0198 | 1.0163 | 0.4901 | 0.7352 | 0.2464 | 0.2892 | -0.087 ± 0.019 | -0.06 (2) |

### gen2 -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 4536 | 0.1917 | 0.192 | -0.0003 ± 0.0002 | 0.559 | 0.5594 | 0.5075 | 0.4925 | 0.5101 | -0.038 ± 0.0067 | -0.0154 (26) |
| 3-5 | 3090 | 0.1926 | 0.1916 | +0.0010 ± 0.0006 | 0.5616 | 0.5582 | 0.5102 | 0.4705 | 0.4767 | -0.046 ± 0.0081 | 0.01 (2) |
| 5-10 | 6830 | 0.1974 | 0.1939 | +0.0034 ± 0.0008 | 0.5796 | 0.5673 | 0.5081 | 0.434 | 0.4507 | -0.041 ± 0.0054 | -0.0117 (6) |
| 10-15 | 5695 | 0.2017 | 0.1914 | +0.0103 ± 0.0015 | 0.5927 | 0.5598 | 0.5104 | 0.3865 | 0.4076 | -0.044 ± 0.0059 | -0.0189 (18) |
| 15-25 | 8055 | 0.2166 | 0.1813 | +0.0353 ± 0.0019 | 0.6293 | 0.5318 | 0.5242 | 0.3286 | 0.3388 | -0.059 ± 0.0048 | -0.0084 (43) |
| 25-40 | 7256 | 0.2506 | 0.1372 | +0.1134 ± 0.0028 | 0.7081 | 0.4195 | 0.5598 | 0.2429 | 0.226 | -0.080 ± 0.0043 | -0.0095 (20) |
| 40+ | 5657 | 0.4015 | 0.0593 | +0.3422 ± 0.0037 | 1.0589 | 0.2136 | 0.6545 | 0.1193 | 0.0808 | -0.074 ± 0.0032 | -0.06 (2) |

### gen1_elo -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 984 | 0.1959 | 0.1974 | -0.0015 ± 0.0005 | 0.5714 | 0.5751 | 0.5028 | 0.4874 | 0.5356 | -0.049 ± 0.0148 | -0.012 (10) |
| 3-5 | 687 | 0.2069 | 0.2054 | +0.0015 ± 0.0014 | 0.5994 | 0.5944 | 0.4947 | 0.4552 | 0.4585 | -0.110 ± 0.0181 | -0.0 (4) |
| 5-10 | 1535 | 0.202 | 0.1987 | +0.0033 ± 0.0017 | 0.5888 | 0.5794 | 0.5121 | 0.4384 | 0.4521 | -0.103 ± 0.0118 | -0.01 (9) |
| 10-15 | 1229 | 0.2107 | 0.2015 | +0.0092 ± 0.0032 | 0.612 | 0.585 | 0.5363 | 0.4132 | 0.4394 | -0.108 ± 0.0128 | -0.0286 (7) |
| 15-25 | 1479 | 0.2305 | 0.2126 | +0.0179 ± 0.0047 | 0.6582 | 0.6094 | 0.5851 | 0.3909 | 0.4415 | -0.106 ± 0.012 | -0.03 (1) |
| 25-40 | 882 | 0.2124 | 0.2084 | +0.0040 ± 0.009 | 0.6134 | 0.5988 | 0.6589 | 0.3481 | 0.4955 | -0.055 ± 0.0139 | -0.0267 (3) |
| 40+ | 195 | 0.3097 | 0.1824 | +0.1274 ± 0.0275 | 0.8383 | 0.5387 | 0.7419 | 0.2873 | 0.3846 | -0.087 ± 0.0282 | -- (0) |

### gen1_elo -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5107 | 0.1853 | 0.186 | -0.0007 ± 0.0002 | 0.5461 | 0.547 | 0.4859 | 0.4706 | 0.4905 | -0.031 ± 0.0061 | -0.0137 (41) |
| 3-5 | 3623 | 0.2043 | 0.2027 | +0.0017 ± 0.0006 | 0.5934 | 0.5877 | 0.4777 | 0.4382 | 0.4378 | -0.055 ± 0.0076 | -0.01 (19) |
| 5-10 | 7820 | 0.1956 | 0.1905 | +0.0050 ± 0.0007 | 0.5741 | 0.5584 | 0.487 | 0.413 | 0.4165 | -0.054 ± 0.005 | -0.0105 (37) |
| 10-15 | 6293 | 0.1933 | 0.1781 | +0.0152 ± 0.0013 | 0.5711 | 0.5274 | 0.4937 | 0.3705 | 0.3704 | -0.062 ± 0.0053 | -0.0146 (13) |
| 15-25 | 8093 | 0.2113 | 0.1723 | +0.0389 ± 0.0018 | 0.6164 | 0.5084 | 0.5122 | 0.3177 | 0.3158 | -0.069 ± 0.0046 | -0.0533 (3) |
| 25-40 | 6132 | 0.217 | 0.1275 | +0.0896 ± 0.0029 | 0.6274 | 0.3905 | 0.5294 | 0.2138 | 0.2319 | -0.049 ± 0.0044 | -0.02 (4) |
| 40+ | 4051 | 0.3918 | 0.0495 | +0.3423 ± 0.004 | 1.0216 | 0.1849 | 0.6405 | 0.1086 | 0.0659 | -0.076 ± 0.0034 | -- (0) |

### gen1_ledger -- pregame_clean_first_per_match

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 1416 | 0.1972 | 0.1973 | -0.0001 ± 0.0004 | 0.5727 | 0.5728 | 0.5085 | 0.4935 | 0.4993 | -0.067 ± 0.0121 | -0.0213 (54) |
| 3-5 | 1015 | 0.1885 | 0.1882 | +0.0003 ± 0.0011 | 0.555 | 0.5523 | 0.495 | 0.4552 | 0.47 | -0.059 ± 0.0139 | -0.0194 (34) |
| 5-10 | 2052 | 0.199 | 0.1946 | +0.0045 ± 0.0015 | 0.5874 | 0.5721 | 0.5068 | 0.4332 | 0.4401 | -0.074 ± 0.01 | -0.005 (78) |
| 10-15 | 1412 | 0.2139 | 0.2018 | +0.0121 ± 0.003 | 0.6211 | 0.5872 | 0.542 | 0.4192 | 0.4299 | -0.088 ± 0.0123 | 0.0014 (65) |
| 15-25 | 1832 | 0.2303 | 0.207 | +0.0234 ± 0.0042 | 0.6575 | 0.5976 | 0.5891 | 0.3941 | 0.434 | -0.088 ± 0.0107 | -0.0214 (59) |
| 25-40 | 1111 | 0.2399 | 0.2097 | +0.0302 ± 0.0084 | 0.6854 | 0.6021 | 0.688 | 0.3759 | 0.4833 | -0.088 ± 0.0129 | -0.0252 (27) |
| 40+ | 393 | 0.3271 | 0.2023 | +0.1247 ± 0.0217 | 0.9425 | 0.5885 | 0.8163 | 0.3403 | 0.4631 | -0.098 ± 0.0203 | -0.0543 (7) |

### gen1_ledger -- all_observations

| bucket | N settled | model Brier | Kalshi Brier | diff ± se | model LL | Kalshi LL | model-side p | Kalshi-side p | observed | after-fee / contract | strict CLV (n) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-3 | 5210 | 0.1776 | 0.1778 | -0.0002 ± 0.0002 | 0.5255 | 0.5254 | 0.512 | 0.4967 | 0.509 | -0.037 ± 0.0059 | -0.0145 (98) |
| 3-5 | 3599 | 0.1955 | 0.1947 | +0.0008 ± 0.0006 | 0.5699 | 0.5674 | 0.5003 | 0.4606 | 0.471 | -0.040 ± 0.0074 | -0.0204 (72) |
| 5-10 | 7318 | 0.196 | 0.1898 | +0.0063 ± 0.0008 | 0.5788 | 0.5595 | 0.5007 | 0.427 | 0.4225 | -0.061 ± 0.0051 | -0.0084 (134) |
| 10-15 | 5013 | 0.2085 | 0.1929 | +0.0156 ± 0.0015 | 0.6076 | 0.5664 | 0.537 | 0.414 | 0.4107 | -0.070 ± 0.0063 | -0.0053 (106) |
| 15-25 | 6087 | 0.2302 | 0.1993 | +0.0309 ± 0.0023 | 0.6618 | 0.5777 | 0.5748 | 0.3794 | 0.3989 | -0.066 ± 0.0058 | -0.026 (108) |
| 25-40 | 3999 | 0.2568 | 0.1893 | +0.0675 ± 0.0043 | 0.7268 | 0.5519 | 0.6393 | 0.3266 | 0.3776 | -0.067 ± 0.0067 | -0.0246 (52) |
| 40+ | 1760 | 0.3706 | 0.16 | +0.2106 ± 0.0098 | 1.0466 | 0.4761 | 0.7441 | 0.2436 | 0.2938 | -0.064 ± 0.0091 | -0.0308 (12) |

### Calibration slopes (pregame-clean, first observation per match; slope < 1 = too extreme)

| model | N | model slope ± se | Kalshi slope (same rows) | model extremity | Kalshi extremity | model Brier | Kalshi Brier |
|---|---|---|---|---|---|---|---|
| fair_v1 | 6991 | 1.032 ± 0.033 | 1.107 | 0.1694 | 0.1695 | 0.2143 | 0.2033 |
| gen2 | 6991 | 0.826 ± 0.03 | 1.078 | 0.1736 | 0.1699 | 0.2327 | 0.2032 |
| gen1_elo | 6991 | 1.011 ± 0.032 | 1.097 | 0.1759 | 0.1696 | 0.2135 | 0.2034 |
| gen1_sr | 6991 | 1.01 ± 0.04 | 1.137 | 0.1336 | 0.1715 | 0.229 | 0.2028 |
| gen1_ledger | 9231 | 0.867 ± 0.024 | 1.076 | 0.1901 | 0.1765 | 0.2165 | 0.2 |

## 10. Strict CLV

Strict executable CLV exists only where first-ball truth exists (ATP/WTA main tour) and only for pregame-clean entries before the strict close; per-bucket values and counts are in the tables above (`strict CLV (n)`).

## 11. Root causes of large gaps (primary match-winner models)

### >= ge_15 pp (N = 32,715)

| primary cause | class | N | share |
|---|---|---|---|
| STALE_QUOTE | market_freshness | 7,552 | 23.1% |
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 7,363 | 22.5% |
| BOOK_QUALITY | execution | 5,906 | 18.1% |
| POOR_DATA | data | 3,811 | 11.7% |
| LIMITED_DATA | data | 2,029 | 6.2% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,876 | 5.7% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 1,358 | 4.2% |
| IDENTITY_AMBIGUOUS | mapping | 1,342 | 4.1% |
| IN_PLAY_QUOTE | market_freshness/coverage | 934 | 2.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 543 | 1.7% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: market_freshness 23.1%, coverage 22.5%, execution 18.1%, data 17.8%, market_freshness/coverage 8.6%, model_calibration_or_unknown 4.2%, mapping 4.1%, model_calibration 1.7%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 96.5%, START_UNVERIFIABLE 94.5%, LOW_DATA_QUALITY 71.6%, THIN_PLAYER_HISTORY 59.9%, STALE_PLAYER_DATA 52.1%, STALE_KALSHI_QUOTE 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.2%, ASYMMETRIC_SAMPLE_SIZE 33.1%, WIDE_SPREAD 24.3%, MODEL_HIGH_UNCERTAINTY 18.6%, PLAYER_IDENTITY_RISK 15.3%, LEVEL_TRANSFER_RISK 10.1%, LOW_DISPLAYED_LIQUIDITY 8.4%, EVENT_MAPPING_RISK 7.2%, MODEL_CALIBRATION_OUTLIER 3.7%, EXTERNAL_MARKET_REJECTION 3.3%, UNKNOWN 0.8%, EXTERNAL_MARKET_CONFIRMATION 0.2%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 24.9%, POST_SETTLEMENT_OBSERVATION 22.5%, POSSIBLE_IN_PLAY_QUOTE 6.1%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### >= ge_25 pp (N = 17,380)

| primary cause | class | N | share |
|---|---|---|---|
| MARKET_ALREADY_SETTLED_WHEN_PRICED | coverage | 5,900 | 34.0% |
| STALE_QUOTE | market_freshness | 3,381 | 19.4% |
| BOOK_QUALITY | execution | 3,065 | 17.6% |
| POOR_DATA | data | 1,611 | 9.3% |
| POSSIBLY_IN_PLAY_QUOTE | market_freshness/coverage | 1,001 | 5.8% |
| IDENTITY_AMBIGUOUS | mapping | 746 | 4.3% |
| IN_PLAY_QUOTE | market_freshness/coverage | 611 | 3.5% |
| LIMITED_DATA | data | 595 | 3.4% |
| UNEXPLAINED_MODEL_DISAGREEMENT | model_calibration_or_unknown | 336 | 1.9% |
| MODEL_LONE_OUTLIER_VS_EXTERNAL | model_calibration | 133 | 0.8% |
| EXTERNAL_SUPPORTS_MODEL | possible_market_error | 1 | 0.0% |

Cause class: coverage 34.0%, market_freshness 19.4%, execution 17.6%, data 12.7%, market_freshness/coverage 9.3%, mapping 4.3%, model_calibration_or_unknown 1.9%, model_calibration 0.8%, possible_market_error 0.0%

Ex-ante reason tags (multi-label, available at the observation's own time): NO_EXTERNAL_REFERENCE 98.0%, START_UNVERIFIABLE 97.0%, LOW_DATA_QUALITY 75.0%, THIN_PLAYER_HISTORY 61.9%, STALE_KALSHI_QUOTE 53.3%, STALE_PLAYER_DATA 45.9%, MODEL_INTERNAL_DISAGREEMENT 42.3%, ASYMMETRIC_SAMPLE_SIZE 34.3%, WIDE_SPREAD 23.7%, MODEL_HIGH_UNCERTAINTY 19.3%, PLAYER_IDENTITY_RISK 18.4%, LEVEL_TRANSFER_RISK 8.9%, EVENT_MAPPING_RISK 8.9%, LOW_DISPLAYED_LIQUIDITY 8.2%, MODEL_CALIBRATION_OUTLIER 4.9%, EXTERNAL_MARKET_REJECTION 1.9%, UNKNOWN 0.2%, EXTERNAL_MARKET_CONFIRMATION 0.1%

Hindsight tags (diagnosis only): LIKELY_IN_PLAY_QUOTE 37.0%, POST_SETTLEMENT_OBSERVATION 34.0%, POSSIBLE_IN_PLAY_QUOTE 6.2%, CONFIRMED_IN_PLAY_QUOTE 0.3%

### Identity / side integrity audit, every >= 25 pp comparison

Status: {"IDENTITY_VERIFIED": 13853, "IDENTITY_AMBIGUOUS": 3527}; ticker orientation: {"VERIFIED": 17380}.

Checks: discipline:AMBIGUOUS 1170, discipline:PASS 16210, identity_confidence:AMBIGUOUS 3197, identity_confidence:PASS 14183, level_mapping:NA 1182, level_mapping:PASS 16198, market_pair:AMBIGUOUS 491, market_pair:NA 376, market_pair:PASS 16513, model_complement:NA 338, model_complement:PASS 17042, namesake:AMBIGUOUS 6, namesake:PASS 17374, physical_match_id:NA 5943, physical_match_id:PASS 11437, player_ids:PASS 17380, same_pair_other_event:PASS 17380, ticker_orientation:PASS 17380

## 12. Level analysis

| level | N | >=25 all | >=25 clean | share of all >=25 | >=25 cause classes | median clean | clean Brier model / Kalshi (n) | stale | data POOR | identity not verified | settled/in-play |
|---|---|---|---|---|---|---|---|---|---|---|---|
| ATP | 6,247 | 3.8% | 3.3% | 1.4% | {"market_freshness": 57, "model_calibration_or_unknown": 53, "data": 36, "model_calibration": 28, "execution": 25, "coverage": 21, "market_freshness/coverage": 17} | 5.53 | 0.2264 / 0.2215 (793) | 24.6% | 2.5% | 3.1% | 2.8% |
| CHALLENGER | 11,397 | 16.2% | 6.2% | 10.7% | {"coverage": 1089, "market_freshness/coverage": 217, "market_freshness": 214, "data": 157, "model_calibration_or_unknown": 79, "execution": 41, "model_calibration": 36, "mapping": 17, "possible_market_error": 1} | 7.39 | 0.2193 / 0.2095 (2678) | 37.8% | 15.4% | 4.1% | 22.4% |
| DOUBLES | 2,515 | 46.5% | 46.5% | 6.7% | {"execution": 661, "mapping": 329, "market_freshness": 106, "market_freshness/coverage": 67, "coverage": 7} | 23.31 | 0.2976 / 0.2337 (620) | 9.3% | 0.0% | 100.0% | 6.2% |
| ITF_MEN | 22,801 | 24.8% | 17.4% | 32.5% | {"coverage": 1962, "market_freshness": 1099, "execution": 976, "data": 837, "market_freshness/coverage": 566, "mapping": 205, "model_calibration": 6, "model_calibration_or_unknown": 2} | 11.67 | 0.2155 / 0.1984 (4813) | 39.7% | 69.0% | 15.3% | 21.4% |
| ITF_WOMEN | 29,764 | 26.5% | 18.9% | 45.3% | {"coverage": 2766, "market_freshness": 1702, "execution": 1304, "data": 1111, "market_freshness/coverage": 688, "mapping": 189, "model_calibration_or_unknown": 93, "model_calibration": 22} | 12.51 | 0.2032 / 0.1934 (5738) | 40.9% | 57.2% | 9.8% | 21.6% |
| OTHER | 155 | 7.7% | 7.0% | 0.1% | {"execution": 5, "market_freshness": 2, "model_calibration_or_unknown": 2, "coverage": 1, "mapping": 1, "market_freshness/coverage": 1} | 8.22 | 0.1411 / 0.1522 (42) | 31.0% | 7.7% | 5.8% | 7.7% |
| WTA | 4,772 | 6.1% | 5.1% | 1.7% | {"market_freshness": 110, "model_calibration_or_unknown": 51, "coverage": 40, "execution": 29, "data": 24, "model_calibration": 21, "market_freshness/coverage": 13, "mapping": 1} | 7.69 | 0.2299 / 0.2206 (768) | 29.7% | 2.0% | 1.3% | 3.6% |
| WTA125 | 2,583 | 11.3% | 9.9% | 1.7% | {"market_freshness": 91, "model_calibration_or_unknown": 56, "market_freshness/coverage": 43, "data": 41, "execution": 24, "model_calibration": 20, "coverage": 14, "mapping": 4} | 9.17 | 0.2071 / 0.1891 (770) | 28.9% | 10.7% | 4.2% | 7.4% |

## 13. Top 50 largest discrepancies (one per event)

| # | event | level | model | model / Kalshi | gap | cause | identity | fresh | external | data | outcome | explanation |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | `KXITFWMATCH-26OCT14MAZBUL-BUL` | ITF_WOMEN | fair_v1 | 97% / 2% | +96 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 91 min (STALE); data POOR (grade D, thinner serve sample 206.0, ratio 16.58); no external reference |
| 2 | `KXITFMATCH-26NOV05VANBAI-BAI` | ITF_MEN | fair_v1 | 95% / 2% | +93 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 8.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 523 min (STALE); data POOR (grade D, thinner serve sample 786.0, ratio 1.52); no external reference |
| 3 | `KXITFMATCH-26NOV05ARCOMA-OMA` | ITF_MEN | fair_v1 | 91% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 638 min (STALE); data POOR (grade D, thinner serve sample 522.0, ratio 4.78); no external reference |
| 4 | `KXITFWMATCH-26OCT28THOBAC-BAC` | ITF_WOMEN | fair_v1 | 90% / 2% | +89 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 286 min (STALE); data LIMITED (grade C, thinner serve sample 1699.0, ratio 1.98); no external reference |
| 5 | `KXITFWMATCH-26OCT01MESSNI-SNI` | ITF_WOMEN | gen1_ledger | 93% / 5% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.1h before the model priced it (a finished match); the quote was captured 18 min before settlement (in-play print); quote age at model time 207 min (STALE); data LIMITED (grade C, thinner serve sample 688.0, ratio 5.27); no external reference |
| 6 | `KXITFMATCH-26OCT07BENGEN-BEN` | ITF_MEN | fair_v1 | 94% / 6% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 19 min (AGING); data LIMITED (grade C, thinner serve sample 856.0, ratio 2.47); no external reference |
| 7 | `KXITFWMATCH-26OCT20BOUVRA-VRA` | ITF_WOMEN | fair_v1 | 91% / 2% | +88 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 74 min (STALE); data LIMITED (grade C, thinner serve sample 476.0, ratio 6.57); no external reference |
| 8 | `KXITFMATCH-26OCT28MACBAI-BAI` | ITF_MEN | fair_v1 | 88% / 2% | +87 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 12.8h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 773 min (STALE); data POOR (grade F, thinner serve sample 153.0, ratio 25.42); no external reference |
| 9 | `KXITFMATCH-26OCT20BROGHA-BRO` | ITF_MEN | fair_v1 | 87% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 507 min (STALE); data LIMITED (grade C, thinner serve sample 399.0, ratio 4.2); no external reference |
| 10 | `KXITFWMATCH-26OCT27BARMUS-MUS` | ITF_WOMEN | fair_v1 | 88% / 2% | +86 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 8.5h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 517 min (STALE); data LIMITED (grade C, thinner serve sample 1840.0, ratio 1.21); no external reference |
| 11 | `KXITFWMATCH-26OCT19OVCSUN-OVC` | ITF_WOMEN | gen1_ledger | 90% / 6% | +85 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 14 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 1617.39); no external reference |
| 12 | `KXWTADOUBLES-26SEP13KOZLUMDAYZAR-DAYZAR` | DOUBLES | gen1_ledger | 88% / 3% | +85 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.5h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 44 min (STALE); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 13 | `KXATPCHALLENGERMATCH-26OCT13BUEZEI-BUE` | CHALLENGER | fair_v1 | 86% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.6h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 226 min (STALE); data LIMITED (grade C, thinner serve sample 747.0, ratio 5.6); no external reference |
| 14 | `KXATPCHALLENGERMATCH-26OCT27HARJAS-HAR` | CHALLENGER | fair_v1 | 87% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.8h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 113 min (STALE); no external reference |
| 15 | `KXITFMATCH-26OCT06BROTRU-BRO` | ITF_MEN | fair_v1 | 88% / 4% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 209 min (STALE); data LIMITED (grade C, thinner serve sample 1162.0, ratio 1.68); no external reference |
| 16 | `KXATPCHALLENGERDOUBLES-26OCT08DRZKALKARPAU-KARPAU` | DOUBLES | gen1_ledger | 88% / 4% | +84 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 17 | `KXITFWMATCH-26OCT19CABSED-CAB` | ITF_WOMEN | gen1_ledger | 92% / 8% | +84 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 31 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 674.0, ratio 5.72); no external reference |
| 18 | `KXATPCHALLENGERMATCH-26OCT05PURPEL-PUR` | CHALLENGER | fair_v1 | 85% / 2% | +84 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 1.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 86 min (STALE); no external reference |
| 19 | `KXITFWMATCH-26OCT11SIMMON-SIM` | ITF_WOMEN | fair_v1 | 88% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.2h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 23 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 179.6); no external reference |
| 20 | `KXITFMATCH-26OCT23DELVUJ-DEL` | ITF_MEN | fair_v1 | 89% / 6% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.6h before the model priced it (a finished match); the quote was captured 5 min before settlement (in-play print); quote age at model time 43 min (STALE); data POOR (grade D, thinner serve sample 65.0, ratio 18.47); no external reference |
| 21 | `KXITFMATCH-26OCT21SENBRA-BRA` | ITF_MEN | fair_v1 | 86% / 4% | +83 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 8 min before settlement (in-play print); quote age at model time 52 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 1799.43); no external reference |
| 22 | `KXITFWMATCH-26SEP30VANDAY-DAY` | ITF_WOMEN | fair_v1 | 88% / 5% | +83 | UNEXPLAINED_MODEL_DISAGREEMENT | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | ADEQUATE | -- | quote age at model time 28 min (AGING); no external reference |
| 23 | `KXITFWMATCH-26OCT08ANDSEN-SEN` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.5h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 633 min (STALE); data POOR (grade D, thinner serve sample 611.0, ratio 3.54); no external reference |
| 24 | `KXITFMATCH-26OCT15MUESEL-SEL` | ITF_MEN | fair_v1 | 86% / 4% | +82 | STALE_QUOTE | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | -- | quote age at model time 85 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 2214.28); no external reference |
| 25 | `KXITFWMATCH-26NOV05KOVMUN-KOV` | ITF_WOMEN | fair_v1 | 86% / 4% | +82 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 9.4h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 573 min (STALE); data POOR (grade D, thinner serve sample 269.0, ratio 7.71); no external reference |
| 26 | `KXITFMATCH-26OCT27ROTKOB-ROT` | ITF_MEN | gen1_ledger | 87% / 4% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 8 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade C, thinner serve sample 1144.0, ratio 3.85); no external reference |
| 27 | `KXITFWMATCH-26OCT19KOLHAY-KOL` | ITF_WOMEN | gen1_ledger | 89% / 8% | +82 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 632.0, ratio 4.16); no external reference |
| 28 | `KXITFWMATCH-26OCT22HAAGIZ-HAA` | ITF_WOMEN | gen1_ledger | 84% / 2% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 21 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade F, thinner serve sample 808.0, ratio 3.92); no external reference |
| 29 | `KXITFWMATCH-26OCT14KUMKOT-KOT` | ITF_WOMEN | fair_v1 | 88% / 7% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 704 min (STALE); data LIMITED (grade C, thinner serve sample 1232.0, ratio 2.39); no external reference |
| 30 | `KXITFMATCH-26OCT02MADPAA-MAD` | ITF_MEN | fair_v1 | 90% / 8% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 7.7h before the model priced it (a finished match); the quote was captured 12 min before settlement (in-play print); quote age at model time 476 min (STALE); data LIMITED (grade C, thinner serve sample 1300.0, ratio 1.14); no external reference |
| 31 | `KXITFWMATCH-26OCT28NAVTIK-TIK` | ITF_WOMEN | fair_v1 | 93% / 12% | +81 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | YES | quote age at model time 34 min (STALE); data LIMITED (grade C, thinner serve sample 845.0, ratio 3.15); no external reference |
| 32 | `KXITFWMATCH-26OCT27SMIELJ-SMI` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | NO | the quote was captured 22 min before settlement (in-play print); quote age at model time 0 min (FRESH); data LIMITED (grade B, thinner serve sample 1798.0, ratio 1.11); no external reference |
| 33 | `KXITFMATCH-26OCT14HONHUA-HUA` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.8h before the model priced it (a finished match); the quote was captured 9 min before settlement (in-play print); quote age at model time 236 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 920.39); no external reference |
| 34 | `KXITFMATCH-26OCT20KIVBEL-KIV` | ITF_MEN | fair_v1 | 82% / 2% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 10.3h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 627 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 951.34); no external reference |
| 35 | `KXITFWMATCH-26OCT20IVADES-DES` | ITF_WOMEN | gen1_ledger | 88% / 8% | +81 | IN_PLAY_QUOTE | VERIFIED | FRESH | NO_EXTERNAL_REFERENCE | POOR | NO | the quote was captured 9 min before settlement (in-play print); quote age at model time 0 min (FRESH); data POOR (grade D, thinner serve sample 528.0, ratio 3.67); no external reference |
| 36 | `KXITFWMATCH-26OCT07BURSTE-STE` | ITF_WOMEN | fair_v1 | 84% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 5.3h before the model priced it (a finished match); the quote was captured 10 min before settlement (in-play print); quote age at model time 329 min (STALE); data POOR (grade F, thinner serve sample 191.0, ratio 7.98); no external reference |
| 37 | `KXITFMATCH-26SEP23MORPOU-POU` | ITF_MEN | gen1_ledger | 85% / 4% | +81 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 1.1h before the model priced it (a finished match); the quote was captured 6 min before settlement (in-play print); quote age at model time 73 min (STALE); data POOR (grade F, thinner serve sample 590.0, ratio 13.93); no external reference |
| 38 | `KXITFWMATCH-26OCT22TICOBR-TIC` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 2 min before settlement (in-play print); quote age at model time 369 min (STALE); data POOR (grade D, thinner serve sample 929.0, ratio 1.77); no external reference |
| 39 | `KXITFMATCH-26OCT13KELBAI-BAI` | ITF_MEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 6.1h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 376 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 193.35); no external reference |
| 40 | `KXITFMATCH-26OCT01CHAVAN-CHA` | ITF_MEN | fair_v1 | 84% / 4% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | NO | Kalshi had settled this market 0.7h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 55 min (STALE); data LIMITED (grade A, thinner serve sample 2787.0, ratio 1.19); no external reference |
| 41 | `KXITFWMATCH-26OCT09GARROU-GAR` | ITF_WOMEN | fair_v1 | 83% / 3% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 2.4h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 149 min (STALE); no external reference |
| 42 | `KXITFWMATCH-26OCT16PETGLU-GLU` | ITF_WOMEN | fair_v1 | 83% / 2% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | ADEQUATE | NO | Kalshi had settled this market 3.4h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 213 min (STALE); no external reference |
| 43 | `KXITFMATCH-26OCT31SOTREN-SOT` | ITF_MEN | fair_v1 | 86% / 6% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 3.3h before the model priced it (a finished match); the quote was captured 4 min before settlement (in-play print); quote age at model time 203 min (STALE); data POOR (grade D, thinner serve sample 468.0, ratio 8.94); no external reference |
| 44 | `KXITFMATCH-26OCT23GOGYME-GOG` | ITF_MEN | fair_v1 | 88% / 8% | +80 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | AGING | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 0.1h before the model priced it (a finished match); the quote was captured 20 min before settlement (in-play print); quote age at model time 28 min (AGING); identity AMBIGUOUS (identity_confidence); data POOR (grade F, thinner serve sample 0.0, ratio 74.94); no external reference |
| 45 | `KXITFWMATCH-26OCT13BIOCAS-BIO` | ITF_WOMEN | fair_v1 | 81% / 2% | +80 | STALE_QUOTE | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | LIMITED | -- | quote age at model time 233 min (STALE); data LIMITED (grade C, thinner serve sample 766.0, ratio 1.09); no external reference |
| 46 | `KXITFWMATCH-26SEP23PISLIZ-PIS` | ITF_WOMEN | gen1_ledger | 19% / 98% | -79 | IN_PLAY_QUOTE | VERIFIED | AGING | NO_EXTERNAL_REFERENCE | POOR | YES | the quote was captured 15 min before settlement (in-play print); quote age at model time 13 min (AGING); data POOR (grade F, thinner serve sample 242.0, ratio 7.19); no external reference |
| 47 | `KXATPCHALLENGERDOUBLES-26NOV05REYSTABLAZHE-BLAZHE` | DOUBLES | gen1_ledger | 90% / 11% | +79 | IN_PLAY_QUOTE | AMBIGUOUS | FRESH | NO_EXTERNAL_REFERENCE | LIMITED | YES | the quote was captured 5 min before settlement (in-play print); quote age at model time 0 min (FRESH); identity AMBIGUOUS (identity_confidence, discipline); data LIMITED (grade C, thinner serve sample None, ratio None); no external reference |
| 48 | `KXITFWMATCH-26OCT27BANLAN-BAN` | ITF_WOMEN | fair_v1 | 92% / 14% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 7.1h before the model priced it (a finished match); the quote was captured 17 min before settlement (in-play print); quote age at model time 446 min (STALE); data POOR (grade F, thinner serve sample 155.0, ratio 11.81); no external reference |
| 49 | `KXITFMATCH-26OCT14PORGON-POR` | ITF_MEN | fair_v1 | 82% / 2% | +79 | MARKET_ALREADY_SETTLED_WHEN_PRICED | VERIFIED | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.6h before the model priced it (a finished match); the quote was captured 7 min before settlement (in-play print); quote age at model time 282 min (STALE); data POOR (grade F, thinner serve sample 0.0, ratio 205.18); no external reference |
| 50 | `KXITFMATCH-26OCT30MAUELS-ELS` | ITF_MEN | fair_v1 | 83% / 4% | +78 | MARKET_ALREADY_SETTLED_WHEN_PRICED | AMBIGUOUS | STALE | NO_EXTERNAL_REFERENCE | POOR | NO | Kalshi had settled this market 4.0h before the model priced it (a finished match); the quote was captured 11 min before settlement (in-play print); quote age at model time 252 min (STALE); identity AMBIGUOUS (identity_confidence); data POOR (grade D, thinner serve sample 181.0, ratio 16.74); no external reference |

## 14. Answers (Part M)

* **1_huge_gaps_mostly_lower_tour**: `{"answer": "YES", "share_of_ge_25pp_from_non_main_tour": 0.9698, "by_level_share_of_ge_25pp": {"ATP": 0.0136, "CHALLENGER": 0.1065, "DOUBLES": 0.0673, "ITF_MEN": 0.3253, "ITF_WOMEN": 0.4531, "OTHER": 0.0007, "WTA": 0.0166, "WTA125": 0.0169}}`
* **2_ge_25pp_caused_by_stale_prices**: `{"share_quote_older_than_30min_at_model_time": 0.5332, "share_primary_cause_market_settled_or_in_play": 0.4323, "share_primary_cause_stale_quote_only": 0.1945}`
* **3_ge_25pp_identity_or_ticker_problems**: `{"identity_or_orientation_FAILED": 0, "n_ge_25pp": 17380, "identity_ambiguous_share": 0.2029, "ticker_orientation": {"VERIFIED": 17380}}`
* **4_external_agrees_with_kalshi_not_model**: `{"all_ge_25pp": {"n": 11437, "with_external": 608, "coverage": 0.0532, "external_status": {"EXTERNAL_STALE": 389, "AGREES_WITH_KALSHI": 206, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 389, "MODEL_LONE_OUTLIER": 206, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3388, "share_external_supports_model": 0.0214}, "pregame_clean_ge_25pp": {"n": 5401, "with_external": 578, "coverage": 0.107, "external_status": {"EXTERNAL_STALE": 366, "AGREES_WITH_KALSHI": 199, "SUPPORTS_MODEL_DIRECTION": 12, "AGREES_WITH_MODEL": 1}, "triangulation": {"INSUFFICIENT_INPUTS": 366, "MODEL_LONE_OUTLIER": 199, "ALL_THREE_DISAGREE": 12, "KALSHI_LONE_OUTLIER": 1}, "share_external_agrees_with_kalshi": 0.3443, "share_external_supports_model": 0.0225}}`
* **5_extreme_gaps_and_thin_samples**: `{"median_thinner_serve_points": 490.0, "median_sample_ratio": 2.46, "median_min_matches": 19.0, "median_max_days_since_last": 239.0, "share_severe_asymmetry": 0.2088, "data_status": {"POOR": 9771, "LIMITED": 4514, "ADEQUATE": 3095}, "comparison_lt_10pp": {"median_thinner_serve_points": 1719.0, "median_sample_ratio": 1.7, "median_min_matches": 89.0}}`
* **6_sample_asymmetry_overconfidence**: `{"2-4x": {"n": 1411, "model_minus_observed": 0.0578, "kalshi_minus_observed": -0.0814, "brier_diff_model_minus_kalshi": 0.0007}, "4-10x": {"n": 964, "model_minus_observed": 0.0895, "kalshi_minus_observed": -0.0554, "brier_diff_model_minus_kalshi": 0.0091}, "<2x": {"n": 3430, "model_minus_observed": 0.0999, "kalshi_minus_observed": -0.0232, "brier_diff_model_minus_kalshi": 0.0145}, ">=10x": {"n": 1186, "model_minus_observed": 0.1164, "kalshi_minus_observed": -0.0569, "brier_diff_model_minus_kalshi": 0.0146}}`
* **7_gen2_too_extreme**: `{"gen2": {"n": 6991, "model": {"intercept": -0.556, "slope": 0.826, "slope_se": 0.03}, "kalshi_mid_same_rows": {"intercept": 0.188, "slope": 1.078, "slope_se": 0.034}, "mean_extremity_model": 0.1736, "mean_extremity_kalshi": 0.1699, "model_brier": 0.2327, "kalshi_brier": 0.2032, "brier_diff_model_minus_kalshi": 0.0295, "brier_diff_se": 0.0023, "model_logloss": 0.6625, "kalshi_logloss": 0.5886}, "fair_v1": {"n": 6991, "model": {"intercept": -0.446, "slope": 1.032, "slope_se": 0.033}, "kalshi_mid_same_rows": {"intercept": 0.257, "slope": 1.107, "slope_se": 0.034}, "mean_extremity_model": 0.1694, "mean_extremity_kalshi": 0.1695, "model_brier": 0.2143, "kalshi_brier": 0.2033, "brier_diff_model_minus_kalshi": 0.0109, "brier_diff_se": 0.0018, "model_logloss": 0.6174, "kalshi_logloss": 0.5888}, "gen1_elo": {"n": 6991, "model": {"intercept": -0.434, "slope": 1.011, "slope_se": 0.032}, "kalshi_mid_same_rows": {"intercept": 0.258, "slope": 1.097, "slope_se": 0.034}, "mean_extremity_model": 0.1759, "mean_extremity_kalshi": 0.1696, "model_brier": 0.2135, "kalshi_brier": 0.2034, "brier_diff_model_minus_kalshi": 0.0101, "brier_diff_se": 0.0018, "model_logloss": 0.6162, "kalshi_logloss": 0.5889}}`
* **8_fair_v1_reduces_pathological_gaps**: `{"all": {"fair_v1": {"share_ge_25": 0.2469, "share_ge_15": 0.443, "median_abs_gap": 13.02, "n": 46331}, "gen1_elo": {"share_ge_25": 0.2437, "share_ge_15": 0.439, "median_abs_gap": 12.79, "n": 46331}, "gen1_sr": {"share_ge_25": 0.3128, "share_ge_15": 0.52, "median_abs_gap": 15.8, "n": 46331}, "gen2": {"share_ge_25": 0.3131, "share_ge_15": 0.5095, "median_abs_gap": 15.44, "n": 46331}}, "pregame_clean": {"fair_v1": {"share_ge_25": 0.151, "share_ge_15": 0.3534, "median_abs_gap": 10.71, "n": 35768}, "gen1_elo": {"share_ge_25": 0.1487, "share_ge_15": 0.3485, "median_abs_gap": 10.49, "n": 35768}, "gen1_sr": {"share_ge_25": 0.2165, "share_ge_15": 0.44, "median_abs_gap": 13.0, "n": 35770}, "gen2": {"share_ge_25": 0.2308, "share_ge_15": 0.4388, "median_abs_gap": 12.86, "n": 35770}}}`
* **9_main_tour_gaps_small**: `{"ATP": {"median_abs_gap_pregame_clean": 5.53, "share_ge_25_all": 0.0379, "share_ge_25_pregame_clean": 0.0328}, "WTA": {"median_abs_gap_pregame_clean": 7.69, "share_ge_25_all": 0.0606, "share_ge_25_pregame_clean": 0.0513}}`
* **10_strong_independent_market_proxy**: `{"share_within_5pp_all": 0.2369, "share_within_10pp_all": 0.4391, "share_within_10pp_pregame_clean": 0.4917, "corr_model_vs_mid_pregame_clean": 0.8513}`
* **11_most_trustworthy_range_as_handicapping_input**: `{"basis": "DESCRIPTIVE ONLY: where the model's Brier is closest to Kalshi's on pregame-clean first observations; not a strategy and not an optimised cutoff", "fair_v1_by_bucket": {"0-3": {"n_settled": 1005, "model_brier": 0.197, "kalshi_brier": 0.1974, "brier_diff_model_minus_kalshi": -0.0003}, "10-15": {"n_settled": 1211, "model_brier": 0.2183, "kalshi_brier": 0.2092, "brier_diff_model_minus_kalshi": 0.0091}, "15-25": {"n_settled": 1550, "model_brier": 0.2244, "kalshi_brier": 0.208, "brier_diff_model_minus_kalshi": 0.0164}, "25-40": {"n_settled": 890, "model_brier": 0.2225, "kalshi_brier": 0.2038, "brier_diff_model_minus_kalshi": 0.0187}, "3-5": {"n_settled": 644, "model_brier": 0.2051, "kalshi_brier": 0.205, "brier_diff_model_minus_kalshi": 0.0}, "40+": {"n_settled": 186, "model_brier": 0.2966, "kalshi_brier": 0.1748, "brier_diff_model_minus_kalshi": 0.1217}, "5-10": {"n_settled": 1505, "model_brier": 0.2009, "kalshi_brier": 0.2002, "brier_diff_model_minus_kalshi": 0.0007}}}`

## 15. Model change recommendation

**MODEL_CHANGE_RECOMMENDED = TRUE** (not implemented in this change).

* exact_defect: Gen-1 doubles match-winner probabilities (ELO_DP_FAIR on team ratings) carry no measurable skill on pregame-clean first observations -- Brier no better than a coin flip and far worse than Kalshi -- while being very confident (e.g. 92% / 8%); TOO_EXTREME:gen2: probabilities too extreme for their evidence; TOO_EXTREME:gen1_ledger: probabilities too extreme for their evidence
* affected_populations: ['NO_SKILL:gen1_ledger|DOUBLES', 'TOO_EXTREME:gen1_ledger', 'TOO_EXTREME:gen2']
* proposed_generic_correction: Doubles: stop publishing a doubles probability as a model number until a doubles model passes its own validation -- generically, a model slice that fails criterion B is shown as UNVALIDATED (no probability, no gap). Over-extreme models: a single pre-registered shrinkage of logit(p) toward 0.5 whose strength depends only on evidence depth, fitted walk-forward on pre-freeze history, never on these prospective rows or on P&L.
* prospective_validation_plan: any corrected model is frozen as a NEW candidate beside the current one (no frozen file edited) and scored prospectively on pregame-clean, first-observation-per-match rows from its own effective start; it replaces nothing unless Brier and log loss improve with the 95% interval of the paired difference excluding zero at a pre-registered minimum N
* evidence: `{"TOO_EXTREME:gen2": {"model_slope": {"intercept": -0.556, "slope": 0.826, "slope_se": 0.03}, "kalshi_slope": {"intercept": 0.188, "slope": 1.078, "slope_se": 0.034}, "n": 6991}, "TOO_EXTREME:gen1_ledger": {"model_slope": {"intercept": -0.483, "slope": 0.867, "slope_se": 0.024}, "kalshi_slope": {"intercept": 0.178, "slope": 1.076, "slope_se": 0.029}, "n": 9231}, "NO_SKILL:gen1_ledger|DOUBLES": {"n_settled": 620, "model_brier": 0.2976, "kalshi_brier": 0.2337, "brier_diff_model_minus_kalshi": 0.0639, "brier_diff_se": 0.0118, "corr_model_outcome": 0.0972, "corr_kalshi_outcome": 0.2717}}`

## 16. Unresolved questions

* Strict CLV exists only for ATP/WTA main tour (first-ball truth); lower-tour large gaps cannot be priced against a strict close.
* Historical surface-specific sample sizes per observation are not stored by the producers; only today's state exists.
* Settlement timing is a hindsight proxy for in-play quotes at ITF/Challenger; a quote captured within 45-120 min of settlement may still have been pregame for a short match.
* External coverage (Bovada/Smarkets) of ITF is thin, so most lower-tour extremes have no independent reference.
* Whether the frozen candidates' own evidence harvests exclude post-settlement shadow rows is not re-audited here (their exclusion rules are frozen); the candidate harvester's post-start guard should be checked separately.
* No assisted decision exists yet, so quote age at assisted decision time cannot be measured.
