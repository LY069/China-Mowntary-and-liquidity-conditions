#!/usr/bin/env python3
"""
Emit docs/index.html — a single self-contained page for GitHub Pages.

app/index.html is authored in Artifact form: no <!doctype>, <html>, <head> or
<body>, and its data arrives via <script src="data.js">. That is exactly what
the Artifact publisher wants, but a file opened directly in a browser needs a
document shell and an explicit charset, or the Chinese indicator names garble.

This wraps the fragment and inlines data.js so the result is one portable file.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
fragment = (ROOT / "app" / "index.html").read_text(encoding="utf-8")
data = (ROOT / "app" / "data.js").read_text(encoding="utf-8")

fragment = fragment.replace('<script src="data.js"></script>',
                            "<script>\n" + data + "</script>")

html = (
    '<!doctype html>\n<html lang="en">\n<head>\n'
    '<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
    '<style>\n'
    '  :root{color-scheme:light dark}\n'
    '  body{margin:0;font:14px system-ui,-apple-system,"Segoe UI",sans-serif}\n'
    '  img{max-width:100%}\n'
    '  [hidden]{display:none!important}\n'
    '</style>\n'
    '</head>\n<body>\n'
    + fragment +
    '\n</body>\n</html>\n'
)

out = ROOT / "docs" / "index.html"
out.parent.mkdir(exist_ok=True)
out.write_text(html, encoding="utf-8")
print(f"wrote {out.relative_to(ROOT)}  ({out.stat().st_size/1024:.1f} KB)")
