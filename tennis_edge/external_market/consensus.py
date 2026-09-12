"""Turning several external prices into one reference value, without pretending they are independent.

Two decisions are pre-specified here so that no later result can motivate them:

* **The aggregator is a MEDIAN across independent groups.** Not a fitted weighting. With a handful of
  venues and a few weeks of data, any weight we estimated would be a description of the sample. A median
  also does the one thing we most need: a single venue with a broken line cannot drag the reference.
* **Independence is declared, not inferred.** Sources that resell or mirror the same pricing sit in one
  group and count as ONE witness however many names they appear under. A market-conditioned model, or any
  feed derived from Kalshi itself, is not admissible as an external witness at all.

Staleness is checked in both directions, because the two have different causes: how old the venue said
its price was when we fetched it, and how long ago we fetched. A price that fails either bound is
excluded and counted, never quietly averaged in.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from statistics import median

#: source -> independence group. Sources sharing a group count as one witness.
INDEPENDENCE_GROUPS = {
    "polymarket": "polymarket",
    "espn_bet": "espn",
    "espn_odds": "espn",
    "bovada": "bovada",
    "smarkets": "smarkets",
    "betfair": "betfair",
    "pinnacle": "pinnacle",
}

#: venues whose price is a two-sided market rather than an offered line with a margin
SHARP_KINDS = ("EXCHANGE", "PREDICTION_MARKET")

#: any source whose price is derived from Kalshi cannot be a witness against Kalshi
INADMISSIBLE = ("kalshi",)

DEFAULT_MAX_SOURCE_STALENESS_S = 900.0     # the venue's own timestamp vs when we fetched
DEFAULT_MAX_CAPTURE_AGE_S = 900.0          # when we fetched vs now


def group_of(source: str) -> str:
    return INDEPENDENCE_GROUPS.get(source, source)


@dataclass(frozen=True)
class Reference:
    physical_match_id: str
    market_family: str
    side: str
    value: float | None                  # the reference fair probability, or None if none could be built
    kind: str                            # SHARP_REFERENCE | MULTI_BOOK_CONSENSUS | NONE
    n_observations: int = 0
    n_independent_groups: int = 0
    groups: tuple = ()
    per_group: dict = field(default_factory=dict)
    dispersion: float | None = None      # max - min across groups; the disagreement among witnesses
    excluded_stale: int = 0
    excluded_inadmissible: int = 0
    excluded_no_devig: int = 0
    reason: str = ""
    aggregation: str = "median_across_independent_groups"


def _age(iso_a: str | None, iso_b: str | None) -> float | None:
    if not iso_a or not iso_b:
        return None
    try:
        a = datetime.fromisoformat(str(iso_a).replace("Z", "+00:00"))
        b = datetime.fromisoformat(str(iso_b).replace("Z", "+00:00"))
    except (TypeError, ValueError):
        return None
    return (b - a).total_seconds()


def build_reference(observations, *, now: str, min_groups: int = 1,
                    max_source_staleness_s: float = DEFAULT_MAX_SOURCE_STALENESS_S,
                    max_capture_age_s: float = DEFAULT_MAX_CAPTURE_AGE_S,
                    require_source_timestamp: bool = False) -> Reference:
    """One reference value for one (match, family, side) from a list of ExternalMarketObservation."""
    obs = list(observations)
    if not obs:
        return Reference("", "", "", None, "NONE", reason="no observations")
    head = obs[0]
    excl_stale = excl_inadm = excl_nodevig = 0
    usable = []
    for o in obs:
        if o.source.lower() in INADMISSIBLE:
            excl_inadm += 1
            continue
        if o.devigged_probability is None:
            excl_nodevig += 1
            continue
        cap_age = _age(o.observed_at, now)
        if cap_age is None or cap_age > max_capture_age_s:
            excl_stale += 1
            continue
        src_age = o.staleness_seconds
        if src_age is None:
            if require_source_timestamp:
                excl_stale += 1
                continue
        elif src_age > max_source_staleness_s:
            excl_stale += 1
            continue
        usable.append(o)

    if not usable:
        return Reference(head.physical_match_id or "", head.market_family, head.side, None, "NONE",
                         n_observations=len(obs), excluded_stale=excl_stale,
                         excluded_inadmissible=excl_inadm, excluded_no_devig=excl_nodevig,
                         reason="every observation was stale, inadmissible or un-de-viggable")

    per_group: dict = {}
    for o in usable:
        per_group.setdefault(group_of(o.source), []).append(o.devigged_probability)
    collapsed = {g: float(median(v)) for g, v in per_group.items()}
    if len(collapsed) < min_groups:
        return Reference(head.physical_match_id or "", head.market_family, head.side, None, "NONE",
                         n_observations=len(obs), n_independent_groups=len(collapsed),
                         groups=tuple(sorted(collapsed)), per_group=collapsed,
                         excluded_stale=excl_stale, excluded_inadmissible=excl_inadm,
                         excluded_no_devig=excl_nodevig,
                         reason=f"{len(collapsed)} independent group(s), {min_groups} required")

    vals = sorted(collapsed.values())
    kind = ("SHARP_REFERENCE" if any(o.source_kind in SHARP_KINDS for o in usable)
            else "MULTI_BOOK_CONSENSUS")
    return Reference(physical_match_id=head.physical_match_id or "", market_family=head.market_family,
                     side=head.side, value=float(median(vals)), kind=kind,
                     n_observations=len(obs), n_independent_groups=len(collapsed),
                     groups=tuple(sorted(collapsed)), per_group=collapsed,
                     dispersion=(vals[-1] - vals[0]) if len(vals) > 1 else 0.0,
                     excluded_stale=excl_stale, excluded_inadmissible=excl_inadm,
                     excluded_no_devig=excl_nodevig)
