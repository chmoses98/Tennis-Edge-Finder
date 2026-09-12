"""Kalshi against an independent venue, with our own model as a witness rather than the plaintiff.

Wave 3 established that our model's disagreement with Kalshi does not identify Kalshi's errors. Wave 4's
hypothesis is that another market's disagreement might. So the roles are deliberately unequal here:

    the EXTERNAL reference proposes,
    our MODEL corroborates or objects,
    and nothing our model says on its own can produce a SHADOW_BET.

`triangulate` names which of the three is the odd one out. The interesting case is KALSHI_LONE_OUTLIER --
an independent venue and our fundamental model both on the same side of the Kalshi price. The case that
looks identical on a screener and means the opposite is MODEL_LONE_OUTLIER, where two markets agree with
each other and only we disagree; Wave 3 measured what that is worth, and it is worth less than nothing.

EXTERNAL_EDGE is external fair minus the executable Kalshi ask minus the fee. It is a DISLOCATION SIGNAL.
It is not an edge, and this module never calls it one.
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone

# triangulation outcomes
MARKETS_AGREE = "MARKETS_AGREE"
KALSHI_LONE_OUTLIER = "KALSHI_LONE_OUTLIER"
MODEL_LONE_OUTLIER = "MODEL_LONE_OUTLIER"
EXTERNAL_LONE_OUTLIER = "EXTERNAL_LONE_OUTLIER"
ALL_THREE_DISAGREE = "ALL_THREE_DISAGREE"
INSUFFICIENT_INPUTS = "INSUFFICIENT_INPUTS"

#: below this the two prices are the same price with a spread between them, not a dislocation
AGREEMENT_TOLERANCE = 0.02


def _hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"),
                                     default=str).encode()).hexdigest()


def triangulate(kalshi_mid: float | None, external_fair: float | None, model_fair: float | None,
                tol: float = AGREEMENT_TOLERANCE) -> dict:
    """Which of the three is the odd one out, and by how much.

    Corroboration is about DIRECTION, not proximity. A model at 50% when the external venue says 52% and
    Kalshi says 46% is agreeing that Kalshi is too low, and that is the whole content of the claim; the
    two-cent gap between us and the venue is noise at this sample size. What would NOT be corroboration
    is our model pointing the other way, and that gets its own class.
    """
    eps = 1e-9
    if kalshi_mid is None or external_fair is None:
        return {"class": INSUFFICIENT_INPUTS, "ext_vs_kalshi": None, "model_vs_kalshi": None,
                "model_vs_external": None, "model_overshoots_external": None}
    ext_k = external_fair - kalshi_mid
    mod_k = None if model_fair is None else model_fair - kalshi_mid
    mod_e = None if model_fair is None else model_fair - external_fair
    out = {"ext_vs_kalshi": ext_k, "model_vs_kalshi": mod_k, "model_vs_external": mod_e,
           "model_overshoots_external": None if mod_e is None else abs(mod_e) > tol + eps}

    if abs(ext_k) <= tol + eps:
        # the venues agree with each other. The only question left is whether WE are out of step, which
        # Wave 3 measured and found worthless as a reason to act.
        out["class"] = (MODEL_LONE_OUTLIER if mod_k is not None and abs(mod_k) > tol + eps
                        else MARKETS_AGREE)
        return out

    if mod_k is None:
        out["class"] = KALSHI_LONE_OUTLIER
        out["note"] = "no model probability; the classification rests on the two markets only"
        return out

    same_side = (mod_k > eps and ext_k > eps) or (mod_k < -eps and ext_k < -eps)
    if same_side:
        out["class"] = KALSHI_LONE_OUTLIER
    elif abs(mod_k) <= tol + eps:
        out["class"] = EXTERNAL_LONE_OUTLIER          # our model sides with the Kalshi price
    else:
        out["class"] = ALL_THREE_DISAGREE             # our model runs against the external venue too
    return out


@dataclass(frozen=True)
class Dislocation:
    generated_at: str
    physical_match_id: str
    kalshi_ticker: str
    kalshi_event: str
    side: str
    market_family: str
    kalshi_bid: float | None
    kalshi_ask: float | None
    kalshi_mid: float | None
    kalshi_size: float | None
    kalshi_spread: float | None
    kalshi_fee: float | None
    kalshi_quote_age_s: float | None
    external_sources: tuple = ()
    external_prices: dict = field(default_factory=dict)      # source -> de-vigged probability
    external_raw: dict = field(default_factory=dict)         # source -> raw implied, before the margin
    external_fair: float | None = None                       # the reference value
    reference_kind: str = "NONE"
    reference_dispersion: float | None = None
    external_quote_age_s: float | None = None
    n_independent_groups: int = 0
    model_fair: float | None = None
    model_uncertainty: float | None = None
    external_vs_kalshi: float | None = None
    model_vs_kalshi: float | None = None
    model_vs_external: float | None = None
    triangulation: str = INSUFFICIENT_INPUTS
    external_edge: float | None = None                       # reference - ask - fee. A SIGNAL, not an edge.
    first_ball_classification: str = "START_UNKNOWN"
    first_ball_confidence: str = "UNKNOWN"
    strict_pregame: bool = False
    decision: str = "PASS"
    reason_for: str = ""
    reason_against: str = ""
    candidate_ids: tuple = ()
    selector_version: str = ""
    authority: str = "RESEARCH_ONLY_NO_REAL_MONEY"
    schema_version: int = 1
    fingerprint: str = ""

    def __post_init__(self):
        if self.decision not in ("PASS", "WATCH", "SHADOW_BET"):
            raise ValueError(f"unknown decision {self.decision!r}")
        if self.authority != "RESEARCH_ONLY_NO_REAL_MONEY":
            raise ValueError("authority is fixed: this object cannot express a real wager")
        if self.decision == "SHADOW_BET":
            if self.external_fair is None:
                raise ValueError("a SHADOW_BET must rest on an external reference, not on our model alone")
            if self.triangulation not in (KALSHI_LONE_OUTLIER,):
                raise ValueError("a SHADOW_BET requires Kalshi to be the outlier, not us")
            if not self.reason_against.strip():
                raise ValueError("a SHADOW_BET must carry its strongest opposing reason")
        object.__setattr__(self, "fingerprint",
                           _hash({k: v for k, v in asdict(self).items() if k != "fingerprint"}))

    def to_dict(self) -> dict:
        return asdict(self)


class DislocationLedger:
    """Append-only, hash-chained, one file per UTC day. History is never regenerated."""

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

    def append(self, row: Dislocation) -> dict:
        d = row.to_dict()
        day = (row.generated_at or datetime.now(timezone.utc).isoformat())[:10]
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
                    prev = r.get("row_hash")
        return problems
