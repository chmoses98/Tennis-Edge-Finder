"""Discrepancy sanity layer: WHY is the model so far from the market, before anyone reads the gap as an edge.

The governing view: an independent tennis model should usually sit close to an efficient market. A small
model-market gap is normal, a moderate one may be interesting, a large one needs an explanation and an
extreme one is a diagnostic alarm until proven otherwise. "Model 80%, Kalshi 20%" first asks "why are we
so different?" -- a stale or in-play quote, a mapping or orientation fault, thin player data -- and only
then, maybe, "is the market wrong?".

This module only CLASSIFIES. It never changes a model probability, never re-prices, never re-orients and
never selects a bet: it labels how a disagreement may be presented to a human/ChatGPT handicapper and
which checks a BET on an extreme disagreement must pass before it is even eligible for human review.

Every tag is backed by a measured value carried in `evidence`; nothing is guessed. Thresholds live in
`config/discrepancy_sanity.json` (versioned; never fitted to outcomes or P&L).

Vocabulary
  bands             NORMAL <10pp, REVIEW 10-15, HIGH_REVIEW 15-25, EXTREME >=25 (UNPRICED: no model or no mid)
  sanity status     OK, REVIEW_CONTEXT, EXPLANATION_REQUIRED_BEFORE_BET, DATA_WARNING,
                    ELIGIBLE_FOR_HUMAN_REVIEW (decision time only), NOT_APPLICABLE
  identity          IDENTITY_VERIFIED, IDENTITY_AMBIGUOUS, IDENTITY_FAILED (any ambiguity fails closed)
  orientation       VERIFIED, FAILED, UNKNOWN, NOT_APPLICABLE (contracts with no named player)
  freshness         FRESH <=10 min, AGING <=30 min, STALE >30 min, UNKNOWN
  triangulation     MODEL_LONE_OUTLIER, KALSHI_LONE_OUTLIER, EXTERNAL_LONE_OUTLIER, MARKETS_AGREE,
                    ALL_THREE_DISAGREE, INSUFFICIENT_INPUTS
  external          AGREES_WITH_KALSHI, AGREES_WITH_MODEL, SUPPORTS_MODEL_DIRECTION, EXTERNAL_OUTLIER,
                    ALL_AGREE, ALL_DISAGREE, NO_EXTERNAL_REFERENCE, EXTERNAL_STALE, INSUFFICIENT_INPUTS
  data quality      ADEQUATE, LIMITED, POOR, UNKNOWN
"""
from __future__ import annotations

import json
import math
import os
import re
from datetime import date, datetime, timedelta

HERE = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.abspath(os.path.join(HERE, "..", "..", "config", "discrepancy_sanity.json"))

NORMAL, REVIEW, HIGH_REVIEW, EXTREME, UNPRICED = "NORMAL", "REVIEW", "HIGH_REVIEW", "EXTREME", "UNPRICED"
BANDS = (NORMAL, REVIEW, HIGH_REVIEW, EXTREME)
BAND_RANK = {UNPRICED: -1, NORMAL: 0, REVIEW: 1, HIGH_REVIEW: 2, EXTREME: 3}

OK, REVIEW_CONTEXT, EXPLANATION_REQUIRED = "OK", "REVIEW_CONTEXT", "EXPLANATION_REQUIRED_BEFORE_BET"
DATA_WARNING, ELIGIBLE, NOT_APPLICABLE = "DATA_WARNING", "ELIGIBLE_FOR_HUMAN_REVIEW", "NOT_APPLICABLE"
SANITY_STATUSES = (OK, REVIEW_CONTEXT, EXPLANATION_REQUIRED, DATA_WARNING, ELIGIBLE, NOT_APPLICABLE)

ID_VERIFIED, ID_AMBIGUOUS, ID_FAILED = "IDENTITY_VERIFIED", "IDENTITY_AMBIGUOUS", "IDENTITY_FAILED"
IDENTITY_STATUSES = (ID_VERIFIED, ID_AMBIGUOUS, ID_FAILED)
ORIENT_STATUSES = ("VERIFIED", "FAILED", "UNKNOWN", "NOT_APPLICABLE")
FRESH, AGING, STALE, UNKNOWN = "FRESH", "AGING", "STALE", "UNKNOWN"
FRESHNESS = (FRESH, AGING, STALE, UNKNOWN)
TRIANGULATION = ("MODEL_LONE_OUTLIER", "KALSHI_LONE_OUTLIER", "EXTERNAL_LONE_OUTLIER", "MARKETS_AGREE",
                 "ALL_THREE_DISAGREE", "INSUFFICIENT_INPUTS")
EXTERNAL_STATUSES = ("AGREES_WITH_KALSHI", "AGREES_WITH_MODEL", "SUPPORTS_MODEL_DIRECTION", "EXTERNAL_OUTLIER",
                     "ALL_AGREE", "ALL_DISAGREE", "NO_EXTERNAL_REFERENCE", "EXTERNAL_STALE", "INSUFFICIENT_INPUTS")
EXTERNAL_SUPPORTS = ("AGREES_WITH_MODEL", "SUPPORTS_MODEL_DIRECTION")
EXTERNAL_UNAVAILABLE = ("NO_EXTERNAL_REFERENCE", "EXTERNAL_STALE")
DATA_STATUSES = ("ADEQUATE", "LIMITED", "POOR", "UNKNOWN")

#: structured reason tags. The first block is the mission vocabulary; the second adds measured causes the
#: audit found (in-play risk where no first-ball source exists, models disagreeing with each other).
REASON_TAGS = (
    "STALE_KALSHI_QUOTE", "ONE_SIDED_BOOK", "WIDE_SPREAD", "LOW_DISPLAYED_LIQUIDITY", "PLAYER_IDENTITY_RISK",
    "TICKER_SIDE_RISK", "EVENT_MAPPING_RISK", "LOW_DATA_QUALITY", "THIN_PLAYER_HISTORY", "ASYMMETRIC_SAMPLE_SIZE",
    "STALE_PLAYER_DATA", "LEVEL_TRANSFER_RISK", "SURFACE_DATA_THIN", "MODEL_HIGH_UNCERTAINTY",
    "MODEL_CALIBRATION_OUTLIER", "EXTERNAL_MARKET_CONFIRMATION", "EXTERNAL_MARKET_REJECTION",
    "NO_EXTERNAL_REFERENCE", "UNKNOWN",
    "START_UNVERIFIABLE", "SCHEDULED_START_PASSED", "MODEL_INTERNAL_DISAGREEMENT",
)
#: tags that describe context rather than a candidate CAUSE of the gap (UNKNOWN is set when only these exist)
_CONTEXT_TAGS = {"EXTERNAL_MARKET_CONFIRMATION", "EXTERNAL_MARKET_REJECTION", "NO_EXTERNAL_REFERENCE", "UNKNOWN"}
#: identity checks whose failure is a PLAYER problem vs an EVENT/market mapping problem
_PLAYER_CHECKS = ("player_ids", "identity_confidence", "namesake", "model_name_orientation")
_EVENT_CHECKS = ("physical_match_id", "both_sides_listed", "model_complement", "market_pair", "level_mapping",
                 "same_pair_other_event", "discipline")

#: the nine conditions under which an EXTREME disagreement may become eligible for human review (Part J)
EXTREME_CONDITIONS = ("identity_verified", "ticker_orientation_verified", "fresh_executable_price",
                      "adequate_data_quality", "no_severe_asymmetry_or_justified",
                      "external_supports_or_documented_unavailable", "explains_why_market_may_be_wrong",
                      "explains_why_model_may_be_wrong", "price_clears_fees_and_execution")

_CFG_CACHE: dict = {}


def load_config(path: str | None = None) -> dict:
    p = path or CONFIG_PATH
    if p not in _CFG_CACHE:
        with open(p) as f:
            _CFG_CACHE[p] = json.load(f)
    return _CFG_CACHE[p]


def config_version(cfg: dict | None = None) -> str:
    return (cfg or load_config())["version"]


# ---------------------------------------------------------------------------------------------- numbers
def valid_probability(x) -> bool:
    """A probability is a real, finite number in [0, 1]. Booleans and strings are malformed."""
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x) and 0.0 <= x <= 1.0


def gap_pp(p_model, p_market) -> float | None:
    """Signed model-minus-market gap in percentage points (None when either side is missing/malformed)."""
    if not (valid_probability(p_model) and valid_probability(p_market)):
        return None
    return round(100.0 * (p_model - p_market), 2)


def executable_gap_pp(p_model, bid, ask) -> float | None:
    """How far the model sits OUTSIDE the executable book, before fees: max(p - ask, bid - p, 0) in pp.
    Zero means the model lies inside the spread: nothing is executable in its direction."""
    if not (valid_probability(p_model) and valid_probability(bid) and valid_probability(ask)) or bid > ask:
        return None
    return round(100.0 * max(p_model - ask, bid - p_model, 0.0), 2)


def band_of(gap, cfg: dict | None = None) -> str:
    if gap is None:
        return UNPRICED
    b = (cfg or load_config())["bands_pp"]
    a = abs(gap) + 1e-9                                  # 25.00 pp is EXTREME, 24.99 is not
    if a >= b["EXTREME"]:
        return EXTREME
    if a >= b["HIGH_REVIEW"]:
        return HIGH_REVIEW
    if a >= b["REVIEW"]:
        return REVIEW
    return NORMAL


def audit_bucket(abs_gap, edges=None) -> str | None:
    """'0-3', '3-5', ..., '40+' for an absolute gap in pp (lower edge inclusive)."""
    if abs_gap is None:
        return None
    e = list(edges or load_config()["audit_buckets_pp"])
    a = abs(abs_gap) + 1e-9
    for lo, hi in zip(e, e[1:]):
        if lo <= a < hi:
            return f"{lo}-{hi}"
    return f"{e[-1]}+"


def bucket_labels(edges=None) -> list[str]:
    e = list(edges or load_config()["audit_buckets_pp"])
    return [f"{lo}-{hi}" for lo, hi in zip(e, e[1:])] + [f"{e[-1]}+"]


def freshness_of(age_s, cfg: dict | None = None) -> str:
    """FRESH / AGING / STALE from a quote age in seconds. A negative age beyond clock skew is UNKNOWN."""
    if not isinstance(age_s, (int, float)) or isinstance(age_s, bool) or not math.isfinite(age_s) or age_s < -120:
        return UNKNOWN
    f = (cfg or load_config())["freshness_minutes"]
    m = max(age_s, 0.0) / 60.0
    if m <= f["FRESH"]:
        return FRESH
    if m <= f["AGING"]:
        return AGING
    return STALE


# ---------------------------------------------------------------------------------------------- identity
_CODE_RE = re.compile(r"^\d{2}[A-Z]{3}\d{2}([A-Z0-9]+)$")


def ticker_orientation(ticker: str | None, event: str | None, subject_is_a) -> tuple[str, dict]:
    """Does the contract's YES side name the player our A/B orientation says it does?

    Kalshi match codes are DATE + the two players' codes in listing order (A then B); a match-winner
    ticker ends with its subject's code. VERIFIED: the suffix sits on exactly the side `subject_is_a`
    claims. FAILED: it sits on the other side. UNKNOWN: no claim, no code, or the suffix fits both or
    neither side (never guessed)."""
    ev = {"ticker": ticker, "event": event, "subject_is_a": subject_is_a}
    if subject_is_a is None or not ticker:
        return "UNKNOWN", {**ev, "reason": "no subject orientation to verify"}
    parts = (event or ticker).split("-")
    m = _CODE_RE.match(parts[1]) if len(parts) > 1 else None
    if not m:
        return "UNKNOWN", {**ev, "reason": "unparseable match code"}
    players, suffix = m.group(1), ticker.split("-")[-1]
    first, last = players.startswith(suffix), players.endswith(suffix)
    if first == last:                                     # both (identical codes) or neither: cannot tell
        return "UNKNOWN", {**ev, "players_code": players, "suffix": suffix, "reason": "suffix fits both or neither side"}
    pos_a = first
    status = "VERIFIED" if pos_a == bool(subject_is_a) else "FAILED"
    return status, {**ev, "players_code": players, "suffix": suffix, "suffix_side": "A" if pos_a else "B"}


def derivative_orientation(has_subject: bool, contract_subject_is_a, model_subject_is_a) -> str:
    """Orientation of a derivative contract: NOT_APPLICABLE when it names no player (totals), VERIFIED
    when the contract and the model row agree on which player it names, FAILED when they disagree."""
    if not has_subject:
        return "NOT_APPLICABLE"
    if contract_subject_is_a is None or model_subject_is_a is None:
        return "UNKNOWN"
    return "VERIFIED" if bool(contract_subject_is_a) == bool(model_subject_is_a) else "FAILED"


def identity_status(checks: dict[str, str]) -> str:
    """checks: name -> PASS | AMBIGUOUS | FAIL | NA. Any FAIL fails; any AMBIGUOUS is ambiguous (fail closed)."""
    vals = set(checks.values())
    if "FAIL" in vals:
        return ID_FAILED
    if "AMBIGUOUS" in vals or not any(v == "PASS" for v in vals):
        return ID_AMBIGUOUS
    return ID_VERIFIED


def check_physical_match_id(pmid) -> str:
    if not pmid:
        return "AMBIGUOUS"
    return "PASS" if re.match(r"^(ATP|WTA|MIXED|ANY):[^:]+:[^:]+:\d{4}-\d{2}-\d{2}$", str(pmid)) else "FAIL"


def check_player_ids(a, b) -> str:
    if not a or not b:
        return "AMBIGUOUS"
    return "PASS" if str(a) != str(b) else "FAIL"


def check_identity_confidence(*conf) -> str:
    vals = [c for c in conf if c is not None]
    if not vals:
        return "AMBIGUOUS"
    return "PASS" if all(isinstance(c, (int, float)) and c >= 1.0 - 1e-9 for c in vals) else "AMBIGUOUS"


def check_complement(p_a, p_b, cfg: dict | None = None) -> str:
    """P(A) + P(B) of the same model on the two match-winner contracts must be 1."""
    if not (valid_probability(p_a) and valid_probability(p_b)):
        return "NA"
    tol = (cfg or load_config())["model"]["complement_tolerance"]
    return "PASS" if abs(p_a + p_b - 1.0) <= tol else "FAIL"


def check_market_pair(mid_a, mid_b, cfg: dict | None = None) -> str:
    """The two match-winner books of one event should roughly sum to 1; a large deviation means one book is
    stale, one-sided or not the same match."""
    if not (valid_probability(mid_a) and valid_probability(mid_b)):
        return "NA"
    tol = (cfg or load_config())["book"]["pair_mid_sum_tolerance"]
    return "PASS" if abs(mid_a + mid_b - 1.0) <= tol else "AMBIGUOUS"


def check_level(series_bucket: str | None, model_bucket: str | None) -> str:
    if not series_bucket or not model_bucket or model_bucket == "OTHER" or series_bucket == "OTHER":
        return "NA"
    return "PASS" if series_bucket == model_bucket else "AMBIGUOUS"


def namesake_index(ratings_paths, *, as_of: date | None = None, active_days: int | None = None) -> dict[str, int]:
    """normalised full name -> number of DIFFERENT player ids with that name active within `active_days` of
    `as_of` (rating-state files; missing files are skipped). A count >= 2 is a namesake risk."""
    tables = []
    for p in ratings_paths:
        try:
            tables.append((json.load(open(p)) or {}).get("players") or {})
        except (OSError, ValueError):
            continue
    return namesake_index_from_players(tables, as_of=as_of, active_days=active_days)


def namesake_index_from_players(tables, *, as_of: date | None = None, active_days: int | None = None) -> dict[str, int]:
    """Same as namesake_index, from already-loaded rating-state `players` tables (id -> {name, last_date})."""
    from tennis_edge.identity.names import normalize_name
    active_days = active_days or load_config()["identity"]["namesake_active_days"]
    as_of = as_of or date.today()
    cutoff = (as_of - timedelta(days=active_days)).isoformat()
    out: dict[str, int] = {}
    for players in tables:
        for _pid, v in players.items():
            if not isinstance(v, dict) or not v.get("name") or (v.get("last_date") or "") < cutoff:
                continue
            k = normalize_name(v["name"])
            out[k] = out.get(k, 0) + 1
    return out


def check_namesakes(names, index: dict | None) -> str:
    if index is None:
        return "NA"                                       # no registry loaded: the producers' mapper fails closed on namesakes
    from tennis_edge.identity.names import normalize_name
    return "AMBIGUOUS" if any(index.get(normalize_name(n), 0) >= 2 for n in names if n) else "PASS"


# ---------------------------------------------------------------------------------------------- market / external
def book_tags(bid, ask, bid_size, ask_size, cfg: dict | None = None) -> tuple[list[str], dict]:
    c = (cfg or load_config())["book"]
    two = valid_probability(bid) and valid_probability(ask) and 0 < bid <= ask < 1
    tags, ev = [], {"two_sided": two, "bid": bid, "ask": ask, "bid_size": bid_size, "ask_size": ask_size}
    if not two:
        tags.append("ONE_SIDED_BOOK")
        return tags, ev
    ev["spread"] = round(ask - bid, 4)
    if ask - bid > c["wide_spread"] + 1e-9:
        tags.append("WIDE_SPREAD")
    sizes = [s for s in (bid_size, ask_size) if isinstance(s, (int, float))]
    if sizes and min(sizes) < c["low_displayed_size"]:
        tags.append("LOW_DISPLAYED_LIQUIDITY")
    mid = 0.5 * (bid + ask)
    ev["tail_price"] = mid <= c["tail_mid"] or mid >= 1 - c["tail_mid"]
    return tags, ev


def triangulate(p_model, p_kalshi, p_ext, cfg: dict | None = None) -> str:
    """Which of model / Kalshi / external is the odd one out (agreement = within `external.agree_pp`)."""
    if not (valid_probability(p_model) and valid_probability(p_kalshi) and valid_probability(p_ext)):
        return "INSUFFICIENT_INPUTS"
    tol = (cfg or load_config())["external"]["agree_pp"] / 100.0 + 1e-9
    d = {"ke": abs(p_kalshi - p_ext), "me": abs(p_model - p_ext), "mk": abs(p_model - p_kalshi)}
    agree = {k for k, v in d.items() if v <= tol}
    if len(agree) == 3:
        return "MARKETS_AGREE"
    if not agree:
        return "ALL_THREE_DISAGREE"
    closest = min(agree, key=lambda k: d[k])               # several pairs agree but not all: the tightest pair
    return {"ke": "MODEL_LONE_OUTLIER", "me": "KALSHI_LONE_OUTLIER", "mk": "EXTERNAL_LONE_OUTLIER"}[closest]


def external_confirmation(p_model, p_kalshi, p_ext, ext_age_s=None, cfg: dict | None = None) -> tuple[str, str]:
    """(external confirmation status, triangulation) of a model-vs-Kalshi disagreement."""
    c = (cfg or load_config())["external"]
    if not valid_probability(p_ext):
        return "NO_EXTERNAL_REFERENCE", "INSUFFICIENT_INPUTS"
    if isinstance(ext_age_s, (int, float)) and ext_age_s > c["max_age_minutes"] * 60:
        return "EXTERNAL_STALE", "INSUFFICIENT_INPUTS"
    tri = triangulate(p_model, p_kalshi, p_ext, cfg)
    if tri == "INSUFFICIENT_INPUTS":
        return "INSUFFICIENT_INPUTS", tri
    status = {"MODEL_LONE_OUTLIER": "AGREES_WITH_KALSHI", "KALSHI_LONE_OUTLIER": "AGREES_WITH_MODEL",
              "MARKETS_AGREE": "ALL_AGREE", "EXTERNAL_LONE_OUTLIER": "EXTERNAL_OUTLIER"}.get(tri)
    if status is None:                                     # all three apart: does the external at least lean the model's way?
        tol = c["agree_pp"] / 100.0
        same_dir = (p_ext - p_kalshi) * (p_model - p_kalshi) > 0 and abs(p_ext - p_kalshi) >= tol
        status = "SUPPORTS_MODEL_DIRECTION" if same_dir else "ALL_DISAGREE"
    return status, tri


# ---------------------------------------------------------------------------------------------- data quality
def data_quality(*, grade=None, serve_a=None, serve_b=None, n_a=None, n_b=None, days_a=None, days_b=None,
                 level_familiarity=None, surface_n_a=None, surface_n_b=None, cfg: dict | None = None) -> dict:
    """ADEQUATE / LIMITED / POOR / UNKNOWN plus the measured tags. Asymmetry = deeper / thinner serve sample."""
    c = (cfg or load_config())["data"]
    tags = []
    serves = [s for s in (serve_a, serve_b) if isinstance(s, (int, float))]
    ns = [n for n in (n_a, n_b) if isinstance(n, (int, float))]
    lo = min(serves) if len(serves) == 2 else None
    hi = max(serves) if len(serves) == 2 else None
    ratio = (hi / max(lo, 1.0)) if lo is not None else None
    severe = bool(ratio is not None and (ratio >= c["severe_asymmetry_ratio"]))
    if grade in c["low_grades"]:
        tags.append("LOW_DATA_QUALITY")
    if (lo is not None and lo < c["thin_serve_points"]) or (len(ns) == 2 and min(ns) < c["thin_matches"]):
        tags.append("THIN_PLAYER_HISTORY")
    if ratio is not None and ratio >= c["asymmetry_ratio"]:
        tags.append("ASYMMETRIC_SAMPLE_SIZE")
    days = [d for d in (days_a, days_b) if isinstance(d, (int, float))]
    if days and max(days) > c["stale_player_days"]:
        tags.append("STALE_PLAYER_DATA")
    if isinstance(level_familiarity, (int, float)) and level_familiarity < c["level_familiarity_low"]:
        tags.append("LEVEL_TRANSFER_RISK")
    sn = [s for s in (surface_n_a, surface_n_b) if isinstance(s, (int, float))]
    if sn and min(sn) < c["thin_surface_matches"]:
        tags.append("SURFACE_DATA_THIN")
    if grade is None and lo is None:
        status = "UNKNOWN"
    elif grade in c["poor_grades"] or (lo is not None and lo < c["very_thin_serve_points"]) or severe:
        status = "POOR"
    elif tags:
        status = "LIMITED"
    else:
        status = "ADEQUATE"
    return {"data_quality_status": status, "tags": tags, "severe_sample_asymmetry": severe,
            "evidence": {"grade": grade, "serve_points_a": _r(serve_a, 0), "serve_points_b": _r(serve_b, 0),
                         "thinner_serve_points": _r(lo, 0), "sample_ratio": _r(ratio, 2), "matches_a": n_a,
                         "matches_b": n_b, "days_since_last_a": days_a, "days_since_last_b": days_b,
                         "level_familiarity": level_familiarity, "surface_matches_a": surface_n_a,
                         "surface_matches_b": surface_n_b}}


def _r(x, n=4):
    return round(x, n) if isinstance(x, (int, float)) and not isinstance(x, bool) else x


# ---------------------------------------------------------------------------------------------- assessment
def assess(*, p_model, bid, ask, bid_size=None, ask_size=None, quote_age_s=None, identity: str = ID_AMBIGUOUS,
           identity_checks: dict | None = None, orientation: str = "UNKNOWN", data: dict | None = None,
           p_ext=None, ext_age_s=None, model_uncertainty=None, envelope=None, model_probs: dict | None = None,
           first_ball_source: bool = True, scheduled_start_passed: bool = False, side_edge_after_fees=None,
           cfg: dict | None = None) -> dict:
    """The full sanity block of one contract at one moment (slate build or decision). Pure; no I/O.

    `p_model` and every number are read as given: nothing is re-oriented or re-priced here."""
    cfg = cfg or load_config()
    data = data or data_quality(cfg=cfg)
    malformed = [k for k, v in {"model_probability_yes": p_model, **(model_probs or {})}.items()
                 if v is not None and not valid_probability(v)]
    two = valid_probability(bid) and valid_probability(ask) and 0 < bid <= ask < 1
    mid = 0.5 * (bid + ask) if two else None
    g = gap_pp(p_model, mid) if not malformed else None
    band = band_of(g, cfg)
    fresh = freshness_of(quote_age_s, cfg)
    btags, bev = book_tags(bid, ask, bid_size, ask_size, cfg)
    ext_status, tri = external_confirmation(p_model, mid, p_ext, ext_age_s, cfg) if g is not None \
        else ("INSUFFICIENT_INPUTS", "INSUFFICIENT_INPUTS")
    checks = identity_checks or {}

    tags: list[str] = []
    if fresh == STALE:
        tags.append("STALE_KALSHI_QUOTE")
    tags += btags
    if any(checks.get(k) in ("FAIL", "AMBIGUOUS") for k in _PLAYER_CHECKS):
        tags.append("PLAYER_IDENTITY_RISK")
    if orientation not in ("VERIFIED", "NOT_APPLICABLE"):
        tags.append("TICKER_SIDE_RISK")
    if any(checks.get(k) in ("FAIL", "AMBIGUOUS") for k in _EVENT_CHECKS):
        tags.append("EVENT_MAPPING_RISK")
    tags += data.get("tags") or []
    env_w = (max(envelope) - min(envelope)) if envelope and all(valid_probability(x) for x in envelope) else None
    mc = cfg["model"]
    if (isinstance(model_uncertainty, (int, float)) and model_uncertainty >= mc["high_uncertainty"]) or \
            (env_w is not None and env_w >= mc["wide_envelope"]):
        tags.append("MODEL_HIGH_UNCERTAINTY")
    lo_mid, hi_mid = mc["market_middle"]
    if valid_probability(p_model) and mid is not None and \
            (p_model <= mc["tail_probability"] or p_model >= 1 - mc["tail_probability"]) and lo_mid <= mid <= hi_mid:
        tags.append("MODEL_CALIBRATION_OUTLIER")
    mp = [v for v in (model_probs or {}).values() if valid_probability(v)]
    spread_models = round(100 * (max(mp) - min(mp)), 2) if len(mp) >= 2 else None
    if spread_models is not None and spread_models >= mc["internal_disagreement_pp"]:
        tags.append("MODEL_INTERNAL_DISAGREEMENT")
    if ext_status in EXTERNAL_SUPPORTS:
        tags.append("EXTERNAL_MARKET_CONFIRMATION")
    elif ext_status == "AGREES_WITH_KALSHI":
        tags.append("EXTERNAL_MARKET_REJECTION")
    elif ext_status in EXTERNAL_UNAVAILABLE:
        tags.append("NO_EXTERNAL_REFERENCE")
    if not first_ball_source and BAND_RANK[band] >= BAND_RANK[HIGH_REVIEW]:
        tags.append("START_UNVERIFIABLE")
    if scheduled_start_passed:
        tags.append("SCHEDULED_START_PASSED")
    if g is not None and abs(g) >= cfg["bands_pp"]["HIGH_REVIEW"] and not (set(tags) - _CONTEXT_TAGS):
        tags.append("UNKNOWN")
    tags = [t for t in REASON_TAGS if t in tags]

    # ---- status (the slate can never satisfy the two ChatGPT explanations, so EXTREME stays DATA_WARNING)
    hard = bool(malformed) or identity == ID_FAILED or orientation == "FAILED"
    if malformed:
        status = DATA_WARNING
    elif g is None:
        status = NOT_APPLICABLE
    elif hard or band == EXTREME:
        status = DATA_WARNING
    elif band == HIGH_REVIEW:
        status = DATA_WARNING if identity != ID_VERIFIED else EXPLANATION_REQUIRED
    elif band == REVIEW:
        status = REVIEW_CONTEXT
    else:
        status = OK
    pre = extreme_preconditions(identity=identity, orientation=orientation, freshness=fresh, two_sided=two,
                                data_status=data["data_quality_status"], severe_asymmetry=data["severe_sample_asymmetry"],
                                external_status=ext_status, side_edge_after_fees=side_edge_after_fees)
    return {
        "discrepancy_version": cfg["version"],
        "model_probability_yes": _r(p_model), "kalshi_mid": _r(mid),
        "model_market_gap_pp": g, "abs_model_market_gap_pp": abs(g) if g is not None else None,
        "model_executable_gap_pp": executable_gap_pp(p_model, bid, ask) if not malformed else None,
        "discrepancy_band": band, "audit_bucket": audit_bucket(abs(g)) if g is not None else None,
        "discrepancy_sanity_status": status,
        "discrepancy_reason_tags": tags,
        "identity_check_status": identity, "identity_checks": checks,
        "ticker_orientation_status": orientation,
        "market_freshness_status": fresh,
        "external_confirmation_status": ext_status, "triangulation": tri,
        "data_quality_status": data["data_quality_status"],
        "severe_sample_asymmetry": data["severe_sample_asymmetry"],
        "malformed_probabilities": malformed,
        "extreme_preconditions": pre if band == EXTREME else None,
        "display_status": display_status(status, fresh, band),
        "evidence": {"quote_age_s": _r(quote_age_s, 0), **bev, "external_probability": _r(p_ext),
                     "external_age_s": _r(ext_age_s, 0), "model_uncertainty": _r(model_uncertainty),
                     "fair_envelope_width": _r(env_w), "model_probability_range_pp": spread_models,
                     "model_probabilities": {k: _r(v) for k, v in (model_probs or {}).items()},
                     "first_ball_source": first_ball_source, "scheduled_start_passed": scheduled_start_passed,
                     "model_side_edge_after_fees": _r(side_edge_after_fees),
                     **{f"data_{k}": v for k, v in (data.get("evidence") or {}).items()}},
    }


def extreme_preconditions(*, identity, orientation, freshness, two_sided, data_status, severe_asymmetry,
                          external_status, side_edge_after_fees=None, asymmetry_justification=None,
                          external_unavailable_reason=None, why_market=None, why_model=None,
                          chatgpt_side_edge_after_fees=None, entry_within_limit=None) -> dict:
    """The nine Part J conditions. Conditions 7-9 can only be met at decision time (they need ChatGPT's
    own explanations and price); on the slate they read False, which is why an EXTREME row stays
    DATA_WARNING there. Returns {condition: bool, ..., "all_met": bool, "failed": [...]}."""
    edge = chatgpt_side_edge_after_fees if chatgpt_side_edge_after_fees is not None else None
    c = {
        "identity_verified": identity == ID_VERIFIED,
        "ticker_orientation_verified": orientation in ("VERIFIED", "NOT_APPLICABLE"),
        "fresh_executable_price": freshness == FRESH and bool(two_sided),
        "adequate_data_quality": data_status == "ADEQUATE",
        "no_severe_asymmetry_or_justified": (not severe_asymmetry) or bool(_nonblank(asymmetry_justification)),
        "external_supports_or_documented_unavailable": external_status in EXTERNAL_SUPPORTS or (
            external_status in EXTERNAL_UNAVAILABLE and bool(_nonblank(external_unavailable_reason))),
        "explains_why_market_may_be_wrong": bool(_nonblank(why_market)),
        "explains_why_model_may_be_wrong": bool(_nonblank(why_model)),
        "price_clears_fees_and_execution": bool(edge is not None and edge > 0 and entry_within_limit is not False),
    }
    failed = [k for k in EXTREME_CONDITIONS if not c[k]]
    return {**c, "all_met": not failed, "failed": failed,
            "model_side_edge_after_fees": _r(side_edge_after_fees)}


def _nonblank(x):
    return x.strip() if isinstance(x, str) and x.strip() else None


def display_status(status: str, freshness: str, band: str) -> str:
    if status == DATA_WARNING:
        return "DATA_WARNING / PASS UNTIL RECHECKED"
    if status == EXPLANATION_REQUIRED:
        return "HIGH_REVIEW / EXPLAIN BEFORE ANY BET"
    if status == REVIEW_CONTEXT:
        return "REVIEW / DISCREPANCY CONTEXT"
    if status == ELIGIBLE:
        return "ELIGIBLE FOR HUMAN REVIEW (NOT AN AUTOMATIC BET)"
    if status == NOT_APPLICABLE:
        return "NO MODEL-MARKET COMPARISON"
    return "NORMAL"


def sanity_block_lines(r: dict, *, subject: str | None = None) -> list[str]:
    """The compact DISCREPANCY SANITY CHECK block rendered under a large gap on the slate."""
    d = r.get("discrepancy") or {}

    def pct(x):
        return f"{100 * x:.0f}%" if isinstance(x, (int, float)) else "--"
    g = d.get("model_market_gap_pp")
    ext = d.get("external_confirmation_status")
    dq = (d.get("evidence") or {}).get("data_grade")
    lines = ["```", f"DISCREPANCY SANITY CHECK  {r.get('ticker')}" + (f"  (YES = {subject})" if subject else ""),
             f"Model: {pct(d.get('model_probability_yes'))}",
             f"Kalshi: {pct(d.get('kalshi_mid'))}",
             f"Gap: {g:+.0f} pp" if isinstance(g, (int, float)) else "Gap: --",
             f"Band: {d.get('discrepancy_band')}",
             f"Identity: {(d.get('identity_check_status') or '').replace('IDENTITY_', '')}"
             f" (ticker orientation {d.get('ticker_orientation_status')})",
             f"Quote freshness: {d.get('market_freshness_status')}",
             f"External: {ext}",
             f"Data quality: {dq or '?'} ({d.get('data_quality_status')})",
             f"Reasons: {', '.join(d.get('discrepancy_reason_tags') or []) or '--'}",
             f"Status: {d.get('display_status')}"]
    pre = d.get("extreme_preconditions")
    if pre:
        lines.append("Unmet before human review: " + ", ".join(pre.get("failed") or []))
    lines.append("```")
    return lines


def parse_dt(x) -> datetime | None:
    if isinstance(x, datetime):
        return x
    if isinstance(x, str) and x:
        try:
            return datetime.fromisoformat(x.replace("Z", "+00:00"))
        except ValueError:
            return None
    return None
