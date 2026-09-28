"""Descriptive prospective scorecards: strict CLV by family, the external-market board, settlement.

These are MONITORING tables. None of them is a candidate, none of them selects anything, and the
"model-directed" CLV view below uses the side the ledger row itself named when it was written -- it is a
description of the Gen-1 lane's direction, not a rule and not evidence for any frozen candidate.
"""
from __future__ import annotations

import glob
import os
from collections import Counter, defaultdict
from statistics import median

from tennis_edge.confirmation import sources as src
from tennis_edge.confirmation import stats
from tennis_edge.firstball.classify import STRICT_PREGAME, classify
from tennis_edge.ledger.close import Quote, canonical_close
from tennis_edge.ledger.clv import clv_record
from tennis_edge.pricing.fees import FeeSchedule

FAMILY_ORDER = ("MATCH_WINNER", "SET_WINNER", "EXACT_SET_SCORE", "TOTAL_GAMES", "GAME_SPREAD")
#: families whose YES contracts come in complementary pairs on one physical question (A wins / B wins)
PAIRED_FAMILIES = ("MATCH_WINNER", "SET_WINNER")


def ledger_rows(data_root: str) -> list[dict]:
    return [r for _f, _h, r in src.iter_jsonl(os.path.join(data_root, "research", "ledger", "*.jsonl"))]


def recompute_clv(ctx, rows: list[dict]) -> list[tuple[dict, object]]:
    """(ledger row, ClvRecord) for every ledger row, against the LATEST first-ball truth and the full
    capture quote timeline (market records, order books, candles). Same engine as the settle job."""
    qmap = ctx.quotes({r["ticker"] for r in rows})
    out = []
    for r in rows:
        truth = ctx.truths.get(r["match_id"])
        gen = src.iso(r["generated_at_utc"])
        tc = classify(gen, truth)
        cc = canonical_close(qmap.get(r["ticker"], []), truth)
        dq = r.get("market_quote") or {}
        entry = Quote(gen, dq.get("yes_bid"), dq.get("yes_ask"), no_bid=dq.get("no_bid"), no_ask=dq.get("no_ask"))
        rec = clv_record(prediction_id=r["prediction_id"], ticker=r["ticker"], match_id=r["match_id"],
                         family=r["family"], entry=entry, close=cc, truth=truth, timing=tc,
                         tour=r.get("tour", ""), level=r.get("level", ""),
                         model_prob=(r.get("models") or {}).get("ELO_DP_FAIR"),
                         data_quality_grade=(r.get("quality") or {}).get("grade", ""),
                         fee_schedule=FeeSchedule(fee_type=r.get("fee_type") or "quadratic"))
        out.append((r, rec))
    return out


def _family_key(r: dict) -> str:
    fam = r.get("family") or "UNKNOWN"
    if fam == "MATCH_WINNER" and (r.get("model_version") or "").startswith("doubles"):
        return "MATCH_WINNER (doubles)"
    return fam if fam in FAMILY_ORDER else f"other: {fam}"


def _cell(recs: list, clv_of=lambda rec, r: rec.clv_executable) -> dict:
    exe = [clv_of(rec, r) for r, rec in recs]
    mid = [rec.clv_midpoint for _r, rec in recs]
    ci = stats.mean_ci(exe)
    hz = [rec.seconds_entry_to_first_ball for _r, rec in recs if rec.seconds_entry_to_first_ball is not None]
    return {"n": len(recs), "mean_exec_clv": ci["mean"], "median_exec_clv": ci["median"],
            "ci95": [ci["ci_low"], ci["ci_high"]], "excludes_zero": ci["excludes_zero"],
            "share_positive": (sum(1 for x in exe if x > 0) / len(exe)) if exe else None,
            "mean_mid_clv": stats.mean_ci(mid)["mean"],
            "mean_entry_spread": (sum(rec.entry_spread for _r, rec in recs if rec.entry_spread is not None) / len(recs)) if recs else None,
            "mean_entry_fee": (sum(rec.entry_taker_fee_per_contract or 0 for _r, rec in recs) / len(recs)) if recs else None,
            "median_hours_entry_to_first_ball": (median(hz) / 3600) if hz else None}


def _physical_key(r: dict) -> tuple:
    return ((r["match_id"].split("-") + [""])[1], r["family"], r.get("set_index"), r.get("line"),
            tuple(r["exact_score"]) if r.get("exact_score") else None)


def clv_scorecard(pairs: list) -> dict:
    strict = [(r, rec) for r, rec in pairs if rec.strict]
    out = {"ledger_rows": len(pairs), "strict_rows": len(strict),
           "timing_classes": dict(Counter(rec.timing_class for _r, rec in pairs)),
           "close_basis": dict(Counter(rec.close_basis for _r, rec in pairs)),
           "views": {}}
    # A. every strict observation: both sides of every binary pair, every re-pricing of a contract
    by = defaultdict(list)
    for r, rec in strict:
        by[_family_key(r)].append((r, rec))
    out["views"]["A_all_strict_observations"] = {
        "label": "every strict row; BOTH sides of each binary pair and every re-pricing run are included, so "
                 "the mean is the average cost of crossing the spread in both directions, not a strategy",
        "by_family": {k: _cell(v) for k, v in sorted(by.items())}}
    # B. one row per physical decision: earliest strict observation of each physical question, canonical side
    first = {}
    for r, rec in sorted(strict, key=lambda x: x[0]["generated_at_utc"]):
        if r["family"] in PAIRED_FAMILIES and r.get("subject") != r.get("player_a"):
            continue                                   # keep side A only: one question, one row
        k = _physical_key(r) + ((r["ticker"],) if r["family"] not in PAIRED_FAMILIES else ())
        first.setdefault(k, (r, rec))
    by = defaultdict(list)
    for r, rec in first.values():
        by[_family_key(r)].append((r, rec))
    out["views"]["B_one_row_per_physical_decision"] = {
        "label": "earliest STRICT_PREGAME observation of each physical question; for paired families only the "
                 "side-A contract is kept, so each question counts once; a YES-at-the-ask entry",
        "by_family": {k: _cell(v) for k, v in sorted(by.items())}}

    # C. the direction the ledger row itself named (ev.best_side), on the same one-per-question rows
    def directed(rec, r):
        side = (r.get("ev") or {}).get("best_side")
        if side == "NO":
            return rec.entry_yes_bid - rec.close_yes_ask       # bought NO at 1-bid, NO bid at close = 1-ask
        return rec.clv_executable
    by = defaultdict(list)
    for r, rec in first.values():
        if (r.get("ev") or {}).get("best_side") in ("YES", "NO"):
            by[_family_key(r)].append((r, rec))
    out["views"]["C_model_directed_descriptive"] = {
        "label": "DESCRIPTIVE ONLY: the side the Gen-1 ledger row named at capture (ev.best_side), whatever its "
                 "EV; not a selection rule, not a candidate, and not evidence for any frozen claim",
        "by_family": {k: _cell(v, directed) for k, v in sorted(by.items())}}
    return out


def external_scorecard(data_root: str, since: str, w4_rows: list | None = None) -> dict:
    rows = [r for _f, _h, r in src.iter_jsonl(os.path.join(data_root, "research", "external", "dislocations", "*.jsonl"))]
    post = [r for r in rows if (r.get("generated_at") or "") >= since]

    def srcs(r):
        return {s for s, p in (r.get("external_prices") or {}).items() if p is not None}
    tri_rows = Counter(r.get("triangulation") for r in post)
    tri_contracts = defaultdict(set)
    for r in post:
        tri_contracts[r.get("triangulation")].add(r.get("kalshi_ticker"))
    scans = glob.glob(os.path.join(data_root, "research", "external", "scans", "scan_*.json"))
    compact = since[:19].replace("-", "").replace(":", "")
    out = {"since": since, "scan_passes": sum(1 for p in scans if os.path.basename(p)[5:20] >= compact),
           "dislocation_rows": len(post),
           "matched_matches": len({r.get("physical_match_id") for r in post}),
           "matched_contracts": len({r.get("kalshi_ticker") for r in post}),
           "rows_with_reference": sum(1 for r in post if r.get("external_fair") is not None),
           "three_venue_observations": sum(1 for r in post if {"bovada", "smarkets"} <= srcs(r)),
           "three_venue_contracts": len({r.get("kalshi_ticker") for r in post if {"bovada", "smarkets"} <= srcs(r)}),
           "rows_by_source_set": dict(Counter("+".join(sorted(srcs(r))) or "none" for r in post)),
           "triangulation_rows": dict(tri_rows),
           "triangulation_contracts": {k: len(v) for k, v in tri_contracts.items()},
           "scanner_decisions": dict(Counter(r.get("decision") for r in post))}
    if w4_rows is not None:
        firsts = [r for r in w4_rows if r.extra.get("first_qualifying")]
        elig = [r for r in w4_rows if r.inclusion_result == "INCLUDED"]
        out["w4_first_qualifying_observations"] = len(firsts)
        out["w4_first_qualifying_by_timing"] = dict(Counter(r.timing_class for r in firsts))
        out["w4_eligible_strict_pregame"] = len(elig)
        out["w4_strict_clv_attached"] = sum(1 for r in elig if r.strict_clv_executable is not None)
        out["w4_settled_attached"] = sum(1 for r in elig if r.settlement_value is not None)
        pnl = [r.after_fee_pnl for r in elig if r.after_fee_pnl is not None]
        out["w4_after_fee_pnl"] = stats.mean_ci(pnl)
        out["w4_after_fee_pnl_sum"] = sum(pnl) if pnl else None
    return out


def settlement_audit(data_root: str, settlements: dict, ledger: list[dict]) -> dict:
    """Is settlement ingestion working, and does the health layer see it?"""
    files = sorted(glob.glob(os.path.join(data_root, "research", "settlements", "*.jsonl")))
    seen, dup, rows = set(), 0, []
    for _f, _h, r in src.iter_jsonl(os.path.join(data_root, "research", "settlements", "*.jsonl")):
        pid = r.get("prediction_id")
        if pid in seen:
            dup += 1
            continue
        seen.add(pid)
        rows.append(r)
    by_pid = {r["prediction_id"]: r for r in rows}
    ledger_ids = {r["prediction_id"] for r in ledger}
    orphans = [r for r in rows if r["prediction_id"] not in ledger_ids]
    missing = [r for r in ledger if r["prediction_id"] not in by_pid]
    miss_has_record = [r for r in missing if r["ticker"] in settlements]
    conflicts = 0
    for r in rows:
        cap = settlements.get(r.get("ticker"))
        ex = r.get("exchange") or {}
        if cap and ex.get("result") and cap.get("result") != ex.get("result"):
            conflicts += 1
    sports_src = Counter(((r.get("sports") or {}).get("source") or "none") for r in rows)
    embedded_strict = sum(1 for r in rows if (r.get("clv") or {}).get("strict"))
    return {"ledger_rows": len(ledger), "settlement_files": len(files), "settlement_rows_unique": len(rows),
            "settlement_rows_duplicate_prediction_ids": dup,
            "ledger_rows_settled": len(ledger) - len(missing),
            "settlement_rows_not_in_ledger": len(orphans),
            "settlement_rows_not_in_ledger_sample": [(r.get("ticker"), r.get("generated_at_utc")) for r in orphans[:5]],
            "ledger_rows_without_settlement_row": len(missing),
            "of_which_exchange_has_settled": len(miss_has_record),
            "of_which_not_yet_settled_or_not_swept": len(missing) - len(miss_has_record),
            "settlement_vs_capture_result_conflicts": conflicts,
            "results": dict(Counter(((r.get("exchange") or {}).get("result") or "none") for r in rows)),
            "gradeable_binary": sum(1 for r in rows if r.get("gradeable")),
            "sports_truth_sources": dict(sports_src),
            "strict_clv_embedded_in_settlement_rows": embedded_strict,
            "note": "the settle job embeds the CLV record as computed AT SETTLEMENT TIME; first-ball truth that "
                    "arrives later updates data/research/clv/<run>.jsonl but not the embedded copy"}


# ------------------------------------------------------------------------------------------------------
# Versioned derived view: strict CLV through a SIBLING event of the same canonical physical match.
CLV_JOIN_VERSION = 1
JOIN_METHOD = "CANONICAL_PHYSICAL_MATCH"
#: two sibling truths whose earliest-possible first balls differ by more than this are a disagreement
SIBLING_TRUTH_TOLERANCE_S = 300.0


def _code_date(event_ticker: str) -> str | None:
    """'KXATPMATCH-26SEP11ZVEKHA' -> '2026-09-11' (the date is part of the exchange's own match code)."""
    import re
    from datetime import datetime as _dt
    parts = (event_ticker or "").split("-")
    m = re.match(r"^(\d{2})([A-Z]{3})(\d{2})", parts[1]) if len(parts) > 1 else None
    if not m:
        return None
    try:
        return _dt.strptime(f"20{m.group(1)}{m.group(2)}{m.group(3)}", "%Y%b%d").date().isoformat()
    except ValueError:
        return None


def physical_match_id(row: dict) -> str | None:
    """Canonical physical match identity of a ledger row: tour, discipline, BOTH canonical player ids and
    the exchange's match date. Names, event titles and dates alone are never used."""
    a, b, tour = row.get("player_a_id"), row.get("player_b_id"), row.get("tour")
    d = _code_date(row.get("match_id") or row.get("event_ticker") or "")
    if not a or not b or not tour or not d:
        return None
    disc = "doubles" if ("|" in str(a) or "|" in str(b)) else "singles"
    return f"{tour}:{disc}:{min(str(a), str(b))}:{max(str(a), str(b))}:{d}"


def _is_match_level(event_ticker: str) -> bool:
    """SERIES-CODE only. An event with a third part is a LEG of the match (set n, game n) and is refused
    as a truth source, whatever it shares with the target."""
    return len((event_ticker or "").split("-")) == 2


def sibling_join_clv(ctx, rows: list[dict], exact_pairs: list) -> dict:
    """Strict CLV for ledger rows whose own event has no A/B truth but whose canonical physical match does.

    Never rewrites the exact-join CLV history: this is a separate, versioned view with provenance on every
    row. Refused: a source that is a match leg, a different discipline or physical match, a no-play truth,
    or siblings that disagree about when the first ball could have been struck."""
    exact_strict = {r["prediction_id"] for r, rec in exact_pairs if rec.strict}
    pm_of_event, rejected = {}, Counter()
    for r in rows:
        pm = physical_match_id(r)
        if pm is None:
            continue
        prev = pm_of_event.setdefault(r["match_id"], pm)
        if prev != pm:
            pm_of_event[r["match_id"]] = "CONFLICT"
    truth_by_pm = defaultdict(list)
    for ev_id, t in ctx.truths.items():
        if not (t.strict_eligible and not t.no_play and t.lower_bound_utc is not None):
            continue
        pm = pm_of_event.get(ev_id)
        if pm is None or pm == "CONFLICT":
            continue
        if not _is_match_level(ev_id):
            rejected["source_is_a_match_leg"] += 1
            continue
        truth_by_pm[pm].append((ev_id, t))

    def own_ab(r):
        t = ctx.truths.get(r["match_id"])
        return bool(t and t.strict_eligible and not t.no_play)

    need = [r for r in rows if not own_ab(r)]
    qmap = ctx.quotes({r["ticker"] for r in need})
    out, fam = [], Counter()
    for r in need:
        pm = pm_of_event.get(r["match_id"])
        if pm in (None, "CONFLICT"):
            if pm == "CONFLICT":
                rejected["target_event_maps_to_several_physical_matches"] += 1
            continue
        srcs = [(e, t) for e, t in truth_by_pm.get(pm, []) if e != r["match_id"]]
        if not srcs:
            continue
        lows = [t.lower_bound_utc for _e, t in srcs]
        if (max(lows) - min(lows)).total_seconds() > SIBLING_TRUTH_TOLERANCE_S:
            rejected["sibling_truths_disagree"] += 1
            continue
        src_ev, truth = min(srcs, key=lambda x: x[1].lower_bound_utc)   # earliest first ball: conservative
        gen = src.iso(r["generated_at_utc"])
        tc = classify(gen, truth)
        cc = canonical_close(qmap.get(r["ticker"], []), truth)
        dq = r.get("market_quote") or {}
        entry = Quote(gen, dq.get("yes_bid"), dq.get("yes_ask"), no_bid=dq.get("no_bid"), no_ask=dq.get("no_ask"))
        rec = clv_record(prediction_id=r["prediction_id"], ticker=r["ticker"], match_id=r["match_id"],
                         family=r["family"], entry=entry, close=cc, truth=truth, timing=tc,
                         tour=r.get("tour", ""), level=r.get("level", ""),
                         model_prob=(r.get("models") or {}).get("ELO_DP_FAIR"),
                         fee_schedule=FeeSchedule(fee_type=r.get("fee_type") or "quadratic"))
        d = rec.to_dict()
        d.update(target_event_id=r["match_id"], truth_source_event_id=src_ev, physical_match_id=pm,
                 join_method=JOIN_METHOD, clv_join_version=CLV_JOIN_VERSION)
        out.append(d)
        if rec.strict:
            fam[r["family"]] += 1
    recovered = [d for d in out if d["strict"] and d["prediction_id"] not in exact_strict]
    return {"clv_join_version": CLV_JOIN_VERSION, "join_method": JOIN_METHOD,
            "strict_before": len(exact_strict), "strict_after": len(exact_strict) + len(recovered),
            "rows_given_a_sibling_truth": len(out), "rows_recovered_strict": len(recovered),
            "families_recovered": dict(fam), "rejected": dict(rejected),
            "rows": out}


def weekly_match_winner_clv(pairs: list) -> dict:
    """The one-decision-per-physical-match MATCH_WINNER baseline (view B), by fixed ISO calendar week of
    the entry. Every week is reported; nothing is pooled selectively."""
    strict = [(r, rec) for r, rec in pairs if rec.strict and r.get("family") == "MATCH_WINNER"
              and not (r.get("model_version") or "").startswith("doubles")]
    first = {}
    for r, rec in sorted(strict, key=lambda x: x[0]["generated_at_utc"]):
        if r.get("subject") != r.get("player_a"):
            continue
        first.setdefault(_physical_key(r), (r, rec))
    weeks = defaultdict(list)
    for r, rec in first.values():
        y, w, _ = src.iso(r["generated_at_utc"]).isocalendar()
        weeks[f"{y}-W{w:02d}"].append((r, rec))
    return {"baseline": _cell(list(first.values())),
            "weeks": {k: _cell(v) for k, v in sorted(weeks.items())},
            "note": "descriptive; never used to edit a candidate"}
