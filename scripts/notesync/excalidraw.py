"""Parse Obsidian Excalidraw markdown files into scene JSON plus embedded files."""
from __future__ import annotations

import json
import re
from dataclasses import dataclass, field
from pathlib import Path

from . import lzstring

FENCE_JSON = re.compile(r"```json\r?\n(.*?)\r?\n```", re.S)
FENCE_LZ = re.compile(r"```compressed-json\r?\n(.*?)\r?\n```", re.S)
EMBED_LINE = re.compile(r"^([0-9a-f]{40}|[A-Za-z0-9_-]{8,}):\s*(.*)$")


@dataclass
class Drawing:
    path: Path
    name: str
    scene: dict
    embedded: dict[str, str] = field(default_factory=dict)   # fileId -> "[[image.png]]" or "$$…$$"
    frontmatter: dict = field(default_factory=dict)

    @property
    def elements(self) -> list[dict]:
        return [e for e in self.scene.get("elements", []) if not e.get("isDeleted")]


def _section(text: str, name: str) -> str:
    m = re.search(rf"^## {re.escape(name)}\s*$", text, re.M)
    if not m:
        return ""
    rest = text[m.end():]
    m2 = re.search(r"^(## |%%|# )", rest, re.M)
    return rest[: m2.start()] if m2 else rest


def parse(path: Path) -> Drawing:
    text = path.read_text(encoding="utf-8", errors="replace")
    fm: dict = {}
    m = re.match(r"\A---\r?\n(.*?)\r?\n---", text, re.S)
    if m:
        for line in m.group(1).splitlines():
            km = re.match(r"^([\w-]+):\s*(.*)$", line)
            if km:
                fm[km.group(1)] = km.group(2).strip()
    raw = None
    m = FENCE_JSON.search(text)
    if m:
        raw = m.group(1)
    else:
        m = FENCE_LZ.search(text)
        if m:
            raw = lzstring.decompress_from_base64(m.group(1))
    if not raw:
        raise ValueError(f"no drawing block in {path}")
    scene = json.loads(raw)
    embedded: dict[str, str] = {}
    sec = _section(text, "Embedded Files")
    cur_id = None
    buf: list[str] = []

    def flush():
        if cur_id is not None:
            embedded[cur_id] = "\n".join(buf).strip()

    for line in sec.splitlines():
        em = EMBED_LINE.match(line)
        if em and (em.group(2).startswith("[[") or em.group(2).startswith("$$") or em.group(2) == ""):
            flush()
            cur_id = em.group(1)
            buf = [em.group(2)]
        elif cur_id is not None:
            buf.append(line)
    flush()
    name = path.name[: -len(".excalidraw.md")] if path.name.endswith(".excalidraw.md") else path.stem
    return Drawing(path=path, name=name, scene=scene, embedded=embedded, frontmatter=fm)
