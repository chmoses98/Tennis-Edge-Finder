"""Which matches are worth polling for a first ball, and how urgently.

The watchlist is built from the Kalshi discovery snapshot: every OPEN, match-scope market is grouped by
event, and an event joins the list when both competitors' full names can be recovered from its markets.
Without both names there is nothing to map onto a live-score feed, so such events are reported as a
coverage gap rather than silently skipped.

Urgency tiers exist because the nominal time means different things at different levels:

  RELIABLE nominal (Grand Slam, Masters, Tour 250/500, team events) -- the scheduled time is a real
  scheduled time, so polling can be cheap until it approaches.

  UNRELIABLE nominal (ITF, Challenger, qualifying) -- on this exchange the nominal time routinely falls
  AFTER the market closes, so it is not a start time at all. For these the only safe assumption is that
  play may begin at any point in the window, and they are polled at the medium tier throughout it. This
  is the opposite of the usual optimisation: the levels with the worst metadata get the most attention.
"""
from __future__ import annotations

import glob
import json
import os
from dataclasses import dataclass, asdict
from datetime import datetime, timezone, timedelta

RELIABLE_NOMINAL_LEVELS = ("GRAND_SLAM", "MASTERS_1000", "TOUR_500_250", "TOUR_FINALS", "OLYMPICS", "TEAM")

#: Levels a WIRED first-ball source actually covers. This is NOT the same thing as "the nominal time is
#: reliable", and conflating the two makes the coverage metric lie. Membership is evidence-based: ESPN's
#: league index carries atp and wta only (atp-challenger returns HTTP 400), and its WTA board was observed
#: carrying WTA 125 matches on 2026-09-11. Everything absent here has no first-ball source at all and is
#: expected to stay START_UNKNOWN -- see docs/FIRST_BALL_SOURCES.md.
SOURCE_COVERED_LEVELS = ("GRAND_SLAM", "MASTERS_1000", "TOUR_500_250", "TOUR_FINALS", "OLYMPICS", "TEAM",
                         "WTA_125")

TIER_HOT, TIER_WARM, TIER_COLD = "HOT", "WARM", "COLD"
TIER_SECONDS = {TIER_HOT: 60, TIER_WARM: 300, TIER_COLD: 900}


@dataclass(frozen=True)
class WatchItem:
    match_id: str
    player_a: str
    player_b: str
    doubles: bool
    scheduled_utc: datetime | None
    nominal_reliable: bool
    tour: str
    level: str
    competition: str
    tickers: tuple

    def tier(self, now: datetime, observed_state: str | None = None) -> str:
        """How urgently to poll this match.

        `observed_state` is what a live-score source last said about it, and it dominates the schedule.
        A match we have SEEN still not started, whose nominal time has already passed, is the single most
        urgent thing on the board: it can begin at any second and its schedule has already been proven
        worthless. Tiering that case off the nominal alone put a delayed Grand Slam semifinal on a
        five-minute cadence on 2026-09-11 and cost a confidence-B bracket by 61 seconds -- the exact
        failure this wave exists to prevent.
        """
        if observed_state in ("IN", "POST", "NO_PLAY"):
            return TIER_COLD                       # nothing left to bracket; the poller drops it anyway
        dt = (self.scheduled_utc - now).total_seconds() if self.scheduled_utc else None
        if observed_state == "PRE" and (dt is None or dt <= 1800):
            return TIER_HOT                        # seen not-started, and due or overdue
        if dt is None:
            return TIER_WARM
        if not self.nominal_reliable:
            # the nominal is not a start time; play may already have begun, so stay warm across the window
            return TIER_HOT if -3600 <= dt <= 3 * 3600 else TIER_WARM
        if -1800 <= dt <= 3600:
            return TIER_HOT
        if -3 * 3600 <= dt <= 6 * 3600:
            return TIER_WARM
        return TIER_COLD

    def to_dict(self):
        d = asdict(self)
        d["scheduled_utc"] = self.scheduled_utc.isoformat() if self.scheduled_utc else None
        d["tickers"] = list(self.tickers)
        return d


def _parse_ts(v):
    if not v:
        return None
    try:
        return datetime.fromisoformat(str(v).replace("Z", "+00:00"))
    except ValueError:
        return None


def _fresh_open_tickers(capture_root: str | None, now: datetime, max_age_min: int = 45):
    """Tickers still open in the freshest capture pass, or None when no fresh pass is available.

    A discovery snapshot can be many hours old, and its 'open' markets include matches that have since
    been played and settled. Watching those wastes polling on matches whose first ball is already in the
    past, and -- worse -- produces one-sided C brackets that look like evidence. The capture conductor
    republishes the open universe every ten minutes, so when a recent pass exists it is the live
    universe and the discovery snapshot is only used for names and nominal times.
    """
    import glob as _glob
    import gzip as _gzip
    if not capture_root or not os.path.isdir(capture_root):
        return None
    files = sorted(_glob.glob(os.path.join(capture_root, "*", "*.quotes.jsonl.gz")))
    if not files:
        return None
    tickers, newest = set(), None
    for f in files[-2:]:
        try:
            with _gzip.open(f, "rt") as fh:
                for line in fh:
                    line = line.strip()
                    if not line:
                        continue
                    r = json.loads(line)
                    if r.get("ticker"):
                        tickers.add(r["ticker"])
                    ts = r.get("captured_at")
                    if ts and (newest is None or ts > newest):
                        newest = ts
        except (OSError, ValueError):
            continue
    if not tickers or not newest:
        return None
    try:
        age = (now - datetime.fromisoformat(newest.replace("Z", "+00:00"))).total_seconds() / 60
    except ValueError:
        return None
    return tickers if age <= max_age_min else None


def build_watchlist(discovery_dir: str, *, now: datetime | None = None, capture_root: str | None = None,
                    lookback_hours: int = 6, horizon_hours: int = 14) -> tuple[list[WatchItem], dict]:
    from tennis_edge.kalshi.markets import parse_market
    from tennis_edge.pricing.competition import classify_competition
    now = now or datetime.now(timezone.utc)
    lo, hi = now - timedelta(hours=lookback_hours), now + timedelta(hours=horizon_hours)

    fresh = _fresh_open_tickers(capture_root, now)
    by_event: dict[str, list] = {}
    raw_by_ticker: dict[str, dict] = {}
    for p in glob.glob(os.path.join(discovery_dir, "markets", "*.json")):
        for m in json.load(open(p)).get("open", {}).get("markets") or []:
            pm = parse_market(m)
            if pm.status != "PARSED" or pm.scope != "MATCH":
                continue
            by_event.setdefault(pm.event_ticker, []).append(pm)
            raw_by_ticker[pm.ticker] = m

    items, diag = [], {"events": len(by_event), "no_names": 0, "outside_window": 0, "selected": 0,
                       "closed_since_discovery": 0,
                       "universe": "freshest_capture" if fresh is not None else "discovery_snapshot"}
    for ev, pms in by_event.items():
        names = {True: None, False: None}
        for pm in pms:
            if pm.subject and pm.subject_is_a is not None:
                names[pm.subject_is_a] = names[pm.subject_is_a] or pm.subject
        if not names[True] or not names[False]:
            diag["no_names"] += 1
            continue
        if fresh is not None and not any(pm.ticker in fresh for pm in pms):
            diag["closed_since_discovery"] += 1
            continue
        head = pms[0]
        info = classify_competition(head.competition, head.tour)
        raw = raw_by_ticker.get(head.ticker, {})
        sched = _parse_ts(raw.get("occurrence_datetime") or raw.get("expected_expiration_time"))
        reliable = info["level"] in RELIABLE_NOMINAL_LEVELS
        if sched is not None and not (lo <= sched <= hi):
            diag["outside_window"] += 1
            continue
        items.append(WatchItem(match_id=ev, player_a=names[True], player_b=names[False],
                               doubles=(info["discipline"] != "singles" or head.discipline != "singles"),
                               scheduled_utc=sched, nominal_reliable=reliable, tour=info["tour"],
                               level=info["level"], competition=head.competition,
                               tickers=tuple(sorted(pm.ticker for pm in pms))))
    diag["selected"] = len(items)
    return items, diag


def poll_interval(items: list[WatchItem], now: datetime | None = None,
                  states: dict | None = None) -> tuple[int, dict]:
    """Cadence for the next pass: the most urgent tier any watched match is in.

    `states` maps match_id -> the last state a live-score source reported, so that what we have actually
    SEEN outranks what the exchange scheduled."""
    now = now or datetime.now(timezone.utc)
    states = states or {}
    counts = {TIER_HOT: 0, TIER_WARM: 0, TIER_COLD: 0}
    for it in items:
        counts[it.tier(now, states.get(it.match_id))] += 1
    for tier in (TIER_HOT, TIER_WARM, TIER_COLD):
        if counts[tier]:
            return TIER_SECONDS[tier], counts
    return TIER_SECONDS[TIER_COLD], counts
