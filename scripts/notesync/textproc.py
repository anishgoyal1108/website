"""Text helpers: fence detection, placeholder protection, heading ids, slugs."""
from __future__ import annotations

import re
import unicodedata

FENCE_RE = re.compile(r"^\s{0,3}(`{3,}|~{3,})")


def is_fence(line: str, opened: str | None = None) -> str | None:
    m = FENCE_RE.match(line)
    if not m:
        return None
    mark = m.group(1)
    if opened is None:
        return mark
    return mark if mark[0] == opened[0] and len(mark) >= len(opened) else None


def strip_fenced(text: str) -> str:
    out = []
    fence = None
    for line in text.split("\n"):
        if fence:
            if is_fence(line, fence):
                fence = None
            continue
        f = is_fence(line)
        if f:
            fence = f
            continue
        out.append(line)
    return "\n".join(out)


MATH_CMD_RE = re.compile(r"\\[A-Za-z]+")


def heading_id(text: str, used: dict[str, int] | None = None) -> str:
    """Deterministic slug for a heading: math and TeX commands removed."""
    t = re.sub(r"\$\$?.*?\$\$?", lambda m: MATH_CMD_RE.sub(" ", m.group(0)).replace("$", ""), text)
    t = re.sub(r"[\\{}^_]", " ", t)
    t = re.sub(r"\[\[([^\]|]*)(\|([^\]]*))?\]\]", lambda m: m.group(3) or m.group(1), t)
    t = re.sub(r"[*_`~=]", "", t)
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode()
    t = re.sub(r"[^A-Za-z0-9]+", "-", t).strip("-").lower() or "section"
    if used is not None:
        n = used.get(t, 0)
        used[t] = n + 1
        if n:
            t = f"{t}-{n}"
    return t


class Protector:
    """Swap inline code, fenced code and math for placeholders and back."""

    def __init__(self):
        self.store: list[str] = []

    def _stash(self, s: str) -> str:
        self.store.append(s)
        return f"\x00{len(self.store) - 1}\x00"

    def protect_inline(self, line: str, math: bool = True) -> str:
        line = re.sub(r"(`+)(.+?)\1", lambda m: self._stash(m.group(0)), line)
        if math:
            line = re.sub(r"\$\$(.+?)\$\$", lambda m: self._stash(m.group(0)), line)
            line = re.sub(r"(?<![\\$\w])\$(?!\s)((?:\\.|[^$\\])+?)(?<!\s)\$(?!\w|\$)", lambda m: self._stash(m.group(0)), line)
        return line

    def restore(self, text: str) -> str:
        return re.sub(r"\x00(\d+)\x00", lambda m: self.store[int(m.group(1))], text)
