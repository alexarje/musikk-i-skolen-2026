"""Social and embodied computing as stacked SVG layers, the bridge to the phone apps.

Same person figures as make_4e.py. Layer 1: one person with a phone in the hand and an arrow for
the motion that plays it (kroppslig). Layer 2: four more people with phones. Layer 3: dashed arcs
over the heads between all the phones (sosial).
Writes images/fig-sosial-0..3.svg; layer 0 is empty and sets the size. Run from presentation/.
"""
from itertools import combinations
from pathlib import Path

W, H = 1920, 960
INK = "#231f20"
FONT = "font-family:'Roboto Condensed',Arial,sans-serif;font-weight:700"
FILL = ["#b3e297", "#9a90cf", "#a5cbed", "#efadb2", "#9a90cf"]
# Centre first, then two on each side, in one row.
PEOPLE = [(960, 400), (600, 400), (1320, 400), (240, 400), (1680, 400)]
S = 1.0


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}">'
            f'<defs><marker id="a" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="4" markerHeight="4" '
            f'orient="auto-start-reverse"><path d="M0 0 L10 5 L0 10 z" fill="{INK}"/></marker></defs>'
            f'{body}</svg>')


def phone_at(x, y):
    return x + 105 * S, y - 10 * S


def person(x, y, fill):
    r, hr = 75 * S, 58 * S
    top, bot = y + 70 * S, y + 310 * S
    px, py = phone_at(x, y)
    return (f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{hr:.0f}" fill="{fill}" stroke="{INK}" stroke-width="5"/>'
            f'<path d="M{x - r:.0f} {bot:.0f} L{x - r:.0f} {top + r:.0f} A{r:.0f} {r:.0f} 0 0 1 {x + r:.0f} {top + r:.0f} '
            f'L{x + r:.0f} {bot:.0f} Z" fill="{fill}" stroke="{INK}" stroke-width="5"/>'
            f'<rect x="{px - 22:.0f}" y="{py - 40:.0f}" width="44" height="80" rx="8" fill="#ffffff" '
            f'stroke="{INK}" stroke-width="5"/>')


def label(text, y):
    return f'<text x="{W / 2}" y="{y}" text-anchor="middle" font-size="60" fill="{INK}" style="{FONT}">{text}</text>'


x0, y0 = PEOPLE[0]
px0, py0 = phone_at(x0, y0)
one = (person(x0, y0, FILL[0])
       + f'<line x1="{px0 + 50:.0f}" y1="{py0 - 70:.0f}" x2="{px0 + 50:.0f}" y2="{py0 + 70:.0f}" stroke="{INK}" '
         f'stroke-width="10" marker-start="url(#a)" marker-end="url(#a)"/>'
       + label("Kroppslig", 870))
many = "".join(person(x, y, f) for (x, y), f in zip(PEOPLE[1:], FILL[1:]))


def arc(a, b):
    (x1, y1), (x2, y2) = phone_at(*a), phone_at(*b)
    lift = 0.22 * abs(x2 - x1)
    return (f'<path d="M{x1:.0f} {y1 - 45:.0f} Q{(x1 + x2) / 2:.0f} {y1 - 45 - 2 * lift:.0f} {x2:.0f} {y2 - 45:.0f}" '
            f'fill="none" stroke="{INK}" stroke-width="4" stroke-dasharray="14 12"/>')


links = "".join(arc(a, b) for a, b in combinations(PEOPLE, 2)) + label("og sosial", 950)

for i, body in enumerate(["", one, many, links]):
    Path(f"images/fig-sosial-{i}.svg").write_text(svg(body), encoding="utf-8")
print("wrote images/fig-sosial-0..3.svg")
