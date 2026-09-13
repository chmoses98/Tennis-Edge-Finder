# External dislocation scorecard

804 observations over 92 matches (184 contracts), 2026-09-12T19:32Z to 2026-09-13T04:02Z. **Monitoring only.** Nothing here authorises a rule change.

Decisions: PASS 799, WATCH 5, SHADOW_BET 0

## How far apart are the two venues

| subset | n | median ext-Kalshi | mean | share >2c | share >5c | median edge after fees | share edge >=2c |
|---|---|---|---|---|---|---|---|
| all rows with a reference | 361 | -0.0014 | -0.0006 | 0.100 | 0.000 | -0.0303 | 0.000 |
| ALL_THREE_DISAGREE | 16 | -0.0207 | -0.0089 | 1.000 | 0.000 | -0.0499 | 0.000 |
| KALSHI_LONE_OUTLIER | 20 | -0.0210 | -0.0046 | 1.000 | 0.000 | -0.0463 | 0.000 |
| MARKETS_AGREE | 65 | -0.0037 | -0.0019 | 0.000 | 0.000 | -0.0334 | 0.000 |
| MODEL_LONE_OUTLIER | 260 | -0.0004 | +0.0005 | 0.000 | 0.000 | -0.0264 | 0.000 |

## Kalshi against each venue separately

151 observations had BOTH venues quoting.

| venue | n | median abs gap | p90 | p95 | max | >2c | >3c | >5c | >10c | max edge after fees |
|---|---|---|---|---|---|---|---|---|---|---|
| Bovada (sportsbook, de-vigged) | 778 | 0.0098 | 0.0298 | 0.0320 | 0.0492 | 0.231 | 0.100 | 0.000 | 0.000 | +0.0259 |
| Smarkets (exchange midpoint) | 175 | 0.0086 | 0.0194 | 0.0236 | 0.0799 | 0.091 | 0.046 | 0.011 | 0.000 | +0.0549 |

## Did Kalshi move toward the external reference

| subset | n | mean move toward | 95% CI | share moved toward | median gap (min) |
|---|---|---|---|---|---|
| all rows with a reference | 250 | +0.00050 | [-0.00038, 0.00134] | 0.212 | 29 |
| ALL_THREE_DISAGREE | 8 | -0.01125 | [-0.02187, -0.0] | 0.375 | 31 |
| KALSHI_LONE_OUTLIER | 11 | +0.00545 | [0.00227, 0.00909] | 0.545 | 30 |
| MARKETS_AGREE | 54 | +0.00111 | [-0.00176, 0.00389] | 0.296 | 29 |
| MODEL_LONE_OUTLIER | 177 | +0.00054 | [0.0, 0.00107] | 0.158 | 29 |

## Who was right

No observed contract has settled yet.
