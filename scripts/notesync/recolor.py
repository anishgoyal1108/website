"""Port of the vault's `Excalidraw/Scripts/Catppuccin Recolor.md` (convert direction only).

Maps every element colour of a drawing to the Catppuccin Mocha template palette
the same way the Obsidian script does: default ink to ink, canvas to canvas,
same-named Excalidraw palette colours to the same shade, neutrals by lightness
and accents by nearest hue after undoing Excalidraw's dark-mode filter.
"""
from __future__ import annotations

import json
import math
import re
from pathlib import Path

NEUTRAL_CHROMA = 0.05
PASTEL_DELTA_L = 0.22
NEUTRAL_NAMES = {"text", "surface", "gray", "grey", "neutral", "black", "white"}
SECONDARY_PENALTY = 8
SECONDARY_ACCENTS = {"maroon", "sapphire", "lavender", "bronze", "orange", "cyan", "violet"}
EX_INK = "#1e1e1e"

EX = {
    "transparent": "transparent", "black": "#1e1e1e", "white": "#ffffff",
    "gray": ["#f8f9fa", "#e9ecef", "#ced4da", "#868e96", "#343a40"],
    "red": ["#fff5f5", "#ffc9c9", "#ff8787", "#fa5252", "#e03131"],
    "pink": ["#fff0f6", "#fcc2d7", "#f783ac", "#e64980", "#c2255c"],
    "grape": ["#f8f0fc", "#eebefa", "#da77f2", "#be4bdb", "#9c36b5"],
    "violet": ["#f3f0ff", "#d0bfff", "#9775fa", "#7950f2", "#6741d9"],
    "blue": ["#e7f5ff", "#a5d8ff", "#4dabf7", "#228be6", "#1971c2"],
    "cyan": ["#e3fafc", "#99e9f2", "#3bc9db", "#15aabf", "#0c8599"],
    "teal": ["#e6fcf5", "#96f2d7", "#38d9a9", "#12b886", "#099268"],
    "green": ["#ebfbee", "#b2f2bb", "#69db7c", "#40c057", "#2f9e44"],
    "yellow": ["#fff9db", "#ffec99", "#ffd43b", "#fab005", "#f08c00"],
    "orange": ["#fff4e6", "#ffd8a8", "#ffa94d", "#fd7e14", "#e8590c"],
    "bronze": ["#f8f1ee", "#eaddd7", "#d2bab0", "#a18072", "#846358"],
}
EXCALIDRAW_PALETTE = {"elementStroke": EX, "elementBackground": EX, "canvasBackground": {"white": "#ffffff"}}

_HEX = re.compile(r"^#([0-9a-f]{3}|[0-9a-f]{6}|[0-9a-f]{8})$", re.I)


def is_hex(c) -> bool:
    return isinstance(c, str) and bool(_HEX.match(c))


def hex_to_rgb(h: str) -> tuple[float, float, float]:
    s = h.lstrip("#")
    n = "".join(ch * 2 for ch in s) if len(s) == 3 else s[:6]
    v = int(n, 16)
    return ((v >> 16) & 255, (v >> 8) & 255, v & 255)


def _lin(c: float) -> float:
    c /= 255
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def oklch(rgb) -> tuple[float, float, float]:
    r, g, b = rgb
    lr, lg, lb = _lin(r), _lin(g), _lin(b)
    l = _cbrt(0.4122214708 * lr + 0.5363325363 * lg + 0.0514459929 * lb)
    m = _cbrt(0.2119034982 * lr + 0.6806995451 * lg + 0.1073969566 * lb)
    s = _cbrt(0.0883024619 * lr + 0.2817188376 * lg + 0.6299787005 * lb)
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(a, bb), (math.degrees(math.atan2(bb, a)) + 360) % 360


def _cbrt(x: float) -> float:
    return math.copysign(abs(x) ** (1 / 3), x)


def hue_dist(a: float, b: float) -> float:
    d = abs(a - b) % 360
    return 360 - d if d > 180 else d


def lightness_of(h: str) -> float:
    return oklch(hex_to_rgb(h))[0]


P = 0.93
HR = [[-0.574, 1.430, 0.144], [0.426, 0.430, 0.144], [0.426, 1.430, -0.856]]


def dark_filter(rgb):
    """Excalidraw dark-mode canvas filter: invert(93%) then hue-rotate(180deg), in sRGB."""
    v = [P + (1 - 2 * P) * (x / 255) for x in rgb]
    return [max(0.0, min(1.0, row[0] * v[0] + row[1] * v[1] + row[2] * v[2])) * 255 for row in HR]


def shades_of(entry):
    return entry if isinstance(entry, list) else [entry]


def canonical(entry):
    s = shades_of(entry)
    return s[min(4, len(s) - 1)]


def analyse(palette: dict, canvas_hex: str) -> dict:
    names = list(palette.get("elementStroke", {}).keys()) + list(palette.get("elementBackground", {}).keys())
    has_named_neutrals = any(n.lower() in NEUTRAL_NAMES for n in names)

    def is_neutral(name, hx):
        return name.lower() in NEUTRAL_NAMES if has_named_neutrals else oklch(hex_to_rgb(hx))[1] < NEUTRAL_CHROMA

    neutral_ramp: list[dict] = []
    accents: dict[str, dict] = {}
    lookup: dict[str, dict] = {}
    for kind in ("elementStroke", "elementBackground"):
        for name, entry in (palette.get(kind) or {}).items():
            shades = shades_of(entry)
            for idx, s in enumerate(shades):
                if is_hex(s) and s.lower() not in lookup:
                    lookup[s.lower()] = {"name": name, "idx": idx, "kind": kind}
            if name == "transparent":
                continue
            hx = canonical(entry)
            if not is_hex(hx):
                continue
            if is_neutral(name, hx):
                for s in shades:
                    if is_hex(s):
                        neutral_ramp.append({"hex": s, "L": lightness_of(s)})
            elif oklch(hex_to_rgb(hx))[1] >= NEUTRAL_CHROMA:
                a = accents.setdefault(name, {"stroke": None, "fill": None, "H": oklch(hex_to_rgb(hx))[2]})
                a["stroke" if kind == "elementStroke" else "fill"] = shades
    for a in accents.values():
        a["stroke"] = a["stroke"] or a["fill"]
        a["fill"] = a["fill"] or a["stroke"]
    neutral_ramp.append({"hex": canvas_hex, "L": lightness_of(canvas_hex)})
    return {"neutralRamp": neutral_ramp, "accents": accents, "lookup": lookup}


def make_mapper(source: dict, target: dict):
    src = analyse(source["palette"], source["canvas"])
    dst = analyse(target["palette"], target["canvas"])

    def visible(hx):
        return dark_filter(hex_to_rgb(hx)) if source["dark"] else hex_to_rgb(hx)

    visible_canvas_is_light = oklch(visible(source["canvas"]))[0] > 0.5
    target_canvas_is_light = lightness_of(target["canvas"]) > 0.5

    def perceive(hx):
        return dark_filter(visible(hx)) if visible_canvas_is_light != target_canvas_is_light else visible(hx)

    canvas_l = oklch(perceive(source["canvas"]))[0]
    cache: dict[str, str] = {}

    def pick_shade(arr, idx):
        return arr[min(idx, len(arr) - 1)]

    def map_color(color, role):
        if not is_hex(color):
            return color
        key = role + "|" + color.lower()
        if key in cache:
            return cache[key]
        alpha = color[7:] if len(color) == 9 else ""
        base6 = color[:7].lower()
        known = src["lookup"].get(base6)
        if source.get("ink") and target.get("ink") and base6 == source["ink"].lower():
            out = target["ink"] + alpha
        elif base6 == source["canvas"].lower():
            out = target["canvas"] + alpha
        elif base6 in dst["lookup"]:
            out = color
        elif known and known["name"] in dst["accents"]:
            a = dst["accents"][known["name"]]
            out = pick_shade(a["fill"] if role == "fill" else a["stroke"], known["idx"]) + alpha
        else:
            L, C, H = oklch(perceive(base6))
            neutral = C < NEUTRAL_CHROMA or (known is not None and known["name"].lower() in NEUTRAL_NAMES)
            accent_list = list(dst["accents"].items())
            if neutral or not accent_list:
                best = dst["neutralRamp"][0]
                for n in dst["neutralRamp"]:
                    if abs(n["L"] - L) < abs(best["L"] - L):
                        best = n
                out = best["hex"] + alpha
            else:
                best = None
                best_score = math.inf
                for name, a in accent_list:
                    score = hue_dist(H, a["H"]) + (SECONDARY_PENALTY if name in SECONDARY_ACCENTS else 0)
                    if score < best_score:
                        best_score, best = score, a
                if role == "fill":
                    out = (pick_shade(best["fill"], 1) if abs(L - canvas_l) < PASTEL_DELTA_L else pick_shade(best["fill"], 4)) + alpha
                else:
                    out = pick_shade(best["stroke"], 4) + alpha
        cache[key] = out
        return out

    return map_color


class Catppuccin:
    def __init__(self, template_json: Path):
        tpl = json.loads(template_json.read_text())
        self.palette = tpl["colorPalette"]
        self.canvas = tpl.get("viewBackgroundColor") or "#1e1e2e"
        self.ink = tpl.get("currentItemStrokeColor") or "#cdd6f4"

    def is_catppuccin(self, scene: dict) -> bool:
        st = scene.get("appState", {})
        vb = st.get("viewBackgroundColor")
        canvas_now = vb if vb and vb != "transparent" else "#ffffff"
        els = [e for e in scene.get("elements", []) if not e.get("isDeleted")]
        return any((e.get("customData") or {}).get("ctpDoc") or (e.get("customData") or {}).get("ctp") for e in els) \
            or (st.get("theme") == "light" and canvas_now.lower() == self.canvas.lower())

    def mapper(self, scene: dict):
        st = scene.get("appState", {})
        vb = st.get("viewBackgroundColor")
        canvas_now = vb if vb and vb != "transparent" else "#ffffff"
        return make_mapper(
            {"palette": st.get("colorPalette") or EXCALIDRAW_PALETTE, "dark": st.get("theme") == "dark",
             "canvas": canvas_now, "ink": None if st.get("colorPalette") else EX_INK},
            {"palette": self.palette, "canvas": self.canvas, "ink": self.ink},
        )

    def recolor(self, scene: dict) -> tuple[dict, int]:
        """Return (new scene, elements changed). Image elements are never touched."""
        if self.is_catppuccin(scene):
            return scene, 0
        map_color = self.mapper(scene)
        changed = 0
        elements = []
        for el in scene.get("elements", []):
            if el.get("isDeleted") or el.get("type") == "image":
                elements.append(el)
                continue
            stroke = map_color(el.get("strokeColor"), "stroke")
            fill = map_color(el.get("backgroundColor"), "fill")
            if stroke != el.get("strokeColor") or fill != el.get("backgroundColor"):
                el = dict(el, strokeColor=stroke, backgroundColor=fill)
                changed += 1
            elements.append(el)
        st = dict(scene.get("appState", {}))
        st.update(theme="light", viewBackgroundColor=self.canvas, colorPalette=self.palette,
                  currentItemStrokeColor=self.ink)
        return dict(scene, elements=elements, appState=st), changed

    def recolor_tex(self, tex: str, scene: dict) -> str:
        """Map `\\color{#hex}` in a TeX embed through the same mapper; uncoloured TeX gets the ink colour."""
        if self.is_catppuccin(scene):
            map_color = None
        else:
            map_color = self.mapper(scene)

        def sub(m):
            c = m.group(1)
            return "\\color{" + (map_color(c, "stroke") if map_color else c) + "}"

        if re.search(r"\\color\{#[0-9a-fA-F]{3,8}\}", tex):
            return re.sub(r"\\color\{(#[0-9a-fA-F]{3,8})\}", sub, tex)
        return "\\color{" + self.ink + "} " + tex
