#!/usr/bin/env python3
"""Writes QR codes for the phone apps as images/qr-<app>.svg and .png (Firefly, Pinch Bass).

The address is the GitHub Pages site of the fourMs/omo repository (Pages source: the workflow
.github/workflows/pages.yml, html_url https://fourms.github.io/omo/), plus the app's folder
apps/<app>/. The script decodes nothing itself; check the printed address against the slide.
Run from presentation/:

    .venv/bin/python tools/make_qr.py
"""
import os
import segno

APPS = ["firefly", "pinch-bass"]
BASE = "https://fourms.github.io/omo/apps/{}/"
HERE = os.path.dirname(os.path.abspath(__file__))
IMG = os.path.join(os.path.dirname(HERE), "images")


def main():
    for app in APPS:
        url = BASE.format(app)
        qr = segno.make(url, error="m", micro=False)
        for ext in ("svg", "png"):
            qr.save(os.path.join(IMG, f"qr-{app}.{ext}"), scale=20, border=2, dark="#231f20", light="#ffffff")
        print(f"wrote qr-{app}.svg and .png for", url, "version", qr.version, qr.error)


if __name__ == "__main__":
    main()
