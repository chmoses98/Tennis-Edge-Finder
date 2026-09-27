"""Read-only access to the immutable prospective evidence the confirmation layer scores.

Every loader here READS. None of them writes, sorts in place, or normalises a stored row: what comes back
is what was captured, plus the path and line hash it came from, so an evidence row can cite its source.

Layout (the `tennis-data` branch, extracted under one data root):

  research/edge_candidates/*.json           frozen candidate definitions
  research/external/dislocations/*.jsonl    Wave 4/5 dislocation ledger (external_v1)
  research/external/market/*.jsonl          raw external-venue observations (Bovada, Smarkets)
  research/ledger/*.jsonl                   the prediction ledger (Gen-1 lane)
  research/opportunities/*.jsonl            shadow-board opportunities (fair_v1 + selector_v1)
  research/clv/<run>.jsonl                  CLV v2 rows per settle run (derived)
  firstball/store/                          first-ball observations and truths (append-only)
  kalshi/capture/<day>/*.{quotes,books,candles,settlements}.jsonl.gz   Kalshi capture passes
"""
from __future__ import annotations

import glob
import gzip
import hashlib
import json
import os
from datetime import datetime


def iso(x) -> datetime | None:
    if isinstance(x, datetime):
        return x
    if isinstance(x, str) and x:
        try:
            return datetime.fromisoformat(x.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None


def line_hash(line: str) -> str:
    return hashlib.sha256(line.strip().encode()).hexdigest()


def iter_jsonl(pattern: str, *, gz: bool | None = None):
    """(path, line_hash, row) for every parseable line of every file matching `pattern`, in path order."""
    for f in sorted(glob.glob(pattern)):
        opener = gzip.open if (gz if gz is not None else f.endswith(".gz")) else open
        with opener(f, "rt") as fh:
            for line in fh:
                line = line.strip()
                if not line:
                    continue
                try:
                    row = json.loads(line)
                except ValueError:
                    continue                       # a truncated tail never poisons the stream
                yield f, line_hash(line), row


# --------------------------------------------------------------------------- frozen candidates
def load_candidates(root: str) -> dict[str, dict]:
    """candidate_id -> the frozen definition exactly as stored, with its fingerprint re-verified.

    The fingerprint is recomputed with the registry's own definition. A mismatch means the definition
    was edited after it was frozen, and the candidate is flagged rather than scored."""
    from tennis_edge.research.registry import EdgeCandidate
    out = {}
    for p in sorted(glob.glob(os.path.join(root, "*.json"))):
        raw = json.load(open(p))
        d = dict(raw)
        stored_fp = d.pop("fingerprint", None)
        d["prereg_dimensions"] = tuple(d.get("prereg_dimensions") or ())
        recomputed = EdgeCandidate(**d).fingerprint
        raw["_path"] = p
        raw["_file_sha256"] = hashlib.sha256(open(p, "rb").read()).hexdigest()
        raw["_fingerprint_ok"] = recomputed == stored_fp
        raw["_fingerprint_recomputed"] = recomputed
        out[raw["candidate_id"]] = raw
    return out


# --------------------------------------------------------------------------- Kalshi settlement truth
def settlements(capture_root: str, discovery_dir: str | None = None) -> dict[str, dict]:
    """ticker -> the exchange's own settlement record, with its source and line hash.

    Primary source: the capture conductor's hourly `status=settled` sweep. Fallback: the `settled` block
    of the latest discovery snapshot. Both are the exchange's published result; nothing is inferred from
    prices, and a record without a terminal result is not a settlement."""
    out: dict[str, dict] = {}
    for f, h, r in iter_jsonl(os.path.join(capture_root, "*", "*.settlements*.jsonl.gz")):
        t = r.get("ticker")
        if not t or (r.get("result") or "") not in ("yes", "no", "scalar"):
            continue
        if r.get("settlement_value_dollars") in (None, ""):
            continue
        out.setdefault(t, {**r, "_source": "capture_settlements", "_path": os.path.basename(f), "_line_hash": h})
    if discovery_dir:
        for p in sorted(glob.glob(os.path.join(discovery_dir, "markets", "*.json"))):
            blocks = json.load(open(p))
            for m in (blocks.get("settled") or {}).get("markets") or []:
                t = m.get("ticker")
                if not t or t in out or (m.get("result") or "") not in ("yes", "no", "scalar"):
                    continue
                if m.get("settlement_value_dollars") in (None, ""):
                    continue
                out[t] = {**m, "_source": "discovery_settled", "_path": os.path.basename(p),
                          "_line_hash": hashlib.sha256(json.dumps(m, sort_keys=True).encode()).hexdigest()}
    return out


def settlement_payout(rec: dict | None) -> tuple[str | None, float | None, str | None]:
    """(result, dollars paid per YES contract, settled_at) from a settlement record."""
    if not rec:
        return None, None, None
    try:
        v = float(rec.get("settlement_value_dollars"))
    except (TypeError, ValueError):
        return None, None, None
    return rec.get("result"), v, rec.get("settlement_ts")


# --------------------------------------------------------------------------- first-ball truth
def first_ball_truths(store_root: str) -> dict:
    from tennis_edge.firstball.store import FirstBallStore
    if not os.path.isdir(store_root):
        return {}
    return FirstBallStore(store_root).latest_truths()


# --------------------------------------------------------------------------- capture passes
def capture_quote_records(capture_root: str, since_iso: str | None = None):
    """(run_id, captured_at, record) for every captured market record, chronologically by file."""
    for f, _h, r in iter_jsonl(os.path.join(capture_root, "*", "*.quotes.jsonl.gz")):
        if since_iso and (r.get("captured_at") or "") < since_iso:
            continue
        yield r.get("run_id"), r.get("captured_at"), r


def capture_books(capture_root: str, since_iso: str | None = None):
    """(path, line_hash, record) for every captured order book at or after `since_iso`."""
    for f, h, r in iter_jsonl(os.path.join(capture_root, "*", "*.books.jsonl.gz")):
        if since_iso and (r.get("captured_at") or "") < since_iso:
            continue
        yield f, h, r


def capture_manifests(capture_root: str) -> list[dict]:
    out = []
    for p in sorted(glob.glob(os.path.join(capture_root, "*", "*.manifest.json"))):
        try:
            out.append(json.load(open(p)))
        except ValueError:
            continue
    return out


# --------------------------------------------------------------------------- external venues
def external_match_winner_obs(market_root: str, observed_at: set[str]) -> dict:
    """(observed_at, source) -> list of raw MATCH_WINNER observations from the external store.

    Only the scan instants in `observed_at` are kept. The store row is the venue observation exactly as
    fetched (before mapping), so it carries the venue's own timestamp -- which is what the frozen W4
    freshness condition is about."""
    out: dict = {}
    for f, h, r in iter_jsonl(os.path.join(market_root, "*.jsonl")):
        if r.get("market_family") != "MATCH_WINNER" or r.get("observed_at") not in observed_at:
            continue
        out.setdefault((r["observed_at"], r["source"]), []).append({**r, "_line_hash": h})
    return out
