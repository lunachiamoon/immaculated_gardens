#!/usr/bin/env python3
"""Build the static site and the portable, self-contained HTML copy."""
import base64
import shutil
from pathlib import Path

root = Path(__file__).resolve().parent.parent
html = (root / 'index.html').read_text()
html = html.replace('<link rel="stylesheet" href="styles.css">', '<style>\n' + (root / 'styles.css').read_text() + '\n</style>')
html = html.replace('<script src="app.js"></script>', '<script>\n' + (root / 'app.js').read_text() + '\n</script>')
output = root / 'dist'
output.mkdir(exist_ok=True)
(output / 'index.html').write_text(html)
shutil.copyfile(root / 'garden-study.webp', output / 'garden-study.webp')
image = base64.b64encode((root / 'garden-study.webp').read_bytes()).decode('ascii')
portable = html.replace('src="garden-study.webp"', 'src="data:image/webp;base64,' + image + '"')
(root / 'immaculate-gardens-saul.html').write_text(portable)
print('Built dist/ and immaculate-gardens-saul.html')
