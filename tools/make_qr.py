#!/usr/bin/env python3
"""Writes the QR code for the Firefly app as images/qr-firefly.svg and images/qr-firefly.png.

The address is the GitHub Pages site of the fourMs/omo repository (Pages source: the workflow
.github/workflows/pages.yml, html_url https://fourms.github.io/omo/), plus the app's folder
apps/firefly/. The script decodes nothing itself; check the printed address against the slide.
Run from presentation/:

    .venv/bin/python tools/make_qr.py
"""
import os
import segno

URL = "https://fourms.github.io/omo/apps/firefly/"
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(HERE), "images")


def main():
    qr = segno.make(URL, error="m", micro=False)
    qr.save(os.path.join(IMG, "qr-firefly.svg"), scale=20, border=2, dark="#231f20", light="#ffffff")
    qr.save(os.path.join(IMG, "qr-firefly.png"), scale=20, border=2, dark="#231f20", light="#ffffff")
    print("wrote qr-firefly.svg and qr-firefly.png for", URL, "version", qr.version, qr.error)


if __name__ == "__main__":
    main()
