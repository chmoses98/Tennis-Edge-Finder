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
  discrepancy sanity      every priced contract carries a model-market gap, a band (NORMAL / REVIEW /
                          HIGH_REVIEW / EXTREME), identity / orientation / quote-freshness / external /
                          data-quality checks and the reasons the gap may be fake (tennis_edge.assisted.discrepancy)

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
from . import discrepancy as DS
from tennis_edge.firstball import start_times as ST
from tennis_edge.firstball.start_evidence import board_statuses
from .market import capture_days, first_ball_bound, fnum, iso, load_truths, truth_for
from .schema import (ASSISTED_SCHEMA_VERSION, expression_of_family, level_bucket, match_code_of, preferred_side,
                     series_of, side_edges, surface_bucket)
from .store import canonical_hash

SLATE_VERSION = "assisted_slate_v2"          # v2: discrepancy sanity layer on every priced contract
STALE_QUOTE_S = 30 * 60
STALE_EXTERNAL_S = 30 * 60
WIDE_SPREAD = 0.06
THIN_SIZE = 10.0
STALE_MODEL_H = 13.0
DROP_PAST_SCHEDULED_H = 24.0
#: Gen-1 doubles (ELO_DP_FAIR on team ratings) failed the discrepancy audit's pre-stated no-skill test
#: (research/model_market_discrepancy/AUDIT.md: pregame-clean Brier ~0.32 vs Kalshi ~0.22 vs coin flip 0.25,
#: outcome correlation ~-0.06). It keeps running as research; on the assisted slate it contributes nothing.
GEN1_DOUBLES_WARNING = "GEN1_DOUBLES_UNVALIDATED_DO_NOT_USE"
DOUBLES_MODEL_VALIDITY = {
    "gen1": "UNVALIDATED_DO_NOT_USE", "gen2": "NOT_PRODUCED_FOR_DOUBLES", "fair_v1": "NOT_PRODUCED_FOR_DOUBLES",
    "model4": "NOT_PRODUCED_FOR_DOUBLES",
    "reason": ("Current Gen-1 doubles failed the no-skill validation and is suppressed from assisted handicapping "
               "pending a validated replacement. No model probability is shown for doubles; prices, liquidity and "
               "external markets remain for manual handicapping."),
}
#: first-ball truth sources exist for these levels only (README: ATP/WTA main tour and the Slams)
FIRST_BALL_COVERED = ("ATP", "WTA")

MATCH_SCOPE_SERIES = {s for s, (fam, _t, _l, _d) in SERIES.items()
                      if FAMILIES.get(fam, {}).get("scope") == "MATCH" and expression_of_family(fam)}


# ---------------------------------------------------------------------------------------------- loading
def open_board(capture_root: str, now: datetime | None = None) -> tuple[dict[str, dict], dict]:
    """ticker -> current record: the latest FULL capture snapshot, then every CHANGED pass after it.
    With `now`, nothing captured after `now` is read (replays reproduce the board as it was)."""
    days = capture_days(capture_root)
    if now is not None:
        days = [d for d in days if d <= now.strftime("%Y-%m-%d")]
    days = days[-2:]
    files = []
    for d in days:
        files += sorted(glob.glob(os.path.join(capture_root, d, "*.quotes.jsonl.gz")))
    if now is not None:
        stamp = now.strftime("%Y%m%dT%H%M%SZ")
        files = [f for f in files if os.path.basename(f)[:16] <= stamp]
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
                    if r.get("ticker") and not (now is not None and iso(r.get("captured_at")) and iso(r["captured_at"]) > now):
                        out[r["ticker"]] = r
        except (OSError, EOFError):
            continue
    meta = {"capture_files_read": len(files) - start,
            "base_full_snapshot": os.path.basename(files[start]) if files else None,
            "last_capture_file": os.path.basename(files[-1]) if files else None}
    return out, meta


#: a run snapshot (scripts/kalshi/snapshot_open_markets.py) older than this is not the lifecycle authority
RUN_SNAPSHOT_MAX_AGE_S = 20 * 60


def overlay_run_snapshot(board: dict, meta: dict, snapshot_root: str, now: datetime) -> tuple[dict, dict]:
    """Live builds only: a FULL open snapshot taken minutes ago replaces the incremental board for every
    MATCH-scope ticker. Markets absent from it are closed or settled (the incremental board can lag a closure by
    up to the ~75-minute full-snapshot interval), and its quotes are minutes, not half an hour, old."""
    mans = sorted(glob.glob(os.path.join(snapshot_root, "*", "*.open_snapshot.manifest.json")))
    for mp in reversed(mans):
        try:
            man = json.load(open(mp))
        except (OSError, ValueError):
            continue
        if not man.get("complete"):
            continue
        age = (now - iso(man["finished_at"])).total_seconds()
        data = mp.replace(".open_snapshot.manifest.json", ".open_snapshot.jsonl.gz")
        if age > RUN_SNAPSHOT_MAX_AGE_S or not os.path.exists(data):
            break
        snap = {}
        with gzip.open(data, "rt") as fh:
            for line in fh:
                if line.strip():
                    r = json.loads(line)
                    snap[r["ticker"]] = r
        out = {tk: r for tk, r in board.items() if tk.split("-")[0] not in MATCH_SCOPE_SERIES}
        dropped = sum(1 for tk in board if tk.split("-")[0] in MATCH_SCOPE_SERIES and tk not in snap)
        out.update(snap)
        return out, {**meta, "run_snapshot": man["run_id"], "run_snapshot_age_s": round(age, 1),
                     "dropped_not_open_in_run_snapshot": dropped}
    return board, {**meta, "run_snapshot": None}


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
def build_slate(data_root: str, *, now: datetime | None = None, replay: bool = False) -> dict:
    """`replay=True` rebuilds the slate exactly AS OF `now` (no capture file or record after `now` is read);
    production builds at the real clock, where no later file can exist."""
    now = now or datetime.now(timezone.utc)
    capture_root = os.path.join(data_root, "kalshi", "capture")
    research = os.path.join(data_root, "research")
    boardd, bmeta = open_board(capture_root, now if replay else None)
    if not replay:
        boardd, bmeta = overlay_run_snapshot(boardd, bmeta, os.path.join(data_root, "kalshi", "run_snapshots"), now)
    truths = load_truths(os.path.join(data_root, "firstball", "store"))

    ledger = _latest_rows(os.path.join(research, "ledger"), ts_key="generated_at_utc")
    shadow = _latest_rows(os.path.join(research, "frozen_producers", "shadow_board"), ts_key="predicted_at")
    model4 = _latest_rows(os.path.join(research, "frozen_producers", "model4"), ts_key="predicted_at")

    ratings = _ratings_context(data_root, now)
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
    pair_keys = {}                                  # the same two players listed under more than one match
    for key, items in groups.items():
        pk = _pair_key(items)
        if pk:
            pair_keys.setdefault(pk, set()).add(key)
    ratings["pair_keys"] = pair_keys

    # ---- start-time reconciliation for every match on the board: what the live sources and first-ball truth
    # say, never the nominal alone (tennis_edge.firstball.start_times)
    board_rows = []
    for key, items in groups.items():
        mws = [(pm, m) for pm, m, fam in items if fam == "MATCH_WINNER"]
        if mws:
            s0 = series_of(mws[0][0].ticker)
            board_rows.append({"match_id": key, "code": key.split(":")[1], "series": s0,
                               "nominal": mws[0][1].get("occurrence_datetime") or mws[0][1].get("expected_expiration_time"),
                               "level_bucket": level_bucket(s0, None, SERIES[s0][3])})
    starts = board_statuses(board_rows, store_root=os.path.join(data_root, "firstball", "store"), now=now)

    matches = []
    for key, items in groups.items():
        mws = [(pm, m) for pm, m, fam in items if fam == "MATCH_WINNER"]
        if not mws:
            skipped["no_match_winner_listed"] = skipped.get("no_match_winner_listed", 0) + 1
            continue
        code = key.split(":")[1]
        truth = truth_for(truths, mws[0][1].get("event_ticker") or mws[0][0].ticker)
        start = starts.get(key)
        if start and start["start_status"] == ST.STARTED:
            skipped["first_ball_already_observed"] = skipped.get("first_ball_already_observed", 0) + 1
            continue
        if start and start["start_status"] == ST.NO_PLAY:
            skipped["no_play_confirmed"] = skipped.get("no_play_confirmed", 0) + 1
            continue
        sched = mws[0][1].get("occurrence_datetime") or mws[0][1].get("expected_expiration_time")
        sched_dt = iso(sched)
        if sched_dt and (now - sched_dt).total_seconds() > DROP_PAST_SCHEDULED_H * 3600:
            skipped["scheduled_start_over_24h_past"] = skipped.get("scheduled_start_over_24h_past", 0) + 1
            continue
        x = _match_packet(key, code, items, mws, ledger, shadow, model4, disloc, truth, now, sched, ratings)
        _apply_start(x, start)
        matches.append(x)

    matches.sort(key=lambda x: ((x.get("start") or {}).get("current_expected_start") or x["scheduled_start"] or "9999",
                                x["match_key"]))
    plan = ST.plan_windows([{"match_id": x["event_id"], "label": f"{x['players']['a']} vs {x['players']['b']}",
                             "level_bucket": x["level_bucket"], "discipline": x["discipline"], "start": x["start"]}
                            for x in matches], now)
    n_markets = sum(len(x["markets"]) for x in matches)
    rows = [r for x in matches for r in x["markets"]]
    cfg = DS.load_config()
    sanity = {
        "version": cfg["version"],
        "purpose": ("a large model-market gap is a question (WHY are we so different?), not an edge: stale or in-play "
                    "quotes, mapping/orientation faults and thin data are ruled out before a disagreement is read"),
        "bands_pp": cfg["bands_pp"], "freshness_minutes": cfg["freshness_minutes"],
        "rules": {"NORMAL": "no additional restriction", "REVIEW": "discrepancy context surfaced",
                  "HIGH_REVIEW": "an explicit discrepancy_explanation is required before any BET",
                  "EXTREME": ("DATA_WARNING by default; a BET is refused unless all nine Part J conditions hold, and even "
                              "then it is only ELIGIBLE_FOR_HUMAN_REVIEW, never an automatic bet")},
        "model_probabilities_changed": False,
        "namesake_registry_loaded": ratings.get("names") is not None,
        "counts_by_band": _count(rows, "discrepancy_band"),
        "counts_by_status": _count(rows, "discrepancy_sanity_status"),
        "match_winner_counts_by_band": _count([r for r in rows if r["market_family"] == "MATCH_WINNER"], "discrepancy_band"),
        "counts_by_freshness": _count([r for r in rows if r["model_market_gap_pp"] is not None], "market_freshness_status"),
        "extreme": [r["ticker"] for r in rows if r["discrepancy_band"] == DS.EXTREME],
    }
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
        "discrepancy_sanity": sanity,
        "start_time_reconciliation": {
            "authority": ("STARTED is decided by first-ball truth, then live-score state; the expected start by the "
                          "live source's own current time (ESPN timeValid), pulled earlier by court progression, "
                          "else a Kalshi nominal at LOW confidence (never a day placeholder)"),
            "statuses": list(ST.START_STATUSES),
            "bet_rule": ("BET blocked for STARTED / STATUS_AMBIGUOUS / NO_PLAY, and for live-source-covered matches "
                         f"without a live PRE reading in the last {ST.LIVE_STATUS_MAX_AGE_S // 60} min"),
            "counts_by_status": _count([x for x in matches], "start_status"),
            "bet_blocked_matches": sum(1 for x in matches if not (x.get("start") or {}).get("bet_allowed", True)),
        },
        "next_actionable_window": plan["next_window"],
        "upcoming_windows": plan["windows"],
        "main_tour_status_unverified": plan["main_tour_status_unverified"],
        "refresh_due_by": (plan["next_window"] or {}).get("recommended_run_tennis_time"),
        "matches": matches,
    }
    body["content_sha256"] = canonical_hash({k: v for k, v in body.items() if k != "built_at"})
    body["slate_id"] = f"SL-{now.strftime('%Y%m%dT%H%M%SZ')}-{body['content_sha256'][:8]}"
    return body


def _match_packet(key, code, items, mws, ledger, shadow, model4, disloc, truth, now, sched, ratings=None) -> dict:
    pm0, m0 = mws[0]
    series = series_of(pm0.ticker)
    fam_tour, fam_level, disc = SERIES[series][1], SERIES[series][2], SERIES[series][3]
    model_validity = None
    if disc != "singles":
        # no model row of any producer may speak for a doubles contract: the Gen-1 doubles model failed its
        # no-skill test, and no singles producer (shadow board, Model 4) is a doubles model. Raw markets stay.
        ledger, shadow, model4 = {}, {}, {}
        model_validity = dict(DOUBLES_MODEL_VALIDITY)
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
        warnings.append(f"{GEN1_DOUBLES_WARNING}: {DOUBLES_MODEL_VALIDITY['reason']}")
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
                                   disloc.get(pm.ticker), now, model_validity=model_validity))
    mw_rows = [x for x in markets if x["market_family"] == "MATCH_WINNER"]
    identity_checks = _identity_checks(key, series, disc, level, fam_tour, players, per_player, mws, sh, lg, orient,
                                       shadow, mw_rows, ratings or {})
    sab = {"a": (sh or {}).get("player_a_id"), "b": (sh or {}).get("player_b_id")}
    surf = _surface_counts(ratings or {}, sab, surface)
    dq = DS.data_quality(grade=(sh or {}).get("data_quality_grade") or ((lg or {}).get("quality") or {}).get("grade"),
                         serve_a=serve_a, serve_b=serve_b, n_a=n_a, n_b=n_b, days_a=d_a, days_b=d_b,
                         level_familiarity=lp.get("level_familiarity"), surface_n_a=surf[0], surface_n_b=surf[1])
    sched_passed = bool(iso(sched) and iso(sched) <= now)
    for r in markets:
        _apply_discrepancy(r, identity_checks, dq, model4.get(r["ticker"]), shadow.get(r["ticker"]),
                           lb in FIRST_BALL_COVERED, sched_passed)
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
        "model_validity": model_validity,
        "external_context": {x["ticker"]: x["external"] for x in mw_rows},
        "identity_checks": identity_checks,
        "data_quality_check": dq,
        "frozen_rule_context": frozen_context,
        "warnings": warnings,
        "available_expressions": sorted({x["expression"] for x in markets}),
        "markets": markets,
    }


# ---------------------------------------------------------------------------------------------- discrepancy
def _ratings_context(data_root: str, now: datetime) -> dict:
    """Rating-state tables (name, last_date, per-surface counts) for the namesake and surface-sample checks.
    Missing tables leave both checks NA; nothing here reads or changes a rating."""
    tables = {}
    for tour in ("ATP", "WTA"):
        p = os.path.join(data_root, "processed", f"ratings_{tour}.json")
        try:
            tables[tour] = (json.load(open(p)) or {}).get("players") or {}
        except (OSError, ValueError):
            continue
    names = DS.namesake_index_from_players(list(tables.values()), as_of=now.date()) if tables else None
    return {"tables": tables, "names": names}


def _surface_counts(ratings: dict, ids: dict, surface) -> tuple:
    if not surface or not ratings.get("tables"):
        return None, None
    out = []
    for side in ("a", "b"):
        pid = ids.get(side)
        rec = next((t.get(str(pid)) for t in ratings["tables"].values() if pid and str(pid) in t), None)
        if rec is None:
            out.append(None)
            continue
        v = (rec.get("surfaces") or {}).get(surface)
        out.append(v[1] if isinstance(v, list) and len(v) > 1 else 0)
    return tuple(out)


def _pair_key(items) -> frozenset | None:
    from tennis_edge.identity.names import normalize_name
    for pm, _m, fam in items:
        if fam == "MATCH_WINNER" and pm.player_a and pm.player_b:
            return frozenset((normalize_name(pm.player_a), normalize_name(pm.player_b)))
    return None


def _model_level_bucket(level, tour) -> str | None:
    lv = (level or "").upper()
    if not lv:
        return None
    if lv == "ITF":
        return "ITF"
    if lv == "CHALLENGER":
        return "CHALLENGER"
    if lv == "WTA_125":
        return "WTA125"
    if lv in ("OTHER", "TEAM", "EXHIBITION"):
        return "OTHER"
    return tour if tour in ("ATP", "WTA") else None


def _identity_checks(key, series, disc, level, fam_tour, players, per_player, mws, sh, lg, orient, shadow,
                     mw_rows, ratings) -> dict:
    """Match-level identity evidence. PASS / AMBIGUOUS / FAIL / NA per check; nothing is loosened or guessed."""
    lq = ((lg or {}).get("quality") or {})
    c = {
        "physical_match_id": DS.check_physical_match_id((sh or {}).get("physical_match_id")),
        "player_ids": DS.check_player_ids((sh or lg or {}).get("player_a_id"), (sh or lg or {}).get("player_b_id")),
        "identity_confidence": DS.check_identity_confidence(
            *(((sh or {}).get("identity_confidence_a"), (sh or {}).get("identity_confidence_b")) if sh
              else ((lq.get("pillars") or {}).get("identity_confidence"),))),
        "namesake": DS.check_namesakes([players.get("a"), players.get("b")], ratings.get("names")),
        "model_name_orientation": ("PASS" if orient else "AMBIGUOUS") if lg else "NA",
        "both_sides_listed": "PASS" if per_player.get("a") and per_player.get("b") else "AMBIGUOUS",
        "model_complement": DS.check_complement(_sh_p(shadow, per_player, "a", "fair_v1_probability"),
                                                _sh_p(shadow, per_player, "b", "fair_v1_probability")),
        "market_pair": DS.check_market_pair(*[next((r["kalshi"]["mid"] for r in mw_rows if r["ticker"] == per_player.get(sd)), None)
                                              for sd in ("a", "b")]),
        "level_mapping": DS.check_level(level_bucket(series, None, disc), _model_level_bucket(level, fam_tour)),
        "same_pair_other_event": ("AMBIGUOUS" if len((ratings.get("pair_keys") or {}).get(_pair_key(
            [(pm, None, "MATCH_WINNER") for pm, _m in mws]), ()) or ()) > 1 else "PASS"),
        "discipline": "PASS" if disc == "singles" else "AMBIGUOUS",
    }
    if not (sh or lg):
        c["model_row"] = "AMBIGUOUS"
    return c


def _apply_discrepancy(r: dict, checks: dict, dq: dict, m4, sh, first_ball_source: bool, sched_passed: bool):
    """Attach the sanity block to one market row. Reads the row's numbers; changes none of them."""
    k = r["kalshi"]
    fam = r["market_family"]
    if fam == "MATCH_WINNER":
        orient, oev = DS.ticker_orientation(r["ticker"], r["event"], r["subject_is_a"])
        if sh is not None and sh.get("subject_is_a") is not None:
            m_orient, _ = DS.ticker_orientation(r["ticker"], r["event"], sh.get("subject_is_a"))
            if m_orient == "FAILED":
                orient = "FAILED"
            elif m_orient != "VERIFIED" and orient == "VERIFIED":
                orient = "UNKNOWN"
        subj_ok = "PASS" if r["subject"] and r["subject_is_a"] is not None else "AMBIGUOUS"
    else:
        has_subject = bool(r["subject"]) or r["subject_is_a"] is not None
        orient = DS.derivative_orientation(has_subject, r["subject_is_a"], (m4 or {}).get("subject_is_a"))
        subj_ok = "NA"
    checks = {**checks, "ticker_orientation": {"VERIFIED": "PASS", "FAILED": "FAIL", "NOT_APPLICABLE": "NA"}.get(orient, "AMBIGUOUS"),
              "yes_side_meaning": subj_ok}
    mo = r["model"]
    probs = ({"gen1": mo["gen1"], "gen2": mo["gen2"], "fair_v1": mo["fair_v1"]} if fam == "MATCH_WINNER"
             else {"gen1": mo["gen1"], "model4_conditioned": mo["model4_conditioned"], "model4_fundamental": mo["model4_fundamental"]})
    edges = [v for v in (r["model_side_edges"] or {}).values() if isinstance(v, (int, float))]
    e = r["external"] or {}
    d = DS.assess(p_model=r["model_probability_yes"], bid=k["bid"], ask=k["ask"], bid_size=k["bid_size"],
                  ask_size=k["ask_size"], quote_age_s=k["quote_age_s"], identity=DS.identity_status(checks),
                  identity_checks=checks, orientation=orient, data=dq, p_ext=e.get("consensus"),
                  ext_age_s=e.get("external_quote_age_s"), model_uncertainty=mo.get("model_uncertainty"),
                  envelope=mo.get("fair_v1_envelope") if fam == "MATCH_WINNER" else None,
                  model_probs={kk: v for kk, v in probs.items() if v is not None}, first_ball_source=first_ball_source,
                  scheduled_start_passed=sched_passed, side_edge_after_fees=max(edges) if edges else None)
    r["discrepancy"] = d
    for f in ("model_market_gap_pp", "discrepancy_band", "discrepancy_sanity_status", "discrepancy_reason_tags",
              "identity_check_status", "ticker_orientation_status", "market_freshness_status", "external_confirmation_status",
              "data_quality_status"):
        r[f] = d[f]


def _count(rows, key) -> dict:
    out: dict = {}
    for r in rows:
        out[r.get(key)] = out.get(r.get(key), 0) + 1
    return dict(sorted(out.items(), key=lambda kv: str(kv[0])))


def _apply_start(x: dict, start: dict | None):
    """Attach the reconciled start status to a match packet. The nominal stays visible as a prior."""
    st = start or {}
    x["start"] = st
    x["start_status"] = st.get("start_status")
    x["first_ball"].update({"status": st.get("first_ball_status") or x["first_ball"]["status"],
                            "first_ball_source": st.get("first_ball_source"), "start_status": st.get("start_status"),
                            "current_expected_start": st.get("current_expected_start")})
    if st and not st.get("bet_allowed", True):
        x["warnings"].insert(0, f"BET_BLOCKED_START_STATUS: {st.get('start_status')} -- "
                                + "; ".join(r.split(':')[0] for r in st.get("status_reasons") or []))
    if st.get("nominal_is_placeholder"):
        x["warnings"].append("NOMINAL_START_IS_DAY_PLACEHOLDER: Kalshi lists the same time for many matches of this "
                             "series; it is not this match's start")
    if st.get("start_status") == ST.STATUS_AMBIGUOUS:
        x["warnings"].append("STATUS_AMBIGUOUS: re-check live status before any decision; not presented as pregame")


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


def _market_row(pm, m, fam, lg, sh, m4, dl, now, model_validity=None) -> dict:
    bid, ask = fnum(m.get("yes_bid_dollars"), open_unit=True), fnum(m.get("yes_ask_dollars"), open_unit=True)
    two = bid is not None and ask is not None and bid <= ask
    mid = 0.5 * (bid + ask) if two else None
    ask_sz, bid_sz = fnum(m.get("yes_ask_size_fp")), fnum(m.get("yes_bid_size_fp"))
    age = _age_s(now, m.get("captured_at"))
    gen1 = ((lg or {}).get("models") or {}).get("ELO_DP_FAIR")
    fair = (sh or {}).get("fair_v1_probability")
    m4c = (m4 or {}).get("conditioned_probability")
    # Projection V2 (2026-10-05): when the prediction ledger row was priced by the PROMOTED independent model,
    # its probability (every family comes from ONE V2 distribution) is the slate's model number. It never reads a
    # price. fair_v1 / Model 4 / Gen-1 remain the fallbacks, in their old order, for rows V2 did not price.
    v2 = (lg or {}).get("v2") or {}
    p_v2 = gen1 if (lg or {}).get("production_model") == "projection_v2.0" else None
    if p_v2 is not None:
        p, src = p_v2, "projection_v2.0 (prediction ledger)"
    elif fair is not None:
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
    if model_validity:
        w.append(GEN1_DOUBLES_WARNING)
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
                  "projection_v2": _r(p_v2), "projection_v2_grade": v2.get("grade"), "projection_v2_tags": v2.get("tags"),
                  "projection_v2_envelope": [_r(v2.get("envelope_low_yes")), _r(v2.get("envelope_high_yes"))]
                  if v2.get("envelope_low_yes") is not None else None,
                  "incumbent": _r(((lg or {}).get("models") or {}).get("INCUMBENT")),
                  "model4_conditioned": _r(m4c), "model4_fundamental": _r((m4 or {}).get("fundamental_probability")),
                  "model_uncertainty": _r((sh or {}).get("model_uncertainty")),
                  "selector_v1": (sh or {}).get("selector_decision"),
                  "qualification_ok": (sh or {}).get("qualification_ok")},
        "model_probability_yes": _r(p), "model_probability_source": src, "model_validity": model_validity,
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
    w = s.get("next_actionable_window")
    L += ["## NEXT ACTIONABLE MAIN-TOUR WINDOW", ""]
    if w:
        L += [f"* Earliest credible first ball: **{_hm(w['earliest_credible_first_ball'])}**",
              f"* Recommended RUN TENNIS time: **{_hm(w['recommended_run_tennis_time'])}**"
              + ("  (**OVERDUE -- run now**)" if w.get("primary_overdue") else ""),
              f"* Final price/status check time: **{_hm(w['final_status_price_check_time'])}**",
              f"* Number of matches in window: {w['n_matches']} "
              f"({', '.join(m['label'] for m in w['matches'][:6])}{' ...' if w['n_matches'] > 6 else ''})", ""]
    else:
        L += ["* No main-tour singles match has a credible upcoming start time on this slate.", ""]
    unv = s.get("main_tour_status_unverified") or []
    if unv:
        L += [f"* **{len(unv)} main-tour match(es) have NO verified start status** "
              f"({', '.join(sorted({u['status'] for u in unv}))}): BET blocked until a live status check.", ""]
    L += [f"Slate built {s['built_at'][:16]}Z. Refresh due by: {_hm(s.get('refresh_due_by'))}. A slate built before a "
          "window's recommended time, or before a match's status changed, is NOT authoritative for that window.", ""]
    ds = s.get("discrepancy_sanity") or {}
    if ds:
        L += ["**Discrepancy sanity layer** (`" + ds.get("version", "") + "`): the model should usually sit close to the "
              "market. A big gap is a QUESTION -- stale or in-play quote? wrong player or side? thin data? -- before it is "
              "ever an edge. NORMAL <10pp: no restriction · REVIEW 10-15pp: context below · HIGH_REVIEW 15-25pp: explain "
              "the gap before any BET (`discrepancy_explanation`) · EXTREME >=25pp: DATA_WARNING / PASS UNTIL RECHECKED "
              "unless all nine Part J conditions hold, and even then only eligible for human review. Model probabilities "
              "are unchanged by this layer.", "",
              f"Bands (all priced contracts): {json.dumps(ds.get('counts_by_band'))}; match winners: "
              f"{json.dumps(ds.get('match_winner_counts_by_band'))}; quote freshness at build: "
              f"{json.dumps(ds.get('counts_by_freshness'))}.", ""]
    for x in s["matches"]:
        mc = x["model_context"]
        st = x.get("start") or {}
        L += [f"## {x['players']['a']} vs {x['players']['b']} -- {x['competition']} {x['round'] or ''}".rstrip(), "",
              f"**START STATUS: {st.get('start_status') or '--'}**" + ("" if st.get("bet_allowed", True) else " -- BET BLOCKED"),
              f"* Nominal schedule: {_hm(st.get('nominal_scheduled_start'))}"
              + (" (day placeholder, not a start time)" if st.get("nominal_is_placeholder") else ""),
              f"* Current expected start: {_hm(st.get('current_expected_start')) if st.get('current_expected_start') else 'UNKNOWN'}",
              f"* Source: {st.get('start_time_source') or 'none'}; confidence {st.get('start_time_confidence') or 'NONE'}",
              f"* First ball: {st.get('first_ball_status') or '--'}" + (f" ({st['first_ball_source']})" if st.get("first_ball_source") else ""),
              f"* Last status refresh: {_hm(st.get('start_time_last_checked')) if st.get('start_time_last_checked') else 'never (no live reading)'}",
              f"* Recommended handicap-by time: {_hm(st.get('recommended_handicap_by')) if st.get('recommended_handicap_by') else 'UNKNOWN'}",
              ""] + ([f"* Status notes: {'; '.join(st['status_reasons'])}", ""] if st.get("status_reasons") else []) + [
              f"{x['level_bucket']} ({x['level']}) · {x['surface'] or 'surface ?'} · scheduled {x['scheduled_start']} · "
              f"first ball: {x['first_ball']['status']} (source {x['first_ball']['source_coverage']}) · "
              f"match `{x['physical_match_id'] or x['match_key']}`", ""]
        L += ["| YES on | bid / ask (size) | mid | Gen-1 | Gen-2 | fair_v1 [env] | Bovada | Smarkets | consensus | triangulation | selector "
              "| MODEL-MARKET GAP | BAND | FRESHNESS | DATA QUALITY | EXTERNAL | IDENTITY |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in x["markets"]:
            if r["market_family"] != "MATCH_WINNER":
                continue
            k, mo, e = r["kalshi"], r["model"], r["external"] or {}
            env = mo.get("fair_v1_envelope") or [None, None]
            L.append(f"| {r['subject']} (`{r['ticker']}`) | {_c(k['bid'])} / {_c(k['ask'])} ({k['ask_size'] or 0:.0f}) | {_pct(k['mid'])} | "
                     f"{_pct(mo['gen1'])} | {_pct(mo['gen2'])} | {_pct(mo['fair_v1'])} [{_pct(env[0])}-{_pct(env[1])}] | "
                     f"{_pct(e.get('bovada'))} | {_pct(e.get('smarkets'))} | {_pct(e.get('consensus'))} | "
                     f"{e.get('triangulation') or '--'} | {mo.get('selector_v1') or '--'} | {_disc_cells(r)} |")
        if x.get("model_validity"):
            mv = x["model_validity"]
            L += ["", f"* **Model validity: GEN1 DOUBLES = {mv['gen1']}** -- {mv['reason']} Gen-1: --, Gen-2: --, "
                      "fair_v1: -- (no model evidence; prices only)"]
        sv, rs, rf = mc["serve_evidence"], mc["rating_state"], mc["recent_form_inputs"]
        L += ["", f"* Serve evidence (points): A {sv['player_a_points']}, B {sv['player_b_points']}; "
                  f"serve-point win A {_pct(rs['serve_point_win_a'])}, B {_pct(rs['serve_point_win_b'])}; "
                  f"Elo A {rs['elo_a']}, B {rs['elo_b']}; model uncertainty {mc['model_uncertainty']}",
              f"* Form inputs: days since last match A {rf['days_since_last_match_a']}, B {rf['days_since_last_match_b']}; "
              f"matches on record A {rf['matches_on_record_a']}, B {rf['matches_on_record_b']}; "
              f"data quality {mc['data_quality']['grade']}"]
        for r in x["markets"]:
            if r["market_family"] == "MATCH_WINNER" and DS.BAND_RANK.get(r.get("discrepancy_band"), -1) >= DS.BAND_RANK[DS.HIGH_REVIEW] \
                    and (r.get("model_market_gap_pp") or 0) > 0:
                L += [""] + DS.sanity_block_lines(r, subject=r["subject"])
        if mc.get("surface_adjustment"):
            L.append("* Surface-prior sensitivity (P(A) change): " + ", ".join(
                f"{k} {v:+.3f}" for k, v in mc["surface_adjustment"].items() if isinstance(v, float)))
        der = [r for r in x["markets"] if r["market_family"] != "MATCH_WINNER"]
        if der:
            priced = sorted([r for r in der if r["model_minus_mid"] is not None],
                            key=lambda r: -abs(r["model_minus_mid"]))
            L.append(f"* Derivatives listed: {len(der)} ({', '.join(x['available_expressions'])}); "
                     f"{sum(1 for r in der if r['model_probability_yes'] is not None)} carry a model probability")
            for r in priced:
                k = r["kalshi"]
                L.append(f"  * `{r['ticker']}` {r['description']}: {_c(k['bid'])}/{_c(k['ask'])} mid {_pct(k['mid'])}, "
                         f"model {_pct(r['model_probability_yes'])} ({r['model_probability_source']}) -- {_disc_inline(r)}")
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


def _hm(x) -> str:
    d = iso(x)
    return d.strftime("%Y-%m-%d %H:%MZ") if d else "--"


def _disc_cells(r) -> str:
    g = r.get("model_market_gap_pp")
    st = r.get("discrepancy_sanity_status")
    band = r.get("discrepancy_band") or "--"
    if st == DS.DATA_WARNING:
        band += " (DATA_WARNING)"
    return " | ".join([f"{g:+.1f} pp" if isinstance(g, (int, float)) else "--", band,
                       r.get("market_freshness_status") or "--",
                       f"{(r.get('discrepancy') or {}).get('evidence', {}).get('data_grade') or '?'} / {r.get('data_quality_status') or '--'}",
                       r.get("external_confirmation_status") or "--",
                       (r.get("identity_check_status") or "--").replace("IDENTITY_", "")])


def _disc_inline(r) -> str:
    g = r.get("model_market_gap_pp")
    return (f"gap {g:+.1f} pp, {r.get('discrepancy_band')}" if isinstance(g, (int, float)) else "gap --") + \
        f", {r.get('discrepancy_sanity_status')}, quote {r.get('market_freshness_status')}, " \
        f"identity {(r.get('identity_check_status') or '').replace('IDENTITY_', '')}, data {r.get('data_quality_status')}"


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
           "skipped": slate["counts"]["skipped_matches"], "sources": slate["sources"],
           "discrepancy_version": (slate.get("discrepancy_sanity") or {}).get("version"),
           "discrepancy_counts_by_band": (slate.get("discrepancy_sanity") or {}).get("counts_by_band"),
           "discrepancy_counts_by_status": (slate.get("discrepancy_sanity") or {}).get("counts_by_status"),
           "start_counts_by_status": (slate.get("start_time_reconciliation") or {}).get("counts_by_status"),
           "next_window_earliest": (slate.get("next_actionable_window") or {}).get("earliest_credible_first_ball"),
           "refresh_due_by": slate.get("refresh_due_by")}
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
