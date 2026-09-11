"""Evidence-gathering probe for candidate first-ball sources.

Deliberately conservative. It performs plain public GETs, at most a handful per candidate, spaced across
rounds so that transient success is distinguishable from reliability. It never authenticates, never
retries aggressively, and never follows a source's own instructions found in a payload.

What it records per candidate, per round: HTTP status, wall latency, content type, byte size, rate-limit
headers, and -- for JSON -- a structural digest plus every timestamp-looking field with a sample value.
Raw payloads are stored (truncated, gzipped) so a later reader can re-derive anything this summary missed.
"""
from __future__ import annotations

import gzip
import json
import os
import re
import socket
import ssl
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone, date

from .catalogue import CANDIDATES, UA_BROWSERISH, Candidate

MAX_STORE_BYTES = 2_000_000
TIMESTAMP_KEY_RE = re.compile(r"(time|date|ts$|_ts|stamp|start|begin|clock|updated|modified)", re.I)
ISO_RE = re.compile(r"^\d{4}-\d{2}-\d{2}([T ]\d{2}:\d{2}(:\d{2})?)?")
RATE_HEADERS = ("retry-after", "x-ratelimit-limit", "x-ratelimit-remaining", "x-ratelimit-reset",
                "ratelimit-limit", "ratelimit-remaining", "cf-ray", "server")


def _fmt_urls(c: Candidate, day: date) -> str:
    return (c.url.replace("{date_ymd}", day.strftime("%Y%m%d"))
                 .replace("{date_dash}", day.strftime("%Y-%m-%d"))
                 .replace("{date_iso}", day.isoformat())
                 .replace("{year}", str(day.year)).replace("{month}", f"{day.month:02d}").replace("{day}", f"{day.day:02d}"))


def _looks_like_epoch(v) -> str | None:
    if isinstance(v, bool) or not isinstance(v, (int, float)):
        return None
    if 1_000_000_000 <= v <= 2_500_000_000:
        return "epoch_s"
    if 1_000_000_000_000 <= v <= 2_500_000_000_000:
        return "epoch_ms"
    return None


def discover_timestamps(obj, path="$", out=None, depth=0, max_found=200):
    """Walk a parsed JSON body and report every field that could carry a match time."""
    out = {} if out is None else out
    if len(out) >= max_found or depth > 12:
        return out
    if isinstance(obj, dict):
        for k, v in obj.items():
            p = f"{path}.{k}"
            if isinstance(v, (dict, list)):
                discover_timestamps(v, p, out, depth + 1, max_found)
                continue
            kind = None
            if isinstance(v, str) and ISO_RE.match(v):
                kind = "iso8601"
            elif _looks_like_epoch(v):
                kind = _looks_like_epoch(v)
            elif TIMESTAMP_KEY_RE.search(k) and v not in (None, ""):
                kind = "named_but_unparsed"
            if kind:
                gp = re.sub(r"\[\d+\]", "[]", p)
                if gp not in out:
                    out[gp] = {"kind": kind, "sample": v if not isinstance(v, str) else v[:40]}
    elif isinstance(obj, list):
        for i, v in enumerate(obj[:3]):
            discover_timestamps(v, f"{path}[{i}]", out, depth + 1, max_found)
    return out


def structural_digest(obj, depth=0):
    if isinstance(obj, dict):
        return {k: (structural_digest(v, depth + 1) if depth < 3 else type(v).__name__) for k, v in list(obj.items())[:25]}
    if isinstance(obj, list):
        return [f"list[{len(obj)}]"] + ([structural_digest(obj[0], depth + 1)] if obj and depth < 3 else [])
    return type(obj).__name__


def fetch(url: str, *, accept: str, referer: str = "", ua: str = UA_BROWSERISH, timeout: int = 25) -> dict:
    headers = {"Accept": accept, "User-Agent": ua, "Accept-Language": "en-US,en;q=0.9"}
    if referer:
        headers["Referer"] = referer
        headers["Origin"] = "https://" + referer.split("/")[2]
    req = urllib.request.Request(url, headers=headers)
    t0 = time.monotonic()
    rec = {"url": url, "requested_at_utc": datetime.now(timezone.utc).isoformat()}
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            body = r.read(MAX_STORE_BYTES + 1)
            rec.update(status=r.status, latency_ms=round((time.monotonic() - t0) * 1000),
                       content_type=r.headers.get("Content-Type", ""), bytes=len(body),
                       truncated=len(body) > MAX_STORE_BYTES,
                       headers={h: r.headers.get(h) for h in RATE_HEADERS if r.headers.get(h)})
            rec["_body"] = body[:MAX_STORE_BYTES]
    except urllib.error.HTTPError as e:
        body = b""
        try:
            body = e.read(20000)
        except Exception:
            pass
        rec.update(status=e.code, latency_ms=round((time.monotonic() - t0) * 1000), error=f"HTTPError {e.code}",
                   content_type=e.headers.get("Content-Type", "") if e.headers else "", bytes=len(body),
                   headers={h: e.headers.get(h) for h in RATE_HEADERS if e.headers and e.headers.get(h)})
        rec["_body"] = body
    except (urllib.error.URLError, socket.timeout, ssl.SSLError, ConnectionError, OSError) as e:
        rec.update(status=None, latency_ms=round((time.monotonic() - t0) * 1000), error=f"{type(e).__name__}: {e}"[:300], bytes=0)
        rec["_body"] = b""
    return rec


def analyse(rec: dict, expect: str) -> dict:
    body = rec.pop("_body", b"")
    out = dict(rec)
    if not body:
        return out
    if expect in ("json", "unknown"):
        try:
            parsed = json.loads(body.decode("utf-8", "replace"))
        except Exception as e:
            out["parse"] = f"not-json ({type(e).__name__})"
            out["text_head"] = body[:300].decode("utf-8", "replace")
            return out
        out["parse"] = "json"
        out["structure"] = structural_digest(parsed)
        out["timestamp_fields"] = discover_timestamps(parsed)
        out["top_level_count"] = len(parsed) if isinstance(parsed, (list, dict)) else None
    else:
        out["parse"] = "html"
        out["text_head"] = body[:300].decode("utf-8", "replace")
    return out


def robots_for(host: str) -> dict:
    r = fetch(f"https://{host}/robots.txt", accept="text/plain")
    body = r.pop("_body", b"").decode("utf-8", "replace")
    star, cur = [], None
    for line in body.splitlines():
        line = line.split("#")[0].strip()
        if not line:
            continue
        k, _, v = line.partition(":")
        k, v = k.strip().lower(), v.strip()
        if k == "user-agent":
            cur = v
        elif k == "disallow" and cur == "*":
            star.append(v)
    return {"status": r.get("status"), "disallow_star": star[:40], "bytes": len(body)}
