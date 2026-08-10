---
name: kzpresent
description: Create branded «Кузбасс-ЦОТ» one-page technical presentations in a green corporate style as visually verified portrait A4 PNG images from source text, measurements, tables, formulas, diagrams, and images. Use when Codex is asked for a KZCOT or Kuzbass-COT одностраничная презентация, технический лист, A4 infographic, engineering test summary, experiment comparison, method/result poster, project proposal, or another corporate PNG page.
---

# KZPresent

Create one portrait A4 page in the «Кузбасс-ЦОТ» corporate style. Explain one technical subject and end with a defensible conclusion.

## Required workflow

1. Read [references/visual-style.md](references/visual-style.md), [references/content-patterns.md](references/content-patterns.md), and [references/qa-checklist.md](references/qa-checklist.md).
2. Inspect all user inputs. Distinguish measured facts, calculations, assumptions, forecasts, and recommendations. Never invent a metric or silently upgrade a forecast into a result.
3. Select one page pattern from `content-patterns.md`. Write the conclusion first, then retain only the evidence needed to support it.
4. Use `assets/logo.jpg` unchanged as the corporate logo. Use `assets/references/*.png` only for structural composition; ignore their blue palette and SnowGood branding.
5. Use a precise layout workflow that supports deterministic text bounds and high-resolution raster export. Build directly for a portrait A4 canvas (aspect ratio 1:1.4142) and export the final page as PNG. Do not use a generative image model to render the page's text.
6. Run available layout or bounds diagnostics, then inspect the exported PNG at full size. Check every text box, table cell, caption, callout, and page edge for clipped text, text extending beyond its frame, or content leaving the canvas.
7. If any overflow, clipping, collision, unsafe edge placement, or suspicious wrapping appears, shorten the copy or enlarge/rearrange the container while preserving the 12 pt minimum. Export and inspect again. Do not deliver until both automated diagnostics and visual inspection pass.

## Content rules

- Write visible copy in Russian unless the user requests another language.
- Show a date in the header in `ДД.ММ.ГГГГ` format. Prefer the user-supplied event, test, measurement, or reporting date; otherwise use the document creation date. Never present the creation date as the date of an experiment.
- Make the title state the subject; make the final callout state the decision or engineering consequence.
- Prefer concrete numbers, units, conditions, and comparisons over generic claims.
- Mark estimates explicitly: `оценка`, `прогноз`, `ожидаемая точность`, or `рабочая гипотеза`.
- Preserve supplied formulas and units exactly unless correcting an obvious error; disclose corrections.
- Keep the page understandable in this order: title → task → method/evidence → result → conclusion → caveat.
- Use tables only for genuine comparison. Use a short process flow only when sequence or causality matters.
- Do not add decorative stock imagery, fake charts, invented icons, or unsupported precision.

## Deliverables

- Return only the final `.png` as the user-facing document.
- Deliver files only after the final render passes the mandatory visual overflow check.
- Preserve source files and save new outputs separately.
- Mention missing evidence or unresolved assumptions in the handoff.
