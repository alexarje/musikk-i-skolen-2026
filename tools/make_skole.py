"""Two figures for the Skolen? strip, each as stacked layers for click builds.

images/fig-skolefag-0..N.svg: music in the middle, one school subject per layer on a ring around
it, joined to the middle by a plain line (music connects the subjects).
images/fig-effekter-0..N.svg: a different look, since it says a different thing: music on the left
and a fan of arrows out to a column of the areas music influences, one per layer. No numbers.
Run from presentation/.
"""
import math
from pathlib import Path

subjects = [["Matematikk"], ["Naturfag"], ["Programmering"], ["Norsk"], ["Språk"],
            ["Samfunnsfag"], ["Kunst og", "håndverk"], ["Kroppsøving"]]
# From the body outwards: body, feelings and thinking, expression, community and culture.
effects = [["Motorisk"], ["Helse"], ["Emosjonelt"], ["Kognitivt"], ["Språklig"],
           ["Estetisk"], ["Sosialt"], ["Kulturelt"]]
colours = ["#9a90cf", "#a5cbed", "#efadb2", "#b3e297"]

W, H = 1920, 1000
cx, cy, ring, r_item, r_mid = W / 2, H / 2, 370, 122, 170
INK = "#231f20"
FD = "font-family:'Roboto Condensed',Arial,sans-serif;font-weight:700"


def svg(body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<defs>{defs}</defs>{body}</svg>')


def words(x, y, lines, size):
    out = ""
    for i, w in enumerate(lines):
        dy = (i - (len(lines) - 1) / 2) * size * 1.05
        out += (f'<text x="{x:.0f}" y="{y + size * 0.35 + dy:.0f}" text-anchor="middle" font-size="{size}" '
                f'fill="{INK}" style="{FD}">{w}</text>')
    return out


ARROW = (f'<marker id="ar" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" '
         f'orient="auto"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker>')


def build(name, items, arrows):
    centre = (f'<circle cx="{cx}" cy="{cy}" r="{r_mid}" fill="#b3e297" stroke="{INK}" stroke-width="5"/>'
              + words(cx, cy, ["Musikk"], 56))
    Path(f"images/fig-{name}-0.svg").write_text(svg(centre), encoding="utf-8")
    for i, lines in enumerate(items):
        a = math.radians(90 - 360 * i / len(items))
        ux, uy = math.cos(a), -math.sin(a)
        x, y = cx + ring * ux, cy + ring * uy
        gap = 14 if arrows else 0
        x0, y0 = cx + (r_mid + 6) * ux, cy + (r_mid + 6) * uy
        x1, y1 = cx + (ring - r_item - gap) * ux, cy + (ring - r_item - gap) * uy
        marker = ' marker-end="url(#ar)"' if arrows else ""
        size = 30 if max(len(w) for w in lines) > 10 else 36
        body = (f'<line x1="{x0:.0f}" y1="{y0:.0f}" x2="{x1:.0f}" y2="{y1:.0f}" stroke="{INK}" stroke-width="6"{marker}/>'
                f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r_item}" fill="{colours[i % 4]}" stroke="{INK}" stroke-width="4"/>'
                + words(x, y, lines, size))
        Path(f"images/fig-{name}-{i + 1}.svg").write_text(svg(body, ARROW if arrows else ""), encoding="utf-8")
    print(f"wrote images/fig-{name}-0..{len(items)}.svg")


def build_fan(name, items):
    mx, my, mr = 470, H / 2, 200
    px, pw, ph = 1180, 400, 86
    ys = [H / 2 + (i - (len(items) - 1) / 2) * 112 for i in range(len(items))]
    centre = (f'<circle cx="{mx}" cy="{my}" r="{mr}" fill="#b3e297" stroke="{INK}" stroke-width="5"/>'
              + words(mx, my, ["Musikk"], 60))
    Path(f"images/fig-{name}-0.svg").write_text(svg(centre), encoding="utf-8")
    for i, (lines, y) in enumerate(zip(items, ys)):
        a = math.atan2(y - my, px - mx)
        x0, y0 = mx + (mr + 8) * math.cos(a), my + (mr + 8) * math.sin(a)
        x1, y1 = px - 18, y
        cx1 = x0 + (x1 - x0) * 0.55
        body = (f'<path d="M{x0:.0f} {y0:.0f} C{cx1:.0f} {y0:.0f} {cx1:.0f} {y1:.0f} {x1:.0f} {y1:.0f}" fill="none" '
                f'stroke="{INK}" stroke-width="5" marker-end="url(#ar)"/>'
                f'<rect x="{px}" y="{y - ph / 2:.0f}" width="{pw}" height="{ph}" rx="{ph / 2:.0f}" '
                f'fill="{colours[i % 4]}" stroke="{INK}" stroke-width="4"/>'
                + words(px + pw / 2, y, lines, 40))
        Path(f"images/fig-{name}-{i + 1}.svg").write_text(svg(body, ARROW), encoding="utf-8")
    print(f"wrote images/fig-{name}-0..{len(items)}.svg")


build("skolefag", subjects, arrows=False)
build_fan("effekter", effects)
