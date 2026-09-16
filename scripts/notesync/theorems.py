"""Index of theorem callouts, labelled equations and block references.

Numbers are assigned the way math-booster ("LaTeX-like Theorem & Equation
Referencer" v2.2.0, profile "English") does:

* a theorem-type callout without metadata is auto-numbered per note, in
  document order, starting at 1; `[!type|*]` has no number and does not use
  the counter; `[!type|N]` shows N literally;
* the number prefix is the leading number of the note title plus ".", so a
  note called "01 Ray Optics" yields "Theorem 01.1";
* a `$$` block followed by `^id` is an equation; it is numbered only if some
  `[[…#^id]]` link to it exists anywhere in the vault (numberOnlyReferencedEquations);
* `%% display: … %%` names an equation for links, `%% main %%` marks a note's
  main theorem (used as link text for `[[Note]]`).
"""
from __future__ import annotations

import re
from dataclasses import dataclass, field

from .config import Config
from .textproc import heading_id, is_fence, strip_fenced
from .vault import Note, Vault, resolve_note

THEOREM_TYPES = ["axiom", "definition", "lemma", "proposition", "theorem", "corollary", "claim",
                 "assumption", "example", "exercise", "conjecture", "hypothesis", "remark"]
THEOREM_PREFIXES = ["axm", "def", "lem", "prp", "thm", "cor", "clm", "asm", "exm", "exr", "cnj", "hyp", "rmk"]
PREFIX_TO_TYPE = dict(zip(THEOREM_PREFIXES, THEOREM_TYPES))
PROFILE_EN = {
    "axiom": "Axiom", "definition": "Definition", "lemma": "Lemma", "proposition": "Proposition",
    "theorem": "Theorem", "corollary": "Corollary", "claim": "Claim", "assumption": "Assumption",
    "example": "Example", "exercise": "Exercise", "conjecture": "Conjecture", "hypothesis": "Hypothesis",
    "remark": "Remark",
}
PROOF = {"begin": "Proof.", "end": "", "linkedBeginPrefix": "Proof of ", "linkedBeginSuffix": "."}

CALLOUT_RE = re.compile(r"^>\s*\[!\s*([A-Za-z0-9_-]+)\s*(?:\|([^\]]*))?\]([+-])?(?:[ \t]+(.*?))?\s*$")
BLOCK_ID_RE = re.compile(r"^\^([A-Za-z0-9-]+)\s*$")
TRAIL_ID_RE = re.compile(r"^(.*\S)\s+\^([A-Za-z0-9-]+)\s*$")
DISPLAY_RE = re.compile(r"^\s*%%\s*display:\s*(.*?)\s*%%\s*$")
MANUAL_TAG_RE = re.compile(r"\\tag\{(.*?)\}")
NUMBER_PREFIX_RE = re.compile(r"^[0-9]+(\.[0-9]+)*")
REF_RE = re.compile(r"!?\[\[([^\]\|#]*)#\^([A-Za-z0-9-]+)(?:\|[^\]]*)?\]\]")
BLOCK_STARTS = re.compile(r"^(\s*([-*+]|\d+[.)])\s|#{1,6}\s|\$\$|\||```|~~~|\^[A-Za-z0-9-]+\s*$|<|!\[\[|---\s*$)")


@dataclass
class Theorem:
    note: Note
    line: int                 # absolute body line of the callout header
    end: int                  # last line of the run (inclusive)
    type: str
    meta: str                 # raw metadata ("" | "*" | literal)
    title: str | None
    fold: str
    number: str | None = None # e.g. "01.1", None when unnumbered
    label: str | None = None  # ^id following the callout
    main: bool = False
    display: str | None = None

    @property
    def type_name(self) -> str:
        return PROFILE_EN.get(self.type, self.type.capitalize())

    @property
    def main_title(self) -> str:
        return f"{self.type_name} {self.number}" if self.number else self.type_name

    @property
    def full_title(self) -> str:
        t = self.main_title
        if self.title:
            t += f" ({self.title})"
        return t + "."

    @property
    def ref_name(self) -> str:
        if self.display:
            return self.display
        return self.title if self.title else self.main_title


@dataclass
class Equation:
    note: Note
    line: int                 # line of the opening $$
    end: int                  # line of the closing $$
    label: str
    math: str                 # math text without the display comment
    display: str | None = None
    manual_tag: str | None = None
    number: str | None = None # printed number without parentheses

    @property
    def print_name(self) -> str | None:
        return f"({self.number})" if self.number else None

    @property
    def ref_name(self) -> str | None:
        return self.display or self.print_name


@dataclass
class NoteIndex:
    theorems: dict[int, Theorem] = field(default_factory=dict)      # by header line
    equations: dict[int, Equation] = field(default_factory=dict)    # by opening line
    labels: dict[str, object] = field(default_factory=dict)         # ^id -> Theorem | Equation | ("block", line)
    headings: dict[str, str] = field(default_factory=dict)          # heading text (lower) -> id
    heading_lines: dict[int, tuple[int, str]] = field(default_factory=dict)  # line -> (level, id)
    main: Theorem | None = None


class RefIndex:
    def __init__(self, cfg: Config, vault: Vault):
        self.cfg = cfg
        self.vault = vault
        self.notes: dict[str, NoteIndex] = {}
        self.backlinks: set[tuple[str, str]] = set()
        self.strip_zeros = bool(cfg.parity.get("strip_leading_zeros", False))
        self.star_main = bool(cfg.parity.get("star_marks_main", False))
        self.only_referenced = bool(cfg.parity.get("equation_numbers_only_when_referenced", True))

    # ------------------------------------------------------------------ build
    def build(self, report):
        self._scan_references()
        for note in self.vault.notes:
            self.notes[note.rel] = self._index_note(note)
        report.bump("theorem callouts", sum(len(n.theorems) for n in self.notes.values()))
        report.bump("labelled equations", sum(len(n.equations) for n in self.notes.values()))
        report.bump("numbered equations", sum(1 for n in self.notes.values() for e in n.equations.values() if e.number))

    def _scan_references(self):
        vault = self.vault
        seen_paths = set()
        for paths in vault.all_md.values():
            for p in paths:
                rel = p.relative_to(vault.cfg.vault).as_posix()
                if not any(rel.startswith(d) for d in self.cfg.scan_dirs):
                    continue
                if rel in seen_paths:
                    continue
                seen_paths.add(rel)
                try:
                    text = p.read_text(encoding="utf-8", errors="replace")
                except OSError:
                    continue
                if "#^" not in text:
                    continue
                src = vault.by_path.get(rel)
                for m in REF_RE.finditer(strip_fenced(text)):
                    target, bid = m.group(1).strip(), m.group(2)
                    if target == "":
                        if src is not None:
                            self.backlinks.add((src.rel, bid))
                        continue
                    n = resolve_note(vault, target, src)
                    if n is not None:
                        self.backlinks.add((n.rel, bid))

    def number_prefix(self, note: Note) -> str:
        m = NUMBER_PREFIX_RE.match(note.prefix_source)
        if not m:
            return ""
        prefix = m.group(0).strip()
        if self.strip_zeros:
            prefix = ".".join(str(int(x)) for x in prefix.split("."))
        if not prefix.endswith("."):
            prefix += "."
        return prefix

    def _index_note(self, note: Note) -> NoteIndex:
        idx = NoteIndex()
        lines = note.body.split("\n")
        prefix = self.number_prefix(note)
        auto = 0
        eq_count = 0
        used_ids: dict[str, int] = {}
        i = 0
        n = len(lines)
        in_fence = None
        last_block_end = None  # (kind, start, end)
        while i < n:
            line = lines[i]
            if in_fence:
                if is_fence(line, in_fence):
                    in_fence = None
                i += 1
                continue
            f = is_fence(line)
            if f:
                in_fence = f
                i += 1
                continue
            hm = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if hm:
                hid = heading_id(hm.group(2), used_ids)
                idx.headings.setdefault(hm.group(2).strip().lower(), hid)
                idx.heading_lines[i] = (len(hm.group(1)), hid)
                last_block_end = ("heading", i, i)
                i += 1
                continue
            cm = CALLOUT_RE.match(line)
            if cm and not line.startswith("> >"):
                end = callout_run_end(lines, i)
                ctype = cm.group(1).lower()
                if ctype in PREFIX_TO_TYPE:
                    ctype = PREFIX_TO_TYPE[ctype]
                if ctype in THEOREM_TYPES:
                    meta = (cm.group(2) or "").strip()
                    th = Theorem(note=note, line=i, end=end, type=ctype, meta=meta,
                                 title=(cm.group(4) or "").strip() or None, fold=cm.group(3) or "")
                    body_text = "\n".join(lines[i + 1:end + 1])
                    for c in re.findall(r"%%\s*(.*?)\s*%%", body_text):
                        c = c.strip()
                        if c == "main":
                            th.main = True
                        elif c.lower().startswith("display:"):
                            th.display = c.split(":", 1)[1].strip()
                    if meta == "":
                        th.number = f"{prefix}{auto + 1}"
                        auto += 1
                    elif meta == "*":
                        th.number = None
                        if self.star_main:
                            th.main = True
                    else:
                        th.number = meta
                    if th.main and idx.main is None:
                        idx.main = th
                    idx.theorems[i] = th
                    last_block_end = ("theorem", i, end)
                else:
                    last_block_end = ("callout", i, end)
                i = end + 1
                continue
            if line.startswith("$$"):
                end = math_block_end(lines, i)
                raw = lines[i:end + 1]
                inner = "\n".join(raw)
                inner = inner[2:]
                if inner.rstrip().endswith("$$"):
                    inner = inner.rstrip()[:-2]
                display = None
                kept = []
                for l in inner.split("\n"):
                    dm = DISPLAY_RE.match(l)
                    if dm:
                        display = dm.group(1)
                    else:
                        kept.append(l)
                math = "\n".join(kept).strip("\n")
                mt = MANUAL_TAG_RE.search(math)
                label = lookahead_label(lines, end)
                if label:
                    eq = Equation(note=note, line=i, end=end, label=label, math=math, display=display,
                                  manual_tag=mt.group(1) if mt else None)
                    if eq.manual_tag:
                        eq.number = eq.manual_tag
                    elif not self.only_referenced or (note.rel, label) in self.backlinks:
                        eq.number = f"{prefix}{eq_count + 1}"
                        eq_count += 1
                    idx.equations[i] = eq
                    idx.labels[label] = eq
                last_block_end = ("math", i, end)
                i = end + 1
                continue
            bm = BLOCK_ID_RE.match(line)
            if bm:
                label = bm.group(1)
                if last_block_end and last_block_end[0] == "theorem":
                    th = idx.theorems[last_block_end[1]]
                    if th.label is None:
                        th.label = label
                    idx.labels[label] = th
                elif last_block_end and last_block_end[0] == "math":
                    pass  # already attached by lookahead
                elif last_block_end:
                    idx.labels.setdefault(label, ("block", last_block_end[1]))
                i += 1
                continue
            tm = TRAIL_ID_RE.match(line)
            if tm and not line.lstrip().startswith("$$"):
                idx.labels.setdefault(tm.group(2), ("block", i))
            if line.strip():
                if last_block_end and last_block_end[0] == "text" and last_block_end[2] == i - 1:
                    last_block_end = ("text", last_block_end[1], i)
                else:
                    last_block_end = ("text", i, i)
            i += 1
        return idx

    # ------------------------------------------------------------------ lookup
    def note_index(self, note: Note) -> NoteIndex:
        return self.notes[note.rel]

    def lookup_label(self, note: Note, label: str):
        return self.notes.get(note.rel, NoteIndex()).labels.get(label)

    def note_link_text(self, note: Note) -> str:
        """Text for [[Note]]: the main theorem's ref name if the note has one, else the title."""
        idx = self.notes.get(note.rel)
        if idx and idx.main:
            return idx.main.ref_name
        return note.title if note.kind != "concept" else note.name

    def ref_text(self, target: Note, label: str, from_note: Note | None) -> tuple[str | None, str]:
        """Return (link text, kind) for [[target#^label]]. kind: theorem|equation|block|unknown."""
        obj = self.lookup_label(target, label)
        sep = self.cfg.parity.get("cross_note_prefix", " > ")
        cross = from_note is None or target.rel != from_note.rel
        if isinstance(obj, Theorem):
            text = obj.ref_name
            return (f"{target.title}{sep}{text}" if cross else text), "theorem"
        if isinstance(obj, Equation):
            text = obj.ref_name
            if text is None:
                return (target.title if cross else "equation"), "equation"
            return (f"{target.title}{sep}{text}" if cross else text), "equation"
        if isinstance(obj, tuple):
            return target.title, "block"
        return None, "unknown"


# ---------------------------------------------------------------------- helpers
def callout_run_end(lines: list[str], start: int) -> int:
    """Index of the last line belonging to the blockquote/callout starting at `start`.

    Continues on `>` lines and on lazy paragraph continuation lines (a non-blank
    line that does not start a new block), which Obsidian renders inside the callout.
    """
    i = start
    n = len(lines)
    last = start
    in_math = False
    while i < n:
        line = lines[i]
        if line.lstrip().startswith(">"):
            body = line.lstrip()[1:].lstrip()
            if body.count("$$") % 2 == 1:
                in_math = not in_math
            last = i
            i += 1
            continue
        if in_math and line.strip():
            last = i
            i += 1
            continue
        if line.strip() and not BLOCK_STARTS.match(line) and lines[last].lstrip().startswith(">"):
            prev = lines[last].lstrip()[1:].strip()
            if prev and not prev.endswith("$$") and not prev.startswith("$$") and not prev.startswith("```"):
                last = i
                i += 1
                continue
        break
    return last


def math_block_end(lines: list[str], start: int) -> int:
    first = lines[start]
    if len(first.strip()) > 2 and first.strip().endswith("$$") and first.strip().count("$$") >= 2:
        return start
    i = start + 1
    while i < len(lines):
        if "$$" in lines[i]:
            return i
        i += 1
    return len(lines) - 1


def lookahead_label(lines: list[str], end: int) -> str | None:
    j = end + 1
    while j < len(lines) and not lines[j].strip():
        j += 1
    if j < len(lines):
        m = BLOCK_ID_RE.match(lines[j])
        if m:
            return m.group(1)
    return None
