"""How the deck was made: an iterative co-creation loop between Alexander and the agent.

Writes images/fig-samskaping-{0..4}.svg as stacked layers for click builds: layer 0 the two
parties (Alexander's portrait and the agent) with the sources; layers 1 to 3 one round each of
arrows back and forth, tighter each time; layer 4 the result and who answers for it.
No numbers. Run from presentation/.
"""
import base64
from pathlib import Path

W, H = 1600, 800
A, B, Y, R = (300, 400), (1300, 400), 400, 150
INK = "#231f20"
FD = "font-family:'Roboto Condensed',Arial,sans-serif;font-weight:700"
FB = "font-family:Inter,Arial,sans-serif"
photo = base64.b64encode(Path("images/arj-portrett-2025.png").read_bytes()).decode()


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {W} {H}" width="{W}" height="{H}"><defs>'
            f'<marker id="m" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
            f'<path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker>'
            f'<clipPath id="pc"><circle cx="{A[0]}" cy="{A[1]}" r="{R}"/></clipPath></defs>{body}</svg>')


def label(x, y, t, size=26, font=FB, fill=INK, anchor="middle", halo=8):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" fill="{fill}" style="{font}" '
            f'stroke="#ffffff" stroke-width="{halo}" paint-order="stroke" stroke-linejoin="round">{t}</text>')


def layer0():
    b = (f'<image x="{A[0]-R}" y="{A[1]-R}" width="{2*R}" height="{2*R}" preserveAspectRatio="xMidYMid slice" '
         f'clip-path="url(#pc)" xlink:href="data:image/png;base64,{photo}"/>'
         f'<circle cx="{A[0]}" cy="{A[1]}" r="{R}" fill="none" stroke="{INK}" stroke-width="5"/>'
         + label(A[0], A[1] + R + 50, "Alexander", 34, FD)
         + f'<circle cx="{B[0]}" cy="{B[1]}" r="{R}" fill="#b3e297" stroke="{INK}" stroke-width="5"/>'
         + label(B[0], B[1] - 10, "KI-agent", 40, FD)
         + label(B[0], B[1] + R + 50, "Agenten", 34, FD)
)
    return svg(b)


ROUNDS = [("idé og kilder", "første utkast", 120, 270), ("kommentarer", "ny versjon", 80, 175),
          ("flere kommentarer", "ny versjon", 40, 90)]


def round_layer(i):
    """One round: an arrow over the top to the agent and one under the bottom back, tighter each round."""
    top, bottom, dy, bulge = ROUNDS[i]
    dx = (R * R - dy * dy) ** 0.5 + 12
    x1, x2 = A[0] + dx, B[0] - dx
    mid = (x1 + x2) / 2
    up = f'M{x1:.0f} {Y-dy} C{x1+260:.0f} {Y-dy-bulge} {x2-260:.0f} {Y-dy-bulge} {x2:.0f} {Y-dy}'
    down = f'M{x2:.0f} {Y+dy} C{x2-260:.0f} {Y+dy+bulge} {x1+260:.0f} {Y+dy+bulge} {x1:.0f} {Y+dy}'
    w = 6 - i
    peak = 0.75 * bulge
    b = (f'<path d="{up}" fill="none" stroke="{INK}" stroke-width="{w}" marker-end="url(#m)"/>'
         f'<path d="{down}" fill="none" stroke="{INK}" stroke-width="{w}" marker-end="url(#m)"/>'
         + label(mid, Y - dy - peak + 9, top, 25, FD, halo=16)
         + label(mid, Y + dy + peak + 9, bottom, 25, FD, halo=16))
    return svg(b)


def layer4():
    x, y = (A[0] + B[0]) / 2, Y
    b = (f'<rect x="{x-140}" y="{y-34}" width="280" height="68" fill="#9a90cf" stroke="{INK}" stroke-width="4"/>'
         + label(x, y + 11, "Lysbildene", 34, FD)
         + label(x, H - 14, "Ansvaret er mitt.", 30, FD))
    return svg(b)


out = Path("images")
layers = [layer0()] + [round_layer(i) for i in range(len(ROUNDS))] + [layer4()]
for i, s in enumerate(layers):
    (out / f"fig-samskaping-{i}.svg").write_text(s, encoding="utf-8")
print(f"wrote {len(layers)} layers: images/fig-samskaping-0..{len(layers)-1}.svg")
