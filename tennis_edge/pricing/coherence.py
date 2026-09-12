"""Executable cross-market coherence: relative value that needs no view on who wins.

Contracts on one physical match obey relationships that hold whatever the players do. If the executable
prices break one of those relationships, the inconsistency is a fact about the order book, not a forecast,
and it can be checked without any player model at all.

Three relationship shapes are enough to cover the families this project prices:

  PARTITION      mutually exclusive and exhaustive contracts (every exact set score; total sets 2 or 3 in
                 a best-of-three; the two sides of a match winner). Their probabilities sum to exactly 1.
  LADDER         nested thresholds (total games over 21.5 contains over 22.5; a -2.5 game spread contains
                 -3.5). The wider event is at least as likely as the one it contains.
  IMPLICATION    one event strictly implies another (winning the match implies winning at least one set),
                 so the implied event is at least as likely.

Every check is made on EXECUTABLE prices only:

  * buying costs the ASK, selling means buying the other side at 1 - BID;
  * size is the minimum available across the legs, so a one-contract quote yields a one-contract
    opportunity and is reported as such rather than as a headline percentage;
  * Kalshi's taker fee is charged on every leg, at that leg's own price, and subtracted BEFORE anything
    is called an opportunity;
  * the reported margin is the WORST CASE over every state of the world, derived from the relationship
    itself, never an expected value and never a midpoint.

A midpoint-based version of this scan finds "opportunities" constantly and none of them are real. That is
the single most important thing this module refuses to do.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict, field
from datetime import datetime

from tennis_edge.pricing.fees import FeeSchedule, taker_fee

PARTITION_UNDERPRICED = "PARTITION_UNDERPRICED"
PARTITION_OVERPRICED = "PARTITION_OVERPRICED"
COMPOSITE_UNDERPRICED = "COMPOSITE_UNDERPRICED"     # the parts cost less than the whole they add up to
COMPOSITE_OVERPRICED = "COMPOSITE_OVERPRICED"
LADDER_INVERSION = "LADDER_INVERSION"
IMPLICATION_VIOLATION = "IMPLICATION_VIOLATION"


@dataclass(frozen=True)
class Contract:
    """One executable two-sided quote. Prices are dollars per $1 contract."""
    ticker: str
    family: str
    yes_bid: float | None
    yes_ask: float | None
    yes_bid_size: float | None = None
    yes_ask_size: float | None = None
    line: float | None = None
    subject_is_a: bool | None = None
    set_index: int | None = None
    exact_score: str | None = None
    ts: datetime | None = None
    fee_type: str = "quadratic"

    @property
    def executable(self) -> bool:
        return (self.yes_bid is not None and self.yes_ask is not None
                and 0.0 < self.yes_bid <= self.yes_ask < 1.0)

    @property
    def buy_size(self) -> float:
        return self.yes_ask_size if self.yes_ask_size is not None else 0.0

    @property
    def sell_size(self) -> float:
        return self.yes_bid_size if self.yes_bid_size is not None else 0.0


@dataclass
class Leg:
    ticker: str
    side: str            # BUY_YES | BUY_NO   (selling YES on Kalshi means buying NO)
    price: float         # dollars paid per contract for that side
    size: float          # contracts available at that price
    fee: float           # taker fee per contract at this price

    def to_dict(self):
        return asdict(self)


@dataclass
class Opportunity:
    kind: str
    match_id: str
    family: str
    detected_at: str
    legs: list = field(default_factory=list)
    capital_per_set: float = 0.0          # dollars laid out for one unit of the structure
    worst_case_payoff: float = 0.0        # dollars returned in the WORST state of the world
    fees_per_set: float = 0.0
    theoretical_margin: float = 0.0       # ignoring fees, on the same executable prices
    executable_margin: float = 0.0        # after fees; this is the only number that counts
    size: float = 0.0                     # units of the structure available
    total_executable_profit: float = 0.0
    detail: str = ""

    def to_dict(self):
        d = asdict(self)
        d["legs"] = [l if isinstance(l, dict) else l.to_dict() for l in self.legs]
        return d


def _fee(price: float, fee_type: str) -> float:
    return taker_fee(price, 1, FeeSchedule(fee_type=fee_type))


def _mk(kind, match_id, family, legs, worst_case, detail, ts, size):
    capital = sum(l.price for l in legs)
    fees = sum(l.fee for l in legs)
    theo = worst_case - capital
    exe = theo - fees
    return Opportunity(kind=kind, match_id=match_id, family=family,
                       detected_at=ts.isoformat() if hasattr(ts, "isoformat") else str(ts),
                       legs=[l.to_dict() for l in legs], capital_per_set=round(capital, 6),
                       worst_case_payoff=round(worst_case, 6), fees_per_set=round(fees, 6),
                       theoretical_margin=round(theo, 6), executable_margin=round(exe, 6),
                       size=size, total_executable_profit=round(exe * size, 6), detail=detail)


def check_partition(contracts: list[Contract], match_id: str, family: str, ts=None) -> list[Opportunity]:
    """Mutually exclusive and exhaustive contracts: their probabilities sum to exactly 1."""
    cs = [c for c in contracts if c.executable]
    if len(cs) < 2:
        return []
    out = []
    ts = ts or (cs[0].ts if cs[0].ts else "")
    # UNDERPRICED: buy every leg. Exactly one pays $1, whatever happens.
    legs = [Leg(c.ticker, "BUY_YES", c.yes_ask, c.buy_size, _fee(c.yes_ask, c.fee_type)) for c in cs]
    size = min((l.size for l in legs), default=0.0)
    o = _mk(PARTITION_UNDERPRICED, match_id, family, legs, 1.0,
            f"{len(cs)} exhaustive contracts ask-sum {sum(c.yes_ask for c in cs):.4f}", ts, size)
    if o.executable_margin > 0 and size > 0:
        out.append(o)
    # OVERPRICED: sell every leg by buying its NO. Exactly one NO fails, so n-1 of them pay $1.
    legs = [Leg(c.ticker, "BUY_NO", round(1.0 - c.yes_bid, 6), c.sell_size, _fee(1.0 - c.yes_bid, c.fee_type))
            for c in cs]
    size = min((l.size for l in legs), default=0.0)
    o = _mk(PARTITION_OVERPRICED, match_id, family, legs, float(len(cs) - 1),
            f"{len(cs)} exhaustive contracts bid-sum {sum(c.yes_bid for c in cs):.4f}", ts, size)
    if o.executable_margin > 0 and size > 0:
        out.append(o)
    return out


def check_nested(wider: Contract, narrower: Contract, match_id: str, family: str,
                 kind: str = LADDER_INVERSION, detail: str = "", ts=None) -> Opportunity | None:
    """`wider` contains `narrower`, so P(wider) >= P(narrower).

    Trade when the book says otherwise: buy the wider event, sell the narrower one. Whenever the narrower
    event happens the wider one does too, so the pair never loses: worst case both legs pay nothing
    (payoff 0) or both pay (payoff 1 on the YES leg, 0 on the NO leg we sold) -- worst case is 0 plus the
    $1 that the NO leg returns when the narrower event fails and the wider one also fails. Concretely,
    buying wider YES and narrower NO pays at least $1 in every state.
    """
    if not (wider.executable and narrower.executable):
        return None
    legs = [Leg(wider.ticker, "BUY_YES", wider.yes_ask, wider.buy_size, _fee(wider.yes_ask, wider.fee_type)),
            Leg(narrower.ticker, "BUY_NO", round(1.0 - narrower.yes_bid, 6), narrower.sell_size,
                _fee(1.0 - narrower.yes_bid, narrower.fee_type))]
    size = min((l.size for l in legs), default=0.0)
    o = _mk(kind, match_id, family, legs, 1.0,
            detail or f"{narrower.ticker} bid {narrower.yes_bid:.2f} > {wider.ticker} ask {wider.yes_ask:.2f}",
            ts or wider.ts or "", size)
    return o if (o.executable_margin > 0 and size > 0) else None


def _ladder_pairs(contracts: list[Contract], higher_strike_is_wider: bool):
    """Order a threshold ladder so the WIDER (more likely) event comes first in each adjacent pair.

    Every ladder family Kalshi lists for tennis is an "above <line>" contract -- total games above 21.5,
    game differential above 2.5, sets played above 2.5 -- so probability DECREASES with the strike and the
    LOWER strike is the wider event. The flag exists for an under-style ladder, which this exchange does
    not currently list; getting it backwards would turn every coherent ladder into a false opportunity,
    so it is named for what it means rather than for a sort direction.
    """
    cs = sorted([c for c in contracts if c.executable and c.line is not None], key=lambda c: c.line)
    pairs = []
    for i in range(len(cs) - 1):
        lo, hi = cs[i], cs[i + 1]
        pairs.append((hi, lo) if higher_strike_is_wider else (lo, hi))
    return pairs


def check_ladder(contracts: list[Contract], match_id: str, family: str,
                 higher_strike_is_wider: bool = False, ts=None) -> list[Opportunity]:
    """A threshold ladder is monotone in the strike; adjacent rungs are a nested pair."""
    out = []
    for wider, narrower in _ladder_pairs(contracts, higher_strike_is_wider):
        o = check_nested(wider, narrower, match_id, family, LADDER_INVERSION,
                         f"rung {narrower.line} bid {narrower.yes_bid:.2f} exceeds rung {wider.line} "
                         f"ask {wider.yes_ask:.2f} on a monotone ladder", ts)
        if o:
            out.append(o)
    return out


def check_composite(parts: list[Contract], whole: Contract, match_id: str, family: str,
                    detail: str = "", ts=None) -> list[Opportunity]:
    """The parts are mutually exclusive and their union is exactly `whole`, so their prices must sum to it.

    Buying every part while selling the whole pays exactly $1 in every state: either one part fires and
    the sold whole costs $1 back against the $1 it pays, or nothing fires and the NO leg on the whole pays.
    The reverse structure pays exactly n. Both are checked, on executable prices, after fees.
    """
    ps = [c for c in parts if c.executable]
    if len(ps) < 2 or not whole.executable:
        return []
    out, ts = [], ts or whole.ts or ""
    legs = [Leg(c.ticker, "BUY_YES", c.yes_ask, c.buy_size, _fee(c.yes_ask, c.fee_type)) for c in ps]
    legs.append(Leg(whole.ticker, "BUY_NO", round(1.0 - whole.yes_bid, 6), whole.sell_size,
                    _fee(1.0 - whole.yes_bid, whole.fee_type)))
    size = min((l.size for l in legs), default=0.0)
    o = _mk(COMPOSITE_UNDERPRICED, match_id, family, legs, 1.0,
            detail or f"parts ask-sum {sum(c.yes_ask for c in ps):.4f} vs whole bid {whole.yes_bid:.4f}", ts, size)
    if o.executable_margin > 0 and size > 0:
        out.append(o)

    legs = [Leg(whole.ticker, "BUY_YES", whole.yes_ask, whole.buy_size, _fee(whole.yes_ask, whole.fee_type))]
    legs += [Leg(c.ticker, "BUY_NO", round(1.0 - c.yes_bid, 6), c.sell_size, _fee(1.0 - c.yes_bid, c.fee_type))
             for c in ps]
    size = min((l.size for l in legs), default=0.0)
    o = _mk(COMPOSITE_OVERPRICED, match_id, family, legs, float(len(ps)),
            detail or f"parts bid-sum {sum(c.yes_bid for c in ps):.4f} vs whole ask {whole.yes_ask:.4f}", ts, size)
    if o.executable_margin > 0 and size > 0:
        out.append(o)
    return out


def check_implication(implied: Contract, implier: Contract, match_id: str, family: str,
                      detail: str, ts=None) -> Opportunity | None:
    """`implier` happening forces `implied` to happen, so P(implied) >= P(implier)."""
    return check_nested(implied, implier, match_id, family, IMPLICATION_VIOLATION, detail, ts)


def scan_match(contracts: list[Contract], match_id: str, best_of: int = 3, ts=None) -> list[Opportunity]:
    """Every relationship this engine knows, over one physical match's executable board."""
    by_family: dict[str, list[Contract]] = {}
    for c in contracts:
        by_family.setdefault(c.family, []).append(c)
    out: list[Opportunity] = []

    mw = by_family.get("MATCH_WINNER", [])
    sides = {c.subject_is_a for c in mw if c.subject_is_a is not None}
    if len(sides) == 2:
        first = {}
        for c in mw:
            if c.subject_is_a is not None and c.subject_is_a not in first:
                first[c.subject_is_a] = c
        out += check_partition(list(first.values()), match_id, "MATCH_WINNER", ts)

    ex = [c for c in by_family.get("EXACT_SET_SCORE", []) if c.exact_score]
    if len({c.exact_score for c in ex}) >= _exact_partition_size(best_of):
        seen, uniq = set(), []
        for c in ex:
            if c.exact_score not in seen:
                seen.add(c.exact_score)
                uniq.append(c)
        out += check_partition(uniq, match_id, "EXACT_SET_SCORE", ts)

    tot_sets = by_family.get("TOTAL_SETS", [])
    if len({c.line for c in tot_sets if c.line is not None}) >= 2:
        out += check_ladder(tot_sets, match_id, "TOTAL_SETS", ts=ts)

    for fam in ("TOTAL_GAMES", "GAME_SPREAD", "SET_SPREAD"):
        group = by_family.get(fam, [])
        for side in {c.subject_is_a for c in group}:
            rungs = [c for c in group if c.subject_is_a == side]
            if len(rungs) >= 2:
                out += check_ladder(rungs, match_id, fam, ts=ts)

    # the exact scores in which one side wins are mutually exclusive and add up to that side winning
    if mw and ex:
        for side, whole in {c.subject_is_a: c for c in mw if c.subject_is_a is not None}.items():
            parts, seen = [], set()
            for c in ex:
                if c.exact_score in seen:
                    continue
                won = _exact_score_winner_is_a(c)
                if won is None or won != side:
                    continue
                seen.add(c.exact_score)
                parts.append(c)
            if len(parts) >= 2:
                out += check_composite(parts, whole, match_id, "EXACT_SET_SCORE/MATCH_WINNER",
                                       "the exact scores in which this side wins add up to that side winning", ts)

    # winning the match implies winning at least one set
    anyset = {c.subject_is_a: c for c in by_family.get("ANY_SET_WINNER", []) if c.subject_is_a is not None}
    for c in mw:
        a = anyset.get(c.subject_is_a)
        if a is not None:
            o = check_implication(a, c, match_id, "ANY_SET_WINNER/MATCH_WINNER",
                                  "winning the match implies winning at least one set", ts)
            if o:
                out.append(o)
    return out


def _exact_score_winner_is_a(c: Contract) -> bool | None:
    """Which side wins under this exact-score contract, in the distribution's A/B orientation."""
    if not c.exact_score or c.subject_is_a is None:
        return None
    try:
        x, y = (int(v) for v in str(c.exact_score).replace("-", " ").split()[:2])
    except (TypeError, ValueError):
        return None
    subject_wins = x > y
    return c.subject_is_a if subject_wins else (not c.subject_is_a)


def _exact_partition_size(best_of: int) -> int:
    return 4 if best_of == 3 else 6      # 2-0,2-1,0-2,1-2  /  3-0,3-1,3-2,0-3,1-3,2-3
