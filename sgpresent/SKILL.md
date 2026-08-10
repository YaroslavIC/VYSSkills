---
name: sgpresent
description: Create branded SnowGood / «Роботы Севера» one-page technical presentations in portrait A4 format from source text, measurements, tables, formulas, diagrams, and images. Use when Codex is asked for an одностраничная презентация, технический лист, A4 infographic, engineering test summary, experiment comparison, method/result poster, or a new page matching the supplied SGPresent reference style. Produce an editable one-slide PPTX and a visually verified PNG; produce PDF when requested.
---

# SGPresent

Create one portrait A4 page that explains one technical subject and ends with a defensible conclusion.

## Required workflow

1. Read [references/visual-style.md](references/visual-style.md), [references/content-patterns.md](references/content-patterns.md), and [references/qa-checklist.md](references/qa-checklist.md).
2. Inspect all user inputs. Distinguish measured facts, calculations, assumptions, forecasts, and recommendations. Never invent a metric or silently upgrade a forecast into a result.
3. Select one page pattern from `content-patterns.md`. Write the conclusion first, then retain only the evidence needed to support it.
4. Use `assets/logo.png` unchanged. Use `assets/references/*.png` as visual references only; do not copy their subject-specific text into a new presentation.
5. Apply the local `Presentations` skill and its PowerPoint workflow. Build an editable one-slide PPTX with an A4 portrait canvas (210 × 297 mm; aspect ratio 1:1.4142).
6. Run the presentation overflow diagnostics, then render the slide to PNG and inspect it at full size. Check every text box, table cell, caption, callout, and page edge for clipped text, text extending beyond its frame, or content leaving the slide canvas.
7. If any overflow, clipping, collision, unsafe edge placement, suspicious wrapping, or weak visual hierarchy appears, shorten the copy or enlarge/rearrange the container while preserving the role-based type minimums in `visual-style.md`. Render and inspect again. Do not deliver until both automated diagnostics and visual inspection pass. Export PDF only when requested.

## Content rules

- Write visible copy in Russian unless the user requests another language.
- Make the title state the subject; make the final callout state the decision or engineering consequence.
- Prefer concrete numbers, units, conditions, and comparisons over generic claims.
- Mark estimates explicitly: `оценка`, `прогноз`, `ожидаемая точность`, or `рабочая гипотеза`.
- Preserve supplied formulas and units exactly unless correcting an obvious error; disclose corrections.
- Keep the page understandable in this order: title → task → method/evidence → result → conclusion → caveat.
- Use tables only for genuine comparison. Use a short process flow only when sequence or causality matters.
- Do not add decorative stock imagery, fake charts, invented icons, or unsupported precision.

## Deliverables

- Always return the editable `.pptx` and the rendered `.png`.
- Deliver files only after the final render passes the visual overflow check.
- Return `.pdf` when the user requests print distribution.
- Preserve source files and save new outputs separately.
- Mention missing evidence or unresolved assumptions in the handoff.
