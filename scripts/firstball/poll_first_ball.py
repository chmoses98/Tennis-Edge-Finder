#!/usr/bin/env python3
"""Phase 3: adaptive polling for ACTUAL first ball, and the truth it produces.

One process per conductor run. Each pass:
  1. rebuild the watchlist from the Kalshi discovery snapshot (open, match-scope events with both names);
  2. fetch each enabled live-score feed ONCE -- day-level and live-level feeds cover every match at once,
     so the request count depends on the number of SOURCES, not the number of matches;
  3. map feed matches onto our matches, refusing ambiguous pairs;
  4. append one immutable observation per mapped match;
  5. re-derive FirstBallTruth from all observations for that match and append a new derivation version
     ONLY when the answer actually changed;
  6. stop watching a match once its truth is strict-eligible (A/B) or a walkover is confirmed.

Cadence adapts to the watchlist, not to the clock: 60 s when any match is near its expected start (or is
an ITF/Challenger event whose nominal time is not a start time at all), 300 s when something is within
hours, 900 s otherwise.
"""
from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone, timedelta, date

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from tennis_edge.firstball.probe import fetch                              # noqa: E402
from tennis_edge.firstball.sources import REGISTRY                         # noqa: E402
from tennis_edge.firstball.mapping import OurMatch, map_all                # noqa: E402
from tennis_edge.firstball.watchlist import build_watchlist, poll_interval # noqa: E402
from tennis_edge.firstball.store import FirstBallStore                     # noqa: E402
from tennis_edge.firstball.truth import FirstBallObservation               # noqa: E402
from tennis_edge.firstball.reconcile import reconcile                      # noqa: E402

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DEFAULT_SOURCES = "espn_atp,espn_wta"


def latest_discovery(root=None):
    root = root or os.path.join(PROJ, "data", "kalshi", "discovery")
    runs = sorted(glob.glob(os.path.join(root, "*", "summary.json")))
    return os.path.dirname(runs[-1]) if runs else None


def same_answer(a, b) -> bool:
    """Has the ANSWER changed, or only the running lower bound?

    While a match has not started, every pass pushes the lower bound forward by one poll interval, which
    is real information but is not an answer about the first ball -- and it is always recomputable from
    the observations, which are kept. Writing a new derivation version for it every sixty seconds would
    bury the versions that mean something. So a truth with no upper bound is considered unchanged as long
    as its confidence, contradiction status and walkover status are unchanged; the moment an upper bound
    appears (play observed) or any of those change, the new derivation is written.
    """
    if a is None or b is None:
        return False
    if (a.confidence, a.contradiction_status, a.no_play) != (b.confidence, b.contradiction_status, b.no_play):
        return False
    if a.upper_bound_utc is None and b.upper_bound_utc is None:
        return True
    return a.lower_bound_utc == b.lower_bound_utc and a.upper_bound_utc == b.upper_bound_utc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--discovery", default=None)
    ap.add_argument("--store", default=os.path.join(PROJ, "data", "firstball", "store"))
    ap.add_argument("--capture", default=os.path.join(PROJ, "data", "kalshi", "capture"),
                    help="freshest capture pass defines the live open universe; discovery only supplies names")
    ap.add_argument("--sources", default=DEFAULT_SOURCES)
    ap.add_argument("--minutes", type=float, default=55.0)
    ap.add_argument("--max-passes", type=int, default=0, help="0 = unlimited within --minutes")
    ap.add_argument("--min-interval", type=int, default=45, help="floor on the adaptive cadence, seconds")
    ap.add_argument("--once", action="store_true")
    ap.add_argument("--dry-run", action="store_true", help="do not write to the store")
    a = ap.parse_args()

    disc = a.discovery or latest_discovery()
    if not disc:
        print("::warning::no discovery snapshot available; nothing to watch")
        return 0
    adapters = [REGISTRY[s] for s in a.sources.split(",") if s in REGISTRY]
    if not adapters:
        print(f"::error::no known sources in {a.sources!r} (known: {sorted(REGISTRY)})")
        return 2
    store = FirstBallStore(a.store)
    end = time.time() + a.minutes * 60
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    stats = {"run_id": run_id, "started_at": datetime.now(timezone.utc).isoformat(), "passes": 0,
             "requests": 0, "observations": 0, "truths_written": 0, "sources": [x.id for x in adapters],
             "resolved": {}, "http": {}}
    resolved: set[str] = {mid for mid, t in store.latest_truths().items() if t.strict_eligible}
    cache_headers: dict[str, dict] = {}
    last_parse: dict[str, tuple] = {}

    while True:
        now = datetime.now(timezone.utc)
        items, diag = build_watchlist(disc, now=now, capture_root=a.capture)
        items = [it for it in items if it.match_id not in resolved]
        interval, tiers = poll_interval(items, now)
        interval = max(interval, a.min_interval)
        print(f"[{now:%H:%M:%S}] watch={len(items)} tiers={tiers} interval={interval}s "
              f"(discovery {os.path.basename(disc)}, {diag})", flush=True)

        feed = []
        for ad in adapters:
            # A board that spans the whole tournament needs ONE request. For a feed keyed by local date,
            # also ask for tomorrow: a match at 23:40Z sits on tomorrow's board and dropping it would be a
            # silent hole at midnight.
            dates = [now.date()] if getattr(ad, "board_spans_tournament", False) else \
                    [now.date(), (now + timedelta(days=1)).date()]
            urls, seen = [], set()
            for d in dates:
                for u in ad.endpoints(d):
                    if u not in seen:
                        seen.add(u)
                        urls.append(u)
            for url in urls:
                # Conditional GET. These boards are megabytes; re-downloading an unchanged one every
                # 60 s would be rude and pointless, and a 304 is itself evidence that nothing moved.
                rec = fetch(url, accept="application/json", referer=getattr(ad, "referer", ""),
                            extra_headers=cache_headers.get(url) or {})
                stats["requests"] += 1
                code = str(rec.get("status"))
                stats["http"][code] = stats["http"].get(code, 0) + 1
                body = rec.pop("_body", b"")
                if rec.get("status") == 304 and url in last_parse:
                    got, digest = last_parse[url]
                    feed.extend((m, digest, url) for m in got)
                    print(f"    {ad.id} {url[-46:]} -> 304 not modified ({len(got)} cached)", flush=True)
                    continue
                if rec.get("status") != 200 or not body:
                    print(f"    {ad.id} {url[-52:]} -> {rec.get('status')} {rec.get('error','')[:60]}", flush=True)
                    continue
                try:
                    payload = json.loads(body.decode("utf-8", "replace"))
                except ValueError as e:
                    print(f"    {ad.id} unparseable payload: {e}", flush=True)
                    continue
                got = ad.parse(payload)
                digest = hashlib.sha256(body).hexdigest()
                last_parse[url] = (got, digest)
                h = {}
                if rec.get("etag"):
                    h["If-None-Match"] = rec["etag"]
                if rec.get("last_modified"):
                    h["If-Modified-Since"] = rec["last_modified"]
                cache_headers[url] = h
                for m in got:
                    feed.append((m, digest, url))
                print(f"    {ad.id} {url[-46:]} -> {len(got)} matches ({len(body)//1024} KiB)", flush=True)

        if items and feed:
            mp, mdiag = map_all([OurMatch(it.match_id, it.player_a, it.player_b, it.scheduled_utc, it.doubles)
                                 for it in items], [m for m, _, _ in feed])
            by_key = {(m.source, m.source_match_id): (m, h, u) for m, h, u in feed}
            observed_at = datetime.now(timezone.utc)
            for mid, mapping in mp.items():
                if mapping.status not in ("MATCHED", "WEAK"):
                    continue
                sm, digest, url = by_key[(mapping.source, mapping.source_match_id)]
                obs = FirstBallObservation(
                    match_id=mid, source=sm.source, authority=getattr(REGISTRY.get(sm.source), "authority", "secondary"),
                    observed_at_utc=observed_at, state=sm.state, source_match_id=sm.source_match_id,
                    source_status=sm.source_status, source_event_timestamp=sm.scheduled_utc,
                    source_time_interpretation=sm.time_interpretation, explicit_start_utc=sm.claimed_start_utc,
                    games_played=sm.games_played, payload_hash=digest,
                    independence_group=getattr(REGISTRY.get(sm.source), "independence_group", "") or sm.source,
                    raw_evidence_location=f"firstball/poll/{run_id}", mapping_status=mapping.status,
                    mapping_score=mapping.score)
                if not a.dry_run:
                    store.add_observation(obs)
                stats["observations"] += 1
                prev = store.latest_truths().get(mid)
                t = reconcile(mid, store.observations(mid), now=observed_at,
                              derivation_version=(prev.derivation_version + 1) if prev else 1)
                if not same_answer(prev, t):
                    if not a.dry_run:
                        store.add_truth(t)
                    stats["truths_written"] += 1
                    print(f"      TRUTH {mid} {t.confidence} bracket={t.bracket_seconds} "
                          f"{t.derivation_method} {t.contradiction_status}", flush=True)
                if t.strict_eligible:
                    resolved.add(mid)
                    stats["resolved"][mid] = {"confidence": t.confidence, "bracket_s": t.bracket_seconds,
                                              "first_ball": t.actual_first_ball_at_utc.isoformat() if t.actual_first_ball_at_utc else None,
                                              "no_play": t.no_play}
            stats.setdefault("mapping", {})
            for k, v in mdiag["counts"].items():
                stats["mapping"][k] = stats["mapping"].get(k, 0) + v
            # keep WHY a pair was refused: a large AMBIGUOUS count is fail-closed behaviour, but it is
            # only diagnosable if the reason travels with the number
            samples = stats.setdefault("mapping_refusals", {})
            for mid, m in mp.items():
                if m.status in ("AMBIGUOUS", "WEAK") and m.reason and mid not in samples:
                    samples[mid] = {"status": m.status, "reason": m.reason,
                                    "score": round(m.score, 3), "runner_up": round(m.runner_up, 3),
                                    "source": m.source}
                if len(samples) >= 25:
                    break

        stats["passes"] += 1
        if a.once or (a.max_passes and stats["passes"] >= a.max_passes) or time.time() + interval > end:
            break
        time.sleep(interval)

    stats["finished_at"] = datetime.now(timezone.utc).isoformat()
    os.makedirs(a.store, exist_ok=True)
    with open(os.path.join(a.store, f"poll_{run_id}.json"), "w") as f:
        json.dump(stats, f, indent=1, default=str)
    print(json.dumps(stats, indent=1, default=str)[:3000])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
