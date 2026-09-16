"""Render one vault note body into Hugo markdown with Obsidian-parity HTML."""
from __future__ import annotations

import html
import re
from dataclasses import dataclass, field

from . import icons
from .citations import Citations
from .config import Config
from .media import Media, is_excalidraw_name, is_image_name
from .textproc import Protector, is_fence
from .theorems import (BLOCK_ID_RE, CALLOUT_RE, PROOF, TRAIL_ID_RE, Equation, RefIndex, Theorem,
                       callout_run_end, lookahead_label, math_block_end)
from .vault import Note, Vault, resolve_note

EMBED_RE = re.compile(r"!\[\[([^\]]+?)\]\]")
LINK_RE = re.compile(r"(?<!!)\[\[([^\]]+?)\]\]")
HIGHLIGHT_RE = re.compile(r"==(?=\S)(.+?)(?<=\S)==")
PROOF_BEGIN_RE = re.compile(r"`\\begin\{proof\}`(?:@((?:\[\[[^\]]+\]\])(?:\s+AND\s+\[\[[^\]]+\]\])*))?")
PROOF_END_RE = re.compile(r"`\\end\{proof\}`")
YOUTUBE_RE = re.compile(r"!\[\]\((https?://(?:www\.)?(?:youtube\.com|youtu\.be)/[^)\s]+)\)")
REMOTE_IMG_RE = re.compile(r"!\[([^\]]*)\]\((https?://[^)\s]+)\)")
HEADING_RE = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
LIST_RE = re.compile(r"^(\s*)([-*+]|\d+[.)])\s+")
DEFAULT_TITLES = {"tldr": "TL;DR", "faq": "FAQ"}


@dataclass
class Ctx:
    note: Note                    # note whose text is being rendered (link resolution context)
    host: Note                    # page being emitted (collects links/sources)
    depth: int = 0
    stack: tuple = ()
    embed_seq: list = field(default_factory=lambda: [0])
    in_embed: bool = False


def _split_wikilink(inner: str) -> tuple[str, str | None, str | None]:
    """'Target#frag|alias' -> (target, frag, alias). Handles the table-escaped \\| alias."""
    inner = inner.replace("\\|", "\x01")
    alias = None
    if "|" in inner:
        inner, alias = inner.split("|", 1)
        alias = alias.replace("\x01", "|")
    inner = inner.replace("\x01", "|")
    frag = None
    if "#" in inner:
        inner, frag = inner.split("#", 1)
    return inner.strip(), (frag.strip() if frag is not None else None), (alias.strip() if alias is not None else None)


def _indent_cols(prefix: str) -> int:
    col = 0
    for ch in prefix:
        col = (col // 4 + 1) * 4 if ch == "\t" else col + 1
    return col


class Renderer:
    def __init__(self, cfg: Config, vault: Vault, index: RefIndex, media: Media, cites: Citations, report, scrubber):
        self.cfg = cfg
        self.vault = vault
        self.index = index
        self.media = media
        self.cites = cites
        self.report = report
        self.scrub = scrubber
        self.proof_end = cfg.parity.get("proof_end", PROOF["end"])

    # ================================================================== entry
    def render_note(self, note: Note) -> str:
        lines = note.body.split("\n")
        numbered = list(enumerate(lines))
        # drop a leading H1 equal to the title / name
        for k, (_, t) in enumerate(numbered):
            if not t.strip():
                continue
            m = HEADING_RE.match(t)
            if m and len(m.group(1)) == 1 and m.group(2).strip().lower() in (note.title.lower(), note.name.lower()):
                numbered = numbered[k + 1:]
            break
        ctx = Ctx(note=note, host=note)
        out = self.render_lines(numbered, ctx)
        text = "\n".join(out)
        text = re.sub(r"\n{3,}", "\n\n", text).strip("\n") + "\n"
        return self.scrub.scrub(text, note.rel)

    # ================================================================== structure
    def render_lines(self, L: list[tuple[int, str]], ctx: Ctx) -> list[str]:
        out: list[str] = []
        texts = [t for _, t in L]
        i = 0
        n = len(L)
        last_html_block = False   # previous emitted block carried its own id
        fence = None

        def push_block(block: list[str]):
            if out and out[-1].strip():
                out.append("")
            out.extend(block)
            out.append("")

        while i < n:
            ln, text = L[i]
            if fence:
                out.append(text)
                if is_fence(text, fence):
                    fence = None
                i += 1
                continue
            f = is_fence(text)
            if f:
                fence = f
                out.append(text)
                i += 1
                continue
            stripped = text.lstrip()
            # ---- callouts and blockquotes
            if stripped.startswith(">") and not text.startswith((" ", "\t")):
                end = callout_run_end(texts, i)
                run = L[i:end + 1]
                cm = CALLOUT_RE.match(text)
                if cm:
                    block = self.render_callout(run, cm, ctx)
                else:
                    block = self.render_blockquote(run, ctx)
                push_block(block)
                last_html_block = True
                i = end + 1
                # consume a directly following ^id (already applied to the block)
                j = i
                while j < n and not L[j][1].strip():
                    j += 1
                if j < n and BLOCK_ID_RE.match(L[j][1]):
                    i = j + 1
                continue
            # ---- display math blocks
            if stripped.startswith("$$"):
                end = math_block_end(texts, i)
                indent = text[: len(text) - len(stripped)]
                block, labelled = self.render_math(L[i:end + 1], ctx, indent)
                if indent:
                    out.extend(block)
                else:
                    push_block(block)
                last_html_block = labelled
                i = end + 1
                if labelled:
                    j = i
                    while j < n and not L[j][1].strip():
                        j += 1
                    if j < n and BLOCK_ID_RE.match(L[j][1]):
                        i = j + 1
                continue
            # ---- headings
            hm = HEADING_RE.match(text)
            if hm:
                hid = self.heading_id_for(ctx, ln)
                title = self.inline(hm.group(2), ctx)
                out.append(f"{hm.group(1)} {title} {{#{hid}}}" if hid else f"{hm.group(1)} {title}")
                last_html_block = False
                i += 1
                continue
            # ---- standalone block id
            bm = BLOCK_ID_RE.match(text)
            if bm:
                if not last_html_block and not ctx.in_embed:
                    out.append(f"{{#blk-{bm.group(1)}}}")
                i += 1
                continue
            # ---- note transclusions (non-media embeds)
            em = self.find_note_embed(text)
            if em:
                pre, target_inner, post = em
                block = self.render_transclusion(target_inner, ctx)
                lm = LIST_RE.match(pre)
                if lm and pre.strip() == lm.group(2):
                    col = _indent_cols(lm.group(1)) + len(lm.group(2)) + 1
                    pad = " " * col
                    first = f"{lm.group(1)}{lm.group(2)} {block[0]}"
                    rest = [pad + b if b else "" for b in block[1:]]
                    push_block([first] + rest)
                else:
                    if pre.strip():
                        out.append(self.inline(pre.rstrip(), ctx))
                    if lm:
                        col = _indent_cols(lm.group(1)) + len(lm.group(2)) + 1
                        pad = " " * col
                        push_block([pad + b if b else "" for b in block])
                    else:
                        push_block(block)
                if post.strip():
                    out.append(self.inline(post.strip(), ctx))
                last_html_block = True
                i += 1
                continue
            # ---- trailing block id on a list item / paragraph line
            tm = TRAIL_ID_RE.match(text)
            if tm and not stripped.startswith("|"):
                body = tm.group(1)
                anchor = "" if ctx.in_embed else f'<span class="block-anchor" id="blk-{tm.group(2)}"></span>'
                lm = LIST_RE.match(body)
                if lm:
                    body = body[: lm.end()] + anchor + body[lm.end():]
                else:
                    body = anchor + body
                out.append(self.inline(body, ctx))
                last_html_block = False
                i += 1
                continue
            # ---- plain line
            rendered = self.inline(text, ctx)
            if rendered != text and self._is_block_html(rendered) and not LIST_RE.match(rendered):
                push_block([rendered])
                last_html_block = False
            else:
                out.append(rendered)
                if text.strip():
                    last_html_block = False
            i += 1
        return out

    @staticmethod
    def _is_block_html(s: str) -> bool:
        t = s.strip()
        return t.startswith(("<figure", "<img", "<div", "<blockquote", "<a class=\"video-link\"")) and t.endswith(">")

    # ================================================================== headings / ids
    def heading_id_for(self, ctx: Ctx, ln: int) -> str | None:
        ni = self.index.note_index(ctx.note)
        info = ni.heading_lines.get(ln)
        if not info:
            return None
        hid = info[1]
        if ctx.in_embed:
            hid = f"{hid}-embed{ctx.embed_seq[0]}"
        return hid

    # ================================================================== callouts
    def render_callout(self, run: list[tuple[int, str]], cm, ctx: Ctx) -> list[str]:
        ln0 = run[0][0]
        ctype = cm.group(1).lower()
        meta = (cm.group(2) or "").strip()
        fold = cm.group(3) or ""
        title_raw = (cm.group(4) or "").strip()
        inner = [(ln, self._strip_quote(t)) for ln, t in run[1:]]
        # first line may carry content after the header on the same line? (Obsidian: no)
        th = self.index.note_index(ctx.note).theorems.get(ln0)
        content = self.render_lines(inner, ctx)
        while content and not content[0].strip():
            content.pop(0)
        while content and not content[-1].strip():
            content.pop()
        classes = ["callout"]
        attrs = [f'data-callout="{html.escape(ctype)}"']
        if meta:
            attrs.append(f'data-callout-metadata="{html.escape(meta, quote=True)}"')
        if fold:
            attrs.append(f'data-callout-fold="{fold}"')
        if isinstance(th, Theorem):
            classes += ["theorem-callout", f"theorem-callout-{th.type}", "theorem-callout-en", "theorem-callout-mathwiki"]
            if th.number:
                attrs.append(f'data-theorem-index="{html.escape(th.number)}"')
            sub = f' <span class="theorem-callout-subtitle">({self.inline(th.title, ctx)})</span>' if th.title else ""
            title_html = (f'<span class="theorem-callout-main-title">{html.escape(th.main_title)}</span>{sub}.')
            if th.label and not ctx.in_embed:
                attrs.append(f'id="blk-{html.escape(th.label)}"')
            elif th.label:
                attrs.append(f'data-embed-of="blk-{html.escape(th.label)}"')
            icon = icons.callout_icon(th.type, True)
        else:
            title_html = self.inline(title_raw, ctx) if title_raw else html.escape(DEFAULT_TITLES.get(ctype, ctype.replace("-", " ").capitalize()))
            icon = icons.callout_icon(ctype, False)
        attr_s = " ".join([f'class="{" ".join(classes)}"'] + attrs)
        title_row = (f'<div class="callout-icon">{icon}</div>'
                     f'<div class="callout-title-inner">{title_html}</div>')
        if fold:
            chev = f'<div class="callout-fold">{icons.LUCIDE["chevron-down"]}</div>'
            openattr = " open" if fold == "+" else ""
            head = [f"<details {attr_s}{openattr}>",
                    f'<summary class="callout-title">{title_row}{chev}</summary>',
                    '<div class="callout-content">', ""]
            tail = ["", "</div>", "</details>"]
        else:
            head = [f"<div {attr_s}>", f'<div class="callout-title">{title_row}</div>', '<div class="callout-content">', ""]
            tail = ["", "</div>", "</div>"]
        return head + content + tail

    @staticmethod
    def _strip_quote(t: str) -> str:
        s = t.lstrip()
        if s.startswith(">"):
            s = s[1:]
            if s.startswith(" "):
                s = s[1:]
            return s
        return t  # lazy continuation line

    def render_blockquote(self, run: list[tuple[int, str]], ctx: Ctx) -> list[str]:
        inner = [(ln, self._strip_quote(t)) for ln, t in run]
        content = self.render_lines(inner, ctx)
        while content and not content[0].strip():
            content.pop(0)
        while content and not content[-1].strip():
            content.pop()
        cls = ' class="proof"' if any("math-booster-begin-proof" in c for c in content) else ""
        return [f"<blockquote{cls}>", ""] + content + ["", "</blockquote>"]

    # ================================================================== math
    def render_math(self, run: list[tuple[int, str]], ctx: Ctx, indent: str) -> tuple[list[str], bool]:
        ln0 = run[0][0]
        eq = self.index.note_index(ctx.note).equations.get(ln0) if not indent else None
        if eq is None:
            raw = [t for _, t in run]
            raw = [t for t in raw if not re.match(r"^\s*%%.*%%\s*$", t)]
            return [self._escape_shortcodes(t) for t in raw], False
        math = eq.math
        if eq.number and not eq.manual_tag:
            math = insert_tag(math, eq.number)
        body = [f"{indent}$$", *[self._escape_shortcodes(x) for x in math.split("\n")], f"{indent}$$"]
        if ctx.in_embed:
            return ['<div class="math-block" data-embed-of="blk-%s">' % html.escape(eq.label), ""] + body + ["", "</div>"], True
        return [f'<div class="math-block" id="blk-{html.escape(eq.label)}">', ""] + body + ["", "</div>"], True

    @staticmethod
    def _escape_shortcodes(s: str) -> str:
        return s.replace("{{<", "{{ <").replace("{{%", "{{ %")

    # ================================================================== transclusion
    def find_note_embed(self, text: str):
        for m in EMBED_RE.finditer(text):
            target, frag, alias = _split_wikilink(m.group(1))
            base = target.rsplit("/", 1)[-1]
            if is_image_name(base) or base.lower().endswith(".pdf") or is_excalidraw_name(self.vault, base):
                continue
            if REMOTE_IMG_RE.match(text):
                continue
            return text[: m.start()], m.group(1), text[m.end():]
        return None

    def render_transclusion(self, inner: str, ctx: Ctx) -> list[str]:
        target, frag, alias = _split_wikilink(inner)
        tnote = resolve_note(self.vault, target, ctx.note) if target else ctx.note
        label = html.escape(alias or target or frag or "")
        if tnote is None:
            self.report.add("unresolved embeds", f"{ctx.host.rel}: ![[{inner}]]")
            return [f'<div class="transclusion missing"><span class="missing-media">(embedded note unavailable: {label})</span></div>']
        key = (tnote.rel, frag or "")
        if key in ctx.stack or (frag is None and any(r == tnote.rel for r, _ in ctx.stack)) or ctx.depth >= 5:
            self.report.add("embed cycles", f"{ctx.host.rel}: ![[{inner}]]")
            return [f'<div class="transclusion missing"><span class="missing-media">(embed cycle: {label})</span></div>']
        lines = tnote.body.split("\n")
        numbered = list(enumerate(lines))
        ni = self.index.note_index(tnote)
        if frag is None:
            for k, (_, t) in enumerate(numbered):
                if not t.strip():
                    continue
                m = HEADING_RE.match(t)
                if m and len(m.group(1)) == 1 and m.group(2).strip().lower() in (tnote.title.lower(), tnote.name.lower()):
                    numbered = numbered[k + 1:]
                break
            href = tnote.url
            src_label = tnote.title
        elif frag.startswith("^"):
            obj = ni.labels.get(frag[1:])
            if isinstance(obj, Theorem):
                numbered = numbered[obj.line:obj.end + 1]
            elif isinstance(obj, Equation):
                numbered = numbered[obj.line:obj.end + 1]
            elif isinstance(obj, tuple):
                numbered = [numbered[obj[1]]]
            else:
                self.report.add("unresolved embeds", f"{ctx.host.rel}: ![[{inner}]] (block id not found)")
                return [f'<div class="transclusion missing"><span class="missing-media">(embedded block unavailable: {label})</span></div>']
            href = f"{tnote.url}#blk-{frag[1:]}"
            src_label = tnote.title
        else:
            hid = ni.headings.get(frag.lower())
            start = None
            for ln, (lvl, h) in ni.heading_lines.items():
                if h == hid:
                    start = ln
                    level = lvl
                    break
            if start is None:
                self.report.add("unresolved embeds", f"{ctx.host.rel}: ![[{inner}]] (heading not found)")
                return [f'<div class="transclusion missing"><span class="missing-media">(embedded section unavailable: {label})</span></div>']
            end = len(lines)
            for ln, (lvl, h) in sorted(ni.heading_lines.items()):
                if ln > start and lvl <= level:
                    end = ln
                    break
            numbered = numbered[start:end]
            href = f"{tnote.url}#{hid}"
            src_label = f"{tnote.title} › {frag}"
        ctx.embed_seq[0] += 1
        sub = Ctx(note=tnote, host=ctx.host, depth=ctx.depth + 1, stack=ctx.stack + ((ctx.note.rel, ""), key),
                  embed_seq=ctx.embed_seq, in_embed=True)
        content = self.render_lines(numbered, sub)
        while content and not content[0].strip():
            content.pop(0)
        while content and not content[-1].strip():
            content.pop()
        if tnote.url not in ctx.host.links and tnote is not ctx.host:
            ctx.host.links.append(tnote.url)
        head = [f'<div class="transclusion" data-source="{html.escape(tnote.rel, quote=True)}">',
                f'<a class="transclusion-source" href="{href}" title="Open {html.escape(src_label, quote=True)}">'
                f'{icons.LUCIDE["link"]}</a>', ""]
        return head + content + ["", "</div>"]

    # ================================================================== inline
    def inline(self, text: str, ctx: Ctx) -> str:
        if not text.strip():
            return text
        in_table = text.lstrip().startswith("|")
        p = Protector()
        # proofs use inline code, so they go before code protection
        text = PROOF_BEGIN_RE.sub(lambda m: self._proof_begin(m, ctx), text)
        text = PROOF_END_RE.sub(lambda m: f'<span class="math-booster-end-proof">{html.escape(self.proof_end)}</span>', text)
        text = p.protect_inline(text)
        text = YOUTUBE_RE.sub(lambda m: f'<a class="video-link" href="{html.escape(m.group(1), quote=True)}">▶ Watch on YouTube</a>', text)
        text = EMBED_RE.sub(lambda m: self._embed(m.group(1), ctx, in_table), text)
        text = LINK_RE.sub(lambda m: self._link(m.group(1), ctx, in_table), text)
        text = HIGHLIGHT_RE.sub(lambda m: f"<mark>{m.group(1)}</mark>", text)
        text = p.restore(text)
        text = self._escape_shortcodes(text)
        return text

    def _proof_begin(self, m, ctx: Ctx) -> str:
        refs = m.group(1)
        if not refs:
            return f'<span class="math-booster-begin-proof math-booster-begin-proof-en">{html.escape(PROOF["begin"])}</span>'
        parts = re.split(r"\s+AND\s+", refs)
        rendered = [self._link(pp[2:-2], ctx, False) for pp in parts]
        return (f'<span class="math-booster-begin-proof math-booster-begin-proof-en">{html.escape(PROOF["linkedBeginPrefix"])}'
                f'{" AND ".join(rendered)}{html.escape(PROOF["linkedBeginSuffix"])}</span>')

    def _embed(self, inner: str, ctx: Ctx, in_table: bool) -> str:
        target, frag, alias = _split_wikilink(inner)
        base = target.rsplit("/", 1)[-1]
        if is_image_name(base):
            out = self.media.image(target, alias, in_table)
        elif base.lower().endswith(".pdf"):
            out, plain = self.cites.render(base, frag, self.inline(alias, ctx) if alias else None, embed=True)
            if plain not in ctx.host.sources:
                ctx.host.sources.append(plain)
        elif is_excalidraw_name(self.vault, base):
            out = self.media.excalidraw(base, alias)
        else:
            # a note embed that was not on its own line: render inline-ish
            block = self.render_transclusion(inner, ctx)
            out = "\n".join(block)
        return out.replace("|", "&#124;") if in_table else out

    def _link(self, inner: str, ctx: Ctx, in_table: bool) -> str:
        target, frag, alias = _split_wikilink(inner)
        base = target.rsplit("/", 1)[-1]
        alias_html = self.inline_alias(alias, ctx) if alias else None
        if base.lower().endswith(".pdf"):
            out, plain = self.cites.render(base, frag, alias_html, embed=False)
            if plain not in ctx.host.sources:
                ctx.host.sources.append(plain)
            return out.replace("|", "&#124;") if in_table else out
        if is_image_name(base) or is_excalidraw_name(self.vault, base):
            return alias_html or html.escape(base)
        tnote = resolve_note(self.vault, target, ctx.note) if target else ctx.note
        if tnote is None:
            self.report.add("unresolved links", f"{ctx.host.rel}: [[{inner}]]")
            return alias_html or html.escape(base or frag or inner)
        href = tnote.url
        cls = "internal-link"
        text = None
        if frag is None:
            text = alias_html or html.escape(self.index.note_link_text(tnote))
        elif frag.startswith("^"):
            ref, kind = self.index.ref_text(tnote, frag[1:], ctx.note)
            if kind == "unknown":
                self.report.add("unresolved block links", f"{ctx.host.rel}: [[{inner}]]")
                text = alias_html or html.escape(tnote.title)
            else:
                href = f"{tnote.url}#blk-{frag[1:]}"
                cls += f" ref-{kind}"
                text = alias_html or html.escape(ref)
        else:
            ni = self.index.note_index(tnote)
            hid = ni.headings.get(frag.lower()) or ni.headings.get(frag.strip('"').lower())
            if hid:
                href = f"{tnote.url}#{hid}"
            else:
                self.report.add("unresolved heading links", f"{ctx.host.rel}: [[{inner}]]")
            text = alias_html or html.escape(frag)
        if tnote.url not in ctx.host.links and tnote is not ctx.host:
            ctx.host.links.append(tnote.url)
        out = f'<a class="{cls}" href="{href}">{text}</a>'
        return out.replace("|", "&#124;") if in_table else out

    def inline_alias(self, alias: str, ctx: Ctx) -> str:
        """Alias text: math stays raw for MathJax (MathLinks parity); markdown emphasis is kept."""
        p = Protector()
        t = p.protect_inline(alias)
        t = html.escape(t, quote=False)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
        t = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", t)
        t = re.sub(r"(?<![`\w])_(.+?)_(?![`\w])", r"<em>\1</em>", t)
        return p.restore(t)


def insert_tag(math: str, tag: str) -> str:
    """math-booster's insertTagInMathText with lineByLine=true."""
    m = re.match(r"^\s*\\begin\{align\}([\s\S]*)\\end\{align\}\s*$", math)
    if not m:
        return math + f"\\tag{{{tag}}}"
    stack: list[str] = []
    content = "\n".join(_non_comment(l) for l in m.group(1).split("\n"))
    idx = 1
    parts = []
    for line in content.split("\\\\"):
        for w, env in re.findall(r"\\(begin|end)\{(.*?)\}", line):
            if w == "begin":
                stack.append(env)
            elif stack and stack[-1] == env:
                stack.pop()
        if stack or not line.strip() or "\\nonumber" in line:
            parts.append(line)
        else:
            parts.append(line + f"\\tag{{{tag}-{idx}}}")
            idx += 1
    if idx <= 2:
        return math + f"\\tag{{{tag}}}"
    return "\\begin{align}" + "\\\\".join(parts) + "\\end{align}"


def _non_comment(line: str) -> str:
    m = re.search(r"(?<!\\)%", line)
    return line[: m.start()] if m else line
