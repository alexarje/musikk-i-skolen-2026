"""Musicking quadrant with KI in the middle, as three stacked SVG layers for click builds.

Layout follows images/musikkeringskvadranten.png: Forstå and Oppleve on top, Skape and Utøve
below, arrows Skape -> Utøve -> Oppleve -> Forstå -> Skape. Layer 2 adds KI in the middle with
dashed links to all four corners; layer 3 adds the label "mellom". Run from presentation/.
"""
from pathlib import Path

W, H = 1200, 900
R = 150
C = {"Forstå": (300, 220), "Oppleve": (900, 220), "Skape": (300, 680), "Utøve": (900, 680)}
FILL = {"Forstå": "#a5cbed", "Oppleve": "#efadb2", "Skape": "#b3e297", "Utøve": "#9a90cf"}
INK = "#231f20"
FONT = "font-family:'Roboto Condensed',Arial,sans-serif;font-weight:700"


def head():
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" '
            f'orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>')


def edge(p, q, pad=R + 8, dashed=False, arrow=True, width=5):
    (x1, y1), (x2, y2) = p, q
    dx, dy = x2 - x1, y2 - y1
    d = (dx * dx + dy * dy) ** 0.5
    ux, uy = dx / d, dy / d
    a = (x1 + ux * pad[0], y1 + uy * pad[0]) if isinstance(pad, tuple) else (x1 + ux * pad, y1 + uy * pad)
    b = (x2 - ux * pad[1], y2 - uy * pad[1]) if isinstance(pad, tuple) else (x2 - ux * pad, y2 - uy * pad)
    dash = ' stroke-dasharray="14 12"' if dashed else ""
    mk = ' marker-end="url(#a)"' if arrow else ""
    return (f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="{INK}" '
            f'stroke-width="{width}"{dash}{mk}/>')


def layer1():
    s = head()
    for a, b in [("Skape", "Utøve"), ("Utøve", "Oppleve"), ("Oppleve", "Forstå"), ("Forstå", "Skape")]:
        s += edge(C[a], C[b])
    for k, (x, y) in C.items():
        s += (f'<circle cx="{x}" cy="{y}" r="{R}" fill="{FILL[k]}" stroke="{INK}" stroke-width="5"/>'
              f'<text x="{x}" y="{y + 18}" text-anchor="middle" font-size="52" fill="{INK}" style="{FONT}">{k}</text>')
    return s + "</svg>"


def word():
    return (head() + f'<text x="{W/2}" y="{H/2 + 18}" text-anchor="middle" font-size="56" fill="{INK}" '
            f'style="{FONT}">Musikkering</text></svg>')


def layer2():
    s = head()
    m = (W / 2, H / 2)
    for k in C:
        s += edge(m, C[k], pad=(118, R + 6), dashed=True, arrow=False, width=5)
    s += (f'<circle cx="{m[0]}" cy="{m[1]}" r="110" fill="{INK}"/>'
          f'<text x="{m[0]}" y="{m[1] + 22}" text-anchor="middle" font-size="64" fill="#ffffff" style="{FONT}">KI</text></svg>')
    return s


def corner(k, arrow_from=None, closing=False):
    """One corner, with the arrow that leads into it; the last layer also closes the circle."""
    s = head()
    if arrow_from:
        s += edge(C[arrow_from], C[k])
    if closing:
        s += edge(C["Forstå"], C["Skape"])
    x, y = C[k]
    s += (f'<circle cx="{x}" cy="{y}" r="{R}" fill="{FILL[k]}" stroke="{INK}" stroke-width="5"/>'
          f'<text x="{x}" y="{y + 18}" text-anchor="middle" font-size="52" fill="{INK}" style="{FONT}">{k}</text>')
    return s + "</svg>"


out = Path("images")
order = [("Skape", None), ("Utøve", "Skape"), ("Oppleve", "Utøve"), ("Forstå", "Oppleve")]
for i, (k, prev) in enumerate(order, 1):
    (out / f"fig-kvadrant-hjorne-{i}.svg").write_text(corner(k, prev, closing=(k == "Forstå")), encoding="utf-8")
(out / "fig-kvadrant-ki-1.svg").write_text(layer1(), encoding="utf-8")
(out / "fig-kvadrant-ord.svg").write_text(word(), encoding="utf-8")
(out / "fig-kvadrant-ki-2.svg").write_text(layer2(), encoding="utf-8")
print("wrote images/fig-kvadrant-hjorne-1..4.svg, fig-kvadrant-ki-1.svg, fig-kvadrant-ord.svg and fig-kvadrant-ki-2.svg")
