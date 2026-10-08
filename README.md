# Immaculate Gardens

Client-facing bilingual website for Saul Emanuel Urias Rodriguez, Japanese Garden Artist & Designer serving the Portland, Oregon metro area.

## Contents

- Artist introduction and garden philosophy
- Consultation, design, signature commissions, and stewardship
- English and Spanish text
- Three-step project inquiry with copy and download

The inquiry form prepares a local brief; it does not send email or submit to a server. The garden image is an illustrative generated study, not a photograph of Saul's work.

## Run locally

Requires Python 3; no npm dependencies.

```sh
python3 -m http.server 8000
```

Open http://localhost:8000.

## Build

```sh
python3 scripts/build.py
```

The build writes `dist/index.html` with inline CSS and JavaScript, copies the garden image to `dist/`, and writes `immaculate-gardens-saul.html` with the image embedded for a portable single-file version.

Publish `dist/` with any static website host. The repository contains no credentials or hosting account configuration.
