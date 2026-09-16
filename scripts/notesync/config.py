"""Load scripts/notes.toml into plain dataclasses."""
from __future__ import annotations

import os
import re
import tomllib
from dataclasses import dataclass, field
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPTS = HERE.parent
REPO = SCRIPTS.parent
CACHE_DIR = Path(os.environ.get("WEBSITE_SYNC_CACHE", Path.home() / ".cache" / "website-sync"))
DENYLIST = Path(os.environ.get("WEBSITE_SYNC_DENYLIST", Path.home() / ".config" / "website-sync" / "denylist.txt"))


@dataclass
class Course:
    code: str
    slug: str
    title: str
    term: str
    subject: str
    group: str
    folder: str
    exclude: list[str] = field(default_factory=list)
    pinned: list[str] = field(default_factory=list)
    title_overrides: dict[str, str] = field(default_factory=dict)
    blurb: str = ""

    @property
    def heading(self) -> str:
        return f"{self.code}: {self.title}" if self.code != "Self-study" else self.title


@dataclass
class Textbook:
    title: str
    authors: str = ""
    edition: str = ""


@dataclass
class Config:
    vault: Path
    image_dirs: list[str]
    excalidraw_dirs: list[str]
    scan_dirs: list[str]
    exclude_frontmatter_keys: list[str]
    exclude_filename_patterns: list[re.Pattern]
    group_order: list[str]
    parity: dict
    courses: list[Course]
    textbooks: dict[str, Textbook]
    content_dir: Path = REPO / "content" / "notes"
    static_img: Path = REPO / "static" / "notes" / "img"
    static_excalidraw: Path = REPO / "static" / "notes" / "excalidraw"

    def course_by_slug(self, slug: str) -> Course | None:
        for c in self.courses:
            if c.slug == slug or c.code.lower() == slug.lower():
                return c
        return None


def load(path: Path | None = None) -> Config:
    path = path or SCRIPTS / "notes.toml"
    with open(path, "rb") as fh:
        raw = tomllib.load(fh)
    vault = Path(os.environ.get("WEBSITE_VAULT") or raw["vault"]["path"]).expanduser()
    if not vault.is_dir():
        raise SystemExit(f"vault not found: {vault} (set WEBSITE_VAULT)")
    courses = [Course(**c) for c in raw.get("courses", [])]
    seen = set()
    for c in courses:
        if c.slug in seen:
            raise SystemExit(f"duplicate course slug {c.slug}")
        seen.add(c.slug)
    textbooks = {k: Textbook(**v) for k, v in raw.get("textbooks", {}).items()}
    ex = raw.get("exclude", {})
    return Config(
        vault=vault,
        image_dirs=raw["vault"].get("image_dirs", []),
        excalidraw_dirs=raw["vault"].get("excalidraw_dirs", []),
        scan_dirs=raw["vault"].get("scan_dirs", ["04. Notes"]),
        exclude_frontmatter_keys=ex.get("frontmatter_keys", []),
        exclude_filename_patterns=[re.compile(p) for p in ex.get("filename_patterns", [])],
        group_order=raw.get("groups", {}).get("order", []),
        parity=raw.get("parity", {}),
        courses=courses,
        textbooks=textbooks,
    )
