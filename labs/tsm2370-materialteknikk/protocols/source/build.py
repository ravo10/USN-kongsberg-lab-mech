"""Build TSM2370 lab protocols and report template as consistently formatted .docx files."""
import re, sys
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement
from docx.oxml.ns import qn

ACCENT = RGBColor(0x1F, 0x4E, 0x79)
GREY = RGBColor(0x6B, 0x6B, 0x6B)
INK = RGBColor(0x1D, 0x1D, 0x1B)
SHADE = "E8EEF4"
LABEL_SHADE = "F2F2F2"


def shade(cell, fill):
    tcPr = cell._tc.get_or_add_tcPr()
    s = OxmlElement("w:shd"); s.set(qn("w:val"), "clear"); s.set(qn("w:color"), "auto"); s.set(qn("w:fill"), fill)
    tcPr.append(s)


def borders(table, color="A6A6A6"):
    tblPr = table._tbl.tblPr
    b = OxmlElement("w:tblBorders")
    for e in ["top", "left", "bottom", "right", "insideH", "insideV"]:
        x = OxmlElement(f"w:{e}"); x.set(qn("w:val"), "single"); x.set(qn("w:sz"), "4"); x.set(qn("w:color"), color)
        b.append(x)
    tblPr.append(b)


def cell_margins(table, top=60, bottom=60, left=100, right=100):
    tblPr = table._tbl.tblPr
    m = OxmlElement("w:tblCellMar")
    for k, v in dict(top=top, bottom=bottom, left=left, right=right).items():
        x = OxmlElement(f"w:{k}"); x.set(qn("w:w"), str(v)); x.set(qn("w:type"), "dxa"); m.append(x)
    tblPr.append(m)


def fix_table(t, widths, header_row=False):
    t.autofit = False
    tblPr = t._tbl.tblPr
    tw = OxmlElement("w:tblW"); tw.set(qn("w:w"), str(int(sum(widths) * 567))); tw.set(qn("w:type"), "dxa"); tblPr.append(tw)
    lay = OxmlElement("w:tblLayout"); lay.set(qn("w:type"), "fixed"); tblPr.append(lay)
    grid = t._tbl.tblGrid
    for j, gc in enumerate(grid.findall(qn("w:gridCol"))): gc.set(qn("w:w"), str(int(widths[j] * 567)))
    n = len(t.rows)
    for i, row in enumerate(t.rows):
        trPr = row._tr.get_or_add_trPr()
        cs = OxmlElement("w:cantSplit"); trPr.append(cs)
        if header_row and i == 0:
            th = OxmlElement("w:tblHeader"); trPr.append(th)
        for j, c in enumerate(row.cells):
            c.width = Cm(widths[j])
            if i < n - 1:
                for p in c.paragraphs: p.paragraph_format.keep_with_next = True


def add_runs(par, text, size=None, color=None):
    """Inline markup: **bold**, [placeholder] in grey italic."""
    for tok in re.split(r"(\*\*.+?\*\*|\[(?!\d+\])[^\]]+\])", text):
        if not tok:
            continue
        if tok.startswith("**"):
            r = par.add_run(tok[2:-2]); r.bold = True
        elif re.fullmatch(r"\[[^\]]+\]", tok) and not re.fullmatch(r"\[\d+\]", tok):
            r = par.add_run(tok); r.italic = True; r.font.color.rgb = GREY
        else:
            r = par.add_run(tok)
        if size: r.font.size = size
        if color and not tok.startswith("["): r.font.color.rgb = color
    return par


def field(par, code):
    r = par.add_run()
    for kind, val in (("begin", None), ("instr", code), ("separate", None), ("end", None)):
        if kind == "instr":
            t = OxmlElement("w:instrText"); t.set(qn("xml:space"), "preserve"); t.text = val; r._r.append(t)
        else:
            f = OxmlElement("w:fldChar"); f.set(qn("w:fldCharType"), kind); r._r.append(f)
        if kind == "separate":
            t = OxmlElement("w:t"); t.text = "1"; r._r.append(t)


def new_doc(header_text, page_word, of_word):
    d = Document()
    s = d.sections[0]
    s.page_width, s.page_height = Cm(21), Cm(29.7)
    s.left_margin = s.right_margin = Cm(2.2)
    s.top_margin, s.bottom_margin = Cm(2.0), Cm(1.8)
    st = d.styles["Normal"]; st.font.name = "Calibri"; st.font.size = Pt(11); st.font.color.rgb = INK
    st.element.rPr.rFonts.set(qn("w:eastAsia"), "Calibri")
    st.paragraph_format.space_after = Pt(6); st.paragraph_format.line_spacing = 1.15
    for name, size, before in (("Title", 22, 0), ("Heading 1", 14, 16), ("Heading 2", 12, 10)):
        h = d.styles[name]; h.font.name = "Calibri"; h.font.size = Pt(size); h.font.bold = True
        h.font.color.rgb = ACCENT if name != "Title" else INK
        h.element.rPr.rFonts.set(qn("w:asciiTheme"), "") if False else None
        rf = h.element.rPr.rFonts; rf.set(qn("w:ascii"), "Calibri"); rf.set(qn("w:hAnsi"), "Calibri")
        for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
            if rf.get(qn(a)) is not None: del rf.attrib[qn(a)]
        h.paragraph_format.space_before = Pt(before); h.paragraph_format.space_after = Pt(4)
        h.paragraph_format.keep_with_next = True
    d.styles["Title"].paragraph_format.space_after = Pt(10)
    # header / footer
    hp = s.header.paragraphs[0]; hp.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    r = hp.add_run(header_text); r.font.size = Pt(9); r.font.color.rgb = GREY
    fp = s.footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
    for part in (f"{page_word} ", "PAGE", f" {of_word} ", "NUMPAGES"):
        if part in ("PAGE", "NUMPAGES"):
            field(fp, part)
        else:
            rr = fp.add_run(part)
    for rr in fp.runs: rr.font.size = Pt(9); rr.font.color.rgb = GREY
    return d


def block(d, kind, *args):
    if kind == "label":
        p = d.add_paragraph(); r = p.add_run(args[0].upper()); r.bold = True; r.font.size = Pt(10)
        r.font.color.rgb = ACCENT; p.paragraph_format.space_after = Pt(0)
    elif kind == "title":
        d.add_paragraph(args[0], style="Title")
    elif kind == "h1":
        d.add_paragraph(args[0], style="Heading 1")
    elif kind == "h2":
        d.add_paragraph(args[0], style="Heading 2")
    elif kind == "p":
        add_runs(d.add_paragraph(), args[0])
    elif kind == "formula":
        for line in args[0]:
            p = d.add_paragraph(); p.paragraph_format.left_indent = Cm(1); p.paragraph_format.space_after = Pt(2)
            lab, _, eq = line.partition(":")
            if eq:
                r = p.add_run(lab + ":  "); r.font.color.rgb = GREY
                r = p.add_run(eq.strip()); r.italic = True; r.bold = True
            else:
                r = p.add_run(line); r.italic = True
        d.paragraphs[-1].paragraph_format.space_after = Pt(8)
    elif kind in ("ol", "ul"):
        for i, item in enumerate(args[0], 1):
            p = d.add_paragraph(); pf = p.paragraph_format
            pf.left_indent = Cm(0.9); pf.first_line_indent = Cm(-0.6); pf.space_after = Pt(3)
            pf.tab_stops.add_tab_stop(Cm(0.9))
            mark = f"{i}.\t" if kind == "ol" else "•\t"
            r = p.add_run(mark); r.bold = kind == "ol"; r.font.color.rgb = ACCENT
            add_runs(p, item)
        d.paragraphs[-1].paragraph_format.space_after = Pt(8)
    elif kind == "table":
        header, rows, widths = args[0], args[1], args[2] if len(args) > 2 else None
        t = d.add_table(rows=1 + len(rows), cols=len(header)); t.alignment = WD_TABLE_ALIGNMENT.CENTER
        borders(t); cell_margins(t)
        for j, h in enumerate(header):
            c = t.rows[0].cells[j]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.size = Pt(10)
            shade(c, SHADE)
        for i, row in enumerate(rows, 1):
            for j, v in enumerate(row):
                c = t.rows[i].cells[j]; c.text = ""; add_runs(c.paragraphs[0], v, size=Pt(10))
        for row in t.rows:
            for c in row.cells: c.paragraphs[0].paragraph_format.space_after = Pt(0)
        fix_table(t, widths or [16.6 / len(header)] * len(header), header_row=True)
        d.add_paragraph().paragraph_format.space_after = Pt(2)
    elif kind == "info":
        rows = args[0]
        t = d.add_table(rows=len(rows), cols=2); borders(t, "BFBFBF"); cell_margins(t)
        for i, (k, v) in enumerate(rows):
            a, b = t.rows[i].cells
            a.text = ""; r = a.paragraphs[0].add_run(k); r.bold = True; r.font.size = Pt(10); shade(a, LABEL_SHADE)
            b.text = ""; add_runs(b.paragraphs[0], v, size=Pt(10))
            for c in (a, b): c.paragraphs[0].paragraph_format.space_after = Pt(0)
        fix_table(t, [5.2, 11.4])
        d.add_paragraph().paragraph_format.space_after = Pt(4)
    elif kind == "sign":
        date_w, sign_w, statement = args
        p = d.add_paragraph(); p.paragraph_format.space_before = Pt(24)
        p.add_run(f"{date_w}: ______________________        {sign_w}: ______________________________")
        p = d.add_paragraph(); r = p.add_run(statement); r.italic = True; r.font.size = Pt(9.5); r.font.color.rgb = GREY
    elif kind == "pagebreak":
        d.add_paragraph().add_run().add_break(WD_BREAK.PAGE)


def build(spec, path):
    d = new_doc(spec["header"], spec["page"], spec["of"])
    for b in spec["blocks"]:
        block(d, *b)
    cp = d.core_properties
    cp.author = "Rasmus Ullestad Relling"; cp.title = spec["title"]; cp.comments = ""
    cp.last_modified_by = "Rasmus Ullestad Relling"
    d.save(path)


if __name__ == "__main__":
    sys.path.insert(0, sys.argv[1])
    import content
    for name, spec in content.DOCS.items():
        build(spec, f"{sys.argv[2]}/{name}.docx")
        print("built", name)
