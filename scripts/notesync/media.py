"""Images (copied) and Excalidraw drawings (rendered to SVG elsewhere, referenced here)."""
from __future__ import annotations

import html
import re
import shutil
from dataclasses import dataclass, field
from pathlib import Path

from .config import Config
from .vault import IMAGE_EXT, Vault, slugify

PASTED_RE = re.compile(r"^(pasted image \d+|[0-9a-f]{8}-[0-9a-f]{4}-|\{[0-9A-F-]{36}\}|screenshot|image ?\d*)", re.I)


@dataclass
class Media:
    cfg: Config
    vault: Vault
    report: object
    dry_run: bool = False
    images_used: dict[str, Path] = field(default_factory=dict)      # dest basename -> source
    drawings_used: dict[str, Path] = field(default_factory=dict)    # svg slug -> source .excalidraw.md
    drawing_alt: dict[str, str] = field(default_factory=dict)

    # ------------------------------------------------------------------ images
    def image(self, name: str, alias: str | None, in_table: bool = False) -> str:
        base = name.rsplit("/", 1)[-1]
        src = self.vault.images.get(base.lower())
        if src is None:
            self.report.add("missing images", base)
            return f'<em class="missing-media">(image unavailable: {html.escape(base)})</em>'
        stem, ext = base.rsplit(".", 1)
        dest = f"{slugify(stem)}.{ext.lower()}"
        prev = self.images_used.get(dest)
        if prev is not None and prev != src:
            k = 2
            while f"{slugify(stem)}-{k}.{ext.lower()}" in self.images_used:
                k += 1
            dest = f"{slugify(stem)}-{k}.{ext.lower()}"
        self.images_used[dest] = src
        self.report.add("copied images", f"{dest} <- {src.relative_to(self.cfg.vault).as_posix()}")
        width = height = None
        alt = "" if PASTED_RE.match(stem) else stem
        if alias:
            a = alias.strip()
            m = re.match(r"^(\d+)(?:x(\d+))?$", a)
            if m:
                width, height = m.group(1), m.group(2)
            else:
                alt = a
        attrs = [f'src="/notes/img/{dest}"', f'alt="{html.escape(alt, quote=True)}"', 'loading="lazy"']
        if width:
            attrs.append(f'width="{width}"')
        if height:
            attrs.append(f'height="{height}"')
        return f'<a class="zoom" href="/notes/img/{dest}"><img {" ".join(attrs)}></a>'

    def copy_images(self):
        if self.dry_run:
            return
        self.cfg.static_img.mkdir(parents=True, exist_ok=True)
        for dest, src in self.images_used.items():
            d = self.cfg.static_img / dest
            if not d.exists() or d.stat().st_size != src.stat().st_size or d.stat().st_mtime < src.stat().st_mtime:
                shutil.copyfile(src, d)

    # ------------------------------------------------------------------ excalidraw
    def excalidraw(self, name: str, alias: str | None) -> str:
        base = name.rsplit("/", 1)[-1]
        if base.lower().endswith(".excalidraw.md"):
            base = base[:-len(".excalidraw.md")]
        elif base.lower().endswith(".excalidraw"):
            base = base[:-len(".excalidraw")]
        src = self.vault.excalidraw.get(base.lower())
        if src is None:
            self.report.add("missing drawings", base)
            return '<figure class="excalidraw missing"><span class="missing-media">(drawing unavailable)</span></figure>'
        slug = slugify(base)
        self.drawings_used[slug] = src
        self.drawing_alt[slug] = base
        width = ""
        if alias and re.match(r"^\d+(x\d+)?$", alias.strip()):
            width = f' width="{alias.strip().split("x")[0]}"'
        return (f'<figure class="excalidraw"><a class="zoom" href="/notes/excalidraw/{slug}.svg">'
                f'<img src="/notes/excalidraw/{slug}.svg" alt="{html.escape(base, quote=True)}" loading="lazy"{width}></a></figure>')


def is_image_name(name: str) -> bool:
    return Path(name.lower()).suffix in IMAGE_EXT


def is_excalidraw_name(vault: Vault, name: str) -> bool:
    low = name.lower().rsplit("/", 1)[-1]
    if low.endswith(".excalidraw") or low.endswith(".excalidraw.md"):
        return True
    return low in vault.excalidraw and low not in vault.by_name
