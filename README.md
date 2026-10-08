# Immaculate Gardens

Client-facing bilingual website for Saul Emanuel Urias Rodriguez, Japanese Garden Artist & Designer serving the Portland, Oregon metro area.

## Contents

- Artist introduction and garden philosophy
- Consultation, design, signature commissions, and stewardship
- English and Spanish text
- One-page inquiry form with direct email delivery

The inquiry form submits through FormSubmit to `immaculategardensllc@gmail.com`. The recipient must activate FormSubmit using its one-time inbox confirmation after the first submission before delivery is enabled. The form preserves input on errors, prevents duplicate submissions, and provides a direct email link as a fallback. Name, email, and message are required; service and location are optional. Submission behavior was tested with mocked responses; actual inbox delivery requires recipient activation and a live submission. The garden image is an illustrative generated study, not a photograph of Saul's work.

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
