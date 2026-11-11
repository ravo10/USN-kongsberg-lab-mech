#!/usr/bin/env python3
"""Export an equipment guide from Markdown to PDF and Word.

The Markdown files are the master copies. Run this after editing them:

    python tools/export-guide/export.py equipment/hardness-vickers-matsuzawa-mxt50

For each language it finds in the guide folder it writes:

    README.md     ->  guide-en.pdf, guide-en.docx
    README.no.md  ->  guide-no.pdf, guide-no.docx

Options:
    --only pdf|docx   make only one format
    --lang en|no      make only one language
    --quick-card      also print quick-card-*.html in the folder to quick-card-*.pdf
    --check           convert the new .docx files to PDF with LibreOffice and
                      print the page counts (nothing is saved in the guide folder)

Needs:
    pandoc            https://pandoc.org/installing.html
    python-docx       pip install python-docx
    for the PDFs, one of:
      Playwright      pip install playwright, then: playwright install chromium
      Chrome or Edge  used if Playwright is missing (set CHROME=/path/to/browser
                      if it is not found)
    LibreOffice       only for --check
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
STYLE = HERE / "style.css"
LANGS = {"en": "README.md", "no": "README.no.md"}

# Lines that are website navigation only (links to the other language, the
# downloads, and the lab that uses the machine). They are left out of the PDF
# and Word files, where those links would not work.
NAV_LINE = re.compile(r"^(> \*\*|\*\*(Used in|Brukes i):\*\*)")


# ---------------------------------------------------------------- helpers

def find_browser():
    """Chrome or Edge, used only when Playwright is not installed."""
    env = os.environ.get("CHROME")
    if env:
        return env
    for name in ("google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
                 "chrome", "msedge", "microsoft-edge"):
        p = shutil.which(name)
        if p:
            return p
    candidates = [
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for c in candidates:
        if Path(c).exists():
            return c
    sys.exit("Chrome or Edge not found. Set CHROME=/path/to/browser and try again.")


def run(cmd, **kw):
    r = subprocess.run(cmd, capture_output=True, text=True, **kw)
    if r.returncode != 0:
        sys.exit(f"Failed: {' '.join(map(str, cmd))}\n{r.stdout}\n{r.stderr}")
    return r


def print_pdf(browser, html: Path, pdf: Path):
    """Print an HTML file to PDF. Page size and margins come from @page in the CSS.

    Uses Playwright if it is installed (pip install playwright, then
    playwright install chromium), otherwise Chrome or Edge on the command line.
    """
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        sync_playwright = None
    if sync_playwright:
        with sync_playwright() as p:
            kw = {"executable_path": os.environ["CHROME"]} if os.environ.get("CHROME") else {}
            b = p.chromium.launch(**kw)
            page = b.new_page(viewport={"width": 794, "height": 1123})
            page.goto(html.resolve().as_uri(), wait_until="networkidle")
            page.pdf(path=str(pdf), prefer_css_page_size=True, print_background=True)
            b.close()
        return
    browser = browser or find_browser()
    with tempfile.TemporaryDirectory() as profile:
        cmd = [browser, "--headless", "--disable-gpu", "--no-sandbox", "--no-first-run",
               "--no-default-browser-check", "--disable-background-networking",
               "--disable-component-update", "--disable-sync", "--disable-extensions",
               f"--user-data-dir={profile}", "--no-pdf-header-footer",
               "--run-all-compositor-stages-before-draw", "--virtual-time-budget=10000",
               f"--print-to-pdf={pdf}", html.resolve().as_uri()]
        try:
            subprocess.run(cmd, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            sys.exit(f"The browser did not finish printing {html.name} within 2 minutes.\n"
                     "Install Playwright (pip install playwright, then playwright install chromium) and try again.")
    if not pdf.exists():
        sys.exit(f"The browser did not write {pdf}")


def stripped_markdown(src: Path) -> str:
    lines = src.read_text(encoding="utf-8").splitlines()
    out = [l for l in lines if not NAV_LINE.match(l)]
    text = "\n".join(out) + "\n"
    return re.sub(r"\n{3,}", "\n\n", text)


def title_of(md: str) -> str:
    m = re.search(r"^# (.+)$", md, re.M)
    return m.group(1).strip() if m else "Guide"


# ---------------------------------------------------------------- exports

def export_pdf(browser, folder: Path, lang: str, md: str):
    src = folder / f"_tmp_{lang}.md"
    html = folder / f"_tmp_{lang}.html"   # inside the folder so images/ resolve
    css = folder / "_tmp_style.css"
    try:
        src.write_text(md, encoding="utf-8")
        shutil.copy(STYLE, css)
        run(["pandoc", str(src), "-f", "gfm", "-t", "html5", "-s",
             "--metadata", f"pagetitle={title_of(md)}", "--metadata", f"lang={'nb' if lang == 'no' else 'en'}",
             "-c", css.name, "-o", str(html)])
        print_pdf(browser, html, folder / f"guide-{lang}.pdf")
    finally:
        for f in (src, html, css):
            f.unlink(missing_ok=True)
    print(f"  guide-{lang}.pdf")


def export_docx(folder: Path, lang: str, md: str):
    from docx import Document
    from docx.oxml import OxmlElement
    from docx.oxml.ns import qn
    from docx.shared import Cm, Pt

    out = folder / f"guide-{lang}.docx"
    src = folder / f"_tmp_{lang}.md"
    try:
        src.write_text(md, encoding="utf-8")
        run(["pandoc", str(src), "-f", "gfm", "-t", "docx",
             f"--resource-path={folder}", "-o", str(out)])
    finally:
        src.unlink(missing_ok=True)

    doc = Document(str(out))
    for s in doc.sections:
        s.page_width, s.page_height = Cm(21), Cm(29.7)
        s.left_margin = s.right_margin = Cm(2)
        s.top_margin = s.bottom_margin = Cm(1.8)

    max_w, max_h = Cm(17), Cm(10.5)
    for shape in doc.inline_shapes:
        r = min(max_w / shape.width, max_h / shape.height)
        shape.width, shape.height = int(shape.width * r), int(shape.height * r)

    for table in doc.tables:
        tblPr = table._tbl.tblPr
        for old in tblPr.findall(qn("w:tblBorders")):
            tblPr.remove(old)
        borders = OxmlElement("w:tblBorders")
        for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
            el = OxmlElement(f"w:{edge}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), "4")
            el.set(qn("w:space"), "0")
            el.set(qn("w:color"), "999999")
            borders.append(el)
        tblPr.append(borders)
        if table.rows:
            for cell in table.rows[0].cells:
                for p in cell.paragraphs:
                    for run_ in p.runs:
                        run_.bold = True

    normal = doc.styles["Normal"]
    normal.font.name = "Calibri"
    normal.font.size = Pt(10.5)
    rpr = normal.element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), "Calibri")

    doc.save(str(out))
    print(f"  guide-{lang}.docx")


def export_quick_cards(browser, folder: Path):
    cards = sorted(folder.glob("quick-card-*.html"))
    if not cards:
        print("  no quick-card-*.html in this folder")
    for html in cards:
        print_pdf(browser, html, html.with_suffix(".pdf"))
        print(f"  {html.with_suffix('.pdf').name}")


def pdf_pages(pdf: Path) -> int:
    return len(re.findall(rb"/Type\s*/Page[^s]", pdf.read_bytes()))


def check_docx(folder: Path, langs):
    soffice = shutil.which("soffice") or shutil.which("libreoffice")
    if not soffice:
        print("  LibreOffice not found, skipping --check")
        return
    with tempfile.TemporaryDirectory() as tmp:
        for lang in langs:
            docx = folder / f"guide-{lang}.docx"
            if docx.exists():
                run([soffice, "--headless", "--convert-to", "pdf", str(docx), "--outdir", tmp])
                print(f"  guide-{lang}.docx -> {pdf_pages(Path(tmp) / docx.with_suffix('.pdf').name)} pages")


# ---------------------------------------------------------------- main

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("folder", type=Path, help="guide folder, e.g. equipment/hardness-vickers-matsuzawa-mxt50")
    ap.add_argument("--only", choices=["pdf", "docx"])
    ap.add_argument("--lang", choices=sorted(LANGS))
    ap.add_argument("--quick-card", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    folder = a.folder.resolve()
    langs = [a.lang] if a.lang else [l for l, f in LANGS.items() if (folder / f).exists()]
    if not langs:
        sys.exit(f"No README.md or README.no.md in {folder}")
    if not shutil.which("pandoc"):
        sys.exit("pandoc not found. Install it from https://pandoc.org/installing.html")

    browser = None  # looked up on first use, only if Playwright is missing
    print(f"Exporting {folder.name}")
    for lang in langs:
        md = stripped_markdown(folder / LANGS[lang])
        if a.only != "docx":
            export_pdf(browser, folder, lang, md)
            print(f"    {pdf_pages(folder / f'guide-{lang}.pdf')} pages")
        if a.only != "pdf":
            export_docx(folder, lang, md)
    if a.quick_card:
        export_quick_cards(browser, folder)
    if a.check:
        check_docx(folder, langs)


if __name__ == "__main__":
    main()
