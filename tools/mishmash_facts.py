"""Count MishMash facts from the mishmash-web source and write them into index.html.

Reads ~/github/mishmash-web/site: _data/centre_funding.yml (RCN funding, from Prosjektbanken),
_data/partners.yml (partner lists by key) and _directory/people/ (one folder per person), and
replaces the block between <!-- FACTS:BEGIN --> and <!-- FACTS:END --> in index.html.
Run from presentation/ with the folder's .venv.
"""
import re
from pathlib import Path

import yaml

SITE = Path.home() / "github" / "mishmash-web" / "site"
fund = yaml.safe_load((SITE / "_data" / "centre_funding.yml").read_text(encoding="utf-8"))
partners = {g["key"]: len(g["entries"]) for g in yaml.safe_load((SITE / "_data" / "partners.yml").read_text(encoding="utf-8"))}
people = sum(1 for p in (SITE / "_directory" / "people").iterdir() if (p / "index.md").exists())

mnok = round(fund["amount_nok"] / 1e6)
block = (f'<!-- FACTS:BEGIN -->\n'
         f'  <div class="facts fragment"><p><b>{mnok}</b> mill. kr fra Forskningsrådet, {fund["start_year"]}–{fund["end_year"]}</p>'
         f'<p><b>{partners["research"]}</b> forskningspartnere</p>'
         f'<p><b>{partners["other"]}</b> partnere i kulturliv, offentlig sektor og næringsliv</p>'
         f'<p><b>{partners["international"]}</b> internasjonale partnere</p>'
         f'<p><b>{people}</b> personer</p></div>\n'
         f'  <!-- FACTS:END -->')
p = Path("index.html")
s = p.read_text(encoding="utf-8")
s, n = re.subn(r"<!-- FACTS:BEGIN -->.*?<!-- FACTS:END -->", block, s, flags=re.S)
assert n == 1, f"expected one FACTS block, found {n}"
p.write_text(s, encoding="utf-8")
print(f"{mnok} MNOK ({fund['source']}, fetched {fund['fetched']}); partners {partners}; {people} people")
