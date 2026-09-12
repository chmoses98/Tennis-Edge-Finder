# External market protocol

How an independent venue's price is allowed to become an opinion about Kalshi, and what it must survive
first.

## Why this exists

Wave 3 asked whether our own model's disagreement with Kalshi identifies Kalshi's errors. It does not:
the selector failed its holdout, the attractive composite rule failed its holdout, and on every subset
that returned a profit our probability was still less accurate than the price. Wave 4's hypothesis is
that a different market might succeed where our model failed.

So the roles are deliberately unequal:

    the EXTERNAL reference proposes,
    our MODEL corroborates or objects,
    and nothing our model says alone can produce a SHADOW_BET.

That asymmetry is enforced in `Dislocation.__post_init__`, not just described here.

## The pipeline

```
venue payload ──► ExternalMarketObservation ──► de-vig ──► reference ──┐
  (raw bytes archived,      (immutable,          (only whole   (median   │
   hash on every row)        fingerprinted)       markets)      across   ▼
                                                              groups)  triangulate ──► Dislocation
Kalshi capture ───────────────► same player registry ─────────────────►   ▲            (append-only,
  (executable ask, depth)         (a match is common only when              │             hash-chained)
                                   both venues agree who is playing)        │
frozen fair-price layer ────────────────────────────────────────────────────┘
  (Gen-2 blended, 13 configs; a WITNESS, never the plaintiff)
```

## De-vigging

A book quoting 1.90 / 1.90 is not saying 50/50; it is saying 50/50 plus 5.3% for itself. Comparing its
raw 52.6% against a Kalshi ask compares a price to a price-plus-margin, and the margin is larger than any
edge we could plausibly find.

Three methods are computed on every market and the disagreement between them is recorded:

| method | assumption | behaviour |
|---|---|---|
| proportional | margin spread evenly | the default; understates how books price longshots |
| power | `p^k` normalised to 1 | takes proportionally more out of longshots |
| shin | margin as insider insurance | between the two on a binary |

At even money all three agree to within a rounding error. On a 1.10 / 7.50 market they put the longshot at
12.8%, 10.2% and 11.2% — a 2.6-point spread, larger than any dislocation this project has ever measured.
`method_choice_is_material` flags that case, and a row so flagged must be treated as uncertain rather than
exact.

**The opposite side is never fabricated.** A market with one side suspended is stored with its raw implied
probability and no de-vigged value.

## The reference value

`build_reference` takes a median across INDEPENDENT GROUPS, pre-specified, never a fitted weighting. With
one venue and a few weeks of data any weight we estimated would be a description of the sample. A median
also guarantees that one venue with a broken line cannot drag the reference.

Staleness is checked in both directions and a failure excludes the observation rather than discounting it:

* **venue staleness** — the venue's own timestamp against when we fetched. Default bound 15 minutes.
* **capture age** — when we fetched against now. Default bound 15 minutes.

A venue that publishes no timestamp is recorded as unknown, never as zero.

## Triangulation

| class | meaning |
|---|---|
| `MARKETS_AGREE` | the two venues are within 2c. Nothing to see. |
| `MODEL_LONE_OUTLIER` | the venues agree and only we disagree. Wave 3 measured what that is worth. |
| `KALSHI_LONE_OUTLIER` | the venues disagree and our model is on the external side. **The hypothesis.** |
| `EXTERNAL_LONE_OUTLIER` | the venues disagree and our model sides with Kalshi. |
| `ALL_THREE_DISAGREE` | our model runs against the external venue too. |

Corroboration is about DIRECTION, not proximity: a model at 50% when the venue says 52% and Kalshi says
46% is agreeing that Kalshi is too low. A model that overshoots the venue is still corroboration, and the
row records `model_overshoots_external` so a reader can discount it.

## EXTERNAL_EDGE is a signal, not an edge

    EXTERNAL_EDGE = external fair - executable Kalshi ask - Kalshi taker fee

Never against the midpoint. Never against the bid. The fee is Kalshi's real ceil-to-cent taker fee, which
peaks near 1.75c at even money — so a one-cent dislocation is not a small edge, it is a loss.

## Decisions

PASS / WATCH / SHADOW_BET, and there is no fourth. A SHADOW_BET additionally requires the external
reference to exist, Kalshi to be the outlier, the edge to clear 2c after fees, the Kalshi quote to be
two-sided, fresh, inside a 6c spread and backed by size — and a stated reason against, which is never
empty.

WATCH is the right answer, not a consolation, when a dislocation is real but strict first-ball truth is
absent, liquidity is poor, or our model contradicts the external venue.

## What Wave 4 may not do

Retune Gen-1, Gen-2, `selector_v1` or the fair-price layer. Their version strings are asserted by a test.
Operational bug fixes are allowed; a fix that changes historical probabilities requires a new version and
leaves the frozen predictions alone.

## REAL-MONEY AUTHORITY: OFF

No object in this layer can express a wager, and no result so far argues for one.
