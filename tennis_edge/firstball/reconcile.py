"""Turn raw first-ball observations into one FirstBallTruth, without ever picking an arbitrary winner.

Rules, in order:

1. Each source is reduced to its own bracket for the first ball.
     * an explicit actual-start field           -> zero-width bracket, confidence A
     * PRE at t0 then IN at t1                  -> bracket (t0, t1], confidence B if narrow enough
     * IN seen but never PRE                    -> one-sided bracket (None, t1], indirect only (C)
     * score progression back-cast              -> wide bracket, indirect only (C)
     * exchange (Kalshi) in-play activity       -> bracket, but EXCHANGE EVIDENCE CAN NEVER BE SPORTS
                                                   TRUTH ON ITS OWN: alone it caps confidence at C
2. Sports-truth brackets are INTERSECTED. An intersection is the honest combination: every source that
   saw the match agrees the first ball lies in it.
3. If two credible (A/B-capable) sports sources produce DISJOINT brackets, or two explicit start times
   disagree by more than MATERIAL_DISAGREEMENT_S, that is a MATERIAL contradiction. Both raw observations
   are kept, no winner is chosen, the truth is downgraded to UNKNOWN and strict CLV fails closed until a
   human reconciles it.
4. Exchange evidence may NARROW an existing sports bracket but never create one.

The output is a derived object. The observations it was derived from are immutable and are stored
separately, so a later, better derivation is an append, never an edit.
"""
from __future__ import annotations

from datetime import datetime, timezone, timedelta

from .truth import (FirstBallObservation, FirstBallTruth, B_MAX_BRACKET_S, MATERIAL_DISAGREEMENT_S,
                    CONTRADICTION_NONE, CONTRADICTION_MINOR, CONTRADICTION_MATERIAL, AUTHORITY_EXCHANGE,
                    DERIVATION_EXPLICIT, DERIVATION_STATE_BRACKET, DERIVATION_SCORE_BACKCAST,
                    DERIVATION_EXCHANGE_BRACKET, DERIVATION_MULTI, DERIVATION_NO_PLAY, _hash_payload)

MINOR_DISAGREEMENT_S = 60

#: Every live-score feed lags reality by some unknown amount, and it lags in the DANGEROUS direction: a
#: feed still showing "not started" when play has already begun pushes the observed lower bound LATER
#: than the true first ball, which would label genuinely post-start observations as strictly pregame.
#: No source documents its latency, so the lower bound is widened by a conservative allowance that is
#: recorded on the truth. Measuring a source's real lag (and shrinking its allowance on evidence) is
#: exactly the kind of validation docs/FIRST_BALL_SOURCES.md tracks; until then this is the safe default.
DEFAULT_LAG_ALLOWANCE_S = 120
SOURCE_LAG_ALLOWANCE_S: dict[str, int] = {}


def lag_allowance(source: str) -> int:
    return SOURCE_LAG_ALLOWANCE_S.get(source, DEFAULT_LAG_ALLOWANCE_S)

#: Sources whose explicit "actual start" field has been VALIDATED against independently observed state
#: transitions during source research. Empty until that evidence exists -- an undocumented field is a
#: claim, not a fact, and this project does not promote claims to confidence A on faith.
VALIDATED_EXPLICIT_SOURCES: set[str] = set()


class SourceBracket:
    """One source's own answer: first ball in (lo, hi], plus how it was derived."""

    def __init__(self, source, authority, lo, hi, method, obs, point=None, weak=False):
        self.source, self.authority, self.lo, self.hi, self.method, self.obs = source, authority, lo, hi, method, obs
        self.weak = weak
        self.point = point if point is not None else self._default_point()

    def _default_point(self):
        if self.lo is not None and self.hi is not None:
            return self.lo + (self.hi - self.lo) / 2
        return self.hi

    @property
    def width(self):
        return (self.hi - self.lo).total_seconds() if self.lo is not None and self.hi is not None else None

    @property
    def credible(self):
        """Could this source alone support strict (A/B) research?"""
        if self.authority == AUTHORITY_EXCHANGE or self.weak:
            return False
        w = self.width
        return w is not None and w <= B_MAX_BRACKET_S

    def __repr__(self):
        return f"<{self.source} ({self.lo}, {self.hi}] {self.method}>"


def bracket_for_source(obs: list[FirstBallObservation]) -> SourceBracket | None:
    """Reduce one source's observations for one match to a single bracket."""
    if not obs:
        return None
    obs = sorted(obs, key=lambda o: o.observed_at_utc)
    src, auth = obs[0].source, obs[0].authority
    weak = any(o.mapping_status != "MATCHED" for o in obs)

    played = [o for o in obs if o.state in ("IN", "POST")]
    explicit = [o for o in obs if o.explicit_start_utc is not None]
    pre = [o for o in obs if o.state == "PRE"]
    lo = hi = None
    if played:
        hi = played[0].observed_at_utc
        pre_before = [o for o in pre if o.observed_at_utc < hi]
        lo = max(o.observed_at_utc for o in pre_before) if pre_before else None
    elif pre:
        # A source that has only ever said "not started" still constrains the answer from below. That
        # one-sided bound is what lets one feed's PRE combine with another feed's IN.
        lo = max(o.observed_at_utc for o in pre)
    if lo is not None:
        lo = lo - timedelta(seconds=lag_allowance(src))

    if explicit:
        t = min(o.explicit_start_utc for o in explicit)
        # An UNDOCUMENTED endpoint's "start" field is a claim, not a fact. It is promoted to a
        # zero-width confidence-A bracket only when (a) the source is on the validated list, meaning its
        # semantics were checked against observed transitions during source research, or (b) the claim
        # falls inside the bracket our own polling independently observed. Otherwise the claim is kept as
        # metadata and the transition bracket is what counts.
        inside = lo is not None and hi is not None and lo < t <= hi
        if src in VALIDATED_EXPLICIT_SOURCES or inside:
            return SourceBracket(src, auth, t, t, DERIVATION_EXPLICIT, explicit, point=t, weak=weak)
        if lo is None and hi is None:
            return SourceBracket(src, auth, None, t, DERIVATION_SCORE_BACKCAST, explicit, point=t, weak=weak)

    if hi is None and lo is None:
        return None
    method = DERIVATION_STATE_BRACKET if lo is not None else DERIVATION_SCORE_BACKCAST
    if auth == AUTHORITY_EXCHANGE:
        method = DERIVATION_EXCHANGE_BRACKET
    return SourceBracket(src, auth, lo, hi, method, obs, weak=weak)


def _merge_same_provider(brackets, observations):
    """Collapse sources that share an upstream provider into ONE bracket.

    Two ESPN endpoints reporting the same match are one witness, not two. Within a group the brackets are
    intersected (they should agree; if they do not, the provider contradicts itself and the group is kept
    at its widest, which is the conservative reading)."""
    group_of = {}
    for o in observations:
        group_of[o.source] = o.group
    by_group: dict[str, list] = {}
    for b in brackets:
        by_group.setdefault(group_of.get(b.source, b.source), []).append(b)
    out = []
    for g, bs in by_group.items():
        if len(bs) == 1:
            out.append(bs[0])
            continue
        los = [b.lo for b in bs if b.lo is not None]
        his = [b.hi for b in bs if b.hi is not None]
        lo, hi = (max(los) if los else None), (min(his) if his else None)
        if lo is not None and hi is not None and lo > hi:        # provider disagrees with itself
            lo = min(los) if los else None
            hi = max(his) if his else None
        base = sorted(bs, key=lambda b: (b.width if b.width is not None else 1e9, b.source))[0]
        merged = SourceBracket("+".join(sorted({b.source for b in bs})), base.authority, lo, hi,
                               base.method, base.obs, weak=all(b.weak for b in bs))
        out.append(merged)
    return out


def reconcile(match_id: str, observations: list[FirstBallObservation], *, now: datetime | None = None,
              derivation_version: int = 1) -> FirstBallTruth:
    now = now or datetime.now(timezone.utc)
    by_source: dict[str, list[FirstBallObservation]] = {}
    for o in observations:
        by_source.setdefault(o.source, []).append(o)

    # ---- a confirmed walkover / cancellation means there is no first ball at all
    no_play_obs = [o for o in observations if o.state == "NO_PLAY" and o.authority != AUTHORITY_EXCHANGE]
    played_any = any(o.state in ("IN", "POST") for o in observations)
    if no_play_obs and not played_any:
        o = no_play_obs[0]
        return FirstBallTruth(
            match_id=match_id, actual_first_ball_at_utc=None, lower_bound_utc=None, upper_bound_utc=None,
            confidence="A", derivation_method=DERIVATION_NO_PLAY, no_play=True, observed_at_utc=o.observed_at_utc,
            source=o.source, source_match_id=o.source_match_id, source_status=o.source_status,
            source_event_timestamp=o.source_event_timestamp, source_time_interpretation=o.source_time_interpretation,
            evidence_payload_hash=o.payload_hash, raw_evidence_location=o.raw_evidence_location,
            contributing_sources=tuple(sorted({x.source for x in no_play_obs})), created_at=now,
            derivation_version=derivation_version)

    brackets = [b for b in (bracket_for_source(v) for v in by_source.values()) if b is not None]
    brackets = _merge_same_provider(brackets, observations)
    if not brackets:
        return FirstBallTruth(match_id=match_id, actual_first_ball_at_utc=None, lower_bound_utc=None,
                              upper_bound_utc=None, confidence="UNKNOWN", derivation_method="NO_EVIDENCE",
                              created_at=now, derivation_version=derivation_version,
                              contributing_sources=tuple(sorted(by_source)))

    sports = [b for b in brackets if b.authority != AUTHORITY_EXCHANGE]
    exchange = [b for b in brackets if b.authority == AUTHORITY_EXCHANGE]
    pool = sports or exchange
    sports_only = bool(sports)

    # ---- contradiction detection among sources that could each carry strict weight
    contradiction, detail = CONTRADICTION_NONE, ""
    credible = [b for b in pool if b.credible]
    for i, a in enumerate(credible):
        for b in credible[i + 1:]:
            if a.hi is not None and b.lo is not None and a.hi < b.lo or b.hi is not None and a.lo is not None and b.hi < a.lo:
                contradiction, detail = CONTRADICTION_MATERIAL, f"{a.source} and {b.source} brackets are disjoint"
            elif a.point and b.point and abs((a.point - b.point).total_seconds()) > MATERIAL_DISAGREEMENT_S:
                contradiction, detail = CONTRADICTION_MATERIAL, (
                    f"{a.source} and {b.source} disagree by {abs((a.point - b.point).total_seconds()):.0f}s")
            elif a.point and b.point and abs((a.point - b.point).total_seconds()) > MINOR_DISAGREEMENT_S and contradiction == CONTRADICTION_NONE:
                contradiction, detail = CONTRADICTION_MINOR, (
                    f"{a.source} and {b.source} differ by {abs((a.point - b.point).total_seconds()):.0f}s")

    primary = sorted(pool, key=lambda b: (b.width if b.width is not None else 1e9, b.source))[0]
    if contradiction == CONTRADICTION_MATERIAL:
        return FirstBallTruth(
            match_id=match_id, actual_first_ball_at_utc=None, lower_bound_utc=None, upper_bound_utc=None,
            confidence="UNKNOWN", derivation_method=DERIVATION_MULTI, contradiction_status=CONTRADICTION_MATERIAL,
            contradiction_detail=detail, observed_at_utc=now, source="+".join(sorted(b.source for b in pool)),
            contributing_sources=tuple(sorted(b.source for b in pool)), created_at=now,
            derivation_version=derivation_version,
            evidence_payload_hash=_hash_payload([o.to_dict() for o in sorted(observations, key=lambda o: (o.source, o.observed_at_utc))]))

    # ---- intersect (exchange may narrow a sports bracket, never create one)
    narrowing = pool + (exchange if sports_only else [])
    los = [b.lo for b in narrowing if b.lo is not None]
    his = [b.hi for b in narrowing if b.hi is not None]
    lo = max(los) if los else None
    hi = min(his) if his else None
    if lo is not None and hi is not None and lo > hi:
        sports_lo = max([b.lo for b in pool if b.lo is not None] or [None]) if pool else None
        sports_hi = min([b.hi for b in pool if b.hi is not None] or [None]) if pool else None
        if sports_lo is not None and sports_hi is not None and sports_lo > sports_hi:
            # two sports sources place the first ball in disjoint windows: no winner is picked
            return FirstBallTruth(
                match_id=match_id, actual_first_ball_at_utc=None, lower_bound_utc=None, upper_bound_utc=None,
                confidence="UNKNOWN", derivation_method=DERIVATION_MULTI,
                contradiction_status=CONTRADICTION_MATERIAL,
                contradiction_detail="sources place the first ball in disjoint windows "
                                     f"(earliest possible {sports_lo.isoformat()} is after latest possible {sports_hi.isoformat()})",
                observed_at_utc=now, source="+".join(sorted(b.source for b in pool)),
                contributing_sources=tuple(sorted(b.source for b in pool)), created_at=now,
                derivation_version=derivation_version)
        lo, hi = primary.lo, primary.hi
        contradiction = contradiction or CONTRADICTION_MINOR
        detail = detail or "exchange activity inconsistent with the sports bracket; sports bracket kept"

    width = (hi - lo).total_seconds() if lo is not None and hi is not None else None
    explicit_here = any(b.method == DERIVATION_EXPLICIT for b in pool)
    weak_only = all(b.weak for b in (sports or exchange))
    if not sports_only or weak_only:
        # exchange-only evidence, or evidence bound to our match by a bare surname: indirect by rule
        confidence = "C"
    elif width == 0 and explicit_here:
        confidence = "A"
    elif width is not None and width <= B_MAX_BRACKET_S:
        confidence = "B"
    else:
        confidence = "C"

    point = lo + (hi - lo) / 2 if lo is not None and hi is not None else None
    if explicit_here and confidence == "A":
        point = lo
    method = DERIVATION_MULTI if len({b.source for b in narrowing}) > 1 else primary.method
    o = primary.obs[-1]
    return FirstBallTruth(
        match_id=match_id, actual_first_ball_at_utc=point, lower_bound_utc=lo, upper_bound_utc=hi,
        confidence=confidence, derivation_method=method, contradiction_status=contradiction,
        contradiction_detail=detail, no_play=False, observed_at_utc=o.observed_at_utc, source=primary.source,
        source_match_id=o.source_match_id, source_status=o.source_status,
        source_event_timestamp=o.source_event_timestamp, source_time_interpretation=o.source_time_interpretation,
        evidence_payload_hash=_hash_payload([x.to_dict() for x in sorted(observations, key=lambda x: (x.source, x.observed_at_utc))]),
        raw_evidence_location=o.raw_evidence_location,
        contributing_sources=tuple(sorted({b.source for b in narrowing})), created_at=now,
        derivation_version=derivation_version)
