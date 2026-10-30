"""4E cognition as stacked SVG layers for click builds, redrawn from the Still Standing figure.

Source: writing/1-Still standing/.../figures/theory/4e-cognition/4e-cognition-crop.pdf. Four panels,
one per layer: kroppsliggjort (arrow through the body), situert (a frame round the person),
enaktiv (an arrow out through the frame), utvidet (an arrow to a thing outside the body). The last
two layers put music under all four and technology for body and mind over them.
Writes images/fig-4e-0..6.svg; layer 0 is empty and sets the size.
Run from presentation/.
"""
from pathlib import Path

W, H = 1920, 960
INK = "#231f20"
FONT = "font-family:'Roboto Condensed',Arial,sans-serif;font-weight:700"
FILL = ["#9a90cf", "#a5cbed", "#efadb2", "#b3e297"]
LABELS = ["Kroppsliggjort", "Situert", "Enaktiv", "Utvidet"]
XS = [240 + 480 * i for i in range(4)]
HEAD_Y, HEAD_R, BODY_TOP, BODY_BOT, BODY_W = 340, 58, 410, 650, 150


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" '
            f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>'
            f'{body}</svg>')


def person(cx, fill):
    r = BODY_W / 2
    return (f'<circle cx="{cx}" cy="{HEAD_Y}" r="{HEAD_R}" fill="{fill}" stroke="{INK}" stroke-width="5"/>'
            f'<path d="M{cx - r} {BODY_BOT} L{cx - r} {BODY_TOP + r} A{r} {r} 0 0 1 {cx + r} {BODY_TOP + r} '
            f'L{cx + r} {BODY_BOT} Z" fill="{fill}" stroke="{INK}" stroke-width="5"/>')


def arrow(x1, y1, x2, y2):
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="10" '
            f'marker-start="url(#a)" marker-end="url(#a)"/>')


def frame(cx):
    return (f'<rect x="{cx - 185}" y="{HEAD_Y - 110}" width="370" height="{BODY_BOT + 40 - HEAD_Y + 110}" '
            f'rx="40" fill="none" stroke="{INK}" stroke-width="5"/>')


def label(cx, text):
    return f'<text x="{cx}" y="790" text-anchor="middle" font-size="58" fill="{INK}" style="{FONT}">{text}</text>'


def panel(i):
    cx = XS[i]
    if i == 0:
        art = person(cx, FILL[i]) + arrow(cx, HEAD_Y - 20, cx, BODY_BOT - 50)
    elif i == 1:
        art = frame(cx) + person(cx, FILL[i])
    elif i == 2:
        art = frame(cx) + person(cx - 30, FILL[i]) + arrow(cx - 10, 560, cx + 250, 560)
    else:
        art = (person(cx - 60, FILL[i])
               + f'<rect x="{cx + 120}" y="500" width="90" height="120" rx="14" fill="{FILL[i]}" '
                 f'stroke="{INK}" stroke-width="5"/>'
               + arrow(cx - 40, 560, cx + 100, 560))
    return art + label(cx, LABELS[i])


music = (f'<rect x="60" y="850" width="{W - 120}" height="96" rx="48" fill="#ffffff" stroke="{INK}" stroke-width="5"/>'
         f'<text x="{W / 2}" y="916" text-anchor="middle" font-size="60" fill="{INK}" style="{FONT}">Musikk</text>')

tech = (f'<rect x="60" y="40" width="{W - 120}" height="96" rx="48" fill="#ffffff" stroke="{INK}" stroke-width="5" '
        f'stroke-dasharray="18 12"/>'
        f'<text x="{W / 2}" y="106" text-anchor="middle" font-size="60" fill="{INK}" style="{FONT}">'
        f'Teknologi for kropp og sinn</text>')

layers = [""] + [panel(i) for i in range(4)] + [music, tech]
for i, body in enumerate(layers):
    Path(f"images/fig-4e-{i}.svg").write_text(svg(body), encoding="utf-8")
print(f"wrote images/fig-4e-0..{len(layers) - 1}.svg")
