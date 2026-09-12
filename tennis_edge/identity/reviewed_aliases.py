"""Human-reviewed name aliases: an allowlist, not a matcher.

The automated resolver already does everything it can do safely -- an exact normalised full-name match,
plus one guarded rule for a surname that grew (Wave 3). What remains is a residue of nickname
substitutions and married names where the only honest evidence is a person checking a governing-body
record. That evidence cannot be derived from the data we hold, so it is stored rather than guessed.

Two properties keep this file from becoming a back door:

* an entry is inert until a person sets `review_status` to ACCEPTED, and code never sets it;
* an accepted alias resolves at confidence 0.95 -- exactly the floor a shadow bet requires and no more --
  so an alias can restore board coverage without ever being the reason a decision was taken.
"""
from __future__ import annotations

import json
import os

from tennis_edge.identity.names import normalize_name

ACCEPTED = "ACCEPTED"
PENDING_REVIEW = "PENDING_REVIEW"
REJECTED = "REJECTED"
ALIAS_CONFIDENCE = 0.95

DEFAULT_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "data", "identity",
                            "reviewed_aliases.json")


def load(path: str = DEFAULT_PATH) -> dict:
    """{(tour, normalised name): entry} for ACCEPTED entries with a canonical id. Others are ignored."""
    p = os.path.abspath(path)
    if not os.path.exists(p):
        return {}
    obj = json.load(open(p))
    out = {}
    for a in obj.get("aliases") or []:
        if a.get("review_status") != ACCEPTED or not a.get("canonical_id"):
            continue
        key = (a.get("tour"), normalize_name(a.get("source_name") or ""))
        if key[1]:
            out[key] = a
    return out


def audit(path: str = DEFAULT_PATH) -> dict:
    p = os.path.abspath(path)
    if not os.path.exists(p):
        return {"file": p, "exists": False}
    obj = json.load(open(p))
    aliases = obj.get("aliases") or []
    by = {}
    for a in aliases:
        by[a.get("review_status", "?")] = by.get(a.get("review_status", "?"), 0) + 1
    return {"file": p, "exists": True, "total": len(aliases), "by_status": by,
            "accepted_in_use": len(load(path)),
            "blocked_contracts_pending": sum(a.get("blocked_contracts_when_unresolved") or 0
                                             for a in aliases if a.get("review_status") == PENDING_REVIEW)}
