"""Edge-candidate registry with a discovery/confirmation firewall.

One rule, enforced in code rather than in a document: **a candidate discovered on a dataset may not be
confirmed on that same dataset.** Every candidate records the window it was discovered on and the instant
it was frozen; confirmation evidence is only accepted from strictly after the freeze. A candidate that
tries to promote itself using its own discovery data is rejected, not warned about.

A candidate is a frozen, executable claim: an exact inclusion rule, a market family, a model version,
minimum sample size, and the accuracy, CLV and after-fee conditions it must meet. Nothing here can grant
real-money authority; the only statuses that exist stop at ELIGIBLE_FOR_CEO_REVIEW.
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone

DISCOVERY_ONLY = "DISCOVERY_ONLY"
PROSPECTIVE_PENDING = "PROSPECTIVE_PENDING"
REJECTED = "REJECTED"
SUPPORTED_FOR_MORE_RESEARCH = "SUPPORTED_FOR_MORE_RESEARCH"
ELIGIBLE_FOR_CEO_REVIEW = "ELIGIBLE_FOR_CEO_REVIEW"
STATUSES = (DISCOVERY_ONLY, PROSPECTIVE_PENDING, REJECTED, SUPPORTED_FOR_MORE_RESEARCH,
            ELIGIBLE_FOR_CEO_REVIEW)

#: statuses a candidate may reach only on evidence from strictly after its freeze
REQUIRES_OUT_OF_SAMPLE = (SUPPORTED_FOR_MORE_RESEARCH, ELIGIBLE_FOR_CEO_REVIEW)


class FirewallError(RuntimeError):
    """Raised when a candidate would be confirmed on the data that produced it."""


@dataclass
class EdgeCandidate:
    candidate_id: str
    hypothesis: str
    inclusion_rule: str                 # exact, machine-checkable prose; the filter a row must satisfy
    market_family: str
    model_version: str
    discovery_window_start: str         # ISO date
    discovery_window_end: str
    frozen_at: str                      # ISO instant; nothing before this counts as confirmation
    confirmation_start: str             # ISO instant; must be >= frozen_at
    minimum_n: int
    required_accuracy_condition: str    # e.g. "brier below the market's by >= 0.005 with a CI excluding 0"
    required_clv_condition: str         # e.g. "mean strict executable CLV > 0 with a CI excluding 0"
    required_after_fee_condition: str   # e.g. "after-fee EV per contract > 0 at the executable ask"
    status: str = DISCOVERY_ONLY
    rationale: str = ""
    strongest_opposing_reason: str = ""
    prereg_dimensions: tuple = ()
    post_hoc: bool = False
    evidence: list = field(default_factory=list)
    schema_version: int = 1

    def __post_init__(self):
        if self.status not in STATUSES:
            raise ValueError(f"bad status {self.status!r}")
        if self.confirmation_start < self.frozen_at:
            raise FirewallError(f"{self.candidate_id}: confirmation starts before the freeze")

    @property
    def fingerprint(self) -> str:
        body = {k: v for k, v in asdict(self).items() if k not in ("status", "evidence")}
        return hashlib.sha256(json.dumps(body, sort_keys=True, default=str).encode()).hexdigest()[:16]

    def to_dict(self):
        d = asdict(self)
        d["prereg_dimensions"] = list(self.prereg_dimensions)
        d["fingerprint"] = self.fingerprint
        return d


def add_evidence(cand: EdgeCandidate, *, observed_from: str, observed_to: str, n: int,
                 metrics: dict, note: str = "") -> EdgeCandidate:
    """Attach out-of-sample evidence. Evidence overlapping the discovery window is refused outright."""
    if observed_from < cand.frozen_at:
        raise FirewallError(
            f"{cand.candidate_id}: evidence starts {observed_from}, before the freeze at {cand.frozen_at}. "
            "A candidate cannot be confirmed on the data that produced it.")
    cand.evidence.append({"observed_from": observed_from, "observed_to": observed_to, "n": int(n),
                          "metrics": metrics, "note": note,
                          "recorded_at": datetime.now(timezone.utc).isoformat()})
    return cand


def set_status(cand: EdgeCandidate, status: str) -> EdgeCandidate:
    if status not in STATUSES:
        raise ValueError(f"bad status {status!r}")
    if status in REQUIRES_OUT_OF_SAMPLE:
        oos = [e for e in cand.evidence if e["observed_from"] >= cand.frozen_at]
        if not oos:
            raise FirewallError(f"{cand.candidate_id}: {status} needs evidence from after the freeze")
        if sum(e["n"] for e in oos) < cand.minimum_n:
            raise FirewallError(f"{cand.candidate_id}: {status} needs at least {cand.minimum_n} "
                                f"out-of-sample observations, has {sum(e['n'] for e in oos)}")
    cand.status = status
    return cand


def save(cand: EdgeCandidate, root: str) -> str:
    os.makedirs(root, exist_ok=True)
    path = os.path.join(root, f"{cand.candidate_id}.json")
    json.dump(cand.to_dict(), open(path, "w"), indent=1, default=str)
    return path


def load_all(root: str) -> list[EdgeCandidate]:
    out = []
    if not os.path.isdir(root):
        return out
    for fn in sorted(os.listdir(root)):
        if not fn.endswith(".json"):
            continue
        d = json.load(open(os.path.join(root, fn)))
        d.pop("fingerprint", None)
        d["prereg_dimensions"] = tuple(d.get("prereg_dimensions") or ())
        out.append(EdgeCandidate(**d))
    return out
