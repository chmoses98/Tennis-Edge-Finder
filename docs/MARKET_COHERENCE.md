# Cross-market coherence

Contracts on one physical match obey relationships that hold whatever the players do. If executable
prices break one, the inconsistency is a fact about the order book rather than a forecast, and it can be
checked with no player model at all. That makes this the one edge hypothesis in the project that does not
depend on beating anyone at tennis.

## Relationships checked

| shape | meaning | example |
|---|---|---|
| PARTITION | mutually exclusive and exhaustive: probabilities sum to exactly 1 | the two sides of a match winner; every exact set score |
| COMPOSITE | mutually exclusive parts whose union is another listed contract | the exact scores in which A wins add up to A winning |
| LADDER | nested thresholds: the wider event is at least as likely | total games above 21.5 contains above 22.5 |
| IMPLICATION | one event forces another | winning the match implies winning at least one set |

Every Kalshi tennis ladder is an "above `<line>`" contract, so probability FALLS as the strike rises and
the LOWER strike is the wider event. The direction is named for what it means rather than for a sort
order, because getting it backwards would report every coherent ladder as an opportunity.

## What counts as an opportunity

* **Executable prices only.** Buying costs the ASK; selling means buying the other side at 1 minus the
  BID. The midpoint is never used. A board whose midpoints sum to 0.92 while its asks sum to 1.08 is not
  an opportunity, and a test pins that case.
* **Size is the minimum across legs**, taken from the captured order book. A one-contract quote yields a
  one-contract opportunity and is reported as such, not as a headline percentage.
* **Fees are charged on every leg**, at that leg's own price, and subtracted before anything is called an
  opportunity.
* **The margin is the worst case** over every state of the world, derived from the relationship itself.
  Never an expected value.

## Result on the captured board (2026-09-12)

**Zero violations, price-only or size-verified.** The null result is only readable with the board's shape
attached:

| measure | value |
|---|---|
| open executable quotes by family | MATCH_WINNER 206, SET_WINNER 68, EXACT_SET_SCORE 4, TOTAL_GAMES 3 |
| contracts per match | 136 matches with 2, one match with 9 |
| two-sided match-winner pairs | 103 |
| ask-sum median (arbitrage needs below 1 minus fees) | 1.0200 |
| ask-sum minimum observed | 0.9900 |
| bid-sum median (arbitrage needs above 1 plus fees) | 0.9800 |
| round-trip spread median | 0.0300 |
| pairs with ask-sum below 1.00 | 1 |

Two conclusions, and they matter more than the zero:

1. **The fee wall is wider than the inconsistency.** Kalshi's taker fee on a two-leg structure near even
   money is roughly four cents. The single sub-1.00 ask-sum observed was 0.99, a one-cent gap. For
   cross-market arbitrage to exist here the board would have to be off by more than the fee, and over
   ten capture passes it never was.
2. **There is almost no derivative board to be incoherent about.** 136 of 137 matches had exactly two
   open contracts, the two sides of the match winner. Seven ladder contracts were open across the whole
   universe. A relative-value strategy needs related contracts to trade against each other, and on Kalshi
   tennis today they mostly do not exist.

The second point also constrains two other lanes: market-conditioned derivative pricing has almost no
live derivative market to price against, and a lead-lag study has almost no derivative series to measure
a lag in. Those are reported as structurally under-powered rather than as null results.

## What would change the answer

More derivative listings; a fee change; a period of fast price movement, when a stale rung is most likely
(the scan tracks persistence per structure, so a transient inversion would be recorded with its
duration); or a second venue to price against, which this project does not have.
