"""MODEL 3 -- Gen-2 fundamental tennis model. Market prices are PROHIBITED as inputs.

What it is
----------
A dynamic hierarchical serve/return system, fitted strictly in match order. Each player carries a
time-decayed, precision-weighted estimate of two latent abilities on the logit scale:

    s_p   serve ability   deviation from the tour baseline
    r_p   return ability  deviation from the tour baseline

and, separately, a per-surface DEVIATION from their own overall ability, partially pooled toward it. The
prediction for A serving to B on surface S at level L is

    logit P(A wins a point on serve) = base(tour) + level(tour, L) + s_A(S) - r_B(S)

where s_A(S) = s_A + w_A(S) * ds_A(S), and w is the shrinkage weight implied by how much surface-specific
evidence that player actually has.

What is different from Gen-1 (`serve_return.py`), and why
--------------------------------------------------------
1. LEVEL TRANSLATION. Gen-1 has one baseline per (tour, surface); a serve point at an ITF event and one
   at a Masters counted the same. Gen-2 estimates a level offset online from residuals, so evidence
   earned at one level translates to another instead of being silently mis-scaled.
2. PER-PLAYER SURFACE DEVIATIONS. Gen-1 put surface only in the BASELINE, so it could not express that a
   particular player serves better on grass. Gen-2 gives each player a surface deviation with its own
   precision, pooled toward their overall ability so a three-match grass sample cannot run away.
3. UNCERTAINTY IS CARRIED, NOT ASSUMED AWAY. Every ability has a precision, and the prediction shrinks
   toward the baseline in proportion to it. A player with 80 serve points is not treated like one with
   8,000.
4. A PRIOR FOR PLAYERS WITH NO SERVE DATA. Serve statistics exist for 78-81% of tour-level matches but
   only 4.6% of ITF ones, so Gen-1 returns the baseline for most of the universe -- it has nothing to say
   below Challenger. Gen-2 seeds a player's abilities from a rating-implied point probability, which is
   fundamental information, not market information.

Market discipline: this module imports nothing that touches prices, and `tests/test_gen2.py` asserts it.
The market-conditioned lane is a SEPARATE model (Model 4) that says so in its name.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field, asdict

import pandas as pd

from tennis_edge.models.elo import match_sort_key

MODEL_VERSION = "gen2_dyn_hier_sr_v1"


def logit(p: float) -> float:
    p = min(max(p, 1e-6), 1 - 1e-6)
    return math.log(p / (1 - p))


def sigmoid(x: float) -> float:
    if x >= 0:
        z = math.exp(-x)
        return 1.0 / (1.0 + z)
    z = math.exp(x)
    return z / (1.0 + z)


@dataclass
class Gen2Config:
    #: serve points of zero-mean prior evidence. Larger = stronger shrinkage for thin players.
    prior_points: float = 500.0
    #: half-life of evidence, in days
    half_life_days: float = 300.0
    #: prior evidence for a player's SURFACE deviation, in serve points. Deliberately large: a surface
    #: effect is a second-order refinement and must not be learned from one good week.
    surface_prior_points: float = 1500.0
    #: prior evidence for a (tour, level) offset, in serve points
    level_prior_points: float = 20000.0
    #: below this many observed serve points a player's abilities are seeded from their rating
    seed_below_points: float = 300.0
    #: how much of a rating-implied point edge to attribute to serve vs return (the rest goes to return)
    seed_serve_share: float = 0.5
    #: cap on any single ability, on the logit scale, so one broken row cannot move a player far
    ability_clip: float = 0.60

    def to_dict(self):
        return asdict(self)


@dataclass
class _Ability:
    num: float = 0.0          # decayed sum of (opponent-adjusted excess * points)
    den: float = 0.0          # decayed sum of points
    last: object = None       # date of the last update


@dataclass
class Gen2State:
    cfg: Gen2Config = field(default_factory=Gen2Config)
    serve: dict = field(default_factory=dict)          # pid -> _Ability
    ret: dict = field(default_factory=dict)
    surf_serve: dict = field(default_factory=dict)     # (pid, surface) -> _Ability
    surf_ret: dict = field(default_factory=dict)
    base_num: dict = field(default_factory=dict)       # tour -> decayed serve points won
    base_den: dict = field(default_factory=dict)
    level_num: dict = field(default_factory=dict)      # (tour, level) -> residual sum
    level_den: dict = field(default_factory=dict)
    seeded: set = field(default_factory=set)

    # ---------------------------------------------------------------- decay
    def _decay_factor(self, last, date) -> float:
        if last is None or date is None:
            return 1.0
        days = (date - last).days
        if days <= 0:
            return 1.0
        return 0.5 ** (days / self.cfg.half_life_days)

    def _get(self, store, key, date) -> _Ability:
        a = store.get(key)
        if a is None:
            a = _Ability()
            store[key] = a
        f = self._decay_factor(a.last, date)
        if f != 1.0:
            a.num *= f
            a.den *= f
        a.last = date
        return a

    # ---------------------------------------------------------------- read
    def baseline(self, tour: str) -> float:
        d = self.base_den.get(tour, 0.0)
        return logit(self.base_num.get(tour, 0.0) / d) if d > 500 else logit(0.62 if tour == "ATP" else 0.57)

    def level_offset(self, tour: str, level: str) -> float:
        k = (tour, level)
        den = self.level_den.get(k, 0.0)
        return self.level_num.get(k, 0.0) / (den + self.cfg.level_prior_points) if den else 0.0

    def _shrunk(self, ab: _Ability, prior_points: float) -> tuple[float, float]:
        """(value, weight): a precision-weighted mean against a zero prior, and how much evidence backs it."""
        den = ab.den if ab else 0.0
        num = ab.num if ab else 0.0
        v = num / (den + prior_points) if (den + prior_points) > 0 else 0.0
        return max(-self.cfg.ability_clip, min(self.cfg.ability_clip, v)), den

    def ability(self, pid: str, surface: str | None) -> tuple[float, float, float]:
        """(serve, return, serve points of evidence) including the pooled surface deviation."""
        s, sden = self._shrunk(self.serve.get(pid), self.cfg.prior_points)
        r, rden = self._shrunk(self.ret.get(pid), self.cfg.prior_points)
        if surface:
            ds, _ = self._shrunk(self.surf_serve.get((pid, surface)), self.cfg.surface_prior_points)
            dr, _ = self._shrunk(self.surf_ret.get((pid, surface)), self.cfg.surface_prior_points)
            s += ds
            r += dr
        return s, r, sden

    def predict_serve(self, a: str, b: str, tour: str, level: str, surface: str | None) -> float:
        sa, _, _ = self.ability(a, surface)
        _, rb, _ = self.ability(b, surface)
        return sigmoid(self.baseline(tour) + self.level_offset(tour, level) + sa - rb)

    def predict_point_probs(self, a: str, b: str, tour: str, level: str, surface: str | None) -> tuple[float, float]:
        """The pair the scoring engine expects, BOTH from A's point of view:

            pa = P(A wins a point on A's serve)
            pb = P(A wins a point on B's serve) = 1 - P(B holds a point on B's serve)

        Returning (A holds, B holds) instead is the same shape and completely wrong: the engine then
        believes A wins most points on return, and every match prices at 0.99.
        """
        return (self.predict_serve(a, b, tour, level, surface),
                1.0 - self.predict_serve(b, a, tour, level, surface))

    def evidence(self, pid: str) -> float:
        a = self.serve.get(pid)
        return a.den if a else 0.0

    # ---------------------------------------------------------------- write
    def seed_from_rating(self, pid: str, p_point_on_serve: float, tour: str, weight_points: float = 250.0):
        """Give a player with no serve statistics a fundamental prior from their rating.

        The rating is built from RESULTS, never from prices, so this stays inside Model 3's contract.
        """
        if pid in self.seeded:
            return
        self.seeded.add(pid)
        excess = logit(p_point_on_serve) - self.baseline(tour)
        share = self.cfg.seed_serve_share
        for store, part in ((self.serve, share * excess), (self.ret, -(1 - share) * excess)):
            ab = store.setdefault(pid, _Ability())
            ab.num += part * weight_points
            ab.den += weight_points

    def observe(self, *, server: str, returner: str, points: float, won: float, tour: str, level: str,
                surface: str | None, date):
        """One side of one match: `won` serve points out of `points`, opponent-adjusted."""
        if not points or points <= 0 or won is None or won < 0 or won > points:
            return
        rate = min(max(won / points, 1e-4), 1 - 1e-4)
        self.base_num[tour] = self.base_num.get(tour, 0.0) + won
        self.base_den[tour] = self.base_den.get(tour, 0.0) + points

        s_ab = self._get(self.serve, server, date)
        r_ab = self._get(self.ret, returner, date)
        s_now, _ = self._shrunk(s_ab, self.cfg.prior_points)
        r_now, _ = self._shrunk(r_ab, self.cfg.prior_points)
        base, lvl = self.baseline(tour), self.level_offset(tour, level)
        obs = logit(rate)

        # OPPONENT-ADJUSTED EXCESS, not an innovation. Each ability is a precision-weighted MEAN of the
        # excess its owner produced, so the numerator must carry the full excess relative to the
        # baseline and the OPPONENT's ability -- never the residual left after subtracting the ability
        # being estimated. Accumulating the residual instead makes the estimator eat itself: as the
        # ability approaches the truth the residual goes to zero, the numerator stops growing while the
        # denominator keeps growing, and every player decays back to the baseline. That produced a model
        # that predicted 0.50 for every match, with a Brier of 0.4989.
        adj_serve = obs - base - lvl + r_now        # the server did this well, crediting the returner
        adj_ret = -(obs - base - lvl - s_now)       # the returner allowed this, crediting the server
        s_ab.num += adj_serve * points
        s_ab.den += points
        r_ab.num += adj_ret * points
        r_ab.den += points

        # the level offset explains what neither player's ability accounts for
        k = (tour, level)
        self.level_num[k] = self.level_num.get(k, 0.0) + (obs - base - (s_now - r_now)) * points
        self.level_den[k] = self.level_den.get(k, 0.0) + points

        # a surface DEVIATION is the part of the excess the player's overall ability did not explain
        if surface:
            ss = self._get(self.surf_serve, (server, surface), date)
            rs = self._get(self.surf_ret, (returner, surface), date)
            ss.num += (adj_serve - s_now) * points
            ss.den += points
            rs.num += (adj_ret - r_now) * points
            rs.den += points


def _num(x):
    try:
        v = float(x)
        return None if v != v else v
    except (TypeError, ValueError):
        return None


def serve_points(row, side: str) -> tuple[float | None, float | None]:
    """(serve points played, serve points won) for 'w' or 'l'."""
    svpt = _num(row.get(f"{side}_svpt"))
    if not svpt or svpt <= 0:
        return None, None
    first_won, second_won = _num(row.get(f"{side}_1stWon")), _num(row.get(f"{side}_2ndWon"))
    if first_won is None or second_won is None:
        return None, None
    won = first_won + second_won
    if won < 0 or won > svpt:
        return None, None
    return svpt, won


def run(matches: pd.DataFrame, cfg: Gen2Config = Gen2Config(), seeder=None) -> Gen2State:
    """Replay the canonical table in match order. `seeder(pid, tour)` may return a rating-implied
    P(point on serve) for a player with no serve statistics; it must not see prices."""
    st = Gen2State(cfg=cfg)
    m = match_sort_key(matches)
    for row in m.to_dict("records"):
        tour = row.get("tour")
        level = row.get("level_canonical") or "OTHER"
        surface = row.get("surface")
        date = row.get("tourney_date")
        w, l = str(row.get("winner_id")), str(row.get("loser_id"))
        if seeder is not None:
            for pid in (w, l):
                if pid not in st.seeded and st.evidence(pid) < cfg.seed_below_points:
                    p = seeder(pid, tour)
                    if p is not None:
                        st.seed_from_rating(pid, p, tour)
        wp, ww = serve_points(row, "w")
        lp, lw = serve_points(row, "l")
        if wp and lp:
            st.observe(server=w, returner=l, points=wp, won=ww, tour=tour, level=level, surface=surface, date=date)
            st.observe(server=l, returner=w, points=lp, won=lw, tour=tour, level=level, surface=surface, date=date)
    return st
