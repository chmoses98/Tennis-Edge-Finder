#!/usr/bin/env python3
"""Record the 2026-10-06 alias review: per-candidate checks, the decision, and its evidence.

This script does not decide by itself. It computes the CHECKS a reviewer reads (date of birth, nationality,
governing-body id, official profile, shared matches, activity) from the collected evidence, applies the acceptance
criteria written below, and then applies the reviewer's explicit per-case notes (REVIEWER_NOTES) -- which are part
of the review record and are reproduced verbatim in the output. Every ACCEPTED pair is written to
data/identity/reviewed_aliases.json (`crosswalk_aliases`) with its evidence; nothing else is.

Acceptance criteria (all must hold):
  A1  exactly one proposed canonical id survives on the foreign id's own tour;
  A2  no conflicting evidence: dates of birth do not disagree, nationality does not disagree (unless a reviewer
      note explains a documented source error), the foreign id is not shared by two people;
  A3  identity is established by at least one DIRECT link:
        - EXACT date of birth from a foreign-side source (ESPN athlete record for that ESPN id; the ATP-site
          database record for that TML/ATP id) equal to the canonical player's date of birth, or
        - the governing-body id: the canonical player's Wikidata ATP id (P536) equals the TML (ATP-site) id, or
        - SHARED MATCHES: the same match (same opponent, same result, same week) recorded under both ids,
      AND by a second, independent line (nationality agreement, an official WTA profile with the same date of birth,
      shared matches, or a date of birth implied by the source's own per-match ages within 22 days).
Rejected: a candidate whose date of birth or nationality contradicts the foreign record with no shared match.
Ambiguous: evidence lines contradict each other, or more than one candidate survives.
Insufficient evidence: none of the A3 links is available.
"""
from __future__ import annotations

import argparse
import csv
import glob
import gzip
import io
import json
import os
import re
import sys
from datetime import date, datetime, timezone

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
sys.path.insert(0, PROJ)
from tennis_edge.identity.names import normalize_name  # noqa: E402

D = os.path.join(PROJ, "research", "projection_v2", "alias_review")
OUT_JSON = os.path.join(PROJ, "research", "projection_v2", "ALIAS_REVIEW_DECISION.json")
ALIASES = os.path.join(PROJ, "data", "identity", "reviewed_aliases.json")
REVIEWER = "Claude (AI reviewer acting for the repository owner, session 2026-10-06); evidence-based, not name-based"
REVIEWED_AT = "2026-10-06"

#: reviewer notes: a decision and its reason where the checks alone do not settle a case, or where the case was flagged
#: for extra caution in the review brief. Keyed by (foreign id, canonical id or "*").
REVIEWER_NOTES = {
    ("espn:2509", "203288"): ("ACCEPTED", "Flagged ambiguity (two Sackmann Lus). ESPN's athlete record for 2509 is 'Lu Jia-Jing', born "
                              "1989-11-18 in Liaoning, CHN. Sackmann 203288 'Jia Jing Lu' and the official WTA profile 313225 "
                              "'Jia-Jing Lu' are both born 1989-11-18 (Wikidata Q17281094 agrees); two of ESPN's matches are the "
                              "same matches Sackmann records for 203288. Note: the brief listed this as espn:2567; ESPN 2567 is "
                              "Sun Fajing (ATP) -- the Lu Jia Jing row is espn:2509."),
    ("espn:2509", "201582"): ("REJECTED", "Sackmann 201582 / WTA 313765 'Jing-Jing Lu' is born 1989-05-05 -- a different player from "
                              "ESPN 2509 (born 1989-11-18); no shared match."),
    ("espn:13444", "212044"): ("ACCEPTED", "Flagged ambiguity (three Sackmann Zhous). ESPN 13444 is an ATP (men's) record: 'Zhou Yi', born "
                               "2005-03-14, Beijing, CHN. Sackmann ATP 212044 'Yi Zhou' is born 2005-03-14, CHN, and his Challenger "
                               "career (last Tunis CH 2026-05-11) continues into ESPN's rows (RG/Wimbledon qualifying from "
                               "2026-05-19, Chengdu, China Open). Decided on date of birth + nationality + tour + career "
                               "continuity, not on the name."),
    ("espn:13444", "201609"): ("REJECTED", "201609 'Yi Miao Zhou' is a WTA player (WTA 313280, born 1991-02-07); ESPN 13444 plays ATP. "
                               "(As an ATP id, 201609 is an unrelated player.)"),
    ("espn:13444", "207528"): ("REJECTED", "207528 'Yi Zhou Liu' (ATP) is born 1998-10-14 and last played 2017; ESPN 13444 is born 2005-03-14."),
    ("espn:17802", "205957"): ("REJECTED", "Different people: ESPN 17802 'Sara Alejandra Lozano Avellaneda' is born 2011-04-02, COL; "
                               "Sackmann 205957 'Alejandra Lozano' is born 1991-06-14, MEX, last result 2010."),
    ("espn:15544", "221181"): ("AMBIGUOUS", "Contradictory evidence. ESPN 15544 'Wang Jiaqi' is born 2007-09-08; Sackmann 221181 'Jiaqi "
                               "Wang' is born 2002-03-25 -- yet two of ESPN's matches (Huzhou 2026 qualifying) are matches Sackmann "
                               "records under 221181. Either a source has the wrong date of birth or Sackmann merged two Chinese "
                               "players named Jiaqi Wang. Left fail-closed."),
    ("espn:12587", "207794"): ("ACCEPTED", "ESPN lists citizenship 'Laos' (LAO) and birthplace Montreal for 12587, which contradicts every "
                               "other source; the date of birth (2001-04-18) equals Sackmann 207794 and the ATP-site database record "
                               "for 'Younes Lalami Laaroussi' (MAR), and ESPN's one match is a match Sackmann records for 207794. "
                               "The LAO flag is treated as an ESPN data error; the identity rests on DOB + a shared match."),
    ("tml:Z363", "110774"): ("ACCEPTED", "TML Z363 carries no age or nationality and has no ATP-database record, so no date of birth "
                             "or nationality can be compared -- but 19 of its 21 matches (2013-2023) are the same matches, against the "
                             "same opponents with the same results, that Sackmann records for 110774 'Marcelo Zormann Da Silva' (BRA). "
                             "A namesake cannot produce nineteen shared matches. Name differs only by the dropped second surname."),
    ("tml:A0JF", "119643"): ("REJECTED", "Rejected as an ALIAS, not as an identity: TML carries this player twice. TML H811 'Abel "
                             "Hernandez-Aguila' already maps to Sackmann 119643 by exact name; A0JF ('Hernandez Aguila Abel', one row, "
                             "Troyes 2022, a match Sackmann already records) is a second TML id for the same man. Binding a second id of "
                             "one source to one canonical player is the duplicate identity the build refuses "
                             "(apply_reviewed_aliases: 'already bound to another tml id'). No live impact."),
    ("tml:S0H7", "208095"): ("INSUFFICIENT_EVIDENCE", "TML S0H7 has one row (Puerto Vallarta CH 2018) with no age, no nationality and "
                             "no ATP-database record; Sackmann 208095's only row is a different match (Mexico F2 2018). Nothing "
                             "links the two ids. No live impact."),
}

IOC = {"China": "CHN", "Spain": "ESP", "Germany": "GER", "Croatia": "CRO", "Colombia": "COL", "Laos": "LAO", "Morocco": "MAR"}


def _csv(p):
    return csv.DictReader(io.TextIOWrapper(gzip.open(p), encoding="utf-8", errors="replace") if p.endswith(".gz") else open(p))


def _dob(x):
    if not x:
        return None
    x = str(x).strip().lstrip("+")
    if re.match(r"^\d{4}-\d{2}-\d{2}", x):
        return x[:10]
    if re.match(r"^\d{8}$", x) and x[4:] != "0000":
        return f"{x[:4]}-{x[4:6]}-{x[6:8]}"
    return None


def _yf(d):
    if not d:
        return None
    dt = date.fromisoformat(d)
    return dt.year + (dt.timetuple().tm_yday - 1) / 365.25


def atp_database(data_root):
    hits = sorted(glob.glob(os.path.join(data_root, "sources", "*", "tml", "ATP_Database.csv*")))
    by_id, by_name = {}, {}
    if hits:
        for r in _csv(hits[-1]):
            rec = {"atp_id": r["id"], "atpname": r.get("atpname"), "player": r.get("player"), "birthdate": _dob(r.get("birthdate")),
                   "ioc": r.get("ioc"), "birthplace": r.get("birthplace"), "file": os.path.relpath(hits[-1], PROJ)}
            by_id[r["id"].upper()] = rec
            for nm in {normalize_name(r.get("atpname")), normalize_name(r.get("player"))}:
                if nm:
                    by_name.setdefault(frozenset(nm.split()), []).append(rec)
    return by_id, by_name


def live_unmapped(proj_dir):
    """{(tour, normalised name): [tickers]} for players the latest board could not map, and the run id."""
    lj = os.path.join(proj_dir, "latest.json")
    if not os.path.exists(lj):
        return {}, None
    p = json.load(open(lj))
    out = {}
    for e in p.get("excluded") or []:
        if e.get("stage") != "identity":
            continue
        tour = "WTA" if ("WTA" in e["ticker"] or "ITFW" in e["ticker"]) else "ATP"
        for part in e["reason"].split("; "):
            m = re.match(r"^(.*?): (UNMAPPED|AMBIGUOUS)", part)
            if m:
                out.setdefault((tour, normalize_name(m.group(1))), set()).add(e["ticker"])
    return {k: sorted(v) for k, v in out.items()}, p.get("run_id")


def checks_for(row, cid, tour, atp_by_id, atp_by_name):
    c = row["canonical"][cid][tour]
    s = c["sackmann"]
    fo = row["foreign"]
    ev = {"tour": tour, "canonical_name": s["name"], "sources": []}
    # ---- dates of birth
    f_dob, f_src = None, None
    if row["foreign_system"] == "espn" and fo.get("espn"):
        f_dob, f_src = fo["espn"].get("dob"), f"ESPN athlete record {fo['espn'].get('url')}"
    elif row["foreign_system"] == "tml":
        rec = atp_by_id.get(row["foreign_id"].upper())
        if rec and rec.get("birthdate"):
            f_dob, f_src = rec["birthdate"], f"ATP-site player database (TML ATP_Database.csv, id {rec['atp_id']}, name {rec['atpname']!r})"
    c_dob = s.get("dob")
    wta = c.get("wta_api") or {}
    wdd = c.get("wikidata") or {}
    canon_dobs = {x for x in [c_dob, wta.get("dob")] + list(wdd.get("dob") or []) if x}
    # the ATP-site record for the CANONICAL player (by the ATP id on its Wikidata item, else by its exact name)
    atp_rec = None
    for aid in wdd.get("atp_id") or []:
        atp_rec = atp_by_id.get(str(aid).upper()) or atp_rec
    if atp_rec is None and tour == "ATP" and s.get("name"):
        recs = atp_by_name.get(frozenset(normalize_name(s["name"]).split()), [])
        atp_rec = recs[0] if len(recs) == 1 else None
    if atp_rec and atp_rec.get("birthdate"):
        canon_dobs.add(atp_rec["birthdate"])
    implied_f = (fo.get("activity") or {}).get("birth_year_implied_by_row_ages")
    if f_dob and c_dob:
        dob = "EXACT" if f_dob == c_dob else "CONFLICT"
    elif implied_f and c_dob:
        dob = "AGE_CONSISTENT" if abs(implied_f - _yf(c_dob)) <= 0.06 else "CONFLICT"
    else:
        dob = "UNAVAILABLE"
    if len(canon_dobs) > 1:
        ev["canonical_dob_sources_disagree"] = sorted(canon_dobs)
    ev.update(foreign_dob=f_dob, foreign_dob_source=f_src, foreign_birth_year_implied_by_row_ages=implied_f,
              canonical_dob=c_dob, dob_check=dob)
    # ---- nationality
    f_nat = None
    if row["foreign_system"] == "espn" and fo.get("espn"):
        f_nat = IOC.get(fo["espn"].get("country"), fo["espn"].get("country"))
    elif row["foreign_system"] == "tml":
        rec = atp_by_id.get(row["foreign_id"].upper())
        f_nat = (rec or {}).get("ioc") or None
        if not f_nat:
            rows_ioc = (fo.get("activity") or {}).get("ioc_on_rows") or {}
            f_nat = max(rows_ioc, key=rows_ioc.get) if rows_ioc else None
    c_nat = s.get("ioc") or wta.get("country") or None
    nat = "UNAVAILABLE" if not (f_nat and c_nat) else ("MATCH" if f_nat == c_nat else "CONFLICT")
    ev.update(foreign_nationality=f_nat, canonical_nationality=c_nat, nationality_check=nat)
    # ---- governing-body id, official profile, shared matches
    gb = None
    if row["foreign_system"] == "tml" and wdd.get("atp_id"):
        gb = "MATCH" if row["foreign_id"].upper() in {str(x).upper() for x in wdd["atp_id"]} else "CONFLICT"
    ev["governing_body_id_check"] = gb or "UNAVAILABLE"
    if wdd:
        ev["wikidata"] = {k: wdd.get(k) for k in ("qid", "label", "atp_id", "wta_id", "dob")}
    if wta:
        ev["official_wta_profile"] = wta
        ev["official_wta_dob_matches"] = bool(c_dob and wta.get("dob") == c_dob)
    if atp_rec:
        ev["atp_site_record_for_canonical"] = atp_rec
    ev["shared_matches"] = c.get("shared_matches") or 0
    ev["shared_match_examples"] = (c.get("shared_match_examples") or [])[:3]
    fa, ca = fo.get("activity") or {}, c.get("activity") or {}
    ev["foreign_activity"] = {k: fa.get(k) for k in ("n_matches", "first", "last")}
    ev["canonical_activity"] = {k: ca.get(k) for k in ("n_matches", "first", "last")}
    return ev


def proposed(ev):
    direct = []
    if ev["dob_check"] == "EXACT":
        direct.append("exact date of birth")
    if ev["governing_body_id_check"] == "MATCH":
        direct.append("ATP id on the canonical player's Wikidata item equals the foreign id")
    if ev["shared_matches"] >= 1:
        direct.append(f"{ev['shared_matches']} shared match(es)")
    second = []
    if ev["nationality_check"] == "MATCH":
        second.append("nationality")
    if ev.get("official_wta_dob_matches"):
        second.append("official WTA profile date of birth")
    if ev["dob_check"] == "AGE_CONSISTENT":
        second.append("date of birth implied by per-match ages")
    conflict = [k for k in ("dob_check", "nationality_check", "governing_body_id_check") if ev[k] == "CONFLICT"]
    if conflict:
        if ev["shared_matches"] >= 1:
            return "AMBIGUOUS", f"conflicting evidence ({', '.join(conflict)}) despite {ev['shared_matches']} shared match(es)"
        return "REJECTED", f"contradicted by {', '.join(conflict)} and no shared match"
    if direct and (second or len(direct) >= 2):
        return "ACCEPTED", "; ".join(direct + second)
    if not direct and ev["dob_check"] == "AGE_CONSISTENT" and ev["nationality_check"] == "MATCH":
        return "ACCEPTED", "date of birth implied by the source's per-match ages agrees within 22 days; nationality"
    return "INSUFFICIENT_EVIDENCE", "no direct link (no exact date of birth, governing-body id or shared match) on both sides"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--data-root", default=os.path.join(PROJ, "data"))
    ap.add_argument("--projections", default=None, help="projections dir of the board used for live impact")
    ap.add_argument("--write-aliases", action="store_true")
    a = ap.parse_args()
    summ = json.load(open(os.path.join(D, "evidence_summary.json")))
    cands = json.load(open(os.path.join(D, "candidates.json")))
    order = [(c["foreign_system"], c["foreign_id"]) for c in cands["candidates"] + cands.get("kalshi_names", [])]
    by_key = {(r["foreign_system"], r["foreign_id"]): r for r in summ}
    atp_by_id, atp_by_name = atp_database(a.data_root)
    live, board_run = live_unmapped(a.projections or os.path.join(a.data_root, "research", "projections"))
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")
    decisions = []
    for key in order:
        r = by_key[key]
        nkey = "tml:" + r["foreign_id"] if r["foreign_system"] == "tml" else r["foreign_id"]
        for cid in r["canonical"]:
            for tour in r["canonical"][cid]:
                if r["foreign_system"] == "kalshi":
                    continue
                ev = checks_for(r, cid, tour, atp_by_id, atp_by_name)
                dec, why = proposed(ev)
                note = REVIEWER_NOTES.get((nkey, cid))
                if note:
                    dec, why = note[0], note[1]
                lk = (tour, normalize_name(r["foreign_name"]))
                decisions.append({
                    "foreign_system": r["foreign_system"], "foreign_id": r["foreign_id"], "foreign_name": r["foreign_name"],
                    "tour": tour, "proposed_canonical_id": cid, "proposed_canonical_name": ev["canonical_name"],
                    "decision": dec, "rationale": why, "reviewer_note": bool(note),
                    "evidence": ev, "raw_evidence_file": r["raw_file"],
                    "evidence_sources": sorted({x for x in [ev.get("foreign_dob_source"),
                                                            "Sackmann players file (dob, ioc, wikidata id)",
                                                            "official WTA API" if ev.get("official_wta_profile") else None,
                                                            f"Wikidata {ev['wikidata']['qid']}" if ev.get("wikidata") else None,
                                                            "ATP-site player database (TML)" if ev.get("atp_site_record_for_canonical") else None,
                                                            "shared matches in the canonical table (TML/ESPN vs Sackmann)" if ev["shared_matches"] else None]
                                                if x}),
                    "reviewer": REVIEWER, "reviewed_at": now,
                    "changes_live_coverage": lk in live, "live_tickers_naming_this_player": len(live.get(lk, [])),
                })
    # A1: within one foreign id, two ACCEPTED candidates = ambiguous for all of them
    from collections import defaultdict
    acc = defaultdict(list)
    for d in decisions:
        if d["decision"] == "ACCEPTED":
            acc[(d["foreign_system"], d["foreign_id"])].append(d)
    for k, ds in acc.items():
        if len(ds) > 1:
            for d in ds:
                d["decision"], d["rationale"] = "AMBIGUOUS", "more than one candidate passed: " + d["rationale"]
    # Kalshi-name entries (no foreign id: only who officially carries the name can be checked)
    kalshi = []
    for key in order:
        r = by_key[key]
        if r["foreign_system"] != "kalshi":
            continue
        kalshi.append(kalshi_decision(r, now))
    per_foreign = {}
    for d in decisions:
        per_foreign.setdefault((d["foreign_system"], d["foreign_id"]), []).append(d["decision"])
    outcome = {}
    for k, v in per_foreign.items():
        outcome[k] = ("ACCEPTED" if "ACCEPTED" in v else "AMBIGUOUS" if "AMBIGUOUS" in v
                      else "INSUFFICIENT_EVIDENCE" if "INSUFFICIENT_EVIDENCE" in v else "REJECTED")
    tally = {s: sum(1 for x in outcome.values() if x == s) for s in ("ACCEPTED", "REJECTED", "AMBIGUOUS", "INSUFFICIENT_EVIDENCE")}
    doc = {"review": "mint-twin alias review (research/projection_v2/ALIAS_REVIEW_MINT_TWINS.md) + Kalshi-name queue",
           "reviewed_at": now, "reviewer": REVIEWER, "criteria": __doc__.split("Acceptance criteria")[1].strip(),
           "board_used_for_live_impact": board_run,
           "foreign_ids_reviewed": len(outcome), "foreign_id_outcomes": tally,
           "pairs_reviewed": len(decisions),
           "pair_decisions": {s: sum(1 for d in decisions if d["decision"] == s) for s in ("ACCEPTED", "REJECTED", "AMBIGUOUS", "INSUFFICIENT_EVIDENCE")},
           "decisions": decisions, "kalshi_name_decisions": kalshi}
    json.dump(doc, open(OUT_JSON, "w"), indent=1, default=str)
    print(json.dumps({k: doc[k] for k in ("foreign_ids_reviewed", "foreign_id_outcomes", "pair_decisions")}))
    if a.write_aliases:
        write_aliases(decisions, kalshi)
    return 0


KALSHI_NOTES = {
    "Mimi Xu": None,   # decided from evidence below
    "Bella Bergqvist Larsson": ("INSUFFICIENT_EVIDENCE", "The registry's Bella Bergkvist Larsson (SWE, born 2006-03-09) is confirmed by the "
                                "official WTA profile 331422 under the spelling 'Bergkvist'. Kalshi spells it 'Bergqvist' and exposes no "
                                "date of birth or id, and the registry also holds a different Swede, Wilma Bergqvist. Very probably the same "
                                "player, but nothing on Kalshi's side identifies her: left PENDING."),
}


def kalshi_decision(r, now):
    name = r["foreign_name"]
    tour = r["tours"][0] if r["tours"] else None
    out = {"foreign_system": "kalshi", "kalshi_name": name, "tour": tour, "reviewer": REVIEWER, "reviewed_at": now,
           "raw_evidence_file": r["raw_file"], "candidates": []}
    for cid, pt in r["canonical"].items():
        c = pt.get(tour) or {}
        s = c.get("sackmann") or {}
        out["candidates"].append({"canonical_id": cid, "canonical_name": s.get("name"), "dob": s.get("dob"), "ioc": s.get("ioc"),
                                  "official_wta_profile": c.get("wta_api"), "last_result": (c.get("activity") or {}).get("last")})
    note = KALSHI_NOTES.get(name)
    if note:
        out["decision"], out["rationale"] = note
        return out
    if name == "Mimi Xu":
        hits = [p for p in ((r["foreign"].get("wikidata_search") or {}).get("players") or []) if p]
        wta = r["foreign"].get("wta_api") or {}
        cand = out["candidates"][0]
        same = [p for p in hits if cand["dob"] and cand["dob"] in (p.get("dob") or [])]
        if wta and normalize_name(wta.get("name")) == "mimi xu" and wta.get("dob") == cand["dob"] and len(same) == 1:
            out["decision"] = "ACCEPTED"
            out["rationale"] = (f"The official WTA profile {wta.get('wta_id')} is named {wta.get('name')!r}, born {wta.get('dob')}, "
                                f"{wta.get('country')} -- the date of birth and nationality of the registry's Mingge Xu (259685, "
                                f"{cand['dob']}, {cand['ioc']}); Wikidata {same[0].get('qid')} carries the same date of birth.")
        elif same and len(same) == 1:
            out["decision"] = "ACCEPTED" if (same[0].get("wta_id") and cand["dob"]) else "INSUFFICIENT_EVIDENCE"
            out["rationale"] = (f"Wikidata {same[0].get('qid')} ({same[0].get('label')!r}, aliases {same[0].get('aliases')}) is the "
                                f"tennis player found for 'Mimi Xu', born {cand['dob']} like the registry's Mingge Xu (259685, {cand['ioc']}), "
                                f"WTA id {same[0].get('wta_id')}.")
        else:
            out["decision"] = "INSUFFICIENT_EVIDENCE"
            out["rationale"] = ("No governing-body record reachable from this review ties the name 'Mimi Xu' to the registry's "
                                "Mingge Xu (259685, GBR, born 2007-10-02): the official WTA lookup and Wikidata search returned no "
                                "player record for 'Mimi Xu'. Left PENDING_REVIEW, as instructed.")
        out["evidence"] = {"wikidata_search": r["foreign"].get("wikidata_search"), "official_wta_profile_for_name": wta}
        return out
    # the remaining queue names: every candidate has a different given name and, mostly, a career decades apart
    out["decision"] = "REJECTED"
    out["rationale"] = ("Every candidate is a different person: a different given name (" +
                        ", ".join(f"{x['canonical_name']} b.{(x['dob'] or '?')[:4]} {x['ioc'] or ''}".strip() for x in out["candidates"]) +
                        "). The Kalshi name stays unmapped (no history), which is correct.")
    return out


def write_aliases(decisions, kalshi):
    obj = json.load(open(ALIASES))
    obj["schema_version"] = 2
    rules = obj.setdefault("rules", [])
    extra = ("crosswalk_aliases bind a SOURCE-SPECIFIC foreign id (ESPN / TML) to an existing canonical (Sackmann) id on one "
             "tour. They are applied by the canonical build (identity/crosswalk.apply_reviewed_aliases) only where the automated "
             "crosswalk left the id unmapped, and never overwrite a mapped or minted id. Only ACCEPTED entries are listed; every "
             "other decision is in research/projection_v2/ALIAS_REVIEW_DECISION.json.")
    if extra not in rules:
        rules.append(extra)
    # this review created the section; it is regenerated from the decision record so a reversed decision cannot linger
    have = set()
    xs = obj["crosswalk_aliases"] = []
    for d in decisions:
        if d["decision"] != "ACCEPTED" or (d["foreign_system"], d["foreign_id"]) in have:
            continue
        ev = d["evidence"]
        xs.append({"foreign_system": d["foreign_system"], "foreign_id": d["foreign_id"], "foreign_name": d["foreign_name"],
                   "tour": d["tour"], "canonical_id": d["proposed_canonical_id"],
                   "canonical_name": normalize_name(d["proposed_canonical_name"]), "review_status": "ACCEPTED",
                   "evidence": {"dob_check": ev["dob_check"], "foreign_dob": ev.get("foreign_dob"), "canonical_dob": ev.get("canonical_dob"),
                                "nationality": [ev.get("foreign_nationality"), ev.get("canonical_nationality")],
                                "governing_body_id_check": ev["governing_body_id_check"], "shared_matches": ev["shared_matches"],
                                "official_wta_profile": (ev.get("official_wta_profile") or {}).get("url"),
                                "wikidata": (ev.get("wikidata") or {}).get("qid"), "sources": d["evidence_sources"],
                                "raw": d["raw_evidence_file"]},
                   "provenance": d["rationale"], "decision_ref": "research/projection_v2/ALIAS_REVIEW_DECISION.json",
                   "reviewer": d["reviewer"], "reviewed_at": REVIEWED_AT})
    for k in kalshi:
        if k["kalshi_name"] == "Mimi Xu":
            for a_ in obj["aliases"]:
                if a_.get("source_name") == "Mimi Xu":
                    a_["review_history"] = [h for h in a_.get("review_history") or [] if h.get("reviewed_at") != REVIEWED_AT]
                    a_["review_history"].append({"reviewed_at": REVIEWED_AT, "reviewer": k["reviewer"],
                                                                "decision": k["decision"], "rationale": k["rationale"]})
                    if k["decision"] == "ACCEPTED":
                        a_["review_status"] = "ACCEPTED"
                        a_["canonical_id"] = "259685"
                        a_["provenance"] = a_["provenance"] + " | 2026-10-06 review: " + k["rationale"]
    json.dump(obj, open(ALIASES, "w"), indent=2)
    print(f"crosswalk_aliases: {len(xs)}")


if __name__ == "__main__":
    sys.exit(main())
