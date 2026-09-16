// Render Excalidraw scenes to SVG with the official @excalidraw/excalidraw exportToSvg,
// driven by scripts/sync_notes.py through a JSON manifest:
//   { "out": "<dir>", "jobs": [ { slug, elements, appState, files: {id: {kind:"image",dataURL} | {kind:"tex",tex}}, digest } ] }
// TeX embeds are typeset with MathJax (SVG output) inside the same page.
// Needs network for the CDN modules; CI never runs this (SVGs are committed).
import fs from "node:fs";
import path from "node:path";
import { chromium } from "playwright";

const EXCALIDRAW = "https://esm.sh/@excalidraw/excalidraw@0.18.0?deps=react@19.1.0,react-dom@19.1.0";
const ASSET_PATH = "https://esm.sh/@excalidraw/excalidraw@0.18.0/dist/prod/";
const MATHJAX = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js";

const manifestPath = process.argv[2];
if (!manifestPath) { console.error("usage: node render_excalidraw.mjs manifest.json"); process.exit(2); }
const manifest = JSON.parse(fs.readFileSync(manifestPath, "utf8"));
fs.mkdirSync(manifest.out, { recursive: true });

const browser = await chromium.launch();
const page = await browser.newPage();
page.on("pageerror", (e) => console.error("pageerror:", e.message));
await page.setContent(`<!doctype html><html><head><meta charset="utf-8">
<script>window.EXCALIDRAW_ASSET_PATH = ${JSON.stringify(ASSET_PATH)};
window.MathJax = { svg: { fontCache: "none" }, startup: { typeset: false } };</script>
<script src="${MATHJAX}"></script></head><body></body></html>`, { waitUntil: "load" });
await page.evaluate(async (url) => {
  window.__ex = await import(url);
  await MathJax.startup.promise;
}, EXCALIDRAW);

for (const job of manifest.jobs) {
  const dest = path.join(manifest.out, `${job.slug}.svg`);
  try {
    const svg = await page.evaluate(async (job) => {
      const files = {};
      for (const [id, f] of Object.entries(job.files || {})) {
        if (f.kind === "image") {
          const mime = f.dataURL.slice(5, f.dataURL.indexOf(";"));
          files[id] = { id, dataURL: f.dataURL, mimeType: mime, created: 0 };
        } else if (f.kind === "tex") {
          const node = await MathJax.tex2svgPromise(f.tex, { display: true });
          const svgEl = node.querySelector("svg");
          svgEl.setAttribute("xmlns", "http://www.w3.org/2000/svg");
          svgEl.setAttribute("xmlns:xlink", "http://www.w3.org/1999/xlink");
          const src = new XMLSerializer().serializeToString(svgEl);
          files[id] = { id, dataURL: "data:image/svg+xml;base64," + btoa(unescape(encodeURIComponent(src))), mimeType: "image/svg+xml", created: 0 };
        }
      }
      const el = await window.__ex.exportToSvg({
        elements: job.elements,
        appState: { ...job.appState, exportBackground: true, viewBackgroundColor: job.appState.viewBackgroundColor, theme: "light",
                    exportWithDarkMode: false, exportEmbedScene: false, exportPadding: 16 },
        files,
        exportPadding: 16,
      });
      return el.outerHTML;
    }, job);
    fs.writeFileSync(dest, svg);
    console.log(`rendered ${job.slug} ${svg.length}`);
  } catch (e) {
    console.log(`failed ${job.slug}: ${e.message}`);
    console.error(e);
  }
}
await browser.close();
