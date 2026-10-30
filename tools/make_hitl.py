"""Human in the loop: the last layer on the KI types figure (fig-ki-typer-*.svg).

A person pictogram in the empty upper left of the figure, with one arrow from the person to the
line of system types and one arrow back, so the two make a loop through the line. Same
1600 x 800 viewBox as images/ki-admin-autonomi.svg; the line runs from Boter (252, 649) to
Autonome systemer (1330, 162). Writes images/fig-ki-typer-hitl.svg. Run from presentation/.
"""
from pathlib import Path

INK = "#1a202c"
FILL = "#efadb2"
cx, cy = 400, 260
LINE = (252, 649), (1330, 162)


def on_line(x):
    (x0, y0), (x1, y1) = LINE
    return x, y0 + (x - x0) * (y1 - y0) / (x1 - x0)


def curve(p, c, q):
    return (f"<path d='M{p[0]:.0f} {p[1]:.0f} Q{c[0]:.0f} {c[1]:.0f} {q[0]:.0f} {q[1]:.0f}' fill='none' "
            f"stroke='{INK}' stroke-width='9' marker-end='url(#hl)'/>")


# Out: from the person over the top to the line between Assistenter and Agenter.
tx, ty = on_line(760)
out = curve((cx + 70, cy - 40), (720, 170), (tx, ty - 30))
# Back: from the line between Chatboter and Assistenter round underneath to the person.
bx, by = on_line(560)
back = curve((bx - 10, by + 25), (cx + 10, by + 40), (cx, cy + 125))

r = 48
person = (f"<circle cx='{cx}' cy='{cy - 62}' r='38' fill='{FILL}' stroke='{INK}' stroke-width='5'/>"
          f"<path d='M{cx - r} {cy + 95} L{cx - r} {cy - 2 + r} A{r} {r} 0 0 1 {cx + r} {cy - 2 + r} "
          f"L{cx + r} {cy + 95} Z' fill='{FILL}' stroke='{INK}' stroke-width='5'/>")
label = (f"<text x='{cx}' y='{cy - 130}' text-anchor='middle' font-size='40' fill='{INK}' "
         f"font-weight='bold'>Mennesket i løkken</text>")
svg = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1600 800' "
       "font-family='Inter, Helvetica Neue, Helvetica, Arial, sans-serif'>"
       f"<defs><marker id='hl' viewBox='0 0 10 10' refX='7' refY='5' markerWidth='4' markerHeight='4' "
       f"orient='auto'><path d='M0 0 L10 5 L0 10 z' fill='{INK}'/></marker></defs>"
       + out + back + person + label + "</svg>")
Path("images/fig-ki-typer-hitl.svg").write_text(svg, encoding="utf-8")
print("wrote images/fig-ki-typer-hitl.svg")
