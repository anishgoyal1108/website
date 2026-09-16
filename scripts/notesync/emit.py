"""Write generated content files and prune stale ones. Hand-written files are never removed."""
from __future__ import annotations

import re
from pathlib import Path

from . import frontmatter as fmlib
from .config import Config, Course
from .vault import Note

GENERATED_MARK = "generated: true"


def description_of(body: str, scrubber) -> str:
    for line in body.split("\n"):
        s = line.strip()
        if not s or s.startswith(("#", ">", "$$", "|", "```", "^", "![[", "{#", "<", "---")):
            continue
        s = re.sub(r"%%.*?%%", "", s).strip()
        if not s:
            continue
        s = re.sub(r"^(\s*([-*+]|\d+[.)])\s+)", "", s)
        s = re.sub(r"!?\[\[([^\]|#]*)(#[^\]|]*)?(\|([^\]]*))?\]\]", lambda m: m.group(4) or m.group(1), s)
        s = re.sub(r"\$\$?(.+?)\$\$?", r"\1", s)
        s = re.sub(r"[*_`=~]", "", s)
        s = re.sub(r"\\[a-zA-Z]+", "", s)
        s = re.sub(r"\s+", " ", s).strip()
        if len(s) < 12:
            continue
        if len(s) > 160:
            s = s[:157].rsplit(" ", 1)[0] + "…"
        return scrubber.scrub(s, "description")
    return ""


def note_frontmatter(note: Note, body_md: str, created, modified, scrubber) -> dict:
    words = len(re.findall(r"\S+", body_md))
    title = scrubber.scrub(note.title, "title")
    fm = {
        "author": "Anish Goyal",
        "title": title,
        "description": description_of(note.body, scrubber),
        "tags": ["notes", note.course.subject, note.course.slug],
        "date": fmlib.iso(created),
        "modified": fmlib.iso(modified),
        "readingtime": str(max(1, round(words / 200))),
        "course": note.course.code if note.course.code != "Self-study" else note.course.title,
        "course_slug": note.course.slug,
        "subject": note.course.subject,
        "kind": note.kind,
        "ordinal": note.ordinal if note.ordinal is not None else None,
        "weight": note.weight,
        "slug": note.slug,
        "links": sorted(set(note.links)),
        "sources": sorted(set(note.sources)),
        "generated": True,
    }
    if note.ordinal is None:
        fm.pop("ordinal")
    return fm


def course_index(course: Course, weight: int, count: dict[str, int]) -> str:
    fm = {
        "title": course.heading,
        "layout": "course",
        "code": course.code,
        "course_title": course.title,
        "subject": course.subject,
        "group": course.group,
        "term": course.term,
        "weight": weight,
        "outputs": ["html"],
        "lectures": count.get("lecture", 0),
        "concepts": count.get("concept", 0),
        "guides": count.get("guide", 0),
        "generated": True,
    }
    body = f"\n{course.blurb.strip()}\n" if course.blurb.strip() else ""
    return fmlib.dump(fm) + body


class Writer:
    def __init__(self, cfg: Config, dry_run: bool, report):
        self.cfg = cfg
        self.dry_run = dry_run
        self.report = report
        self.written: set[Path] = set()
        self.changed = 0

    def write(self, path: Path, text: str):
        self.written.add(path)
        if path.exists() and path.read_text(encoding="utf-8") == text:
            return
        self.changed += 1
        if self.dry_run:
            self.report.add("would write", str(path.relative_to(self.cfg.content_dir.parent.parent)))
            return
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def prune(self, course_slugs: set[str] | None, keep_static: set[Path]):
        """Delete generated files not written this run. With --only, only inside those courses."""
        root = self.cfg.content_dir
        if root.is_dir():
            for p in root.rglob("*.md"):
                if p in self.written:
                    continue
                if course_slugs is not None and p.parent.name not in course_slugs and p.parent != root:
                    continue
                try:
                    head = p.read_text(encoding="utf-8")[:2000]
                except OSError:
                    continue
                if GENERATED_MARK in head:
                    self.report.add("pruned", str(p.relative_to(root.parent.parent)))
                    self.changed += 1
                    if not self.dry_run:
                        p.unlink()
            for d in sorted(root.glob("*/"), reverse=True):
                if d.is_dir() and not any(d.iterdir()) and not self.dry_run:
                    d.rmdir()
        for sdir in (self.cfg.static_img, self.cfg.static_excalidraw):
            if not sdir.is_dir():
                continue
            for p in sdir.iterdir():
                if p not in keep_static and p.is_file():
                    self.report.add("pruned", str(p.relative_to(root.parent.parent)))
                    self.changed += 1
                    if not self.dry_run:
                        p.unlink()
