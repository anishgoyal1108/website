"""Minimal YAML frontmatter reader/writer and Templater date parsing."""
from __future__ import annotations

import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

FM_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.S)


def split(text: str) -> tuple[dict, str]:
    """Return (frontmatter dict, body). Handles scalars, inline and block lists."""
    m = FM_RE.match(text)
    if not m:
        return {}, text
    fm: dict = {}
    key = None
    for line in m.group(1).splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")) and key is not None:
            s = line.strip()
            if s.startswith("- "):
                fm.setdefault(key, [])
                if not isinstance(fm[key], list):
                    fm[key] = []
                fm[key].append(_scalar(s[2:]))
            continue
        km = re.match(r"^([A-Za-z0-9_\-]+):\s*(.*)$", line)
        if not km:
            continue
        key, val = km.group(1), km.group(2).strip()
        if val == "":
            fm[key] = None
        elif val.startswith("[") and val.endswith("]"):
            inner = val[1:-1].strip()
            fm[key] = [_scalar(x.strip()) for x in inner.split(",")] if inner else []
        else:
            fm[key] = _scalar(val)
    return fm, text[m.end():]


def _scalar(v: str):
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
        return v[1:-1]
    return v


MONTHS = {m: i for i, m in enumerate(
    ["january", "february", "march", "april", "may", "june", "july", "august",
     "september", "october", "november", "december"], 1)}
LONG_RE = re.compile(
    r"^(?:[A-Za-z]+,\s*)?([A-Za-z]+)\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4}),?\s+(\d{1,2}):(\d{2})(?::(\d{2}))?\s*([ap]m)?\s*$",
    re.I)
ISO_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})(?:[ T](\d{1,2}):(\d{2})(?::(\d{2}))?)?")


def parse_date(value) -> datetime | None:
    """Parse Templater long form (weekday ignored, so 'Satunday' is fine) or ISO."""
    if value is None:
        return None
    s = str(value).strip()
    m = LONG_RE.match(s)
    if m:
        mon = MONTHS.get(m.group(1).lower())
        if not mon:
            return None
        h = int(m.group(4))
        ampm = (m.group(7) or "").lower()
        if ampm == "pm" and h < 12:
            h += 12
        if ampm == "am" and h == 12:
            h = 0
        return datetime(int(m.group(3)), mon, int(m.group(2)), h, int(m.group(5)), int(m.group(6) or 0))
    m = ISO_RE.match(s)
    if m:
        return datetime(int(m.group(1)), int(m.group(2)), int(m.group(3)),
                        int(m.group(4) or 0), int(m.group(5) or 0), int(m.group(6) or 0))
    return None


def iso(dt: datetime) -> str:
    return dt.strftime("%Y-%m-%dT%H:%M:%S")


class GitDates:
    """First/last commit dates for vault files, cached on disk. Read-only git use."""

    def __init__(self, vault: Path, cache_dir: Path):
        self.vault = vault
        self.cache_file = cache_dir / "gitdates.json"
        try:
            self.cache = json.loads(self.cache_file.read_text())
        except Exception:
            self.cache = {}
        self.dirty = False

    def lookup(self, rel: str, mtime: float) -> tuple[datetime | None, datetime | None]:
        key = f"{rel}@{int(mtime)}"
        if key in self.cache:
            a, b = self.cache[key]
            return (datetime.fromisoformat(a) if a else None, datetime.fromisoformat(b) if b else None)
        created = modified = None
        try:
            out = subprocess.run(
                ["git", "-C", str(self.vault), "log", "--follow", "--format=%aI", "--", rel],
                capture_output=True, text=True, timeout=60).stdout.split()
            if out:
                modified = datetime.fromisoformat(out[0]).replace(tzinfo=None)
                created = datetime.fromisoformat(out[-1]).replace(tzinfo=None)
        except Exception:
            pass
        self.cache[key] = (iso(created) if created else None, iso(modified) if modified else None)
        self.dirty = True
        return created, modified

    def save(self):
        if self.dirty:
            self.cache_file.parent.mkdir(parents=True, exist_ok=True)
            self.cache_file.write_text(json.dumps(self.cache, indent=0, sort_keys=True))


def dump(fm: dict) -> str:
    """Serialize a flat frontmatter dict deterministically."""
    out = ["---"]
    for k, v in fm.items():
        if v is None:
            continue
        if isinstance(v, bool):
            out.append(f"{k}: {'true' if v else 'false'}")
        elif isinstance(v, (int, float)):
            out.append(f"{k}: {v}")
        elif isinstance(v, list):
            if not v:
                out.append(f"{k}: []")
            else:
                out.append(f"{k}:")
                out.extend(f"  - {_q(x)}" for x in v)
        else:
            out.append(f"{k}: {_q(v)}")
    out.append("---")
    return "\n".join(out) + "\n"


def _q(v) -> str:
    s = str(v)
    if re.match(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}$", s):
        return s
    return json.dumps(s, ensure_ascii=False)
