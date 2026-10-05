"""Opponent-adjusted current form and pre-match context.

FORM is never a win-loss record. A player's form at horizon h is the exponentially decayed sum of their
rating residuals,

    form_h(p, D) = sum_i  w_i * (y_i - E_i) * 0.5 ** ((D - d_i) / h)

where E_i is the reference rating's PRE-match probability that p would win match i, y_i the result and w_i
the retirement weight. A win over a much stronger player adds nearly +1, a win over a much weaker one adds
almost nothing, so the statistic is opponent-adjusted by construction. Because the rating already moves by
K * (y - E), form measures only whether RECENT surprises deserve more weight than the rating gives them;
if they do not, the walk-forward ensemble gives it zero weight and it is not promoted.

CONTEXT holds facts about the schedule, all known before the first ball:
  days since last match, matches in the previous 14 days, minutes in the previous 7 days (where recorded),
  a retirement LOSS in the previous 30 days (the retiring player is the loser of a RETIRED row), a surface
  switch within 21 days, matches already played in this event (qualifiers arrive with extra matches).
"""
from __future__ import annotations

import math
from collections import deque

HORIZONS = (30, 60, 120, 240)


class FormState:
    __slots__ = ("s", "c", "last")

    def __init__(self):
        self.s: dict = {}      # (pid, h) -> decayed residual sum
        self.c: dict = {}      # (pid, h) -> decayed match count
        self.last: dict = {}   # pid -> date of last update

    def read(self, p, date) -> dict:
        out = {}
        last = self.last.get(p)
        days = (date - last).days if (last is not None and date is not None) else None
        for h in HORIZONS:
            f = 1.0 if days is None or days <= 0 else 0.5 ** (days / h)
            out[f"form{h}"] = self.s.get((p, h), 0.0) * f
            out[f"cnt{h}"] = self.c.get((p, h), 0.0) * f
        return out

    def update(self, p, date, residual: float, weight: float = 1.0):
        last = self.last.get(p)
        days = (date - last).days if (last is not None and date is not None) else 0
        for h in HORIZONS:
            f = 1.0 if days <= 0 else 0.5 ** (days / h)
            self.s[(p, h)] = self.s.get((p, h), 0.0) * f + weight * residual
            self.c[(p, h)] = self.c.get((p, h), 0.0) * f + weight
        if date is not None:
            self.last[p] = date


class ContextState:
    __slots__ = ("recent", "last_surface", "last_ret_loss", "event")

    def __init__(self):
        self.recent: dict = {}          # pid -> deque[(date, minutes or None)] (last 60 days)
        self.last_surface: dict = {}    # pid -> (date, surface)
        self.last_ret_loss: dict = {}   # pid -> date the player retired from a match
        self.event: dict = {}           # pid -> (tourney_key, matches played in it)

    def read(self, p, date, surface, tourney_key) -> dict:
        dq = self.recent.get(p)
        last = dq[-1][0] if dq else None
        days = (date - last).days if (last is not None and date is not None) else None
        n14 = mins7 = 0.0
        if dq:
            for d, mins in dq:
                gap = (date - d).days
                if gap < 14:
                    n14 += 1
                if gap < 7:
                    mins7 += mins if mins is not None else 100.0
        ls = self.last_surface.get(p)
        switch = 1.0 if (ls and surface and ls[1] and ls[1] != surface and (date - ls[0]).days <= 21) else 0.0
        lr = self.last_ret_loss.get(p)
        ret30 = 1.0 if (lr is not None and (date - lr).days <= 30) else 0.0
        ev = self.event.get(p)
        in_event = float(ev[1]) if (ev and ev[0] == tourney_key) else 0.0
        return {"days": days, "n14": n14, "mins7": mins7, "surf_switch": switch, "ret30": ret30,
                "in_event": in_event}

    def update(self, p, date, minutes, surface, tourney_key, retired_loser: bool):
        dq = self.recent.setdefault(p, deque())
        dq.append((date, minutes))
        while dq and (date - dq[0][0]).days > 60:
            dq.popleft()
        if surface:
            self.last_surface[p] = (date, surface)
        if retired_loser:
            self.last_ret_loss[p] = date
        ev = self.event.get(p)
        self.event[p] = (tourney_key, (ev[1] + 1) if (ev and ev[0] == tourney_key) else 1)


def rest_feature(days) -> float:
    """log(1 + days since last match), capped at a year; a debut reads as a year."""
    return math.log1p(min(days, 365)) if days is not None else math.log1p(365)
