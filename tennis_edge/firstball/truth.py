"""FirstBallTruth: the canonical, immutable answer to "when did play actually begin?".

Why this exists
---------------
Kalshi publishes a nominal `occurrence_datetime` and a `close_time`. Neither is a first-ball timestamp.
For ITF and Challenger the nominal time frequently falls AFTER the market closed, and on courts with a
rolling order of play a match scheduled for 14:00 can start at 16:40. Any research claim of the form
"this observation existed before the first ball" that rests on a scheduled time is unfalsifiable, so the
system needs a separate truth object with its own provenance and its own confidence.

The bracket is the object, not the point estimate
-------------------------------------------------
Except when a source states the start time outright, what a poller really learns is a BRACKET: the match
was not yet in progress at t0, and was in progress at t1, so the first ball fell in (t0, t1]. Every
FirstBallTruth therefore carries `lower_bound_utc` and `upper_bound_utc`, and classification uses the
bounds rather than the point estimate. An observation counts as strictly pregame only if it precedes the
EARLIEST possible first ball, and as post-start only if it follows the LATEST possible one. Anything
inside the bracket is AMBIGUOUS. That is what makes the claim survive a hostile audit: the uncertainty is
carried in the data instead of being rounded away.

Confidence
----------
A        an authoritative source states the actual start / first point outright (zero-width bracket)
B        a timestamped live-state transition proves play began within a narrow bracket
         (<= B_MAX_BRACKET_S seconds; the width is always recorded, so research can demand tighter)
C        indirect bound only (wide bracket, back-cast from score progression, exchange-only evidence)
UNKNOWN  insufficient evidence

Only A and B are eligible for strict pregame research. C and UNKNOWN are never silently promoted:
`classify()` treats C as START_UNKNOWN unless a caller explicitly opts in for exploratory work.

Immutability
------------
Rows are append-only and hash-chained (see store.py). Newly acquired evidence never edits an existing
row and never touches an observation's captured-at timestamp; it appends a new derivation with a higher
`derivation_version`, and the classification is RECOMPUTED from it. Sports truth may be recovered after
the fact. Prediction and quote timestamps may not be rewritten, ever.
"""
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass, asdict, field, replace
from datetime import datetime, timedelta, timezone

SCHEMA_VERSION = 1

CONFIDENCE_LEVELS = ("A", "B", "C", "UNKNOWN")
STRICT_ELIGIBLE = ("A", "B")

#: widest bracket that still counts as confidence B. Wider evidence is only an indirect bound (C).
B_MAX_BRACKET_S = 300
#: two credible point estimates further apart than this are a MATERIAL contradiction
MATERIAL_DISAGREEMENT_S = 300

CONTRADICTION_NONE = "NONE"
CONTRADICTION_MINOR = "MINOR"
CONTRADICTION_MATERIAL = "MATERIAL"

DERIVATION_EXPLICIT = "EXPLICIT_START_FIELD"
DERIVATION_FIRST_LIVE_EVENT = "FIRST_LIVE_EVENT"
DERIVATION_STATE_BRACKET = "STATE_TRANSITION_BRACKET"
DERIVATION_SCORE_BACKCAST = "SCORE_PROGRESSION_BACKCAST"
DERIVATION_EXCHANGE_BRACKET = "EXCHANGE_ACTIVITY_BRACKET"
DERIVATION_MULTI = "MULTI_SOURCE_INTERSECTION"
DERIVATION_NO_PLAY = "NO_PLAY_CONFIRMED"

#: source classes. Exchange evidence corroborates; it is never sports truth on its own.
AUTHORITY_OFFICIAL = "official"
AUTHORITY_SECONDARY = "secondary"
AUTHORITY_EXCHANGE = "exchange"


def _iso(dt: datetime | None) -> str | None:
    return dt.isoformat() if dt else None


def _hash_payload(obj) -> str:
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


@dataclass(frozen=True)
class FirstBallObservation:
    """One raw reading of one source at one moment. Never edited; it is the evidence, not the answer."""
    match_id: str
    source: str                             # catalogue candidate id, e.g. "espn_site_atp_scoreboard"
    authority: str                          # official | secondary | exchange
    observed_at_utc: datetime               # when WE read it (runner clock, UTC)
    state: str                              # PRE | IN | POST | NO_PLAY | UNKNOWN
    source_match_id: str = ""
    source_status: str = ""                 # the source's own status string, verbatim
    source_event_timestamp: datetime | None = None    # a time the SOURCE asserts (start, last update, ...)
    source_time_interpretation: str = ""    # how that timestamp was read: "epoch_s_utc", "iso_with_offset", ...
    explicit_start_utc: datetime | None = None        # only when the source states the actual start outright
    games_played: int | None = None
    payload_hash: str = ""
    raw_evidence_location: str = ""         # path on the tennis-data branch
    mapping_status: str = "MATCHED"         # MATCHED | WEAK -- how firmly this reading is bound to OUR match
    mapping_score: float = 1.0
    #: Sources that share an upstream data provider are NOT independent evidence. ESPN's atp and wta
    #: scoreboards return the same combined event during a Grand Slam, so counting them as two agreeing
    #: sources would manufacture confidence that does not exist. Defaults to the source id.
    independence_group: str = ""

    @property
    def group(self) -> str:
        return self.independence_group or self.source

    def to_dict(self):
        d = asdict(self)
        for k in ("observed_at_utc", "source_event_timestamp", "explicit_start_utc"):
            d[k] = _iso(d[k])
        return d


@dataclass(frozen=True)
class FirstBallTruth:
    """The derived answer for one match, at one derivation version."""
    match_id: str
    actual_first_ball_at_utc: datetime | None
    lower_bound_utc: datetime | None
    upper_bound_utc: datetime | None
    confidence: str
    derivation_method: str
    contradiction_status: str = CONTRADICTION_NONE
    no_play: bool = False
    observed_at_utc: datetime | None = None
    source: str = ""                        # winning/primary source id (or a "+"-joined list)
    source_match_id: str = ""
    source_status: str = ""
    source_event_timestamp: datetime | None = None
    source_time_interpretation: str = ""
    evidence_payload_hash: str = ""
    raw_evidence_location: str = ""
    contributing_sources: tuple = ()
    contradiction_detail: str = ""
    created_at: datetime | None = None
    derivation_version: int = 1
    schema_version: int = SCHEMA_VERSION

    def __post_init__(self):
        if self.confidence not in CONFIDENCE_LEVELS:
            raise ValueError(f"bad confidence {self.confidence!r}")
        if self.contradiction_status not in (CONTRADICTION_NONE, CONTRADICTION_MINOR, CONTRADICTION_MATERIAL):
            raise ValueError(f"bad contradiction_status {self.contradiction_status!r}")
        if self.lower_bound_utc and self.upper_bound_utc and self.lower_bound_utc > self.upper_bound_utc:
            raise ValueError("lower_bound after upper_bound")
        if self.confidence in STRICT_ELIGIBLE and not self.no_play:
            if self.lower_bound_utc is None or self.upper_bound_utc is None:
                raise ValueError("A/B confidence requires a bounded bracket")

    @property
    def bracket_seconds(self) -> float | None:
        if self.lower_bound_utc is None or self.upper_bound_utc is None:
            return None
        return (self.upper_bound_utc - self.lower_bound_utc).total_seconds()

    @property
    def strict_eligible(self) -> bool:
        """May this truth be used for strict pregame research?"""
        return (self.confidence in STRICT_ELIGIBLE
                and self.contradiction_status != CONTRADICTION_MATERIAL) or self.no_play

    def to_dict(self):
        d = asdict(self)
        for k in ("actual_first_ball_at_utc", "lower_bound_utc", "upper_bound_utc", "observed_at_utc",
                  "source_event_timestamp", "created_at"):
            d[k] = _iso(d[k])
        d["contributing_sources"] = list(self.contributing_sources)
        d["bracket_seconds"] = self.bracket_seconds
        return d

    @classmethod
    def from_dict(cls, d: dict) -> "FirstBallTruth":
        def p(k):
            v = d.get(k)
            return datetime.fromisoformat(v.replace("Z", "+00:00")) if isinstance(v, str) and v else None
        return cls(
            match_id=d["match_id"], actual_first_ball_at_utc=p("actual_first_ball_at_utc"),
            lower_bound_utc=p("lower_bound_utc"), upper_bound_utc=p("upper_bound_utc"),
            confidence=d["confidence"], derivation_method=d["derivation_method"],
            contradiction_status=d.get("contradiction_status", CONTRADICTION_NONE), no_play=bool(d.get("no_play")),
            observed_at_utc=p("observed_at_utc"), source=d.get("source", ""), source_match_id=d.get("source_match_id", ""),
            source_status=d.get("source_status", ""), source_event_timestamp=p("source_event_timestamp"),
            source_time_interpretation=d.get("source_time_interpretation", ""),
            evidence_payload_hash=d.get("evidence_payload_hash", ""), raw_evidence_location=d.get("raw_evidence_location", ""),
            contributing_sources=tuple(d.get("contributing_sources", ())), contradiction_detail=d.get("contradiction_detail", ""),
            created_at=p("created_at"), derivation_version=int(d.get("derivation_version", 1)),
            schema_version=int(d.get("schema_version", SCHEMA_VERSION)))


def unknown_truth(match_id: str, reason: str = "no evidence", **kw) -> FirstBallTruth:
    return FirstBallTruth(match_id=match_id, actual_first_ball_at_utc=None, lower_bound_utc=None,
                          upper_bound_utc=None, confidence="UNKNOWN", derivation_method=reason,
                          created_at=kw.pop("created_at", None) or datetime.now(timezone.utc), **kw)
