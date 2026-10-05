# Model card -- Projection V2 (`projection_v2.0`)

| | |
|---|---|
| Purpose | Independent pre-match probability that player A beats player B in men's/women's professional singles, and (through one exact scoring distribution) every derivative market Kalshi lists on the match |
| Owner | tennis-edge-finder (research; real-money authority OFF) |
| Version | `projection_v2.0`, frozen spec `40e74a71621a24ff` (`FROZEN_CHALLENGER.json`), 2026 coefficients fingerprint in `config/projection_v2/coefficients.json` |
| Status | Promoted 2026-10-05 by the preregistered rules (P1-P8 pass; P9 operational checks in the PR). Incumbent kept on every row; rollback = `production_model: "incumbent"` |
| Inputs | Match results and serve/return statistics (Sackmann forks, TML + mirror, ESPN results), player ages. **No market data.** |
| Not inputs | Rankings (no current free feed), injuries/withdrawals, weather, travel, court speed, odds of any kind |
| Output | `p` (format-adjusted), envelope `[p_low, p_high]`, grade HIGH/MEDIUM/LOW/POOR, warning tags, evidence, components, fingerprints |

## Training and evaluation

* Ratings replayed chronologically from 1990; stacker fitted walk-forward (season Y on seasons Y-6..Y-1).
* Selection 2016-2020; evaluation 2021-2024; validation 2025; holdout 2026 YTD (each revealed once, in order).
* Paired comparisons with a cluster bootstrap over tournament instances.

Headline (Brier, lower is better; `RESULTS.md` for everything):

| window | ATP incumbent (Brier / LL) | ATP V2 | ATP V2 - incumbent [95% CI] | WTA incumbent | WTA V2 | WTA V2 - incumbent [95% CI] |
|---|---|---|---|---|---|---|
| 2021-2025 | 0.2073 / 0.6005 | 0.1989 / 0.5808 | -0.0084 [-0.0088, -0.0080] | 0.1979 / 0.5794 | 0.1833 / 0.5420 | -0.0146 [-0.0151, -0.0141] |
| 2026-holdout | 0.2083 / 0.6034 | 0.2003 / 0.5846 | -0.0080 [-0.0092, -0.0070] | 0.2040 / 0.5930 | 0.1968 / 0.5760 | -0.0072 [-0.0088, -0.0056] |

Numbers copied from `results_summary.json` (written by `write_report.py`).

## Intended use

* The independent number on the Sift / Edge Finder app and the assisted slate, with its envelope and grade.
* A research baseline whose disagreement with the market is a QUESTION for review, not an edge.

## Out of scope / misuse

* Autonomous or real-money betting (authority OFF; no order surface exists).
* Treating a large model-market gap as an opportunity: on Pinnacle-linked ATP matches the side V2 prefers by
  20pp+ wins about as often as the market implied, not as V2 implied.
* Doubles (V2 is singles-only; doubles stay on the unvalidated baseline, grade capped).
* Team events, exhibitions, formats the registry cannot resolve (fail closed upstream).

## Performance by segment

Every tour x level segment with n >= 2,000 improves or is not significantly worse (rule P5). The gain is
largest at ITF level (the incumbent's ratings were too slow there) and smallest at tour level, where V2 and
the incumbent are within a few thousandths of Brier.

## Limitations

1. **Data freshness is the binding constraint.** No free, permitted source publishes ITF results after
   2026-04-27 (WTA) / 2026-06-01 (ATP) or WTA 125 results outside ESPN's partial coverage; ATP Challenger (TML
   mirror) lags ~2 weeks. Live ITF projections are therefore graded POOR, with schedule features neutralised.
   This is also why most open ITF players are UNMAPPED: they appear in no source we can reach.
2. **WTA serve statistics stop 2026-04-27.** Gen-2 is starved for women; the stacker shrinks Gen-2's weight
   by evidence, so this degrades gracefully but it is a real loss.
3. **ESPN rows carry no serve statistics, minutes, and often no surface;** ESPN level labels are unreliable
   (WTA 125 events labelled 250/500). This affects 2026 rows only and is visible in the 2026 holdout's smaller
   gain.
4. **The market is better.** V2 closes part of the gap to Pinnacle and adds essentially no information beyond
   it at tour level (post-freeze benchmark).
5. **Context features need complete data.** The layoff signal is the single largest gain in the backtest;
   live it is only usable where results are current (tour level). Where it is neutralised the model is
   calibrated as if both players had been active, which is the best available assumption, not a measurement.
6. **Rating drift under stale data** is an assumed 0.30 logits per sqrt(year), used only to widen the envelope --
   per level when the match's level is stale, and per player when a player is probably missing results from a
   level whose source stopped (PLAYER_RESULTS_INCOMPLETE; never graded HIGH).
7. **Frozen scoring-engine bug** (advantage-set tail, `docs/PROJECTION_ENGINE_V2.md` section 5): affects only
   pre-2022 formats; documented, not fixed in place because the file is a frozen source.
8. **2026 is not virgin territory** for the Elo family in general (earlier waves studied it); it was virgin for
   every V2 component, and a prospective comparison runs from 2026-10-05 (both models on every ledger row).
9. Identity: transliteration aliases (Pyotr/Petr) map at confidence 0.85 and are tagged; dropped-middle-name
   and spelling variants are review candidates only. Sackmann carries a few same-person duplicate ids
   (e.g. Anastasia/Anastasiia Grechkina); they are rated separately.

## Monitoring

* Every ledger row carries `models.INCUMBENT` and `models.V2`; the prospective paired comparison (PREREGISTRATION
  section 6) is reported after 1,500 independently settled matches and triggers rollback if it contradicts the
  backtest.
* Independent sports truth (TENNIS-8/9) grades settled rows from non-Kalshi results.
