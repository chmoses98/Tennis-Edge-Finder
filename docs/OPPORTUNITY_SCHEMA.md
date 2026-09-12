# The Opportunity object

One market, one side, one moment, one decision. Everything the system used to reach that decision travels
on the object, and the object cannot be edited afterwards.

`tennis_edge/opportunity/schema.py`. Store: `data/research/opportunities/<UTC day>.jsonl`, append-only and
hash-chained.

## Why it exists

A decision whose inputs are not written down cannot be audited, and a decision that can be edited once the
outcome is known is not evidence of anything. Three properties are enforced in code rather than described
here:

* **Immutable.** The dataclass is frozen and the fingerprint covers every field. `evolve()` returns a NEW
  object with its own fingerprint; there is no in-place edit anywhere in the codebase.
* **No real-money state.** `authority` is a constant, `RESEARCH_ONLY_NO_REAL_MONEY`, and the constructor
  rejects anything else. The decision enum has exactly three members and none of them is a wager.
* **A SHADOW_BET must survive qualification and must state the case against itself.** Construction fails if
  any qualification filter is False, if the qualification dict is empty, if `reason_against` is blank, or
  if the market is POST_START.

## Fields

| group | fields |
|---|---|
| identity | `opportunity_id`, `generated_at`, `physical_match_id`, `event`, `ticker`, `family`, `side`, `strike` |
| our number | `lane`, `model_version`, `fair_prob`, `uncertainty`, `fair_prob_low`, `fair_prob_high` |
| the market | `executable_ask`, `executable_bid`, `midpoint`, `spread`, `available_size`, `fee_per_contract` |
| the edge | `raw_edge`, `fee_adjusted_edge`, `uncertainty_adjusted_edge`, `robust_edge`, `bet_up_to`, `ev_curve` |
| the evidence | `data_quality_score`, `data_quality_grade`, `serve_evidence_points`, `identity_confidence`, `source_freshness_days` |
| when | `first_ball_classification`, `first_ball_confidence`, `seconds_to_first_ball`, `seconds_to_first_ball_basis`, `quote_age_seconds` |
| context | `market_movement`, `liquidity_context` |
| the decision | `selector_score`, `selector_version`, `decision`, `reason_for`, `reason_against`, `candidate_ids`, `qualification` |
| provenance | `authority`, `schema_version`, `fingerprint` |

Prices are dollars in [0, 1] and always describe the named `side`. `midpoint` is carried because it is
informative and is never the basis of an edge.

## The four edges are four different things

| name | definition | what it is for |
|---|---|---|
| `raw_edge` | `fair - ask` | what a naive screen prints |
| `fee_adjusted_edge` | `raw - fee` | what the exchange leaves. The taker fee peaks near 1.75c at even money; a 1c "edge" is a losing trade |
| `uncertainty_adjusted_edge` | fee-adjusted less one half-width of the perturbation envelope | our own parameter uncertainty, priced |
| `robust_edge` | `min(fair over every configuration) - ask - fee` | the worst case over the defensible parameter set |

`bet_up_to` is the highest whole-cent price at which the trade is still non-negative after the REAL fee,
which Kalshi rounds up to the cent. `ev_curve` gives EV per contract at the ask and at 1, 2, 3 and 5 cents
worse.

## Qualification

`tennis_edge/opportunity/qualify.py`, policy `qualify_v1`, frozen and versioned. Twelve checks; every one
must pass before a row can be a SHADOW_BET: contract semantics known, identity safe (>= 0.95), a model
probability exists, a two-sided executable price exists, the quote is under an hour old, size is behind it,
spread <= 6c, the price is out of the tails (2c-98c), the fee is known, the market is not POST_START, no
critical health gate relevant to the market is broken, data quality >= 0.40.

One deliberate asymmetry: **START_UNKNOWN does not block qualification; POST_START does.** At the levels
Kalshi actually lists there is no A/B first-ball source, and blocking would end the research rather than
protect it. START_UNKNOWN is carried forward as itself, is never relabelled STRICT_PREGAME, and every
consumer displays it.

## What the historical research rows cannot tell you

The candle archive carries no order-book depth, so in `research/selector/opportunities.parquet`
`available_size` is an open-interest proxy and every economic figure assumes ONE contract at the last
displayed ask. The live board reads real displayed depth from the capture.
