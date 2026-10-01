"""The candidate-evidence row, and the append-only store that holds it.

An evidence row is DERIVED. It points at an immutable original observation (a dislocation row, a
capture-pass order book, ...) by id and by hash, restates the fields the frozen inclusion rule needed
exactly as they were preserved at capture, and then attaches truth that could only be known later:
settlement, first-ball timing, the strict executable close. The original observation is never written.

Two kinds of field, kept apart on purpose:

  observation fields   copied from the immutable capture; identical in every version of the row
  attachment fields    settlement, timing, strict close, P&L; allowed to arrive late, so a later
                       harvest may append a NEWER VERSION of the row when, say, a match settles

The store is append-only and hash-chained per candidate. A harvest never rewrites a line: it appends a
row only when that row's content fingerprint is new, so re-running a harvest on unchanged evidence
writes nothing, and a row whose settlement has since arrived is appended as a new version. Readers take
the latest version per (candidate_id, observation_id).
"""
from __future__ import annotations

import hashlib
import json
import os
from dataclasses import dataclass, asdict, field

EVIDENCE_SCHEMA_VERSION = 1

# inclusion outcomes
INCLUDED = "INCLUDED"
EXCLUDED = "EXCLUDED"
UNSCORABLE = "UNSCORABLE"

# exclusion reasons (a row can carry several; the first is the binding one)
R_PRE_FREEZE = "OBSERVED_BEFORE_CONFIRMATION_START"
R_RULE_FAILED = "FROZEN_INCLUSION_RULE_NOT_MET"
R_REOBSERVATION = "REOBSERVATION_OF_CONTRACT_ALREADY_COUNTED"
R_TIMING_UNKNOWN = "TIMING_START_UNKNOWN"
R_TIMING_POST = "TIMING_POST_START"
R_TIMING_AMBIG = "TIMING_AMBIGUOUS"
R_TRUTH_C = "FIRST_BALL_CONFIDENCE_C_ONLY"
R_MISSING_FIELD = "MISSING_HISTORICAL_FIELD"
R_FRESHNESS_UNVERIFIED = "EXTERNAL_FRESHNESS_UNVERIFIABLE"
R_FRESHNESS_MIXED = "EXTERNAL_FRESHNESS_AMBIGUOUS"
#: the exchange's own recorded settlement_ts is at or before the observation: the contract was already
#: terminal when the producer priced it, so the row cannot be prospective pregame evidence. Distinct from
#: TIMING_POST_START (play known to have begun): this needs no first-ball source, only Kalshi's settlement.
R_SETTLED_BEFORE_OBSERVATION = "MARKET_SETTLED_BEFORE_OBSERVATION"


def canonical_hash(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def file_sha256(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


@dataclass(frozen=True)
class EvidenceRow:
    # ---- identity
    candidate_id: str
    observation_id: str                 # stable id of the ORIGINAL observation (its row hash or key)
    physical_match_id: str | None
    ticker: str | None
    market_family: str | None
    side: str | None
    # ---- the freeze firewall
    captured_at: str | None
    candidate_freeze_at: str
    confirmation_start: str
    candidate_fingerprint: str
    # ---- decision-time fields, as preserved at capture
    model_version: str | None = None
    fair_probability: float | None = None          # the probability the frozen rule decides on
    model_probability: float | None = None         # our model, where it is a witness rather than the claim
    kalshi_bid: float | None = None
    kalshi_ask: float | None = None
    kalshi_mid: float | None = None
    kalshi_spread: float | None = None
    fee: float | None = None
    displayed_size: float | None = None
    kalshi_quote_age_s: float | None = None
    external_reference: float | None = None
    external_sources: tuple = ()
    external_venue_ages_s: dict = field(default_factory=dict)
    external_freshness: str | None = None          # VERIFIED_FRESH | UNVERIFIABLE | MIXED | STALE
    triangulation: str | None = None
    decision_edge: float | None = None             # the rule's own edge measure (e.g. external_edge)
    extra: dict = field(default_factory=dict)      # candidate-specific preserved fields
    # ---- later truth (attachments)
    first_ball_confidence: str | None = None
    first_ball_lower_utc: str | None = None
    timing_class: str | None = None                # STRICT_PREGAME | POST_START | AMBIGUOUS | START_UNKNOWN
    strict_close_ts: str | None = None
    strict_close_bid: float | None = None
    strict_close_ask: float | None = None
    close_basis: str | None = None
    strict_clv_executable: float | None = None
    strict_clv_midpoint: float | None = None
    settlement_result: str | None = None           # yes | no | scalar | None (unsettled)
    settlement_value: float | None = None
    settled_at: str | None = None
    after_fee_pnl: float | None = None             # payout - ask - fee, one contract
    # ---- outcome of the frozen rule
    inclusion_result: str = EXCLUDED               # INCLUDED | EXCLUDED | UNSCORABLE
    exclusion_reasons: tuple = ()
    # ---- provenance
    source_hashes: dict = field(default_factory=dict)
    harvester_version: int = 1
    schema_version: int = EVIDENCE_SCHEMA_VERSION
    authority: str = "RESEARCH_ONLY_NO_REAL_MONEY"

    def __post_init__(self):
        if self.authority != "RESEARCH_ONLY_NO_REAL_MONEY":
            raise ValueError("authority is fixed: an evidence row cannot express a real wager")
        if self.inclusion_result not in (INCLUDED, EXCLUDED, UNSCORABLE):
            raise ValueError(f"bad inclusion_result {self.inclusion_result!r}")
        if self.inclusion_result == INCLUDED and self.exclusion_reasons:
            raise ValueError("an INCLUDED row cannot carry an exclusion reason")
        if self.inclusion_result != INCLUDED and not self.exclusion_reasons:
            raise ValueError("an excluded or unscorable row must say why")
        if self.captured_at is not None and self.inclusion_result == INCLUDED \
                and self.captured_at < self.confirmation_start:
            raise ValueError("a row observed before confirmation_start can never be INCLUDED")

    @property
    def evidence_fingerprint(self) -> str:
        return canonical_hash(asdict(self))

    def to_dict(self) -> dict:
        d = asdict(self)
        d["external_sources"] = list(self.external_sources)
        d["exclusion_reasons"] = list(self.exclusion_reasons)
        d["evidence_fingerprint"] = self.evidence_fingerprint
        return d


class EvidenceStore:
    """One hash-chained JSONL per candidate under `root`. Append-only; never rewritten."""

    def __init__(self, root: str):
        self.root = root
        os.makedirs(root, exist_ok=True)

    def path(self, candidate_id: str) -> str:
        return os.path.join(self.root, f"{candidate_id}.evidence.jsonl")

    def rows(self, candidate_id: str) -> list[dict]:
        p = self.path(candidate_id)
        if not os.path.exists(p):
            return []
        with open(p) as f:
            return [json.loads(line) for line in f if line.strip()]

    def latest(self, candidate_id: str) -> dict[str, dict]:
        """observation_id -> the newest version of its evidence row."""
        out = {}
        for r in self.rows(candidate_id):
            out[r["observation_id"]] = r
        return out

    def append_new(self, candidate_id: str, rows: list[EvidenceRow], harvest_run: str) -> int:
        """Append rows whose content fingerprint is new. Returns how many were written."""
        if not rows:
            return 0
        existing = self.rows(candidate_id)
        seen = {r["evidence_fingerprint"] for r in existing}
        prev = existing[-1]["row_hash"] if existing else "GENESIS"
        n = 0
        with open(self.path(candidate_id), "a") as f:
            for row in rows:
                if row.candidate_id != candidate_id:
                    raise ValueError(f"row for {row.candidate_id} written to {candidate_id}")
                d = row.to_dict()
                if d["evidence_fingerprint"] in seen:
                    continue
                d["harvest_run"] = harvest_run
                d["prev_hash"] = prev
                d["row_hash"] = canonical_hash({k: v for k, v in d.items() if k != "row_hash"})
                f.write(json.dumps(d, separators=(",", ":"), default=str) + "\n")
                prev = d["row_hash"]
                seen.add(d["evidence_fingerprint"])
                n += 1
        return n

    def verify_chain(self, candidate_id: str) -> list[str]:
        problems, prev = [], "GENESIS"
        for i, r in enumerate(self.rows(candidate_id)):
            if r.get("prev_hash") != prev:
                problems.append(f"{candidate_id}:{i}: prev_hash mismatch")
            if canonical_hash({k: v for k, v in r.items() if k != "row_hash"}) != r.get("row_hash"):
                problems.append(f"{candidate_id}:{i}: row modified after it was written")
            body = {k: v for k, v in r.items()
                    if k not in ("evidence_fingerprint", "harvest_run", "prev_hash", "row_hash")}
            body["external_sources"] = tuple(body.get("external_sources") or ())
            body["exclusion_reasons"] = tuple(body.get("exclusion_reasons") or ())
            try:
                if EvidenceRow(**body).evidence_fingerprint != r.get("evidence_fingerprint"):
                    problems.append(f"{candidate_id}:{i}: evidence fingerprint does not match content")
            except (TypeError, ValueError) as e:
                problems.append(f"{candidate_id}:{i}: not a valid evidence row ({e})")
            prev = r.get("row_hash")
        return problems
