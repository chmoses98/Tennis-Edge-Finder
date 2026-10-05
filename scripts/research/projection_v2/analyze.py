#!/usr/bin/env python3
"""Projection V2 step 2: staged, preregistered analysis (research/projection_v2/PREREGISTRATION.md).

Stages (each one can only see the seasons it is allowed to see):
  select    2016-2020 only: Elo tournament, greedy block selection, form horizon, L2 -> FROZEN_CHALLENGER.json
  evaluate  <= 2024: incumbent vs challenger vs references, ablations, segments, seasons (needs the frozen spec)
  validate  adds 2025 (refuses to run without the frozen spec)
  holdout   adds 2026 (refuses to run without the frozen spec and a completed validate stage)
"""
from __future__ import annotations

import argparse, json, os, sys, time
from datetime import datetime, timezone

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from tennis_edge.v2.evaluate import cluster_bootstrap_diff, favourite_scores, reliability, scores  # noqa: E402
from tennis_edge.v2.stacker import BLOCK_ORDER, StackerSpec, level_group, walk_forward, fit  # noqa: E402

TOURS = ("ATP", "WTA")
SELECT = (2016, 2020)
EVAL = (2021, 2024)
VALID = 2025
HOLD = 2026
FORM_H = (30, 60, 120, 240)
C_GRID = (0.01, 0.1, 1.0, 10.0)
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "..", "research", "projection_v2")


def load(replay_dir, max_season):
    d = {}
    for t in TOURS:
        df = pd.read_parquet(os.path.join(replay_dir, f"replay_{t}.parquet"))
        d[t] = df[df.season <= max_season].reset_index(drop=True)
    return d


def ll(y, p):
    p = np.clip(p, 1e-6, 1 - 1e-6)
    return float(-np.mean(y * np.log(p) + (1 - y) * np.log(1 - p)))


def pooled_ll(dfs, preds, mask_fn):
    num = den = 0.0
    per = {}
    for t in TOURS:
        m = mask_fn(dfs[t])
        y = dfs[t]["y"].to_numpy()[m]
        v = ll(y, preds[t][m])
        per[t] = v
        num += v * m.sum()
        den += m.sum()
    return num / den, per


def sel_mask(df):
    return ((df.season >= SELECT[0]) & (df.season <= SELECT[1])).to_numpy()


# ------------------------------------------------------------------------------------------------ select
def stage_select(dfs, log):
    seasons = list(range(SELECT[0], SELECT[1] + 1))
    elo_names = sorted(c[3:] for c in dfs["ATP"].columns if c.startswith("pf_E"))
    tourn = {}
    for name in elo_names:
        pooled, per = pooled_ll(dfs, {t: dfs[t][f"pf_{name}"].to_numpy() for t in TOURS}, sel_mask)
        tourn[name] = {"pooled_ll": pooled, **{f"{t}_ll": per[t] for t in TOURS}}
    best_elo = min(tourn, key=lambda k: tourn[k]["pooled_ll"])
    log["elo_tournament_2016_2020"] = tourn
    log["chosen_elo"] = best_elo
    print("Elo tournament (2016-2020 log loss):")
    for k, v in sorted(tourn.items(), key=lambda kv: kv[1]["pooled_ll"]):
        print(f"  {k:16s} pooled {v['pooled_ll']:.5f}  ATP {v['ATP_ll']:.5f}  WTA {v['WTA_ll']:.5f}")

    def evaluate_spec(spec):
        preds = {t: walk_forward(dfs[t], spec, seasons) for t in TOURS}
        return pooled_ll(dfs, preds, sel_mask)

    blocks: list = []
    form_h = 120
    cur_pooled, cur_per = evaluate_spec(StackerSpec(elo=best_elo, blocks=()))
    log["greedy"] = [{"step": "base", "pooled_ll": cur_pooled, **cur_per}]
    print(f"base stacker (z only): pooled {cur_pooled:.5f} {cur_per}")
    for blk in BLOCK_ORDER:
        if blk == "form":
            trials = {}
            for h in FORM_H:
                trials[h] = evaluate_spec(StackerSpec(elo=best_elo, blocks=tuple(blocks + ["form"]), form_horizon=h))
            h_best = min(trials, key=lambda h: trials[h][0])
            log["form_horizon_trials"] = {str(h): {"pooled_ll": v[0], **v[1]} for h, v in trials.items()}
            new_pooled, new_per = trials[h_best]
            cand_h = h_best
        else:
            new_pooled, new_per = evaluate_spec(StackerSpec(elo=best_elo, blocks=tuple(blocks + [blk]), form_horizon=form_h))
            cand_h = form_h
        gain = {t: cur_per[t] - new_per[t] for t in TOURS}
        pooled_gain = cur_pooled - new_pooled
        keep = (all(g >= 0.0002 for g in gain.values())
                or (pooled_gain >= 0.0004 and all(g >= -0.0001 for g in gain.values())))
        log["greedy"].append({"step": blk, "pooled_ll": new_pooled, **new_per, "gain": gain,
                              "pooled_gain": pooled_gain, "kept": bool(keep), **({"form_horizon": cand_h} if blk == "form" else {})})
        print(f"  + {blk:8s} pooled {new_pooled:.5f} gain ATP {gain['ATP']:+.5f} WTA {gain['WTA']:+.5f} -> {'KEEP' if keep else 'drop'}")
        if keep:
            blocks.append(blk)
            cur_pooled, cur_per = new_pooled, new_per
            if blk == "form":
                form_h = cand_h
    c_trials = {}
    for C in C_GRID:
        c_trials[C] = evaluate_spec(StackerSpec(elo=best_elo, blocks=tuple(blocks), form_horizon=form_h, C=C))
    C_best = min(c_trials, key=lambda c: c_trials[c][0])
    log["C_trials"] = {str(c): {"pooled_ll": v[0], **v[1]} for c, v in c_trials.items()}
    spec = StackerSpec(elo=best_elo, blocks=tuple(blocks), form_horizon=form_h, C=C_best)
    frozen = {"frozen_at": datetime.now(timezone.utc).isoformat(), "spec": spec.to_dict(),
              "spec_fingerprint": spec.fingerprint(), "selection_window": list(SELECT),
              "selection_pooled_ll": c_trials[C_best][0], "selection_per_tour_ll": c_trials[C_best][1],
              "note": "Chosen on 2016-2020 only, per PREREGISTRATION.md section 3. Not to be edited."}
    return frozen


# ---------------------------------------------------------------------------------------------- evaluate
def candidates(dfs, spec, seasons):
    """Every lane's walk-forward predictions for the given seasons, per tour."""
    out = {}
    for t in TOURS:
        df = dfs[t]
        lanes = {"INCUMBENT": df["pf_incumbent"].to_numpy(), "FAIR_V1": df["pf_fair_v1"].to_numpy(),
                 f"ELO_RAW[{spec.elo}]": df[f"pf_{spec.elo}"].to_numpy(),
                 "ELO_PROD_RAW": df["pf_E_prod"].to_numpy()}
        lanes["ELO+PLATT"] = walk_forward(df, StackerSpec(elo=spec.elo, blocks=(), C=spec.C), seasons)
        lanes["CHALLENGER"] = walk_forward(df, spec, seasons)
        for blk in spec.blocks:
            ab = StackerSpec(elo=spec.elo, blocks=tuple(b for b in spec.blocks if b != blk),
                             form_horizon=spec.form_horizon, C=spec.C, window=spec.window)
            lanes[f"ABLATE-{blk}"] = walk_forward(df, ab, seasons)
        # additive ablation from the bare rating, for the "which additions mattered" table
        acc = []
        for blk in spec.blocks:
            acc.append(blk)
            lanes[f"ADD-{'+'.join(acc)}"] = walk_forward(
                df, StackerSpec(elo=spec.elo, blocks=tuple(acc), form_horizon=spec.form_horizon, C=spec.C), seasons)
        out[t] = lanes
    return out


def segment_cols(df):
    nmin = np.minimum(df["n_a"].to_numpy(), df["n_b"].to_numpy())
    ev = df["g2_ev_min"].to_numpy()
    fav = np.maximum(df["pf_incumbent"].to_numpy(), 1 - df["pf_incumbent"].to_numpy())
    return {
        "level": level_group(df["level"].to_numpy()),
        "surface": df["surface"].fillna("unknown").to_numpy(),
        "experience": np.select([nmin < 10, nmin < 50, nmin < 200], ["<10", "10-49", "50-199"], ">=200"),
        "serve_evidence": np.select([ev < 1, ev < 1000, ev < 5000, ev < 20000], ["none", "<1k", "1k-5k", "5k-20k"], ">=20k"),
        "favourite_prob": np.select([fav < 0.6, fav < 0.7, fav < 0.8, fav < 0.9], ["50-60", "60-70", "70-80", "80-90"], "90-100"),
        "form_data": np.where(np.minimum(df["cnt120_a"].to_numpy(), df["cnt120_b"].to_numpy()) >= 3, "both_recent", "thin_recent"),
        "season": df["season"].astype(str).to_numpy(),
    }


def report(dfs, preds, seasons, nboot):
    res = {}
    for t in TOURS:
        df = dfs[t]
        m = df["season"].isin(seasons).to_numpy()
        y = df["y"].to_numpy()[m]
        cl = (df["tourney_id"].astype(str) + "|" + df["season"].astype(str)).to_numpy()[m]
        inc = preds[t]["INCUMBENT"][m]
        r = {"lanes": {}, "vs_incumbent": {}, "segments": {}, "reliability": {}}
        for name, p in preds[t].items():
            pm = p[m]
            r["lanes"][name] = {**scores(y, pm), **favourite_scores(y, pm)}
            if name != "INCUMBENT":
                r["vs_incumbent"][name] = cluster_bootstrap_diff(y, pm, inc, cl, n_boot=nboot)
        if "ELO_RAW" in "".join(preds[t]):
            pass
        r["vs_elo_platt"] = cluster_bootstrap_diff(y, preds[t]["CHALLENGER"][m], preds[t]["ELO+PLATT"][m], cl, n_boot=nboot)
        r["reliability"] = {k: reliability(y, preds[t][k][m]) for k in ("INCUMBENT", "CHALLENGER")}
        segs = segment_cols(df.loc[m].reset_index(drop=True))
        ch = preds[t]["CHALLENGER"][m]
        for sname, vals in segs.items():
            r["segments"][sname] = {}
            for v in sorted(set(vals)):
                sm = vals == v
                if sm.sum() < 300:
                    continue
                r["segments"][sname][v] = {
                    "n": int(sm.sum()),
                    "incumbent": scores(y[sm], inc[sm]), "challenger": scores(y[sm], ch[sm]),
                    "diff": cluster_bootstrap_diff(y[sm], ch[sm], inc[sm], cl[sm], n_boot=max(400, nboot // 4))}
        res[t] = r
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("stage", choices=("select", "evaluate", "validate", "holdout"))
    ap.add_argument("--replay", default="/home/user/work/v2/replay")
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--nboot", type=int, default=2000)
    a = ap.parse_args()
    os.makedirs(a.out, exist_ok=True)
    frozen_path = os.path.join(a.out, "FROZEN_CHALLENGER.json")
    t0 = time.time()
    if a.stage == "select":
        if os.path.exists(frozen_path):
            raise SystemExit("FROZEN_CHALLENGER.json exists: the challenger is frozen; selection cannot be re-run")
        dfs = load(a.replay, SELECT[1])
        log = {}
        frozen = stage_select(dfs, log)
        json.dump(log, open(os.path.join(a.out, "selection_log.json"), "w"), indent=1, default=lambda o: o.item() if hasattr(o, "item") else str(o))
        json.dump(frozen, open(frozen_path, "w"), indent=1)
        print(json.dumps(frozen, indent=1))
        return
    if not os.path.exists(frozen_path):
        raise SystemExit("no FROZEN_CHALLENGER.json: run the select stage first")
    fz = json.load(open(frozen_path))
    s = fz["spec"]
    spec = StackerSpec(elo=s["elo"], blocks=tuple(s["blocks"]), form_horizon=s["form_horizon"], C=s["C"], window=s["window"])
    assert spec.fingerprint() == fz["spec_fingerprint"], "frozen spec was edited"
    if a.stage == "evaluate":
        seasons, maxs = list(range(EVAL[0], EVAL[1] + 1)), EVAL[1]
    elif a.stage == "validate":
        seasons, maxs = list(range(EVAL[0], VALID + 1)), VALID
    else:
        if not os.path.exists(os.path.join(a.out, "results_validate.json")):
            raise SystemExit("holdout refused: the validate stage has not been run")
        seasons, maxs = [HOLD], HOLD
    dfs = load(a.replay, maxs)
    preds = candidates(dfs, spec, seasons)
    res = report(dfs, preds, seasons, a.nboot)
    res["_meta"] = {"stage": a.stage, "seasons": seasons, "spec": fz["spec"], "spec_fingerprint": fz["spec_fingerprint"],
                    "computed_at": datetime.now(timezone.utc).isoformat(), "seconds": round(time.time() - t0, 1)}
    json.dump(res, open(os.path.join(a.out, f"results_{a.stage}.json"), "w"), indent=1, default=float)
    # per-match predictions for downstream (market benchmark after freeze, derivative validation)
    rows = []
    for t in TOURS:
        df = dfs[t]
        m = df["season"].isin(seasons).to_numpy()
        keep = df.loc[m, ["uid", "date", "season", "tourney_id", "level", "surface", "best_of", "y", "a_id", "b_id"]].copy()
        keep["tour"] = t
        for name in ("INCUMBENT", "CHALLENGER", "FAIR_V1", "ELO+PLATT"):
            keep[name] = preds[t][name][m]
        rows.append(keep)
    pd.concat(rows).to_parquet(os.path.join(a.out, f"predictions_{a.stage}.parquet"), index=False)
    for t in TOURS:
        print(t)
        for name, v in res[t]["vs_incumbent"].items():
            print(f"  {name:40s} dBrier {v['brier_diff']:+.5f} [{v['brier_ci'][0]:+.5f},{v['brier_ci'][1]:+.5f}]  dLL {v['ll_diff']:+.5f}")


if __name__ == "__main__":
    main()
