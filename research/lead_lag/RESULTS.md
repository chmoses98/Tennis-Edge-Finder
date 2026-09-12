# Lead-lag between related Kalshi tennis markets

**Can this even be measured on the data we have?** That question comes first.

| measure | value |
|---|---|
| capture passes available | 10 |
| distinct quoted contract series | 297 |
| series quoted in at least 6 passes | 208 |
| physical matches quoted | 140 |
| matches with two or more FAMILIES quoted | 2 |
| family pairs examined | 3 |
| pairs with enough overlapping observations | 1 |

## Verdict: not measurable yet

A lead-lag estimate needs many matches carrying at least two related families quoted simultaneously over a long enough window. On this archive that population is 1 pairs, which is far too few to distinguish a lead from noise. This is a POWER problem, not a null result: the honest statement is that the question remains open, and it will stay open until Kalshi lists more derivative contracts or the capture archive covers many more days.

The cause is the same structural fact the coherence scan found: almost every tennis match on this exchange has exactly two open contracts, the two sides of the match winner. There is no derivative to lag behind anything.
