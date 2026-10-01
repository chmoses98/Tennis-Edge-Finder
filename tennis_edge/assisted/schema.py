"""Schemas, vocabularies and fixed classification rules of the assisted-handicapping lane.

Every constant here was fixed BEFORE the first assisted decision existed. Changing one after decisions
accumulate changes what the scorecard measures, so a change is a new schema version, never an edit.

Probability convention: every probability stored on a decision (`chatgpt_fair_probability`, every model
probability, `kalshi_mid`, `market_implied_probability`, `external_consensus`) is P(the ticker resolves
YES). Side-specific numbers (`side_entry_price`, `bet_up_to_price`, `bet_up_to_probability`) are for the
contract side the decision names. One convention for every family means a Brier score is always
(p_yes - outcome_yes)^2 and nobody has to remember which way a row was flipped.
"""
from __future__ import annotations

import re

#: v1: the launch schema (2026-09-30; no decision was ever recorded under it).
#: v2: adds the discrepancy-sanity group to decisions (model-market gap, band, identity / orientation /
#:     freshness / external / data-quality status and the Part J conditions); wagers, postmortems and
#:     evidence are unchanged apart from the version number. A v1 record keeps validating against v1.
ASSISTED_SCHEMA_VERSION = 2

DECISIONS = ("BET", "PASS", "WATCH")
SIDES = ("YES", "NO")
CONFIDENCE = ("LOW", "MEDIUM", "HIGH")

FACTOR_TAGS = (
    "SERVE_EDGE", "RETURN_EDGE", "SURFACE_FIT", "PLAYER_FORM", "FATIGUE", "TRAVEL", "SCHEDULING", "INJURY",
    "MATCHUP_STYLE", "LEFTY_RIGHTY", "TIEBREAK_PROFILE", "BREAK_POINT_PROFILE", "OPPONENT_QUALITY",
    "TOURNAMENT_CONTEXT", "MOTIVATION_CONTEXT", "EXTERNAL_MARKET_CONFIRMATION", "MARKET_OVERREACTION",
    "MARKET_UNDERREACTION", "MODEL_DISAGREEMENT", "PRICE_VALUE", "DERIVATIVE_VALUE", "LIQUIDITY", "OTHER",
)

MARKET_EXPRESSIONS = (
    "MATCH_WINNER", "SET_WINNER", "GAME_SPREAD", "TOTAL_GAMES", "TOTAL_SETS", "EXACT_SET_SCORE",
    "PLAYER_SET_HANDICAP", "OTHER_SUPPORTED_KALSHI_MARKET",
)
#: Kalshi family (tennis_edge.kalshi.families) -> the expression vocabulary above
FAMILY_EXPRESSION = {
    "MATCH_WINNER": "MATCH_WINNER", "SET_WINNER": "SET_WINNER", "GAME_SPREAD": "GAME_SPREAD",
    "TOTAL_GAMES": "TOTAL_GAMES", "TOTAL_SETS": "TOTAL_SETS", "EXACT_SET_SCORE": "EXACT_SET_SCORE",
    "SET_SPREAD": "PLAYER_SET_HANDICAP",
    "ANY_SET_WINNER": "OTHER_SUPPORTED_KALSHI_MARKET", "TIEBREAK_OCCURS": "OTHER_SUPPORTED_KALSHI_MARKET",
}
#: only MATCH-scope families can carry an assisted match decision (futures and novelties cannot)
SUPPORTED_FAMILIES = tuple(FAMILY_EXPRESSION)

AGREED_WITH_MODEL = "AGREED_WITH_MODEL"
OVERRULED_MODEL = "OVERRULED_MODEL"
MODEL_NEUTRAL = "MODEL_NEUTRAL"
MODEL_AND_CHATGPT_BOTH_PASS = "MODEL_AND_CHATGPT_BOTH_PASS"
AGREEMENT_STATES = (AGREED_WITH_MODEL, OVERRULED_MODEL, MODEL_NEUTRAL, MODEL_AND_CHATGPT_BOTH_PASS)

#: a side is "preferred" when its fee-adjusted executable edge is strictly positive (price the side can
#: actually be bought at, taker fee included). Fixed before any decision; the pass-quality question
#: ("did the model help us PASS bad apparent edges?") is defined on exactly these rows.
PREFERENCE_MIN_EDGE = 0.0
#: |chatgpt_fair_probability - kalshi_mid| at or above this is a MATERIAL disagreement with Kalshi
MATERIAL_DISAGREEMENT = 0.05

LOSS_ATTRIBUTION = ("PROCESS", "VARIANCE", "BOTH", "UNCLEAR", "NOT_A_LOSS")
WAGER_STATUS = ("FILLED", "PARTIAL_FILL", "CANCELLED", "VOIDED_BY_EXCHANGE")
WAGER_SOURCES = ("MANUAL_KALSHI_UI", "MANUAL_KALSHI_API", "KALSHI_ROUTER", "OTHER")

LEVEL_BUCKETS = ("ATP", "WTA", "CHALLENGER", "WTA125", "ITF", "DOUBLES", "OTHER")
SURFACE_BUCKETS = ("HARD", "CLAY", "GRASS", "INDOOR", "OTHER")

#: a decision may be recorded at most this long after it was made, and never before the track started:
#: the lane is prospective, and a decision written up hours later is a reconstruction.
MAX_RECORDING_LAG_S = 3 * 3600
MAX_CLOCK_SKEW_S = 120

# ---------------------------------------------------------------------------------------------- fields
#: The EXACT decision schema, in record order. Groups are documentation; every key is always present.
DECISION_SCHEMA = {
    "identity": ["decision_id", "schema_version", "track", "created_at", "recorded_at", "recorder_version",
                 "code_sha", "slate_id", "slate_built_at", "input_payload_sha256"],
    "match": ["physical_match_id", "event_id", "match_code", "ticker", "series", "tour", "level", "level_bucket",
              "competition", "surface", "surface_bucket", "players", "market_family", "market_description",
              "side", "strike", "scheduled_start", "first_ball_status_at_decision", "first_ball_source_coverage",
              "scheduled_start_passed_at_decision"],
    "model_context": ["gen1_probability", "gen2_probability", "model4_probability_if_applicable",
                      "fair_v1_probability", "model_probability_yes", "model_probability_source", "selector_state",
                      "model_uncertainty", "serve_evidence_player_a", "serve_evidence_player_b", "rating_state",
                      "surface_adjustment", "recent_form_inputs", "additional_model_inputs", "model_context_source"],
    "market_context": ["kalshi_bid", "kalshi_ask", "kalshi_mid", "kalshi_spread", "displayed_size", "fee",
                       "market_implied_probability", "side_entry_price", "side_fee", "market_quote_source",
                       "market_quote_observed_at", "market_quote_age_seconds", "repo_market_at_decision"],
    "external_context": ["bovada_probability_if_available", "smarkets_probability_if_available",
                         "external_consensus", "triangulation_state", "external_freshness",
                         "external_context_source"],
    "handicapping": ["chatgpt_fair_probability", "chatgpt_confidence", "chatgpt_thesis", "key_supporting_factors",
                     "key_opposing_factors", "factor_tags", "model_agreement_state", "model_preferred_side",
                     "chatgpt_preferred_side", "model_side_edges", "material_disagreement_with_kalshi",
                     "market_disagreement_reason", "why_market_may_be_wrong", "why_model_may_be_wrong",
                     "pass_reason_if_pass"],
    "discrepancy_sanity": ["model_market_gap_pp", "discrepancy_band", "discrepancy_sanity_status",
                           "discrepancy_reason_tags", "identity_check_status", "ticker_orientation_status",
                           "market_freshness_status", "external_confirmation_status", "data_quality_status",
                           "discrepancy_conditions", "discrepancy_explanation", "sample_asymmetry_justification",
                           "external_unavailable_reason", "discrepancy_context_source"],
    "expression": ["primary_match_thesis", "available_expressions", "chosen_expression",
                   "why_chosen_expression_best_matches_thesis"],
    "decision": ["decision", "recommended_price", "bet_up_to_probability", "bet_up_to_price",
                 "stake_units_if_bet", "actual_wagered"],
    "authority": ["authority", "autonomous_real_money_authority", "automated_execution", "warnings"],
}
DECISION_FIELDS = [k for g in DECISION_SCHEMA.values() for k in g]
DECISION_FIELDS_BY_VERSION = {1: [k for g, ks in DECISION_SCHEMA.items() if g != "discrepancy_sanity" for k in ks],
                              2: DECISION_FIELDS}

#: Once written these can never change. The whole record is fingerprinted; this list is what the
#: integrity check names when a fingerprint breaks (Part 11).
IMMUTABLE_DECISION_FIELDS = (
    "decision_id", "created_at", "ticker", "side", "decision", "chatgpt_fair_probability", "chatgpt_confidence",
    "chatgpt_thesis", "key_supporting_factors", "key_opposing_factors", "factor_tags", "primary_match_thesis",
    "chosen_expression", "why_chosen_expression_best_matches_thesis", "bet_up_to_probability", "bet_up_to_price",
    "recommended_price", "stake_units_if_bet", "kalshi_bid", "kalshi_ask", "kalshi_mid", "side_entry_price",
    "market_implied_probability", "model_agreement_state", "model_preferred_side", "chatgpt_preferred_side",
    "model_market_gap_pp", "discrepancy_band", "discrepancy_sanity_status", "discrepancy_explanation",
)

WAGER_FIELDS = ["wager_id", "decision_id", "schema_version", "recorded_at", "placed_at", "ticker", "side",
                "entry_price", "contracts", "stake_dollars", "fees", "source", "status", "external_order_id",
                "decision_was_bet", "placed_after_first_ball", "first_ball_status_at_placement",
                "input_payload_sha256", "authority", "warnings"]

SETTLEMENT_FIELDS = ["settlement_id", "row_kind", "decision_id", "wager_id", "revision", "settled_at",
                     "settlement_result", "settlement_value_yes", "side", "side_won", "entry_price", "contracts",
                     "gross_pnl", "fees", "net_pnl", "roi", "strict_close", "strict_executable_clv",
                     "midpoint_clv", "clv_timing_class", "clv_exclusion_reason", "first_ball_confidence",
                     "first_ball_lower_utc", "post_start_violation", "settlement_source", "settled_by"]

POSTMORTEM_FIELDS = ["postmortem_id", "decision_id", "schema_version", "recorded_at", "result",
                     "what_thesis_got_right", "what_thesis_got_wrong", "whether_loss_was_process_or_variance",
                     "data_that_would_have_helped", "potential_research_question", "use_restriction",
                     "input_payload_sha256"]

EVIDENCE_FIELDS = ["evidence_id", "decision_id", "schema_version", "recorded_at", "discovered_at",
                   "evidence", "source", "bears_on", "input_payload_sha256"]

POSTMORTEM_USE_RESTRICTION = ("HYPOTHESIS_GENERATION_ONLY: never modifies model weights, thresholds, selectors "
                              "or rules, and never becomes a rule without its own pre-registered, prospective test")

_ID_RE = re.compile(r"^[A-Z]{2}-\d{8}-[0-9a-f]{12}$")
_TICKER_RE = re.compile(r"^KX[A-Z0-9]+-[A-Z0-9]+(-[A-Z0-9.]+)*$")
_PHYS_RE = re.compile(r"^(ATP|WTA|MIXED|ANY):[^:]+:[^:]+:\d{4}-\d{2}-\d{2}$")


class AssistedValidationError(ValueError):
    """A submission the lane refuses. `code` is stable and machine-readable."""

    def __init__(self, code: str, message: str):
        super().__init__(f"{code}: {message}")
        self.code = code


def valid_record_id(x: str, prefix: str) -> bool:
    return isinstance(x, str) and x.startswith(prefix + "-") and bool(_ID_RE.match(x))


def valid_ticker(x) -> bool:
    return isinstance(x, str) and bool(_TICKER_RE.match(x))


def valid_physical_match_id(x) -> bool:
    return isinstance(x, str) and bool(_PHYS_RE.match(x))


def match_code_of(ticker_or_event: str) -> str:
    """The date+players code every series of one physical match shares (see firstball.started)."""
    parts = (ticker_or_event or "").split("-")
    return parts[1] if len(parts) > 1 else ""


def series_of(ticker: str) -> str:
    return (ticker or "").split("-")[0]


# ---------------------------------------------------------------------------------------------- buckets
def level_bucket(series: str, level: str | None = None, discipline: str | None = None) -> str:
    """ATP / WTA / CHALLENGER / WTA125 / ITF / DOUBLES / OTHER for scorecard slicing."""
    from tennis_edge.kalshi.families import SERIES
    fam = SERIES.get(series)
    disc = discipline or (fam[3] if fam else "singles")
    if disc in ("doubles", "mixed"):
        return "DOUBLES"
    lv = (level or "").upper()
    if lv == "ITF" or series in ("KXITFMATCH", "KXITFWMATCH"):
        return "ITF"
    if lv == "WTA_125" or series == "KXWTACHALLENGERMATCH":
        return "WTA125"
    if lv == "CHALLENGER" or series in ("KXATPCHALLENGERMATCH", "KXCHALLENGERMATCH"):
        return "CHALLENGER"
    tour = fam[1] if fam else ""
    if lv in ("OTHER", "TEAM", "EXHIBITION") or (fam and fam[2] in ("TEAM", "EXHIBITION")):
        return "OTHER"
    if tour in ("ATP", "WTA"):
        return tour
    return "OTHER"


def surface_bucket(surface: str | None, competition: str | None = None) -> str:
    s, c = (surface or "").lower(), (competition or "").lower()
    if "indoor" in s or "indoor" in c or "(i)" in c:
        return "INDOOR"
    if s.startswith("hard"):
        return "HARD"
    if s.startswith("clay"):
        return "CLAY"
    if s.startswith("grass"):
        return "GRASS"
    return "OTHER"


def expression_of_family(family: str) -> str | None:
    return FAMILY_EXPRESSION.get(family)


# ---------------------------------------------------------------------------------------------- prices
def side_prices(side: str, yes_bid, yes_ask) -> tuple[float | None, float | None]:
    """(bid, ask) of the named contract side from the YES book (NO bid = 1 - YES ask)."""
    if yes_bid is None or yes_ask is None:
        return None, None
    return (yes_bid, yes_ask) if side == "YES" else (1.0 - yes_ask, 1.0 - yes_bid)


def side_edges(p_yes: float | None, yes_bid, yes_ask) -> dict:
    """Fee-adjusted executable edge of buying each side at its ask, for a YES-probability p_yes."""
    from tennis_edge.pricing.fees import taker_fee
    out = {"YES": None, "NO": None}
    if p_yes is None or yes_bid is None or yes_ask is None or not (0 < yes_bid <= yes_ask < 1):
        return out
    for side, p in (("YES", p_yes), ("NO", 1.0 - p_yes)):
        _bid, ask = side_prices(side, yes_bid, yes_ask)
        out[side] = round(p - ask - taker_fee(ask, 1.0), 6)
    return out


def preferred_side(p_yes: float | None, yes_bid, yes_ask) -> str:
    """YES / NO when that side's fee-adjusted executable edge is > PREFERENCE_MIN_EDGE, NEUTRAL when
    neither side clears it, NONE when there is no probability or no two-sided quote to compare with."""
    e = side_edges(p_yes, yes_bid, yes_ask)
    if e["YES"] is None:
        return "NONE"
    if e["YES"] > PREFERENCE_MIN_EDGE:
        return "YES"
    if e["NO"] > PREFERENCE_MIN_EDGE:
        return "NO"
    return "NEUTRAL"


def classify_agreement(decision: str, model_side: str, chatgpt_side: str) -> str:
    """Part 4. BET: agreed if ChatGPT bought the side the model prefers, overruled if it bought the other
    side, model-neutral if the model had no preference. PASS/WATCH: both-pass if the model had no
    preference either, overruled if the model preferred a side ChatGPT declined to bet."""
    model_has_view = model_side in ("YES", "NO")
    if decision == "BET":
        if not model_has_view:
            return MODEL_NEUTRAL
        return AGREED_WITH_MODEL if chatgpt_side == model_side else OVERRULED_MODEL
    return OVERRULED_MODEL if model_has_view else MODEL_AND_CHATGPT_BOTH_PASS
