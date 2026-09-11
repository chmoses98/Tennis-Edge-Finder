"""Append-only, hash-chained storage for first-ball observations and derived truths.

Two files per UTC day under the store root:
  observations/<day>.jsonl   raw readings. Written once. Never edited, never deleted.
  truths/<day>.jsonl         derived FirstBallTruth rows, one per (match_id, derivation_version).

Re-deriving a match's truth from better evidence APPENDS a row with derivation_version + 1. Readers use
`latest_truths()`, which keeps the highest version per match. That is how "first-ball truth recovered
days later" updates a classification without rewriting a single historical byte.
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone

from .truth import FirstBallTruth, FirstBallObservation


def _hash(obj: dict) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


class FirstBallStore:
    def __init__(self, root: str):
        self.root = root
        self.obs_dir = os.path.join(root, "observations")
        self.truth_dir = os.path.join(root, "truths")
        os.makedirs(self.obs_dir, exist_ok=True)
        os.makedirs(self.truth_dir, exist_ok=True)

    # ------------------------------------------------------------------ writing
    @staticmethod
    def _append(path: str, row: dict) -> dict:
        prev = "GENESIS"
        if os.path.exists(path):
            with open(path) as f:
                for line in f:
                    if line.strip():
                        prev = json.loads(line).get("row_hash", prev)
        row = dict(row)
        row["prev_hash"] = prev
        row["row_hash"] = _hash({k: v for k, v in row.items() if k != "row_hash"})
        with open(path, "a") as f:
            f.write(json.dumps(row, separators=(",", ":"), default=str) + "\n")
        return row

    def add_observation(self, o: FirstBallObservation) -> dict:
        day = o.observed_at_utc.astimezone(timezone.utc).strftime("%Y-%m-%d")
        return self._append(os.path.join(self.obs_dir, f"{day}.jsonl"), o.to_dict())

    def add_truth(self, t: FirstBallTruth) -> dict:
        day = (t.created_at or datetime.now(timezone.utc)).astimezone(timezone.utc).strftime("%Y-%m-%d")
        return self._append(os.path.join(self.truth_dir, f"{day}.jsonl"), t.to_dict())

    def next_derivation_version(self, match_id: str) -> int:
        cur = self.latest_truths().get(match_id)
        return (cur.derivation_version + 1) if cur else 1

    # ------------------------------------------------------------------ reading
    @staticmethod
    def _rows(d: str):
        if not os.path.isdir(d):
            return
        for fn in sorted(os.listdir(d)):
            if fn.endswith(".jsonl"):
                with open(os.path.join(d, fn)) as f:
                    for line in f:
                        if line.strip():
                            yield json.loads(line)

    def observations(self, match_id: str | None = None) -> list[FirstBallObservation]:
        out = []
        for r in self._rows(self.obs_dir):
            if match_id and r.get("match_id") != match_id:
                continue
            r = {k: v for k, v in r.items() if k not in ("prev_hash", "row_hash")}
            for k in ("observed_at_utc", "source_event_timestamp", "explicit_start_utc"):
                if r.get(k):
                    r[k] = datetime.fromisoformat(r[k].replace("Z", "+00:00"))
            out.append(FirstBallObservation(**r))
        return out

    def truth_rows(self) -> list[dict]:
        return list(self._rows(self.truth_dir))

    def latest_truths(self) -> dict[str, FirstBallTruth]:
        best: dict[str, FirstBallTruth] = {}
        for r in self._rows(self.truth_dir):
            t = FirstBallTruth.from_dict(r)
            cur = best.get(t.match_id)
            if cur is None or t.derivation_version > cur.derivation_version:
                best[t.match_id] = t
        return best

    def verify_chain(self) -> list[str]:
        v = []
        for d in (self.obs_dir, self.truth_dir):
            for fn in sorted(os.listdir(d)) if os.path.isdir(d) else []:
                if not fn.endswith(".jsonl"):
                    continue
                prev = "GENESIS"
                with open(os.path.join(d, fn)) as f:
                    for i, line in enumerate(f):
                        if not line.strip():
                            continue
                        r = json.loads(line)
                        if r.get("prev_hash") != prev:
                            v.append(f"{os.path.basename(d)}/{fn}:{i}: prev_hash mismatch")
                        if _hash({k: val for k, val in r.items() if k != "row_hash"}) != r.get("row_hash"):
                            v.append(f"{os.path.basename(d)}/{fn}:{i}: row modified")
                        prev = r.get("row_hash")
        return v
