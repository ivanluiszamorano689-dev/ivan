#!/usr/bin/env python3
"""Arma los PDFs de Economía III.

Cada documento vive en docs/<nombre>/ con un manifest.json y fragmentos HTML.
Uso:
    python3 build.py                 # todos los documentos
    python3 build.py teoria practica # solo algunos
    python3 build.py --figs          # regenera además todos los gráficos

Pasos por documento:
  1. Ensambla portada + índice + fragmentos en _build/<doc>.html
  2. Imprime con Chromium (render.mjs) -> PDF de primera pasada
  3. Lee el outline del PDF para obtener la página de cada título
  4. Vuelve a imprimir con los números de página en el índice
"""
import html
import json
import re
import subprocess
import sys
from pathlib import Path

import pymupdf

SRC = Path(__file__).resolve().parent
OUT_PDF = SRC.parent / "pdf"
BUILD = SRC / "_build"

HEAD = """<!doctype html>
<html lang="es">
<head>
<meta charset="utf-8">
<base href="../">
<title>{title}</title>
<link rel="stylesheet" href="assets/vendor/katex/katex.min.css">
<link rel="stylesheet" href="assets/style.css">
<style>@page {{ @bottom-left {{ content: "{short_title}"; }} }}</style>
<script src="assets/vendor/katex/katex.min.js"></script>
<script src="assets/vendor/katex/contrib/auto-render.min.js"></script>
{mermaid}
</head>
<body class="{body_class}">
"""

MERMAID = '<script src="assets/vendor/mermaid.min.js"></script>'

TAIL = """
<script>
window.__TOC_PAGES = {toc_pages};
(async function () {{
  const report = {{ katexErrors: [], missingImages: [], overflow: [] }};
  // 1) Matemática (solo \\( \\) y \\[ \\] — el signo $ queda libre para pesos)
  renderMathInElement(document.body, {{
    delimiters: [
      {{ left: "\\\\[", right: "\\\\]", display: true }},
      {{ left: "\\\\(", right: "\\\\)", display: false }}
    ],
    throwOnError: false,
    strict: "ignore",
    macros: {{
      "\\\\kt": "\\\\tilde{{k}}",
      "\\\\yt": "\\\\tilde{{y}}",
      "\\\\ct": "\\\\tilde{{c}}",
      "\\\\gk": "\\\\gamma_{{k}}",
      "\\\\gkt": "\\\\gamma_{{\\\\tilde k}}"
    }}
  }});
  document.querySelectorAll('.katex-error').forEach(e => report.katexErrors.push(e.getAttribute('title') || e.textContent));

  // 2) Diagramas mermaid (opcionales)
  if (window.mermaid) {{
    mermaid.initialize({{ startOnLoad: false, theme: 'base', securityLevel: 'loose',
      themeVariables: {{ fontFamily: 'Inter, sans-serif', fontSize: '13px', primaryColor: '#eef5fd',
        primaryBorderColor: '#2a78d6', primaryTextColor: '#1d1d1b', lineColor: '#52514e',
        secondaryColor: '#fdf1ea', tertiaryColor: '#e8f7f0' }},
      flowchart: {{ htmlLabels: true, curve: 'basis' }} }});
    try {{ await mermaid.run({{ querySelector: '.mermaid' }}); }} catch (e) {{ report.mermaidError = String(e); }}
  }}

  // 3) Índice automático a partir de h2/h3 (data-toc="no" para excluir)
  const toc = document.querySelector('#toc-list');
  if (toc) {{
    let i = 0;
    const heads = [...document.querySelectorAll('main h2, main h3')].filter(h => h.dataset.toc !== 'no' && !h.closest('.toc'));
    const depth = parseInt(toc.dataset.depth || '3', 10);
    heads.forEach(h => {{
      const lvl = parseInt(h.tagName[1], 10);
      if (lvl > depth) return;
      if (!h.id) h.id = 'h-' + (i++);
      const li = document.createElement('li');
      li.className = 'l' + lvl;
      const num = h.querySelector('.num');
      const label = h.dataset.tocLabel || (num ? num.textContent.trim() + '  ' + h.textContent.replace(num.textContent, '').trim() : h.textContent.trim());
      const a = document.createElement('a'); a.href = '#' + h.id; a.textContent = label;
      const dots = document.createElement('span'); dots.className = 'dots';
      const pg = document.createElement('span'); pg.className = 'pg';
      const key = h.textContent.replace(/\\s+/g, ' ').trim();
      pg.textContent = (window.__TOC_PAGES && window.__TOC_PAGES[key]) || '';
      li.append(a, dots, pg); toc.appendChild(li);
    }});
  }}

  // 4) Controles: imágenes faltantes y desbordes horizontales
  await Promise.all([...document.images].map(img => img.complete ? null : new Promise(r => {{ img.onload = img.onerror = r; }})));
  document.querySelectorAll('img').forEach(img => {{ if (!img.naturalWidth) report.missingImages.push(img.getAttribute('src')); }});
  const mainW = document.querySelector('main') ? document.querySelector('main').clientWidth : 0;
  document.querySelectorAll('main table, main .katex-display, main figure, main .calc').forEach(el => {{
    if (el.scrollWidth > el.clientWidth + 2 || (mainW && el.getBoundingClientRect().width > mainW + 2)) {{
      report.overflow.push((el.className || el.tagName) + ': ' + el.textContent.trim().slice(0, 70));
    }}
  }});
  window.__REPORT = report;
  window.__READY = true;
}})();
</script>
</body>
</html>
"""


def cover_html(m):
    chips = "".join(f"<span>{html.escape(c)}</span>" for c in m.get("chips", []))
    art = f'<img class="cover-art" src="{m["cover_art"]}" alt="">' if m.get("cover_art") else ""
    return f"""
<section class="cover {m.get('cover_class', '')}">
  <div class="cover-kicker">{m.get('kicker', 'Economía III · FCEJyS · UNSa')}</div>
  <h1 data-toc="no">{m['title']}</h1>
  <div class="cover-sub">{m.get('subtitle', '')}</div>
  <div class="cover-chips">{chips}</div>
  {art}
  <div class="cover-meta"><div>{m.get('meta_left', '')}</div><div>{m.get('meta_right', '')}</div></div>
</section>
"""


def toc_html(m):
    if not m.get("toc", True):
        return ""
    intro = m.get("toc_intro", "")
    return f"""
<section class="toc">
  <h2 data-toc="no">Índice</h2>
  {intro}
  <ol id="toc-list" data-depth="{m.get('toc_depth', 3)}"></ol>
</section>
"""


def assemble(doc, toc_pages=None, manifest=None, out_name=None):
    ddir = SRC / "docs" / doc
    m = manifest or json.loads((ddir / "manifest.json").read_text(encoding="utf-8"))
    parts = [HEAD.format(title=html.escape(m["title_plain"]), short_title=m.get("short_title", m["title_plain"]).replace('"', "'"),
                         body_class=m.get("body_class", ""), mermaid=MERMAID if m.get("mermaid") else "")]
    if not m.get("no_cover"):
        parts.append(cover_html(m))
    parts.append("<main>")
    parts.append(toc_html(m))
    for frag in m["fragments"]:
        p = ddir / frag
        if not p.exists():
            print(f"  ! falta el fragmento {p.relative_to(SRC)}", file=sys.stderr)
            continue
        parts.append(f"\n<!-- ===== {frag} ===== -->\n")
        parts.append(p.read_text(encoding="utf-8"))
    parts.append("</main>")
    parts.append(TAIL.format(toc_pages=json.dumps(toc_pages or {}, ensure_ascii=False)))
    BUILD.mkdir(exist_ok=True)
    out = BUILD / f"{out_name or doc}.html"
    out.write_text("".join(parts), encoding="utf-8")
    return m, out


def render(html_path, pdf_path):
    r = subprocess.run(["node", str(SRC / "render.mjs"), str(html_path), str(pdf_path)], cwd=SRC,
                       capture_output=True, text=True)
    if r.returncode != 0:
        print(r.stdout, r.stderr, file=sys.stderr)
        raise SystemExit(f"falló el render de {html_path}")
    rep = json.loads(Path(str(pdf_path).replace(".pdf", ".render.json")).read_text())
    return rep


def outline_pages(pdf_path):
    d = pymupdf.open(pdf_path)
    pages = {}
    for lvl, title, page in d.get_toc():
        key = re.sub(r"\s+", " ", title).strip()
        pages.setdefault(key, page)
    return pages, d.page_count


def build(doc):
    print(f"== {doc}")
    m, h = assemble(doc)
    tmp = BUILD / f"{doc}.pass1.pdf"
    render(h, tmp)
    pages, _ = outline_pages(tmp)
    m, h = assemble(doc, pages)
    final = OUT_PDF / m["filename"]
    OUT_PDF.mkdir(exist_ok=True)
    rep = render(h, final)
    # pymupdf: metadata limpia
    d = pymupdf.open(final)
    d.set_metadata({"title": m["title_plain"], "author": "Economía III — material de estudio", "subject": m.get("subtitle_plain", ""),
                    "creator": "Chromium + KaTeX + matplotlib", "producer": "build.py"})
    tmpfinal = final.with_suffix(".tmp.pdf")
    d.save(tmpfinal, garbage=3, deflate=True)
    d.close()
    tmpfinal.replace(final)
    n = pymupdf.open(final).page_count
    r = rep.get("report", {})
    probs = rep.get("problems", [])
    print(f"   {final.name}: {n} páginas | katex err: {len(r.get('katexErrors', []))} | "
          f"img faltantes: {len(r.get('missingImages', []))} | desbordes: {len(r.get('overflow', []))} | consola: {len(probs)}")
    for k in ("katexErrors", "missingImages", "overflow"):
        for e in r.get(k, [])[:30]:
            print(f"   - {k}: {e}")
    for p in probs[:20]:
        print(f"   - consola: {p}")
    return final


def preview(name, frags, dpi=60):
    """Vista previa aislada de algunos fragmentos (sin portada ni índice).
    python3 build.py --preview <nombre> docs/teoria/02-tema2.html [otro.html ...]
    Genera _build/preview_<nombre>.pdf y _build/preview_<nombre>/p-NN.png"""
    frags = [Path(f).resolve() for f in frags]
    doc = frags[0].parent.name
    ddir = SRC / "docs" / doc
    base = json.loads((ddir / "manifest.json").read_text(encoding="utf-8")) if (ddir / "manifest.json").exists() else {}
    m = dict(base, no_cover=True, toc=False, title_plain=base.get("title_plain", name),
             fragments=[str(f.relative_to(ddir)) for f in frags])
    _, h = assemble(doc, manifest=m, out_name=f"preview_{name}")
    pdf = BUILD / f"preview_{name}.pdf"
    rep = render(h, pdf)
    d = pymupdf.open(pdf)
    pdir = BUILD / f"preview_{name}"
    pdir.mkdir(exist_ok=True)
    for old in pdir.glob("p-*.png"):
        old.unlink()
    for i, pg in enumerate(d):
        pg.get_pixmap(dpi=dpi).save(pdir / f"p-{i + 1:02d}.png")
    r = rep.get("report", {})
    print(f"preview {pdf} : {d.page_count} páginas -> PNG en {pdir}")
    for k in ("katexErrors", "missingImages", "overflow"):
        for e in r.get(k, []):
            print(f"   - {k}: {e}")
    for p in rep.get("problems", []):
        print(f"   - consola: {p}")


def main():
    if "--preview" in sys.argv:
        i = sys.argv.index("--preview")
        preview(sys.argv[i + 1], sys.argv[i + 2:])
        return
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if "--figs" in sys.argv:
        for f in sorted((SRC / "figs").glob("*.py")):
            print(f"figs: {f.name}")
            subprocess.run([sys.executable, str(f)], cwd=SRC / "figs", check=True)
    docs = args or [d.name for d in sorted((SRC / "docs").iterdir()) if (d / "manifest.json").exists()]
    for d in docs:
        build(d)


if __name__ == "__main__":
    main()
