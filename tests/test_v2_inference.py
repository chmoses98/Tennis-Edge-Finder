"""Train/serve parity: live inference over persisted states reproduces the replay's own prediction."""
import json
import os
from datetime import timedelta

import numpy as np
import pandas as pd

from tennis_edge.v2.inference import ProjectionV2
from tennis_edge.v2.production import build_state, load_coefficients
from tennis_edge.v2.replay import finalise, replay
from tennis_edge.v2.stacker import FittedStacker
from tests.test_v2_engine import synthetic


def _roundtrip(state):
    return json.loads(json.dumps(state, default=str))


def test_live_inference_equals_replay_record_for_the_same_state():
    m = synthetic(n=1500)
    hist, nxt = m.iloc[:-1].copy(), m.iloc[[-1]].copy()
    # put the last match in a NEW event so 'matches already played in this event' is 0 for both, as live
    nxt["tourney_id"] = "new_event"
    nxt["tourney_date"] = hist["tourney_date"].max() + timedelta(days=7)
    coef = load_coefficients()
    st = _roundtrip(build_state(hist, "ATP", coef))
    pv = ProjectionV2(st, coef)
    full = pd.concat([hist, nxt], ignore_index=True)
    rec, _ = replay(full, "ATP", record_from=2015)
    rec = finalise(rec)
    last = rec.iloc[[-1]].reset_index(drop=True)
    a, b = last["a_id"].iloc[0], last["b_id"].iloc[0]
    fr = pv.frame(a, b, on=nxt["tourney_date"].iloc[0], level=last["level"].iloc[0], surface=last["surface"].iloc[0],
                  best_of=int(last["best_of"].iloc[0]))
    shared = [c for c in fr.columns if c in last.columns and c not in ("y", "age_a", "age_b", "season")]
    for c in shared:
        x, y = fr[c].iloc[0], last[c].iloc[0]
        if isinstance(x, (float, np.floating)) or isinstance(y, (float, np.floating)):
            assert (np.isnan(x) and np.isnan(y)) or abs(float(x) - float(y)) < 1e-12, (c, x, y)
        else:
            assert x == y, (c, x, y)
    fr[["age_a", "age_b"]] = last[["age_a", "age_b"]].to_numpy()
    base = FittedStacker.from_dict(coef["tours"]["ATP"]["variants"]["base"])
    assert abs(base.predict(fr)[0] - base.predict(last)[0]) < 1e-12


def test_symmetry_and_envelope_of_live_projection():
    m = synthetic(n=1200)
    coef = load_coefficients()
    pv = ProjectionV2(_roundtrip(build_state(m, "ATP", coef)), coef)
    on = m["tourney_date"].max() + timedelta(days=3)
    r1 = pv.project("p1", "p2", on=on, level="TOUR_500_250", surface="Hard")
    r2 = pv.project("p2", "p1", on=on, level="TOUR_500_250", surface="Hard")
    assert abs(r1["p"] + r2["p"] - 1) < 1e-9
    assert r1["p_low"] <= r1["p"] <= r1["p_high"]
    assert r1["grade"] in ("HIGH", "MEDIUM", "LOW", "POOR")


def test_stale_level_neutralises_schedule_features_and_widens_envelope():
    m = synthetic(n=1200)
    coef = load_coefficients()
    pv = ProjectionV2(_roundtrip(build_state(m, "ATP", coef)), coef)
    on = m["tourney_date"].max() + timedelta(days=200)
    r = pv.project("p1", "p2", on=on, level="ITF", surface="Clay")
    assert r["context_neutralised"] and any(t.startswith("CONTEXT_NEUTRALISED") for t in r["tags"])
    for f in ("rest", "layoff60", "layoff180", "n14", "mins7", "ret30", "surf_switch", "form30"):
        assert r["features"][f] == 0.0
    assert r["rating_drift_logit_1p645"] > 0 and r["grade"] != "HIGH"


def test_evidence_reports_true_staleness_and_old_players_grade_poor():
    m = synthetic(n=1200)
    coef = load_coefficients()
    pv = ProjectionV2(_roundtrip(build_state(m, "ATP", coef)), coef)
    on = m["tourney_date"].max() + timedelta(days=200)
    r = pv.project("p1", "p2", on=on, level="ITF", surface="Clay")
    assert r["evidence"]["days_since_last_result_in_data_a"] >= 200          # not the neutralised placeholder
    assert r["grade"] == "POOR" and any(t.startswith("STALE_PLAYER_RATING") for t in r["tags"])
