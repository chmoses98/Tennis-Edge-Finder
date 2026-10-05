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
from tennis_edge.identity.reviewed_aliases import ALIAS_CONFIDENCE, load as load_reviewed_aliases

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
        self.index_by_id = {pid: rec for st in states.values() for pid, rec in st["players"].items()}
        # Human-reviewed aliases only. Nothing here is inferred; an entry is inert until a person
        # accepts it, and an accepted one resolves at 0.95 -- the floor a shadow bet requires and no
        # more, so an alias can restore coverage without ever being the reason a decision was taken.
        self.aliases = load_reviewed_aliases()
        self.cache_path = cache_path
        self.cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}

    def resolve(self, tour: str, full_name: str, competitor_id: str | None = None, today: date | None = None) -> dict:
        today = today or date.today()
        if competitor_id and competitor_id in self.cache and self.cache[competitor_id].get("tour") == tour:
            return dict(self.cache[competitor_id], source="cache")
        nm = normalize_name(full_name or "")
        hits = self.index.get(tour, {}).get(nm, [])
        if not hits:
            al = self.aliases.get((tour, nm))
            if al:
                rec = self.index_by_id.get(str(al["canonical_id"]), {})
                out = {"status": "MAPPED", "player_id": str(al["canonical_id"]),
                       "confidence": ALIAS_CONFIDENCE, "name": full_name, "tour": tour,
                       "canonical_name": rec.get("name"), "last_date": rec.get("last_date"),
                       "reason": f"human-reviewed alias: {al.get('provenance', '')[:120]}"}
                if competitor_id:
                    self.cache[competitor_id] = out
                return out
            ext = self._compound_surname(tour, nm, today) or self._given_name_transliteration(tour, nm, today)
            if ext:
                if competitor_id:
                    self.cache[competitor_id] = ext
                return ext
            cands = self.review_candidates(tour, nm)
            reason = ("no exact full-name match; alias candidates queued for human review" if cands
                      else "no exact full-name match and no player with this surname in the rating universe "
                           "(most often a player absent from every reachable results source)")
            return {"status": "UNMAPPED", "reason": reason, "player_id": None, "confidence": 0.0, "name": full_name,
                    "tour": tour, "unmapped_kind": "ALIAS_CANDIDATES" if cands else "NO_HISTORY",
                    "review_candidates": cands}
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

    # ------------------------------------------------------------------ given-name transliteration (2026-10-05)
    def _given_name_transliteration(self, tour: str, nm: str, today: date) -> dict | None:
        """One more guarded rule: the SAME given name written in another transliteration.

        Kalshi lists "Pyotr Nesterov"; the registry has "Petr Nesterov". Russian, Ukrainian and Belarusian
        given names reach the West in several spellings, and that is the whole of what this rule covers:
        the first token must belong to one curated equivalence class (`GIVEN_NAME_CLASSES`), every other
        token must match exactly, exactly one registry player may qualify across the whole class, and that
        player must have played within 18 months. It does NOT cover a different given name ("Mimi" /
        "Mingge"), a dropped middle name, or a misspelt surname -- those are only ever review candidates.
        Confidence 0.85: below the 0.95 a shadow bet requires.
        """
        toks = nm.split()
        if len(toks) < 2:
            return None
        cls = GIVEN_NAME_INDEX.get(toks[0])
        if not cls:
            return None
        idx = self.index.get(tour, {})
        hits = []
        for variant in cls:
            if variant == toks[0]:
                continue
            for pid, rec in idx.get(" ".join([variant] + toks[1:]), []):
                hits.append((pid, rec))
        if len(hits) != 1:
            return None
        pid, rec = hits[0]
        last = rec.get("last_date")
        if not last or last == "None" or date.fromisoformat(last[:10]) < today - timedelta(days=548):
            return None
        return {"status": "MAPPED", "player_id": pid, "confidence": 0.85, "name": nm, "tour": tour,
                "canonical_name": rec.get("name"), "last_date": last,
                "reason": f"given-name transliteration of {rec.get('name')!r}"}

    def review_candidates(self, tour: str, nm: str) -> list:
        """Registry players a PERSON should look at for an unmapped name. Never used to map anything.

        Kinds: DROPPED_TOKEN (the Kalshi name minus one interior token is a registry name -- a middle
        name, or one half of a double surname, which is exactly why this is not automatic), SURNAME_SPELLING
        (same given name, one surname token one edit away), SAME_SURNAME_INITIAL.
        """
        toks = nm.split()
        if len(toks) < 2:
            return []
        idx = self.index.get(tour, {})
        out = []
        if len(toks) >= 3:
            for i in range(1, len(toks) - 1):
                k = " ".join(toks[:i] + toks[i + 1:])
                for pid, rec in idx.get(k, []):
                    out.append({"kind": "DROPPED_TOKEN", "player_id": pid, "name": rec.get("name"), "last_date": rec.get("last_date")})
        first, last = toks[0], toks[-1]
        for k, hits in idx.items():
            kt = k.split()
            if len(kt) < 2 or k == nm:
                continue
            diff = [i for i in range(len(kt)) if len(kt) == len(toks) and kt[i] != toks[i]]
            if kt[0] == first and len(kt) == len(toks) and len(diff) == 1 and diff[0] > 0 and _edit1(kt[diff[0]], toks[diff[0]]):
                for pid, rec in hits:
                    out.append({"kind": "SURNAME_SPELLING", "player_id": pid, "name": rec.get("name"), "last_date": rec.get("last_date")})
            elif kt[-1] == last and kt[0][:1] == first[:1] and kt[0] != first:
                for pid, rec in hits:
                    out.append({"kind": "SAME_SURNAME_INITIAL", "player_id": pid, "name": rec.get("name"), "last_date": rec.get("last_date")})
        seen, uniq = set(), []
        for c in out:
            if c["player_id"] not in seen:
                seen.add(c["player_id"]); uniq.append(c)
        return uniq[:5]

    def save_cache(self):
        os.makedirs(os.path.dirname(self.cache_path), exist_ok=True)
        json.dump(self.cache, open(self.cache_path, "w"), indent=1, sort_keys=True)


#: Given names that are ONE name written in different transliterations (first token only). Curated, short,
#: and reviewed: adding a class is a decision about identity and belongs in review like any alias.
GIVEN_NAME_CLASSES = (
    ("pyotr", "petr", "piotr"),
    ("aleksandr", "alexander", "aleksander", "alexandr", "oleksandr"),
    ("alexey", "aleksei", "alexei", "aleksey", "oleksii", "oleksiy"),
    ("dmitry", "dmitri", "dmitrii", "dmytro"),
    ("yuri", "yury", "yuriy", "iurii"),
    ("evgeny", "evgeniy", "yevgeny", "evgenii", "ievgen", "yevgen"),
    ("andrey", "andrei", "andriy"),
    ("sergey", "sergei", "serhiy", "sergiy"),
    ("nikolay", "nikolai", "mykola"),
    ("mikhail", "mykhailo"),
    ("ilya", "ilia"),
    ("maxim", "maksim", "maksym"),
    ("vitaly", "vitaliy", "vitalii"),
    ("vladyslav", "vladislav"),
    ("timofey", "timofei"),
    ("arseny", "arseniy", "arsenii"),
    ("yulia", "iuliia", "yuliya", "julia"),
    ("anastasia", "anastasiya", "anastasiia"),
    ("daria", "darya", "dariya"),
    ("kseniya", "ksenia", "xenia", "kseniia"),
    ("natalia", "natalya", "nataliya", "nataliia"),
    ("valeria", "valeriya", "valeriia"),
    ("elizaveta", "yelizaveta"),
    ("ekaterina", "yekaterina"),
    ("aleksandra", "alexandra", "oleksandra", "aliaksandra"),
    ("tatiana", "tatyana", "tetiana"),
    ("polina", "palina"),
)
GIVEN_NAME_INDEX = {n: cls for cls in GIVEN_NAME_CLASSES for n in cls}


def _edit1(a: str, b: str) -> bool:
    """True when a and b differ by exactly one substitution, insertion or deletion."""
    if a == b or abs(len(a) - len(b)) > 1:
        return False
    if len(a) == len(b):
        return sum(x != y for x, y in zip(a, b)) == 1
    if len(a) > len(b):
        a, b = b, a
    i = 0
    while i < len(a) and a[i] == b[i]:
        i += 1
    return a[i:] == b[i + 1:]
