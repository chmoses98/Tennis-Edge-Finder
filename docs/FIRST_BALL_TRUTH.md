# First-ball truth

## The claim this machinery has to survive

> *This observation existed before the first ball.*

Before this wave, that claim rested on a Kalshi `occurrence_datetime`. It cannot. On this exchange the
nominal time is a scheduling artefact: for ITF and Challenger series it routinely falls **after** the
market has already closed, and on any court with a rolling order of play a match nominally at 14:00 can
begin at 16:40. A claim anchored to it is unfalsifiable, which is worse than being wrong.

So first-ball truth is a separate object, with its own evidence, its own confidence and its own
provenance, and every timing claim is derived from it.

## The bracket is the object

Except when a source states the start outright, what polling actually learns is a **bracket**: the match
was not in progress at `t0`, and was in progress at `t1`, so the first ball fell in `(t0, t1]`.

Every `FirstBallTruth` therefore carries `lower_bound_utc` and `upper_bound_utc`, and **classification
uses the bounds, never the point estimate**:

| condition | class |
|---|---|
| `captured_at < lower_bound` | `STRICT_PREGAME` |
| `captured_at >= upper_bound` | `POST_START` |
| inside the bracket | `AMBIGUOUS` |
| credible sources contradict | `AMBIGUOUS` |
| no trustworthy evidence | `START_UNKNOWN` |

An observation exactly **at** the first ball is `POST_START`, not pregame. An observation one second
after it is `POST_START`. The uncertainty lives in the data instead of being rounded away, which is what
lets the claim survive a hostile reading.

## Confidence

| level | meaning | eligible for strict research |
|---|---|---|
| **A** | an authoritative source states the actual start outright, or a source's claimed start is confirmed inside an independently observed bracket: zero width | yes |
| **B** | a timestamped live-state transition proves play began within a bracket no wider than 300 s | yes |
| **C** | indirect bound only: a wide bracket, a one-sided bound, a score back-cast, exchange-only evidence, or a match bound to the feed by a bare surname | **no** |
| **UNKNOWN** | insufficient evidence | no |

C is **never silently promoted**. `classify()` reports C as `START_UNKNOWN` unless a caller explicitly
passes `allow_indirect=True`, which strict research never does.

## Feed lag, and why the lower bound is widened

Every live-score feed lags reality by an unknown amount, and it lags in the direction that does damage:
a feed still showing *not started* when play has already begun pushes the observed lower bound **later**
than the true first ball, which would relabel genuinely post-start observations as strictly pregame.

No candidate source documents its latency. So the lower bound carries a conservative allowance
(`DEFAULT_LAG_ALLOWANCE_S = 120`), recorded on the truth and subtracted before any classification.
Measuring a source's real lag and shrinking its allowance on evidence is future work; until then the
allowance is what stops an undocumented feed from silently inflating the strict-pregame set.

## Reconciliation: no arbitrary winners

1. Each source is reduced to its own bracket. A source that has only ever said "not started" still
   contributes a one-sided lower bound, which is how one feed's `PRE` can combine with another feed's
   `IN`.
2. Brackets are **intersected**, because an intersection is the honest combination of witnesses.
3. Sources that share an upstream provider are merged **first**. ESPN's ATP and WTA boards return the
   same combined event during a Grand Slam; treating them as two agreeing witnesses would manufacture
   confidence that does not exist.
4. If two credible sports sources place the first ball in **disjoint** windows, or two explicit start
   times disagree by more than 300 s, that is a `MATERIAL` contradiction: both raw observations are
   kept, no winner is chosen, the truth drops to `UNKNOWN`, and strict CLV fails closed until a human
   reconciles it.
5. **Exchange evidence may narrow a sports bracket. It may never create one.** Kalshi in-play activity
   alone caps confidence at C. SPORTS_TRUTH and EXCHANGE_TRUTH remain separate objects, as they have
   been since the first version of this system.

## Identity, and the two Zverevs

A first-ball system fails silently if it binds the wrong match. Mapping onto a feed requires exactly one
candidate that fits both players better than any other; a tie, a cross-claim (two of our matches wanting
the same feed row) or a doubles/singles mismatch yields `AMBIGUOUS` and no mapping at all. A pairing that
rests on a bare surname with no initial to verify is reported `WEAK`, and a weak binding caps the
resulting truth at confidence C no matter how tight the bracket looks.

## Immutability

* Observations are append-only and hash-chained. They are written once and never edited.
* Truths are append-only too. Re-deriving from better evidence **appends** a row with
  `derivation_version + 1`; readers take the highest version per match.
* Classification is derived, not stored on the ledger row. A ledger row's `generated_at_utc` is never
  rewritten, by anything, ever. That is the line between recovering sports truth (allowed, and the whole
  point of Phase 8) and rewriting history (forbidden).

## What this does not solve

ESPN reaches ATP and WTA main tour and the Grand Slams. **Challenger, ITF and qualifying have no
reachable first-ball source at all**, and doubles coverage is unverified. Those matches stay
`START_UNKNOWN` and are excluded from strict pregame research. Their start times are not guessed, not
back-filled from the nominal time, and not inferred from market activity. See
[FIRST_BALL_SOURCES.md](FIRST_BALL_SOURCES.md) for the evidence behind each of those statements.
