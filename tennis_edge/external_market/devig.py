"""Removing a bookmaker's margin, three ways, and reporting when the choice matters.

A book quoting 1.90 / 1.90 is not saying "50/50". It is saying "50/50 plus 5.3% for us". Comparing the
raw implied 52.6% against a Kalshi ask is comparing a price to a price-plus-margin, and the margin is
usually larger than any edge we could find. So the margin comes out first, and the method used to remove
it is recorded on the row rather than assumed.

Three methods, because they disagree most exactly where it matters -- on longshots:

* **proportional** divides every implied probability by the overround. Simple, transparent, and it
  assumes the margin is spread evenly across outcomes, which books demonstrably do not do.
* **power** solves for k in p_i^k so the normalised probabilities sum to one. It takes proportionally more
  margin out of longshots, which matches how books actually price them.
* **shin** models the margin as insurance against insider money. Standard in the literature; on a
  two-outcome market it is close to power.

`devig_all` runs all three and reports the spread between them. When that spread is material the row says
so, and downstream code must treat the de-vigged number as uncertain rather than exact.
"""
from __future__ import annotations

import math
from dataclasses import dataclass

#: below this the three methods agree closely enough that the choice does not change a decision
MATERIAL_METHOD_SPREAD = 0.01


def american_to_decimal(american: float) -> float:
    a = float(american)
    if a == 0:
        raise ValueError("american odds of zero are not a price")
    return 1.0 + (a / 100.0 if a > 0 else 100.0 / abs(a))


def decimal_to_american(decimal: float) -> float:
    d = float(decimal)
    if d <= 1.0:
        raise ValueError(f"decimal odds must exceed 1.0, got {d}")
    return round((d - 1.0) * 100.0) if d >= 2.0 else round(-100.0 / (d - 1.0))


def implied(decimal: float) -> float:
    if decimal <= 1.0:
        raise ValueError(f"decimal odds must exceed 1.0, got {decimal}")
    return 1.0 / decimal


def overround(decimals) -> float:
    """Sum of implied probabilities. 1.0 is a fair book; 1.05 is a five-point margin."""
    return sum(implied(d) for d in decimals)


def devig_proportional(decimals) -> list[float]:
    ps = [implied(d) for d in decimals]
    s = sum(ps)
    return [p / s for p in ps]


def devig_power(decimals, tol=1e-10, iters=200) -> list[float]:
    """Solve sum(p_i^k) = 1. k > 1 pushes longshots down further than proportional does."""
    ps = [implied(d) for d in decimals]
    if abs(sum(ps) - 1.0) < tol:
        return list(ps)
    lo, hi = 0.2, 8.0
    for _ in range(iters):
        k = 0.5 * (lo + hi)
        s = sum(p ** k for p in ps)
        if s > 1.0:
            lo = k
        else:
            hi = k
        if abs(s - 1.0) < tol:
            break
    k = 0.5 * (lo + hi)
    out = [p ** k for p in ps]
    s = sum(out)
    return [o / s for o in out]


def devig_shin(decimals, tol=1e-12, iters=300) -> list[float]:
    """Shin's model: an insider fraction z that the book prices against.

    p_i = ( sqrt(z^2 + 4(1-z) * pi_i^2 / S) - z ) / (2(1-z)), with S the overround. Solved by bisection
    on z; z = 0 reproduces the proportional answer.
    """
    ps = [implied(d) for d in decimals]
    S = sum(ps)
    if abs(S - 1.0) < 1e-12 or len(ps) < 2:
        return [p / S for p in ps]

    def probs(z):
        if z <= 0:
            return [p / S for p in ps]
        out = []
        for p in ps:
            v = math.sqrt(z * z + 4.0 * (1.0 - z) * p * p / S) - z
            out.append(v / (2.0 * (1.0 - z)))
        return out

    lo, hi = 0.0, 0.6
    for _ in range(iters):
        z = 0.5 * (lo + hi)
        s = sum(probs(z))
        if s > 1.0:
            lo = z
        else:
            hi = z
        if abs(s - 1.0) < tol:
            break
    out = probs(0.5 * (lo + hi))
    s = sum(out)
    return [o / s for o in out]


@dataclass(frozen=True)
class DevigResult:
    probabilities: tuple            # by the primary method
    method: str
    overround: float
    margin: float                   # overround - 1
    by_method: dict                 # method -> tuple of probabilities
    max_method_spread: float        # largest disagreement on any single outcome
    method_choice_is_material: bool
    n_sides: int


def devig_all(decimals, primary: str = "proportional") -> DevigResult:
    """De-vig a COMPLETE market. Two or more sides required; a single offered price has no removable
    margin and asking for one is a bug, not a degraded case."""
    ds = [float(d) for d in decimals]
    if len(ds) < 2:
        raise ValueError("de-vigging needs the whole market: at least two observed sides")
    by = {"proportional": tuple(devig_proportional(ds)),
          "power": tuple(devig_power(ds)),
          "shin": tuple(devig_shin(ds))}
    spread = max(max(v[i] for v in by.values()) - min(v[i] for v in by.values()) for i in range(len(ds)))
    S = overround(ds)
    return DevigResult(probabilities=by[primary], method=primary, overround=S, margin=S - 1.0,
                       by_method=by, max_method_spread=spread,
                       method_choice_is_material=spread >= MATERIAL_METHOD_SPREAD, n_sides=len(ds))
