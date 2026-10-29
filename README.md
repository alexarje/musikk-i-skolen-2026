# Verden i dag og verden i morgen

Slides in Norwegian for the talk "Verden i dag og verden i morgen: hvor er vi på vei? Menneskets kreative potensiale i lys av KI" at Kultur- og skolekonferansen 2026 (Musikk i Skolen and Norges musikkhøgskole), M28 Auditorium, Møllergata 28, Oslo, Friday 30 October 2026, 13.30 to 13.50. The deck is `index.html` in the MishMash 2026 identity; the flat PDF is `musikk-i-skolen-2026-10-30.pdf`. Press S for the notes, D for dark mode.

The deck is built in question strips, each opened by a coloured divider: the title, the roles ring, fourMs, RITMO and MishMash slides; the MishMash strip (logo, bubbles, sentence, work packages, cube, live network); KI? (KI is not one thing, the six system types, data plus algorithm equals model with one model in many tools, and more below); Musikk? (the musicking quadrant with KI in the middle); Skolen? (music connecting the school subjects, and what music influences); Fremtiden? (explore, reflect, create; what MishMash can do and what schools must do); Eksempler (the Firefly QR code and two demos from `apps/`); and the closing cycle around the MishMash logo, with the co-creation loop below it. Almost everything builds on click. Click outside an embedded demo before using the arrow keys again.

The site is deployed to GitHub Pages by `.github/workflows/pages.yml` on every push to `main`; nothing is built, the folder is uploaded as it stands. The PDF, the screenshots in `.shots/` and the venv are not in the repository.

The demos are single-file apps copied from `~/github/Music-AI-introduction/apps/` (commit 055af95) and run with no network. The copy of `next-token-sampler` has one addition: `?no` starts it with the Norwegian sample loaded. The spectrogram asks for the microphone. The Firefly app is not copied; the QR code points to https://fourms.github.io/omo/apps/firefly/, the GitHub Pages site of the fourMs/omo repository, so the audience needs mobile data or the venue network.

## Abstract

Kunstig intelligens (KI) er ikke én ting, og den er ikke ny. Musikk har vært med i utviklingen av KI fra de første datamaskinene, og dagens modeller er først og fremst blitt gode til å lage produkter: en låt, et bilde, en tekst. Det nye er skalaen og de kommersielle kreftene bak, og det gir grunn til å være kritisk, men ikke til å være imot. I dette innlegget argumenterer jeg for at det er nettopp derfor de praktiske og estetiske fagene blir viktigere, ikke mindre viktige, i fremtidens skole. Musikk er først og fremst en prosess, ikke et produkt: å skape, å utøve, å oppleve og å forstå. Den prosessen kan ingen maskin gjennomføre på vegne av elevene. Med eksempler fra egen undervisning viser jeg hvordan KI kan brukes til det som kan gjøres utenfor timen, slik at timen kan brukes på det bare mennesker kan gjøre sammen: lytte, synge, bygge, diskutere. Til slutt peker jeg på hva elever, lærere, skoleledere og lærerutdanningen kan gjøre: lage selv, også med maskiner, forstå hvordan teknologien virker, beskytte elevenes stemmer, bilder og data, og ta KI inn i de praktisk-estetiske fagene og ikke bare i IKT. Er fagene pynt eller motor? Mitt svar er motor.

The 300- and 400-word versions are in `../abstract.md`.

## Building

From this folder:

    .venv/bin/python tools/build_pdf.py --out musikk-i-skolen-2026-10-30.pdf
    .venv/bin/python tools/notes_sheet.py        # regenerate ../notes.md
    .venv/bin/python tools/make_qr.py            # regenerate images/qr-firefly.svg and .png

`lib/`, `fonts/`, `logo/`, `js/`, `tools/`, `images/rcn-logo.svg` and `images/qr-mishmash.svg` are copied from the 4 November 2026 roundtable deck (`../../2026-11-04-Dep-møte/presentation/`). The venv here holds pillow and segno (`tools/requirements.txt`). `images/fig-syklus-*.svg` are copied from the BI lecture deck (`../../2026-11-09-BI-forelesning/presentation/`), where `tools/make_figures.py` draws them.

## Sources

The text is drawn from his own posts on arj.no: musikk-ki-fredrikstad (process not product, the musicking quadrant, the trombone, "imot strøm"), ki-utdanning-idemote (KI outside the lesson, more machine more human, open teaching material), ki-i-scenekunstfagene-yellow-brick-road (train a model, sew a button, stand on a stage; reflect, document, credit) and mellom-menneske-og-maskin (Boden, new and valuable). The MishMash education work package and its partners are from the project description in the funding agreement (`Aktiv/MishMash-ARJ/13-kontrakt4/357438_Document_270571.pdf`). The photographs on the slides are the Kristiansand group photo (Hadle Kloster, UiA) and three from `~/github/mishmash-presentation/images/` (a classroom from the education work package, the opening panel and the hackathon). `images/` also holds the figures and photographs of the earlier 30-slide version, which is kept whole in `../presentation-backup-2026-10-28/`.
