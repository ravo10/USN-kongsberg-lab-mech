#!/usr/bin/env python3
"""Prepare and label photos for the equipment guides.

Prepare a phone photo (turn it upright, scale it to 1050 px wide, remove
metadata such as GPS position):

    python tools/photo/photo.py prepare IMG_1234.jpg equipment/<folder>/images/01-front-view.jpg

Add numbered yellow labels (the style used in all guides):

    python tools/photo/photo.py label equipment/<folder>/images/01-front-view.jpg labels.json

labels.json lists one label per line: the number, the point it marks, and
where the numbered circle goes (pixels from the top-left corner):

    [
      [1, [518, 728], [330, 640]],
      [2, [420, 1070], [380, 950]]
    ]

Labelling overwrites the photo, so keep the unlabelled original (for
example as 01-front-view.raw.jpg outside the repository) in case you need to
move a label later. Open the result and check that no label hides a button
or its text.

Needs: pip install pillow
"""

import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont, ImageOps

WIDTH = 1050
YELLOW, BLACK, RADIUS = (255, 196, 0), (0, 0, 0), 26


def prepare(src, dst):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    if im.width > WIDTH:
        im = im.resize((WIDTH, round(im.height * WIDTH / im.width)), Image.LANCZOS)
    # Saving without exif= writes no metadata (no GPS position, no camera data).
    im.save(dst, quality=85, optimize=True, progressive=True)
    print(f"{dst}: {im.width} x {im.height} px, metadata removed")


def font(size):
    for name in ("DejaVuSans-Bold.ttf", "arialbd.ttf", "Arial Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            pass
    return ImageFont.load_default()


def label(path, spec_file):
    spec = json.loads(Path(spec_file).read_text(encoding="utf-8"))
    im = Image.open(path).convert("RGB")
    d = ImageDraw.Draw(im)
    f = font(30)
    for _, (tx, ty), (cx, cy) in spec:  # leader lines first, under the circles
        d.line([(cx, cy), (tx, ty)], fill=BLACK, width=8)
        d.line([(cx, cy), (tx, ty)], fill=YELLOW, width=4)
        d.ellipse([tx - 7, ty - 7, tx + 7, ty + 7], fill=YELLOW, outline=BLACK, width=3)
    for n, _, (cx, cy) in spec:
        d.ellipse([cx - RADIUS, cy - RADIUS, cx + RADIUS, cy + RADIUS], fill=YELLOW, outline=BLACK, width=4)
        d.text((cx, cy + 1), str(n), fill=BLACK, font=f, anchor="mm")
    im.save(path, quality=88, optimize=True, progressive=True)
    print(f"{path}: {len(spec)} labels")


if __name__ == "__main__":
    if len(sys.argv) == 4 and sys.argv[1] == "prepare":
        prepare(sys.argv[2], sys.argv[3])
    elif len(sys.argv) == 4 and sys.argv[1] == "label":
        label(sys.argv[2], sys.argv[3])
    else:
        sys.exit(__doc__)
