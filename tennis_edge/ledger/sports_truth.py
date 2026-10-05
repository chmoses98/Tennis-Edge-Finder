"""Independent sports truth: what happened on court, from results sources that are NOT the exchange.

Until 2026-10-05 every settled row's "sports truth" was copied from Kalshi's own result (source
"kalshi_result"), which cannot be reconciled against Kalshi. This module resolves a settled prediction to ONE
physical match in the canonical results table (Sackmann / TML / ESPN -- none of them derived from Kalshi) and
records winner, score, outcome type (completed / retired / walkover / default) and provenance.

Fail closed:
  * the match must be found by the CANONICAL ids of both players (the ids the projection itself used) on the
    same tour, in a date window around the prediction -- never by name similarity;
  * exactly one candidate match may qualify; two (the same pair meeting twice in the window) is AMBIGUOUS;
  * a level whose independent source has not published results up to the match date is NOT_COVERED, never a
    silent miss (ITF has no free results feed after April (WTA) / June (ATP) 2026).

Window. The anchor is the match day in Kalshi's event ticker (KX...-26SEP29...), falling back to the prediction date.
Each source dates a match differently, so each gets its own window around the anchor D:
  Sackmann                   tournament START date   in [D - 15, D + 1]
  TML main tour (+ mirror)   tournament date         in [D - 15, D + 4]
  TML Challenger mirror      tournament START or END in [D - 7, D + 8]  (both conventions occur in 2026 files)
  ESPN                       the day it was played   in [D - 1, D + 3]  (rain delays / reschedules: +2 is common)
Measured on production evidence (2026-10-05): offsets of the nearest same-pair result to the ticker day cluster
at ESPN +2, TML Challenger -2..-6 and TML main +2..+3; previous meetings sit at -13 days or earlier.
A single wide window ([-14, +10] for everything) was tried first and produced 10 false "conflicts" in
production data: the same two players had also met in an adjacent week. Tight, source-aware windows fix that,
and anything still ambiguous stays AMBIGUOUS.
"""
from __future__ import annotations

import re

from dataclasses import dataclass, asdict
from datetime import date, timedelta

import pandas as pd

LEVEL_GROUP = {"GRAND_SLAM": "GS", "MASTERS_1000": "M", "TOUR_FINALS": "M", "OLYMPICS": "M", "TOUR_500_250": "T",
               "CHALLENGER": "C", "WTA_125": "C", "ITF": "I", "TEAM": "O", "OTHER": "O"}
SOURCE_WINDOWS = {"sackmann": (15, 1), "tml_ATP_main": (15, 4), "tml_ATP_main_mirror": (15, 4),
                  "tml_ATP_challenger": (7, 8), "espn": (1, 3)}
_MONTHS = {m: i for i, m in enumerate(("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"), 1)}


def ticker_date(event_ticker: str | None) -> date | None:
    """'KXWTACHALLENGERMATCH-26SEP29KOSCEN' -> 2026-09-29 (Kalshi's scheduled match day)."""
    m = re.search(r"-(\d{2})([A-Z]{3})(\d{2})", event_ticker or "")
    if not m or m.group(2) not in _MONTHS:
        return None
    try:
        return date(2000 + int(m.group(1)), _MONTHS[m.group(2)], int(m.group(3)))
    except ValueError:
        return None


def _window(source_label: str) -> tuple[int, int]:
    if source_label in SOURCE_WINDOWS:
        return SOURCE_WINDOWS[source_label]
    for k, v in SOURCE_WINDOWS.items():
        if source_label and source_label.startswith(k):
            return v
    return (15, 1)

RESOLVED, NOT_FOUND, AMBIGUOUS, NOT_COVERED, NO_IDS = "RESOLVED", "NOT_FOUND", "AMBIGUOUS", "NOT_COVERED", "NO_CANONICAL_IDS"


@dataclass(frozen=True)
class IndependentTruth:
    status: str
    winner_id: str | None = None
    loser_id: str | None = None
    outcome_type: str | None = None
    score_raw: str | None = None
    games_w: float | None = None
    games_l: float | None = None
    sets_w: float | None = None
    sets_l: float | None = None
    source_label: str | None = None
    match_key: str | None = None
    tourney_name: str | None = None
    tourney_date: str | None = None
    reason: str = ""

    def to_dict(self):
        return asdict(self)


class ResultsIndex:
    """Canonical results keyed by (tour, unordered canonical pair). Built from matches.parquet."""

    def __init__(self, matches: pd.DataFrame, since: date):
        m = matches[(matches["canonical_id_status"] == "MAPPED") & matches["tourney_date"].notna()].copy()
        m["d"] = pd.to_datetime(m["tourney_date"]).dt.date
        m = m[m["d"] >= since]
        self.by_pair: dict = {}
        for r in m.itertuples(index=False):
            w, l = str(r.canonical_winner_id), str(r.canonical_loser_id)
            self.by_pair.setdefault((r.tour, frozenset((w, l))), []).append(r)
        full = matches[matches["tourney_date"].notna()]
        lg = full["level_canonical"].map(lambda x: LEVEL_GROUP.get(str(x), "O"))
        self.horizon = {(t, g): pd.to_datetime(grp).max().date()
                        for (t, g), grp in full["tourney_date"].groupby([full["tour"], lg])}

    def resolve(self, tour: str, a: str | None, b: str | None, level: str, on: date) -> IndependentTruth:
        if not a or not b:
            return IndependentTruth(NO_IDS, reason="prediction carries no canonical player ids")
        cands = []
        for r in self.by_pair.get((tour, frozenset((str(a), str(b)))), []):
            before, after = _window(r.source_label)
            if on - timedelta(days=before) <= r.d <= on + timedelta(days=after) and levels_compatible(level, r.level_canonical, r.source_label):
                cands.append(r)
        if len(cands) > 1:
            # the same physical match from two sources was deduplicated upstream; two rows here are two matches
            return IndependentTruth(AMBIGUOUS, reason=f"{len(cands)} matches between these players in the window")
        if len(cands) == 1:
            r = cands[0]
            return IndependentTruth(RESOLVED, str(r.canonical_winner_id), str(r.canonical_loser_id), r.outcome_type,
                                    r.score_raw, _f(r.games_w), _f(r.games_l), _f(r.sets_w), _f(r.sets_l),
                                    r.source_label, r.match_key, r.tourney_name, str(r.d))
        hz = self.horizon.get((tour, LEVEL_GROUP.get(level, "O")))
        if hz is None or hz < on:
            return IndependentTruth(NOT_COVERED, reason=f"independent results for {tour} {level} end {hz}; match on {on}")
        return IndependentTruth(NOT_FOUND, reason="no result between these canonical players in the window although the level is covered")


LEVEL_FAMILY = {"GS": "TOUR", "M": "TOUR", "T": "TOUR", "O": "TOUR", "C": "CHALLENGER", "I": "ITF"}


def levels_compatible(market_level: str, result_level: str, source_label: str | None) -> bool:
    """A tour-level market cannot be settled by a Challenger result between the same two players (production case
    2026-10-05: Tomic-Sun met in ATP qualifying, then again at a Challenger six days later; TML dates Challengers by
    either start or end, so the second meeting fell inside the window). ESPN mislabels WTA 125 events as 250/500,
    so for ESPN rows tour and Challenger/125 are treated as compatible."""
    fm = LEVEL_FAMILY.get(LEVEL_GROUP.get(str(market_level), "O"), "TOUR")
    fr = LEVEL_FAMILY.get(LEVEL_GROUP.get(str(result_level), "O"), "TOUR")
    if fm == fr:
        return True
    return bool(source_label and source_label.startswith("espn")) and {fm, fr} == {"TOUR", "CHALLENGER"}


def _f(x):
    try:
        v = float(x)
        return None if v != v else v
    except (TypeError, ValueError):
        return None


def reconcile_match_winner(truth: IndependentTruth, exchange: dict, subject_id: str | None) -> dict:
    """Kalshi MATCH_WINNER vs independent truth. Kalshi's rule: YES if the subject wins 'after a ball has been
    played'; a walkover (no ball) resolves to a fair price (scalar), a retirement to the player who advances."""
    res = (exchange or {}).get("result")
    if truth.status != RESOLVED:
        return {"status": "NOT_RECONCILED", "reason": truth.status}
    if truth.outcome_type == "WALKOVER":
        ok = res == "scalar"
        return {"status": "AGREE" if ok else "CONFLICT", "explained": "walkover: exchange should settle at a fair price",
                "exchange_result": res}
    if res not in ("yes", "no"):
        return {"status": "CONFLICT" if truth.outcome_type == "COMPLETED" else "EXPLAINED",
                "explained": None if truth.outcome_type == "COMPLETED" else f"{truth.outcome_type}: exchange settled {res}",
                "exchange_result": res}
    subj_won = subject_id is not None and str(subject_id) == truth.winner_id
    agree = (res == "yes") == subj_won
    return {"status": "AGREE" if agree else "CONFLICT", "exchange_result": res, "independent_subject_won": subj_won,
            "explained": None}
