#!/usr/bin/env python3
"""Frozen MODEL 4 (market_conditioned_v1 + gen2_dyn_hier_sr_v1), run live on LISTED Kalshi derivatives.

For every physical match on the live board that has at least one listed EXACT_SET_SCORE, GAME_SPREAD or
TOTAL_GAMES contract, this writes what the two frozen lanes of the Wave 2 study said about each listed
contract, at the moment it said it:

  FUNDAMENTAL        one distribution from the Gen-2 point probabilities (the frozen study's comparator)
  MARKET-CONDITIONED keeps the Gen-2 service LEVEL and reproduces the de-vigged Kalshi match-winner price

Nothing is fitted. The Gen-2 point probabilities come from the walk-forward as-of artifact read strictly
before the match date, with the artifact's own frozen Gen-2 configuration; the conditioning is
`tennis_edge.models.market_conditioned.conditioned_distribution`, unchanged; each contract is read off
the distribution by the frozen pricer `tennis_edge.pricing.payoffs.price_market`.

Operationalisation fixed here, before any prospective outcome was read, and recorded on every row:
the Wave 2 study de-vigged a bookmaker's two OFFERED prices proportionally; the Kalshi analogue is the two
match-winner YES ASKS, de-vigged proportionally. Bids and mids are stored beside it so any other reading
remains auditable. A match whose match-winner quote is not two-sided is recorded with no conditioned
lane rather than silently conditioned on something else.

Only contracts Kalshi actually lists are recorded. Nothing here expresses a wager.
"""
from __future__ import annotations

import argparse
import glob
import gzip
import json
import os
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.firstball.started import match_code, matches_already_started            # noqa: E402
from tennis_edge.identity.kalshi_map import KalshiPlayerMapper                             # noqa: E402
from tennis_edge.kalshi.families import SERIES                                             # noqa: E402
from tennis_edge.kalshi.markets import parse_market                                        # noqa: E402
from tennis_edge.models.market_conditioned import MODEL_VERSION as MC_VERSION, conditioned_distribution  # noqa: E402
from tennis_edge.pricing.competition import classify_competition                           # noqa: E402
from tennis_edge.pricing.fees import FeeSchedule, taker_fee                                # noqa: E402
from tennis_edge.pricing.payoffs import PricingError, price_market                         # noqa: E402
from tennis_edge.producers.records import ProducerStore, code_sha, ensure_experiment_starts  # noqa: E402
from tennis_edge.rules.formats import FormatResolutionError, resolve_format                # noqa: E402
from tennis_edge.sim.analytic import match_distribution                                    # noqa: E402

PRODUCER = "model4_board_v1"
FUND_VERSION = "gen2_dyn_hier_sr_v1"
DERIV_FAMILIES = ("EXACT_SET_SCORE", "GAME_SPREAD", "TOTAL_GAMES")
DEVIG_METHOD = "proportional over the two match-winner YES asks"
MW_SERIES = {tk for tk, (fam, tour, lvl, disc) in SERIES.items()
             if fam == "MATCH_WINNER" and disc == "singles" and tour in ("ATP", "WTA")}
DERIV_SERIES = {tk for tk, (fam, tour, lvl, disc) in SERIES.items() if fam in DERIV_FAMILIES and disc == "singles"}


def _f(x):
    try:
        v = float(x)
    except (TypeError, ValueError):
        return None
    return v if 0.0 < v < 1.0 else None


def latest_quotes(capture_root: str) -> dict:
    """Carry-forward board from the latest capture day (the capture writes only changed markets)."""
    days = sorted(d for d in glob.glob(os.path.join(capture_root, "*")) if os.path.isdir(d))
    out = {}
    if not days:
        return out
    for f in sorted(glob.glob(os.path.join(days[-1], "*.quotes.jsonl.gz"))):
        with gzip.open(f, "rt") as fh:
            for line in fh:
                if line.strip():
                    m = json.loads(line)
                    out[m["ticker"]] = m
    return out


def summarise(d) -> dict:
    return {"p_match_a": d.p_match,
            "set_score": {f"{a}-{b}": v for (a, b), v in sorted(d.set_score.items())},
            "e_game_diff_a": sum(k * v for k, v in d.game_diff.items()),
            "e_total_games": sum(k * v for k, v in d.total_games.items())}


def build_rows(quotes: dict, *, asof: dict, mapper, surface_of, started: set, now: datetime, sha: str) -> tuple[list, dict]:
    """Pure function of its inputs: every listed derivative contract on a mapped, not-started match."""
    by_code: dict = {}
    for tk, m in quotes.items():
        if m.get("status") != "active":
            continue
        series = tk.split("-")[0]
        if series in MW_SERIES or series in DERIV_SERIES:
            by_code.setdefault(match_code(m.get("event_ticker") or ""), []).append(m)
    rows, skipped = [], {}

    def skip(k):
        skipped[k] = skipped.get(k, 0) + 1

    for code, ms in sorted(by_code.items()):
        parsed = [(parse_market(m), m) for m in ms]
        parsed = [(pm, m) for pm, m in parsed if pm.status == "PARSED"]
        derivs = [(pm, m) for pm, m in parsed if pm.family in DERIV_FAMILIES]
        mws = [(pm, m) for pm, m in parsed if pm.family == "MATCH_WINNER" and pm.series_ticker in MW_SERIES]
        if not derivs:
            continue                                   # no listed derivative: nothing to record, by design
        if code in started:
            skip("first_ball_already_observed"); continue
        sides = {pm.subject_is_a: (pm, m) for pm, m in mws}
        if True not in sides or False not in sides:
            skip("no_match_winner_pair_for_identity"); continue
        pm_a, m_a = sides[True]
        pm_b, m_b = sides[False]
        info = classify_competition(pm_a.competition, pm_a.tour)
        tour = info["tour"] if info["tour"] in ("ATP", "WTA") else (
            "WTA" if pm_a.series_ticker.startswith(("KXWTA", "KXITFW")) else "ATP")
        sched = m_a.get("occurrence_datetime") or m_a.get("expected_expiration_time")
        on = datetime.fromisoformat(sched.replace("Z", "+00:00")).date() if sched else now.date()
        ma = mapper.resolve(tour, pm_a.subject, pm_a.competitor_id, on)
        mb = mapper.resolve(tour, pm_b.subject, pm_b.competitor_id, on)
        if ma["status"] != "MAPPED" or mb["status"] != "MAPPED":
            skip("unmapped_identity"); continue
        try:
            fmt = resolve_format(tour, info["level"], on.year,
                                 info["competition"] if info["level"] == "GRAND_SLAM" else None, "singles")
        except FormatResolutionError:
            skip("format_unresolved"); continue
        st = asof[tour]
        pa_id, pb_id = ma["player_id"], mb["player_id"]
        if not st.state(pa_id, on) or not st.state(pb_id, on):
            skip("no_rating_state"); continue
        surface = surface_of(pm_a.competition, info["surface_hint"])
        g2 = st.gen2_state([pa_id, pb_id], on)
        gpa, gpb = g2.predict_point_probs(pa_id, pb_id, tour, info["level"], surface)
        d_fund = match_distribution(gpa, gpb, fmt)
        ask_a, ask_b = _f(m_a.get("yes_ask_dollars")), _f(m_b.get("yes_ask_dollars"))
        bid_a, bid_b = _f(m_a.get("yes_bid_dollars")), _f(m_b.get("yes_bid_dollars"))
        mw_two_sided = all(v is not None for v in (ask_a, ask_b, bid_a, bid_b))
        p_mkt_a = (ask_a / (ask_a + ask_b)) if (ask_a and ask_b) else None
        d_mc, cond = (conditioned_distribution(p_mkt_a, gpa, gpb, fmt) if p_mkt_a is not None else (None, None))
        common = {
            "producer": PRODUCER, "code_sha": sha, "predicted_at": now.isoformat(),
            "physical_match_id": f"{tour}:{min(pa_id, pb_id)}:{max(pa_id, pb_id)}:{on}",
            "match_code": code, "tour": tour, "level": info["level"], "competition": pm_a.competition,
            "surface": surface, "format": fmt.name, "best_of": fmt.best_of, "match_date": str(on),
            "player_a_id": pa_id, "player_b_id": pb_id, "scheduled_start": sched,
            "model_version": MC_VERSION, "fundamental_version": FUND_VERSION,
            "asof_base_date": str(st.base_date), "gen2_pa": gpa, "gen2_pb": gpb,
            "gen2_evidence_a": g2.evidence(pa_id), "gen2_evidence_b": g2.evidence(pb_id),
            "conditioning": {"mw_ticker_a": pm_a.ticker, "mw_ticker_b": pm_b.ticker,
                             "ask_a": ask_a, "ask_b": ask_b, "bid_a": bid_a, "bid_b": bid_b,
                             "two_sided": mw_two_sided, "devig_method": DEVIG_METHOD,
                             "p_market_a": p_mkt_a,
                             "quote_captured_at": max(m_a.get("captured_at") or "", m_b.get("captured_at") or "") or None,
                             "service_level": cond.service_level if cond else None},
            "fundamental_distribution": summarise(d_fund),
            "conditioned_distribution": summarise(d_mc) if d_mc is not None else None,
            "first_ball_status_at_prediction": "NOT_OBSERVED_STARTED",
        }
        for pm, m in derivs:
            if not (same_player(pm.player_a, pm_a.player_a) and same_player(pm.player_b, pm_a.player_b)):
                skip("orientation_mismatch"); continue
            try:
                p_f = price_market(pm, d_fund).fair_yes
                p_c = price_market(pm, d_mc).fair_yes if d_mc is not None else None
            except PricingError:
                skip("pricing_error"); continue
            bid, ask = _f(m.get("yes_bid_dollars")), _f(m.get("yes_ask_dollars"))
            rows.append({**common, "ticker": pm.ticker, "event": pm.event_ticker, "market_family": pm.family,
                         "subject": pm.subject, "subject_is_a": pm.subject_is_a, "line": pm.line,
                         "exact_score": list(pm.exact_score) if pm.exact_score else None,
                         "fundamental_probability": p_f, "conditioned_probability": p_c,
                         "kalshi_bid": bid, "kalshi_ask": ask,
                         "spread": (ask - bid) if (bid is not None and ask is not None) else None,
                         "fee": taker_fee(ask, 1.0, FeeSchedule()) if ask is not None else None,
                         "displayed_ask_size": _f_size(m.get("yes_ask_size_fp")),
                         "displayed_bid_size": _f_size(m.get("yes_bid_size_fp")),
                         "quote_captured_at": m.get("captured_at")})
    return rows, skipped


def same_player(a: str, b: str) -> bool:
    """Derivative rules text names players in full ('Coleman Wong'), match-winner text by surname
    ('Wong'). Same side iff one normalised name equals, or ends with, the other as whole words. Anything
    else -- including the two names in the opposite order -- is refused, never flipped."""
    from tennis_edge.identity.names import normalize_name
    x, y = normalize_name(a or ""), normalize_name(b or "")
    if not x or not y:
        return False
    return x == y or x.endswith(" " + y) or y.endswith(" " + x)


def _f_size(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"))
    ap.add_argument("--asof", default=os.path.join(PROJ, "data", "processed", "asof"))
    ap.add_argument("--store", default=os.path.join(PROJ, "data", "research", "frozen_producers", "model4"))
    ap.add_argument("--starts", default=os.path.join(PROJ, "data", "research", "experiment_starts"))
    ap.add_argument("--firstball", default=os.path.join(PROJ, "data", "firstball", "store"))
    ap.add_argument("--candidates", default=os.path.join(PROJ, "data", "research", "edge_candidates"))
    a = ap.parse_args()

    import pandas as pd
    from tennis_edge.models.asof import AsOfStates
    from tennis_edge.models.state import load_state
    from tennis_edge.pricing.competition import build_surface_lookup, lookup_surface

    now = datetime.now(timezone.utc)
    quotes = latest_quotes(a.capture)
    if not quotes:
        print("::warning::model4: no capture on disk"); return 0
    states = {t: load_state(os.path.join(PROJ, "data", "processed", f"ratings_{t}.json")) for t in ("ATP", "WTA")}
    asof = {t: AsOfStates.load(os.path.join(a.asof, f"asof_{t}.json.gz")) for t in ("ATP", "WTA")}
    mapper = KalshiPlayerMapper(states, cache_path=os.path.join(PROJ, "data", "research", "model4_map_cache.json"))
    mtab = pd.read_parquet(os.path.join(PROJ, "data", "processed", "matches.parquet"),
                           columns=["tourney_name", "surface", "season"])
    lookup = build_surface_lookup(mtab)
    sha = code_sha(PROJ)
    rows, skipped = build_rows(quotes, asof=asof, mapper=mapper,
                               surface_of=lambda comp, hint: lookup_surface(comp, hint, lookup)[0],
                               started=matches_already_started(a.firstball, now), now=now, sha=sha)
    store = ProducerStore(a.store)
    for r in rows:
        store.append(r)
    # the producer ran; its effective start is fixed by its first production run, rows or not: "Kalshi
    # listed nothing qualifying" is a valid outcome, a dead producer is not
    cdefs = {}
    for fn in glob.glob(os.path.join(a.candidates, "*.json")):
        c = json.load(open(fn)); cdefs[c["candidate_id"]] = c
    ensure_experiment_starts(a.starts, PRODUCER, started_at=now.isoformat(), main_sha=sha,
                             candidate_defs=cdefs, producer_version=f"{PRODUCER}@{sha[:12]}")
    hb = {"producer": PRODUCER, "ran_at": now.isoformat(), "code_sha": sha, "rows": len(rows),
          "matches": len({r["match_code"] for r in rows}),
          "by_family": {f: sum(1 for r in rows if r["market_family"] == f) for f in DERIV_FAMILIES},
          "skipped": skipped, "authority": "RESEARCH_ONLY_NO_REAL_MONEY"}
    write_heartbeat(os.path.dirname(a.store), hb)
    print(json.dumps(hb, indent=1))
    return 0


def write_heartbeat(root: str, hb: dict) -> None:
    """Append-only run log: proves the producer ran even when it had nothing to record."""
    os.makedirs(root, exist_ok=True)
    with open(os.path.join(root, "heartbeats.jsonl"), "a") as f:
        f.write(json.dumps(hb, default=str) + "\n")


if __name__ == "__main__":
    raise SystemExit(main())
