"""Edge Finder research graph (explorer) for TENNIS: what the repository already stores -> app/latest/explorer.

A PURE ADAPTER beside ``tennis_edge.app_export`` (contract 1.1.0, ``research.publish_explorer``). It runs AFTER the
v1 export, reads the v1 payload it describes (``<app_root>/{manifest,health,events,markets,model_prices,...}.json``)
and the data the repository already commits or captures, and publishes navigable documents:

    players/<prt_>.json        rating-state profile (overall + per-surface Elo with match counts, structural
                               serve/return abilities, serve-point evidence, last match date) for every v1
                               participant and the top-N active players by Elo per tour
    rankings/<rnk_>.json       Elo overall and per surface, per tour, over that universe (arithmetic only)
    events/<evt_>.json         one per v1 event: matchup rows, v1 markets, v1 model prices, the prediction
                               ledger's six model numbers per run, Model 4 distributions and fair_v1 envelopes
                               (RESEARCH), first-ball / start status, external venue comparison
    market_history/<evt_>.json Kalshi quote history per ticker (10-15 min capture) for the current events
    series/<ser_>.json         per-ticker model fair value from the prediction ledger, x = RUN
    metrics.json / capabilities.json / search_index.json

Inputs (data-root relative): ``processed/ratings_{ATP,WTA}.json``, ``research/ledger/*.jsonl``,
``research/settlements/*.jsonl`` (+ ``SCORECARD.md``), ``research/candidate_confirmation/*.json``,
``kalshi/capture/<day>/*.quotes.jsonl.gz``, ``research/external/dislocations/<day>.jsonl``,
``firstball/store/truths/<day>.jsonl``, ``research/frozen_producers/model4/<day>.jsonl``, the assisted slate; and
from the repository itself ``research/market_benchmark/results_ATP.json`` and ``research/elo_study/results_*.json``.

It fits nothing, refits nothing and changes nothing the production pipelines write: every number is a stored
value or simple arithmetic over stored values (rankings). No network. Stdlib + the repository's own stdlib
modules, so the assisted-slate workflow (which installs nothing) can run it. See docs/APP_EXPORT.md "Explorer".
"""
from __future__ import annotations

import glob
import gzip
import json
import os
import re
import sys
from datetime import date, timedelta
from pathlib import Path

from tennis_edge import app_export as ax  # also puts contract/ on sys.path

from edge_finder_contract import build, freshness, research as R, timeutil  # noqa: E402
from edge_finder_contract.publish import dumps  # noqa: E402
from tennis_edge.assisted.slate import load_slate  # noqa: E402
from tennis_edge.identity.names import normalize_name  # noqa: E402

SPORT = ax.SPORT
REPO_ROOT = ax.REPO_ROOT
METHODOLOGY_VERSION = "tennis_explorer_v1"
AUDIT_DATE = "2026-10-03"
TOP_N = 200                      # top players by overall Elo per tour, among the recently active
ACTIVE_DAYS = 365                # "recently active" = last rated match within this many days of ratings as_of_date
CAPTURE_DAYS = 3                 # capture / dislocation / first-ball / Model 4 day files read (now - N .. now)
SURFACES = ("Hard", "Clay", "Grass", "Carpet")
LEDGER_MODELS = ("ELO", "STRUCTURAL", "ENSEMBLE", "ELO_DP_FAIR", "MARKET_MID", "HYBRID_MARKET_MODEL",
                 "INCUMBENT", "V2", "PRODUCTION")   # the last three exist on rows priced since Projection V2 (2026-10-05)
SERIES_MODELS = ("ELO_DP_FAIR",)  # one per-ticker series (the explorer index budget); all six ride in projections
INDEX_BUDGET = 300_000           # bytes of explorer/index.json (one file entry per published document)
AUTHORITY = "RESEARCH_ONLY"

# the identity statuses of tennis_edge/identity/crosswalk.py (that module needs pandas; this one must not)
MAPPED, AMBIGUOUS_NAME, NO_CANONICAL, NO_NAME = "MAPPED", "AMBIGUOUS_NAME", "NO_CANONICAL_MATCH", "NO_USABLE_NAME"
NOT_SINGLES, NO_STATE, CONFLICT = "NOT_APPLICABLE_DOUBLES", "NO_RATING_STATE", "CONFLICTS_WITH_SLATE_PLAYER_ID"

TICKER_RE = re.compile(r'"ticker":\s*"([^"]+)"')
KALSHI_TICKER_RE = re.compile(r'"kalshi_ticker":\s*"([^"]+)"')
MATCH_ID_RE = re.compile(r'"match_id":\s*"([^"]+)"')
PRED_RE = re.compile(r'"prediction_id":\s*"([^"]+)"')

# audit limitations (scratchpad/phase2/audit_tennis.md §4 / §10), verbatim where the audit states them
LIM_RATINGS = "end-state only, overwritten each run; no W-L, no career aggregates"
LIM_OPP_ADJ = ("production formula, tested, end-state only: Elo is opponent-adjusted through its expectation; the "
               "structural serve/return model is a sequential, simple adjustment against the opponent's pre-match estimate")
LIM_MATCHUP = "point-win probabilities per matchup are the model's native matchup object"
LIM_PROJ_DIST = "5 days, listed derivatives only"
LIM_CALIBRATION = "prospective since 2026-09-11; research walk-forwards 1990-2026"
LIM_TRUTH = "sports truth 0% (TENNIS-8): only exchange result is used"
LIM_CLV = "TENNIS-10 FAIL (2,722 of 16,394 closes)"
LIM_FIRST_BALL = "Challenger/ITF/qualifying have no source"
LIM_SURFACE = "no home/away, no handedness split stored (hand column exists)"
LIM_AUTHORITY = "model output: authority RESEARCH_ONLY (real-money authority is OFF everywhere)"


class ResearchExportError(RuntimeError):
    """The explorer cannot be built consistently with the published v1 payload; nothing is written."""


# ---------------------------------------------------------------------------------------------- reading
def _read_json(path) -> object:
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return None


def _rows(path, keep=None, *, gz: bool = False) -> list[dict]:
    """JSONL rows; ``keep(line)`` is a cheap pre-filter on the raw line before parsing."""
    out = []
    try:
        fh = gzip.open(path, "rt", encoding="utf-8") if gz else open(path, encoding="utf-8")
        with fh:
            for line in fh:
                line = line.strip()
                if line and (keep is None or keep(line)):
                    out.append(json.loads(line))
    except (OSError, EOFError):
        return []
    return out


def _match(regex, wanted: set):
    def keep(line: str) -> bool:
        m = regex.search(line)
        return bool(m) and m.group(1) in wanted
    return keep


def _days(now, n: int) -> list[str]:
    d = timeutil.parse_ts(now).date()
    return [(d - timedelta(days=i)).isoformat() for i in range(n, -1, -1)]


def _items(app_root: Path, name: str) -> list[dict]:
    doc = _read_json(app_root / f"{name}.json")
    return list(doc["items"]) if isinstance(doc, dict) and isinstance(doc.get("items"), list) else []


def load_inputs(data_root: str, app_root: str, *, now=None, repo_root: str = REPO_ROOT,
                capture_days: int = CAPTURE_DAYS) -> dict:
    """Everything the explorer reads. The published v1 payload and the slate it was built from are required;
    every research input is optional (absent -> a warning and an UNAVAILABLE capability, never an invention)."""
    app_root = Path(app_root)
    manifest = _read_json(app_root / "manifest.json")
    if not isinstance(manifest, dict) or not manifest.get("run_id"):
        raise ResearchExportError(f"no v1 manifest at {app_root / 'manifest.json'}: run the app export first")
    health = _read_json(app_root / "health.json") or {}
    export_status = ((health.get("components") or {}).get("export") or {}).get("status")
    if export_status not in (None, "OK") or (health.get("payload_run_id") not in (None, manifest["run_id"])):
        raise ResearchExportError("the v1 export of this run failed (health.json export component not OK); "
                                  "the explorer is left as last-known-good")
    now = now if now is not None else manifest["generated_at"]
    runs = _items(app_root, "runs")
    slate = load_slate(os.path.join(data_root, "research", "assisted_slates"))
    native = ((runs[0] if runs else {}).get("source_ids") or {}).get("native_run_id")
    if not isinstance(slate, dict) or slate.get("slate_id") != native:
        raise ResearchExportError(f"the slate on disk ({(slate or {}).get('slate_id')}) is not the slate the published "
                                  f"v1 payload was built from ({native})")
    v1 = {k: _items(app_root, k) for k in ("events", "markets", "model_prices", "recommendations", "wagers")}
    warnings: list[str] = []
    tickers = {m["kalshi_ticker"] for m in v1["markets"]}
    event_tickers = {(e.get("source_ids") or {}).get(ax.EVENT_SOURCE) for e in v1["events"]}
    codes = {(m.get("tour"), m.get("match_code")) for m in slate["matches"]}

    ratings = {}
    for tour in ("ATP", "WTA"):
        st = _read_json(os.path.join(data_root, "processed", f"ratings_{tour}.json"))
        if isinstance(st, dict) and isinstance(st.get("players"), dict):
            ratings[tour] = st
        else:
            warnings.append(f"processed/ratings_{tour}.json not found: {tour} players carry no rating")

    research = os.path.join(data_root, "research")
    ledger_files = sorted(glob.glob(os.path.join(research, "ledger", "*.jsonl")))
    ledger = [r for f in ledger_files for r in _rows(f, _match(TICKER_RE, tickers))]
    if not ledger_files:
        warnings.append("research/ledger not found: no model-price history")
    pids = {r["prediction_id"] for r in ledger if r.get("prediction_id")}
    settle_files = sorted(glob.glob(os.path.join(research, "settlements", "*.jsonl")))
    settlements = {}
    for f in settle_files:
        for r in _rows(f, _match(PRED_RE, pids)):
            settlements[r["prediction_id"]] = r          # later runs supersede earlier ones
    scorecard_path = os.path.join(research, "settlements", "SCORECARD.md")
    scorecard_text = open(scorecard_path, encoding="utf-8").read() if os.path.exists(scorecard_path) else None
    clv_scorecard = _read_json(os.path.join(research, "candidate_confirmation", "CLV_SCORECARD.json"))
    candidates = []
    for f in sorted(glob.glob(os.path.join(research, "candidate_confirmation", "*.json"))):
        d = _read_json(f)
        if isinstance(d, dict) and d.get("candidate_id") and d.get("status"):
            candidates.append({k: d.get(k) for k in ("candidate_id", "kind", "status", "status_reason")})

    days = _days(now, capture_days)
    quotes, dislocations, truths, model4 = [], [], [], []
    for day in days:
        for f in sorted(glob.glob(os.path.join(data_root, "kalshi", "capture", day, "*.quotes.jsonl.gz"))):
            quotes.extend(_rows(f, _match(TICKER_RE, tickers), gz=True))
        dislocations.extend(_rows(os.path.join(research, "external", "dislocations", f"{day}.jsonl"),
                                  _match(KALSHI_TICKER_RE, tickers)))
        truths.extend(_rows(os.path.join(data_root, "firstball", "store", "truths", f"{day}.jsonl"),
                            _match(MATCH_ID_RE, event_tickers)))
        model4.extend(r for r in _rows(os.path.join(research, "frozen_producers", "model4", f"{day}.jsonl"),
                                       lambda line: '"match_code"' in line)
                      if (r.get("tour"), r.get("match_code")) in codes)
    capture_days_present = sorted({d for d in days if glob.glob(os.path.join(data_root, "kalshi", "capture", d, "*.quotes.jsonl.gz"))})
    if not capture_days_present:
        warnings.append(f"no kalshi/capture quote files for {days[0]}..{days[-1]}: market history is empty")
    studies = {
        "pinnacle_ATP": _read_json(os.path.join(repo_root, "research", "market_benchmark", "results_ATP.json")),
        "elo_study_ATP": _read_json(os.path.join(repo_root, "research", "elo_study", "results_ATP.json")),
        "elo_study_WTA": _read_json(os.path.join(repo_root, "research", "elo_study", "results_WTA.json")),
        "projection_v2_validate": _read_json(os.path.join(repo_root, "research", "projection_v2", "results_validate.json")),
        "projection_v2_holdout": _read_json(os.path.join(repo_root, "research", "projection_v2", "results_holdout.json")),
        "projection_v2_decision": _read_json(os.path.join(repo_root, "research", "projection_v2", "PROMOTION_DECISION.json")),
        "projection_v2_derivatives": _read_json(os.path.join(repo_root, "research", "projection_v2", "derivatives_eval.json")),
    }
    return {"manifest": manifest, "slate": slate, "v1": v1, "ratings": ratings, "ledger": ledger,
            "ledger_days": [os.path.basename(f)[:10] for f in ledger_files], "settlements": settlements,
            "settlement_runs": [os.path.basename(f)[:16] for f in settle_files],
            "scorecard_text": scorecard_text, "clv_scorecard": clv_scorecard if isinstance(clv_scorecard, dict) else None,
            "candidates": candidates, "quotes": quotes, "capture_days": capture_days_present, "window_days": days,
            "dislocations": dislocations, "truths": truths, "model4": model4, "studies": studies,
            "warnings": warnings, "now": timeutil.to_iso(now)}


# ---------------------------------------------------------------------------------------------- identity
def rating_name_index(ratings: dict) -> dict:
    """{tour: {normalised full name: [rating ids]}} over the whole rating state of each tour."""
    out = {}
    for tour, st in ratings.items():
        idx: dict[str, list[str]] = {}
        for pid, rec in st["players"].items():
            key = normalize_name(rec.get("name") or "")
            if key:
                idx.setdefault(key, []).append(str(pid))
        out[tour] = idx
    return out


def resolve_rating(tour, display_name, discipline, slate_ids, index: dict) -> dict:
    """The crosswalk rule (identity/crosswalk.py): an exact normalised full name that identifies exactly ONE
    rating id of the tour; nothing on surname, fuzzy distance or row counts. A hit that contradicts the slate's own
    resolved player ids (``physical_match_id``) is refused, not overridden."""
    if discipline and discipline != "singles":
        return {"status": NOT_SINGLES, "rating_id": None, "reason": "doubles pair: no per-player rating applies"}
    if tour not in index:
        return {"status": NO_STATE, "rating_id": None, "reason": f"no rating state for tour {tour!r}"}
    key = normalize_name(display_name or "")
    if not key:
        return {"status": NO_NAME, "rating_id": None, "reason": "no usable name"}
    hits = sorted(set(index[tour].get(key, [])))
    if not hits:
        return {"status": NO_CANONICAL, "rating_id": None, "reason": f"no {tour} rated player uses this name"}
    if len(hits) > 1:
        return {"status": AMBIGUOUS_NAME, "rating_id": None, "reason": f"{len(hits)} {tour} rated players share this name"}
    if slate_ids and hits[0] not in slate_ids:
        return {"status": CONFLICT, "rating_id": None,
                "reason": f"exact-name id {hits[0]} is not one of the slate's resolved ids {sorted(slate_ids)}"}
    return {"status": MAPPED, "rating_id": hits[0], "reason": "exact normalised full name, unique in the tour's rating state"}


def _slate_ids(physical_match_id) -> set[str]:
    parts = str(physical_match_id or "").split(":")
    return set(parts[1:3]) if len(parts) == 4 else set()


# ---------------------------------------------------------------------------------------------- helpers
def _f(v):
    try:
        return None if v is None or v == "" else float(v)
    except (TypeError, ValueError):
        return None


def _prob(v):
    x = _f(v)
    return x if x is not None and 0.0 <= x <= 1.0 else None


def _latest(stamps) -> str | None:
    real = [s for s in stamps if s]
    return timeutil.to_iso(max(real, key=timeutil.parse_ts)) if real else None


def _earliest(stamps) -> str | None:
    real = [s for s in stamps if s]
    return timeutil.to_iso(min(real, key=timeutil.parse_ts)) if real else None


def _run_label(ts) -> str:
    return "run " + timeutil.parse_ts(ts).strftime("%Y-%m-%dT%H:%MZ")


def _parse_scorecard(text: str | None) -> dict | None:
    if not text:
        return None
    out: dict = {"forecasters": {}}
    m = re.search(r"\(([0-9T:\-.+]+)\)", text.splitlines()[0]) if text.splitlines() else None
    out["generated_at"] = m.group(1) if m else None
    m = re.search(r"ledger rows: (\d+); settled rows: (\d+); gradeable with market mid: (\d+)", text)
    if m:
        out.update(ledger_rows=int(m.group(1)), settled_rows=int(m.group(2)), gradeable_with_mid=int(m.group(3)))
    for name, key in (("market mid at decision", "market_mid_at_decision"), ("model fair", "model_fair")):
        m = re.search(r"\| " + re.escape(name) + r" \| (\d+) \| ([0-9.]+) \| ([0-9.]+) \| ([0-9.\-]+) \|", text)
        if m:
            out["forecasters"][key] = {"n": int(m.group(1)), "brier": float(m.group(2)), "log_loss": float(m.group(3)),
                                       "cal_slope": float(m.group(4))}
    m = re.search(r"STRICT executable CLV rows: (\d+); mean ([0-9.\-]+)", text)
    if m:
        out["strict_executable_clv"] = {"n": int(m.group(1)), "mean": float(m.group(2))}
    return out if out["forecasters"] else None


# ---------------------------------------------------------------------------------------------- build
class _Ctx:
    """Shared state for one build (pure: derived from the inputs and ``now`` only)."""

    def __init__(self, inputs: dict, now, run_id: str):
        self.inputs, self.now, self.run_id = inputs, timeutil.to_iso(now), run_id
        self.ratings = inputs["ratings"]
        self.rating_built = {t: timeutil.to_iso(st["built_at"]) for t, st in self.ratings.items() if st.get("built_at")}
        self.ratings_as_of = {t: st.get("as_of_date") for t, st in self.ratings.items()}


def _quality(status, source, ctx, *, as_of=None, production=True, coverage=None, sample_size=None, limitations=None,
             source_version=None) -> dict:
    return R.quality(status=status, source=source, generated_at=ctx.now, production=production, data_as_of=as_of,
                     source_version=source_version, methodology_version=METHODOLOGY_VERSION, coverage=coverage,
                     sample_size=sample_size, limitations=limitations)


def _metrics(ctx: _Ctx, q: dict) -> dict:
    """The registry: one entry per metric actually published (``q`` holds the quality objects by dataset)."""
    fresh_ratings = freshness.status_for(_latest(ctx.rating_built.values()), thresholds=ax.MODEL_THRESHOLDS, now=ctx.now)
    fresh_ledger = freshness.status_for(q["ledger_as_of"], thresholds=ax.MODEL_THRESHOLDS, now=ctx.now) if q["ledger_as_of"] else "UNKNOWN"
    fresh_m4 = freshness.status_for(q["model4_as_of"], thresholds=ax.MODEL_THRESHOLDS, now=ctx.now) if q["model4_as_of"] else "UNKNOWN"
    rating_src = "processed/ratings_{ATP,WTA}.json (tennis_edge.models.state, RUN TENNIS every 6 h)"
    mv = ", ".join(sorted({st.get("model_version") or "?" for st in ctx.ratings.values()})) or None
    common_rating = dict(sport=SPORT, entity_type="PLAYER", source=rating_src, quality=q["ratings"], freshness=fresh_ratings,
                         source_version=mv, methodology_version=METHODOLOGY_VERSION, update_frequency="every 6 h (RUN TENNIS)",
                         known_limitations=[LIM_RATINGS, LIM_AUTHORITY])
    m = {}
    m["elo"] = R.metric(slug="elo_overall", name="Elo rating (overall)", short_name="Elo", category="rating", stat_type="RATING",
                        description=("The production overall Elo of the player's tour rating state: K = 180/(n+5)^0.4, level priors "
                                     "1300 (ITF) .. 1600 (Finals) at first appearance, walkovers skipped, retirements half weight. "
                                     "Opponent strength enters through the Elo expectation. Sample size = rated matches."),
                        higher_is_better=True, unit="Elo points", comparison_universe="rated players of one tour (see ranking filter)",
                        supports=R.supports(rank=True, percentile=True, opponent_adjustment=True), windows=["RATING_STATE"],
                        related_metrics=["met_tennis.elo_surface"], **common_rating)
    m["elo_surface"] = R.metric(slug="elo_surface", name="Elo rating (surface)", short_name="Surface Elo", category="rating",
                                stat_type="RATING", subcategory="surface",
                                description=("The per-surface Elo the rating state stores for Hard / Clay / Grass / Carpet, with the "
                                             "player's match count on that surface (sample size). Pricing blends it with the overall "
                                             "rating, w = 0.5*n_s/(n_s+20); the blend is not stored and not shown."),
                                higher_is_better=True, unit="Elo points", comparison_universe="rated players of one tour with a rating on the surface",
                                supports=R.supports(rank=True, percentile=True, splits=True, opponent_adjustment=True),
                                windows=["RATING_STATE"], splits=["surface"], related_metrics=["met_tennis.elo_overall"], **common_rating)
    m["sr_serve"] = R.metric(slug="sr_serve_ability", name="Structural serve ability", short_name="Serve",
                             category="serve_return", stat_type="INDEX",
                             description=("s_i of the structural serve/return model (tennis_edge/models/serve_return.py): the player's "
                                          "serve-point win ability as a logit deviation from the running tour-by-surface baseline, "
                                          "estimated against each opponent's current return ability (logit p = base + s_A - r_B), "
                                          "365-day decay, shrunk with 600 prior points. 0 = tour baseline."),
                             higher_is_better=True, unit="logit", supports=R.supports(opponent_adjustment=True),
                             windows=["RATING_STATE"], related_metrics=["met_tennis.sr_return_ability", "met_tennis.serve_point_evidence"],
                             **common_rating)
    m["sr_return"] = R.metric(slug="sr_return_ability", name="Structural return ability", short_name="Return",
                              category="serve_return", stat_type="INDEX",
                              description=("r_i of the structural serve/return model: the player's ability to win points on the "
                                           "opponent's serve, as a logit deviation from the tour-by-surface baseline (higher = better "
                                           "returner); same estimation as the serve ability."),
                              higher_is_better=True, unit="logit", supports=R.supports(opponent_adjustment=True),
                              windows=["RATING_STATE"], related_metrics=["met_tennis.sr_serve_ability"], **common_rating)
    m["sr_points"] = R.metric(slug="serve_point_evidence", name="Serve-point evidence", short_name="SR pts",
                              category="serve_return", stat_type="COUNT",
                              description=("sr_points: the decayed number of serve points behind the structural abilities. The ledger "
                                           "uses the structural model only when both players have >= 1,000; the data-quality grade "
                                           "saturates at 1,500."),
                              higher_is_better=None, unit="serve points (decayed)", windows=["RATING_STATE"], **common_rating)
    ledger_src = "research/ledger/<day>.jsonl (scripts/run_tennis.py, append-only, hash-chained)"
    common_match = dict(sport=SPORT, entity_type="PLAYER", category="matchup", stat_type="PROBABILITY", unit="probability",
                        higher_is_better=True, windows=["GAME"], update_frequency="every 6 h (RUN TENNIS)")
    m["ledger_spw"] = R.metric(slug="ledger_serve_point_win", name="P(win a point on serve), ledger ensemble",
                               short_name="SPW (ledger)", source=ledger_src, quality=q["matchup"], freshness=fresh_ledger,
                               description=("inputs.pa / inputs.pb of the newest prediction-ledger row for the match: the probability "
                                            "that the player wins a point on their own serve against THIS opponent, inverted from the "
                                            "ensemble (Elo + structural) match probability on a best-of-3 basis; every derivative of "
                                            "the match is priced from it."),
                               supports=R.supports(opponent_adjustment=True), known_limitations=[LIM_MATCHUP, LIM_AUTHORITY],
                               related_metrics=["met_tennis.ledger_structural_serve_point_win"], **common_match)
    m["ledger_sr_spw"] = R.metric(slug="ledger_structural_serve_point_win", name="P(win a point on serve), structural",
                                  short_name="SPW (structural)", source=ledger_src, quality=q["matchup"], freshness=fresh_ledger,
                                  description=("inputs.sr_pa / inputs.sr_pb of the newest ledger row: base + s_player - r_opponent "
                                               "through the logistic, the structural model's serve-point probability in this matchup."),
                                  supports=R.supports(opponent_adjustment=True), known_limitations=[LIM_MATCHUP, LIM_AUTHORITY],
                                  related_metrics=["met_tennis.ledger_serve_point_win"], **common_match)
    m["gen2_spw"] = R.metric(slug="gen2_serve_point_win", name="P(win a point on serve), Gen-2 (Model 4)",
                             short_name="SPW (Gen-2)", source="research/frozen_producers/model4/<day>.jsonl (model4_board_v1)",
                             quality=q["model4"], freshness=fresh_m4,
                             description=("gen2_pa / gen2_pb of the newest Model 4 row for the match: the Gen-2 dynamic hierarchical "
                                          "serve/return model's serve-point probability for the player against this opponent (adds "
                                          "tour-level offsets and surface deviations). Model 4 is a frozen RESEARCH producer."),
                             supports=R.supports(opponent_adjustment=True), known_limitations=[LIM_PROJ_DIST, LIM_AUTHORITY],
                             **common_match)
    for model in LEDGER_MODELS:
        slug = "ledger_p_" + model.lower()
        desc = {
            "ELO": "the Elo match probability translated to point probabilities and back under the actual format (MATCH_WINNER rows only)",
            "STRUCTURAL": "the structural serve/return match probability under the actual format (MATCH_WINNER rows only)",
            "ENSEMBLE": "the logit average of Elo and structural on a best-of-3 basis, re-derived under the format (MATCH_WINNER rows only)",
            "ELO_DP_FAIR": "the model fair value of the contract: the frozen DP engine's price from the ensemble point probabilities (every family; the scorecard's 'model fair')",
            "MARKET_MID": "the Kalshi YES mid (bid+ask)/2 the run priced against",
            "HYBRID_MARKET_MODEL": "the hybrid market-model column (null on every row so far)",
            "INCUMBENT": "the pre-V2 production model (elo_surface_k_lo + Gen-1 serve/return ensemble), kept on every row since Projection V2 for comparison (MATCH_WINNER rows only)",
            "V2": "Projection V2: the independent walk-forward ensemble (MOV Elo, Gen-2 by evidence, form, context, age); no market input (MATCH_WINNER rows only)",
            "PRODUCTION": "the match probability of the distribution that priced every family on the row (V2 when promoted, else the incumbent)",
        }[model]
        m["ledger_" + model] = R.metric(
            sport=SPORT, slug=slug, name=f"Ledger P(YES): {model}", short_name=model, entity_type="MARKET", category="model_price",
            stat_type="PROBABILITY", unit="probability", higher_is_better=None, source=ledger_src, quality=q["ledger"],
            freshness=fresh_ledger, description=f"models.{model} of a prediction-ledger row: {desc}. P(ticker resolves YES), one value per run.",
            supports=R.supports(time_series=model in SERIES_MODELS), windows=["RUN"], update_frequency="every 6 h (RUN TENNIS)",
            known_limitations=[LIM_AUTHORITY, "rows per ticker median 2, max 8 (a ticker is re-priced only while listed)"],
            methodology_version=METHODOLOGY_VERSION)
    sc = q["scorecard"]
    if sc is not None:
        m["brier"] = R.metric(sport=SPORT, slug="settled_brier_score", name="Brier score on settled contracts", short_name="Brier",
                              entity_type="MARKET", category="calibration", stat_type="SCORE", higher_is_better=False,
                              source="research/settlements/SCORECARD.md (scripts/ops/settle_ledger.py)", quality=q["calibration"],
                              freshness=freshness.status_for(sc.get("generated_at"), thresholds=ax.MODEL_THRESHOLDS, now=ctx.now) if sc.get("generated_at") else "UNKNOWN",
                              description=("Brier score, log loss and calibration slope of the market mid at decision vs the model fair "
                                           "value over every gradeable settled ledger row (prospective, exchange truth). The values "
                                           "are in extensions.scorecard."),
                              update_frequency="every 6 h (RUN TENNIS)", known_limitations=[LIM_CALIBRATION, LIM_TRUTH],
                              extensions={"scorecard": sc, "candidate_confirmation": q["candidates"]})
    if q["clv"] is not None:
        m["clv"] = R.metric(sport=SPORT, slug="strict_executable_clv", name="Strict executable CLV", short_name="CLV",
                            entity_type="MARKET", category="clv", stat_type="PROBABILITY", unit="dollars per contract",
                            higher_is_better=True, source="research/candidate_confirmation/CLV_SCORECARD.json, research/settlements/<run>.jsonl",
                            quality=q["calibration_clv"], freshness="UNKNOWN",
                            description=("close_bid - entry_ask on ledger rows whose close is anchored to an A/B first-ball truth "
                                         "(fees separate). Per-family means with bootstrap CIs are in extensions.clv_scorecard; "
                                         "per-ticker values ride in event research extensions.ledger."),
                            update_frequency="every 6 h (RUN TENNIS)", known_limitations=[LIM_CLV, LIM_TRUTH],
                            extensions={"clv_scorecard": q["clv"]})
    for key, study in q["studies"].items():
        m[key] = R.metric(**study)
    return m


def build_explorer(inputs: dict, *, now, run_id: str, top_n: int = TOP_N, active_days: int = ACTIVE_DAYS) -> list[dict]:
    """Every explorer document from the loaded inputs. Deterministic for the same inputs, ``now`` and ``run_id``."""
    ctx = _Ctx(inputs, now, run_id)
    v1, slate = inputs["v1"], inputs["slate"]
    ratings = inputs["ratings"]
    index = rating_name_index(ratings)
    packets = {m.get("event_id"): m for m in slate["matches"]}
    markets_by_event: dict[str, list[dict]] = {}
    market_by_ticker = {}
    for mk in v1["markets"]:
        market_by_ticker[mk["kalshi_ticker"]] = mk
        if mk.get("event_id"):
            markets_by_event.setdefault(mk["event_id"], []).append(mk)
    prices_by_market: dict[str, list[dict]] = {}
    for mp in v1["model_prices"]:
        prices_by_market.setdefault(mp["market_id"], []).append(mp)
    events = sorted(v1["events"], key=lambda e: (e["start_time_utc"], e["event_id"]))

    # ---- identity: every v1 participant keeps its prt_ id; the rating id attaches only on an exact unique name
    players: dict[str, dict] = {}            # participant_id -> {participant, tour, rating_id, resolution, events}
    for ev in events:
        tour = ev.get("league")
        disc = (ev.get("extensions") or {}).get("discipline")
        sids = _slate_ids((ev.get("source_ids") or {}).get("physical_match_id"))
        for p in ev["participants"]:
            row = players.setdefault(p["participant_id"], {"participant": p, "tour": tour, "events": [], "slate": True,
                                                           "source": ax.PARTICIPANT_SOURCE, "source_id": ax._norm_name(p["display_name"]),
                                                           "resolution": resolve_rating(tour, p["display_name"], disc, sids, index)})
            row["events"].append(ev["event_id"])
    by_rating: dict[tuple[str, str], str] = {}
    for pid in sorted(players):
        res = players[pid]["resolution"]
        if res["rating_id"]:
            by_rating.setdefault((players[pid]["tour"], res["rating_id"]), pid)

    # ---- the universe: v1 players with a rating + the top-N active players by overall Elo per tour
    top_ids: dict[str, list[str]] = {}
    for tour, st in sorted(ratings.items()):
        asof = date.fromisoformat(str(st.get("as_of_date"))[:10]) if st.get("as_of_date") else None
        active = [(pid, rec) for pid, rec in st["players"].items()
                  if asof and rec.get("last_date") and rec["last_date"] != "None"
                  and date.fromisoformat(rec["last_date"][:10]) >= asof - timedelta(days=active_days)]
        active.sort(key=lambda kv: (-float(kv[1]["elo"]), kv[0]))
        top_ids[tour] = [pid for pid, _ in active[:top_n]]
        for rid in top_ids[tour]:
            if (tour, rid) in by_rating:
                continue
            rec = st["players"][rid]
            part = build.participant(sport=SPORT, participant_type="PLAYER", source="tennis_rating_id", source_id=f"{tour}:{rid}",
                                     display_name=rec.get("name") or f"{tour} {rid}")
            players[part["participant_id"]] = {"participant": part, "tour": tour, "events": [], "slate": False,
                                               "source": "tennis_rating_id", "source_id": f"{tour}:{rid}",
                                               "resolution": {"status": MAPPED, "rating_id": rid,
                                                              "reason": "rating-state id (top-N universe member)"}}
            by_rating[(tour, rid)] = part["participant_id"]
    rated = {pid: row for pid, row in players.items() if row["resolution"]["rating_id"] and row["tour"] in ratings}
    unresolved = sorted(pid for pid, row in players.items() if row["slate"] and pid not in rated)
    n_slate = sum(1 for r in players.values() if r["slate"])

    # ---- datasets for quality objects
    ledger = inputs["ledger"]
    ledger_by_ticker: dict[str, list[dict]] = {}
    for r in ledger:
        ledger_by_ticker.setdefault(r["ticker"], []).append(r)
    for rows in ledger_by_ticker.values():
        rows.sort(key=lambda r: (timeutil.parse_ts(r["generated_at_utc"]), r.get("prediction_id") or ""))
    ledger_as_of = _latest(r.get("generated_at_utc") for r in ledger)
    model4_by_code: dict[tuple, list[dict]] = {}
    for r in inputs["model4"]:
        model4_by_code.setdefault((r.get("tour"), r.get("match_code")), []).append(r)
    model4_as_of = _latest(r.get("predicted_at") for r in inputs["model4"])
    quotes_by_ticker: dict[str, list[dict]] = {}
    for qrow in inputs["quotes"]:
        quotes_by_ticker.setdefault(qrow["ticker"], []).append(qrow)
    disl_by_ticker: dict[str, list[dict]] = {}
    for d in inputs["dislocations"]:
        disl_by_ticker.setdefault(d["kalshi_ticker"], []).append(d)
    truths_by_event: dict[str, list[dict]] = {}
    for t in inputs["truths"]:
        truths_by_event.setdefault(t["match_id"], []).append(t)
    scorecard = _parse_scorecard(inputs["scorecard_text"])
    clv_sc = inputs["clv_scorecard"]
    by_status: dict[str, int] = {}
    for pid in unresolved:
        st_ = players[pid]["resolution"]["status"]
        by_status[st_] = by_status.get(st_, 0) + 1
    unres_note = (f"{len(unresolved)} of {n_slate} v1 slate players carry no rating ("
                  + ", ".join(f"{k} {v}" for k, v in sorted(by_status.items()))
                  + "): they keep their v1 identity and carry no rating observation")
    universe_filter = {t: (f"{t} players on the current v1 slate whose Kalshi name resolves exactly and uniquely to a {t} rating id, "
                           f"plus the top {top_n} by overall Elo among {t} players whose last rated match is within {active_days} days "
                           f"of ratings as_of_date {ctx.ratings_as_of.get(t)}") for t in ratings}
    n_rated = {t: sum(1 for r in rated.values() if r["tour"] == t) for t in ratings}
    q = {
        "ratings": _quality("PARTIAL", "processed/ratings_{ATP,WTA}.json (tennis_edge.models.state)", ctx,
                            as_of=_latest(ctx.rating_built.values()), sample_size=sum(n_rated.values()),
                            source_version=", ".join(sorted({st.get("model_version") or "?" for st in ratings.values()})) or None,
                            coverage="; ".join(f"{t}: {len(st['players'])} rated ids, {n_rated[t]} published (as_of_date "
                                               f"{st.get('as_of_date')})" for t, st in sorted(ratings.items())) or None,
                            limitations=[LIM_RATINGS, LIM_AUTHORITY, unres_note]),
        "matchup": _quality("PARTIAL", "research/ledger inputs (pa/pb, sr_pa/sr_pb)", ctx, as_of=ledger_as_of,
                            limitations=[LIM_MATCHUP, LIM_AUTHORITY]),
        "model4": _quality("RESEARCH", "research/frozen_producers/model4 (model4_board_v1, frozen)", ctx, as_of=model4_as_of,
                           production=True, limitations=[LIM_PROJ_DIST, "Model 4 is a frozen RESEARCH producer", LIM_AUTHORITY]),
        "ledger": _quality("VERIFIED", "research/ledger/<day>.jsonl (scripts/run_tennis.py)", ctx, as_of=ledger_as_of,
                           sample_size=len(ledger), coverage=(f"{len(ledger_by_ticker)} current tickers with ledger rows; ledger days "
                                                              f"{inputs['ledger_days'][0]}..{inputs['ledger_days'][-1]}") if inputs["ledger_days"] else None,
                           limitations=[LIM_AUTHORITY, "doubles rows (doubles_baseline_prior_v0) failed the no-skill test and are RESEARCH"]),
        "ledger_as_of": ledger_as_of, "model4_as_of": model4_as_of, "scorecard": scorecard,
        "candidates": inputs["candidates"],
        "clv": ({k: clv_sc.get(k) for k in ("ledger_rows", "strict_rows", "timing_classes", "close_basis", "views",
                                             "published_clv_run", "published_strict_rows")} if clv_sc else None),
        "calibration": _quality("PARTIAL", "research/settlements/SCORECARD.md", ctx,
                                as_of=(scorecard or {}).get("generated_at"), sample_size=(scorecard or {}).get("gradeable_with_mid"),
                                limitations=[LIM_CALIBRATION, LIM_TRUTH]),
        "calibration_clv": _quality("PARTIAL", "research/candidate_confirmation/CLV_SCORECARD.json", ctx,
                                    sample_size=(clv_sc or {}).get("strict_rows"), limitations=[LIM_CLV, LIM_TRUTH]),
        "studies": _studies(inputs["studies"], ctx),
    }
    metrics = _metrics(ctx, q)
    mid = {k: v["metric_id"] for k, v in metrics.items()}
    registry = R.metric_registry(sport=SPORT, run_id=run_id, generated_at=ctx.now, metrics=list(metrics.values()))
    w_state = R.window("CUSTOM", label="RATING_STATE")

    # ---- rankings: Elo overall and per surface, per tour, over the published universe
    rankings: dict[tuple, dict] = {}
    for tour in sorted(ratings):
        members = sorted(pid for pid, r in rated.items() if r["tour"] == tour)
        st = ratings[tour]
        recs = {pid: st["players"][rated[pid]["resolution"]["rating_id"]] for pid in members}
        label = f"{tour} rated players: current slate + top {top_n} active by Elo"
        rq = q["ratings"]
        vals = [{"entity_id": pid, "display_name": players[pid]["participant"]["display_name"], "value": recs[pid].get("elo"),
                 "sample_size": recs[pid].get("n")} for pid in members]
        if sum(1 for v in vals if v["value"] is not None) >= 2:
            rankings[(tour, None)] = R.ranking(
                sport=SPORT, metric_id=mid["elo"], universe_label=label, entity_type="PLAYER", window=w_state,
                as_of=ctx.rating_built.get(tour) or ctx.now, higher_is_better=True, values=vals, run_id=run_id, generated_at=ctx.now,
                quality=rq, season=None, universe_filter=universe_filter[tour], path_for=R.player_path,
                links=[R.link(rel="METRIC", target_kind="metric_registry", label="metric registry", path=R.app_path(R.METRICS_NAME))])
        for surf in SURFACES:
            vals = []
            for pid in members:
                s = (recs[pid].get("surfaces") or {}).get(surf)
                if s and s[0] is not None and (s[1] or 0) > 0:
                    vals.append({"entity_id": pid, "display_name": players[pid]["participant"]["display_name"],
                                 "value": s[0], "sample_size": s[1]})
            if len(vals) >= 2:
                rankings[(tour, surf)] = R.ranking(
                    sport=SPORT, metric_id=mid["elo_surface"], universe_label=label, entity_type="PLAYER", window=w_state,
                    as_of=ctx.rating_built.get(tour) or ctx.now, higher_is_better=True, values=vals, run_id=run_id,
                    generated_at=ctx.now, quality=rq, universe_filter=universe_filter[tour] + f"; with >= 1 rated {surf} match",
                    split=R.split("surface", surf), path_for=R.player_path,
                    links=[R.link(rel="METRIC", target_kind="metric_registry", label="metric registry", path=R.app_path(R.METRICS_NAME))])

    # ---- per-player rating observations
    obs_by_player: dict[str, dict] = {}
    for pid, row in sorted(rated.items()):
        tour, rid = row["tour"], row["resolution"]["rating_id"]
        rec = ratings[tour]["players"][rid]
        as_of = ctx.rating_built.get(tour) or ctx.now
        ext = {"rating_id": rid, "tour": tour, "ratings_as_of": ctx.ratings_as_of.get(tour)}

        def ob(key, value, *, sample=None, split=None, context=None, display=None, unit=None):
            return R.observation(sport=SPORT, metric_id=mid[key], entity_id=pid, entity_type="PLAYER", value=value, window=w_state,
                                 as_of=as_of, source=f"processed/ratings_{tour}.json", quality_status="PARTIAL", sample_size=sample,
                                 split=split, context=context, display_value=display, unit=unit, extensions=ext)
        rk = rankings.get((tour, None))
        main = [ob("elo", rec.get("elo"), sample=rec.get("n"), context=R.context_from_ranking(rk, pid) if rk else None,
                   display=f"{rec['elo']:.0f}" if rec.get("elo") is not None else None, unit="Elo points"),
                ob("sr_serve", rec.get("sr_s"), display=f"{rec['sr_s']:+.3f}" if rec.get("sr_s") is not None else None, unit="logit"),
                ob("sr_return", rec.get("sr_r"), display=f"{rec['sr_r']:+.3f}" if rec.get("sr_r") is not None else None, unit="logit"),
                ob("sr_points", rec.get("sr_points"), display=f"{rec['sr_points']:.0f}" if rec.get("sr_points") is not None else None)]
        surf_obs = []
        for surf in SURFACES:
            s = (rec.get("surfaces") or {}).get(surf)
            if s and s[0] is not None and (s[1] or 0) > 0:
                rks = rankings.get((tour, surf))
                surf_obs.append(ob("elo_surface", s[0], sample=s[1], split=R.split("surface", surf),
                                   context=R.context_from_ranking(rks, pid) if rks else None, display=f"{s[0]:.0f}", unit="Elo points"))
        obs_by_player[pid] = {"main": main, "surface": surf_obs, "rec": rec}

    # ---- per-event matchup observations (GAME window): ledger pa/pb, sr_pa/sr_pb; Model 4 gen2_pa/pb
    game_obs: dict[str, list[dict]] = {}          # participant_id -> GAME observations
    event_docs, mh_docs, series_docs = [], [], []
    series_refs_by_player: dict[str, list[dict]] = {}
    series_by_ticker: dict[str, list[dict]] = {}
    w_game = R.window("GAME")
    for ev in events:
        eid = ev["event_id"]
        ek = (ev.get("source_ids") or {}).get(ax.EVENT_SOURCE)
        pk = packets.get(ek) or {}
        side_pid = {}
        for side, p in zip(("a", "b"), ev["participants"]):
            side_pid[side] = p["participant_id"]
        rid_side = {players[p]["resolution"]["rating_id"]: s for s, p in side_pid.items() if players[p]["resolution"]["rating_id"]}
        name_side = {normalize_name(players[p]["participant"]["display_name"]): s for s, p in side_pid.items()}

        def side_of(rating_id, name):
            return rid_side.get(str(rating_id)) if rating_id is not None and str(rating_id) in rid_side else name_side.get(normalize_name(name or ""))
        ev_tickers = sorted(mk["kalshi_ticker"] for mk in markets_by_event.get(eid, []))
        ev_ledger = sorted((r for t in ev_tickers for r in ledger_by_ticker.get(t, [])),
                           key=lambda r: (timeutil.parse_ts(r["generated_at_utc"]), r["ticker"]))
        newest = ev_ledger[-1] if ev_ledger else None
        if newest and len(side_pid) == 2:
            inp = newest.get("inputs") or {}
            sa, sb = side_of(newest.get("player_a_id"), newest.get("player_a")), side_of(newest.get("player_b_id"), newest.get("player_b"))
            if sa and sb and sa != sb:
                for key, va, vb in (("ledger_spw", inp.get("pa"), inp.get("pb")), ("ledger_sr_spw", inp.get("sr_pa"), inp.get("sr_pb"))):
                    for s, val, other in ((sa, va, sb), (sb, vb, sa)):
                        if _prob(val) is not None:
                            game_obs.setdefault(side_pid[s], []).append(R.observation(
                                sport=SPORT, metric_id=mid[key], entity_id=side_pid[s], entity_type="PLAYER", value=val, window=w_game,
                                as_of=newest["generated_at_utc"], source="research/ledger (newest row for the match)",
                                quality_status="RESEARCH" if "DOUBLES" in str(newest.get("series_ticker")) else "PARTIAL",
                                event_id=eid, opponent_id=side_pid[other], display_value=f"{float(val):.3f}", unit="probability",
                                extensions={"prediction_id": newest.get("prediction_id"), "ticker": newest["ticker"],
                                            "ratings_as_of": newest.get("ratings_as_of"), "model_version": newest.get("model_version")}))
        m4rows = sorted(model4_by_code.get((pk.get("tour"), pk.get("match_code")), []),
                        key=lambda r: (timeutil.parse_ts(r["predicted_at"]), r.get("ticker") or ""))
        m4 = m4rows[-1] if m4rows else None
        if m4 and len(side_pid) == 2:
            sa, sb = side_of(m4.get("player_a_id"), None), side_of(m4.get("player_b_id"), None)
            if sa and sb and sa != sb:
                for s, val, other in ((sa, m4.get("gen2_pa"), sb), (sb, m4.get("gen2_pb"), sa)):
                    if _prob(val) is not None:
                        game_obs.setdefault(side_pid[s], []).append(R.observation(
                            sport=SPORT, metric_id=mid["gen2_spw"], entity_id=side_pid[s], entity_type="PLAYER", value=val, window=w_game,
                            as_of=m4["predicted_at"], source="research/frozen_producers/model4 (newest row for the match)",
                            quality_status="RESEARCH", event_id=eid, opponent_id=side_pid[other], display_value=f"{float(val):.3f}",
                            unit="probability", extensions={"producer": m4.get("producer"), "fundamental_version": m4.get("fundamental_version"),
                                                            "evidence_points": m4.get("gen2_evidence_a" if s == sa else "gen2_evidence_b")}))

        # ---- ledger series (x = RUN) and the six model numbers as projections
        projections = []
        ledger_ext: dict[str, list[dict]] = {}
        settlements = inputs["settlements"]
        for t in ev_tickers:
            mk = market_by_ticker[t]
            rows = ledger_by_ticker.get(t, [])
            for r in rows:
                doubles = "DOUBLES" in str(r.get("series_ticker"))
                st = settlements.get(r.get("prediction_id")) or {}
                clv = st.get("clv") or {}
                exch = st.get("exchange") or {}
                ledger_ext.setdefault(t, []).append({
                    "run": _run_label(r["generated_at_utc"]), "generated_at": timeutil.to_iso(r["generated_at_utc"]),
                    "prediction_id": r.get("prediction_id"), "models": {k: (r.get("models") or {}).get(k) for k in LEDGER_MODELS},
                    "market_quote": {k: (r.get("market_quote") or {}).get(k) for k in ("yes_bid", "yes_ask", "quote_ts", "source")},
                    "quality_grade": (r.get("quality") or {}).get("grade"), "data_quality_score": (r.get("quality") or {}).get("data_quality_score"),
                    "start_basis": r.get("start_basis"), "ratings_as_of": r.get("ratings_as_of"), "model_version": r.get("model_version"),
                    "authority": r.get("authority"), "doubles": doubles,
                    "settlement": ({"status": exch.get("status"), "result": exch.get("result"), "settlement_ts": exch.get("settlement_ts"),
                                    "y_yes": st.get("y_yes"), "gradeable": st.get("gradeable"), "settled_run": st.get("settled_run")} if st else None),
                    "clv": ({"strict": clv.get("strict"), "clv_executable": clv.get("clv_executable"), "clv_ask_to_ask": clv.get("clv_ask_to_ask"),
                             "clv_midpoint": clv.get("clv_midpoint"), "timing_class": clv.get("timing_class"),
                             "truth_confidence": clv.get("truth_confidence"), "exclusion_reason": clv.get("exclusion_reason")} if clv else None)})
                for model in LEDGER_MODELS:
                    val = _prob((r.get("models") or {}).get(model))
                    if val is None or model == "MARKET_MID":
                        continue
                    projections.append({
                        "model_price_id": None, "market_id": mk["market_id"], "event_id": eid, "metric_id": mid["ledger_" + model],
                        "fair_probability": round(val, 6), "market_probability": _prob((r.get("models") or {}).get("MARKET_MID")),
                        "edge": None, "projection_value": None, "projection_unit": None, "lower_bound": None, "upper_bound": None,
                        "generated_at": timeutil.to_iso(r["generated_at_utc"]), "run_id": None,
                        "model_version": f"ledger {model} ({r.get('model_version')})", "research_only": True, "authority": AUTHORITY,
                        "quality_status": "RESEARCH" if doubles else "VERIFIED"})
            # one MATCH_WINNER series per match: the side-B contract is the ledger's exact complement of side A
            if (str(mk.get("market_family")).upper() == "MATCH_WINNER" and mk.get("participant_id") == side_pid.get("b")
                    and any(str(o.get("market_family")).upper() == "MATCH_WINNER" and o.get("participant_id") == side_pid.get("a")
                            and ledger_by_ticker.get(o["kalshi_ticker"]) for o in markets_by_event.get(eid, []))):
                continue
            for model in SERIES_MODELS:
                pts = []
                for r in rows:
                    val = _prob((r.get("models") or {}).get(model))
                    if val is None:
                        continue
                    pts.append(R.point(x=_run_label(r["generated_at_utc"]), t=r["generated_at_utc"], value=round(val, 6),
                                       quality_status="RESEARCH" if "DOUBLES" in str(r.get("series_ticker")) else "VERIFIED",
                                       event_id=eid, source="research/ledger", path=R.event_path(eid)))
                if not pts:
                    continue
                ser = R.time_series(sport=SPORT, metric_id=mid["ledger_" + model], entity_id=mk["market_id"], entity_type="MARKET",
                                    x_axis="RUN", points=pts, as_of=_latest(p["t"] for p in pts), run_id=run_id, generated_at=ctx.now,
                                    quality=q["ledger"], unit="probability",
                                    links=[R.link(rel="EVENT_RESEARCH", target_kind="event_research", label="event research", target_id=eid, path=R.event_path(eid)),
                                           R.link(rel="MARKET_HISTORY", target_kind="market_history", label="Kalshi quote history", target_id=eid, path=R.market_history_path(eid))])
                series_docs.append(ser)
                ref = {"series_id": ser["series_id"], "metric_id": ser["metric_id"], "x_axis": "RUN", "split": None, "path": R.series_path(ser["series_id"])}
                series_by_ticker.setdefault(t, []).append(ref)
                if mk.get("participant_id") and str(mk.get("market_family")).upper() == "MATCH_WINNER":
                    series_refs_by_player.setdefault(mk["participant_id"], []).append(ref)

        # ---- distributions (RESEARCH): Model 4 set-score / games, fair_v1 envelopes
        distributions = []
        if m4:
            a_pid = side_pid.get(side_of(m4.get("player_a_id"), None) or "")
            a_name = players[a_pid]["participant"]["display_name"] if a_pid else m4.get("player_a_id")
            for kind in ("fundamental", "conditioned"):
                d = m4.get(f"{kind}_distribution") or {}
                if not d:
                    continue
                base = {"market_id": None, "metric_id": None, "entity_id": a_pid, "samples": None, "run_id": None, "stdev": None,
                        "generated_at": timeutil.to_iso(m4["predicted_at"]), "quality_status": "RESEARCH",
                        "source": f"model4_board_v1 {kind}_distribution ({m4.get('fundamental_version') if kind == 'fundamental' else m4.get('model_version')})"}
                if d.get("set_score"):
                    distributions.append(dict(base, label=f"Model 4 {kind}: P(set score), player A = {a_name} (exact DP, not quantiles)",
                                              quantiles={k: round(float(v), 6) for k, v in sorted(d["set_score"].items())},
                                              mean=None))
                if d.get("e_total_games") is not None:
                    distributions.append(dict(base, label=f"Model 4 {kind}: expected total games", quantiles={}, mean=round(float(d["e_total_games"]), 6)))
                if d.get("e_game_diff_a") is not None:
                    distributions.append(dict(base, label=f"Model 4 {kind}: expected game difference, player A = {a_name}",
                                              quantiles={}, mean=round(float(d["e_game_diff_a"]), 6)))
                if d.get("p_match_a") is not None:
                    distributions.append(dict(base, label=f"Model 4 {kind}: P(player A = {a_name} wins the match)",
                                              quantiles={}, mean=round(float(d["p_match_a"]), 6)))
        for mk in sorted(markets_by_event.get(eid, []), key=lambda m: m["kalshi_ticker"]):
            for mp in prices_by_market.get(mk["market_id"], []):
                if mp.get("lower_bound") is not None and mp.get("upper_bound") is not None:
                    distributions.append({"market_id": mk["market_id"], "metric_id": None, "entity_id": mk.get("participant_id"),
                                          "label": "fair_v1 envelope: P(YES) under the 13 frozen perturbations (min / max)",
                                          "quantiles": {"envelope_low": mp["lower_bound"], "envelope_high": mp["upper_bound"]},
                                          "mean": None, "stdev": None, "samples": None, "run_id": mp.get("run_id"),
                                          "generated_at": mp["generated_at"], "source": f"{mp.get('model_version')} via the assisted slate",
                                          "quality_status": "RESEARCH"})

        # ---- market history (Kalshi capture quotes)
        series = []
        for mk in sorted(markets_by_event.get(eid, []), key=lambda m: m["market_id"]):
            pts = [R.price_point(captured_at=qr["captured_at"], yes_bid=_prob(qr.get("yes_bid_dollars")), yes_ask=_prob(qr.get("yes_ask_dollars")),
                                 last_price=_prob(qr.get("last_price_dollars")), volume=_f(qr.get("volume_fp")),
                                 open_interest=_f(qr.get("open_interest_fp")),
                                 source=f"kalshi_capture {qr.get('run_id')} {qr.get('snapshot_kind') or ''}".strip())
                   for qr in quotes_by_ticker.get(mk["kalshi_ticker"], []) if qr.get("captured_at")]
            dedup = {p["captured_at"]: p for p in sorted(pts, key=lambda p: (p["captured_at"], p["source"] or ""))}
            series.append({"market_id": mk["market_id"], "kalshi_ticker": mk["kalshi_ticker"], "points": list(dedup.values())})
        n_pts = sum(len(s["points"]) for s in series)
        days = inputs["capture_days"]
        mh_q = _quality("VERIFIED", "kalshi/capture/<day>/<run>.quotes.jsonl.gz (scripts/kalshi/capture_tennis.py)", ctx,
                        as_of=_latest(p["captured_at"] for s in series for p in s["points"]), sample_size=n_pts,
                        coverage=(f"capture days {days[0]}..{days[-1]}" if days else "no capture day in the window"),
                        limitations=[f"only the {CAPTURE_DAYS + 1} most recent capture days are read "
                                     f"({inputs['window_days'][0]}..{inputs['window_days'][-1]}); the branch keeps every day since 2026-09-11",
                                     "quote rows are written when the quote changes plus an hourly full snapshot"])
        mh_docs.append(R.market_history(sport=SPORT, run_id=run_id, generated_at=ctx.now, event_id=eid,
                                        as_of=mh_q["data_as_of"] or ctx.now, series=series, quality=mh_q,
                                        links=[R.link(rel="EVENT_RESEARCH", target_kind="event_research", label="event research",
                                                      target_id=eid, path=R.event_path(eid))]))

        # ---- first ball / start status, external venues, notes
        evx = ev.get("extensions") or {}
        truth_rows = sorted(truths_by_event.get(ek, []), key=lambda t: (timeutil.parse_ts(t["observed_at_utc"]), t.get("row_hash") or ""))
        truth = truth_rows[-1] if truth_rows else None
        start_block = {k: (pk.get("start") or {}).get(k) for k in ("start_status", "first_ball_status", "first_ball_at", "current_expected_start",
                                                                   "start_time_source", "start_time_confidence", "nominal_scheduled_start",
                                                                   "nominal_is_placeholder", "live_source_covered", "court", "bet_allowed",
                                                                   "status_reasons", "evaluated_at")}
        first_ball = {"slate_start": start_block, "first_ball": pk.get("first_ball"),
                      "truth": ({k: truth.get(k) for k in ("actual_first_ball_at_utc", "lower_bound_utc", "upper_bound_utc", "confidence",
                                                           "derivation_method", "no_play", "source", "source_status", "observed_at_utc",
                                                           "contradiction_status")} if truth else None),
                      "truth_rows": len(truth_rows),
                      "coverage_note": None if truth else f"no first-ball truth row for this match ({LIM_FIRST_BALL})"}
        externals = {}
        for t in ev_tickers:
            rows = sorted(disl_by_ticker.get(t, []), key=lambda d: (timeutil.parse_ts(d["generated_at"]), d.get("row_hash") or ""))
            if rows:
                d = rows[-1]
                externals[t] = {k: d.get(k) for k in ("generated_at", "side", "kalshi_bid", "kalshi_ask", "kalshi_mid", "external_sources",
                                                      "external_prices", "external_raw", "external_fair", "reference_kind", "n_independent_groups",
                                                      "model_fair", "external_vs_kalshi", "model_vs_kalshi", "model_vs_external", "triangulation",
                                                      "external_quote_age_s", "decision", "authority")}
                externals[t]["passes_in_window"] = len(rows)
                externals[t]["source"] = "research/external/dislocations (external_v1 scan; prices de-vigged)"
            else:
                ec = (pk.get("external_context") or {}).get(t) or {}
                if ec.get("consensus") is not None or ec.get("bovada") is not None or ec.get("smarkets") is not None:
                    externals[t] = dict(ec, source="assisted slate external_context (no dislocation row in the window)")
        notes = [f"start: {start_block.get('start_status')} ({start_block.get('start_time_source') or 'no live source'}, "
                 f"confidence {start_block.get('start_time_confidence')}); first ball: {(pk.get('first_ball') or {}).get('status')}"]
        if truth:
            notes.append(f"first-ball truth ({truth.get('source')}, confidence {truth.get('confidence')}): "
                         f"{truth.get('actual_first_ball_at_utc') or 'bracket ' + str(truth.get('lower_bound_utc')) + '..' + str(truth.get('upper_bound_utc'))}")
        for t, x in sorted(externals.items()):
            if x.get("external_fair") is not None:
                notes.append(f"external {t}: de-vigged {', '.join(x.get('external_sources') or [])} {x['external_fair']:.3f} vs Kalshi mid "
                             f"{x.get('kalshi_mid')} vs model {x.get('model_fair') if x.get('model_fair') is None else round(x['model_fair'], 3)}"
                             f" ({x.get('triangulation')}, {x.get('generated_at')})")
        dq = pk.get("data_quality_check") or {}
        if dq.get("data_quality_status"):
            notes.append(f"slate data quality {dq.get('data_quality_status')}: {', '.join(dq.get('tags') or [])}")
        for t, rows in sorted(ledger_ext.items()):
            last = rows[-1]
            if last.get("settlement"):
                c = last.get("clv") or {}
                notes.append(f"settled {t}: result {last['settlement'].get('result')}; strict CLV "
                             f"{c.get('clv_executable') if c.get('strict') else 'n/a (' + str(c.get('timing_class')) + ')'}")
        surface = evx.get("surface")
        venue = ({"surface": surface, "surface_bucket": evx.get("surface_bucket"), "competition": ev.get("competition"),
                  "level": evx.get("level"), "indoor": None,
                  "note": "surface only (pricing/competition.py lookup as the slate states it); no court speed, altitude or indoor flag"}
                 if surface else None)

        # ---- matchup rows (tennis has no home/away: 'home' slot = player A, 'away' slot = player B)
        a_pid, b_pid = side_pid.get("a"), side_pid.get("b")
        matchup = []

        def pick(pid, key, split_value=None):
            if pid is None:
                return None
            if key in ("elo", "sr_serve", "sr_return", "sr_points") and pid in obs_by_player:
                return next((o for o in obs_by_player[pid]["main"] if o["metric_id"] == mid[key]), None)
            if key == "elo_surface" and pid in obs_by_player:
                return next((o for o in obs_by_player[pid]["surface"] if o["split"]["value"] == split_value), None)
            return next((o for o in game_obs.get(pid, []) if o["metric_id"] == mid[key] and o["event_id"] == eid), None)
        note = "tennis has no home/away: 'home' = player A, 'away' = player B in the slate's order"
        for key in ("elo", "elo_surface", "sr_serve", "sr_return", "sr_points", "ledger_spw", "ledger_sr_spw", "gen2_spw"):
            sv = surface if key == "elo_surface" else None
            if key == "elo_surface" and not surface:
                continue
            ha, hb = pick(a_pid, key, sv), pick(b_pid, key, sv)
            if ha or hb:
                matchup.append({"metric_id": mid[key], "name": metrics[key]["name"] + (f" ({surface})" if sv else ""),
                                "home": ha, "away": hb, "note": note})

        prices = [mp for mk in markets_by_event.get(eid, []) for mp in prices_by_market.get(mk["market_id"], [])]
        v1_proj = []
        for mp in sorted(prices, key=lambda r: (r["market_id"], r["generated_at"])):
            src = (mp.get("model_version") or "").lower()
            v1_proj.append(R.projection_ref(mp, research_only=True, authority=AUTHORITY,
                                            quality_status="VERIFIED" if src.startswith("gen1") else "RESEARCH"))
        parts = [{"participant_id": p["participant_id"], "display_name": p["display_name"], "home_away": None,
                  "path": R.player_path(p["participant_id"])} for p in ev["participants"]]
        links = [R.link(rel="MARKET_HISTORY", target_kind="market_history", label="Kalshi quote history", target_id=eid,
                        path=R.market_history_path(eid))]
        links += [R.link(rel="PLAYER", target_kind="entity_profile", label=p["display_name"], target_id=p["participant_id"],
                         path=R.player_path(p["participant_id"])) for p in ev["participants"]]
        for t in ev_tickers:
            links += [R.link(rel="SERIES", target_kind="time_series", label=f"{t} ledger {ref['metric_id'].split('.')[-1]}",
                             target_id=ref["series_id"], path=ref["path"]) for ref in series_by_ticker.get(t, [])]
        er_q = _quality("PARTIAL", "v1 payload + rating state + prediction ledger + capture + first-ball store + external scan", ctx,
                        as_of=_latest([ev.get("last_updated_at"), newest.get("generated_at_utc") if newest else None,
                                       mh_q["data_as_of"]]),
                        limitations=["no injuries, no draws, no weather/venue beyond surface, no rankings consumed, no form model",
                                     f"first-ball truth exists only for ATP/WTA main tour + Slams ({LIM_FIRST_BALL})", LIM_AUTHORITY])
        wagers = sorted(w["wager_id"] for w in v1["wagers"] if w.get("event_id") == eid)
        event_docs.append(R.event_research(
            sport=SPORT, run_id=run_id, generated_at=ctx.now, event=ev, quality=er_q, participants=parts, matchup=matchup,
            projections=v1_proj + projections, distributions=distributions,
            markets=[R.market_ref(mk) for mk in sorted(markets_by_event.get(eid, []), key=lambda m: m["kalshi_ticker"])],
            market_history_path=R.market_history_path(eid),
            context={"venue": venue, "notes": notes}, wagers=wagers, links=links,
            extensions={"first_ball": first_ball, "external_venues": externals, "ledger": ledger_ext,
                        "identity": {p["participant_id"]: players[p["participant_id"]]["resolution"] for p in ev["participants"]},
                        "slate_model_context": {k: (pk.get("model_context") or {}).get(k) for k in
                                                ("player_a_win", "model_uncertainty", "serve_evidence", "data_quality", "selector_v1",
                                                 "surface_adjustment", "recent_form_inputs", "model_rows_predicted_at")},
                        "frozen_rule_context": pk.get("frozen_rule_context"), "authority": AUTHORITY}))

    # ---- profiles
    profiles = []
    events_by_id = {ev["event_id"]: ev for ev in events}
    for pid in sorted(players):
        row = players[pid]
        part = dict(row["participant"])
        res = row["resolution"]
        rid = res["rating_id"] if pid in rated else None
        rec = obs_by_player.get(pid, {}).get("rec")
        tour = row["tour"]
        sids = dict(part.get("source_ids") or {})
        meta = dict(part.get("metadata") or {})
        if rid:
            sids["tennis_rating_id"] = f"{tour}:{rid}"
            meta.update({"tour": tour, "rating_name": rec.get("name"), "last_match_date": rec.get("last_date")})
        part = build.participant(sport=SPORT, participant_type=part["participant_type"], source=row["source"],
                                 source_id=row["source_id"], display_name=part["display_name"], short_name=part.get("short_name"),
                                 source_ids=sids, metadata=meta)
        if part["participant_id"] != pid:
            raise ResearchExportError(f"participant id drift for {row['participant']['display_name']}: {part['participant_id']} != {pid}")
        metrics_obs = list(obs_by_player.get(pid, {}).get("main", [])) + list(game_obs.get(pid, []))
        splits = {"surface": obs_by_player[pid]["surface"]} if obs_by_player.get(pid, {}).get("surface") else {}
        games, opponents, mrefs, projs, links = [], [], [], [], []
        for eid in row["events"]:
            ev = events_by_id[eid]
            opp = next((p for p in ev["participants"] if p["participant_id"] != pid), None)
            games.append(R.game_ref(event_id=eid, start_time_utc=ev["start_time_utc"], status=ev["status"],
                                    opponent_id=opp["participant_id"] if opp else None, opponent_name=opp["display_name"] if opp else None,
                                    competition=ev.get("competition"), path=R.event_path(eid)))
            if opp:
                opponents.append({"participant_id": opp["participant_id"], "display_name": opp["display_name"], "event_ids": [eid],
                                  "path": R.player_path(opp["participant_id"])})
                links.append(R.link(rel="OPPONENT", target_kind="entity_profile", label=opp["display_name"],
                                    target_id=opp["participant_id"], path=R.player_path(opp["participant_id"])))
            links.append(R.link(rel="EVENT", target_kind="event_research", label=ev.get("competition") or "event", target_id=eid,
                                path=R.event_path(eid)))
            for mk in sorted(markets_by_event.get(eid, []), key=lambda m: m["kalshi_ticker"]):
                if mk.get("participant_id") == pid:
                    mrefs.append(R.market_ref(mk))
                    for mp in prices_by_market.get(mk["market_id"], []):
                        src = (mp.get("model_version") or "").lower()
                        projs.append(R.projection_ref(mp, research_only=True, authority=AUTHORITY,
                                                      quality_status="VERIFIED" if src.startswith("gen1") else "RESEARCH"))
        rk_refs = []
        if pid in rated:
            for (t, surf), rk in sorted(rankings.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
                if t == tour and any(e["entity_id"] == pid for e in rk["entries"]):
                    rk_refs.append({"ranking_id": rk["ranking_id"], "metric_id": rk["metric_id"], "window_label": rk["window"]["label"],
                                    "split": rk["split"], "path": R.ranking_path(rk["ranking_id"])})
                    links.append(R.link(rel="RANKING", target_kind="ranking", label=f"{tour} Elo{(' ' + surf) if surf else ''}",
                                        target_id=rk["ranking_id"], path=R.ranking_path(rk["ranking_id"])))
        srefs = sorted(series_refs_by_player.get(pid, []), key=lambda r: r["series_id"])
        links += [R.link(rel="SERIES", target_kind="time_series", label="ledger model fair (match winner)", target_id=r["series_id"],
                         path=r["path"]) for r in srefs]
        membership = (["V1_SLATE"] if row["slate"] else []) + (["TOP_ELO_ACTIVE"] if rid and rid in top_ids.get(tour, []) else [])
        if rid:
            pq = q["ratings"]
        else:
            pq = _quality("PARTIAL", "v1 payload (assisted slate)", ctx, as_of=ctx.now,
                          limitations=[f"no rating: {res['status']} ({res['reason']})", unres_note, LIM_AUTHORITY])
        profiles.append(R.entity_profile(
            sport=SPORT, run_id=run_id, generated_at=ctx.now, entity=part, entity_type="PLAYER", quality=pq, league=tour,
            metrics=metrics_obs, splits=splits, series=srefs, rankings=rk_refs, games=games, opponents=opponents,
            markets=mrefs, projections=projs, links=links,
            extensions={"tour": tour, "universe_membership": membership,
                        "identity": {"status": res["status"], "reason": res["reason"], "rating_id": rid,
                                     "method": "exact normalised full name, unique in the tour rating state (identity/crosswalk.py rule)"},
                        "rating": ({"rating_id": rid, "ratings_as_of": ctx.ratings_as_of.get(tour), "ratings_built_at": ctx.rating_built.get(tour),
                                    "model_version": ratings[tour].get("model_version"), "matches_rated": rec.get("n"),
                                    "last_match_date": rec.get("last_date"),
                                    "surface_matches": {s: (rec.get("surfaces") or {}).get(s, [None, 0])[1] for s in SURFACES},
                                    "authority": AUTHORITY} if rid else None),
                        "discipline": "doubles" if res["status"] == NOT_SINGLES else "singles"}))

    # ---- capabilities, search
    docs = [registry] + list(rankings.values()) + profiles + event_docs + mh_docs + series_docs
    docs.append(_capabilities(ctx, inputs, q, metrics, rankings, profiles, event_docs, mh_docs, series_docs, unresolved, n_slate, top_n))
    docs.append(_search(ctx, players, rated, metrics, rankings, events))
    return docs


def _studies(studies: dict, ctx: _Ctx) -> dict:
    """RESEARCH registry entries for the committed one-off studies (Pinnacle benchmark, Elo walk-forward)."""
    out = {}
    pin = studies.get("pinnacle_ATP")
    if isinstance(pin, dict) and pin.get("scores"):
        qq = _quality("RESEARCH", "research/market_benchmark/results_ATP.json (one-off study on main)", ctx, production=False,
                      sample_size=pin.get("n_linked"), limitations=["one-off study (ATP only, 2020-2025 Pinnacle-linked matches)",
                                                                    "used for the Pinnacle benchmark only"])
        out["pinnacle"] = dict(sport=SPORT, slug="pinnacle_benchmark_brier", name="Pinnacle benchmark Brier (research)",
                               short_name="Pinnacle Brier", entity_type="MARKET", category="calibration", subcategory="benchmark",
                               stat_type="SCORE", higher_is_better=False, source="research/market_benchmark/results_ATP.json",
                               quality=qq, freshness="UNKNOWN",
                               description=("Walk-forward Brier / log loss / calibration of the production Elo column against de-vigged "
                                            "Pinnacle closing odds on linked ATP matches; extensions.scores carries the stored values and "
                                            "the paired bootstrap of Brier(model) - Brier(market)."),
                               update_frequency="one-off", known_limitations=["model worse than Pinnacle on every cut"],
                               extensions={"model_col": pin.get("model_col"), "n_linked": pin.get("n_linked"), "scores": pin.get("scores"),
                                           "bootstrap_model_minus_market_brier": pin.get("bootstrap_model_minus_market_brier")})
    elo = {t: studies.get(f"elo_study_{t}") for t in ("ATP", "WTA")}
    if any(isinstance(v, dict) and v.get("symmetric_scores") for v in elo.values()):
        qq = _quality("RESEARCH", "research/elo_study/results_{ATP,WTA}.json (one-off study on main)", ctx, production=False,
                      limitations=["one-off walk-forward study 1990-2026; per-match predictions in elo_study/predictions_*.parquet are not published"])
        out["elo_study"] = dict(sport=SPORT, slug="elo_study_brier", name="Elo variant walk-forward Brier (research)",
                                short_name="Elo study Brier", entity_type="MARKET", category="calibration", subcategory="walk_forward",
                                stat_type="SCORE", higher_is_better=False, source="research/elo_study/results_{ATP,WTA}.json",
                                quality=qq, freshness="UNKNOWN",
                                description=("Walk-forward (pre-match, no leakage) Brier / log loss / calibration of the Elo variants on "
                                             "every rated match since eval_from; extensions carry the stored symmetric scores, the best "
                                             "variant by log loss and the bootstrap against plain Elo."),
                                update_frequency="one-off", known_limitations=["Elo over-confident at K0 >= 250"],
                                extensions={t: ({k: v.get(k) for k in ("eval_from", "n_eval", "best_by_logloss", "symmetric_scores",
                                                                        "bootstrap_vs_elo_plain")} if isinstance(v, dict) else None)
                                            for t, v in elo.items()})
    val, hold, dec = studies.get("projection_v2_validate"), studies.get("projection_v2_holdout"), studies.get("projection_v2_decision")
    if isinstance(val, dict) and isinstance(dec, dict):
        def _lane(r, t, name):
            x = ((r or {}).get(t) or {}).get("lanes", {}).get(name) or {}
            return {k: x.get(k) for k in ("n", "brier", "log_loss", "cal_slope", "ece", "accuracy")}

        def _diff(r, t):
            x = ((r or {}).get(t) or {}).get("vs_incumbent", {}).get("CHALLENGER") or {}
            return {k: x.get(k) for k in ("n", "clusters", "brier_diff", "brier_ci", "ll_diff", "ll_ci")}
        qq = _quality("RESEARCH", "research/projection_v2/results_{validate,holdout}.json (preregistered study on main)", ctx,
                      production=False, sample_size=sum((_lane(val, t, "CHALLENGER").get("n") or 0) for t in ("ATP", "WTA")),
                      limitations=["2026 holdout data stops at the April (WTA ITF/125) / June (ATP ITF) source freeze",
                                   "live ITF projections run on 4-5 months of missing results and are graded POOR"])
        out["projection_v2"] = dict(sport=SPORT, slug="projection_v2_backtest", name="Projection V2 vs incumbent (preregistered backtest)",
                                    short_name="Projection V2", entity_type="MARKET", category="calibration", subcategory="walk_forward",
                                    stat_type="SCORE", higher_is_better=False, source="research/projection_v2/",
                                    quality=qq, freshness="UNKNOWN",
                                    description=("Independent pre-match model (no market input): margin-of-victory Elo + Gen-2 serve/return "
                                                 "by evidence + form + rest/layoff context + age, fitted walk-forward. 2021-2025 and the 2026 "
                                                 "holdout vs the incumbent, paired cluster bootstrap over tournaments; promotion rules P1-P9 "
                                                 "were committed before any result."),
                                    update_frequency="per research cycle", known_limitations=["the market remains more accurate than this model"],
                                    extensions={"verdict": dec.get("verdict"), "rules": dec.get("rules"),
                                                "spec_fingerprint": dec.get("spec_fingerprint"),
                                                **{f"{t}_2021_2025": {"incumbent": _lane(val, t, "INCUMBENT"),
                                                                      "challenger": _lane(val, t, "CHALLENGER"),
                                                                      "challenger_minus_incumbent": _diff(val, t)} for t in ("ATP", "WTA")},
                                                **{f"{t}_2026_holdout": {"incumbent": _lane(hold, t, "INCUMBENT"),
                                                                         "challenger": _lane(hold, t, "CHALLENGER"),
                                                                         "challenger_minus_incumbent": _diff(hold, t)} for t in ("ATP", "WTA")},
                                                "derivatives": (studies.get("projection_v2_derivatives") or {}).get("summary")})
    return out


def _capabilities(ctx, inputs, q, metrics, rankings, profiles, event_docs, mh_docs, series_docs, unresolved, n_slate, top_n) -> dict:
    C = R.capability
    mid = {k: v["metric_id"] for k, v in metrics.items()}
    rated_profile = next((p for p in profiles if (p["extensions"].get("rating") or {}).get("rating_id")), None)
    any_profile = profiles[0] if profiles else None
    ev0 = event_docs[0] if event_docs else None
    n_points = sum(len(s["points"]) for d in mh_docs for s in d["series"])
    first_quote = _earliest(p["captured_at"] for d in mh_docs for s in d["series"] for p in s["points"])
    m4_events = [d for d in event_docs if any(x["source"].startswith("model4") for x in d["distributions"])]
    split_ev = next((d for d in event_docs if any(r["metric_id"] == mid["elo_surface"] for r in d["matchup"])), None)
    matchup_ev = next((d for d in event_docs if any(r["metric_id"] in (mid["ledger_spw"], mid["gen2_spw"]) for r in d["matchup"])), None)
    ledger_since = inputs["ledger_days"][0] if inputs["ledger_days"] else None
    settle_since = inputs["settlement_runs"][0][:8] if inputs["settlement_runs"] else None
    settle_since = f"{settle_since[:4]}-{settle_since[4:6]}-{settle_since[6:8]}" if settle_since else None
    canon = ("the canonical match table (processed/matches.parquet) is rebuilt every run and is not on any branch; it cannot be "
             "loaded from committed files without a full rebuild, which this export does not do")
    caps = [
        C(capability="team_profiles", status="UNAVAILABLE", summary="tennis has no teams", reasons=["individual sport; Davis/United Cup rubbers are priced as singles; no team model"]),
        C(capability="team_metrics", status="UNAVAILABLE", summary="no team metrics", reasons=["individual sport; no team model (families.py: team-tie model not built)"]),
        C(capability="team_game_logs", status="UNAVAILABLE", summary="no teams", reasons=["individual sport"]),
        C(capability="player_game_logs", status="UNAVAILABLE", summary="per-player match history not published", reasons=[canon]),
        C(capability="historical_results", status="UNAVAILABLE", summary="results history not published", reasons=[canon]),
        C(capability="opponents", status="UNAVAILABLE", summary="historical opponents / H2H not published",
          reasons=[canon + "; H2H is derivable from that table but not stored", "profiles link only the current slate opponent"]),
        C(capability="schedule_strength", status="UNAVAILABLE", summary="no schedule-strength metric",
          reasons=["Gen-2 has per-(tour,level) offsets, not an opponent-schedule metric"]),
        C(capability="recent_form_windows", status="UNAVAILABLE", summary="no W-L form windows",
          reasons=["L5/L10 W-L not computed anywhere; the ledger/slate carry recency/experience inputs only ('not a win-loss form model')"]),
        C(capability="usage", status="UNAVAILABLE", summary="match duration not published", reasons=["the only usage datum (minutes) lives in the canonical table; " + canon]),
        C(capability="lineups", status="UNAVAILABLE", summary="no draws", reasons=["draw feed not wired (futures/draw.py exists, KNOWN_LIMITATIONS.md)"]),
        C(capability="injuries", status="UNAVAILABLE", summary="no injury / availability feed", reasons=["retirements/walkovers recorded post hoc as outcome_type only"]),
        C(capability="advanced_stats", status="UNAVAILABLE", summary="serve/return box statistics not published",
          reasons=["Sackmann serve statistics live in the canonical table; " + canon, "Match Charting Project files are downloaded but never read by code",
                   "the structural serve/return abilities are published under player_metrics"]),
        C(capability="player_props", status="UNAVAILABLE", summary="player props not priced", reasons=["PLAYER_ACES parsed, projectable: False (families.py)"]),
        C(capability="team_props", status="UNAVAILABLE", summary="no team props", reasons=["individual sport"]),
        C(capability="play_by_play", status="UNAVAILABLE", summary="no play-by-play", reasons=["MCP point-level files not ingested; in-play markets not priced"]),
        C(capability="weather", status="UNAVAILABLE", summary="no weather", reasons=["docs/DATA_SOURCES.md: not wired"]),
        C(capability="venue_effects", status="UNAVAILABLE", summary="no venue effects beyond surface",
          reasons=["surface lookup only (pricing/competition.py); indoor only from TML; altitude/court speed absent; the event's surface is shown in event context"]),
        C(capability="wager_history", status="UNAVAILABLE", summary="no wagers", reasons=["accounting-data ledgers empty; assisted track 0 decisions / 0 wagers"]),
    ]
    if rated_profile:
        n_rated = sum(1 for p in profiles if (p["extensions"].get("rating") or {}).get("rating_id"))
        caps += [
            C(capability="player_profiles", status="PARTIAL", entity_types=["PLAYER"],
              summary="rating-state profiles for every v1 participant and the top-N active players per tour",
              limitations=[LIM_RATINGS, LIM_AUTHORITY, q["ratings"]["limitations"][-1],
                           f"universe: v1 slate players + top {top_n} active by Elo per tour ({len(profiles)} profiles)"],
              evidence=[R.player_path(rated_profile["entity"]["participant_id"])], coverage=f"{len(profiles)} profiles, {n_rated} rated",
              metrics=[mid["elo"], mid["elo_surface"], mid["sr_serve"], mid["sr_return"], mid["sr_points"]], windows=["RATING_STATE"]),
            C(capability="player_metrics", status="PARTIAL", entity_types=["PLAYER"], summary="overall + surface Elo, structural serve/return abilities, serve-point evidence",
              limitations=[LIM_RATINGS, LIM_AUTHORITY], evidence=[R.player_path(rated_profile["entity"]["participant_id"])],
              coverage=q["ratings"]["coverage"], metrics=[mid["elo"], mid["elo_surface"], mid["sr_serve"], mid["sr_return"], mid["sr_points"]],
              windows=["RATING_STATE"]),
            C(capability="opponent_adjustment", status="PARTIAL", entity_types=["PLAYER"], summary="Elo and structural serve/return are opponent-adjusted by construction",
              limitations=[LIM_OPP_ADJ, LIM_RATINGS], evidence=[R.player_path(rated_profile["entity"]["participant_id"])],
              metrics=[mid["elo"], mid["sr_serve"], mid["sr_return"]]),
            C(capability="situational_splits", status="PARTIAL", entity_types=["PLAYER"], summary="per-surface Elo with surface match counts",
              limitations=[LIM_SURFACE, LIM_RATINGS], evidence=[R.player_path(rated_profile["entity"]["participant_id"])],
              metrics=[mid["elo_surface"]], splits=["surface"]),
        ]
    else:
        caps += [C(capability=c, status="UNAVAILABLE", summary="no rating state in this run", reasons=["processed/ratings_{ATP,WTA}.json absent"])
                 for c in ("player_metrics", "opponent_adjustment", "situational_splits")]
        if any_profile:      # v1 identities are still published, so the proving kind exists: PARTIAL, never UNAVAILABLE
            caps.append(C(capability="player_profiles", status="PARTIAL", entity_types=["PLAYER"], summary="v1 identities only (no rating state)",
                          limitations=["no rating state in this run"], evidence=[R.player_path(any_profile["entity"]["participant_id"])]))
        else:
            caps.append(C(capability="player_profiles", status="UNAVAILABLE", summary="no players", reasons=["no v1 events and no rating state"]))
    if rankings:
        rk0 = sorted(rankings.values(), key=lambda r: r["ranking_id"])[0]
        caps.append(C(capability="rankings", status="PARTIAL", entity_types=["PLAYER"], summary="Elo overall and per surface, per tour",
                      limitations=[LIM_RATINGS, "the universe is the published one (slate + top-N active), not every rated player"],
                      evidence=[R.ranking_path(rk0["ranking_id"])], metrics=[mid["elo"], mid["elo_surface"]], splits=["surface"],
                      coverage=f"{len(rankings)} rankings"))
    else:
        caps.append(C(capability="rankings", status="UNAVAILABLE", summary="no rankings", reasons=["no rating state in this run"]))
    if ev0:
        caps += [
            C(capability="event_research", status="PARTIAL", entity_types=["EVENT"], summary="one research document per v1 event",
              limitations=ev0["quality"]["limitations"], evidence=[R.event_path(ev0["event"]["event_id"])], coverage=f"{len(event_docs)} events"),
            C(capability="market_prices", status="VERIFIED", entity_types=["MARKET"], summary="every v1 market with bid/ask/captured_at",
              evidence=[R.event_path(ev0["event"]["event_id"])], coverage=f"{sum(len(d['markets']) for d in event_docs)} markets"),
            C(capability="game_markets", status="VERIFIED", entity_types=["MARKET"],
              summary="MATCH_WINNER, SET_WINNER, EXACT_SET_SCORE, TOTAL_GAMES, GAME_SPREAD, TOTAL_SETS, SET_SPREAD captured and priced",
              evidence=[R.event_path(ev0["event"]["event_id"])]),
            C(capability="comparisons", status="PARTIAL", entity_types=["PLAYER", "EVENT"], summary="side-by-side matchup rows with ranking context",
              limitations=[LIM_RATINGS, "player A sits in the 'home' slot and player B in the 'away' slot (no home/away in tennis)"],
              evidence=[R.event_path((split_ev or ev0)["event"]["event_id"])]),
        ]
    if mh_docs and n_points:
        caps.append(C(capability="market_price_history", status="VERIFIED", entity_types=["MARKET"],
                      summary="Kalshi quote history per ticker (10-15 min capture) for the current events",
                      limitations=mh_docs[0]["quality"]["limitations"], evidence=[R.market_history_path(mh_docs[0]["event_id"])],
                      coverage=f"{n_points} quote points over {len(mh_docs)} events", since=first_quote))
    else:
        caps.append(C(capability="market_price_history", status="UNAVAILABLE" if not mh_docs else "PARTIAL",
                      summary="no capture quotes in the window", reasons=["no kalshi/capture quote file in the read window"],
                      limitations=["no capture quotes in the window"] if mh_docs else None,
                      evidence=[R.market_history_path(mh_docs[0]["event_id"])] if mh_docs else None))
    if series_docs:
        caps += [
            C(capability="raw_projections", status="VERIFIED", entity_types=["MARKET"],
              summary="the prediction ledger's six model numbers per ticker per run (event projections) + per-ticker model-fair series",
              limitations=[LIM_AUTHORITY], evidence=[R.series_path(series_docs[0]["series_id"]),
                                                     R.event_path(series_docs[0]["points"][0]["event_id"])],
              coverage=q["ledger"]["coverage"], since=ledger_since, metrics=[mid["ledger_" + m] for m in LEDGER_MODELS], windows=["RUN"]),
            C(capability="time_series", status="PARTIAL", entity_types=["MARKET"], summary="per-ticker ledger model fair value, x = RUN",
              limitations=["per-ticker ledger history only (rows per ticker median 2, max 8); no per-player rating trajectory is published",
                           LIM_AUTHORITY], evidence=[R.series_path(series_docs[0]["series_id"])],
              coverage=f"{len(series_docs)} series", since=ledger_since, metrics=[mid["ledger_" + m] for m in SERIES_MODELS]),
        ]
    else:
        caps += [C(capability="raw_projections", status="UNAVAILABLE", summary="no ledger rows for the current tickers",
                   reasons=["research/ledger has no row for any current v1 ticker in this run"]),
                 C(capability="time_series", status="UNAVAILABLE", summary="no series", reasons=["no ledger rows for the current tickers"])]
    if m4_events:
        caps.append(C(capability="projection_distributions", status="RESEARCH", entity_types=["EVENT"],
                      summary="Model 4 set-score / games distributions and fair_v1 envelopes",
                      limitations=[LIM_PROJ_DIST, "Model 4 and fair_v1 are frozen RESEARCH producers", LIM_AUTHORITY],
                      evidence=[R.event_path(m4_events[0]["event"]["event_id"])], coverage=f"{len(m4_events)} events with Model 4 rows"))
    else:
        caps.append(C(capability="projection_distributions", status="UNAVAILABLE", summary="no Model 4 rows for the current matches in the window",
                      reasons=["research/frozen_producers/model4 has no row for a current match in the read window"]))
    if matchup_ev:
        caps.append(C(capability="matchup_metrics", status="PARTIAL", entity_types=["PLAYER"], summary="per-matchup serve-point probabilities (ledger inputs; Gen-2 RESEARCH)",
                      limitations=[LIM_MATCHUP, LIM_AUTHORITY], evidence=[R.event_path(matchup_ev["event"]["event_id"])],
                      metrics=[mid["ledger_spw"], mid["ledger_sr_spw"], mid["gen2_spw"]], windows=["GAME"]))
    else:
        caps.append(C(capability="matchup_metrics", status="UNAVAILABLE", summary="no ledger / Model 4 row for a current match",
                      reasons=["no matchup inputs stored for the current matches in this run"]))
    if "brier" in metrics:
        caps += [
            C(capability="calibration", status="PARTIAL", entity_types=["MARKET"], summary="market-vs-model Brier / log loss / calibration slope on settled rows",
              limitations=[LIM_CALIBRATION, LIM_TRUTH], evidence=[R.app_path(R.METRICS_NAME)], metrics=[mid["brier"]], since=settle_since,
              coverage=f"{(q['scorecard'] or {}).get('gradeable_with_mid')} gradeable settled rows"),
            C(capability="historical_accuracy", status="PARTIAL", entity_types=["MARKET"],
              summary="settlement scorecard + frozen-candidate confirmation statuses (+ per-ticker settlement in event research)",
              limitations=[LIM_TRUTH, "every frozen edge candidate is INSUFFICIENT_N or FAIL_ACCURACY"], evidence=[R.app_path(R.METRICS_NAME)],
              metrics=[mid["brier"]], since=settle_since),
        ]
    else:
        caps += [C(capability=c, status="UNAVAILABLE", summary="no settlement scorecard in this run", reasons=["research/settlements/SCORECARD.md absent"])
                 for c in ("calibration", "historical_accuracy")]
    if "clv" in metrics:
        caps.append(C(capability="clv", status="PARTIAL", entity_types=["MARKET"], summary="strict executable CLV by family with bootstrap CIs; per-ticker strict CLV where present",
                      limitations=[LIM_CLV, LIM_TRUTH, "Challenger, ITF and TEAM have 0 strict rows"], evidence=[R.app_path(R.METRICS_NAME)],
                      metrics=[mid["clv"]], since=settle_since))
    else:
        caps.append(C(capability="clv", status="UNAVAILABLE", summary="no CLV scorecard in this run", reasons=["research/candidate_confirmation/CLV_SCORECARD.json absent"]))
    caps.append(C(capability="search", status="VERIFIED", summary="players, events, metrics, rankings and series", evidence=[R.app_path(R.SEARCH_NAME)]))
    notes = [
        "audit: scratchpad/phase2/audit_tennis.md (2026-10-03), §4 capability matrix and §10 recommendations",
        "every model number is RESEARCH_ONLY authority: Kalshi mid Brier 0.1776 vs model 0.2193 on 15,117 settled rows; no evidence of edge",
        "identity: v1 participants keep their kalshi_player_name prt_ ids; a rating id attaches only on an exact, unique normalised full-name "
        "match in the tour's rating state that agrees with the slate's own player ids (crosswalk rule); top-N players not on the slate use "
        "the tennis_rating_id namespace",
        "external venue prices (Bovada/Smarkets de-vigged vs Kalshi vs model, VERIFIED production capture) ride in event research "
        "extensions.external_venues and context notes",
        "first-ball / start status per match (PARTIAL: ATP/WTA main tour + Slams only) rides in event research extensions.first_ball",
        "RESEARCH: Model 4 derivative distributions, fair_v1 envelopes, doubles ledger rows, the Pinnacle benchmark and the elo_study "
        "results (metrics.json); the elo_study per-match parquet files are not published",
        "UNAVAILABLE beyond the vocabulary: official rankings (acquired, unused), tournament-winner pricing, sports truth independent of the exchange",
        f"frozen candidates: {', '.join(c['candidate_id'] + ' ' + c['status'] for c in inputs['candidates'])}" if inputs["candidates"] else
        "frozen candidates: no candidate_confirmation files in this run",
    ] + list(inputs["warnings"])
    windows = [R.window("CUSTOM", label="RATING_STATE"), R.window("GAME"), R.window("RUN")]
    surf_vals = sorted({o["split"]["value"] for p in profiles for o in (p["splits"].get("surface") or [])})
    return R.capability_manifest(sport=SPORT, run_id=ctx.run_id, generated_at=ctx.now, capabilities=caps, audit_date=AUDIT_DATE,
                                 split_dimensions=[{"dimension": "surface", "values": surf_vals, "status": "PARTIAL"}] if surf_vals else [],
                                 windows=windows, notes=notes)


def _search(ctx, players, rated, metrics, rankings, events) -> dict:
    entries = []
    for pid in sorted(players):
        row = players[pid]
        p = row["participant"]
        rid = row["resolution"]["rating_id"] if pid in rated else None
        rec = ctx.ratings[row["tour"]]["players"][rid] if rid else {}
        aliases = [x for x in ((rec.get("name") if rec.get("name") != p["display_name"] else None), f"{row['tour']}:{rid}" if rid else None) if x]
        entries.append(R.search_entry(id=pid, kind="PLAYER", label=p["display_name"], path=R.player_path(pid), sport=SPORT,
                                      secondary=" · ".join(x for x in (row["tour"], "on the current slate" if row["slate"] else None) if x),
                                      aliases=aliases, league=row["tour"]))
    for ev in events:
        names = " vs ".join(p["display_name"] for p in ev["participants"]) or ev["event_id"]
        entries.append(R.search_entry(id=ev["event_id"], kind="EVENT", label=names, path=R.event_path(ev["event_id"]), sport=SPORT,
                                      secondary=ev.get("competition"), aliases=[(ev.get("source_ids") or {}).get(ax.EVENT_SOURCE) or ""],
                                      league=ev.get("league"), season=ev.get("season")))
    for m in metrics.values():
        entries.append(R.search_entry(id=m["metric_id"], kind="METRIC", label=m["name"], path=R.app_path(R.METRICS_NAME), sport=SPORT,
                                      secondary=m["category"], aliases=[m["short_name"]]))
    for (tour, surf), rk in sorted(rankings.items(), key=lambda kv: (kv[0][0], kv[0][1] or "")):
        entries.append(R.search_entry(id=rk["ranking_id"], kind="RANKING", label=f"{tour} Elo ranking{(' (' + surf + ')') if surf else ''}",
                                      path=R.ranking_path(rk["ranking_id"]), sport=SPORT, secondary=rk["universe"]["label"], league=tour))
    return R.search_index(sport=SPORT, run_id=ctx.run_id, generated_at=ctx.now, entries=entries)


def explorer_as_of(inputs: dict) -> str | None:
    """The newest data timestamp the explorer describes."""
    stamps = [st.get("built_at") for st in inputs["ratings"].values()]
    stamps += [inputs["slate"].get("built_at")]
    stamps += [r.get("generated_at_utc") for r in inputs["ledger"]] + [r.get("captured_at") for r in inputs["quotes"]]
    stamps += [r.get("generated_at") for r in inputs["dislocations"]] + [r.get("observed_at_utc") for r in inputs["truths"]]
    stamps += [r.get("predicted_at") for r in inputs["model4"]]
    real = [s for s in stamps if s and timeutil.parse_ts(s) <= timeutil.parse_ts(inputs["now"])]
    return _latest(real)


def index_bytes(docs: list[dict], *, run_id: str, now) -> int:
    """Size of the explorer/index.json these documents would produce (the publication builds the same table)."""
    by_path = {R.path_for(d): d for d in docs}
    texts = {rel: dumps(d) for rel, d in by_path.items()}
    probe = R.quality(status="UNKNOWN", source="index size probe", generated_at=now, production=False)
    idx = R.build_index(sport=SPORT, run_id=run_id, generated_at=now, documents=by_path, texts=texts, quality=probe)
    return len(dumps(idx, compact=False).encode("utf-8"))


def fit_index_budget(inputs: dict, *, now, run_id: str, top_n: int = TOP_N, budget: int = INDEX_BUDGET,
                     margin: int = 2_500) -> tuple[list[dict], int]:
    """Build with ``top_n``; if the index would exceed the budget, shrink the top-N tail (never a v1 participant)
    until it fits. Deterministic for the same inputs. Returns (documents, the top-N actually used)."""
    n = top_n
    while True:
        docs = build_explorer(inputs, now=now, run_id=run_id, top_n=n)
        excess = index_bytes(docs, run_id=run_id, now=now) - (budget - margin)
        if excess <= 0 or n == 0:
            return docs, n
        n = max(0, n - (excess // 500 + 1))


def export_explorer(app_root: str, data_root: str, *, now=None, repo_root: str = REPO_ROOT, top_n: int = TOP_N,
                    capture_days: int = CAPTURE_DAYS, commit_sha=None) -> dict:
    """Load, build and publish atomically (``research.publish_explorer``). Raises without touching the previous tree."""
    inputs = load_inputs(data_root, app_root, now=now, repo_root=repo_root, capture_days=capture_days)
    manifest = inputs["manifest"]
    now = inputs["now"]
    run_id = manifest["run_id"]
    docs, n_used = fit_index_budget(inputs, now=now, run_id=run_id, top_n=top_n)
    if n_used != top_n:
        inputs = dict(inputs, warnings=inputs["warnings"] + [
            f"top-N reduced from {top_n} to {n_used} per tour to keep explorer/index.json under {INDEX_BUDGET} bytes"])
        docs = build_explorer(inputs, now=now, run_id=run_id, top_n=n_used)
    as_of = explorer_as_of(inputs)
    q = R.quality(status="PARTIAL", source="Tennis-Edge-Finder committed data (tennis-data branch + research/ on main)",
                  generated_at=now, production=True, data_as_of=as_of, methodology_version=METHODOLOGY_VERSION,
                  limitations=[LIM_RATINGS, LIM_AUTHORITY, "see capabilities.json for every UNAVAILABLE capability and why"])
    return R.publish_explorer(app_root=Path(app_root), sport=SPORT, run_id=run_id, generated_at=now, documents=docs, quality=q,
                              as_of=as_of, commit_sha=commit_sha or manifest.get("commit_sha"), base_manifest_run_id=run_id,
                              windows=[R.window("CUSTOM", label="RATING_STATE"), R.window("GAME"), R.window("RUN")],
                              warnings=inputs["warnings"])


def run_cli(argv: list[str] | None = None) -> int:
    import argparse

    ap = argparse.ArgumentParser(description="Publish the TENNIS research graph (explorer/) beside the v1 app export")
    ap.add_argument("--out", default=os.path.join("data", "app", "latest"), help="the v1 app root (same --out as app_export.py)")
    ap.add_argument("--data-root", default="data")
    ap.add_argument("--now", default=None, help="ISO timestamp with zone; default: the v1 manifest's generated_at")
    ap.add_argument("--repo-root", default=REPO_ROOT)
    ap.add_argument("--top-n", type=int, default=TOP_N)
    ap.add_argument("--capture-days", type=int, default=CAPTURE_DAYS)
    ap.add_argument("--commit-sha", default=None)
    a = ap.parse_args(argv)
    try:
        index = export_explorer(a.out, a.data_root, now=timeutil.parse_ts(a.now) if a.now else None, repo_root=a.repo_root,
                                top_n=a.top_n, capture_days=a.capture_days, commit_sha=a.commit_sha)
    except Exception as exc:  # noqa: BLE001 -- the explorer is additive: report, leave the previous tree, exit 1
        problems = getattr(exc, "problems", None)
        print(f"research export FAILED ({type(exc).__name__}): {exc}", file=sys.stderr)
        for p in (problems or [])[:20]:
            print(f"  - {p}", file=sys.stderr)
        print("explorer/ left as last-known-good; the v1 payload is unaffected", file=sys.stderr)
        return 1
    sizes = R.tree_bytes(Path(a.out))
    print(f"research export OK: run {index['run_id']} -> {os.path.join(a.out, R.EXPLORER_DIR)}")
    print("  " + " ".join(f"{k}={v}" for k, v in index["counts"].items()))
    print("  bytes " + " ".join(f"{k}={v}" for k, v in sizes.items()))
    return 0
