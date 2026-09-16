"""Decode, recolor and render Excalidraw drawings to SVG (Playwright via render_excalidraw.mjs)."""
from __future__ import annotations

import base64
import hashlib
import json
import mimetypes
import re
import shutil
import subprocess
from pathlib import Path

from . import config as cfglib
from . import excalidraw as exlib
from .recolor import Catppuccin

TEMPLATE = Path(__file__).resolve().parent / "catppuccin_mocha.json"


def _scene_cache(cache_dir: Path, src: Path) -> dict:
    """Decoded scene JSON cached by mtime+size (LZ decoding is slow in pure Python)."""
    key = hashlib.sha1(f"{src}|{src.stat().st_mtime_ns}|{src.stat().st_size}".encode()).hexdigest()
    cp = cache_dir / "scenes" / f"{key}.json"
    if cp.exists():
        return json.loads(cp.read_text())
    d = exlib.parse(src)
    data = {"scene": d.scene, "embedded": d.embedded, "name": d.name}
    cp.parent.mkdir(parents=True, exist_ok=True)
    cp.write_text(json.dumps(data))
    return data


def build_job(cfg, vault, slug: str, src: Path, scrubber, ctp: Catppuccin, report) -> dict | None:
    data = _scene_cache(cfglib.CACHE_DIR, src)
    scene = data["scene"]
    embedded: dict[str, str] = data["embedded"]
    scene2, changed = ctp.recolor(scene)
    files = {}
    for fid, ref in embedded.items():
        if ref.startswith("$$"):
            tex = ref.strip()
            if tex.startswith("$$") and tex.endswith("$$"):
                tex = tex[2:-2].strip()
            files[fid] = {"kind": "tex", "tex": ctp.recolor_tex(tex, scene)}
        else:
            m = re.match(r"^\[\[([^\]|#]+)", ref)
            if not m:
                continue
            base = m.group(1).strip().rsplit("/", 1)[-1]
            if base.lower().endswith(".pdf") or "#" in base:
                report.add("drawing pdf embeds skipped", f"{slug}: {base}")
                continue
            ip = vault.images.get(base.lower())
            if ip is None:
                report.add("missing drawing images", f"{slug}: {base}")
                continue
            mime = mimetypes.guess_type(ip.name)[0] or "image/png"
            files[fid] = {"kind": "image", "dataURL": f"data:{mime};base64," + base64.b64encode(ip.read_bytes()).decode()}
    # name scrub on text elements
    els = []
    for e in scene2.get("elements", []):
        if e.get("type") == "text":
            e = dict(e)
            for k in ("text", "originalText", "rawText"):
                if isinstance(e.get(k), str):
                    e[k] = scrubber.scrub(e[k], f"drawing:{slug}")
        els.append(e)
    scene2 = dict(scene2, elements=els)
    for fid, f in files.items():
        if f["kind"] == "tex":
            f["tex"] = scrubber.scrub(f["tex"], f"drawing:{slug}")
    payload = {"slug": slug, "elements": [e for e in els if not e.get("isDeleted")],
               "appState": {k: v for k, v in scene2.get("appState", {}).items()
                            if k in ("theme", "viewBackgroundColor", "gridSize", "colorPalette")},
               "files": files}
    payload["appState"]["viewBackgroundColor"] = ctp.canvas
    payload["appState"]["theme"] = "light"
    digest = hashlib.sha256(json.dumps(payload, sort_keys=True).encode()).hexdigest()
    payload["digest"] = digest
    report.bump("drawings recolored elements", changed)
    return payload


def render_all(cfg, vault, media, scrubber, report, args) -> list[Path]:
    """Return the list of SVG paths that should exist in static/notes/excalidraw."""
    out_dir = cfg.static_excalidraw
    svg_cache = cfglib.CACHE_DIR / "svg"
    svg_cache.mkdir(parents=True, exist_ok=True)
    ctp = Catppuccin(TEMPLATE)
    wanted: list[Path] = []
    jobs: list[dict] = []
    for slug, src in sorted(media.drawings_used.items()):
        dest = out_dir / f"{slug}.svg"
        wanted.append(dest)
        job = build_job(cfg, vault, slug, src, scrubber, ctp, report)
        if job is None:
            continue
        cached = svg_cache / f"{slug}.svg"
        if not args.force_render and cached.exists():
            head = cached.read_text(encoding="utf-8", errors="replace")[:200]
            if f"scene:{job['digest']}" in head:
                if not args.dry_run:
                    out_dir.mkdir(parents=True, exist_ok=True)
                    if not dest.exists() or dest.read_bytes() != cached.read_bytes():
                        shutil.copyfile(cached, dest)
                continue
        jobs.append(job)
    report.bump("drawings referenced", len(wanted))
    report.bump("drawings to render", len(jobs))
    if not jobs or args.dry_run:
        return wanted
    if args.no_excalidraw:
        for j in jobs:
            report.add("drawings not rendered (--no-excalidraw)", j["slug"])
        return wanted
    manifest = cfglib.CACHE_DIR / "render-manifest.json"
    manifest.write_text(json.dumps({"out": str(svg_cache), "jobs": jobs}))
    script = cfglib.SCRIPTS / "render_excalidraw.mjs"
    proc = subprocess.run(["node", str(script), str(manifest)], cwd=str(cfglib.SCRIPTS), text=True,
                          capture_output=True)
    if proc.returncode != 0:
        report.add("render errors", proc.stderr[-2000:])
        raise SystemExit(f"excalidraw render failed:\n{proc.stderr[-4000:]}")
    for line in proc.stdout.splitlines():
        if line.startswith("rendered "):
            report.bump("drawings rendered")
        elif line.startswith("failed "):
            report.add("drawings failed", line[7:])
    out_dir.mkdir(parents=True, exist_ok=True)
    for j in jobs:
        cached = svg_cache / f"{j['slug']}.svg"
        if cached.exists():
            svg = cached.read_text(encoding="utf-8")
            if not svg.startswith("<!-- scene:"):
                svg = _postprocess(svg, j["digest"])
                cached.write_text(svg, encoding="utf-8")
            shutil.copyfile(cached, out_dir / f"{j['slug']}.svg")
    return wanted


def _round_numbers(svg: str) -> str:
    """Round path/point coordinates to 0.1 px; Excalidraw exports 3-4 decimals of freedraw outline."""
    def rnd(m):
        r = round(float(m.group(0)), 1)
        return str(int(r)) if r == int(r) else f"{r:.1f}"

    def fix(m):
        return m.group(1) + re.sub(r"-?\d+\.\d+", rnd, m.group(2)) + '"'

    svg = re.sub(r'(\sd=")([^"]*)"', fix, svg)
    svg = re.sub(r'(\spoints=")([^"]*)"', fix, svg)
    svg = re.sub(r'(\stransform=")([^"]*)"', fix, svg)
    return svg


def _postprocess(svg: str, digest: str) -> str:
    svg = re.sub(r"<!--\s*payload-(?:type|version|start|end)[\s\S]*?-->", "", svg)
    svg = re.sub(r"<!--\s*svg-source:excalidraw\s*-->", "", svg)
    svg = re.sub(r"<!--\s*payload:[\s\S]*?-->", "", svg)
    svg = re.sub(r"<\?xml[^>]*\?>\s*", "", svg)
    svg = re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg)
    svg = _round_numbers(svg)
    return f"<!-- scene:{digest} -->\n" + svg.strip() + "\n"
