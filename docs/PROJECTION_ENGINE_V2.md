# Projection Engine V2

An independent, pre-match tennis probability model: it estimates who wins (and, through one exact scoring
distribution, every derivative) from results and serve/return statistics alone. **No market price is an
input anywhere in `tennis_edge/v2/`** (`tests/test_v2_engine.py::test_v2_package_cannot_reach_a_price` walks
the import graph). Markets appear only downstream, beside the frozen output, and in a benchmark computed after
the model was frozen.

Status (2026-10-05): **promoted** by the preregistered rules (`research/projection_v2/PREREGISTRATION.md`,
`PROMOTION_DECISION.json`); production switch `config/projection_v2/production.json`. The incumbent
(`elo_surface_k_lo+sr_v0.1`) is still computed on every projection row (`models.INCUMBENT`) and a rollback is
one line in that file. Results: `research/projection_v2/RESULTS.md`; model card: `MODEL_CARD.md`.

```
canonical results (Sackmann / TML / ESPN; canonical_v2: deduplicated, crosswalked, new players minted)
   │  chronological replay (tennis_edge/v2/replay.py) -- every state read BEFORE the match is applied
   ├─► rating          margin-of-victory Elo with light surface pooling (E_mov_surf25)
   ├─► serve/return    Gen-2: opponent-adjusted, time-decayed, level- and surface-aware (half-lives 300 d and 60 d)
   ├─► form            opponent-adjusted rating residuals, 30-day half-life
   ├─► context         rest, layoffs (60 / 180 d), 14-day load, 7-day minutes, recent retirement, surface switch
   └─► age             youth / veteran indicators
   ▼
evidence-aware logistic stacker (tennis_edge/v2/stacker.py) -- antisymmetric features, no intercept,
L2, weights fitted walk-forward on the six previous seasons; doubles as outcome-only calibration
   ▼
P(A beats B) on the match format ──► point probabilities (Gen-2 service level) ──► exact DP distribution
   ▼                                                                               (every family, coherent)
uncertainty envelope + data-quality grade + warning tags (tennis_edge/v2/inference.py)
   ▼
run_tennis.py ledger row ─► assisted slate ─► app export (edge_finder.app.v1) ─► research explorer
```

## 1. Data (`tennis_edge/data/build.py`, `canonical_v2`)

Sources are unchanged in kind (Sackmann ATP/WTA forks, TML upstream + the gmalbert mirror, ESPN results), but
three defects were fixed:

| defect | effect | fix |
|---|---|---|
| exact-key dedupe across id systems | 85,008 duplicate matches: the TML Challenger mirror dates a match on the tournament's last day, Sackmann on its first, so ~80k Challenger matches entered twice; ESPN (per-match dates, "Round 2") duplicated ~1,750 tour matches | `tennis_edge/data/dedupe.py`: same canonical winner/loser, different id systems, within 16 days, identical sets+games (or same tournament id + round). Audited sample of the name-mismatched pairs: all true duplicates |
| mirror main-tour files ignored | ATP main-tour serve statistics stopped in May 2026 although the mirror carries them to September | loaded as `tml_ATP_main_mirror` |
| players unknown to Sackmann dropped | every player who turned professional after the Sackmann freeze had no rating at all | `identity/crosswalk.py::mint_new_players`: a foreign-only player gets a canonical id unless a canonical player shares surname + first initial (then NEAR_CANONICAL_MATCH, left for review) |

`build.py --legacy` reproduces `canonical_v1` for before/after studies. The data fix was judged on its own
(`DATA_FIX_DECISION.json`): deploy (incumbent model, v2 vs v1 data, not significantly worse on either tour).

## 2. Opponent adjustment, everywhere it matters

* **Rating.** Elo is opponent-adjusted by construction (result minus expected given the opponent's rating).
  The margin-of-victory multiplier scales K by dominance `(games_w - games_l) / (games_w + games_l)`
  (`k * (0.6 + 1.6 d)`) -- still a function of result minus expectation, so a rout of a weak opponent moves
  little. Retirements count at half weight, walkovers not at all.
* **Serve/return.** Gen-2 credits a server with `observed - baseline - level + returner's return ability` and
  a returner symmetrically (`tennis_edge/models/gen2.py`; orientation `pb = P(A wins a point on B's serve)`).
  Abilities are precision-weighted means against a zero prior worth 500 serve points; surface deviations have
  their own 1,500-point prior; level offsets are learnt from residuals.
* **Form.** Never a win-loss record: the decayed sum of `result - expected` under the reference Elo.

## 3. Rating tournament (C1)

Fifteen Elo variants were replayed side by side (`tennis_edge/v2/replay.py::ELO_VARIANTS`): plain, level prior,
K 180-320, slower K decay, surface pooling 0.25/0.5, level-specific K, margin of victory (two strengths, with
surface, with K 200), layoff K boost, and the incumbent configuration reproduced bit-for-bit (including Gen-1's
quirk of seeding a first surface rating from the post-update overall rating). On the 2016-2020 selection
window the incumbent configuration ranked **last** on both tours; margin-of-victory variants ranked first.
The gain is concentrated at ITF level, where the incumbent's low K (180, times 0.8 for ITF) left fast-moving
ratings stale.

## 4. Ensemble and calibration (D, E)

A regularised logistic regression with **no intercept and only antisymmetric features**, so
`P(A beats B) = 1 - P(B beats A)` exactly. Blocks were added greedily on 2016-2020 only (`selection_log.json`):

| block | kept | what the weights say (2026 coefficients, `config/projection_v2/coefficients.json`) |
|---|---|---|
| base `z = logit(Elo)` | -- | slope ~0.80: MOV Elo alone is over-confident; this is the outcome-only calibration |
| level slopes | yes | per-level sharpness (Slams sharper; WTA Challenger/ITF sharper) |
| experience buckets | no | no gain once the rest is in |
| Gen-2 by evidence bucket | yes | weight on `logit(Gen-2) - z` rises with the THINNER player's serve evidence: ~0 below 300 points, 0.15-0.35 at 1k-5k, 0.34-0.46 at 5k-20k |
| Gen-1 structural | no | adds nothing beyond Gen-2 |
| Gen-2 short half-life | yes | recent serve/return form, evidence >= 1,000 points |
| form (30 d) | yes | small positive |
| context | yes | the largest single gain: a 180+ day layoff (or debut) costs ~0.5-0.6 logit; 60-180 d ~0.15; surface switch, recent retirement, heavy recent minutes small negatives |
| age | yes | under-23 +0.15-0.17, over-30 -0.24..-0.32 per unit (ratings lag improving / declining players) |

Separate Platt / isotonic calibration was tested implicitly (`ELO+PLATT` lane) and is dominated by the stacker,
which is itself a walk-forward logistic recalibration with segment slopes.

## 5. Exact scoring layer (G)

Unchanged engine (`tennis_edge/sim/analytic.py`, a FROZEN source of the prospective experiments). New:
`tennis_edge/sim/vectorized.py`, the same recursion over numpy arrays (tested to 1e-9 against the scalar engine),
used by every study. While writing it a bug was found in the frozen engine's **advantage-set tail truncation**
(the 40-40 residual is split with `1 - P(break)` where `P(break)` belongs): with two strong servers ~6% of the
mass reaches the truncation and set probabilities move by up to ~0.04. Every ADVANTAGE format in
`config/formats.json` ended in 2021, so **no live price is affected**; the frozen file is not edited, the
vectorised engine is exact, and the test documents the gap.

V2 prices derivatives from ONE distribution: the V2 match probability is inverted to point probabilities with
the Gen-2 implied service level (`derivative_spw_rule: gen2`, chosen on 2023-2024). Against real scores
(`derivatives_eval.json`) every V2 distribution beats the incumbent on every proper score (total games RPS,
game-differential RPS, exact set score log score, deciding-set and over/under Brier) in both tours and both
windows.

## 6. Uncertainty and data quality (F)

`ProjectionV2.project()` returns, besides `p`:

* **envelope** `[p_low, p_high]`: the span of six coefficient variants fitted the same way (base, the
  second-best rating, no context, no structural blocks, weaker L2, 4-season window) plus, when the data are
  stale, a labelled rating-drift widening (`DRIFT_LOGIT_PER_SQRT_YEAR = 0.30`: an assumption, not a fit);
* **grade** HIGH / MEDIUM / LOW / POOR from identity confidence, rated matches, serve evidence, data staleness
  (level horizon and the player's own last result) and envelope width;
* **tags** THIN_RATING_HISTORY, NO_SERVE_EVIDENCE, CONTEXT_NEUTRALISED_STALE_DATA(nd), STALE_PLAYER_RATING(nd),
  PLAYER_RESULTS_INCOMPLETE(A~n over nd,...), IDENTITY_ALIAS, FORMAT_TRANSLATED, WIDE_ENVELOPE;
* evidence counts, components (Elo, Gen-2, service levels) and every fingerprint.

With V2 in production a projection is actionable in the RUN TENNIS report only at grade HIGH/MEDIUM and on a
FRESH quote; the assisted slate's discrepancy layer (TENNIS-17) is unchanged and still holds EXTREME gaps.

## 7. Inference lifecycle (I)

1. RUN TENNIS rebuilds `canonical_v2` and replays it into end states (`scripts/ops/build_v2_state.py`,
   ~1.5 min for both tours, `data/processed/v2/state_<tour>.json.gz`, published with the processed artifacts).
2. Coefficients are a COMMITTED artifact (`config/projection_v2/coefficients.json`, fingerprint inside):
   fitted for the live season on seasons Y-6..Y-1 exactly as in the backtest; the 2026 coefficients reproduce
   the 2026 holdout predictions bit-for-bit (asserted when they are fitted). They change only by a deliberate,
   versioned refit (`scripts/research/projection_v2/fit_coefficients.py --season 2027`).
3. `run_tennis.py` resolves identities, format and surface, calls `ProjectionV2.project` per singles event,
   prices every family from the V2 distribution (or the incumbent's if V2 is not production / fails to load),
   and writes both models, the V2 block (envelope, grade, tags, evidence, fingerprints, state build time and
   last result date) and `production_model` on every ledger row.
4. **Stale data.** No free source publishes ITF results after April (WTA) / June (ATP) 2026; ATP Challenger
   lags ~2 weeks. Live, a player with no recent result in our data would look laid off. When the match level's
   data horizon is more than 10 days old, the schedule features are neutralised for both players (difference
   0) and the projection is tagged and downgraded -- ITF projections are POOR today, by design.
   **Data horizon = source freshness (2026-10-05, after the first live run).** A level's horizon is the newest
   last result among the SOURCES that still cover it (>= 20 of its results in the final year of the source's
   own data), not the last date the level happened to have a match: Grand Slams are seasonal and would have
   read four months stale on the first day of every Slam, and ESPN files WTA 1000 events under 500/250. Levels
   whose only source stopped keep that source's date (ATP ITF 2026-06-01; WTA ITF and WTA 125 2026-04-27).
   **Player-level incompleteness.** The match level being current does not make both players' data current:
   on the first live board ITF-heavy Challenger players were missing ~4 months of ITF results and were graded
   HIGH. The state now stores each player's results per stale level in the year before its horizon; at
   inference the expected number of missing results is that rate times the days since the horizon. At >= 3
   (`MISSING_RESULTS_FLAG`) the projection is tagged PLAYER_RESULTS_INCOMPLETE, schedule features are
   neutralised exactly as for a stale level, the drift widening uses each player's own gap
   (1.645 * 0.30 * sqrt((gap_a + gap_b) / 365): the former formula when only the level is stale), HIGH is
   impossible and MEDIUM needs every gap <= 60 days. No price enters any of this.
5. **Parity.** `tests/test_v2_inference.py` rebuilds the one-row frame from persisted states and asserts it
   equals the replay's own record for the same match, then the same probability to 1e-12.

## 8. What V2 is not

* Not market-aware, and not tuned against any market sample. The post-freeze Pinnacle benchmark
  (`market_benchmark_v2.json`) shows V2 closes about a third of the incumbent's gap to Pinnacle on ATP main-tour
  matches and adds essentially no information the market lacks; large V2-market disagreements are mostly V2
  error. Real-money authority stays OFF.
* Not a cure for missing data. Most remaining error is information free, lagging results cannot carry
  (injury/withdrawal news, form beyond the data horizon, ITF results after the source freeze).

## 9. Known limitations

See `research/projection_v2/MODEL_CARD.md` section "Limitations".
