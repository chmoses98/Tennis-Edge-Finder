# Cross-market coherence scan (20260912T045611Z)

Discovery `20260912T003216Z`, 10 capture passes, 60826 parsed match-scope markets, 2290 executable quotes read, 1179 match-passes scanned.

| scan | what it counts | violations |
|---|---|---|
| price-only | executable BID/ASK break a relationship, size ignored | 0 |
| size-verified | same, but every leg had order-book depth | 0 |

## Size-verified opportunities

**None.** No structure on the captured board violated a relationship after order-book depth and taker fees were applied.


## Board shape (latest pass), which is what makes the null result readable

| measure | value |
|---|---|
| open executable quotes by family | {'MATCH_WINNER': 206, 'SET_WINNER': 68, 'EXACT_SET_SCORE': 4, 'TOTAL_GAMES': 3} |
| contracts per match | {'2': 136, '9': 1} |
| two-sided match-winner pairs | 103 |
| ask-sum, median (arb needs < 1 minus fees) | 1.02 |
| ask-sum, minimum seen | 0.99 |
| bid-sum, median (arb needs > 1 plus fees) | 0.98 |
| bid-sum, maximum seen | 1.0 |
| round-trip spread, median | 0.03 |
| pairs with ask-sum below 1.00 | 1 |
| pairs with bid-sum above 1.00 | 0 |

