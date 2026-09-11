"""Timing classification: does an observation provably precede the first ball?

Four classes, and only four:

  STRICT_PREGAME   the observation was captured strictly before the EARLIEST possible first ball
  POST_START       the observation was captured at or after the LATEST possible first ball
  AMBIGUOUS        the observation falls inside the first-ball bracket, or credible sources contradict
  START_UNKNOWN    there is no trustworthy first-ball evidence for this match

Deliberate design choices
-------------------------
* `classify()` takes a FirstBallTruth OBJECT, never a bare datetime. That is what structurally prevents
  the failure this whole wave exists to fix: you cannot pass a scheduled start, a Kalshi
  occurrence_datetime or a market close time into it by accident, because none of them is a truth object.
* The BOUNDS decide, not the point estimate. Strict pregame requires captured_at < lower_bound; post
  start requires captured_at >= upper_bound. An observation one second after the first ball is
  POST_START; an observation exactly AT the first ball is POST_START too, never pregame.
* Confidence C is an indirect bound only. It is NOT silently promoted: by default it classifies as
  START_UNKNOWN. `allow_indirect=True` exists for exploratory work and is never used by strict research.
* A MATERIAL contradiction is AMBIGUOUS, not START_UNKNOWN. The two states mean different things: one
  says the sources fight, the other says nobody looked.
* Classification is DERIVED. Re-running it against a better truth changes the label and nothing else;
  the observation's captured-at timestamp is never touched.
"""
from __future__ import annotations

from dataclasses import dataclass, asdict
from datetime import datetime, timezone

from .truth import FirstBallTruth, CONTRADICTION_MATERIAL, STRICT_ELIGIBLE

CLASSIFIER_VERSION = 1

STRICT_PREGAME = "STRICT_PREGAME"
POST_START = "POST_START"
AMBIGUOUS = "AMBIGUOUS"
START_UNKNOWN = "START_UNKNOWN"
TIMING_CLASSES = (STRICT_PREGAME, POST_START, AMBIGUOUS, START_UNKNOWN)

BASIS_EXPLICIT = "ACTUAL_FIRST_BALL"
BASIS_BRACKET = "FIRST_BALL_BRACKET"
BASIS_NO_PLAY = "NO_PLAY"
BASIS_CONTRADICTION = "MATERIAL_CONTRADICTION"
BASIS_NO_TRUTH = "NO_FIRST_BALL_TRUTH"
BASIS_INDIRECT = "INDIRECT_BOUND_ONLY"


@dataclass(frozen=True)
class TimingClassification:
    timing_class: str
    basis: str
    truth_confidence: str
    derivation_version: int
    classifier_version: int = CLASSIFIER_VERSION
    seconds_before_lower_bound: float | None = None
    seconds_after_upper_bound: float | None = None
    bracket_seconds: float | None = None
    classified_at_utc: str = ""

    @property
    def strict(self) -> bool:
        return self.timing_class == STRICT_PREGAME

    def to_dict(self):
        return asdict(self)


def classify(captured_at_utc: datetime, truth: FirstBallTruth | None, *, allow_indirect: bool = False,
             now: datetime | None = None) -> TimingClassification:
    now_s = (now or datetime.now(timezone.utc)).isoformat()
    if truth is None:
        return TimingClassification(START_UNKNOWN, BASIS_NO_TRUTH, "UNKNOWN", 0, classified_at_utc=now_s)
    common = dict(truth_confidence=truth.confidence, derivation_version=truth.derivation_version,
                  bracket_seconds=truth.bracket_seconds, classified_at_utc=now_s)
    if truth.contradiction_status == CONTRADICTION_MATERIAL:
        return TimingClassification(AMBIGUOUS, BASIS_CONTRADICTION, **common)
    if truth.no_play:
        # No ball was ever struck, so nothing can be post-start. Such matches are excluded from CLV by
        # SportsTruth/ExchangeTruth (walkover, scalar settlement), not by pretending the start is unknown.
        return TimingClassification(STRICT_PREGAME, BASIS_NO_PLAY, **common)
    usable = truth.confidence in STRICT_ELIGIBLE or (allow_indirect and truth.confidence == "C")
    if not usable or truth.lower_bound_utc is None or truth.upper_bound_utc is None:
        basis = BASIS_INDIRECT if truth.confidence == "C" else BASIS_NO_TRUTH
        return TimingClassification(START_UNKNOWN, basis, **common)
    basis = BASIS_EXPLICIT if truth.bracket_seconds == 0 else BASIS_BRACKET
    if captured_at_utc < truth.lower_bound_utc:
        return TimingClassification(STRICT_PREGAME, basis,
                                    seconds_before_lower_bound=(truth.lower_bound_utc - captured_at_utc).total_seconds(),
                                    **common)
    if captured_at_utc >= truth.upper_bound_utc:
        return TimingClassification(POST_START, basis,
                                    seconds_after_upper_bound=(captured_at_utc - truth.upper_bound_utc).total_seconds(),
                                    **common)
    return TimingClassification(AMBIGUOUS, basis, **common)
