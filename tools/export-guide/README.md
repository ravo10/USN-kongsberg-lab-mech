# Export a guide to PDF and Word

The Markdown files in each equipment folder (`README.md` in English, `README.no.md` in Norwegian) are the master copies. The PDF and Word files are made from them with `export.py`. Edit the Markdown first, then run the script from the repository root:

```bash
python tools/export-guide/export.py equipment/hardness-vickers-matsuzawa-mxt50
```

This writes `guide-en.pdf`, `guide-en.docx`, `guide-no.pdf` and `guide-no.docx` in the guide folder. The PDFs are made from `style.css` in this folder; the Word files get A4 pages, 2 cm side margins, Calibri 10.5 pt, images scaled to fit, and borders on all tables.

The navigation lines at the top of a guide (the line starting with `> **Norsk versjon:**` or `> **English version:**` that links to the other language and the downloads, and the **Used in:** / **Brukes i:** line) are only for the website and are left out of the PDF and Word files.

## Options

| Option | What it does |
| --- | --- |
| `--only pdf` or `--only docx` | Make only one format |
| `--lang en` or `--lang no` | Make only one language |
| `--quick-card` | Also print `quick-card-*.html` in the folder to `quick-card-*.pdf` (one A4 page, no margins). Edit the HTML first if the card text changes. |
| `--check` | Convert the new Word files to PDF with LibreOffice and print the page counts, to see that nothing broke |

## What you need

- [pandoc](https://pandoc.org/installing.html)
- python-docx: `pip install python-docx`
- For the PDFs, one of:
  - Playwright (recommended): `pip install playwright`, then `playwright install chromium`
  - Chrome or Microsoft Edge. The script uses it if Playwright is missing. If it is not found, set `CHROME` to the browser's path.
- LibreOffice, only for `--check`

## After exporting

Open the new PDFs and check the pages: images not cut in half, tables readable, the quick card still on one page. Then commit the Markdown and the exported files together.
