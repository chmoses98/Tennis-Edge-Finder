# Close, CLV and settlement

## Two truths
* **SPORTS_TRUTH** (`tennis_edge/ledger/truth.py:SportsTruth`): winner, score, outcome type
  (COMPLETED/RETIRED/WALKOVER/DEFAULT/UNFINISHED/UNKNOWN), retiring player, sets/games completed, actual
  first ball / finish when known, source and confidence. Model scoring uses this and only when
  `gradeable_binary` (completed/retired/default with a winner and confidence >= 0.9).
* **EXCHANGE_TRUTH** (`ExchangeTruth`): Kalshi `result` (yes/no/scalar), `settlement_value_dollars`,
  `settlement_ts`, `expiration_value` verbatim. P/L, hypothetical or real, is computed from this only.
* `reconcile()` cross-checks them; a contradiction is a TENNIS-8/9 failure, never auto-resolved.

## Canonical close (`tennis_edge/ledger/close.py`)

Rewritten in the first-ball wave (2026-09-11).

CANONICAL_CLOSE = the last EXECUTABLE quote strictly before the **earliest possible first ball**.
Executable means a real two-sided quote (both sides present, `0 < bid <= ask < 1`) from a market record,
an orderbook top or a bid/ask candle. A trade print is never a quote: it says someone dealt, not that
you could have. A settlement value is never a quote either.

Three things the function now refuses to do:

1. **It will not take a bare datetime as "the start".** `canonical_close()` takes a `FirstBallTruth`
   object. A scheduled time, a Kalshi `occurrence_datetime` and a market `close_time` are not truth
   objects, so none of them can be substituted by accident. A scheduled-time close is still computable
   for diagnostics, but only via `allow_scheduled_fallback=True`, and the result is stamped
   `strict=False` and excluded from strict research.
2. **It will not use the point estimate of a bracketed start.** The cutoff is the bracket's LOWER bound,
   so the close is chosen only from quotes that provably precede any possible first ball.
3. **It will not synthesise.** No executable quote before the cutoff means `NO_EXECUTABLE_QUOTE`, and the
   row says so.

`close_basis` is one of `ACTUAL_FIRST_BALL` (zero-width truth), `FIRST_BALL_BRACKET_LOWER`,
`SCHEDULED_MINUS_MARGIN` (never strict), `NO_FIRST_BALL_TRUTH`, `NO_EXECUTABLE_QUOTE`.
Retained with the close: yes and no bid/ask, mid, spread, sizes/depth, timestamp, seconds to the cutoff
and seconds to the first ball.

## CLV v2 (`tennis_edge/ledger/clv.py`)

CLV is an **information and execution diagnostic**, never profit, and it is never netted against
realised P/L. Three measures are kept separate and never averaged together:

| measure | definition | role |
|---|---|---|
| `clv_executable` | `close_yes_bid - entry_yes_ask` | **primary.** What a taker who bought YES could have sold back for at the close. Spread-inclusive, therefore pessimistic, which is the point. |
| `clv_ask_to_ask` | `close_yes_ask - entry_yes_ask` | same side of the book at both ends; separates level movement from spread movement |
| `clv_midpoint` | `close_mid - entry_mid` | secondary, meaningful only where both ends are two-sided |

**Units.** A Kalshi YES contract pays $1, so its price in dollars IS the market-implied probability of
the event. Price-space and probability-space movement are therefore the SAME NUMBER for every family
here, spreads and totals included, whose contracts are binary on a threshold. Both `price_move_cents`
and `prob_move` are reported with explicit units so neither is later mistaken for independent evidence.

Every record also carries: entry and close timestamps, seconds from entry to first ball, seconds from
close to first ball, spread and depth at both ends, market family, tour, level, data-quality grade,
model probability, model-market disagreement, timing class, truth confidence and derivation version.
Fees are computed per contract at both ends and reported **separately**; they are never folded into a
CLV number.

A record is `strict` only when the close is first-ball anchored AND the entry itself classifies as
`STRICT_PREGAME` AND both quotes are executable. Anything else is retained with an
`exclusion_reason`, never dropped.

## Decision horizons (`tennis_edge/firstball/horizons.py`)

T-6h, T-3h, T-1h, T-30m, T-15m, T-10m, T-5m and LAST_VALID_PREMATCH, all measured from the **actual**
first ball, because a two-hour court delay moves every horizon defined against a schedule. A horizon is
filled from the last executable quote at or before its target instant, never from one after it, and is
reported MISSING (with the staleness recorded) rather than filled from a quote that is too old. Each
populated horizon stores the target instant, the quote timestamp, the distance from the target and the
distance from the first ball.

## First-ball problem: what changed, and what did not

Kalshi exposes `occurrence_datetime` (a nominal, scheduled time) and `close_time` (set after the winner
is declared), and no start. The first-ball wave answered this properly rather than approximating it:

* **Solved for ATP and WTA main tour and the Grand Slams.** The ESPN public scoreboard gives a per-match
  state (`pre` / `in` / `post`), so polling brackets the first ball between the last "not started"
  reading and the first "in progress" one. See [FIRST_BALL_TRUTH.md](FIRST_BALL_TRUTH.md).
* **Unsolved for Challenger, ITF and qualifying.** No reachable source covers them. Those matches stay
  `START_UNKNOWN`, produce no strict close and no strict CLV. Their start times are not guessed, not
  back-filled from the nominal time, and not inferred from market activity. See
  [FIRST_BALL_SOURCES.md](FIRST_BALL_SOURCES.md) for the probe evidence.
* **Historical recovery is not available.** `scripts/firstball/assess_historical_recovery.py` scanned
  1,378 completed ESPN competitions: every one reports a `startDate` identical to its scheduled date and
  none reports an end time. Across that many completed matches some certainly ran late, so the field is a
  SCHEDULE. Prospective rows captured before first-ball polling existed therefore remain
  `START_UNKNOWN`, and are reclassified automatically if trustworthy truth ever arrives.
* **Price-path evidence still is not truth.** A large first candle move after the nominal time can bound
  the start from above, and Kalshi activity may narrow a bracket a sports source already established, but
  exchange evidence alone caps confidence at C and can never be sports truth.

Reclassification is deterministic and versioned. `scripts/ops/settle_ledger.py` re-derives the timing
class of EVERY ledger row from the latest truths on every run and writes it to a separate table with the
classifier version and the truth's derivation version. The ledger row itself, and above all its
`generated_at_utc`, is never touched.

## Bookmaker benchmark vs Kalshi close
tennis-data.co.uk prices are a separate, pre-match reference benchmark (capture time undocumented) used for
historical model-vs-market research; they are never substituted for Kalshi closes or CLV.
