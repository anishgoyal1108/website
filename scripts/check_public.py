#!/usr/bin/env python3
"""Post-build gates over public/. Exit non-zero on any failure.

1. denylist grep (names that must never appear), when the denylist is available;
2. generic honorific + capitalised-name pattern in notes and posts;
3. no raw wikilink brackets outside code in notes HTML;
4. every root-relative href/src resolves to a built file, and #fragments on /notes/ targets exist;
5. every referenced Excalidraw SVG exists.
"""
from __future__ import annotations

import html
import os
import re
import sys
from urllib.parse import unquote
from html.parser import HTMLParser
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PUBLIC = Path(os.environ.get("PUBLIC_DIR", REPO / "public"))
DENYLIST = Path(os.environ.get("WEBSITE_SYNC_DENYLIST", Path.home() / ".config" / "website-sync" / "denylist.txt"))
HONORIFIC = re.compile(r"\b(?:Dr|Prof|Professor)\.?\s+[A-Z][a-z]+")


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links: list[tuple[str, str]] = []
        self.ids: set[str] = set()
        self.in_code = 0
        self.text: list[str] = []

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in ("a", "link") and a.get("href"):
            self.links.append(("href", a["href"]))
        if tag in ("img", "script", "source") and a.get("src"):
            self.links.append(("src", a["src"]))
        if a.get("id"):
            self.ids.add(a["id"])
        if tag in ("code", "pre", "script", "style"):
            self.in_code += 1

    def handle_endtag(self, tag):
        if tag in ("code", "pre", "script", "style") and self.in_code:
            self.in_code -= 1

    def handle_data(self, data):
        if not self.in_code:
            self.text.append(data)


def load_denylist() -> list[str]:
    names = []
    if DENYLIST.is_file():
        for line in DENYLIST.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or line.lower().startswith("allow:") or "=>" not in line:
                continue
            names.append(line.split("=>", 1)[0].strip())
    return names


def main() -> int:
    if not PUBLIC.is_dir():
        print("public/ missing; run hugo first")
        return 2
    failures: list[str] = []
    names = load_denylist()
    name_res = [re.compile(r"\b" + re.escape(n) + r"\b", re.I) for n in names]
    if not names:
        print("note: denylist missing or empty; skipping the name gate")
    pages: dict[Path, Links] = {}
    for p in PUBLIC.rglob("*"):
        if not p.is_file():
            continue
        rel = p.relative_to(PUBLIC).as_posix()
        if p.suffix in (".html", ".xml", ".json", ".svg", ".txt"):
            try:
                text = p.read_text(encoding="utf-8", errors="replace")
            except OSError:
                continue
            for n, rx in zip(names, name_res):
                if rx.search(text):
                    failures.append(f"denylist: {n!r} in {rel}")
            if p.suffix == ".html":
                parser = Links()
                parser.feed(text)
                pages[p] = parser
                body = html.unescape("".join(parser.text))
                if rel.startswith(("notes/", "blog/", "writeups/")):
                    for m in HONORIFIC.finditer(body):
                        failures.append(f"honorific: {m.group(0)!r} in {rel}")
                if rel.startswith("notes/") and ("[[" in body or "]]" in body):
                    failures.append(f"raw wikilink brackets in {rel}")
    # link checker
    def exists(path: str) -> bool:
        path = unquote(path.split("?")[0])
        target = PUBLIC / path.lstrip("/")
        return target.is_file() or (target / "index.html").is_file()

    ids_cache: dict[str, set[str]] = {}
    for p, parser in pages.items():
        rel = p.relative_to(PUBLIC).as_posix()
        for kind, url in parser.links:
            if not url.startswith("/") or url.startswith("//"):
                continue
            path, _, frag = url.partition("#")
            if path and not exists(path):
                failures.append(f"broken {kind}: {url} in {rel}")
                continue
            if frag and path.startswith("/notes/"):
                target = PUBLIC / path.lstrip("/")
                tfile = target / "index.html" if target.is_dir() else target
                if tfile.suffix == ".html" and tfile.is_file():
                    if str(tfile) not in ids_cache:
                        lp = Links()
                        lp.feed(tfile.read_text(encoding="utf-8", errors="replace"))
                        ids_cache[str(tfile)] = lp.ids
                    if frag not in ids_cache[str(tfile)]:
                        failures.append(f"missing fragment #{frag} for {url} in {rel}")
    # svg references
    for p, parser in pages.items():
        rel = p.relative_to(PUBLIC).as_posix()
        for kind, url in parser.links:
            if url.startswith("/notes/excalidraw/") and not exists(url):
                failures.append(f"missing drawing {url} in {rel}")
    seen = set()
    for f in failures:
        if f not in seen:
            seen.add(f)
            print("FAIL", f)
    print(f"check_public: {len(pages)} pages, {len(seen)} failure(s)")
    return 1 if seen else 0


if __name__ == "__main__":
    sys.exit(main())
