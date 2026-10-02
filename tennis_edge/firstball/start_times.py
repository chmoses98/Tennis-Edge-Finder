"""Start-time reconciliation: WHEN is a match actually going to start, and has it already started?

Why this exists (2026-10-02): six WTA Beijing matches sat on the assisted slate with Kalshi's nominal
06:00Z while ESPN's own order of play had them at 03:05Z-05:50Z. Kalshi's `occurrence_datetime` was the same
06:00:00Z for every match of that day: a DAY PLACEHOLDER, not a start time. RUN TENNIS was timed off it, and
by the time the handicap was done the first ball had been struck. A nominal time is therefore a PRIOR here,
never truth, and a nominal shared by many matches of one series is not even a prior.

Authority order for "has it started?" (highest first; a lower rung can never override a higher one):
  1. First-ball TRUTH with play observed (an upper bound / actual first ball at or before now) -> STARTED.
     A material contradiction between sports sources -> STATUS_AMBIGUOUS. A confirmed walkover -> NO_PLAY.
  2. A live-score observation of play (IN / POST) at or before now -> STARTED, unless another independent
     source said PRE AFTER that reading, in which case the sources disagree -> STATUS_AMBIGUOUS.
  3. Nothing else can say "started"; and nothing at all -- not a future Kalshi time, not an open market --
     can say "pregame" for a source-covered match without a recent live PRE reading.

Authority order for "when will it start?" (current_expected_start):
  1. The live source's own CURRENT scheduled time (ESPN `date`), only when the source vouches for it
     (ESPN `timeValid` is not False). ESPN moves this time as its courts progress.
  2. Court progression: if the match before this one on the same court is in progress, a conservative
     EARLY estimate of when it frees the court. It can only pull the estimate earlier, never later.
  3. Kalshi's nominal time -- LOW confidence, main-tour levels only, and never when it is a day
     placeholder (>= PLACEHOLDER_MIN_MATCHES matches of one series share the identical time).
  Otherwise the expected start is UNKNOWN. Nothing is invented.

Statuses (stable machine values):
  VERIFIED_UPCOMING   not started; a live source said PRE recently and gives a credible time well ahead
  ESTIMATED_UPCOMING  not started as far as known; the time is an estimate (court progression, a stale
                      live reading, or a Kalshi nominal) -- lower confidence
  START_IMMINENT      expected within IMMINENT_S, or overdue but seen PRE within PRE_POSITIVE_S
  STARTED             play observed (truth or live state)
  STATUS_AMBIGUOUS    sources disagree, or the expected start has passed and play is not positively known
                      to be pending -> fail closed
  START_UNKNOWN       no credible start time
  NO_PLAY             walkover / cancellation confirmed

BET rule (fail closed): a BET is allowed only for VERIFIED_UPCOMING / ESTIMATED_UPCOMING / START_IMMINENT /
START_UNKNOWN, and for a match a wired live source covers (ATP / WTA main tour, WTA 125) only with a live PRE
reading no older than LIVE_STATUS_MAX_AGE_S and a credible expected start. STARTED, NO_PLAY and
STATUS_AMBIGUOUS never allow a BET. Levels with no first-ball source (Challenger, ITF) keep their existing
treatment (START_UNKNOWN warnings, the frozen ITF abstention context).

Everything here is a pure function of recorded evidence and an explicit `now`: replaying the same store at
the same instant reproduces every status. Observations stamped after `now` are ignored.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone

VERIFIED_UPCOMING = "VERIFIED_UPCOMING"
ESTIMATED_UPCOMING = "ESTIMATED_UPCOMING"
START_IMMINENT = "START_IMMINENT"
STARTED = "STARTED"
STATUS_AMBIGUOUS = "STATUS_AMBIGUOUS"
START_UNKNOWN = "START_UNKNOWN"
NO_PLAY = "NO_PLAY"
START_STATUSES = (VERIFIED_UPCOMING, ESTIMATED_UPCOMING, START_IMMINENT, STARTED, STATUS_AMBIGUOUS,
                  START_UNKNOWN, NO_PLAY)
UPCOMING = (VERIFIED_UPCOMING, ESTIMATED_UPCOMING, START_IMMINENT)
BET_BLOCKING = (STARTED, STATUS_AMBIGUOUS, NO_PLAY)

HIGH, MEDIUM, LOW, NONE = "HIGH", "MEDIUM", "LOW", "NONE"

#: primary handicap packet: 45 -> 30 minutes before the earliest credible first ball of a window
PRIMARY_LEAD_S = 45 * 60
PRIMARY_LATEST_S = 30 * 60
#: final status / price refresh: 10 -> 5 minutes before
FINAL_LEAD_S = 10 * 60
FINAL_LATEST_S = 5 * 60
IMMINENT_S = 15 * 60
#: a live PRE reading this old still counts as the current status (COLD poll cadence 15 min + publish 10 min)
LIVE_STATUS_MAX_AGE_S = 30 * 60
#: past its expected start a match counts as pending only on a PRE reading at most this old
PRE_POSITIVE_S = 180
#: this many matches of one series sharing one identical nominal time = a day placeholder, not a start
PLACEHOLDER_MIN_MATCHES = 4
#: matches whose expected starts fall within this span of a window's earliest start share the window
WINDOW_SPAN_S = 90 * 60
#: court progression: minutes the preceding match may still need, deliberately on the SHORT side (an early
#: estimate pulls the refresh forward; a late one would repeat the 2026-10-02 failure). best_of -> set -> min.
COURT_REMAINING_MIN = {3: {1: 35, 2: 10, 3: 5}, 5: {1: 60, 2: 35, 3: 10, 4: 5, 5: 5}}
COURT_TURNOVER_MIN = 5
#: level buckets a wired live first-ball source (ESPN) covers; see firstball/watchlist.SOURCE_COVERED_LEVELS
COVERED_BUCKETS = ("ATP", "WTA", "WTA125")
MAIN_TOUR = ("ATP", "WTA")


def _utc(d: datetime | None) -> datetime | None:
    if d is None:
        return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


def _iso(d):
    return d.isoformat() if isinstance(d, datetime) else d


def _parse(x) -> datetime | None:
    if isinstance(x, datetime):
        return _utc(x)
    if isinstance(x, str) and x:
        try:
            return _utc(datetime.fromisoformat(x.replace("Z", "+00:00")))
        except ValueError:
            return None
    return None


# ---------------------------------------------------------------------------------------------- court order
def court_context(target, feed) -> dict | None:
    """The order of play on `target`'s court in ONE live-feed snapshot: the match scheduled immediately before
    it on the same court of the same tournament, with that match's state and current set, plus how many
    not-started matches are queued ahead. Recorded with each observation as evidence; returns None when the
    source publishes no court, or the order cannot be determined (a tie is never guessed)."""
    if not getattr(target, "court", "") or target.scheduled_utc is None:
        return None
    same = [m for m in feed if m is not target and m.source == target.source and m.tournament == target.tournament
            and getattr(m, "court", "") == target.court and m.source_match_id != target.source_match_id
            and m.scheduled_utc is not None
            and timedelta(0) <= target.scheduled_utc - m.scheduled_utc <= timedelta(hours=18)]
    ahead = sorted((m for m in same if m.scheduled_utc < target.scheduled_utc), key=lambda m: m.scheduled_utc)
    ties = [m for m in same if m.scheduled_utc == target.scheduled_utc]
    if not ahead:
        return {"court": target.court, "preceding": None, "queue_ahead_pre": 0, "same_time_on_court": len(ties)}
    p = ahead[-1]
    return {"court": target.court, "same_time_on_court": len(ties),
            "queue_ahead_pre": sum(1 for m in ahead if m.state == "PRE"),
            "preceding": {"source_match_id": p.source_match_id, "players": [p.player_a, p.player_b],
                          "state": p.state, "period": getattr(p, "period", None),
                          "best_of": getattr(p, "best_of", None), "games_played": p.games_played,
                          "scheduled_utc": _iso(p.scheduled_utc), "time_valid": getattr(p, "time_valid", None)}}


def court_estimate(ctx: dict | None, observed_at: datetime) -> tuple[datetime | None, str]:
    """Conservative EARLY start estimate from a recorded court context. None when it implies nothing."""
    if not ctx or not ctx.get("preceding"):
        return None, ""
    p = ctx["preceding"]
    bo = p.get("best_of") if p.get("best_of") in COURT_REMAINING_MIN else 3
    if p.get("state") == "IN":
        st = p.get("period") or 1
        rem = COURT_REMAINING_MIN[bo].get(int(st), min(COURT_REMAINING_MIN[bo].values()))
        return observed_at + timedelta(minutes=rem + COURT_TURNOVER_MIN), (
            f"preceding match on {ctx.get('court')} in progress (set {st} of best-of-{bo})")
    if p.get("state") in ("POST", "NO_PLAY") and (ctx.get("queue_ahead_pre") or 0) == 0:
        return observed_at + timedelta(minutes=COURT_TURNOVER_MIN), f"preceding match on {ctx.get('court')} finished"
    return None, ""


# ---------------------------------------------------------------------------------------------- placeholders
def placeholder_nominals(nominals: list[tuple[str, datetime | None]], *, min_matches: int = PLACEHOLDER_MIN_MATCHES) -> set:
    """{(series, nominal)} shared by >= min_matches matches: a day placeholder, not a start time.
    `nominals` is one (series, nominal) pair per MATCH."""
    counts: dict = {}
    for k in nominals:
        if k[1] is not None:
            counts[k] = counts.get(k, 0) + 1
    return {k for k, n in counts.items() if n >= min_matches}


# ---------------------------------------------------------------------------------------------- reconciliation
def reconcile_start(*, match_id: str, nominal, level_bucket: str, observations=(), truth=None, now: datetime,
                    nominal_is_placeholder: bool = False) -> dict:
    """The start status of one match at `now`. Observations later than `now` are ignored."""
    now = _utc(now)
    nominal = _parse(nominal)
    covered = level_bucket in COVERED_BUCKETS
    obs = sorted((o for o in observations if _utc(o.observed_at_utc) <= now), key=lambda o: _utc(o.observed_at_utc))
    sports = [o for o in obs if o.authority != "exchange"]
    reasons: list[str] = []
    last_checked = _utc(sports[-1].observed_at_utc) if sports else None
    out = {"match_id": match_id, "evaluated_at": now.isoformat(), "nominal_scheduled_start": _iso(nominal),
           "nominal_is_placeholder": bool(nominal_is_placeholder), "live_source_covered": covered,
           "start_time_last_checked": _iso(last_checked), "current_expected_start": None,
           "start_time_source": None, "start_time_confidence": NONE, "start_time_candidates": [],
           "earliest_safe_handicap_time": None, "recommended_handicap_by": None, "final_check_time": None,
           "first_ball_status": "NOT_OBSERVED_STARTED" if covered else "NO_FIRST_BALL_SOURCE",
           "first_ball_source": None, "first_ball_at": None, "court": None, "court_context": None}

    def done(status, *, bet=None):
        out["start_status"] = status
        out["status_reasons"] = reasons
        allowed = status not in BET_BLOCKING if bet is None else bet
        out["bet_allowed"] = bool(allowed)
        return out

    # ---- 1. first-ball truth outranks every schedule
    if truth is not None:
        tsrc = f"{truth.source or 'first-ball store'} (confidence {truth.confidence})"
        if truth.no_play:
            out.update(first_ball_status="NO_PLAY", first_ball_source=tsrc)
            reasons.append("WALKOVER_OR_CANCELLATION_CONFIRMED")
            return done(NO_PLAY)
        if truth.contradiction_status == "MATERIAL":
            out.update(first_ball_status="CONTRADICTED", first_ball_source=tsrc)
            reasons.append(f"FIRST_BALL_SOURCES_CONTRADICT: {truth.contradiction_detail}")
            return done(STATUS_AMBIGUOUS)
        ub = _utc(truth.upper_bound_utc)
        if ub is not None and ub <= now:
            fb = _utc(truth.actual_first_ball_at_utc) or ub
            out.update(first_ball_status="OBSERVED_STARTED", first_ball_source=tsrc, first_ball_at=_iso(fb))
            reasons.append("PLAY_OBSERVED_BY_FIRST_BALL_TRUTH")
            return done(STARTED)

    # ---- 2. a live reading of play; another witness saying PRE afterwards is a disagreement
    played = [o for o in sports if o.state in ("IN", "POST")]
    if any(o.state == "NO_PLAY" for o in sports) and not played:
        out.update(first_ball_status="NO_PLAY", first_ball_source=sports[-1].source)
        reasons.append("SOURCE_REPORTS_NO_PLAY")
        return done(NO_PLAY)
    if played:
        p0 = played[0]
        later_pre = [o for o in sports if o.state == "PRE" and o.group != p0.group
                     and _utc(o.observed_at_utc) > _utc(p0.observed_at_utc)]
        out.update(first_ball_source=f"{p0.source} ({p0.source_status or p0.state})",
                   first_ball_at=_iso(_utc(p0.observed_at_utc)))
        if later_pre:
            out["first_ball_status"] = "SOURCES_DISAGREE"
            reasons.append(f"SOURCES_DISAGREE: {p0.source} reported play at {_iso(_utc(p0.observed_at_utc))}, "
                           f"{later_pre[-1].source} reported not started at {_iso(_utc(later_pre[-1].observed_at_utc))}")
            return done(STATUS_AMBIGUOUS)
        out["first_ball_status"] = "OBSERVED_STARTED"
        reasons.append("PLAY_OBSERVED_BY_LIVE_SOURCE")
        return done(STARTED)

    # ---- 3. not started as far as anyone knows: when will it start?
    pre = [o for o in sports if o.state == "PRE"]
    last_pre = _utc(pre[-1].observed_at_utc) if pre else None
    pre_age = (now - last_pre).total_seconds() if last_pre else None
    live_current = pre_age is not None and pre_age <= LIVE_STATUS_MAX_AGE_S
    fresh_pre = pre_age is not None and pre_age <= PRE_POSITIVE_S
    cands = []
    sched = next((o for o in reversed(sports) if o.source_event_timestamp is not None), None)
    live = None
    if sched is not None and sched.source_time_valid is not False:
        age = (now - _utc(sched.observed_at_utc)).total_seconds()
        conf = HIGH if (sched.source_time_valid is True and age <= LIVE_STATUS_MAX_AGE_S) else MEDIUM
        live = (_utc(sched.source_event_timestamp), f"LIVE_SCHEDULE:{sched.source}", conf)
        cands.append(live)
    elif sched is not None:
        reasons.append(f"LIVE_TIME_IS_PLACEHOLDER: {sched.source} marks {_iso(_utc(sched.source_event_timestamp))} "
                       "as not a valid time")
    cc_obs = next((o for o in reversed(sports) if o.court_context), None)
    court = None
    if cc_obs is not None:
        out["court"], out["court_context"] = cc_obs.court_context.get("court"), cc_obs.court_context
        est, why = court_estimate(cc_obs.court_context, _utc(cc_obs.observed_at_utc))
        if est is not None:
            court = (est, f"COURT_PROGRESSION: {why}", MEDIUM)
            cands.append(court)
    nom = None
    if nominal is not None:
        if nominal_is_placeholder:
            reasons.append("NOMINAL_IS_DAY_PLACEHOLDER: Kalshi lists this time for many matches of the series")
        elif level_bucket in MAIN_TOUR:
            nom = (nominal, "KALSHI_NOMINAL", LOW)
            cands.append(nom)
        else:
            reasons.append("NOMINAL_UNRELIABLE_AT_THIS_LEVEL")
    out["start_time_candidates"] = [{"time": _iso(t), "source": s, "confidence": c} for t, s, c in cands]
    if live is not None:
        chosen = court if (court is not None and court[0] < live[0]) else live
    elif court is not None:
        chosen = court
    else:
        chosen = nom
    if chosen is not None:
        exp = chosen[0]
        out.update(current_expected_start=exp.isoformat(), start_time_source=chosen[1], start_time_confidence=chosen[2],
                   earliest_safe_handicap_time=(exp - timedelta(seconds=PRIMARY_LEAD_S)).isoformat(),
                   recommended_handicap_by=(exp - timedelta(seconds=PRIMARY_LEAD_S)).isoformat(),
                   final_check_time=(exp - timedelta(seconds=FINAL_LEAD_S)).isoformat())
        if nom is not None and chosen is not nom and abs((nom[0] - exp).total_seconds()) >= 15 * 60:
            reasons.append(f"EXPECTED_START_DIFFERS_FROM_NOMINAL_BY_{int((exp - nom[0]).total_seconds() // 60):+d}_MIN")

    if covered and not live_current:
        reasons.append("NO_RECENT_LIVE_STATUS: no live PRE reading within "
                       f"{LIVE_STATUS_MAX_AGE_S // 60} min" + ("" if last_pre else " (never observed by a live source)"))

    if chosen is None:
        reasons.append("NO_CREDIBLE_START_TIME")
        return done(START_UNKNOWN, bet=not covered)
    exp = chosen[0]
    to_go = (exp - now).total_seconds()
    if to_go <= 0:
        if fresh_pre:
            reasons.append(f"OVERDUE_BUT_SEEN_NOT_STARTED_{int(pre_age)}S_AGO")
            return done(START_IMMINENT, bet=True)
        reasons.append("EXPECTED_START_PASSED_FIRST_BALL_NOT_POSITIVELY_KNOWN")
        return done(STATUS_AMBIGUOUS)
    bet = live_current if covered else True
    if to_go <= IMMINENT_S:
        return done(START_IMMINENT, bet=bet)
    if live_current and chosen is not nom:
        return done(VERIFIED_UPCOMING, bet=bet)
    return done(ESTIMATED_UPCOMING, bet=bet)


# ---------------------------------------------------------------------------------------------- windows
def plan_windows(entries: list[dict], now: datetime, *, span_s: int = WINDOW_SPAN_S) -> dict:
    """Group upcoming main-tour singles matches into practical windows by EARLIEST credible expected start.

    `entries`: [{"match_id", "label", "level_bucket", "discipline", "start": reconcile_start(...)}].
    The primary handicap refresh targets the window's earliest credible first ball, not each nominal time."""
    now = _utc(now)
    rel = []
    unverified = []
    for e in entries:
        st = e.get("start") or {}
        if e.get("level_bucket") not in MAIN_TOUR or (e.get("discipline") or "singles") != "singles":
            continue
        if st.get("start_status") in (START_UNKNOWN, STATUS_AMBIGUOUS):
            unverified.append({"match_id": e["match_id"], "label": e.get("label"), "status": st.get("start_status"),
                               "reasons": st.get("status_reasons")})
        exp = _parse(st.get("current_expected_start"))
        if st.get("start_status") in UPCOMING and exp is not None:
            rel.append((exp, e))
    rel.sort(key=lambda x: (x[0], x[1]["match_id"]))
    windows = []
    for exp, e in rel:
        if not windows or (exp - windows[-1]["_start"]).total_seconds() > span_s:
            windows.append({"_start": exp, "matches": []})
        st = e["start"]
        windows[-1]["matches"].append({"match_id": e["match_id"], "label": e.get("label"),
                                       "current_expected_start": st["current_expected_start"],
                                       "start_status": st["start_status"], "start_time_source": st["start_time_source"],
                                       "start_time_confidence": st["start_time_confidence"]})
    out = []
    for w in windows:
        s0 = w.pop("_start")
        primary = s0 - timedelta(seconds=PRIMARY_LEAD_S)
        out.append({"earliest_credible_first_ball": s0.isoformat(),
                    "recommended_run_tennis_time": primary.isoformat(),
                    "primary_refresh_window": [primary.isoformat(), (s0 - timedelta(seconds=PRIMARY_LATEST_S)).isoformat()],
                    "final_status_price_check_time": (s0 - timedelta(seconds=FINAL_LEAD_S)).isoformat(),
                    "final_refresh_window": [(s0 - timedelta(seconds=FINAL_LEAD_S)).isoformat(),
                                             (s0 - timedelta(seconds=FINAL_LATEST_S)).isoformat()],
                    "primary_overdue": primary <= now, "n_matches": len(w["matches"]), "matches": w["matches"]})
    nxt = out[0] if out else None
    return {"evaluated_at": now.isoformat(), "next_window": nxt, "windows": out[:6],
            "main_tour_status_unverified": unverified,
            "rule": ("primary handicap refresh 45->30 min before the EARLIEST credible first ball of the window; final "
                     "status/price refresh 10->5 min before; times come from start reconciliation, never a nominal alone")}


# ---------------------------------------------------------------------------------------------- dispatch
FULL_RUN_MAX_MODEL_AGE_S = 3 * 3600      # producer rows older than this -> a full RUN TENNIS before the window
FULL_RUN_LEAD_S = 95 * 60                # a full RUN TENNIS needs ~25-50 min to publish its slate
MIN_DISPATCH_GAP_S = 15 * 60
DAILY_FULL_RUN_CAP = 6


def window_key(earliest: datetime) -> str:
    e = _utc(earliest)
    return e.replace(minute=(e.minute // 15) * 15, second=0, microsecond=0).strftime("%Y%m%dT%H%MZ")


def due_actions(plan: dict, now: datetime, *, last_slate_built_at=None, last_model_run_at=None,
                dispatch_log: list[dict] = ()) -> list[dict]:
    """Which refreshes to dispatch NOW for the next window. Pure; the caller performs (or dry-runs) them.

      run_tennis      full RUN TENNIS (producers + slate) when the producer rows are older than
                      FULL_RUN_MAX_MODEL_AGE_S and the window is <= FULL_RUN_LEAD_S away
      slate_primary   assisted slate only, inside [earliest - 55 min, earliest - FINAL_LEAD_S), when no slate
                      was built since the primary window opened
      slate_final     assisted slate only, inside [earliest - 15 min, earliest), for the final status/price check
    Each (window, kind) is dispatched at most once; a window whose earliest start moves 15+ minutes earlier
    gets a new key and is re-planned. Biased early: when unsure, refresh sooner."""
    now = _utc(now)
    w = (plan or {}).get("next_window")
    if not w:
        return []
    e = _parse(w["earliest_credible_first_ball"])
    to_go = (e - now).total_seconds()
    if to_go <= 0:
        return []
    key = window_key(e)
    built = _parse(last_slate_built_at)
    model = _parse(last_model_run_at)
    log = list(dispatch_log or [])

    def done_for(kind):
        return any(d.get("window") == key and d.get("kind") == kind for d in log)

    def recent(kind):
        return any(d.get("kind") == kind and _parse(d.get("at")) and (now - _parse(d["at"])).total_seconds() < MIN_DISPATCH_GAP_S
                   for d in log)
    acts = []
    full_today = sum(1 for d in log if d.get("kind") == "run_tennis" and (_parse(d.get("at")) or now).date() == now.date())
    model_stale = model is None or (now - model).total_seconds() > FULL_RUN_MAX_MODEL_AGE_S
    run_pending = any(d.get("window") == key and d.get("kind") == "run_tennis" and _parse(d.get("at"))
                      and (now - _parse(d["at"])).total_seconds() < 50 * 60 for d in log)
    if model_stale and PRIMARY_LEAD_S < to_go <= FULL_RUN_LEAD_S and not done_for("run_tennis") \
            and full_today < DAILY_FULL_RUN_CAP and not recent("run_tennis"):
        acts.append({"kind": "run_tennis", "window": key, "reason": f"producer rows stale; window at {e.isoformat()}"})
        run_pending = True
    primary_open = e - timedelta(seconds=PRIMARY_LEAD_S + 10 * 60)
    if FINAL_LEAD_S < to_go <= PRIMARY_LEAD_S + 10 * 60 and not done_for("slate_primary") and not run_pending \
            and (built is None or built < primary_open) and not recent("slate_primary"):
        acts.append({"kind": "slate_primary", "window": key, "reason": f"primary handicap packet for window at {e.isoformat()}"})
    final_open = e - timedelta(seconds=FINAL_LEAD_S + 5 * 60)
    if to_go <= FINAL_LEAD_S + 5 * 60 and not done_for("slate_final") and (built is None or built < final_open) \
            and not recent("slate_final"):
        acts.append({"kind": "slate_final", "window": key, "reason": f"final status/price check for window at {e.isoformat()}"})
    for a in acts:
        a["at"] = now.isoformat()
        a["earliest_credible_first_ball"] = e.isoformat()
    return acts


def slate_freshness(slate: dict | None, plan: dict, now: datetime) -> dict:
    """Is the published assisted slate still authoritative? Stale when the primary refresh time of the next
    window has passed without a newer slate, or when a match the slate shows as upcoming has since STARTED /
    become ambiguous / moved 15+ minutes earlier."""
    now = _utc(now)
    if not slate:
        return {"stale": True, "reasons": ["NO_SLATE"]}
    built = _parse(slate.get("built_at"))
    reasons = []
    w = (plan or {}).get("next_window")
    if w and built is not None:
        primary = _parse(w["recommended_run_tennis_time"])
        if now >= primary and built < primary:
            reasons.append(f"PRIMARY_REFRESH_DUE: window at {w['earliest_credible_first_ball']}, slate built {built.isoformat()}")
    current = {m["match_id"]: m for win in (plan or {}).get("windows") or [] for m in win["matches"]}
    changed = []
    for x in slate.get("matches") or []:
        st = x.get("start") or {}
        mid = x.get("event_id")
        if st.get("start_status") not in UPCOMING:
            continue
        exp_then = _parse(st.get("current_expected_start"))
        if exp_then is not None and now >= exp_then:
            changed.append({"match": mid, "change": "EXPECTED_START_PASSED_SINCE_BUILD"})
            continue
        cur = current.get(mid)
        exp_now = _parse((cur or {}).get("current_expected_start"))
        if exp_then and exp_now and (exp_then - exp_now).total_seconds() >= 15 * 60:
            changed.append({"match": mid, "change": f"EXPECTED_START_MOVED_EARLIER_{int((exp_then - exp_now).total_seconds() // 60)}_MIN"})
    for s in (plan or {}).get("status_changes") or []:
        changed.append(s)
    if changed:
        reasons.append(f"STATUS_OR_SCHEDULE_CHANGED_SINCE_BUILD: {len(changed)} match(es)")
    return {"stale": bool(reasons), "reasons": reasons, "changed_matches": changed[:30],
            "slate_id": slate.get("slate_id"), "slate_built_at": slate.get("built_at"), "checked_at": now.isoformat()}
