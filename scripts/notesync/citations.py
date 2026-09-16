"""PDF references become citations; no PDF is ever copied."""
from __future__ import annotations

import html
import re

from .config import Config

PATTERNS = [
    (re.compile(r"^(\d+\.\d+) AW$"), lambda m: f"Lecture notes §{m.group(1)}"),
    (re.compile(r"^(\d+\.\d+) HQ$"), lambda m: f"Homework quiz §{m.group(1)}"),
    (re.compile(r"^(\d+\.\d+) SS$"), lambda m: f"Self-study problems §{m.group(1)}"),
    (re.compile(r"^HQ-(\d+)-(\d+)-sol$"), lambda m: f"Standalone quiz {m.group(1)}.{m.group(2)} solutions"),
    (re.compile(r"^HQ-(\d+)-(\d+)$"), lambda m: f"Standalone quiz {m.group(1)}.{m.group(2)}"),
    (re.compile(r"^lecture(\d+)-(\d+)-3421$"), lambda m: f"Course lecture slides {int(m.group(1))}–{int(m.group(2))}"),
    (re.compile(r"^lecture(\d+)-3421$"), lambda m: f"Course lecture slides {int(m.group(1))}"),
    (re.compile(r"^HW(\d+)(?:-3421)?$"), lambda m: f"Homework {m.group(1)}"),
    (re.compile(r"^HW(\d+) - (.+?)\s*$"), lambda m: f"Homework {m.group(1)} ({m.group(2).strip()})"),
    (re.compile(r"^Chap(\d+)$"), lambda m: f"Textbook chapter {m.group(1)} slides"),
    (re.compile(r"^\d+_EENG3341_Chapter_(\d+)_(.+)$"), lambda m: f"Course slides, chapter {int(m.group(1))}: {m.group(2).replace('_', ' ')}"),
    (re.compile(r"^EENG 5342 Chapter (\d+) Lectures$"), lambda m: f"Course slides, chapter {m.group(1)}"),
    (re.compile(r"^Chapter_(\d+)_(.+)$"), lambda m: f"Course slides, chapter {int(m.group(1))}: {m.group(2).replace('_', ' ')}"),
    (re.compile(r"^\d+_(.+)$"), lambda m: f"Course slides: {m.group(1).replace('_', ' ')}"),
    (re.compile(r"^(\d+\.\d+) (.+)$"), lambda m: f"Course slides §{m.group(1)}: {m.group(2)}"),
    (re.compile(r"^(\d+)\) (.+)$"), lambda m: f"Course handout {m.group(1)}: {m.group(2)}"),
    (re.compile(r"^(Practice \d+) solution$"), lambda m: f"{m.group(1)} solutions"),
    (re.compile(r"^(.+?) table$"), lambda m: f"{m.group(1).capitalize()} table (course handout)"),
    (re.compile(r"^(?:Complete |Preliminary )?Mock Test (\d+)$"), lambda m: f"Mock test {m.group(1)}"),
    (re.compile(r"^MATH2160-final-sample$"), lambda m: "Sample final exam"),
]


class Citations:
    def __init__(self, cfg: Config):
        self.cfg = cfg

    def title_html(self, name: str) -> tuple[str, str]:
        """(html, plain) source description for a PDF basename."""
        base = name.rsplit("/", 1)[-1]
        if base.lower().endswith(".pdf"):
            base = base[:-4]
        tb = self.cfg.textbooks.get(base + ".pdf")
        if tb:
            h = f"{html.escape(tb.authors)}, <em>{html.escape(tb.title)}</em>" if tb.authors else f"<em>{html.escape(tb.title)}</em>"
            if tb.edition:
                h += f", {html.escape(tb.edition)}"
            plain = f"{tb.authors}, {tb.title}" if tb.authors else tb.title
            return h, plain
        for pat, fn in PATTERNS:
            m = pat.match(base)
            if m:
                t = fn(m)
                return html.escape(t), t
        t = re.sub(r"[_]+", " ", base).strip()
        t = re.sub(r"\s+", " ", t)
        if t and t[0].islower():
            t = t[0].upper() + t[1:]
        return html.escape(t + " (course handout)"), t

    @staticmethod
    def _page(frag: str | None) -> str | None:
        if not frag:
            return None
        m = re.search(r"(?:^|&)page=(\d+)", frag)
        return m.group(1) if m else None

    def render(self, name: str, frag: str | None, alias: str | None, embed: bool) -> tuple[str, str]:
        """Return (html, plain source title). alias is already inline-processed text."""
        src_html, plain = self.title_html(name)
        page = self._page(frag)
        pg = f", p.&nbsp;{page}" if page else ""
        selection = bool(frag and "selection=" in frag) or bool(frag and "annotation=" in frag)
        if embed:
            if page:
                return f'<span class="cite cite-embed">Source: {src_html}{pg}</span>', plain
            return f'<span class="cite cite-ref">{src_html}</span>', plain
        if alias:
            cls = "cite cite-quote" if selection else "cite"
            return f'<cite class="{cls}">{alias} <span class="cite-src">[{src_html}{pg}]</span></cite>', plain
        return f'<cite class="cite">{src_html}{pg}</cite>', plain
