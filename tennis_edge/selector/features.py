"""Features for the abstention model, and the four edges that are NOT the same thing.

The target this feeds is not "who wins". It is "is our disagreement with the price informative", which
is a different question with a different answer: we are globally worse than Kalshi at picking winners
(Wave 2, fact 3) and the only interesting question left is whether the subset where we disagree for good
reasons behaves differently from the subset where we disagree for bad ones.

Every feature here is knowable at the quote cutoff. That is not a convention, it is checked:
`assert_no_leakage` refuses any column derived from the outcome, the settlement, or a later quote.
"""
from __future__ import annotations

import numpy as np
import pandas as pd

FEATURE_VERSION = "features_v1"

#: columns that describe what happened AFTER the decision. Nothing derived from these may be a feature.
FORBIDDEN = ("y", "settlement", "result", "outcome", "pnl", "won", "clv")

FEATURES = (
    # how big is the disagreement, and in which direction
    "disagreement", "abs_disagreement", "raw_edge", "fee_adjusted_edge", "robust_edge",
    "uncertainty_adjusted_edge",
    # do our independent lanes agree with each other
    "lane_gap_gen2_elo", "lanes_agree", "lane_gap_sr_gen2", "n_lanes_agreeing",
    # how stable is the number under a defensible reparameterisation
    "env_width", "env_sign_stable",
    # how much evidence stands behind it
    "log_ev_min", "log_ev_side", "blend_weight", "log_n_matches_min", "data_quality",
    "identity_confidence", "days_stale", "serve_level",
    # what the market looks like
    "spread", "log_oi", "favouriteness", "is_underdog", "two_sided_gap",
    # how the market has been behaving (timestamp-safe)
    "move_6h_toward_us", "abs_move_6h", "volatility_24h", "log_volume_24h", "n_quotes_24h",
    "hours_since_last_change",
    # when
    "hours_to_sched", "quote_age_h",
    # where
    "is_itf", "is_challenger", "is_tour", "is_wta",
)


def assert_no_leakage(df: pd.DataFrame, features=FEATURES) -> None:
    """A feature whose NAME carries an outcome token is a bug, not a feature. Tokens, not substrings:
    "data_quality" contains a "y" and is fine; "won_rate" is not."""
    bad = [f for f in features if set(f.lower().split("_")) & set(FORBIDDEN)]
    if bad:
        raise ValueError(f"feature names look like outcome information: {bad}")


def edges(d: pd.DataFrame) -> pd.DataFrame:
    """The four edges. They differ, and the difference is the whole point of Phase 3.

    RAW                 what a naive screen would print
    FEE_ADJUSTED        what the exchange leaves after the taker fee
    UNCERTAINTY_ADJUSTED  fee-adjusted, less one standard width of our own parameter uncertainty
    ROBUST              the WORST fee-adjusted edge over the defensible parameter set
    """
    out = pd.DataFrame(index=d.index)
    out["raw_edge"] = d.p_fair - d.kalshi_ask
    out["fee_adjusted_edge"] = out.raw_edge - d.fee
    sigma = 0.5 * (d.p_env_max - d.p_env_min)
    out["sigma_env"] = sigma
    out["uncertainty_adjusted_edge"] = out.fee_adjusted_edge - sigma
    out["robust_edge"] = d.p_env_min - d.kalshi_ask - d.fee
    return out


def build_features(d: pd.DataFrame) -> pd.DataFrame:
    assert_no_leakage(d)
    e = edges(d)
    mid = d.kalshi_mid
    f = pd.DataFrame(index=d.index)
    f["disagreement"] = d.p_fair - mid
    f["abs_disagreement"] = (d.p_fair - mid).abs()
    f["raw_edge"] = e.raw_edge
    f["fee_adjusted_edge"] = e.fee_adjusted_edge
    f["robust_edge"] = e.robust_edge
    f["uncertainty_adjusted_edge"] = e.uncertainty_adjusted_edge

    dis_gen2 = d.p_fair - mid
    dis_elo = d.p_elo - mid
    dis_sr = d.p_sr - mid
    f["lane_gap_gen2_elo"] = (d.p_fair - d.p_elo).abs()
    f["lane_gap_sr_gen2"] = (d.p_sr - d.p_fair).abs()
    f["lanes_agree"] = ((np.sign(dis_gen2) == np.sign(dis_elo)) & (dis_gen2.abs() > 1e-9)).astype(float)
    f["n_lanes_agreeing"] = sum((np.sign(x) == np.sign(dis_gen2)).astype(float) for x in (dis_elo, dis_sr))

    f["env_width"] = d.p_env_max - d.p_env_min
    f["env_sign_stable"] = ((d.p_env_min - d.kalshi_ask - d.fee > 0) |
                            (d.p_env_max - d.kalshi_ask - d.fee < 0)).astype(float)

    f["log_ev_min"] = np.log1p(d.ev_min) / 10.0
    f["log_ev_side"] = np.log1p(d.ev_side) / 10.0
    f["blend_weight"] = d.blend_weight
    f["log_n_matches_min"] = np.log1p(d.n_matches_min) / 5.0
    f["data_quality"] = d.data_quality
    f["identity_confidence"] = d.identity_confidence
    f["days_stale"] = np.minimum(d.days_stale_max.fillna(365), 365) / 365.0
    f["serve_level"] = d.serve_level

    f["spread"] = d.spread
    f["log_oi"] = np.log1p(d.kalshi_oi) / 10.0
    f["favouriteness"] = (mid - 0.5).abs()
    f["is_underdog"] = (mid < 0.5).astype(float)
    f["two_sided_gap"] = d.two_sided_gap.fillna(0.0)

    toward = np.sign(f.disagreement).replace(0, 1)
    f["move_6h_toward_us"] = d.mv_move_6h.fillna(0.0) * toward
    f["abs_move_6h"] = d.mv_abs_move_6h.fillna(0.0)
    f["volatility_24h"] = d.mv_volatility_24h.fillna(0.0)
    f["log_volume_24h"] = np.log1p(d.mv_volume_24h.fillna(0.0)) / 10.0
    f["n_quotes_24h"] = d.mv_n_quotes_24h.fillna(0.0) / 24.0
    f["hours_since_last_change"] = np.minimum(d.mv_hours_since_last_change.fillna(48.0), 48.0) / 48.0

    f["hours_to_sched"] = np.minimum(d.hours_to_sched, 72.0) / 72.0
    f["quote_age_h"] = np.minimum(d.quote_age_s / 3600.0, 24.0) / 24.0

    f["is_itf"] = (d.level == "ITF").astype(float)
    f["is_challenger"] = (d.level == "CHALLENGER").astype(float)
    f["is_tour"] = d.level.isin(("TOUR_500_250", "MASTERS_1000", "GRAND_SLAM", "WTA_125")).astype(float)
    f["is_wta"] = (d.tour == "WTA").astype(float)
    return f[list(FEATURES)].astype(float).fillna(0.0)
