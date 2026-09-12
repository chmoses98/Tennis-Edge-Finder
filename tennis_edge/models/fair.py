"""One place where "our fair probability" is computed, so the research and the board cannot drift apart.

Given walk-forward rating states and a match, this produces the four fundamental lanes (rank-free):

    MODEL_1  Elo               ratings only
    MODEL_2  Gen-1 serve/return structural
    MODEL_3  Gen-2 blended     structural, shrunk toward the rating-implied point probabilities in
                               proportion to the serve evidence the thinner player actually has

and it does so under a CONFIGURATION, because the same match priced under a different but equally
defensible parameterisation is the cheapest honest test of whether an edge is real. `FairConfig` holds
the assumptions a reasonable person could argue about; `PERTURBATIONS` is the defensible set we vary
over, and an edge that changes sign inside that set is not an edge, it is a parameter choice.

No prices enter this module. It is Model 3 discipline: the import graph is checked by tests.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, replace
from datetime import date as _date

from tennis_edge.models.elo import expected as elo_expected
from tennis_edge.models.gen2 import Gen2Config
from tennis_edge.rules.formats import MatchFormat, TOUR_SINGLES_BO3
from tennis_edge.sim.analytic import match_win_prob, point_probs_from_match_prob

FAIR_VERSION = "fair_v1"

_MWP: dict = {}
_INV: dict = {}


def _mwp(pa: float, pb: float, fmt: MatchFormat) -> float:
    key = (round(float(pa), 3), round(float(pb), 3), fmt.best_of, fmt.tiebreak_at, fmt.tiebreak_to,
           fmt.final_set, fmt.no_ad)
    v = _MWP.get(key)
    if v is None:
        v = match_win_prob(key[0], key[1], fmt)
        _MWP[key] = v
    return v


def _inv(p_match: float, lvl: float):
    key = (round(float(p_match), 3), round(float(lvl), 2))
    v = _INV.get(key)
    if v is None:
        v = point_probs_from_match_prob(min(max(key[0], 1e-4), 1 - 1e-4), key[1], TOUR_SINGLES_BO3)
        _INV[key] = v
    return v


@dataclass(frozen=True)
class FairConfig:
    """The assumptions a reasonable person could argue about."""
    name: str = "base"
    surface_w_max: float = 0.5              # how far a surface-specific Elo pulls the overall rating
    surface_n_half: float = 20.0
    gen2_prior_points: float = 500.0        # serve/return shrinkage toward the baseline
    gen2_surface_prior_points: float = 1500.0
    blend_points: float = 1500.0            # evidence at which Gen-2 gets half the weight vs the rating
    extra_half_life_days: float | None = None   # additional recency discount on Gen-2 evidence


#: the defensible uncertainty set. Centre plus one-at-a-time moves plus two corners; an edge that
#: survives all of these is ROBUST in the only sense we can check without new data.
PERTURBATIONS = (
    FairConfig(),
    FairConfig(name="surface_pool_low", surface_w_max=0.25),
    FairConfig(name="surface_pool_high", surface_w_max=0.75),
    FairConfig(name="shrink_low", gen2_prior_points=250.0),
    FairConfig(name="shrink_high", gen2_prior_points=1000.0),
    FairConfig(name="surface_dev_loose", gen2_surface_prior_points=750.0),
    FairConfig(name="surface_dev_tight", gen2_surface_prior_points=3000.0),
    FairConfig(name="blend_structural", blend_points=750.0),
    FairConfig(name="blend_rating", blend_points=3000.0),
    FairConfig(name="recency_hard", extra_half_life_days=180.0),
    FairConfig(name="recency_soft", extra_half_life_days=365.0),
    FairConfig(name="corner_structural", surface_w_max=0.75, gen2_prior_points=250.0, blend_points=750.0),
    FairConfig(name="corner_rating", surface_w_max=0.25, gen2_prior_points=1000.0, blend_points=3000.0,
               extra_half_life_days=180.0),
)


def _surface_rating(rec: dict, surface: str | None, cfg: FairConfig) -> float:
    r = rec["elo"]
    surfaces = rec.get("surfaces") or {}
    if surface and surface in surfaces:
        rs, ns = surfaces[surface]
        w = cfg.surface_w_max * ns / (ns + cfg.surface_n_half)
        return (1 - w) * r + w * rs
    return r


def _decay_gen2(state, on: _date, half_life: float | None):
    """Apply an EXTRA recency discount to every stored ability, in place, on a private state object.

    Down-weighting old evidence can only move a player toward the baseline, so this perturbation is
    conservative by construction: it never invents confidence the data does not support.
    """
    if not half_life:
        return state
    for store in (state.serve, state.ret, state.surf_serve, state.surf_ret):
        for ab in store.values():
            if ab.last is None:
                continue
            days = (on - ab.last).days
            if days > 0:
                f = 0.5 ** (days / half_life)
                ab.num *= f
                ab.den *= f
    return state


@dataclass(frozen=True)
class Fair:
    p_elo: float
    p_sr: float
    p_gen2: float
    p_gen2_blend: float
    blend_weight: float
    evidence_a: float
    evidence_b: float
    serve_level: float                # (pa + 1 - pb) / 2: how dominant serve is in this matchup
    config: str


def compute_fair(asof, pa_id: str, pb_id: str, *, tour: str, level: str, surface: str | None,
                 fmt: MatchFormat, on: _date, cfg: FairConfig = FairConfig()) -> Fair | None:
    """Our probability that player A beats player B, from ratings known the morning of `on`."""
    ra_rec, rb_rec = asof.state(pa_id, on), asof.state(pb_id, on)
    if not ra_rec or not rb_rec or ra_rec.get("elo") is None or rb_rec.get("elo") is None:
        return None
    ra, rb = _surface_rating(ra_rec, surface, cfg), _surface_rating(rb_rec, surface, cfg)
    spw = asof.baselines.get(f"{tour}|{surface}") or (0.64 if tour == "ATP" else 0.57)
    p_elo = _mwp(*_inv(elo_expected(ra, rb), 2 * spw), fmt)

    base = math.log(spw / (1 - spw))
    sr_pa = 1 / (1 + math.exp(-(base + ra_rec["sr_s"] - rb_rec["sr_r"])))
    sr_pb = 1 - 1 / (1 + math.exp(-(base + rb_rec["sr_s"] - ra_rec["sr_r"])))
    p_sr = _mwp(sr_pa, sr_pb, fmt)

    g2 = asof.gen2_state([pa_id, pb_id], on)
    g2.cfg = replace(Gen2Config(**g2.cfg.to_dict()), prior_points=cfg.gen2_prior_points,
                     surface_prior_points=cfg.gen2_surface_prior_points)
    _decay_gen2(g2, on, cfg.extra_half_life_days)
    gpa, gpb = g2.predict_point_probs(pa_id, pb_id, tour, level, surface)
    p_gen2 = _mwp(gpa, gpb, fmt)

    ev_a, ev_b = g2.evidence(pa_id), g2.evidence(pb_id)
    ev_min = min(ev_a, ev_b)
    w = ev_min / (ev_min + cfg.blend_points)
    serve_level = 0.5 * (gpa + (1.0 - gpb))
    epa, epb = _inv(p_elo, 2 * serve_level)
    p_blend = _mwp(w * gpa + (1 - w) * epa, w * gpb + (1 - w) * epb, fmt)
    return Fair(p_elo=p_elo, p_sr=p_sr, p_gen2=p_gen2, p_gen2_blend=p_blend, blend_weight=w,
                evidence_a=ev_a, evidence_b=ev_b, serve_level=serve_level, config=cfg.name)


def fair_envelope(asof, pa_id: str, pb_id: str, *, tour: str, level: str, surface: str | None,
                  fmt: MatchFormat, on: _date, configs=PERTURBATIONS) -> dict:
    """Every configuration in the defensible set, and the envelope they trace."""
    out = {}
    for cfg in configs:
        f = compute_fair(asof, pa_id, pb_id, tour=tour, level=level, surface=surface, fmt=fmt, on=on, cfg=cfg)
        if f is not None:
            out[cfg.name] = f
    if not out:
        return {}
    vals = [f.p_gen2_blend for f in out.values()]
    return {"fairs": out, "p_min": min(vals), "p_max": max(vals), "p_base": out["base"].p_gen2_blend
            if "base" in out else sum(vals) / len(vals), "n_configs": len(out)}
