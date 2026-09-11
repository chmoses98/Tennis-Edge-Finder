"""Adapters that turn a live-score feed into first-ball OBSERVATIONS.

Design rules that matter more than the parsing:

* One request per SOURCE per poll, never one per match. Every feed here is a day-level or live-level
  list, so a single response covers every match we care about. That is what keeps an adaptive cadence
  polite enough to run unattended.
* An adapter reports what the feed SAYS (`state`, the source's own status string, the timestamp it
  claims) and nothing more. It never guesses a start time, never fills a missing field, and maps an
  unrecognised status to UNKNOWN rather than to PRE.
* `claimed_start_utc` is a claim, not a fact. reconcile.bracket_for_source decides whether it may be
  promoted to confidence A; an unvalidated claim from an undocumented endpoint is not.
* Timezone semantics are recorded per adapter in `time_interpretation`, because a silent local-time
  reading is exactly the kind of error that would make every pregame label wrong by hours.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone, date

STATE_PRE, STATE_IN, STATE_POST, STATE_NO_PLAY, STATE_UNKNOWN = "PRE", "IN", "POST", "NO_PLAY", "UNKNOWN"


@dataclass(frozen=True)
class SourceMatch:
    source: str
    source_match_id: str
    player_a: str
    player_b: str
    state: str
    source_status: str = ""
    scheduled_utc: datetime | None = None
    claimed_start_utc: datetime | None = None
    games_played: int | None = None
    tournament: str = ""
    level_hint: str = ""
    doubles: bool = False
    time_interpretation: str = ""

    def to_dict(self):
        d = asdict(self)
        for k in ("scheduled_utc", "claimed_start_utc"):
            d[k] = d[k].isoformat() if d[k] else None
        return d


def _epoch(v) -> datetime | None:
    try:
        v = float(v)
    except (TypeError, ValueError):
        return None
    if 1_000_000_000 <= v <= 2_500_000_000:
        return datetime.fromtimestamp(v, tz=timezone.utc)
    if 1_000_000_000_000 <= v <= 2_500_000_000_000:
        return datetime.fromtimestamp(v / 1000, tz=timezone.utc)
    return None


def _iso_utc(v) -> datetime | None:
    if not isinstance(v, str) or not v:
        return None
    s = v.strip().replace("Z", "+00:00")
    try:
        d = datetime.fromisoformat(s)
    except ValueError:
        try:
            d = datetime.strptime(s[:16], "%Y-%m-%dT%H:%M")
        except ValueError:
            return None
    # A feed that omits an offset is NOT assumed to be UTC by fiat; the adapter must say so explicitly.
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)


class Adapter:
    id = ""
    authority = "secondary"
    levels: tuple = ()
    time_interpretation = ""

    def endpoints(self, day: date) -> list[str]:
        raise NotImplementedError

    def parse(self, payload) -> list[SourceMatch]:
        raise NotImplementedError


# --------------------------------------------------------------------------- ESPN
class EspnAdapter(Adapter):
    """ESPN's public site API. `events[].competitions[].status.type.state` is pre | in | post.

    ESPN's `date` on an event is the SCHEDULED time (ISO 8601 with an explicit Z), so it is reported as
    `scheduled_utc` and never as a claimed start. The state field is what proves play began.
    """
    authority = "secondary"
    time_interpretation = "iso8601_explicit_utc"

    def __init__(self, league: str = "atp"):
        self.league = league
        self.id = f"espn_{league}"
        self.levels = ("ATP", "GRAND_SLAM") if league == "atp" else ("WTA", "GRAND_SLAM")

    def endpoints(self, day: date) -> list[str]:
        return [f"https://site.api.espn.com/apis/site/v2/sports/tennis/{self.league}/scoreboard?dates={day:%Y%m%d}"]

    @staticmethod
    def _state(comp) -> tuple[str, str]:
        st = ((comp.get("status") or {}).get("type") or {})
        raw = st.get("state") or ""
        desc = st.get("description") or st.get("detail") or ""
        if "walkover" in desc.lower() or "cancel" in desc.lower():
            return STATE_NO_PLAY, desc
        return {"pre": STATE_PRE, "in": STATE_IN, "post": STATE_POST}.get(raw, STATE_UNKNOWN), desc or raw

    def parse(self, payload) -> list[SourceMatch]:
        out = []
        for ev in (payload or {}).get("events") or []:
            comps = list(ev.get("competitions") or [])
            for g in ev.get("groupings") or []:
                comps += list(g.get("competitions") or [])
            for comp in comps:
                names = []
                for c in comp.get("competitors") or []:
                    a = c.get("athlete") or c.get("team") or {}
                    n = a.get("displayName") or a.get("fullName") or a.get("shortDisplayName") or ""
                    if not n and isinstance(c.get("roster"), list):
                        n = " / ".join((r.get("athlete") or {}).get("displayName", "") for r in c["roster"])
                    names.append(n)
                if len(names) != 2 or not all(names):
                    continue
                state, desc = self._state(comp)
                games = None
                try:
                    games = sum(int(ls.get("value") or 0) for c in comp.get("competitors") or []
                                for ls in (c.get("linescores") or []))
                except (TypeError, ValueError):
                    games = None
                out.append(SourceMatch(
                    source=self.id, source_match_id=str(comp.get("id") or ev.get("id") or ""),
                    player_a=names[0], player_b=names[1], state=state, source_status=desc,
                    scheduled_utc=_iso_utc(comp.get("date") or ev.get("date")), claimed_start_utc=None,
                    games_played=games, tournament=(ev.get("name") or ""),
                    level_hint=self.league.upper(), doubles="/" in names[0],
                    time_interpretation=self.time_interpretation))
        return out


# --------------------------------------------------------------------------- SofaScore
class SofascoreAdapter(Adapter):
    """SofaScore's public JSON. Epoch seconds, UTC by construction.

    `startTimestamp` is reported as a CLAIM, not as truth: on this feed it is the scheduled time for a
    not-started event and is understood to be updated once play begins, but that behaviour is
    undocumented, so it is only ever promoted to confidence A when it falls inside a bracket our own
    polling observed independently (see reconcile.bracket_for_source).
    """
    authority = "secondary"
    time_interpretation = "epoch_seconds_utc"
    levels = ("ATP", "WTA", "CHALLENGER", "ITF_M", "ITF_W", "QUALIFYING", "DOUBLES", "GRAND_SLAM")

    def __init__(self, mode: str = "live"):
        self.mode = mode
        self.id = f"sofascore_{mode}"

    def endpoints(self, day: date) -> list[str]:
        if self.mode == "live":
            return ["https://api.sofascore.com/api/v1/sport/tennis/events/live"]
        return [f"https://api.sofascore.com/api/v1/sport/tennis/scheduled-events/{day:%Y-%m-%d}"]

    @staticmethod
    def _state(ev) -> tuple[str, str]:
        st = ev.get("status") or {}
        t = (st.get("type") or "").lower()
        desc = st.get("description") or ""
        if t in ("canceled", "cancelled", "postponed") or "walkover" in desc.lower():
            return STATE_NO_PLAY, desc or t
        return {"notstarted": STATE_PRE, "inprogress": STATE_IN, "finished": STATE_POST}.get(t, STATE_UNKNOWN), desc or t

    def parse(self, payload) -> list[SourceMatch]:
        out = []
        for ev in (payload or {}).get("events") or []:
            home = ((ev.get("homeTeam") or {}).get("name") or "").strip()
            away = ((ev.get("awayTeam") or {}).get("name") or "").strip()
            if not home or not away:
                continue
            state, desc = self._state(ev)
            trn = ev.get("tournament") or {}
            cat = ((trn.get("category") or {}).get("name") or "")
            claimed = _epoch(ev.get("startTimestamp")) if state in (STATE_IN, STATE_POST) else None
            games = None
            try:
                hs, as_ = ev.get("homeScore") or {}, ev.get("awayScore") or {}
                games = sum(int(v) for d in (hs, as_) for k, v in d.items()
                            if k.startswith("period") and isinstance(v, (int, float)))
            except (TypeError, ValueError):
                games = None
            out.append(SourceMatch(
                source=self.id, source_match_id=str(ev.get("id") or ""), player_a=home, player_b=away,
                state=state, source_status=desc,
                scheduled_utc=_epoch(ev.get("startTimestamp")), claimed_start_utc=claimed, games_played=games,
                tournament=(trn.get("name") or ""), level_hint=cat,
                doubles="/" in home or "/" in away, time_interpretation=self.time_interpretation))
        return out


REGISTRY: dict[str, Adapter] = {}


def register(a: Adapter) -> Adapter:
    REGISTRY[a.id] = a
    return a


for _a in (EspnAdapter("atp"), EspnAdapter("wta"), SofascoreAdapter("live"), SofascoreAdapter("scheduled")):
    register(_a)
