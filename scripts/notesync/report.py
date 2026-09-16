"""Collects warnings and statistics for the end-of-run report."""
from __future__ import annotations

from collections import Counter, defaultdict


class Report:
    def __init__(self):
        self.sections: dict[str, list[str]] = defaultdict(list)
        self.counts: Counter = Counter()

    def add(self, section: str, line: str):
        if line not in self.sections[section]:
            self.sections[section].append(line)

    def bump(self, key: str, n: int = 1):
        self.counts[key] += n

    def render(self, verbose: bool = True) -> str:
        out = ["== sync report =="]
        for k, v in sorted(self.counts.items()):
            out.append(f"  {k}: {v}")
        for name, lines in self.sections.items():
            out.append(f"-- {name} ({len(lines)})")
            if verbose:
                out.extend("   " + l for l in lines)
            else:
                out.extend("   " + l for l in lines[:15])
                if len(lines) > 15:
                    out.append(f"   ... {len(lines) - 15} more")
        return "\n".join(out)
