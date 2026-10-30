"""Human in the loop: the last layer on the KI types figure (fig-ki-typer-*.svg).

A person pictogram in the empty upper left of the figure, with two curved arrows that make a loop
round it, and a label. Same 1600 x 800 viewBox as images/ki-admin-autonomi.svg. Writes
images/fig-ki-typer-hitl.svg. Run from presentation/.
"""
import math
from pathlib import Path

INK = "#1a202c"
FILL = "#efadb2"
cx, cy, R = 400, 230, 140


def pt(deg, r=R):
    a = math.radians(deg)
    return cx + r * math.cos(a), cy + r * math.sin(a)


def arc(a0, a1):
    (x0, y0), (x1, y1) = pt(a0), pt(a1)
    return (f"<path d='M{x0:.0f} {y0:.0f} A{R} {R} 0 0 1 {x1:.0f} {y1:.0f}' fill='none' stroke='{INK}' "
            f"stroke-width='9' marker-end='url(#hl)'/>")


r = 48
person = (f"<circle cx='{cx}' cy='{cy - 62}' r='38' fill='{FILL}' stroke='{INK}' stroke-width='5'/>"
          f"<path d='M{cx - r} {cy + 95} L{cx - r} {cy - 2 + r} A{r} {r} 0 0 1 {cx + r} {cy - 2 + r} "
          f"L{cx + r} {cy + 95} Z' fill='{FILL}' stroke='{INK}' stroke-width='5'/>")
label = (f"<text x='{cx}' y='{cy + R + 60}' text-anchor='middle' font-size='40' fill='{INK}' "
         f"font-weight='bold'>Mennesket i løkka</text>")
svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1600 800' "
       "font-family='Inter, Helvetica Neue, Helvetica, Arial, sans-serif'>"
       f"<defs><marker id='hl' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='4' markerHeight='4' "
       f"orient='auto'><path d='M0 0 L10 5 L0 10 z' fill='{INK}'/></marker></defs>"
       + arc(-70, 70) + arc(110, 250) + person + label + "</svg>")
Path("images/fig-ki-typer-hitl.svg").write_text(svg, encoding="utf-8")
print("wrote images/fig-ki-typer-hitl.svg")
