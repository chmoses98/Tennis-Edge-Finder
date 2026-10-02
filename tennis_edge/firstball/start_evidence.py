"""Load the start-time evidence the reconciliation needs, and run it for a board of matches.

Reads the append-only first-ball store (observations of the last few UTC days, every truth). Nothing here
writes the store. Observations and truths are grouped by the physical match CODE (date + players) that every
Kalshi series of one match shares, so the match-winner, set-winner and derivative events of one match all
see the same evidence.
"""
from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone

from .start_times import placeholder_nominals, reconcile_start
from .truth import FirstBallObservation, FirstBallTruth


def match_code(ticker_or_event: str) -> str:
    parts = (ticker_or_event or "").split("-")
    return parts[1] if len(parts) > 1 else ""


def _obs_from_row(r: dict) -> FirstBallObservation:
    r = {k: v for k, v in r.items() if k not in ("prev_hash", "row_hash")}
    for k in ("observed_at_utc", "source_event_timestamp", "explicit_start_utc"):
        if r.get(k):
            r[k] = datetime.fromisoformat(r[k].replace("Z", "+00:00"))
    known = FirstBallObservation.__dataclass_fields__
    return FirstBallObservation(**{k: v for k, v in r.items() if k in known})


def load_recent_observations(store_root: str, now: datetime, *, days: int = 2) -> dict[str, list[FirstBallObservation]]:
    """match code -> observations from the last `days` UTC day files (and today's), oldest first."""
    out: dict[str, list] = {}
    d = os.path.join(store_root, "observations")
    if not os.path.isdir(d):
        return out
    wanted = {(now - timedelta(days=i)).strftime("%Y-%m-%d") for i in range(days + 1)}
    for fn in sorted(os.listdir(d)):
        if not fn.endswith(".jsonl") or fn[:-6] not in wanted:
            continue
        with open(os.path.join(d, fn)) as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    o = _obs_from_row(json.loads(line))
                except (ValueError, TypeError):
                    continue
                out.setdefault(match_code(o.match_id), []).append(o)
    for v in out.values():
        v.sort(key=lambda o: o.observed_at_utc)
    return out


def load_truths_by_code(store_root: str) -> dict[str, list[FirstBallTruth]]:
    from tennis_edge.assisted.market import load_truths
    out: dict[str, list] = {}
    for mid, t in load_truths(store_root).items():
        out.setdefault(match_code(mid), []).append(t)
    return out


def governing_truth(truths: list[FirstBallTruth] | None, now: datetime) -> FirstBallTruth | None:
    """Of the truths of one physical match (one per listed event), the one that says the most: a confirmed
    walkover, else a material contradiction, else the EARLIEST observed play, else any (pregame-only)."""
    ts = [t for t in (truths or []) if t.created_at is None or t.created_at <= now or t.upper_bound_utc is not None]
    if not ts:
        return None
    for t in ts:
        if t.no_play:
            return t
    for t in ts:
        if t.contradiction_status == "MATERIAL":
            return t
    played = [t for t in ts if t.upper_bound_utc is not None]
    if played:
        return min(played, key=lambda t: t.upper_bound_utc)
    return ts[0]


def board_statuses(matches: list[dict], *, store_root: str | None, now: datetime, obs_by_code=None,
                   truths_by_code=None) -> dict[str, dict]:
    """matches: [{"match_id", "code", "series", "nominal", "level_bucket"}] -> match_id -> reconcile_start(...).
    Placeholder nominals are detected across the whole board (one vote per match)."""
    if obs_by_code is None:
        obs_by_code = load_recent_observations(store_root, now) if store_root else {}
    if truths_by_code is None:
        truths_by_code = load_truths_by_code(store_root) if store_root and os.path.isdir(os.path.join(store_root, "truths")) else {}
    ph = placeholder_nominals([(m["series"], _p(m.get("nominal"))) for m in matches])
    out = {}
    for m in matches:
        nominal = _p(m.get("nominal"))
        out[m["match_id"]] = reconcile_start(
            match_id=m["match_id"], nominal=nominal, level_bucket=m["level_bucket"],
            observations=obs_by_code.get(m["code"], ()), truth=governing_truth(truths_by_code.get(m["code"]), now),
            now=now, nominal_is_placeholder=(m["series"], nominal) in ph)
    return out


def _p(x):
    if isinstance(x, datetime):
        return x if x.tzinfo else x.replace(tzinfo=timezone.utc)
    if isinstance(x, str) and x:
        try:
            d = datetime.fromisoformat(x.replace("Z", "+00:00"))
            return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
        except ValueError:
            return None
    return None
