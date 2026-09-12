"""Fit the production rating state (Elo family + serve/return) on the full canonical table and persist it
with provenance, so `run_tennis` prices from a versioned artifact instead of re-replaying 1.6M matches.

Artifact: data/processed/ratings_<tour>.json
  {model_version, built_at, matches_sha256, elo_config, n_matches, as_of_date,
   players: {id: {elo, n, last_date, surfaces: {Hard: [rating, n], ...}, sr_s, sr_r, sr_points, name}}}
The as_of_date is the max tourney_date consumed; predictions made later than that carry
`ratings_as_of` so staleness is visible (health gate TENNIS-14).
"""
from __future__ import annotations

import hashlib
import json
import os
from datetime import datetime, timezone

import pandas as pd

from tennis_edge.models.elo import Elo, EloConfig, match_sort_key
from tennis_edge.models.serve_return import ServeReturnModel, SRConfig

PROJ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODEL_VERSION = "elo_surface_k_lo+sr_v0.1"
PROD_ELO = EloConfig(k0=180, use_surface=True, use_level_k=True, use_level_prior=True)


def fit_state(matches: pd.DataFrame, tour: str, elo_cfg: EloConfig = PROD_ELO, sr_cfg: SRConfig = SRConfig()) -> dict:
    # ONE rating entity per player. Rows are keyed on the CANONICAL player id, which is the Sackmann id
    # for Sackmann rows and the crosswalked Sackmann id for foreign rows whose BOTH players resolve to
    # exactly one Sackmann player (identity/crosswalk.py). Rows that do not crosswalk are excluded, so a
    # duplicate rating entity ("Zverev twice") remains impossible while the fresher mirror rows are used.
    m = matches[(matches.tour == tour) & (matches.outcome_type != "WALKOVER") & matches.tourney_date.notna()].copy()
    if "canonical_id_status" in m.columns:
        m = m[m.canonical_id_status == "MAPPED"].copy()
        m["winner_id"] = m["canonical_winner_id"].astype(str)
        m["loser_id"] = m["canonical_loser_id"].astype(str)
    else:                                  # pre-crosswalk artifacts: fall back to the old, safe restriction
        m = m[m.id_system == "sackmann"].copy()
    m["tourney_date"] = pd.to_datetime(m["tourney_date"]).dt.date
    m = match_sort_key(m)
    elo = Elo(elo_cfg); elo.run(m)
    sr = ServeReturnModel(sr_cfg); sr.run(m)
    names = {}
    for w, l, wn, ln in zip(m.winner_id, m.loser_id, m.winner_name, m.loser_name):
        names[w] = wn; names[l] = ln
    players = {}
    for p, r in elo.r.items():
        surfaces = {s: [elo.rs[(p, s)], elo.ns[(p, s)]] for s in ("Hard", "Clay", "Grass", "Carpet") if (p, s) in elo.rs}
        s_ab, r_ab = sr.abilities(p)
        players[p] = {"elo": r, "n": elo.n[p], "last_date": str(elo.last_date.get(p)), "surfaces": surfaces,
                      "sr_s": s_ab, "sr_r": r_ab, "sr_points": sr.points_seen(p), "name": names.get(p)}
    id_systems = {k: int(v) for k, v in m["id_system"].value_counts().items()} if "id_system" in m else {}
    return {"model_version": MODEL_VERSION, "tour": tour, "id_systems_used": id_systems, "built_at": datetime.now(timezone.utc).isoformat(), "elo_config": elo_cfg.__dict__,
            "sr_config": sr_cfg.__dict__, "n_matches": int(len(m)), "as_of_date": str(m.tourney_date.max()),
            "baselines": {f"{k[0]}|{k[1]}": sr.base_num[k] / sr.base_den[k] for k in sr.base_den if sr.base_den[k] > 0}, "players": players}


def save_state(state: dict, path: str):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        json.dump(state, f, separators=(",", ":"), default=str)


def load_state(path: str) -> dict:
    return json.load(open(path))


if __name__ == "__main__":
    import argparse, logging
    logging.basicConfig(level=logging.ERROR)
    ap = argparse.ArgumentParser(); ap.add_argument("--tour", default="ATP"); a = ap.parse_args()
    mp = os.path.join(PROJ, "data", "processed", "matches.parquet")
    st = fit_state(pd.read_parquet(mp), a.tour)
    st["matches_sha256"] = hashlib.sha256(open(mp, "rb").read()).hexdigest()
    save_state(st, os.path.join(PROJ, "data", "processed", f"ratings_{a.tour}.json"))
    print(a.tour, st["n_matches"], "players", len(st["players"]), "as_of", st["as_of_date"])
