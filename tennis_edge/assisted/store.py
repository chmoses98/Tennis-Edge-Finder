"""Write-once assisted records and the append-only canonical ledgers compiled from them.

Why one file per record
-----------------------
Evidence reaches the `tennis-data` branch through `scripts/ci/publish_branch.py`, which COPIES a local
tree over the branch tip. Two workflows appending to one shared JSONL (the recorder dispatched by a
person, and RUN TENNIS) could therefore overwrite each other's rows: whichever pushed last would publish
its stale copy. A decision is instead written as its own file, whose path is its id:

  <root>/records/decisions/<YYYY-MM-DD>/<decision_id>.json
  <root>/records/wagers/<YYYY-MM-DD>/<wager_id>.json
  <root>/records/postmortems/<YYYY-MM-DD>/<postmortem_id>.json
  <root>/records/evidence/<YYYY-MM-DD>/<evidence_id>.json

A path that exists is never written again (duplicate ids are refused, never overwritten), and two
recorders can never touch the same path, so a publish can never lose one.

The canonical flat ledgers (`assisted_decisions.jsonl`, `assisted_wagers.jsonl`,
`assisted_postmortems.jsonl`, `assisted_evidence.jsonl`) are compiled from those records by ONE writer
(the RUN TENNIS pipeline). Compilation only ever APPENDS records it has not seen; a compiled row is
never rewritten, and every row is fingerprinted and hash-chained. If a record that was compiled later
changes or disappears, that is reported as an integrity violation -- it is never "fixed" by rewriting.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
from datetime import datetime, timezone

from . import ASSISTED_AUTHORITY, AUTONOMOUS_REAL_MONEY_AUTHORITY, CHATGPT_ASSISTED_TRACK, TRACK_NAME
from .schema import AssistedValidationError

KINDS = {"decisions": "AD", "wagers": "AW", "postmortems": "AP", "evidence": "AE"}
ID_KEY = {"decisions": "decision_id", "wagers": "wager_id", "postmortems": "postmortem_id",
          "evidence": "evidence_id"}
CANONICAL = {"decisions": "assisted_decisions.jsonl", "wagers": "assisted_wagers.jsonl",
             "postmortems": "assisted_postmortems.jsonl", "evidence": "assisted_evidence.jsonl"}
SETTLEMENTS_FILE = "assisted_settlements.jsonl"
TRACK_START_FILE = "TRACK_START.json"
_CHAIN_KEYS = ("fingerprint", "prev_hash", "row_hash")


def canonical_hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def fingerprint(rec: dict) -> str:
    return canonical_hash({k: v for k, v in rec.items() if k not in _CHAIN_KEYS})


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


# ---------------------------------------------------------------------------------------------- track start
def load_track_start(root: str) -> dict | None:
    p = os.path.join(root, TRACK_START_FILE)
    if not os.path.exists(p):
        return None
    r = json.load(open(p))
    r["_fingerprint_ok"] = fingerprint({k: v for k, v in r.items() if k != "_fingerprint_ok"}) == r.get("fingerprint")
    return r


def ensure_track_start(root: str, *, started_at: str, main_sha: str) -> dict | None:
    """Write the track's effective start ONCE. Returns the record if this call wrote it, else None.

    Only the scheduled pipeline calls this (one writer). Decisions created before `effective_start` are
    refused: the lane measures prospective decisions only and never reconstructs historical ones."""
    os.makedirs(root, exist_ok=True)
    p = os.path.join(root, TRACK_START_FILE)
    if os.path.exists(p):
        return None
    rec = {
        "track": TRACK_NAME,
        "effective_start": started_at,
        "activating_main_sha": main_sha,
        "AUTONOMOUS_REAL_MONEY_AUTHORITY": AUTONOMOUS_REAL_MONEY_AUTHORITY,
        "CHATGPT_ASSISTED_TRACK": CHATGPT_ASSISTED_TRACK,
        "authority": ASSISTED_AUTHORITY,
        "admission": ("decisions are admitted only if created at or after effective_start, recorded within the "
                      "maximum recording lag, and made before any observed first ball of their match; no "
                      "historical assisted decision is reconstructed"),
        "profitability_claim": "NONE: the track starts with zero evidence",
        "written_at": _now_iso(),
    }
    rec["fingerprint"] = fingerprint(rec)
    tmp = p + ".tmp"
    with open(tmp, "w") as f:
        json.dump(rec, f, indent=1)
    os.replace(tmp, p)
    return rec


# ---------------------------------------------------------------------------------------------- records
class RecordStore:
    """The write-once record tree under `<root>/records/`."""

    def __init__(self, root: str):
        self.root = root

    def _dir(self, kind: str) -> str:
        if kind not in KINDS:
            raise ValueError(f"unknown record kind {kind!r}")
        return os.path.join(self.root, "records", kind)

    def path_for(self, kind: str, rec_id: str, recorded_at: str) -> str:
        return os.path.join(self._dir(kind), recorded_at[:10], f"{rec_id}.json")

    def find(self, kind: str, rec_id: str) -> str | None:
        hits = glob.glob(os.path.join(self._dir(kind), "*", f"{rec_id}.json"))
        return hits[0] if hits else None

    def exists(self, kind: str, rec_id: str) -> bool:
        return self.find(kind, rec_id) is not None

    def get(self, kind: str, rec_id: str) -> dict | None:
        p = self.find(kind, rec_id)
        return json.load(open(p)) if p else None

    def write(self, kind: str, rec: dict) -> str:
        """Write a new record. Refuses (never overwrites) an id that already exists anywhere in the tree."""
        key = ID_KEY[kind]
        rec_id = rec.get(key)
        if not rec_id:
            raise AssistedValidationError("MISSING_ID", f"{kind} record has no {key}")
        if self.exists(kind, rec_id):
            raise AssistedValidationError("DUPLICATE_ID", f"{key} {rec_id} already exists; records are never overwritten")
        d = {k: v for k, v in rec.items() if k not in _CHAIN_KEYS}
        d["fingerprint"] = fingerprint(d)
        p = self.path_for(kind, rec_id, rec["recorded_at"])
        os.makedirs(os.path.dirname(p), exist_ok=True)
        # O_EXCL: even a concurrent writer in this process tree cannot replace an existing record
        fd = os.open(p, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o644)
        with os.fdopen(fd, "w") as f:
            json.dump(d, f, indent=1, sort_keys=False, default=str)
            f.write("\n")
        return p

    def records(self, kind: str) -> list[dict]:
        """Every record of a kind, oldest recording first (ties broken by id), with its integrity flag."""
        out = []
        for p in sorted(glob.glob(os.path.join(self._dir(kind), "*", "*.json"))):
            try:
                r = json.load(open(p))
            except (OSError, ValueError):
                out.append({"_path": p, "_unreadable": True, "_fingerprint_ok": False})
                continue
            r["_path"] = p
            r["_fingerprint_ok"] = fingerprint({k: v for k, v in r.items() if not k.startswith("_")}) == r.get("fingerprint")
            out.append(r)
        out.sort(key=lambda r: (r.get("recorded_at") or "", r.get(ID_KEY[kind]) or ""))
        return out


# ---------------------------------------------------------------------------------------------- JSONL
class AppendOnlyJsonl:
    """One hash-chained JSONL. Rows are appended, fingerprinted, and never rewritten."""

    def __init__(self, path: str):
        self.path = path

    def rows(self) -> list[dict]:
        if not os.path.exists(self.path):
            return []
        out = []
        with open(self.path) as f:
            for line in f:
                if line.strip():
                    out.append(json.loads(line))
        return out

    def _last_hash(self) -> str:
        rows = self.rows()
        return rows[-1].get("row_hash", "GENESIS") if rows else "GENESIS"

    def append(self, row: dict) -> dict:
        d = {k: v for k, v in row.items() if k not in _CHAIN_KEYS and not k.startswith("_")}
        d["fingerprint"] = fingerprint(d)
        d["prev_hash"] = self._last_hash()
        d["row_hash"] = canonical_hash({k: v for k, v in d.items() if k != "row_hash"})
        os.makedirs(os.path.dirname(self.path) or ".", exist_ok=True)
        with open(self.path, "a") as f:
            f.write(json.dumps(d, separators=(",", ":"), default=str) + "\n")
        return d

    def verify_chain(self) -> list[str]:
        problems, prev = [], "GENESIS"
        for i, r in enumerate(self.rows()):
            if r.get("prev_hash") != prev:
                problems.append(f"{os.path.basename(self.path)}:{i}: prev_hash mismatch (row removed or reordered)")
            if canonical_hash({k: v for k, v in r.items() if k != "row_hash"}) != r.get("row_hash"):
                problems.append(f"{os.path.basename(self.path)}:{i}: row modified after it was written")
            if fingerprint(r) != r.get("fingerprint"):
                problems.append(f"{os.path.basename(self.path)}:{i}: fingerprint mismatch")
            prev = r.get("row_hash")
        return problems


def compile_canonical(root: str, kind: str) -> dict:
    """Append every not-yet-compiled record of `kind` to its canonical JSONL; verify the rest.

    Returns {appended, total, violations}. A compiled row whose record is now missing, or whose record's
    fingerprint no longer matches the compiled one, is an integrity violation (Part 11): reported, never
    repaired by rewriting either side."""
    key = ID_KEY[kind]
    ledger = AppendOnlyJsonl(os.path.join(root, CANONICAL[kind]))
    compiled = ledger.rows()
    violations = list(ledger.verify_chain())
    by_id = {r.get(key): r for r in compiled}
    recs = RecordStore(root).records(kind)
    rec_ids = set()
    appended = 0
    for r in recs:
        if r.get("_unreadable"):
            violations.append(f"unreadable record {r['_path']}")
            continue
        rid = r.get(key)
        if rid in rec_ids:
            violations.append(f"duplicate {key} {rid} in the record tree")
            continue
        rec_ids.add(rid)
        if not r["_fingerprint_ok"]:
            violations.append(f"{key} {rid}: record modified after it was written")
        if rid in by_id:
            body = {k: v for k, v in r.items() if not k.startswith("_")}
            if fingerprint(body) != by_id[rid].get("fingerprint"):
                changed = sorted(k for k in set(body) | set(by_id[rid])
                                 if k not in _CHAIN_KEYS and body.get(k) != by_id[rid].get(k))
                violations.append(f"{key} {rid}: record differs from its compiled row (immutable fields changed: {changed})")
            continue
        if not r["_fingerprint_ok"]:
            continue                          # a tampered record is never compiled into the canonical ledger
        body = {k: v for k, v in r.items() if not k.startswith("_") and k != "fingerprint"}
        ledger.append(body)
        appended += 1
    for rid in by_id:
        if rid not in rec_ids:
            violations.append(f"{key} {rid}: compiled row has no record (record deleted)")
    return {"kind": kind, "appended": appended, "total": len(compiled) + appended, "violations": violations}


def changed_immutable_fields(original: dict, current: dict, fields) -> list[str]:
    """Which of `fields` differ between two versions of one record (used to NAME a violation)."""
    return [k for k in fields if original.get(k) != current.get(k)]
