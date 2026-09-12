"""Map Kalshi competitor names (full names in rules_primary, plus the exchange's competitor UUID) to canonical
player ids. Exact-normalised full-name match against the registry of a tour; ambiguous or absent -> UNMAPPED
(fail closed). Successful mappings are cached by competitor UUID in config/kalshi_competitor_map.json so a
player is resolved once and the cache is reviewable.

Confidence: 1.0 for a unique exact normalised full-name hit that also played in the last 24 months;
0.9 for a unique exact hit with no recent activity (could be a namesake); 0.0 otherwise.
"""
from __future__ import annotations

import json
import os
from datetime import date, timedelta

from tennis_edge.identity.names import normalize_name

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
CACHE = os.path.join(PROJ, "config", "kalshi_competitor_map.json")


class KalshiPlayerMapper:
    def __init__(self, states: dict, cache_path: str = CACHE):
        """states: {'ATP': ratings_state, 'WTA': ratings_state} (tennis_edge.models.state artifacts)."""
        self.index = {}
        for tour, st in states.items():
            idx = {}
            for pid, rec in st["players"].items():
                nm = normalize_name(rec.get("name") or "")
                if nm:
                    idx.setdefault(nm, []).append((pid, rec))
            self.index[tour] = idx
        self.cache_path = cache_path
        self.cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}

    def resolve(self, tour: str, full_name: str, competitor_id: str | None = None, today: date | None = None) -> dict:
        today = today or date.today()
        if competitor_id and competitor_id in self.cache and self.cache[competitor_id].get("tour") == tour:
            return dict(self.cache[competitor_id], source="cache")
        nm = normalize_name(full_name or "")
        hits = self.index.get(tour, {}).get(nm, [])
        if not hits:
            ext = self._compound_surname(tour, nm, today)
            if ext:
                if competitor_id:
                    self.cache[competitor_id] = ext
                return ext
            return {"status": "UNMAPPED", "reason": "no exact full-name match", "player_id": None, "confidence": 0.0, "name": full_name, "tour": tour}
        if len(hits) > 1:
            # prefer the single recently-active namesake; otherwise ambiguous
            recent = [(pid, r) for pid, r in hits if r.get("last_date") and r["last_date"] != "None" and date.fromisoformat(r["last_date"][:10]) >= today - timedelta(days=730)]
            if len(recent) != 1:
                return {"status": "AMBIGUOUS", "reason": f"{len(hits)} namesakes, {len(recent)} recently active", "player_id": None, "confidence": 0.0, "name": full_name, "tour": tour,
                        "candidates": [pid for pid, _ in hits]}
            hits = recent
        pid, rec = hits[0]
        active = rec.get("last_date") and rec["last_date"] != "None" and date.fromisoformat(rec["last_date"][:10]) >= today - timedelta(days=730)
        out = {"status": "MAPPED", "player_id": pid, "confidence": 1.0 if active else 0.9, "name": full_name, "tour": tour, "canonical_name": rec.get("name"), "last_date": rec.get("last_date")}
        if competitor_id:
            self.cache[competitor_id] = out
        return out

    def _compound_surname(self, tour: str, nm: str, today: date) -> dict | None:
        """One guarded alias rule: a surname that GREW.

        Kalshi lists "Nicole Melichar-Martinez"; the registry, built on older results, has "Nicole
        Melichar". A married or compound surname appends tokens to the end and changes nothing else, so
        a candidate whose leading tokens exactly reproduce a registry player and which only ADDS trailing
        tokens is that player -- provided exactly one registry player qualifies and nobody else is a
        near-neighbour of the candidate.

        Deliberately NOT covered: a substituted given name. Kalshi's "Mimi Xu" is very probably the
        registry's "Mingge Xu", and this rule will not touch it, because "very probably" is how two
        different players become one rating entity. Matches here are confidence 0.9, below the 0.95 a
        shadow bet requires: they restore board coverage without ever driving a decision.
        """
        toks = nm.split()
        if len(toks) < 3:                       # "first last-extra" needs at least three tokens
            return None
        idx = self.index.get(tour, {})
        cands = []
        for k, hits in idx.items():
            kt = k.split()
            if len(kt) >= 2 and len(kt) < len(toks) and toks[:len(kt)] == kt and len(hits) == 1:
                cands.append((k, hits[0]))
        if len(cands) != 1:
            return None
        key, (pid, rec) = cands[0]
        last = rec.get("last_date")
        if not last or last == "None" or date.fromisoformat(last[:10]) < today - timedelta(days=730):
            return None                          # an inactive namesake root is not evidence
        return {"status": "MAPPED", "player_id": pid, "confidence": 0.9, "name": nm, "tour": tour,
                "canonical_name": rec.get("name"), "last_date": last,
                "reason": f"compound-surname alias of {rec.get('name')!r}"}

    def save_cache(self):
        os.makedirs(os.path.dirname(self.cache_path), exist_ok=True)
        json.dump(self.cache, open(self.cache_path, "w"), indent=1, sort_keys=True)
