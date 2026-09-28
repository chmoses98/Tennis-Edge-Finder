"""Append-only producer stores and write-once experiment-start records."""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
from datetime import datetime, timezone

PRODUCER_SCHEMA_VERSION = 1

#: the five candidates whose decision probabilities were never produced after their freeze, and which
#: producer each needs. The candidate definitions themselves are not touched.
PRODUCERS = {
    "shadow_board_v1": {
        "entrypoint": "scripts/ops/shadow_board.py",
        "model_version": "gen2_dyn_hier_sr_v1+fair_v1+selector_v1",
        "candidates": ("EC-2026-003-GEN2-MODERATE-EVIDENCE", "W3-2026-001-ABSTAIN-ITF",
                       "W3-2026-002-NONITF-POSITIVE-EDGE"),
    },
    "model4_board_v1": {
        "entrypoint": "scripts/ops/model4_board.py",
        "model_version": "market_conditioned_v1 + gen2_dyn_hier_sr_v1",
        "candidates": ("EC-2026-001-MKTCOND-EXACT-SCORE", "EC-2026-002-MKTCOND-GAME-SPREAD"),
    },
}
CANDIDATE_PRODUCER = {cid: name for name, p in PRODUCERS.items() for cid in p["candidates"]}

#: how each producer's rows are admitted on timing, fixed at experiment start and before any outcome.
TIMING_ADMISSION = {
    "EC-2026-003-GEN2-MODERATE-EVIDENCE": "accuracy on rows not confirmed POST_START/AMBIGUOUS; strict CLV on STRICT_PREGAME (A/B) only",
    "W3-2026-001-ABSTAIN-ITF": "rows not confirmed POST_START/AMBIGUOUS (the frozen rule has no first-ball condition and ITF has no first-ball source)",
    "W3-2026-002-NONITF-POSITIVE-EDGE": "accuracy and P&L on rows not confirmed POST_START/AMBIGUOUS; strict CLV on STRICT_PREGAME (A/B) only",
    "EC-2026-001-MKTCOND-EXACT-SCORE": "predictions refused once the first-ball store has seen the match start; rows later confirmed POST_START/AMBIGUOUS excluded",
    "EC-2026-002-MKTCOND-GAME-SPREAD": "as EC-2026-001",
}


def canonical_hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def code_sha(proj: str) -> str:
    sha = os.environ.get("GITHUB_SHA")
    if sha:
        return sha
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=proj, capture_output=True, text=True).stdout.strip() or "unknown"
    except Exception:                                                        # noqa: BLE001
        return "unknown"


class ProducerStore:
    """One hash-chained JSONL per UTC day. Rows are fingerprinted and never rewritten."""

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

    def append(self, row: dict) -> dict:
        if "predicted_at" not in row:
            raise ValueError("a producer row must carry its prediction timestamp")
        d = dict(row)
        d.setdefault("schema_version", PRODUCER_SCHEMA_VERSION)
        d.setdefault("authority", "RESEARCH_ONLY_NO_REAL_MONEY")
        if d["authority"] != "RESEARCH_ONLY_NO_REAL_MONEY":
            raise ValueError("authority is fixed")
        d["fingerprint"] = canonical_hash({k: v for k, v in d.items() if k not in ("fingerprint", "prev_hash", "row_hash")})
        path = self._path(d["predicted_at"][:10])
        d["prev_hash"] = self._last_hash(path)
        d["row_hash"] = canonical_hash({k: v for k, v in d.items() if k != "row_hash"})
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
                    if canonical_hash({k: v for k, v in r.items() if k != "row_hash"}) != r.get("row_hash"):
                        problems.append(f"{fn}:{i}: row modified after it was written")
                    prev = r.get("row_hash")
        return problems


def start_record_path(root: str, candidate_id: str) -> str:
    return os.path.join(root, f"{candidate_id}.json")


def load_start_records(root: str) -> dict[str, dict]:
    out = {}
    if not os.path.isdir(root):
        return out
    for fn in sorted(os.listdir(root)):
        if fn.endswith(".json"):
            r = json.load(open(os.path.join(root, fn)))
            body = {k: v for k, v in r.items() if k != "fingerprint"}
            r["_fingerprint_ok"] = canonical_hash(body) == r.get("fingerprint")
            out[r["candidate_id"]] = r
    return out


def ensure_experiment_starts(root: str, producer: str, *, started_at: str, main_sha: str,
                             candidate_defs: dict, producer_version: str) -> list[dict]:
    """Write the experiment-start record for every candidate this producer serves, ONCE.

    Called by the producer after it has written its first live row. An existing record is never
    rewritten, whatever the caller passes: the first production run fixes the effective start."""
    os.makedirs(root, exist_ok=True)
    written = []
    for cid in PRODUCERS[producer]["candidates"]:
        path = start_record_path(root, cid)
        if os.path.exists(path):
            continue
        cand = candidate_defs.get(cid) or {}
        rec = {
            "candidate_id": cid,
            "original_frozen_at": cand.get("frozen_at"),
            "original_confirmation_start": cand.get("confirmation_start"),
            "producer_missing_period_start": cand.get("confirmation_start"),
            "producer_missing_period_end": started_at,
            "effective_scorable_start": started_at,
            "model_version": cand.get("model_version"),
            "producer": producer,
            "producer_entrypoint": PRODUCERS[producer]["entrypoint"],
            "producer_version": producer_version,
            "activating_main_sha": main_sha,
            "timing_admission": TIMING_ADMISSION.get(cid),
            "reason_prior_period_unscorable": (
                "the frozen decision probability this candidate needs was not produced by any scheduled job between "
                "its confirmation_start and this producer's first production run; those observations are "
                "permanently UNSCORABLE and are never reconstructed"),
            "candidate_definition_fingerprint": cand.get("fingerprint"),
            "written_at": datetime.now(timezone.utc).isoformat(),
            "authority": "RESEARCH_ONLY_NO_REAL_MONEY",
        }
        rec["fingerprint"] = canonical_hash(rec)
        tmp = path + ".tmp"
        with open(tmp, "w") as f:
            json.dump(rec, f, indent=1)
        os.replace(tmp, path)
        written.append(rec)
    return written
