"""The portrait between art and science, in Norwegian, as stacked SVG layers for click builds.

Same figure as the EDM deck (2026-10-29-EDM-workshop/presentation/tools/make_intro.py). Writes
images/fig-kunstvit-0.svg (an empty frame that sizes the stack), fig-kunstvit-1..8.svg (the two
fields and their items) and fig-kunstvit-meg.svg (the portrait, last so it stays on top).
Run from presentation/.
"""
import base64
import math
from pathlib import Path

INK = "#231f20"
FD = "font-family:'Roboto Condensed',Arial,sans-serif;font-weight:700"


def svg(w, h, body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {w} {h}" width="{w}" height="{h}"><defs>{defs}</defs>{body}</svg>')


def text(x, y, t, size):
    return (f'<text x="{x:.0f}" y="{y:.0f}" text-anchor="middle" font-size="{size}" fill="{INK}" '
            f'style="{FD}">{t}</text>')


def write(name, content):
    Path(f"images/{name}").write_text(content, encoding="utf-8")


W, H = 1920, 1000
cy, rf, r_me, r_item = H / 2, 420, 165, 98
fields = [("Kunst", 650, "#efadb2", ["Musikk", "Fremføring", "Installasjon"]),
          ("Vitenskap", 1270, "#b3e297", ["Fenomenologi", "Psykologi", "Teknologi"])]
write("fig-kunstvit-0.svg", svg(W, H, ""))
n = 1
for name, fx, col, items in fields:
    write(f"fig-kunstvit-{n}.svg", svg(W, H,
          f'<circle cx="{fx}" cy="{cy}" r="{rf}" fill="{col}" fill-opacity=".55" stroke="{INK}" stroke-width="5"/>'
          + text(fx, cy - rf + 70, name, 56)))
    n += 1
    side = -1 if fx < W / 2 else 1
    for k, it in enumerate(items):
        # on an arc around the portrait, on the field's own side
        a = math.radians((180 if side < 0 else 0) + side * (k - 1) * 40)
        x, y = W / 2 + 300 * math.cos(a), cy + 300 * math.sin(a)
        write(f"fig-kunstvit-{n}.svg", svg(W, H,
              f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r_item}" fill="#ffffff" stroke="{INK}" stroke-width="4"/>'
              + text(x, y + 10, it, 26 if len(it) > 11 else 32)))
        n += 1
photo = base64.b64encode(Path("images/arj-portrett-2025.png").read_bytes()).decode()
write("fig-kunstvit-meg.svg", svg(W, H,
      f'<image x="{W / 2 - r_me}" y="{cy - r_me}" width="{2 * r_me}" height="{2 * r_me}" '
      f'preserveAspectRatio="xMidYMid slice" clip-path="url(#pc)" xlink:href="data:image/png;base64,{photo}"/>'
      f'<circle cx="{W / 2}" cy="{cy}" r="{r_me}" fill="none" stroke="{INK}" stroke-width="6"/>',
      f'<clipPath id="pc"><circle cx="{W / 2}" cy="{cy}" r="{r_me}"/></clipPath>'))
print(f"wrote images/fig-kunstvit-0..{n - 1}.svg and fig-kunstvit-meg.svg")
