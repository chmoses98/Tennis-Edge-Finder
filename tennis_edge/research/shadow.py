"""MODEL-agnostic prospective shadow board. No real bets, ever.

A frozen recommendation ledger. Rows are written when a candidate observation is generated and are never
regenerated afterwards: the file is append-only and hash-chained, exactly like the prediction ledger, so
a row cannot be quietly improved once the outcome is known. Settlement information is APPENDED as a
separate record keyed by shadow_id, never merged back into the original row.

Every row carries the strongest reason NOT to take it. That field is mandatory: a recommendation with no
stated counter-argument is a recommendation nobody stress-tested.
"""
from __future__ import annotations

import hashlib
import json
import os
import uuid
from dataclasses import dataclass, asdict, field
from datetime import datetime, timezone

REQUIRED = ("match_id", "ticker", "family", "lane", "model_version", "market_prob", "executable_ask",
            "first_ball_classification", "rationale", "strongest_opposing_reason")


class ShadowError(RuntimeError):
    pass


def _hash(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


@dataclass
class ShadowRow:
    match_id: str
    ticker: str
    family: str
    lane: str                        # MODEL_1 | MODEL_3 | MODEL_4 | MODEL_5 | COHERENCE
    model_version: str
    market_prob: float | None
    executable_bid: float | None
    executable_ask: float | None
    available_size: float | None
    spread: float | None
    fee_estimate: float | None
    fundamental_prob: float | None = None
    hybrid_prob: float | None = None
    edge: float | None = None
    fair_price: float | None = None
    bet_up_to: float | None = None
    data_quality: str = ""
    uncertainty: float | None = None
    first_ball_classification: str = "START_UNKNOWN"
    candidate_id: str = ""
    rationale: str = ""
    strongest_opposing_reason: str = ""
    authority: str = "RESEARCH_ONLY_NO_REAL_MONEY"

    def to_dict(self):
        return asdict(self)


class ShadowBoard:
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

    def append(self, row: ShadowRow) -> dict:
        d = row.to_dict()
        missing = [k for k in REQUIRED if d.get(k) in (None, "")]
        if missing:
            raise ShadowError(f"shadow row missing required fields {missing}")
        now = datetime.now(timezone.utc)
        d["shadow_id"] = str(uuid.uuid4())
        d["generated_at"] = now.isoformat()
        path = self._path(now.strftime("%Y-%m-%d"))
        d["prev_hash"] = self._last_hash(path)
        d["row_hash"] = _hash({k: v for k, v in d.items() if k != "row_hash"})
        with open(path, "a") as f:
            f.write(json.dumps(d, separators=(",", ":"), default=str) + "\n")
        return d

    def settle(self, shadow_id: str, *, outcome, exchange_settlement=None, strict_close=None,
               executable_clv=None, midpoint_clv=None, after_fee_pl=None, note: str = "") -> dict:
        """Settlement is APPENDED as its own record. The original row is never touched."""
        now = datetime.now(timezone.utc)
        rec = {"kind": "settlement", "shadow_id": shadow_id, "settled_at": now.isoformat(),
               "outcome": outcome, "exchange_settlement": exchange_settlement,
               "strict_close": strict_close, "executable_clv": executable_clv,
               "midpoint_clv": midpoint_clv, "hypothetical_after_fee_pl": after_fee_pl, "note": note}
        path = os.path.join(self.root, "settlements.jsonl")
        rec["prev_hash"] = self._last_hash(path)
        rec["row_hash"] = _hash({k: v for k, v in rec.items() if k != "row_hash"})
        with open(path, "a") as f:
            f.write(json.dumps(rec, separators=(",", ":"), default=str) + "\n")
        return rec

    def rows(self):
        for fn in sorted(os.listdir(self.root)):
            if fn.endswith(".jsonl") and fn != "settlements.jsonl":
                with open(os.path.join(self.root, fn)) as f:
                    for line in f:
                        if line.strip():
                            yield json.loads(line)

    def verify_chain(self) -> list[str]:
        v = []
        for fn in sorted(os.listdir(self.root)):
            if not fn.endswith(".jsonl"):
                continue
            prev = "GENESIS"
            with open(os.path.join(self.root, fn)) as f:
                for i, line in enumerate(f):
                    if not line.strip():
                        continue
                    r = json.loads(line)
                    if r.get("prev_hash") != prev:
                        v.append(f"{fn}:{i}: prev_hash mismatch")
                    if _hash({k: val for k, val in r.items() if k != "row_hash"}) != r.get("row_hash"):
                        v.append(f"{fn}:{i}: row modified after the fact")
                    prev = r.get("row_hash")
        return v
