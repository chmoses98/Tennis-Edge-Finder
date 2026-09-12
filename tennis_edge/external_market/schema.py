"""One observation of one side of one market at one external venue, at one instant.

Three rules are enforced rather than documented, because each one corresponds to a way this data could
quietly become fiction:

* **Never fabricate the opposite side.** A book that quoted only one side is stored as one side, with a
  de-vigged probability of None. Inventing `1 - p` from a single offered price silently converts a
  bookmaker's margin into a probability and makes an overround look like an edge.
* **Never fabricate a timestamp.** `source_timestamp` is what the venue said, or None. `observed_at` is
  when WE fetched it, always ours, never inferred. Two fields because they answer different questions and
  the difference between them is how staleness is measured.
* **Raw evidence is preserved.** `raw_evidence_hash` and `raw_evidence_location` point at the stored
  payload the row was derived from, so the derivation can be re-checked against the bytes.

Rows are immutable and fingerprinted; the store is append-only and hash-chained.
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, asdict, field, replace
from datetime import datetime, timezone

#: what kind of venue produced the price. The distinction matters: an exchange's two-sided book is
#: directly comparable to Kalshi's, while a book's offered odds carry a margin that must be removed.
EXCHANGE = "EXCHANGE"
SPORTSBOOK = "SPORTSBOOK"
PREDICTION_MARKET = "PREDICTION_MARKET"
AGGREGATOR = "AGGREGATOR"
SOURCE_KINDS = (EXCHANGE, SPORTSBOOK, PREDICTION_MARKET, AGGREGATOR)


class ExternalMarketError(RuntimeError):
    pass


def _hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"),
                                     default=str).encode()).hexdigest()


@dataclass(frozen=True)
class ExternalMarketObservation:
    source: str                          # "polymarket", "espn_bet", ...
    source_kind: str                     # one of SOURCE_KINDS
    source_event_id: str
    observed_at: str                     # ISO instant WE fetched it. Never inferred.
    physical_match_id: str | None        # our canonical key, or None when mapping failed
    participant_a: str                   # as the SOURCE names them
    participant_b: str
    market_family: str                   # MATCH_WINNER, TOTAL_GAMES, ...
    side: str                            # which participant / outcome this row prices
    strike: float | None = None          # the line, where the family has one
    decimal_odds: float | None = None
    american_odds: float | None = None
    back_price: float | None = None      # exchanges: the price you can take
    lay_price: float | None = None       # exchanges: the price you can offer
    implied_probability: float | None = None    # 1/decimal, margin INCLUDED
    devigged_probability: float | None = None   # None unless the full market was present
    devig_method: str = ""
    source_margin: float | None = None          # overround - 1, None if not computable
    n_sides_in_market: int | None = None        # how many outcomes the de-vig actually saw
    line: str = ""                              # the venue's own description of the market
    status: str = ""                            # the venue's status string
    is_pregame: bool | None = None
    source_timestamp: str | None = None         # what the VENUE said, or None. Never inferred.
    mapping_confidence: float | None = None
    mapping_status: str = "UNMAPPED"
    raw_evidence_hash: str = ""
    raw_evidence_location: str = ""
    schema_version: int = 1
    fingerprint: str = ""

    def __post_init__(self):
        if self.source_kind not in SOURCE_KINDS:
            raise ExternalMarketError(f"source_kind must be one of {SOURCE_KINDS}, got {self.source_kind!r}")
        for name in ("implied_probability", "devigged_probability"):
            v = getattr(self, name)
            if v is not None and not 0.0 < v < 1.0:
                raise ExternalMarketError(f"{name} out of range: {v}")
        if self.devigged_probability is not None and not self.devig_method:
            raise ExternalMarketError("a de-vigged probability must name the method that produced it")
        if self.devigged_probability is not None and (self.n_sides_in_market or 0) < 2:
            raise ExternalMarketError(
                "refusing a de-vigged probability derived from fewer than two observed sides: "
                "the opposite side must be observed, never fabricated")
        if self.decimal_odds is not None and self.decimal_odds <= 1.0:
            raise ExternalMarketError(f"decimal odds must exceed 1.0, got {self.decimal_odds}")
        object.__setattr__(self, "fingerprint", _hash(
            {k: v for k, v in asdict(self).items() if k != "fingerprint"}))

    @property
    def staleness_seconds(self) -> float | None:
        """How old the venue said its price was when we saw it. None when the venue gave no timestamp --
        which is itself information, and must not be silently treated as zero."""
        if not self.source_timestamp:
            return None
        try:
            a = datetime.fromisoformat(self.source_timestamp.replace("Z", "+00:00"))
            b = datetime.fromisoformat(self.observed_at.replace("Z", "+00:00"))
        except (TypeError, ValueError):
            return None
        return (b - a).total_seconds()

    def to_dict(self) -> dict:
        return asdict(self)

    def evolve(self, **changes) -> "ExternalMarketObservation":
        changes.pop("fingerprint", None)
        return replace(self, **changes)


class ExternalStore:
    """Append-only, hash-chained, one file per UTC day. Same contract as the other evidence stores."""

    def __init__(self, root: str):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def _path(self, day: str) -> str:
        return os.path.join(self.root, f"{day}.jsonl")

    def _last_hash(self, path: str) -> str:
        prev = "GENESIS"
        if os.path.exists(path):
            with open(path) as f:
                for line in f:
                    if line.strip():
                        prev = json.loads(line).get("row_hash", prev)
        return prev

    def append_many(self, rows) -> int:
        n = 0
        for row in rows:
            d = row.to_dict()
            day = (row.observed_at or datetime.now(timezone.utc).isoformat())[:10]
            path = self._path(day)
            d["prev_hash"] = self._last_hash(path)
            d["row_hash"] = _hash({k: v for k, v in d.items() if k != "row_hash"})
            with open(path, "a") as f:
                f.write(json.dumps(d, separators=(",", ":"), default=str) + "\n")
            n += 1
        return n

    def rows(self):
        if not os.path.isdir(self.root):
            return
        for fn in sorted(os.listdir(self.root)):
            if fn.endswith(".jsonl"):
                with open(os.path.join(self.root, fn)) as f:
                    for line in f:
                        if line.strip():
                            yield json.loads(line)

    def verify_chain(self) -> list[str]:
        problems = []
        for fn in sorted(os.listdir(self.root)) if os.path.isdir(self.root) else []:
            if not fn.endswith(".jsonl"):
                continue
            prev = "GENESIS"
            with open(os.path.join(self.root, fn)) as f:
                for i, line in enumerate(f):
                    if not line.strip():
                        continue
                    r = json.loads(line)
                    if r.get("prev_hash") != prev:
                        problems.append(f"{fn}:{i}: prev_hash mismatch")
                    if _hash({k: v for k, v in r.items() if k != "row_hash"}) != r.get("row_hash"):
                        problems.append(f"{fn}:{i}: row modified after the fact")
                    prev = r.get("row_hash")
        return problems
