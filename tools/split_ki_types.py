"""Split images/ki-admin-autonomi.svg into click layers.

Writes images/fig-ki-typer-0.svg (the two axes) and fig-ki-typer-1..N.svg, one system type per
layer: its dashed link from the previous type, its dot and its label. Run from presentation/.
"""
import math
import re
from pathlib import Path


def shorten(path, gap=30):
    """Trim a dashed link so it stops at the dots instead of crossing them."""
    x1, y1, x2, y2 = map(float, re.search(r"d='M(\S+) (\S+) L(\S+) (\S+)'", path).groups())
    d = math.hypot(x2 - x1, y2 - y1)
    ux, uy = (x2 - x1) / d, (y2 - y1) / d
    new = f"d='M{x1 + gap * ux:.0f} {y1 + gap * uy:.0f} L{x2 - gap * ux:.0f} {y2 - gap * uy:.0f}'"
    return re.sub(r"d='M[^']*'", new, path)


src = Path("images/ki-admin-autonomi.svg").read_text(encoding="utf-8")
head = src[:src.index("</defs>") + len("</defs>")]
body = src[len(head):src.rindex("</svg>")].strip()
elements = re.findall(r"<(?:path|circle)[^>]*/>|<text[^>]*>[^<]*</text>", body)
assert sum(len(e) for e in elements) == len(re.sub(r"\s+$", "", body)), "unparsed content in the SVG"

groups, pending = [[]], []
for e in elements:
    if e.startswith("<circle"):
        groups.append(pending + [e])
        pending = []
    elif "stroke-dasharray" in e:
        pending.append(shorten(e))
    elif len(groups) == 1:
        groups[0].append(e)
    else:
        groups[-1].append(e)

for i, g in enumerate(groups):
    Path(f"images/fig-ki-typer-{i}.svg").write_text(head + "".join(g) + "</svg>", encoding="utf-8")
print(f"wrote images/fig-ki-typer-0..{len(groups) - 1}.svg")
