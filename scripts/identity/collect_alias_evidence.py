#!/usr/bin/env python3
"""Fetch the EXTERNAL evidence a person needs to review a player-alias candidate. Decides nothing.

Runs on a GitHub runner (the research sandbox cannot reach ESPN, Wikidata or the tours). For every candidate in
`research/projection_v2/alias_review/candidates.json` it records, verbatim and timestamped:

* the source-specific profile of the FOREIGN id
    - ESPN ids: ESPN's athlete record for exactly that id (name, date of birth, citizenship);
    - TML ids: these ARE ATP-site player ids, so the ATP's own profile for that id, and every Wikidata item that
      carries that ATP id (property P536);
* for every proposed CANONICAL (Sackmann) id: the Wikidata item Sackmann's own players file links it to, with that
  item's governing-body identifiers (ATP P536, WTA P597, ITF P8618), date of birth and sporting nationality, and
  the WTA / ATP / ITF profile those identifiers point to when the tour answers.

Every request's URL, HTTP status and body (or error) is kept in `evidence_raw/<key>.json`, so the review can be
re-read without trusting this script's summary. Nothing here maps a player: acceptance is a human decision recorded
in data/identity/reviewed_aliases.json with this evidence as provenance.
"""
from __future__ import annotations

import argparse
import csv
import glob
import gzip
import io
import json
import os
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(PROJ, "research", "projection_v2", "alias_review")
UA = "tennis-edge-finder identity review (research; contact via GitHub repo)"


def get(url: str, accept: str = "application/json", timeout: int = 25) -> dict:
    """GET with polite pacing; HTTP 429 is retried with backoff (Wikidata rate-limits shared runner IPs)."""
    for attempt in range(5):
        rec = _get_once(url, accept, timeout)
        if rec.get("status") != 429:
            return rec
        time.sleep(15 * (attempt + 1))
    return rec


def _get_once(url: str, accept: str, timeout: int) -> dict:
    rec = {"url": url, "fetched_at": datetime.now(timezone.utc).isoformat()}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": accept})
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read()
            rec["status"] = r.status
            txt = body.decode("utf-8", "replace")
            try:
                rec["json"] = json.loads(txt)
            except ValueError:
                rec["text"] = txt[:20000]
    except urllib.error.HTTPError as e:
        rec["status"] = e.code
        rec["error"] = str(e)[:300]
    except Exception as e:  # noqa: BLE001 -- recorded, never fatal
        rec["status"] = None
        rec["error"] = f"{type(e).__name__}: {e}"[:300]
    time.sleep(1.0 if "wikidata" in url else 0.4)
    return rec


def _open(p):
    return io.TextIOWrapper(gzip.open(p), encoding="utf-8", errors="replace") if p.endswith(".gz") else open(p, encoding="utf-8", errors="replace")


def sackmann_players(data_root: str) -> dict:
    """{(tour, player_id): row} from the newest Sackmann atp/wta players files (dob, ioc, wikidata_id).

    Keyed by TOUR: Sackmann ATP and WTA ids share one numeric range (212044 is an ATP man and a WTA woman)."""
    out = {}
    for tour in ("atp", "wta"):
        hits = sorted(glob.glob(os.path.join(data_root, "sources", "*", "sackmann", f"tennis_{tour}", f"{tour}_players.csv*")))
        if not hits:
            continue
        for r in csv.DictReader(_open(hits[-1])):
            r["_tour"] = tour.upper()
            r["_file"] = os.path.relpath(hits[-1], PROJ)
            out[(tour.upper(), str(r.get("player_id")))] = r
    return out


WD_PROPS = {"P536": "atp_id", "P597": "wta_id", "P8618": "itf_id", "P569": "date_of_birth", "P27": "citizenship",
            "P1532": "country_for_sport", "P735": "given_name", "P734": "family_name"}


def wikidata_summary(entity: dict) -> dict:
    claims = entity.get("claims") or {}
    out = {"qid": entity.get("id"), "label_en": ((entity.get("labels") or {}).get("en") or {}).get("value"),
           "label_zh": ((entity.get("labels") or {}).get("zh") or {}).get("value"),
           "aliases_en": [a.get("value") for a in (entity.get("aliases") or {}).get("en") or []]}
    for p, name in WD_PROPS.items():
        vals = []
        for c in claims.get(p) or []:
            v = ((c.get("mainsnak") or {}).get("datavalue") or {}).get("value")
            if isinstance(v, dict):
                v = v.get("time") or v.get("id") or v
            vals.append(v)
        if vals:
            out[name] = vals
    return out


def wikidata_entity(qid: str) -> dict:
    rec = get(f"https://www.wikidata.org/wiki/Special:EntityData/{qid}.json")
    ent = ((rec.get("json") or {}).get("entities") or {}).get(qid)
    if ent:
        rec["summary"] = wikidata_summary(ent)
        rec.pop("json", None)           # the summary keeps every field the review reads; the raw entity is huge
    return rec


def wikidata_items_by_atp_id(ids: list) -> dict:
    """ONE SPARQL query for every ATP id (P536, matched case-insensitively), retried on 429. {ATP id upper: [qid]}."""
    vals = " ".join(f'"{i.lower()}" "{i.upper()}"' for i in ids)
    q = f"SELECT ?item ?atp WHERE {{ VALUES ?atp {{ {vals} }} ?item wdt:P536 ?atp . }}"
    rec = {}
    for attempt in range(6):
        rec = get("https://query.wikidata.org/sparql?format=json&query=" + urllib.parse.quote(q),
                  accept="application/sparql-results+json", timeout=60)
        if rec.get("status") == 200:
            break
        time.sleep(10 * (attempt + 1))
    out: dict = {}
    for b in ((rec.get("json") or {}).get("results") or {}).get("bindings") or []:
        out.setdefault(b["atp"]["value"].upper(), []).append(b["item"]["value"].rsplit("/", 1)[-1])
    rec.pop("json", None)
    return {"request": rec, "items": out}


def wikidata_search(name: str, limit: int = 4) -> dict:
    """wbsearchentities for a name, then the entity summary of each hit that is a tennis player (has ATP/WTA/ITF id)."""
    rec = get("https://www.wikidata.org/w/api.php?action=wbsearchentities&format=json&language=en&type=item&limit=10&search="
              + urllib.parse.quote(name))
    hits = [h.get("id") for h in ((rec.get("json") or {}).get("search") or [])][:limit]
    rec.pop("json", None)
    rec["hits"] = hits
    rec["players"] = []
    for q in hits:
        ent = wikidata_entity(q)
        s = ent.get("summary") or {}
        if s.get("atp_id") or s.get("wta_id") or s.get("itf_id"):
            rec["players"].append(ent)
    return rec


def espn_athlete(eid: str) -> list:
    n = eid.split(":", 1)[-1]
    return [get(f"https://sports.core.api.espn.com/v2/sports/tennis/athletes/{n}"),
            get(f"https://site.web.api.espn.com/apis/common/v3/sports/tennis/athletes/{n}")]


def tour_profiles(wd: dict) -> list:
    s = wd.get("summary") or {}
    recs = []
    for atp in s.get("atp_id") or []:
        recs.append(get(f"https://www.atptour.com/en/-/www/players/hero/{str(atp).lower()}?v=1"))
    for wta in s.get("wta_id") or []:
        recs.append(get(f"https://api.wtatennis.com/tennis/players/{wta}"))
        recs.append(get(f"https://www.wtatennis.com/players/{wta}/x", accept="text/html"))
    for itf in s.get("itf_id") or []:
        num = [p for p in str(itf).split("/") if p.isdigit()]
        if num:
            recs.append(get(f"https://www.itftennis.com/tennis/api/PlayerApi/GetPlayerHero?playerId={num[0]}"))
    return recs


def canonical_evidence(cid: str, players: dict, wd_cache: dict, search_name: str | None) -> dict:
    ce = {}
    for tour in ("ATP", "WTA"):
        prow = players.get((tour, cid))
        if not prow:
            continue
        te = {"sackmann_players_row": prow}
        qid = prow.get("wikidata_id") or ""
        if qid.startswith("Q"):
            if qid not in wd_cache:
                wd_cache[qid] = wikidata_entity(qid)
            te["wikidata"] = wd_cache[qid]
            te["tour_profiles"] = tour_profiles(wd_cache[qid])
        else:
            nm = f"{prow.get('name_first', '')} {prow.get('name_last', '')}".strip()
            te["wikidata_search"] = wikidata_search(nm)
            te["tour_profiles"] = [p for ent in te["wikidata_search"]["players"] for p in tour_profiles(ent)]
        ce[tour] = te
    return ce


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--candidates", default=os.path.join(OUT, "candidates.json"))
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--out", default=os.path.join(OUT, "evidence_raw"))
    ap.add_argument("--only", nargs="*", default=None, help="foreign ids to (re)fetch")
    ap.add_argument("--only-file", default=os.path.join(OUT, "REQUEST_ONLY"),
                    help="if this file exists, (re)fetch only the foreign ids it lists, one per line")
    a = ap.parse_args()
    if a.only is None and a.only_file and os.path.exists(a.only_file):
        a.only = [x.strip() for x in open(a.only_file) if x.strip() and not x.startswith("#")]
    os.makedirs(a.out, exist_ok=True)
    doc = json.load(open(a.candidates))
    cands = doc["candidates"] + (doc.get("kalshi_names") or [])
    players = sackmann_players(a.data_root)
    print(f"sackmann players rows: {len(players)}")
    tml_ids = [c["foreign_id"] for c in cands if c["foreign_system"] == "tml" and (not a.only or c["foreign_id"] in a.only)]
    atp_items = wikidata_items_by_atp_id(tml_ids) if tml_ids else {"items": {}}
    json.dump(atp_items, open(os.path.join(a.out, "_wikidata_items_by_tml_atp_id.json"), "w"), indent=1, default=str)
    wd_cache: dict = {}
    for c in cands:
        if a.only and c["foreign_id"] not in a.only:
            continue
        ev = {"foreign_system": c["foreign_system"], "foreign_id": c["foreign_id"], "foreign_name": c["foreign_name"],
              "collected_at": datetime.now(timezone.utc).isoformat(), "foreign": {}, "canonical": {}}
        if c["foreign_system"] == "espn":
            ev["foreign"]["espn_athlete"] = espn_athlete(c["foreign_id"])
            nm = ((ev["foreign"]["espn_athlete"][0].get("json") or {}).get("fullName")) or c["foreign_name"]
            ev["foreign"]["wikidata_search"] = wikidata_search(nm)
        elif c["foreign_system"] == "tml":
            fid = c["foreign_id"]
            ev["foreign"]["atp_profile"] = [get(f"https://www.atptour.com/en/-/www/players/hero/{fid.lower()}?v=1")]
            items = atp_items["items"].get(fid.upper(), [])
            ev["foreign"]["wikidata_items_with_this_atp_id"] = items
            ev["foreign"]["wikidata_entities"] = [wd_cache.setdefault(q, wikidata_entity(q)) for q in items]
        elif c["foreign_system"] == "kalshi":
            # a Kalshi competitor has no public profile id: what can be checked is who carries this NAME officially
            ev["foreign"]["wikidata_search"] = wikidata_search(c["foreign_name"])
            ev["foreign"]["tour_profiles"] = [p for ent in ev["foreign"]["wikidata_search"]["players"] for p in tour_profiles(ent)]
        for cand in c.get("candidates") or []:
            ev["canonical"][cand["canonical_id"]] = canonical_evidence(cand["canonical_id"], players, wd_cache, None)
        key = f"{c['foreign_system']}_{c['foreign_id'].replace(':', '_').replace(' ', '_')}"
        json.dump(ev, open(os.path.join(a.out, f"{key}.json"), "w"), indent=1, default=str)
        print(key, "ok")
    return 0


if __name__ == "__main__":
    sys.exit(main())
