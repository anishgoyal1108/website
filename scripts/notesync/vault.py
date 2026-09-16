"""Discovery: which vault notes are published, with slugs, kinds and weights."""
from __future__ import annotations

import os
import re
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path

from . import frontmatter as fmlib
from .config import Config, Course

ORD_RE = re.compile(r"^(\d{1,3})(?:\.(\d+))?\s+(.+)$")
CHAPTER_RE = re.compile(r"^Chapter (\d+)\b", re.I)
IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp", ".avif"}


def slugify(s: str) -> str:
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-").lower()
    return s or "note"


@dataclass
class Note:
    path: Path
    rel: str
    course: Course
    name: str                      # vault basename (link target)
    title: str
    kind: str                      # lecture | guide | reference | concept
    ordinal: int | None
    sub: int | None
    weight: int
    slug: str
    fm: dict
    body: str
    mtime: float
    links: list[str] = field(default_factory=list)
    sources: list[str] = field(default_factory=list)

    @property
    def url(self) -> str:
        return f"/notes/{self.course.slug}/{self.slug}/"

    @property
    def prefix_source(self) -> str:
        return self.name


@dataclass
class Vault:
    cfg: Config
    notes: list[Note]
    by_name: dict[str, list[Note]]          # basename (lower) -> published notes
    by_path: dict[str, Note]
    all_md: dict[str, list[Path]]           # basename (lower) -> every vault md file
    images: dict[str, Path]                 # basename (lower) -> path
    excalidraw: dict[str, Path]             # basename without .excalidraw.md (lower) -> path
    warnings: list[str] = field(default_factory=list)
    exclusions: list[str] = field(default_factory=list)


def _first_heading(body: str) -> str | None:
    for line in body.splitlines():
        m = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if m:
            return m.group(1).strip()
    return None


def _classify(course: Course, stem: str, body: str) -> tuple[str, int | None, int | None, int, str]:
    title = stem
    ov = course.title_overrides.get(stem)
    if ov == "first-heading":
        title = _first_heading(body) or stem
    elif ov:
        title = ov
    m = ORD_RE.match(stem)
    if m:
        o, sub = int(m.group(1)), int(m.group(2) or 0)
        t = m.group(3).strip()
        if ov is None:
            title = t
        return "lecture", o, sub, o * 10 + sub, title
    m = CHAPTER_RE.match(stem)
    if m:
        return "guide", int(m.group(1)), None, 5000 + int(m.group(1)) * 10, title
    if stem in course.pinned:
        return "reference", None, None, 8000, title
    return "concept", None, None, 9000, title


def discover(cfg: Config, only: set[str] | None = None) -> Vault:
    vault = cfg.vault
    notes: list[Note] = []
    exclusions: list[str] = []
    warnings: list[str] = []
    courses = [c for c in cfg.courses if not only or c.slug in only or c.code.lower() in only]
    for course in courses:
        folder = vault / course.folder
        if not folder.is_dir():
            warnings.append(f"{course.code}: folder missing: {course.folder}")
            continue
        course_notes: list[Note] = []
        for p in sorted(folder.glob("*.md"), key=lambda x: x.name.lower()):
            stem = p.name[:-3]
            rel = p.relative_to(vault).as_posix()
            if p.stat().st_size == 0:
                exclusions.append(f"{rel}: empty file")
                continue
            if stem in course.exclude:
                exclusions.append(f"{rel}: excluded by config")
                continue
            text = p.read_text(encoding="utf-8", errors="replace")
            fm, body = fmlib.split(text)
            if any(k in fm for k in cfg.exclude_frontmatter_keys):
                exclusions.append(f"{rel}: frontmatter key ({', '.join(k for k in cfg.exclude_frontmatter_keys if k in fm)})")
                continue
            if stem.endswith(".excalidraw"):
                exclusions.append(f"{rel}: excalidraw file")
                continue
            if not ORD_RE.match(stem) and any(pat.search(stem) for pat in cfg.exclude_filename_patterns):
                exclusions.append(f"{rel}: filename pattern")
                continue
            if not body.strip():
                exclusions.append(f"{rel}: empty body")
                continue
            kind, o, sub, weight, title = _classify(course, stem, body)
            slug_src = ORD_RE.match(stem).group(3) if kind == "lecture" else stem
            course_notes.append(Note(path=p, rel=rel, course=course, name=stem, title=title, kind=kind,
                                     ordinal=o, sub=sub, weight=weight, slug=slugify(slug_src), fm=fm, body=body,
                                     mtime=p.stat().st_mtime))
        # slugs: lectures win collisions, concepts get -concept
        used: dict[str, Note] = {}
        for n in sorted(course_notes, key=lambda n: (n.kind != "lecture", n.weight, n.name.lower())):
            s = n.slug
            if s in used:
                s2 = s + ("-concept" if n.kind == "concept" else "-2")
                k = 2
                while s2 in used:
                    k += 1
                    s2 = f"{s}-{k}"
                warnings.append(f"{course.code}: slug collision {n.name!r} vs {used[s].name!r} -> {s2}")
                n.slug = s2
                s = s2
            used[s] = n
        # concept ordering: alphabetical, weight 9000+
        concepts = sorted((n for n in course_notes if n.kind == "concept"), key=lambda n: n.name.lower())
        for i, n in enumerate(concepts):
            n.weight = 9000 + i
        notes.extend(sorted(course_notes, key=lambda n: (n.weight, n.name.lower())))

    by_name: dict[str, list[Note]] = {}
    for n in notes:
        by_name.setdefault(n.name.lower(), []).append(n)
    by_path = {n.rel: n for n in notes}

    all_md: dict[str, list[Path]] = {}
    images: dict[str, Path] = {}
    excal: dict[str, Path] = {}
    skip = {".git", ".obsidian", ".trash", "node_modules"}
    for root, dirs, files in os.walk(vault):
        dirs[:] = [d for d in dirs if d not in skip]
        for f in files:
            p = Path(root) / f
            low = f.lower()
            if low.endswith(".excalidraw.md"):
                excal.setdefault(f[:-len(".excalidraw.md")].lower(), p)
            elif low.endswith(".md"):
                all_md.setdefault(f[:-3].lower(), []).append(p)
            elif Path(low).suffix in IMAGE_EXT:
                key = f.lower()
                relroot = Path(root).relative_to(vault).as_posix()
                preferred = any(relroot.startswith(d) for d in cfg.image_dirs)
                if key not in images or preferred:
                    images[key] = p
    return Vault(cfg=cfg, notes=notes, by_name=by_name, by_path=by_path, all_md=all_md, images=images,
                 excalidraw=excal, warnings=warnings, exclusions=exclusions)


def resolve_note(vault: Vault, target: str, from_note: Note | None) -> Note | None:
    """Resolve a wikilink target (basename or vault path) to a published note."""
    t = target.strip()
    if t.lower().endswith(".md"):
        t = t[:-3]
    if "/" in t:
        n = vault.by_path.get(t + ".md")
        if n:
            return n
        if (vault.cfg.vault / (t + ".md")).is_file():
            return None  # a real vault path that is not published
        t = t.rsplit("/", 1)[1]
    cands = vault.by_name.get(t.lower(), [])
    if not cands:
        return None
    if from_note is not None:
        same = [c for c in cands if c.course is from_note.course]
        if same:
            return same[0]
    return cands[0]
