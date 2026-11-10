# Source for the TSM2370 protocols and report template

The Word files in `../` are generated from `content.py` (the text) by `build.py` (the layout), so all documents share the same formatting.

To change a protocol or the template:

1. Edit the text in `content.py`.
2. Run `python build.py . ..` in this folder (needs `pip install python-docx`).
3. Make the PDFs again, e.g. `soffice --headless --convert-to pdf ../*.docx --outdir ..` or *Save as PDF* in Word.

Inline markup in `content.py`: `**bold**`, and `[placeholder]` for text students replace (shown in grey italic).
