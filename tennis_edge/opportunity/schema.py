"""The canonical Opportunity: one market, one side, one moment, one decision.

Everything the system needs in order to say PASS, WATCH or SHADOW_BET travels in this object, and
everything it used to decide is recorded ON the object. That is the point: a decision whose inputs are
not written down cannot be audited later, and a decision that can be edited after the outcome is known
is not evidence of anything.

Three properties are enforced rather than documented:

* **Immutable.** The dataclass is frozen and the fingerprint covers every field. Changing anything
  produces a different object with a different fingerprint; there is no in-place edit.
* **No real-money state.** `authority` is a constant. There is no enum member, no flag and no code path
  in this module that expresses a real wager.
* **A SHADOW_BET must survive qualification and must carry its own counter-argument.** A recommendation
  nobody stress-tested is not a recommendation.

Prices are DOLLARS in [0, 1] and always describe the named `side`: `executable_ask` is what it would cost
to buy that side right now, `executable_bid` what it could be sold for. The midpoint is carried because
it is informative, and is never the basis of an edge.
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, asdict, field, replace
from datetime import datetime, timezone

RESEARCH_AUTHORITY = "RESEARCH_ONLY_NO_REAL_MONEY"

#: the only decisions that exist
PASS = "PASS"
WATCH = "WATCH"
SHADOW_BET = "SHADOW_BET"
DECISIONS = (PASS, WATCH, SHADOW_BET)

#: timing labels, from tennis_edge.firstball.classify; START_UNKNOWN is never treated as pregame
POST_START = "POST_START"


class OpportunityError(RuntimeError):
    pass


class Decision:
    """Namespace, not an enum with a hidden fourth member. There is no real-money decision."""
    PASS = PASS
    WATCH = WATCH
    SHADOW_BET = SHADOW_BET
    ALL = DECISIONS


def _canonical(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)


def _hash(obj) -> str:
    return hashlib.sha256(_canonical(obj).encode()).hexdigest()


@dataclass(frozen=True)
class Opportunity:
    # identity ---------------------------------------------------------------------------------
    opportunity_id: str
    generated_at: str                    # ISO instant the row was produced
    physical_match_id: str               # our own match key, stable across tickers for one match
    event: str                           # Kalshi event ticker
    ticker: str                          # Kalshi market ticker
    family: str                          # MATCH_WINNER, TOTAL_GAMES, ...
    side: str                            # YES or NO on that ticker
    strike: str | None                   # the ladder line, where the family has one

    # what we think ----------------------------------------------------------------------------
    lane: str                            # MODEL_1 | MODEL_3 | MODEL_4 | MODEL_5 | CONSENSUS
    model_version: str
    fair_prob: float                     # our probability that THIS side pays $1
    uncertainty: float                   # our own standard error on fair_prob, not a market quantity
    fair_prob_low: float | None = None   # perturbation envelope (Phase 4)
    fair_prob_high: float | None = None

    # what the market says ---------------------------------------------------------------------
    executable_ask: float | None = None
    executable_bid: float | None = None
    midpoint: float | None = None
    spread: float | None = None
    available_size: float | None = None  # contracts at the displayed ask for this side
    fee_per_contract: float | None = None

    # the edge, in the four forms that mean different things -------------------------------------
    raw_edge: float | None = None                  # fair - ask
    fee_adjusted_edge: float | None = None         # fair - ask - fee
    uncertainty_adjusted_edge: float | None = None # fee-adjusted, discounted by our own error
    robust_edge: float | None = None               # worst case over the perturbation set
    bet_up_to: float | None = None                 # highest price still non-negative after fees
    ev_curve: dict = field(default_factory=dict)   # {"+0c": ev, "+1c": ev, ...}

    # what the evidence is worth ------------------------------------------------------------------
    data_quality_score: float | None = None
    data_quality_grade: str = ""
    serve_evidence_points: float | None = None     # thinner player's serve points
    identity_confidence: float | None = None
    source_freshness_days: float | None = None     # days between the newest result we hold and this match

    # when -------------------------------------------------------------------------------------
    first_ball_classification: str = "START_UNKNOWN"
    first_ball_confidence: str = "UNKNOWN"          # A | B | C | UNKNOWN
    seconds_to_first_ball: float | None = None
    seconds_to_first_ball_basis: str = "NONE"       # STRICT_TRUTH | NOMINAL_SCHEDULE | NONE
    quote_age_seconds: float | None = None

    # context ----------------------------------------------------------------------------------
    market_movement: dict = field(default_factory=dict)   # timestamp-safe, all strictly before generated_at
    liquidity_context: dict = field(default_factory=dict)

    # the decision -------------------------------------------------------------------------------
    selector_score: float | None = None
    selector_version: str = ""
    decision: str = PASS
    reason_for: str = ""
    reason_against: str = ""
    candidate_ids: tuple = ()
    qualification: dict = field(default_factory=dict)     # filter name -> bool, all must pass for SHADOW_BET

    authority: str = RESEARCH_AUTHORITY
    schema_version: int = 1
    fingerprint: str = ""

    def __post_init__(self):
        if self.decision not in DECISIONS:
            raise OpportunityError(f"decision must be one of {DECISIONS}, got {self.decision!r}")
        if self.authority != RESEARCH_AUTHORITY:
            raise OpportunityError("authority is fixed: this object cannot express a real wager")
        if self.side not in ("YES", "NO"):
            raise OpportunityError(f"side must be YES or NO, got {self.side!r}")
        if not 0.0 <= self.fair_prob <= 1.0:
            raise OpportunityError(f"fair_prob out of range: {self.fair_prob}")
        for name in ("executable_ask", "executable_bid", "midpoint"):
            v = getattr(self, name)
            if v is not None and not 0.0 <= v <= 1.0:
                raise OpportunityError(f"{name} out of range: {v}")
        if self.decision == SHADOW_BET:
            if self.first_ball_classification == POST_START:
                raise OpportunityError("a post-start market cannot be a SHADOW_BET")
            if not self.reason_against.strip():
                raise OpportunityError("a SHADOW_BET must carry its strongest opposing reason")
            failed = sorted(k for k, ok in self.qualification.items() if not ok)
            if failed or not self.qualification:
                raise OpportunityError(f"SHADOW_BET requires every qualification filter to pass; failed={failed}")
        object.__setattr__(self, "fingerprint", self._compute_fingerprint())

    def _compute_fingerprint(self) -> str:
        d = {k: v for k, v in asdict(self).items() if k != "fingerprint"}
        return _hash(d)

    def to_dict(self) -> dict:
        return asdict(self)

    def evolve(self, **changes) -> "Opportunity":
        """A NEW opportunity with those fields changed. The original is untouched and keeps its
        fingerprint; the copy gets its own. Nothing in this codebase edits an opportunity in place."""
        changes.pop("fingerprint", None)
        return replace(self, **changes)


class OpportunityStore:
    """Append-only, hash-chained, one file per UTC day. Same contract as the prediction ledger."""

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

    def append(self, opp: Opportunity) -> dict:
        d = opp.to_dict()
        day = (opp.generated_at or datetime.now(timezone.utc).isoformat())[:10]
        path = self._path(day)
        d["prev_hash"] = self._last_hash(path)
        d["row_hash"] = _hash({k: v for k, v in d.items() if k != "row_hash"})
        with open(path, "a") as f:
            f.write(json.dumps(d, separators=(",", ":"), default=str) + "\n")
        return d

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
                    body = {k: v for k, v in r.items() if k not in ("row_hash", "prev_hash", "fingerprint")}
                    if _hash(body) != r.get("fingerprint"):
                        problems.append(f"{fn}:{i}: fingerprint does not match the row content")
                    prev = r.get("row_hash")
        return problems
