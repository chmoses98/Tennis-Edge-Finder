#!/usr/bin/env python3
"""Wave 4's working loop: capture an independent venue, line it up against Kalshi, record the difference.

Runs on a GitHub Actions runner (the research sandbox has no egress to either venue). One pass:

  1. fetch Bovada's public tennis coupon and write the raw bytes for evidence;
  2. parse it into ExternalMarketObservation rows -- de-vigged only where the whole market was present;
  3. read the latest Kalshi capture already on disk (carry-forward across the day's snapshots);
  4. map both sides to canonical physical matches through the SAME registry, refusing anything unsafe;
  5. build a reference value per (match, family, side) and compare it to the executable Kalshi ask;
  6. triangulate with our frozen fundamental model as a witness, never as the plaintiff;
  7. append every qualifying row to the append-only dislocation ledger.

Nothing here retunes a model. The fair-price layer, Gen-1, Gen-2 and selector_v1 are frozen for this
wave; this script reads them and does not fit anything.
"""
from __future__ import annotations

import argparse
import glob
import gzip
import json
import os
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone, date

HERE = os.path.dirname(os.path.abspath(__file__))
PROJ = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, PROJ)

from tennis_edge.external_market.bovada import SOURCE as BOVADA, event_index, parse_coupon  # noqa: E402
from tennis_edge.external_market.consensus import build_reference                            # noqa: E402
from tennis_edge.external_market.dislocation import (Dislocation, DislocationLedger,          # noqa: E402
                                                    KALSHI_LONE_OUTLIER, ScanPolicy, scan_gates,
                                                    triangulate)
from tennis_edge.external_market.mapping import MAPPED, audit, map_event, physical_key        # noqa: E402
from tennis_edge.external_market.schema import ExternalStore                                  # noqa: E402
from tennis_edge.identity.kalshi_map import KalshiPlayerMapper                                # noqa: E402
from tennis_edge.kalshi.families import SERIES                                                # noqa: E402
from tennis_edge.kalshi.markets import parse_market                                           # noqa: E402
from tennis_edge.pricing.competition import classify_competition                              # noqa: E402
from tennis_edge.pricing.fees import FeeSchedule, taker_fee                                    # noqa: E402

BOVADA_URL = ("https://www.bovada.lv/services/sports/event/coupon/events/A/description/tennis?lang=en")
UA = "tennis-edge-finder/1.0 (research; +https://github.com/chmoses98/Tennis-Edge-Finder)"
MATCH_SERIES = {tk for tk, (fam, tour, lvl, disc) in SERIES.items()
                if fam == "MATCH_WINNER" and disc == "singles" and tour in ("ATP", "WTA")}

#: the gates live in the library so the board and the tests share one copy
POLICY = ScanPolicy()
MAX_KALSHI_QUOTE_AGE_S = POLICY.max_kalshi_quote_age_s
MAX_EXTERNAL_STALENESS_S = POLICY.max_external_staleness_s


def _f(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fetch(url: str, timeout=40) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json,*/*"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def latest_kalshi_quotes(capture_root: str) -> dict:
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


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"))
    ap.add_argument("--external-store", default=os.path.join(PROJ, "data", "research", "external", "market"))
    ap.add_argument("--ledger", default=os.path.join(PROJ, "data", "research", "external", "dislocations"))
    ap.add_argument("--raw", default=os.path.join(PROJ, "data", "research", "external", "raw"))
    ap.add_argument("--asof", default=os.path.join(PROJ, "data", "processed", "asof"))
    ap.add_argument("--no-model", action="store_true", help="skip the model witness (no asof artifacts)")
    a = ap.parse_args()

    now = datetime.now(timezone.utc)
    stamp = now.strftime("%Y%m%dT%H%M%SZ")
    os.makedirs(a.raw, exist_ok=True)
    stats = {"generated_at": now.isoformat(), "run_id": stamp}

    # ---------------------------------------------------------------- 1/2. the external venue
    try:
        raw = fetch(BOVADA_URL)
    except (urllib.error.HTTPError, urllib.error.URLError, OSError) as e:
        print(f"::error::bovada fetch failed: {e}")
        json.dump({**stats, "error": str(e)}, open(os.path.join(a.raw, f"{stamp}.error.json"), "w"), indent=1)
        return 1
    raw_path = os.path.join(a.raw, f"{stamp}.bovada.json.gz")
    open(raw_path, "wb").write(gzip.compress(raw))
    payload = json.loads(raw.decode("utf-8", "replace"))
    obs, pstats = parse_coupon(payload, observed_at=now.isoformat(),
                               evidence_location=os.path.relpath(raw_path, PROJ), raw_bytes=raw)
    ExternalStore(a.external_store).append_many(obs)
    stats["external_parse"] = pstats

    # ---------------------------------------------------------------- 3. Kalshi
    quotes = latest_kalshi_quotes(a.capture)
    stats["kalshi_quotes_on_disk"] = len(quotes)

    # ---------------------------------------------------------------- 4. mapping, both sides, one registry
    from tennis_edge.models.state import load_state
    states = {t: load_state(os.path.join(PROJ, "data", "processed", f"ratings_{t}.json")) for t in ("ATP", "WTA")}
    mapper = KalshiPlayerMapper(states, cache_path=os.path.join(PROJ, "data", "research", "wave4_map_cache.json"))

    ext_index, ext_maps = event_index(payload), []
    ext_by_match = {}
    for e in ext_index:
        path = " ".join(e["path"]).lower()
        tour = "WTA" if ("wta" in path or "women" in path) else "ATP"
        me = map_event(mapper, source=BOVADA, source_event_id=e["source_event_id"], tour=tour,
                       name_a=e["a"], name_b=e["b"], start_utc=e["start_utc"])
        ext_maps.append(me)
        if me.status == MAPPED:
            ext_by_match.setdefault(me.physical_match_id, []).append((e, me))
    stats["external_mapping"] = audit(ext_maps)

    kal_events, kal_maps = {}, []
    for tk, m in quotes.items():
        if m.get("status") != "active" or tk.split("-")[0] not in MATCH_SERIES:
            continue
        kal_events.setdefault(m.get("event_ticker"), []).append(m)
    kal_by_match = {}
    for ev, ms in kal_events.items():
        pms = [(parse_market(m), m) for m in ms]
        pms = [x for x in pms if x[0].status == "PARSED"]
        sides = {pm.subject_is_a: (pm, m) for pm, m in pms}
        if True not in sides or False not in sides:
            continue
        pm_a, m_a = sides[True]
        pm_b, m_b = sides[False]
        info = classify_competition(pm_a.competition, pm_a.tour)
        tour = info["tour"] if info["tour"] in ("ATP", "WTA") else (
            "WTA" if pm_a.series_ticker.startswith(("KXWTA", "KXITFW")) else "ATP")
        sched = m_a.get("occurrence_datetime") or m_a.get("expected_expiration_time")
        me = map_event(mapper, source="kalshi", source_event_id=ev, tour=tour,
                       name_a=pm_a.subject, name_b=pm_b.subject, start_utc=sched)
        kal_maps.append(me)
        if me.status == MAPPED:
            kal_by_match[me.physical_match_id] = {
                "event": ev, "tour": tour, "level": info["level"], "start_utc": sched,
                "sides": [(pm_a, m_a, me.player_a_id), (pm_b, m_b, me.player_b_id)],
                "player_a_id": me.player_a_id, "player_b_id": me.player_b_id}
    stats["kalshi_mapping"] = audit(kal_maps)

    from tennis_edge.external_market.mapping import join_to_kalshi
    ext_simple = {k: {"start_utc": v[0][0]["start_utc"]} for k, v in ext_by_match.items()}
    joined_extra = join_to_kalshi(ext_simple, {k: {"start_utc": v["start_utc"]} for k, v in kal_by_match.items()})
    overlap = {k: v for k, v in kal_by_match.items() if k in ext_by_match}
    for k, (_krec, _erec, note) in joined_extra.items():
        if k not in overlap and k in kal_by_match:
            overlap[k] = kal_by_match[k]
    stats["matched_both_venues"] = len(overlap)
    stats["external_mapped_matches"] = len(ext_by_match)
    stats["kalshi_mapped_matches"] = len(kal_by_match)

    # ---------------------------------------------------------------- 5/6/7. reference, triangulate, ledger
    model_ok = not a.no_model and all(
        os.path.exists(os.path.join(a.asof, f"asof_{t}.json.gz")) for t in ("ATP", "WTA"))
    asof = {}
    if model_ok:
        from tennis_edge.models.asof import AsOfStates
        asof = {t: AsOfStates.load(os.path.join(a.asof, f"asof_{t}.json.gz")) for t in ("ATP", "WTA")}
    stats["model_witness_available"] = bool(model_ok)

    ledger = DislocationLedger(a.ledger)
    by_family_side = {}
    for o in obs:
        by_family_side.setdefault((o.source_event_id, o.market_family), []).append(o)

    rows, counts, skips = [], {}, {}
    for pid_match, krec in sorted(overlap.items()):
        ext_events = ext_by_match.get(pid_match) or []
        if not ext_events:
            continue
        e_idx, e_map = ext_events[0]
        ext_mw = [o for o in by_family_side.get((e_idx["source_event_id"], "MATCH_WINNER"), [])]
        if not ext_mw:
            skips["external_has_no_match_winner"] = skips.get("external_has_no_match_winner", 0) + 1
            continue
        # our model's probability that player A (the Kalshi A side) wins
        model_fair_a = None
        model_unc = None
        if model_ok:
            from tennis_edge.models.fair import PERTURBATIONS, compute_fair
            from tennis_edge.rules.formats import FormatResolutionError, resolve_format
            try:
                on = datetime.fromisoformat(str(krec["start_utc"]).replace("Z", "+00:00")).date()
            except (TypeError, ValueError):
                on = now.date()
            try:
                fmt = resolve_format(krec["tour"], krec["level"], on.year, None, "singles")
            except FormatResolutionError:
                fmt = None
            if fmt is not None:
                vals = []
                for cfg in PERTURBATIONS:
                    fr = compute_fair(asof[krec["tour"]], krec["player_a_id"], krec["player_b_id"],
                                      tour=krec["tour"], level=krec["level"], surface=None, fmt=fmt,
                                      on=on, cfg=cfg)
                    if fr is not None:
                        vals.append(fr.p_gen2_blend)
                if vals:
                    model_fair_a = vals[0]
                    model_unc = 0.5 * (max(vals) - min(vals))

        for pm, km, pid in krec["sides"]:
            ask, bid = _f(km.get("yes_ask_dollars")), _f(km.get("yes_bid_dollars"))
            size = _f(km.get("yes_ask_size_fp"))
            if ask is None or bid is None or not (0 < bid <= ask < 1):
                skips["kalshi_not_two_sided"] = skips.get("kalshi_not_two_sided", 0) + 1
                continue
            # which external side is this Kalshi side? match on the canonical player id we mapped
            want_a = pid == e_map.player_a_id
            side_name = e_idx["a"] if want_a else e_idx["b"]
            side_obs = [o for o in ext_mw if o.side == side_name]
            ref = build_reference(side_obs, now=now.isoformat(),
                                  max_source_staleness_s=MAX_EXTERNAL_STALENESS_S,
                                  max_capture_age_s=MAX_KALSHI_QUOTE_AGE_S)
            mid = 0.5 * (ask + bid)
            model_side = None if model_fair_a is None else (model_fair_a if pid == krec["player_a_id"]
                                                            else 1 - model_fair_a)
            tri = triangulate(mid, ref.value, model_side)
            fee = taker_fee(ask, 1.0, FeeSchedule())
            ext_edge = None if ref.value is None else ref.value - ask - fee
            try:
                q_age = (now - datetime.fromisoformat(km["captured_at"])).total_seconds()
            except (KeyError, TypeError, ValueError):
                q_age = None

            res = scan_gates(external_fair=ref.value, kalshi_bid=bid, kalshi_ask=ask, size=size,
                             quote_age_s=q_age, triangulation=tri["class"], external_edge=ext_edge,
                             policy=POLICY)
            gates, failed, decision = res["gates"], res["failed"], res["decision"]

            fors, against = [], []
            if ext_edge is not None:
                fors.append(f"external reference {ref.value*100:.1f}% against an ask of {ask*100:.0f}c "
                            f"leaves {ext_edge*100:+.1f}c after the fee")
            if tri["class"] == KALSHI_LONE_OUTLIER:
                fors.append("an independent venue and our fundamental model sit on the same side of the "
                            "Kalshi price")
            if ref.n_independent_groups:
                fors.append(f"{ref.n_independent_groups} independent witness(es): {', '.join(ref.groups)}")
            if failed:
                against.append("fails: " + ", ".join(failed))
            if ref.n_independent_groups < 2:
                against.append("a single external witness, and it is a recreational sportsbook rather "
                               "than a sharp one: this is two venues disagreeing, not proof of an error")
            if tri.get("model_overshoots_external"):
                against.append("our model disagrees with the external reference by more than 2c, so the "
                               "corroboration is directional only")
            against.append("Wave 3 found no subset where our own disagreement identified a Kalshi error; "
                           "the external hypothesis is untested until strict CLV accumulates")

            row = Dislocation(
                generated_at=now.isoformat(), physical_match_id=pid_match, kalshi_ticker=pm.ticker,
                kalshi_event=krec["event"], side=pm.subject, market_family="MATCH_WINNER",
                kalshi_bid=bid, kalshi_ask=ask, kalshi_mid=mid, kalshi_size=size,
                kalshi_spread=ask - bid, kalshi_fee=fee, kalshi_quote_age_s=q_age,
                external_sources=tuple(sorted({o.source for o in side_obs})),
                external_prices={o.source: o.devigged_probability for o in side_obs},
                external_raw={o.source: o.implied_probability for o in side_obs},
                external_fair=ref.value, reference_kind=ref.kind,
                reference_dispersion=ref.dispersion,
                external_quote_age_s=(side_obs[0].staleness_seconds if side_obs else None),
                n_independent_groups=ref.n_independent_groups,
                model_fair=model_side, model_uncertainty=model_unc,
                external_vs_kalshi=tri["ext_vs_kalshi"], model_vs_kalshi=tri["model_vs_kalshi"],
                model_vs_external=tri["model_vs_external"], triangulation=tri["class"],
                external_edge=ext_edge, first_ball_classification="START_UNKNOWN",
                first_ball_confidence="UNKNOWN", strict_pregame=False,
                decision=decision,
                reason_for="; ".join(fors) or "nothing", reason_against="; ".join(against),
                selector_version="external_v1")
            ledger.append(row)
            rows.append(row)
            counts[row.decision] = counts.get(row.decision, 0) + 1
            counts["tri:" + row.triangulation] = counts.get("tri:" + row.triangulation, 0) + 1

    stats["rows"] = len(rows)
    stats["counts"] = counts
    stats["skips"] = skips
    out_dir = os.path.join(PROJ, "data", "research", "external", "scans")
    os.makedirs(out_dir, exist_ok=True)
    json.dump(stats, open(os.path.join(out_dir, f"scan_{stamp}.json"), "w"), indent=1, default=str)
    print(json.dumps(stats, indent=1, default=str))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
