"""Fill the RITMO facts box in index.html from the RITMO presentation's numbers.

Reads ~/github/ritmo-presentation/data/numbers.json (people per category from the annual reports,
fellows, defences, countries, NVA publications) and rewrites the text between
<!-- RITMOFACTS:BEGIN --> and <!-- RITMOFACTS:END -->. Run from presentation/.
"""
import json
import re
from pathlib import Path

N = json.loads((Path.home() / "github/ritmo-presentation/data/numbers.json").read_text())
last = str(N["staff-last-year"])
people = N["people"][last]
employed = sum(v for k, v in people.items() if k != "Guest researchers")
guests = people["Guest researchers"]

rows = [
    '<p class="disc">Musikkvitenskap + psykologi + informatikk</p>',
    f'<p><b>{employed}</b> personer og <b>{guests}</b> gjesteforskere i {last}</p>',
    f'<p><b>{N["fellows"]}</b> stipendiater og postdoktorer siden 2017</p>',
    f'<p><b>{N["phd-defences"]}</b> doktorgrader</p>',
    f'<p><b>{N["staff-countries"]}</b> land</p>',
    f'<p><b>{N["articles"]}</b> artikler</p>',
]
box = '<div class="facts fragment" style="top:auto;bottom:40px;right:auto;left:40px">' + "".join(rows) + "</div>"

p = Path("index.html")
s = p.read_text(encoding="utf-8")
s, n = re.subn(r"(<!-- RITMOFACTS:BEGIN -->).*?(<!-- RITMOFACTS:END -->)",
               lambda m: m.group(1) + "\n  " + box + "\n  " + m.group(2), s, flags=re.S)
assert n == 1, "RITMOFACTS markers not found"
p.write_text(s, encoding="utf-8")
print(f"RITMO facts: {employed} employed, {guests} guests in {last}, {N['fellows']} fellows, "
      f"{N['phd-defences']} defences, {N['staff-countries']} countries, {N['articles']} articles")
