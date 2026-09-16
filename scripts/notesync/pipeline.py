"""Orchestrates a sync run."""
from __future__ import annotations

import re
from datetime import datetime
from pathlib import Path

from . import config as cfglib
from . import excalidraw_render, frontmatter as fmlib
from .citations import Citations
from .emit import Writer, course_index, note_frontmatter
from .media import Media
from .render import Renderer
from .scrub import Scrubber
from .theorems import RefIndex
from .vault import Vault


def run(cfg, vault: Vault, report, args) -> int:
    scrubber = Scrubber(cfglib.DENYLIST, required=not args.allow_no_denylist)
    index = RefIndex(cfg, vault)
    index.build(report)
    media = Media(cfg, vault, report, dry_run=args.dry_run)
    cites = Citations(cfg)
    renderer = Renderer(cfg, vault, index, media, cites, report, scrubber)
    writer = Writer(cfg, args.dry_run, report)
    gitdates = fmlib.GitDates(cfg.vault, cfglib.CACHE_DIR)

    rendered: dict[str, str] = {}
    for note in vault.notes:
        try:
            rendered[note.rel] = renderer.render_note(note)
        except Exception as ex:  # keep going, report loudly
            report.add("render errors", f"{note.rel}: {type(ex).__name__}: {ex}")
            raise
    # dates
    for note in vault.notes:
        created = fmlib.parse_date(note.fm.get("created"))
        modified = fmlib.parse_date(note.fm.get("modified"))
        if created is None or modified is None:
            gc, gm = gitdates.lookup(note.rel, note.mtime)
            if created is None:
                created = gc
            if modified is None:
                modified = gm or created
            if created is None:
                created = modified = datetime.fromtimestamp(note.mtime)
                report.add("dates from mtime", note.rel)
            else:
                report.add("dates from git", note.rel)
        fm = note_frontmatter(note, rendered[note.rel], created, modified, scrubber)
        path = cfg.content_dir / note.course.slug / f"{note.slug}.md"
        writer.write(path, fmlib.dump(fm) + "\n" + rendered[note.rel])
    gitdates.save()
    from . import icons
    writer.write(cfglib.REPO / "layouts" / "partials" / "callout-icons.html", icons.sprite_html())

    # course hubs
    only = {o.lower() for o in args.only} or None
    for w, course in enumerate(cfg.courses, 1):
        if only and course.slug not in only and course.code.lower() not in only:
            continue
        counts: dict[str, int] = {}
        for n in vault.notes:
            if n.course is course:
                counts[n.kind] = counts.get(n.kind, 0) + 1
        if not counts:
            continue
        writer.write(cfg.content_dir / course.slug / "_index.md", course_index(course, w * 10, counts))

    # media
    media.copy_images()
    keep_static = {cfg.static_img / d for d in media.images_used}
    svgs = excalidraw_render.render_all(cfg, vault, media, scrubber, report, args)
    keep_static |= set(svgs)
    if only:
        # other courses' assets are still referenced by their existing pages
        keep_static |= _referenced_static(cfg)

    writer.prune(only and {c.slug for c in cfg.courses if c.slug in only or c.code.lower() in only}, keep_static)
    report.bump("files changed", writer.changed)
    report.bump("names scrubbed", scrubber.count)
    for k, v in sorted(scrubber.hits.items()):
        report.add("scrub hits", f"{k}: {v}")
    if args.check and writer.changed:
        print(f"--check: {writer.changed} file(s) would change")
        return 3
    return 0


def _referenced_static(cfg) -> set[Path]:
    keep = set()
    if cfg.content_dir.is_dir():
        for p in cfg.content_dir.rglob("*.md"):
            t = p.read_text(encoding="utf-8", errors="replace")
            for m in re.finditer(r"/notes/img/([^\"')\s]+)", t):
                keep.add(cfg.static_img / m.group(1))
            for m in re.finditer(r"/notes/excalidraw/([^\"')\s]+)", t):
                keep.add(cfg.static_excalidraw / m.group(1))
    return keep
