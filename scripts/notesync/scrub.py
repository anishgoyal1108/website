"""Replace real names with role words. Denylist lives outside the repo."""
from __future__ import annotations

import re
from pathlib import Path

HONORIFIC = r"\b(?:Dr|Prof|Professor|Mr|Mrs|Ms|Mx)\.?\s+"


class Scrubber:
    def __init__(self, path: Path, required: bool = True):
        self.rules: list[tuple[re.Pattern, str]] = []
        self.allow: set[str] = set()
        self.count = 0
        self.hits: dict[str, int] = {}
        if not path.is_file():
            if required:
                raise SystemExit(f"denylist not found at {path}; create it or pass --allow-no-denylist")
            return
        for raw in path.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#"):
                continue
            if line.lower().startswith("allow:"):
                self.allow.add(line.split(":", 1)[1].strip())
                continue
            if "=>" not in line:
                continue
            name, repl = (x.strip() for x in line.split("=>", 1))
            if not name:
                continue
            esc = re.escape(name)
            # "Dr. Name's" -> "the instructor's"; then bare "Name"
            self.rules.append((re.compile(HONORIFIC + esc + r"(?=['’]s\b|\b)", re.I), repl))
            self.rules.append((re.compile(r"\b" + esc + r"(?=['’]s\b|\b)"), repl))
            self.rules.append((re.compile(r"\b" + esc + r"(?=['’]s\b|\b)", re.I), repl))

    def scrub(self, text: str, where: str = "") -> str:
        if not text or not self.rules:
            return text
        for pat, repl in self.rules:
            text, n = pat.subn(repl, text)
            if n:
                self.count += n
                self.hits[where] = self.hits.get(where, 0) + n
        return text
