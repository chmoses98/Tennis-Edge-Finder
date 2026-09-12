"""Turn an ESPN tennis scoreboard payload into Sackmann-shaped result rows.

Why: as of 2026-09-12 the Sackmann repositories are gone from upstream and every public fork froze within
days of that (the freshest of 20 forks was pushed 2026-06-10). The community mirror carries ATP results to
2026-09-01 and nothing carries WTA past 2026-04-27. ESPN's public scoreboard is the only reachable feed
that publishes CURRENT completed results for both tours, including the score set by set.

What this is NOT: ESPN publishes no serve or return statistics on the scoreboard, no surface, and no
player ids that mean anything outside ESPN. So these rows refresh the RESULT record (who beat whom, and
by what score) and nothing else. They enter the canonical table as their own id system and are keyed to
canonical players by the fail-closed name crosswalk, exactly like the mirror rows.

Doubles are skipped: ESPN shapes a pair as a roster and this project's singles schema cannot carry it.
"""
from __future__ import annotations

import re
from datetime import datetime, timezone

import pandas as pd

from tennis_edge.pricing.competition import classify_competition

SACKMANN_COLUMNS = ("tourney_id", "tourney_name", "surface", "draw_size", "tourney_level", "tourney_date",
                    "match_num", "winner_id", "winner_name", "loser_id", "loser_name", "score", "best_of",
                    "round", "winner_seed", "loser_seed", "winner_ioc", "loser_ioc")

_ROUNDS = {
    "final": "F", "semifinals": "SF", "semifinal": "SF", "quarterfinals": "QF", "quarterfinal": "QF",
    "round of 16": "R16", "round of 32": "R32", "round of 64": "R64", "round of 128": "R128",
    "1st round": "R32", "first round": "R32", "2nd round": "R16", "second round": "R16",
    "3rd round": "R32", "4th round": "R16",
    "qualifying 1st round": "Q1", "qualifying 2nd round": "Q2", "qualifying 3rd round": "Q3",
    "qualifying final": "Q3", "qualifying": "Q1", "round robin": "RR",
}

_LEVEL_LETTER = {
    ("ATP", "GRAND_SLAM"): "G", ("WTA", "GRAND_SLAM"): "G",
    ("ATP", "MASTERS_1000"): "M", ("WTA", "MASTERS_1000"): "PM",
    ("ATP", "TOUR_500_250"): "A", ("WTA", "TOUR_500_250"): "P",
    ("ATP", "TOUR_FINALS"): "F", ("WTA", "TOUR_FINALS"): "F",
    ("ATP", "TEAM"): "D", ("WTA", "TEAM"): "D",
    ("ATP", "CHALLENGER"): "C", ("WTA", "WTA_125"): "C",
    ("ATP", "OLYMPICS"): "O", ("WTA", "OLYMPICS"): "O",
    ("ATP", "ITF"): "S",
}


def _round_code(display: str | None) -> str | None:
    if not display:
        return None
    key = str(display).strip().lower()
    if key in _ROUNDS:
        return _ROUNDS[key]
    m = re.search(r"round of (\d+)", key)
    if m:
        return f"R{m.group(1)}"
    return str(display).strip()[:12]


def _score_string(win_ls, lose_ls) -> str | None:
    """Sackmann-style score from the MATCH winner's perspective: '7-6(3) 6-3'."""
    if not win_ls or not lose_ls:
        return None
    sets = []
    for w, l in zip(win_ls, lose_ls):
        try:
            wv, lv = int(round(float(w.get("value")))), int(round(float(l.get("value"))))
        except (TypeError, ValueError, AttributeError):
            return None
        wt, lt = w.get("tiebreak"), l.get("tiebreak")
        if wt is not None and lt is not None:
            try:
                sets.append(f"{wv}-{lv}({int(min(float(wt), float(lt)))})")
                continue
            except (TypeError, ValueError):
                pass
        sets.append(f"{wv}-{lv}")
    return " ".join(sets) if sets else None


def _competitions(payload):
    for ev in (payload or {}).get("events") or []:
        for g in ev.get("groupings") or []:
            gr = (g.get("grouping") or {})
            for c in g.get("competitions") or []:
                yield ev, gr, c
        for c in ev.get("competitions") or []:
            yield ev, {}, c


def parse_scoreboard(payload: dict, league: str) -> pd.DataFrame:
    """Completed SINGLES results from one dated scoreboard payload."""
    rows, skipped = [], {"not_final": 0, "doubles": 0, "no_score": 0, "no_names": 0}
    for ev, gr, c in _competitions(payload):
        st = ((c.get("status") or {}).get("type") or {})
        if st.get("state") != "post" or not st.get("completed"):
            skipped["not_final"] += 1
            continue
        slug = (gr.get("slug") or (c.get("type") or {}).get("slug") or "")
        if "doubles" in slug.lower():
            skipped["doubles"] += 1
            continue
        comps = c.get("competitors") or []
        win = next((x for x in comps if x.get("winner")), None)
        lose = next((x for x in comps if x is not win), None)
        if not win or not lose:
            skipped["not_final"] += 1
            continue
        wa, la = (win.get("athlete") or {}), (lose.get("athlete") or {})
        wn, ln = wa.get("displayName"), la.get("displayName")
        if not wn or not ln:
            skipped["no_names"] += 1
            continue
        score = _score_string(win.get("linescores"), lose.get("linescores"))
        if not score:
            skipped["no_score"] += 1
            continue
        when = (c.get("date") or ev.get("date") or "")[:10].replace("-", "")
        name = ev.get("name") or ""
        # A combined event appears on BOTH league boards carrying BOTH draws, so the league alone is not
        # the tour: the wta board returns Wimbledon's mens-singles too. The grouping decides when it
        # names a draw, and "womens" contains "mens", so women are tested first.
        sl = slug.lower()
        if "women" in sl:
            tour_hint = "WTA"
        elif "men" in sl:
            tour_hint = "ATP"
        else:
            tour_hint = "WTA" if league.lower() == "wta" else "ATP"
        info = classify_competition(name, tour_hint)
        tour = info["tour"] if info["tour"] in ("ATP", "WTA") else tour_hint
        # ESPN reports the EVENT's regulation length, so a men's slam says five sets even for a
        # qualifying match that is played best-of-three. The project's own inference already knows the
        # rule, so the field is deliberately left empty rather than carrying a wrong five.
        rows.append({
            "tourney_id": f"espn-{ev.get('id')}-{gr.get('id') or '0'}",
            "tourney_name": name,
            "surface": info.get("surface_hint"),
            "draw_size": None,
            "tourney_level": _LEVEL_LETTER.get((tour, info["level"]), "E"),
            "tourney_date": when or None,
            "match_num": c.get("id"),
            "winner_id": f"espn:{win.get('id') or wa.get('id') or wn}",
            "winner_name": wn,
            "loser_id": f"espn:{lose.get('id') or la.get('id') or ln}",
            "loser_name": ln,
            "score": score,
            "best_of": None,
            "round": _round_code((c.get("round") or {}).get("displayName")),
            "winner_seed": None, "loser_seed": None,
            "winner_ioc": (wa.get("flag") or {}).get("alt"), "loser_ioc": (la.get("flag") or {}).get("alt"),
            "_tour": tour,
        })
    df = pd.DataFrame(rows, columns=list(SACKMANN_COLUMNS) + ["_tour"])
    df.attrs["skipped"] = skipped
    return df


def summarise(df: pd.DataFrame) -> dict:
    if df is None or not len(df):
        return {"rows": 0}
    return {"rows": int(len(df)), "by_tour": {k: int(v) for k, v in df["_tour"].value_counts().items()},
            "date_min": str(df["tourney_date"].min()), "date_max": str(df["tourney_date"].max()),
            "tournaments": int(df["tourney_id"].nunique()), "skipped": df.attrs.get("skipped", {}),
            "parsed_at": datetime.now(timezone.utc).isoformat()}
