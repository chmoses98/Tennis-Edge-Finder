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


def _read(path: str) -> dict:
    p = os.path.abspath(path)
    return json.load(open(p)) if os.path.exists(p) else {}


def load(path: str = DEFAULT_PATH) -> dict:
    """{(tour, normalised name): entry} for ACCEPTED entries with a canonical id. Others are ignored.

    Two kinds of entry feed it: Kalshi-name aliases (`aliases`) and the NAME a reviewed foreign id uses
    (`crosswalk_aliases`, e.g. ESPN's "Zhang Shuai" for Sackmann 201533) -- the review established that this name,
    on this tour, is that player. A name claimed for two different canonical ids is dropped from both (fail closed)."""
    obj = _read(path)
    out, clash = {}, set()

    def put(key, a):
        if not key[1]:
            return
        if key in out and str(out[key]["canonical_id"]) != str(a["canonical_id"]):
            clash.add(key)
        out.setdefault(key, a)

    for a in obj.get("aliases") or []:
        if a.get("review_status") != ACCEPTED or not a.get("canonical_id"):
            continue
        put((a.get("tour"), normalize_name(a.get("source_name") or "")), a)
    for a in obj.get("crosswalk_aliases") or []:
        if a.get("review_status") != ACCEPTED or not a.get("canonical_id") or not a.get("tour"):
            continue
        put((a.get("tour"), normalize_name(a.get("foreign_name") or "")),
            {**a, "source_name": a.get("foreign_name"), "provenance": a.get("provenance") or ""})
    for k in clash:
        out.pop(k, None)
    return out


class CrosswalkAliasError(ValueError):
    """The reviewed crosswalk-alias file is internally inconsistent; nothing from it may be used."""


def load_crosswalk_aliases(path: str = DEFAULT_PATH) -> dict:
    """{(foreign system, foreign id): entry} for ACCEPTED foreign-id aliases (source-specific ids, never names).

    Raises CrosswalkAliasError when one foreign id is accepted for two canonical ids, when one canonical id is
    accepted for two foreign ids of the SAME system (that would rate one person from two id streams of one source),
    or when an accepted entry targets a minted id (an alias only ever points at an existing canonical player)."""
    obj = _read(path)
    out, seen_target = {}, {}
    for a in obj.get("crosswalk_aliases") or []:
        if a.get("review_status") != ACCEPTED:
            continue
        sysname, fid, cid = a.get("foreign_system"), str(a.get("foreign_id") or ""), str(a.get("canonical_id") or "")
        if not (sysname and fid and cid):
            raise CrosswalkAliasError(f"accepted entry missing system/id/canonical: {a}")
        if ":" in cid:
            raise CrosswalkAliasError(f"{sysname}/{fid}: canonical_id {cid} is a minted id, not an existing canonical player")
        key = (sysname, fid)
        if key in out and str(out[key]["canonical_id"]) != cid:
            raise CrosswalkAliasError(f"{key} accepted for two canonical ids")
        if a.get("tour") not in ("ATP", "WTA"):
            raise CrosswalkAliasError(f"{sysname}/{fid}: accepted entry needs tour ATP or WTA (Sackmann ids repeat across tours)")
        tk = (sysname, a["tour"], cid)
        if tk in seen_target and seen_target[tk] != fid:
            raise CrosswalkAliasError(f"{a['tour']} canonical {cid} accepted for two {sysname} ids ({seen_target[tk]}, {fid})")
        seen_target[tk] = fid
        out[key] = a
    return out


def audit(path: str = DEFAULT_PATH) -> dict:
    p = os.path.abspath(path)
    if not os.path.exists(p):
        return {"file": p, "exists": False}
    obj = json.load(open(p))
    aliases = obj.get("aliases") or []
    xw = obj.get("crosswalk_aliases") or []
    xby: dict = {}
    for a in xw:
        xby[a.get("review_status", "?")] = xby.get(a.get("review_status", "?"), 0) + 1
    by = {}
    for a in aliases:
        by[a.get("review_status", "?")] = by.get(a.get("review_status", "?"), 0) + 1
    return {"file": p, "exists": True, "total": len(aliases), "by_status": by,
            "accepted_in_use": len(load(path)),
            "crosswalk_aliases_total": len(xw), "crosswalk_aliases_by_status": xby,
            "blocked_contracts_pending": sum(a.get("blocked_contracts_when_unresolved") or 0
                                             for a in aliases if a.get("review_status") == PENDING_REVIEW)}
