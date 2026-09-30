"""The assisted slate: one handicapping packet per open, not-started match.

It JOINS what the repository already produces -- it computes no new probability and selects nothing:

  Kalshi capture          every open match-scope market of the match: bid/ask/size/spread/fee/age
  Gen-1 ledger            run_tennis.py prediction ledger (ELO_DP_FAIR, Elo, structural; ratings inputs,
                          data-quality pillars incl. recency/experience)
  shadow board companion  frozen fair_v1 / Gen-2 / Gen-1 Elo, the perturbation envelope, serve evidence,
                          selector_v1 decision and qualification
  Model 4 board           frozen market_conditioned_v1 + fundamental Gen-2 on listed derivatives
  external_v1 scan        Bovada / Smarkets de-vigged prices, consensus, triangulation, venue freshness
  first-ball store        matches already seen under way are left off the slate

Every model number is the frozen producer's own output at its own prediction time (carried with that
time); nothing here re-prices, re-fits or re-orients a model.
"""
from __future__ import annotations

import glob
import gzip
import json
import os
from datetime import datetime, timezone

from tennis_edge.kalshi.families import FAMILIES, SERIES
from tennis_edge.kalshi.markets import parse_market
from tennis_edge.pricing.competition import classify_competition
from tennis_edge.pricing.fees import taker_fee

from . import AUTONOMOUS_REAL_MONEY_AUTHORITY, CHATGPT_ASSISTED_TRACK, ASSISTED_AUTHORITY
from .market import capture_days, first_ball_bound, fnum, iso, load_truths, truth_for
from .schema import (ASSISTED_SCHEMA_VERSION, expression_of_family, level_bucket, match_code_of, preferred_side,
                     series_of, side_edges, surface_bucket)
from .store import canonical_hash

SLATE_VERSION = "assisted_slate_v1"
STALE_QUOTE_S = 30 * 60
STALE_EXTERNAL_S = 30 * 60
WIDE_SPREAD = 0.06
THIN_SIZE = 10.0
STALE_MODEL_H = 13.0
DROP_PAST_SCHEDULED_H = 24.0
#: first-ball truth sources exist for these levels only (README: ATP/WTA main tour and the Slams)
FIRST_BALL_COVERED = ("ATP", "WTA")

MATCH_SCOPE_SERIES = {s for s, (fam, _t, _l, _d) in SERIES.items()
                      if FAMILIES.get(fam, {}).get("scope") == "MATCH" and expression_of_family(fam)}


# ---------------------------------------------------------------------------------------------- loading
def open_board(capture_root: str) -> tuple[dict[str, dict], dict]:
    """ticker -> current record: the latest FULL capture snapshot, then every CHANGED pass after it."""
    days = capture_days(capture_root)[-2:]
    files = []
    for d in days:
        files += sorted(glob.glob(os.path.join(capture_root, d, "*.quotes.jsonl.gz")))
    start = 0
    for i in range(len(files) - 1, -1, -1):
        try:
            with gzip.open(files[i], "rt") as fh:
                first = fh.readline()
            if first.strip() and json.loads(first).get("snapshot_kind") == "full":
                start = i
                break
        except (OSError, EOFError, ValueError):
            continue
    out: dict[str, dict] = {}
    for f in files[start:]:
        try:
            with gzip.open(f, "rt") as fh:
                for line in fh:
                    if not line.strip():
                        continue
                    try:
                        r = json.loads(line)
                    except ValueError:
                        continue
                    if r.get("ticker"):
                        out[r["ticker"]] = r
        except (OSError, EOFError):
            continue
    meta = {"capture_files_read": len(files) - start,
            "base_full_snapshot": os.path.basename(files[start]) if files else None,
            "last_capture_file": os.path.basename(files[-1]) if files else None}
    return out, meta


def _latest_rows(root: str, *, ts_key: str, key: str = "ticker", days: int = 2) -> dict[str, dict]:
    """key -> most recent row across the last `days` daily JSONL files of a producer store."""
    files = sorted(glob.glob(os.path.join(root, "*.jsonl")))[-days:]
    out: dict[str, dict] = {}
    for f in files:
        with open(f) as fh:
            for line in fh:
                if not line.strip():
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                k = r.get(key)
                if k and (k not in out or (out[k].get(ts_key) or "") <= (r.get(ts_key) or "")):
                    out[k] = r
    return out


def _latest_dislocations(root: str, tickers: set[str]) -> dict[str, dict]:
    files = sorted(glob.glob(os.path.join(root, "*.jsonl")))[-1:]
    out: dict[str, dict] = {}
    for f in files:
        with open(f) as fh:
            for line in fh:
                if '"kalshi_ticker"' not in line:
                    continue
                try:
                    r = json.loads(line)
                except ValueError:
                    continue
                t = r.get("kalshi_ticker")
                if t in tickers and (t not in out or (out[t].get("generated_at") or "") <= (r.get("generated_at") or "")):
                    out[t] = r
    return out


def _age_s(now: datetime, ts) -> float | None:
    t = iso(ts)
    return round((now - t).total_seconds(), 1) if t else None


def _r(x, n=4):
    return round(x, n) if isinstance(x, (int, float)) else x


# ---------------------------------------------------------------------------------------------- build
def build_slate(data_root: str, *, now: datetime | None = None) -> dict:
    now = now or datetime.now(timezone.utc)
    capture_root = os.path.join(data_root, "kalshi", "capture")
    research = os.path.join(data_root, "research")
    boardd, bmeta = open_board(capture_root)
    truths = load_truths(os.path.join(data_root, "firstball", "store"))

    ledger = _latest_rows(os.path.join(research, "ledger"), ts_key="generated_at_utc")
    shadow = _latest_rows(os.path.join(research, "frozen_producers", "shadow_board"), ts_key="predicted_at")
    model4 = _latest_rows(os.path.join(research, "frozen_producers", "model4"), ts_key="predicted_at")

    groups: dict[str, list] = {}
    skipped = {}
    for tk, m in boardd.items():
        s = series_of(tk)
        if s not in MATCH_SCOPE_SERIES or m.get("status") != "active":
            continue
        pm = parse_market(m)
        fam = SERIES[s][0]
        key = f"{SERIES[s][1]}:{match_code_of(m.get('event_ticker') or tk)}:{SERIES[s][3]}"
        groups.setdefault(key, []).append((pm, m, fam))
    mw_tickers = {pm.ticker for g in groups.values() for pm, _m, fam in g if fam == "MATCH_WINNER"}
    disloc = _latest_dislocations(os.path.join(research, "external", "dislocations"), mw_tickers)

    matches = []
    for key, items in groups.items():
        mws = [(pm, m) for pm, m, fam in items if fam == "MATCH_WINNER"]
        if not mws:
            skipped["no_match_winner_listed"] = skipped.get("no_match_winner_listed", 0) + 1
            continue
        code = key.split(":")[1]
        truth = truth_for(truths, mws[0][1].get("event_ticker") or mws[0][0].ticker)
        fb = first_ball_bound(truth)
        if fb is not None and fb <= now:
            skipped["first_ball_already_observed"] = skipped.get("first_ball_already_observed", 0) + 1
            continue
        sched = mws[0][1].get("occurrence_datetime") or mws[0][1].get("expected_expiration_time")
        sched_dt = iso(sched)
        if sched_dt and (now - sched_dt).total_seconds() > DROP_PAST_SCHEDULED_H * 3600:
            skipped["scheduled_start_over_24h_past"] = skipped.get("scheduled_start_over_24h_past", 0) + 1
            continue
        matches.append(_match_packet(key, code, items, mws, ledger, shadow, model4, disloc, truth, now, sched))

    matches.sort(key=lambda x: (x["scheduled_start"] or "9999", x["match_key"]))
    n_markets = sum(len(x["markets"]) for x in matches)
    body = {
        "slate_version": SLATE_VERSION, "schema_version": ASSISTED_SCHEMA_VERSION,
        "built_at": now.isoformat(),
        "AUTONOMOUS_REAL_MONEY_AUTHORITY": AUTONOMOUS_REAL_MONEY_AUTHORITY,
        "CHATGPT_ASSISTED_TRACK": CHATGPT_ASSISTED_TRACK, "authority": ASSISTED_AUTHORITY,
        "purpose": ("handicapping packet for a human/ChatGPT decision; it selects nothing, ranks nothing as a bet, "
                    "and makes no claim that any number here beats the market"),
        "probability_convention": "every probability is P(ticker resolves YES)",
        "sources": {
            **bmeta,
            "ledger_rows": len(ledger), "ledger_last": max((r.get("generated_at_utc") or "" for r in ledger.values()), default=None),
            "shadow_rows": len(shadow), "shadow_last": max((r.get("predicted_at") or "" for r in shadow.values()), default=None),
            "model4_rows": len(model4), "model4_last": max((r.get("predicted_at") or "" for r in model4.values()), default=None),
            "external_rows": len(disloc), "external_last": max((r.get("generated_at") or "" for r in disloc.values()), default=None),
            "first_ball_truths": len(truths),
        },
        "counts": {"matches": len(matches), "markets": n_markets, "skipped_matches": skipped},
        "matches": matches,
    }
    body["content_sha256"] = canonical_hash({k: v for k, v in body.items() if k != "built_at"})
    body["slate_id"] = f"SL-{now.strftime('%Y%m%dT%H%M%SZ')}-{body['content_sha256'][:8]}"
    return body


def _match_packet(key, code, items, mws, ledger, shadow, model4, disloc, truth, now, sched) -> dict:
    pm0, m0 = mws[0]
    series = series_of(pm0.ticker)
    fam_tour, fam_level, disc = SERIES[series][1], SERIES[series][2], SERIES[series][3]
    info = classify_competition(pm0.competition, pm0.tour or fam_tour)
    sh = next((shadow[pm.ticker] for pm, _ in mws if pm.ticker in shadow), None)
    lg = next((ledger[pm.ticker] for pm, _ in mws if pm.ticker in ledger), None)
    level = (sh or lg or {}).get("level") or info.get("level") or fam_level
    surface = (sh or lg or {}).get("surface")
    lb = level_bucket(series, level, disc)
    warnings = []

    # ---- players, oriented by the rules text (player A = first-listed competitor)
    players = {"a": pm0.player_a, "b": pm0.player_b}
    per_player = {}
    for pm, m in mws:
        side = "a" if pm.subject_is_a else ("b" if pm.subject_is_a is False else None)
        if side:
            per_player[side] = pm.ticker
            players[side] = pm.subject or players[side]          # full name from the contract itself
    ls = (lg or {}).get("inputs") or {}
    lq = ((lg or {}).get("quality") or {}).get("inputs") or {}
    lp = ((lg or {}).get("quality") or {}).get("pillars") or {}
    # ledger/shadow A,B are the ledger's own player_a/b; re-key by NAME so orientation is never guessed
    if lg and lg.get("player_a") == players["a"]:
        orient = "same"
    elif lg and lg.get("player_b") == players["a"]:
        orient = "flipped"
    else:
        orient = None                           # cannot tell which ledger player is A: report nothing

    def _ab(a, b):
        return {"same": (a, b), "flipped": (b, a)}.get(orient, (None, None))
    sflip = bool(sh and sh.get("subject_is_a") is not None and (
        (sh["ticker"] == per_player.get("a")) != bool(sh["subject_is_a"])))

    def _sab(a, b):
        return (b, a) if sflip else (a, b)
    serve_a, serve_b = _sab((sh or {}).get("serve_evidence_a"), (sh or {}).get("serve_evidence_b"))
    elo_a, elo_b = _ab(ls.get("elo_a"), ls.get("elo_b"))
    spw_a, spw_b = _ab(ls.get("pa"), ls.get("pb"))
    sr_a, sr_b = _ab(ls.get("sr_pa"), ls.get("sr_pb"))
    n_a, n_b = _ab(lq.get("n_matches_a"), lq.get("n_matches_b"))
    d_a, d_b = _ab(lq.get("days_since_last_a"), lq.get("days_since_last_b"))
    env = (sh or {}).get("fair_envelope") or {}
    base = env.get("base")
    # the envelope is stored for the shadow row's own subject; express its deltas for player A
    a_sign = -1.0 if (sh and sh.get("ticker") != per_player.get("a")) else 1.0
    surf_adj = None
    if base is not None:
        surf_adj = {"basis": "change in fair_v1 P(player A wins) under the frozen surface-prior perturbations",
                    **{k: _r(a_sign * (env[k] - base)) for k in ("surface_pool_low", "surface_pool_high",
                                                                 "surface_dev_loose", "surface_dev_tight") if k in env}}
    if not sh and not lg:
        warnings.append("NO_MODEL_FOR_MATCH: no Gen-1 ledger or shadow-board row (identity unmapped, doubles, or unpriced format)")
    if disc != "singles":
        warnings.append("DOUBLES_NOT_MODELLED_BY_FROZEN_PRODUCERS")
    if lb not in FIRST_BALL_COVERED:
        warnings.append("FIRST_BALL_SOURCE_UNAVAILABLE: Challenger/ITF/WTA125 starts are not observed; a nominal time is not a first ball")
    sched_dt = iso(sched)
    if sched_dt and sched_dt <= now:
        warnings.append("SCHEDULED_START_PASSED: the match may already be under way")
    if (sh or lg) and ((sh or lg).get("quality") or {}).get("grade", (sh or {}).get("data_quality_grade")) in ("C", "D"):
        warnings.append("LOW_DATA_QUALITY")
    frozen_context = []
    if lb == "ITF":
        frozen_context.append("W3-2026-001-ABSTAIN-ITF: the frozen research rule abstains at ITF (the model's ITF disagreement was worth less than nothing)")

    markets = []
    for pm, m, fam in sorted(items, key=lambda x: (x[2] != "MATCH_WINNER", x[2], x[0].ticker)):
        markets.append(_market_row(pm, m, fam, ledger.get(pm.ticker), shadow.get(pm.ticker), model4.get(pm.ticker),
                                   disloc.get(pm.ticker), now))
    mw_rows = [x for x in markets if x["market_family"] == "MATCH_WINNER"]
    model_age = _age_s(now, (sh or {}).get("predicted_at") or (lg or {}).get("generated_at_utc"))
    if model_age is not None and model_age > STALE_MODEL_H * 3600:
        warnings.append("MODEL_ROW_STALE: newest frozen-producer row is over 13h old")

    return {
        "match_key": key, "match_code": code,
        "physical_match_id": (sh or {}).get("physical_match_id"),
        "event_id": m0.get("event_ticker"),
        "tour": fam_tour if fam_tour in ("ATP", "WTA") else info.get("tour"),
        "level": level, "level_bucket": lb, "discipline": disc,
        "competition": pm0.competition, "round": pm0.round,
        "surface": surface, "surface_bucket": surface_bucket(surface, pm0.competition),
        "players": players, "match_winner_ticker": per_player,
        "scheduled_start": sched,
        "first_ball": {"status": "NOT_OBSERVED_STARTED", "source_coverage": "COVERED" if lb in FIRST_BALL_COVERED else "NO_SOURCE",
                       "truth_confidence": truth.confidence if truth else None,
                       "earliest_possible_first_ball": first_ball_bound(truth).isoformat() if truth and first_ball_bound(truth) else None},
        "model_context": {
            "player_a_win": {"gen1": _r(_ledger_p(ledger, per_player, "a", "ELO_DP_FAIR")),
                             "gen2": _r(_sh_p(shadow, per_player, "a", "gen2_probability")),
                             "fair_v1": _r(_sh_p(shadow, per_player, "a", "fair_v1_probability")),
                             "fair_v1_envelope": [_r(_sh_env(shadow, per_player, "a", min)), _r(_sh_env(shadow, per_player, "a", max))]},
            "model_uncertainty": _r((sh or {}).get("model_uncertainty")),
            "serve_evidence": {"player_a_points": _r(serve_a, 0), "player_b_points": _r(serve_b, 0),
                               "thinner": _r((sh or {}).get("thinner_serve_points"), 0)},
            "rating_state": {"elo_a": _r(elo_a, 1), "elo_b": _r(elo_b, 1),
                             "serve_point_win_a": _r(spw_a), "serve_point_win_b": _r(spw_b),
                             "structural_serve_a": _r(sr_a), "structural_serve_b": _r(sr_b),
                             "tour_serve_baseline": _r(ls.get("spw_baseline")),
                             "hold_break_note": ("hold/break probabilities follow from the serve-point probabilities "
                                                 "through the frozen DP engine; no separate hold/break model exists"),
                             "blend_weight": _r((sh or {}).get("blend_weight")),
                             "ratings_as_of": (lg or {}).get("ratings_as_of"),
                             "asof_base_date": (sh or {}).get("asof_base_date")},
            "surface_adjustment": surf_adj,
            "recent_form_inputs": {"matches_on_record_a": n_a, "matches_on_record_b": n_b,
                                   "days_since_last_match_a": d_a, "days_since_last_match_b": d_b,
                                   "recency_pillar": lp.get("recency"), "experience_pillar": lp.get("experience"),
                                   "note": "the repository holds recency/experience inputs, not a win-loss form model"},
            "data_quality": {"score": (sh or {}).get("data_quality_score") or ((lg or {}).get("quality") or {}).get("data_quality_score"),
                             "grade": (sh or {}).get("data_quality_grade") or ((lg or {}).get("quality") or {}).get("grade")},
            "selector_v1": {pm_t: (shadow.get(pm_t) or {}).get("selector_decision") for pm_t in per_player.values()},
            "model_rows_predicted_at": {"shadow_board": (sh or {}).get("predicted_at"),
                                        "gen1_ledger": (lg or {}).get("generated_at_utc")},
        },
        "external_context": {x["ticker"]: x["external"] for x in mw_rows},
        "frozen_rule_context": frozen_context,
        "warnings": warnings,
        "available_expressions": sorted({x["expression"] for x in markets}),
        "markets": markets,
    }


def _ledger_p(ledger, per_player, side, key):
    t = per_player.get(side)
    r = ledger.get(t) if t else None
    return ((r or {}).get("models") or {}).get(key)


def _sh_p(shadow, per_player, side, key):
    t = per_player.get(side)
    return (shadow.get(t) or {}).get(key) if t else None


def _sh_env(shadow, per_player, side, fn):
    t = per_player.get(side)
    env = (shadow.get(t) or {}).get("fair_envelope") if t else None
    return fn(env.values()) if env else None


def _market_row(pm, m, fam, lg, sh, m4, dl, now) -> dict:
    bid, ask = fnum(m.get("yes_bid_dollars"), open_unit=True), fnum(m.get("yes_ask_dollars"), open_unit=True)
    two = bid is not None and ask is not None and bid <= ask
    mid = 0.5 * (bid + ask) if two else None
    ask_sz, bid_sz = fnum(m.get("yes_ask_size_fp")), fnum(m.get("yes_bid_size_fp"))
    age = _age_s(now, m.get("captured_at"))
    gen1 = ((lg or {}).get("models") or {}).get("ELO_DP_FAIR")
    fair = (sh or {}).get("fair_v1_probability")
    m4c = (m4 or {}).get("conditioned_probability")
    if fair is not None:
        p, src = fair, "fair_v1 (shadow_board_v1)"
    elif m4c is not None:
        p, src = m4c, "market_conditioned_v1 (model4_board_v1)"
    elif gen1 is not None:
        p, src = gen1, "Gen-1 ELO_DP_FAIR (prediction ledger)"
    else:
        p, src = None, None
    w = []
    if not two:
        w.append("ONE_SIDED_OR_NO_QUOTE")
    else:
        if ask - bid > WIDE_SPREAD:
            w.append("WIDE_SPREAD")
        if ask_sz is not None and ask_sz < THIN_SIZE:
            w.append("THIN_DISPLAYED_SIZE")
    if age is not None and age > STALE_QUOTE_S:
        w.append("STALE_QUOTE: captured over 30 min ago; re-check the live book before deciding")
    ext = None
    if fam == "MATCH_WINNER":
        ext = {"bovada": _r((dl or {}).get("external_prices", {}).get("bovada")),
               "smarkets": _r((dl or {}).get("external_prices", {}).get("smarkets")),
               "consensus": _r((dl or {}).get("external_fair")),
               "reference_kind": (dl or {}).get("reference_kind"),
               "n_independent_groups": (dl or {}).get("n_independent_groups"),
               "triangulation": (dl or {}).get("triangulation"),
               "external_quote_age_s": _r((dl or {}).get("external_quote_age_s"), 0),
               "external_v1_decision": (dl or {}).get("decision"),
               "scanned_at": (dl or {}).get("generated_at")}
        if not dl or (ext["bovada"] is None and ext["smarkets"] is None):
            w.append("NO_EXTERNAL_PRICE")
        elif ext["external_quote_age_s"] is not None and ext["external_quote_age_s"] > STALE_EXTERNAL_S:
            w.append("EXTERNAL_PRICE_STALE")
    observed_by = [n for n, r in (("gen1_ledger", lg), ("shadow_board_v1", sh), ("model4_board_v1", m4), ("external_scan", dl)) if r]
    return {
        "ticker": pm.ticker, "event": m.get("event_ticker"), "market_family": fam,
        "expression": expression_of_family(fam),
        "description": m.get("title") or m.get("yes_sub_title"), "yes_means": m.get("yes_sub_title"),
        "subject": pm.subject, "subject_is_a": pm.subject_is_a,
        "line": pm.line, "set_index": pm.set_index, "exact_score": list(pm.exact_score) if pm.exact_score else None,
        "kalshi": {"bid": bid, "ask": ask, "mid": _r(mid), "spread": _r(ask - bid) if two else None,
                   "bid_size": bid_sz, "ask_size": ask_sz, "taker_fee_at_ask": taker_fee(ask, 1.0) if ask else None,
                   "no_ask": _r(1 - bid) if bid is not None else None,
                   "quote_captured_at": m.get("captured_at"), "quote_age_s": age,
                   "open_interest": fnum(m.get("open_interest_fp")), "volume_24h": fnum(m.get("volume_24h_fp"))},
        "model": {"gen1": _r(gen1), "gen1_elo_only": _r(((lg or {}).get("models") or {}).get("ELO")),
                  "gen1_structural": _r(((lg or {}).get("models") or {}).get("STRUCTURAL")),
                  "gen2": _r((sh or {}).get("gen2_probability")), "fair_v1": _r(fair),
                  "fair_v1_envelope": [_r(min(sh["fair_envelope"].values())), _r(max(sh["fair_envelope"].values()))]
                  if (sh or {}).get("fair_envelope") else None,
                  "model4_conditioned": _r(m4c), "model4_fundamental": _r((m4 or {}).get("fundamental_probability")),
                  "model_uncertainty": _r((sh or {}).get("model_uncertainty")),
                  "selector_v1": (sh or {}).get("selector_decision"),
                  "qualification_ok": (sh or {}).get("qualification_ok")},
        "model_probability_yes": _r(p), "model_probability_source": src,
        "model_minus_mid": _r(p - mid) if (p is not None and mid is not None) else None,
        "model_side_edges": side_edges(p, bid, ask),
        "model_preferred_side": preferred_side(p, bid, ask),
        "external": ext,
        "observed_by": observed_by,
        "warnings": w,
    }


# ---------------------------------------------------------------------------------------------- render
def _pct(x):
    return f"{100 * x:.1f}%" if isinstance(x, (int, float)) else "--"


def _c(x):
    return f"{x:.2f}" if isinstance(x, (int, float)) else "--"


def render_markdown(s: dict, *, max_derivatives: int = 6) -> str:
    L = [f"# ASSISTED SLATE -- {s['built_at'][:16]}Z (`{s['slate_id']}`)", "",
         f"**AUTONOMOUS_REAL_MONEY_AUTHORITY = {s['AUTONOMOUS_REAL_MONEY_AUTHORITY']}. "
         f"CHATGPT_ASSISTED_TRACK = {s['CHATGPT_ASSISTED_TRACK']}.** This is a handicapping packet: it selects "
         "nothing and claims no edge. Every probability is P(ticker resolves YES). Quotes are capture snapshots; "
         "re-check the live book before deciding.", "",
         f"{s['counts']['matches']} open matches not seen started, {s['counts']['markets']} markets. "
         f"Skipped: {json.dumps(s['counts']['skipped_matches'])}. Sources: shadow board {s['sources'].get('shadow_last')}, "
         f"Model 4 {s['sources'].get('model4_last')}, Gen-1 ledger {s['sources'].get('ledger_last')}, "
         f"external {s['sources'].get('external_last')}, capture {s['sources'].get('last_capture_file')}.", ""]
    for x in s["matches"]:
        mc = x["model_context"]
        L += [f"## {x['players']['a']} vs {x['players']['b']} -- {x['competition']} {x['round'] or ''}".rstrip(), "",
              f"{x['level_bucket']} ({x['level']}) · {x['surface'] or 'surface ?'} · scheduled {x['scheduled_start']} · "
              f"first ball: {x['first_ball']['status']} (source {x['first_ball']['source_coverage']}) · "
              f"match `{x['physical_match_id'] or x['match_key']}`", ""]
        L += ["| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector |",
              "|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in x["markets"]:
            if r["market_family"] != "MATCH_WINNER":
                continue
            k, mo, e = r["kalshi"], r["model"], r["external"] or {}
            env = mo.get("fair_v1_envelope") or [None, None]
            L.append(f"| {r['subject']} (`{r['ticker']}`) | {_c(k['bid'])} / {_c(k['ask'])} ({k['ask_size'] or 0:.0f}) | {_pct(k['mid'])} | "
                     f"{_pct(mo['gen1'])} | {_pct(mo['gen2'])} | {_pct(mo['fair_v1'])} [{_pct(env[0])}-{_pct(env[1])}] | "
                     f"{_pct(e.get('bovada'))} | {_pct(e.get('smarkets'))} | {_pct(e.get('consensus'))} | "
                     f"{e.get('triangulation') or '--'} | {mo.get('selector_v1') or '--'} |")
        sv, rs, rf = mc["serve_evidence"], mc["rating_state"], mc["recent_form_inputs"]
        L += ["", f"* Serve evidence (points): A {sv['player_a_points']}, B {sv['player_b_points']}; "
                  f"serve-point win A {_pct(rs['serve_point_win_a'])}, B {_pct(rs['serve_point_win_b'])}; "
                  f"Elo A {rs['elo_a']}, B {rs['elo_b']}; model uncertainty {mc['model_uncertainty']}",
              f"* Form inputs: days since last match A {rf['days_since_last_match_a']}, B {rf['days_since_last_match_b']}; "
              f"matches on record A {rf['matches_on_record_a']}, B {rf['matches_on_record_b']}; "
              f"data quality {mc['data_quality']['grade']}"]
        if mc.get("surface_adjustment"):
            L.append("* Surface-prior sensitivity (P(A) change): " + ", ".join(
                f"{k} {v:+.3f}" for k, v in mc["surface_adjustment"].items() if isinstance(v, float)))
        der = [r for r in x["markets"] if r["market_family"] != "MATCH_WINNER"]
        if der:
            priced = sorted([r for r in der if r["model_minus_mid"] is not None],
                            key=lambda r: -abs(r["model_minus_mid"]))[:max_derivatives]
            L.append(f"* Derivatives listed: {len(der)} ({', '.join(x['available_expressions'])}); "
                     f"{sum(1 for r in der if r['model_probability_yes'] is not None)} carry a model probability")
            for r in priced:
                k = r["kalshi"]
                L.append(f"  * `{r['ticker']}` {r['description']}: {_c(k['bid'])}/{_c(k['ask'])} mid {_pct(k['mid'])}, "
                         f"model {_pct(r['model_probability_yes'])} ({r['model_probability_source']})")
        warn = x["warnings"] + sorted({w.split(':')[0] for r in x["markets"] for w in r["warnings"]})
        if warn:
            L.append(f"* Warnings: {'; '.join(w.split(':')[0] for w in warn)}")
        for c in x["frozen_rule_context"]:
            L.append(f"* Frozen research context: {c}")
        L.append("")
    L += ["---", "", "Record a decision (BET / PASS / WATCH) with `scripts/research/record_assisted_decision.py` or the "
          "`TENNIS assisted record` workflow; see docs/ASSISTED_HANDICAPPING.md. Decisions must be recorded before the "
          "first ball and are never edited afterwards.", ""]
    return "\n".join(L)


def write_slate(slate: dict, out_dir: str) -> dict:
    os.makedirs(out_dir, exist_ok=True)
    tmp = os.path.join(out_dir, "latest.json.tmp")
    with open(tmp, "w") as f:
        json.dump(slate, f, indent=1, default=str)
    os.replace(tmp, os.path.join(out_dir, "latest.json"))
    with open(os.path.join(out_dir, "latest.md"), "w") as f:
        f.write(render_markdown(slate))
    run = {"slate_id": slate["slate_id"], "built_at": slate["built_at"], "content_sha256": slate["content_sha256"],
           "matches": slate["counts"]["matches"], "markets": slate["counts"]["markets"],
           "skipped": slate["counts"]["skipped_matches"], "sources": slate["sources"]}
    with open(os.path.join(out_dir, "slate_runs.jsonl"), "a") as f:
        f.write(json.dumps(run, default=str) + "\n")
    return run


def load_slate(out_dir: str) -> dict | None:
    p = os.path.join(out_dir, "latest.json")
    try:
        return json.load(open(p))
    except (OSError, ValueError):
        return None


def slate_market(slate: dict | None, ticker: str) -> tuple[dict | None, dict | None]:
    """(match packet, market row) of a ticker on a slate."""
    for x in (slate or {}).get("matches") or []:
        for r in x["markets"]:
            if r["ticker"] == ticker:
                return x, r
    return None, None
