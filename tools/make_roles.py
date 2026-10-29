"""The professor's many roles as one figure, built on click.

Writes images/fig-roller-0.svg (the portrait in the middle with one ring around it) and
images/fig-roller-1..N.svg, one role bubble on the ring per layer, stacked in the slide so that
each click adds a role. Headings only, no numbers. Run from presentation/.
"""
import base64
import math
from pathlib import Path

# Clockwise from the top. Skaper sits next to Forfatter; Sensor between Veileder and Underviser.
roles = ["Forsker", "Forfatter", "Skaper", "Formidler", "Inspirator", "Innovatør",
         "Entreprenør", "Leder", "Veileder", "Sensor", "Underviser"]
colours = ["#9a90cf", "#b3e297", "#a5cbed", "#efadb2"]

W, H = 1920, 1000
cx, cy, ring, r_role, r_me = W / 2, H / 2, 380, 92, 190
INK = "#231f20"
FD = "font-family:'Roboto Condensed',Arial,sans-serif;font-weight:700"
photo = base64.b64encode((Path("images") / "arj-portrett-2025.png").read_bytes()).decode()


def svg(body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="0 0 {W} {H}" width="{W}" height="{H}">{body}</svg>')


base = (f'<defs><clipPath id="pc"><circle cx="{cx}" cy="{cy}" r="{r_me}"/></clipPath></defs>'
        f'<circle cx="{cx}" cy="{cy}" r="{ring}" fill="none" stroke="{INK}" stroke-width="4"/>'
        f'<image x="{cx - r_me}" y="{cy - r_me}" width="{2 * r_me}" height="{2 * r_me}" '
        f'preserveAspectRatio="xMidYMid slice" clip-path="url(#pc)" xlink:href="data:image/png;base64,{photo}"/>'
        f'<circle cx="{cx}" cy="{cy}" r="{r_me}" fill="none" stroke="{INK}" stroke-width="5"/>')
Path("images/fig-roller-0.svg").write_text(svg(base), encoding="utf-8")

for i, name in enumerate(roles):
    a = math.radians(90 - 360 * i / len(roles))
    x, y = cx + ring * math.cos(a), cy - ring * math.sin(a)
    size = 32 if len(name) > 9 else 36
    body = (f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r_role}" fill="{colours[i % 4]}" stroke="{INK}" stroke-width="4"/>'
            f'<text x="{x:.0f}" y="{y + size * 0.35:.0f}" text-anchor="middle" font-size="{size}" fill="{INK}" '
            f'style="{FD}">{name}</text>')
    Path(f"images/fig-roller-{i + 1}.svg").write_text(svg(body), encoding="utf-8")

print(f"wrote images/fig-roller-0..{len(roles)}.svg")
