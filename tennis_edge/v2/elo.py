"""Configurable chronological Elo for the V2 rating tournament.

A superset of `tennis_edge.models.elo.Elo`: with mov=None and layoff_boost=0 it reproduces the Gen-1
class exactly (tests/test_v2_engine.py asserts this against the production configuration), so the
incumbent and every challenger are scored by the same code path.

Additions, each OFF unless configured:
  * margin of victory (``mov``): the K-factor is scaled by how decisively the match was won,
    k_eff = k * (mov_a + mov_b * d), d = (games_w - games_l) / (games_w + games_l). A 6-0 6-0 win says more
    about relative strength than a 7-6 7-6 win; both are opponent-adjusted because the update is still
    (result - expected). Retirements and matches without a parsed score use multiplier 1.
  * layoff boost (``layoff_boost``): after a long absence a rating is less certain, so it moves faster:
    k_eff = k * (1 + c * clip((days_since_last - 60) / 300, 0, 1)).

Ratings used to predict a match are always the ratings BEFORE that match is applied.
"""
from __future__ import annotations

from dataclasses import dataclass, field, asdict


def _default_level_k():
    return {"GRAND_SLAM": 1.1, "MASTERS_1000": 1.0, "TOUR_FINALS": 1.0, "TOUR_500_250": 1.0, "OLYMPICS": 1.0,
            "TEAM": 0.9, "CHALLENGER": 0.9, "WTA_125": 0.9, "ITF": 0.8, "OTHER": 0.8}


def _default_level_prior():
    return {"GRAND_SLAM": 1550.0, "MASTERS_1000": 1550.0, "TOUR_500_250": 1500.0, "TOUR_FINALS": 1600.0,
            "OLYMPICS": 1500.0, "TEAM": 1450.0, "CHALLENGER": 1400.0, "WTA_125": 1400.0, "ITF": 1300.0, "OTHER": 1350.0}


@dataclass(frozen=True)
class EloV2Config:
    name: str = "elo"
    k0: float = 250.0
    offset: float = 5.0
    shape: float = 0.4
    initial: float = 1500.0
    use_level_prior: bool = True
    use_level_k: bool = False
    surface_w_max: float = 0.0          # 0 = no surface pooling
    surface_n_half: float = 20.0
    retirement_weight: float = 0.5
    mov_a: float | None = None          # None = no margin-of-victory scaling
    mov_b: float = 0.0
    layoff_boost: float = 0.0
    #: reproduce Gen-1's surface seeding exactly: on a player's FIRST match on a surface Gen-1 seeds the
    #: surface rating from the POST-update overall rating and then adds the update again, counting that
    #: match twice. True only for the incumbent replica; V2 configurations seed from the pre-match rating.
    gen1_surface_seed: bool = False
    level_k: dict = field(default_factory=_default_level_k, compare=False, hash=False)
    level_prior: dict = field(default_factory=_default_level_prior, compare=False, hash=False)

    def to_dict(self):
        return asdict(self)


def expected(ra: float, rb: float) -> float:
    return 1.0 / (1.0 + 10.0 ** ((rb - ra) / 400.0))


class EloV2:
    __slots__ = ("cfg", "r", "n", "rs", "ns", "last")

    def __init__(self, cfg: EloV2Config):
        self.cfg = cfg
        self.r: dict = {}
        self.n: dict = {}
        self.rs: dict = {}
        self.ns: dict = {}
        self.last: dict = {}

    def init(self, p, level):
        if p not in self.r:
            c = self.cfg
            self.r[p] = c.level_prior.get(level, c.initial) if c.use_level_prior else c.initial
            self.n[p] = 0

    def rating(self, p, surface) -> float:
        r = self.r[p]
        c = self.cfg
        if c.surface_w_max and surface:
            key = (p, surface)
            ns = self.ns.get(key, 0)
            if ns:
                w = c.surface_w_max * ns / (ns + c.surface_n_half)
                return (1 - w) * r + w * self.rs[key]
        return r

    def predict(self, a, b, surface, level) -> float:
        self.init(a, level)
        self.init(b, level)
        return expected(self.rating(a, surface), self.rating(b, surface))

    def _k(self, p, level, date) -> float:
        c = self.cfg
        k = c.k0 / (self.n[p] + c.offset) ** c.shape
        if c.use_level_k:
            k *= c.level_k.get(level, 1.0)
        if c.layoff_boost and date is not None:
            last = self.last.get(p)
            if last is not None:
                days = (date - last).days
                if days > 60:
                    k *= 1.0 + c.layoff_boost * min((days - 60) / 300.0, 1.0)
        return k

    def update(self, w, l, surface, level, date, retired: bool, dominance: float | None):
        c = self.cfg
        self.init(w, level)
        self.init(l, level)
        pw = expected(self.rating(w, surface), self.rating(l, surface))
        weight = c.retirement_weight if retired else 1.0
        if c.mov_a is not None and not retired and dominance is not None:
            weight *= c.mov_a + c.mov_b * dominance
        kw, kl = self._k(w, level, date), self._k(l, level, date)
        delta = 1.0 - pw
        self.r[w] += weight * kw * delta
        self.r[l] -= weight * kl * delta
        if c.surface_w_max and surface:
            for p, sgn, kk in ((w, 1.0, kw), (l, -1.0, kl)):
                key = (p, surface)
                if key not in self.rs:
                    self.rs[key] = self.r[p] if c.gen1_surface_seed else self.r[p] - sgn * weight * kk * delta
                self.rs[key] += sgn * weight * kk * delta
                self.ns[key] = self.ns.get(key, 0) + 1
        self.n[w] += 1
        self.n[l] += 1
        if date is not None:
            self.last[w] = date
            self.last[l] = date

    def state(self, p) -> dict:
        """JSON-serialisable state of one player (for live inference artifacts)."""
        return {"r": self.r.get(p), "n": self.n.get(p, 0),
                "last": str(self.last[p]) if p in self.last else None,
                "surf": {s: [self.rs[(p, s)], self.ns[(p, s)]] for s in ("Hard", "Clay", "Grass", "Carpet")
                         if (p, s) in self.rs}}
