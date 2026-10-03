"""The research graph (tennis_edge.research_export) against the vendored contract 1.1.0.

Inputs are REAL tennis-data records: the v1 slate fixture (tests/fixtures/app_export, six match packets) plus
tests/fixtures/research_export, carved from tennis-data @ 23add39d9 for exactly those six matches (rating-state
records of their players and every namesake + the top-10 active players per tour, their prediction-ledger rows and
settlement rows, 2026-10-02 Kalshi capture quotes, first-ball truths, Model 4 rows and external dislocation rows;
record fields reduced to the ones the exporter reads, no value altered). The repository's committed research studies
(research/market_benchmark, research/elo_study) are read in place.
"""
from __future__ import annotations

import glob
import hashlib
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO / "contract"))

from edge_finder_contract import CAPABILITIES, packet, research as R, sync, timeutil  # noqa: E402
from tennis_edge import app_export as ax  # noqa: E402
from tennis_edge import research_export as rx  # noqa: E402

V1_FIXTURE = REPO / "tests" / "fixtures" / "app_export"
RESEARCH_FIXTURE = REPO / "tests" / "fixtures" / "research_export"
NOW = "2026-10-02T13:45:00Z"
TOP_N = 5

#: audit_tennis.md §4 / §10 as published for the full fixture (every input present)
EXPECTED_CAPABILITIES = {
    "team_profiles": "UNAVAILABLE", "player_profiles": "PARTIAL", "event_research": "PARTIAL", "team_metrics": "UNAVAILABLE",
    "player_metrics": "PARTIAL", "team_game_logs": "UNAVAILABLE", "player_game_logs": "UNAVAILABLE",
    "historical_results": "UNAVAILABLE", "opponents": "UNAVAILABLE", "opponent_adjustment": "PARTIAL",
    "schedule_strength": "UNAVAILABLE", "recent_form_windows": "UNAVAILABLE", "usage": "UNAVAILABLE", "lineups": "UNAVAILABLE",
    "injuries": "UNAVAILABLE", "matchup_metrics": "PARTIAL", "projection_distributions": "RESEARCH", "raw_projections": "VERIFIED",
    "market_prices": "VERIFIED", "market_price_history": "VERIFIED", "advanced_stats": "UNAVAILABLE", "situational_splits": "PARTIAL",
    "player_props": "UNAVAILABLE", "team_props": "UNAVAILABLE", "game_markets": "VERIFIED", "play_by_play": "UNAVAILABLE",
    "weather": "UNAVAILABLE", "venue_effects": "UNAVAILABLE", "calibration": "PARTIAL", "historical_accuracy": "PARTIAL",
    "clv": "PARTIAL", "wager_history": "UNAVAILABLE", "rankings": "PARTIAL", "time_series": "PARTIAL", "comparisons": "PARTIAL",
    "search": "VERIFIED",
}


@pytest.fixture
def data_root(tmp_path: Path) -> Path:
    root = tmp_path / "data"
    shutil.copytree(V1_FIXTURE, root)
    shutil.copytree(RESEARCH_FIXTURE, root, dirs_exist_ok=True)
    return root


def _v1(data_root: Path, out: Path) -> dict:
    return ax.export(str(data_root), str(out), now=timeutil.parse_ts(NOW))


def _explorer(data_root: Path, out: Path, **kw) -> dict:
    return rx.export_explorer(str(out), str(data_root), top_n=kw.pop("top_n", TOP_N), **kw)


def _digests(root: Path, *, explorer: bool) -> dict[str, str]:
    out = {}
    for p in glob.glob(str(root / "**" / "*.json"), recursive=True):
        rel = os.path.relpath(p, root)
        if rel.startswith("explorer" + os.sep) == explorer:
            out[rel] = hashlib.sha256(Path(p).read_bytes()).hexdigest()
    return out


@pytest.fixture
def published(data_root: Path, tmp_path: Path) -> Path:
    out = tmp_path / "app"
    _v1(data_root, out)
    _explorer(data_root, out)
    return out


def _load(out: Path, name: str) -> dict:
    return json.loads((out / f"{name}.json").read_text())


def test_vendored_contract_intact():
    assert sync.check() == []


def test_publish_after_v1_verifies_and_leaves_v1_untouched(data_root, tmp_path):
    out = tmp_path / "app"
    manifest = _v1(data_root, out)
    v1_before = _digests(out, explorer=False)
    index = _explorer(data_root, out)
    assert R.verify_explorer(out) == []
    assert _digests(out, explorer=False) == v1_before            # the v1 payload is byte-for-byte unchanged
    assert index["run_id"] == manifest["run_id"] == index["base_manifest_run_id"]
    assert index["generated_at"] == timeutil.to_iso(NOW)
    assert index["as_of"] and timeutil.parse_ts(index["as_of"]) <= timeutil.parse_ts(NOW)
    sizes = R.tree_bytes(out)
    assert sizes["index.json"] <= 300_000 and sizes["search_index.json"] <= 300_000
    for rel, entry in index["files"].items():
        cap = {"entity_profile": 150_000, "event_research": 150_000, "market_history": 400_000}.get(entry["kind"])
        assert cap is None or entry["bytes"] <= cap, rel


def test_determinism(data_root, tmp_path):
    a, b = tmp_path / "a", tmp_path / "b"
    for out in (a, b):
        _v1(data_root, out)
        _explorer(data_root, out)
    assert R.digest_tree(a) == R.digest_tree(b)
    _explorer(data_root, a)                                      # re-publishing the same inputs is a no-op
    assert R.digest_tree(a) == R.digest_tree(b)


def test_every_event_and_participant_is_published_with_v1_identities(published):
    index, docs = R.load_explorer(published)
    events = _load(published, "events")["items"]
    for ev in events:
        doc = docs[f"events/{ev['event_id']}.json"]
        assert doc["event"] == ev                                   # the v1 event object, same evt_ id
        assert (published / doc["market_history_path"]).exists()
        v1_markets = {m["market_id"] for m in _load(published, "markets")["items"] if m["event_id"] == ev["event_id"]}
        assert {m["market_id"] for m in doc["markets"]} == v1_markets
        for p in ev["participants"]:
            prof = docs[f"players/{p['participant_id']}.json"]
            assert prof["entity"]["participant_id"] == p["participant_id"]
            # the same build.participant(source=kalshi_player_name, source_id=normalised name) the v1 export uses
            assert ax._participant(p["display_name"], None)["participant_id"] == p["participant_id"]
            assert ev["event_id"] in {g["event_id"] for g in prof["games"]}
    profiles = [d for d in docs.values() if d["kind"] == "entity_profile"]
    v1_ids = {p["participant_id"] for ev in events for p in ev["participants"]}
    top = [d for d in profiles if d["entity"]["participant_id"] not in v1_ids]
    assert top and all(d["entity"]["source_ids"].get("tennis_rating_id") for d in top)
    assert all(d["extensions"]["universe_membership"] == ["TOP_ELO_ACTIVE"] for d in top)
    assert len(top) <= 2 * TOP_N


def test_rating_ids_attach_only_on_an_exact_unique_name(published, data_root):
    from tennis_edge.identity import crosswalk                     # the module whose rule this mirrors (needs pandas)
    assert (rx.MAPPED, rx.AMBIGUOUS_NAME, rx.NO_CANONICAL, rx.NO_NAME) == (
        crosswalk.MAPPED, crosswalk.AMBIGUOUS_NAME, crosswalk.NO_CANONICAL, crosswalk.NO_NAME)
    ratings = {t: json.loads((data_root / "processed" / f"ratings_{t}.json").read_text()) for t in ("ATP", "WTA")}
    _, docs = R.load_explorer(published)
    for d in docs.values():
        if d["kind"] != "entity_profile" or "V1_SLATE" not in d["extensions"]["universe_membership"]:
            continue
        ident = d["extensions"]["identity"]
        if ident["status"] == rx.MAPPED:
            tour = d["extensions"]["tour"]
            rec = ratings[tour]["players"][ident["rating_id"]]
            assert rx.normalize_name(rec["name"]) == rx.normalize_name(d["entity"]["display_name"])
            assert d["entity"]["source_ids"]["tennis_rating_id"] == f"{tour}:{ident['rating_id']}"
            assert d["metrics"] and d["extensions"]["rating"]["rating_id"] == ident["rating_id"]
        else:
            assert d["extensions"]["rating"] is None and not d["entity"]["source_ids"].get("tennis_rating_id")
            assert not [o for o in d["metrics"] if o["window"]["label"] == "RATING_STATE"]
    # doubles pairs are never rated; namesakes and a contradiction with the slate's own ids are refused
    idx = rx.rating_name_index({"ATP": {"players": {"1": {"name": "Jo Smith"}, "2": {"name": "Jo Smith"}, "3": {"name": "Al Roe"}}}})
    assert rx.resolve_rating("ATP", "Jo Smith", "singles", set(), idx)["status"] == rx.AMBIGUOUS_NAME
    assert rx.resolve_rating("ATP", "Al Roe", "singles", set(), idx)["rating_id"] == "3"
    assert rx.resolve_rating("ATP", "Al Roe", "singles", {"7", "8"}, idx)["status"] == rx.CONFLICT
    assert rx.resolve_rating("ATP", "A. Roe", "singles", set(), idx)["status"] == rx.NO_CANONICAL
    assert rx.resolve_rating("ATP", "Roe / Smith", "doubles", set(), idx)["status"] == rx.NOT_SINGLES
    caps = {c["capability"]: c for c in _load(published / "explorer", "capabilities")["items"]}
    assert any("v1 slate players carry no rating" in x for x in caps["player_profiles"]["limitations"])


def test_capabilities_match_the_audit(published):
    caps = _load(published / "explorer", "capabilities")
    assert caps["audit_date"] == "2026-10-03" and caps["count"] == len(CAPABILITIES)
    assert {c["capability"]: c["status"] for c in caps["items"]} == EXPECTED_CAPABILITIES
    for c in caps["items"]:
        if c["status"] in ("PARTIAL", "RESEARCH"):
            assert c["limitations"], c["capability"]
        if c["status"] == "UNAVAILABLE":
            assert c["reasons"] and not c["evidence"], c["capability"]
        for path in c["evidence"]:
            assert (published / path).exists(), path
    canon = {c["capability"]: c for c in caps["items"]}["player_game_logs"]
    assert "not on any branch" in canon["reasons"][0]


def test_metrics_rankings_and_series_are_consistent(published):
    _, docs = R.load_explorer(published)
    registry = {m["metric_id"]: m for m in docs["metrics.json"]["items"]}
    rankings = [d for d in docs.values() if d["kind"] == "ranking"]
    series = [d for d in docs.values() if d["kind"] == "time_series"]
    ranked = {r["metric_id"] for r in rankings}
    for mid_, m in registry.items():
        assert m["description"] and m["quality"]["status"] in ("VERIFIED", "PARTIAL", "RESEARCH")
        assert m["supports"]["rank"] == (mid_ in ranked), mid_
        assert m["supports"]["time_series"] == (mid_ in {s["metric_id"] for s in series}), mid_
    for rk in rankings:
        assert rk["universe"]["filter"] and "top" in rk["universe"]["filter"]
        for e in rk["entries"]:
            prof = docs[f"players/{e['entity_id']}.json"]
            obs = [o for o in prof["metrics"] + prof["splits"].get("surface", []) if (o.get("context") or {}).get("ranking_id") == rk["ranking_id"]]
            assert obs and obs[0]["context"] == R.context_from_ranking(rk, e["entity_id"])
    assert series and all(s["x_axis"] == "RUN" and s["entity_type"] == "MARKET" for s in series)
    for s in series:
        for p in s["points"]:
            assert p["path"] == R.event_path(p["event_id"]) and (published / p["path"]).exists()


def test_event_research_carries_ledger_settlement_distributions_and_history(published):
    _, docs = R.load_explorer(published)
    events = [d for d in docs.values() if d["kind"] == "event_research"]
    ledger_rows = [r for d in events for rows in d["extensions"]["ledger"].values() for r in rows]
    assert ledger_rows and all(set(r["models"]) == set(rx.LEDGER_MODELS) for r in ledger_rows)
    assert any(r["settlement"] and r["settlement"]["result"] in ("yes", "no") for r in ledger_rows)
    assert all(r["quality_grade"] for r in ledger_rows)
    m4 = [x for d in events for x in d["distributions"] if x["source"].startswith("model4")]
    env = [x for d in events for x in d["distributions"] if x["label"].startswith("fair_v1 envelope")]
    assert m4 and env and all(x["quality_status"] == "RESEARCH" for x in m4 + env)
    assert any(x["quantiles"] and abs(sum(x["quantiles"].values()) - 1.0) < 1e-6 for x in m4)   # set-score pmf as stored
    assert any(d["extensions"]["external_venues"] for d in events)
    assert any(d["extensions"]["first_ball"]["truth"] for d in events)
    hist = [d for d in docs.values() if d["kind"] == "market_history"]
    pts = [p for d in hist for s in d["series"] for p in s["points"]]
    assert len(hist) == len(events) and len(pts) > 100 and all(p["source"].startswith("kalshi_capture") for p in pts)
    for d in events:
        proj = [p for p in d["projections"] if p["model_price_id"] is None]
        assert all(p["research_only"] and p["authority"] == "RESEARCH_ONLY" for p in d["projections"])
        assert all(p["metric_id"] in {m["metric_id"] for m in docs["metrics.json"]["items"]} for p in proj)
        assert d["context"]["injuries"] == [] and d["context"]["weather"] is None and d["context"]["lineups"] == []


def test_packet_for_a_game(published):
    ev = _load(published, "events")["items"][0]
    pkt = packet.build(app_root=published, scope_kind="GAME", event_id=ev["event_id"])
    assert pkt["quality"]["missing"] == []
    v1_markets = {m["market_id"] for m in _load(published, "markets")["items"] if m["event_id"] == ev["event_id"]}
    assert v1_markets and {m["market_id"] for m in pkt["markets"]} == v1_markets
    assert {e["entity_id"] for e in pkt["evidence"]} == {p["participant_id"] for p in ev["participants"]}
    assert all(e["observations"] for e in pkt["evidence"])
    assert packet.build(app_root=published, scope_kind="GAME", event_id=ev["event_id"]) == pkt


def test_research_status_survives_into_profiles_and_packet(published):
    _, docs = R.load_explorer(published)
    registry = {m["metric_id"]: m for m in docs["metrics.json"]["items"]}
    research_metric = registry["met_tennis.gen2_serve_point_win"]
    assert research_metric["quality"]["status"] == "RESEARCH"
    holders = [d for d in docs.values() if d["kind"] == "entity_profile"
               and any(o["metric_id"] == research_metric["metric_id"] for o in d["metrics"])]
    assert holders
    for prof in holders:
        assert all(o["quality_status"] == "RESEARCH" for o in prof["metrics"] if o["metric_id"] == research_metric["metric_id"])
    eid = holders[0]["games"][0]["event_id"]
    pkt = packet.build(app_root=published, scope_kind="GAME", event_id=eid)
    obs = [o for e in pkt["evidence"] for o in e["observations"] if o["metric_id"] == research_metric["metric_id"]]
    assert obs and all(o["quality_status"] == "RESEARCH" for o in obs)
    assert research_metric["metric_id"] in pkt["quality"]["research_only_items"]


def test_no_secret_shaped_strings(published):
    assert R.no_secret_shaped_strings(published) == []


def test_failed_publish_leaves_previous_tree_intact(data_root, published, monkeypatch):
    before = R.digest_tree(published)
    real_build = rx.build_explorer
    monkeypatch.setattr(rx, "build_explorer", lambda *a, **k: [d for d in real_build(*a, **k) if d["kind"] != "metric_registry"])
    with pytest.raises(R.ExplorerError):
        _explorer(data_root, published)
    assert R.digest_tree(published) == before and R.verify_explorer(published) == []
    monkeypatch.setattr(rx, "build_explorer", real_build)
    # a slate that is not the one the v1 payload was built from: refused, explorer untouched, exit 1
    slate_path = data_root / "research" / "assisted_slates" / "latest.json"
    slate = json.loads(slate_path.read_text())
    slate["slate_id"] = "SL-OTHER"
    slate_path.write_text(json.dumps(slate))
    assert rx.run_cli(["--data-root", str(data_root), "--out", str(published), "--top-n", str(TOP_N)]) == 1
    assert R.digest_tree(published) == before


def test_refuses_after_a_failed_v1_export(data_root, published):
    before = R.digest_tree(published)
    (data_root / "research" / "assisted_slates" / "latest.json").write_text("{corrupt")
    assert ax.run_cli(["--data-root", str(data_root), "--out", str(published), "--now", "2026-10-02T13:50:00Z"]) == 1
    with pytest.raises(rx.ResearchExportError):
        _explorer(data_root, published)
    assert R.digest_tree(published) == before


def test_index_budget_shrinks_only_the_top_n_tail(data_root, tmp_path):
    out = tmp_path / "app"
    manifest = _v1(data_root, out)
    inputs = rx.load_inputs(str(data_root), str(out))
    full, n = rx.fit_index_budget(inputs, now=inputs["now"], run_id=manifest["run_id"], top_n=TOP_N)
    assert n == TOP_N
    size = rx.index_bytes(full, run_id=manifest["run_id"], now=inputs["now"])
    small, n2 = rx.fit_index_budget(inputs, now=inputs["now"], run_id=manifest["run_id"], top_n=TOP_N, budget=size - 1500, margin=0)
    assert n2 < TOP_N
    v1_ids = {p["participant_id"] for ev in _load(out, "events")["items"] for p in ev["participants"]}
    published_ids = {d["entity"]["participant_id"] for d in small if d["kind"] == "entity_profile"}
    assert v1_ids <= published_ids


def test_cli_script_runs(data_root, tmp_path):
    out = tmp_path / "app"
    _v1(data_root, out)
    r = subprocess.run([sys.executable, str(REPO / "scripts" / "research_export.py"), "--data-root", str(data_root), "--out", str(out),
                        "--top-n", str(TOP_N)], capture_output=True, text=True, cwd=str(REPO))
    assert r.returncode == 0, r.stderr
    assert "research export OK" in r.stdout and R.verify_explorer(out) == []
    assert _load(out / "explorer", "index")["generated_at"] == _load(out, "manifest")["generated_at"]


@pytest.mark.parametrize("wf", ["tennis-run.yml", "tennis-assisted-slate.yml"])
def test_workflows_run_the_explorer_after_the_v1_export_and_fail_after_publish(wf):
    import yaml
    steps = yaml.safe_load((REPO / ".github" / "workflows" / wf).read_text())["jobs"]
    steps = next(iter(steps.values()))["steps"]
    i_exp = next(i for i, s in enumerate(steps) if "scripts/app_export.py" in s.get("run", ""))
    run = steps[i_exp]["run"]
    assert run.index("scripts/app_export.py") < run.index("scripts/research_export.py --data-root data --out data/app/latest")
    assert 'echo "RESEARCH_EXPORT_FAILED=1" >> "$GITHUB_ENV"' in run and "GITHUB_STEP_SUMMARY" in run
    i_pub = next(i for i, s in enumerate(steps) if "publish_branch.py" in s.get("run", "") and "data/app" in s.get("run", ""))
    i_fail = next(i for i, s in enumerate(steps) if s.get("if") == "env.RESEARCH_EXPORT_FAILED == '1'")
    assert i_exp < i_pub < i_fail and "exit 1" in steps[i_fail]["run"]
