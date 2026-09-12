# Edge research protocol

The question is not "can we beat Pinnacle". It is: **are there identifiable situations where we hold a
small incremental advantage that survives out of sample, fees, liquidity and time?** A repeatable one to
three percentage points inside a narrow, liquid family is worth more than a large edge that evaporates on
the second look. This document is the discipline that makes the difference checkable.

## Model lanes, kept strictly apart

| lane | what it is | may see prices |
|---|---|---|
| MODEL 0 | the market itself | it is the market |
| MODEL 1 | Gen-1 Elo family | no |
| MODEL 2 | Gen-1 structural serve/return | no |
| MODEL 3 | Gen-2 dynamic hierarchical serve/return | **no, and a test enforces it** |
| MODEL 4 | market-conditioned distribution | **yes, by design and by name** |
| MODEL 5 | market-residual model | yes; its target IS the market's error |

Model 3 must never learn from a price, or the comparison against the market becomes circular.
`tests/test_gen2.py` imports the module graph and fails if anything price-bearing appears in it. Model 4
says so in its name and in its docstring, so nobody can mistake its winner probability for a forecast: by
construction that probability IS the market's.

## Pre-registered segments

`tennis_edge/research/segments.py` fixes the research buckets in code, dated, before results were read:
tour, surface, market family, favourite probability, disagreement, liquidity, spread width, time to first
ball, data quality, model uncertainty, favourite/underdog, central/tail derivative.

A bucket invented after seeing results is a **discovery**, not a confirmation. Such dimensions go in
`POST_HOC_DIMENSIONS` with the date they were added, and anything resting on them can only ever reach
`DISCOVERY_ONLY`.

## The discovery/confirmation firewall

`tennis_edge/research/registry.py` holds every candidate as a frozen, executable claim: an exact
inclusion rule, market family, model version, discovery window, freeze instant, minimum sample, and the
accuracy, CLV and after-fee conditions it must meet.

**A candidate discovered on a dataset may not be confirmed on that same dataset.** This is enforced, not
requested: evidence whose window starts before the freeze raises `FirewallError`, and the statuses that
imply support (`SUPPORTED_FOR_MORE_RESEARCH`, `ELIGIBLE_FOR_CEO_REVIEW`) refuse to be set without
sufficient post-freeze evidence.

Statuses stop at `ELIGIBLE_FOR_CEO_REVIEW`. Nothing in this repository can grant real-money authority.

## Statistical discipline

* Strict chronology. Every model predicts a match before that match updates its state.
* Orientation randomised per match, so a model cannot score by favouring the winner column.
* Paired bootstrap on differences, reported with a 95% interval, never a bare point estimate.
* Minimum sample sizes stated in advance; below them, no score is reported at all.
* Calibration reported next to accuracy: a model can be sharper and still worse.
* Executable CLV and after-fee economics, never midpoint CLV alone.
* Many hypotheses are searched, so a single low p-value is not evidence. Findings are reported with the
  number of comparisons that produced them.

**"23 bets, +18% ROI" is not a finding.** It is a sample too small to distinguish from noise, and the
protocol refuses to report it as one.

## What gets frozen for prospective tracking

A hypothesis earns a frozen candidate when it is specific enough to be wrong: an exact inclusion rule, a
named family, a stated minimum N, and a pre-committed pass/fail condition on accuracy, CLV and after-fee
economics. Anything vaguer stays in the report as an observation.

## The graveyard

`research/REJECTED_HYPOTHESES.md` records what did not work and why, so a future agent does not rediscover
it and overfit it a second time. A rejected hypothesis is only retested when something material changed:
new data, a new source, a structural change in the market.
