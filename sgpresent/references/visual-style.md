# SGPresent visual style

## Reference assets

Inspect all three files before composing a new page:

- `../assets/references/gnss-antennas-a4.png`
- `../assets/references/camera-laser-a4.png`
- `../assets/references/camera-accuracy-a4.png`

Treat the samples as the final authority when a written rule and the visual evidence differ.

## Canvas and grid

- Use portrait A4: 210 × 297 mm.
- Keep a full-width dark navy header occupying roughly 9–12% of page height. This is 70% of the height used in the original references; preserve the reference color while making the header visibly more compact.
- Place the logo at the upper left. Align the title and subtitle in a column to its right.
- Use consistent outer margins, approximately 5–7% of page width.
- Organize the body into two to four horizontal bands. Align edges across bands.
- Fill the page, but preserve visible gaps between sections. Avoid tiny orphaned elements.

## Palette

Sample colors from the references when exact matching matters. Use these starting values:

| Role | Approximate color |
|---|---|
| Header navy | `#031B34` |
| Deep panel blue | `#0A355D` |
| Medium blue | `#0D5B89` |
| Accent cyan | `#00A3E0` |
| Pale blue | `#CBEAFA` |
| Page background | `#EFF8FD` |
| Primary text | `#08223A` |
| Secondary text | `#607D96` |
| Warning orange | `#E77D00` |

Use orange only for a losing option, warning, or failed threshold. Do not introduce unrelated accent colors.

## Typography

- Use a clean sans-serif with Cyrillic support. Prefer Arial or Aptos when no house font is supplied.
- Use bold or semibold for titles, section headings, metrics, table headers, and conclusions.
- Use white for the main title, pale cyan for the header subtitle, and cyan for body section headings.
- Keep the main title to one or two lines. Never shrink it into body-text scale.
- Treat 12 pt as an emergency lower bound for secondary text, not as a universal target. Use these role-based minimums:

| Text role | Minimum | `artifact-tool` equivalent |
|---|---:|---:|
| Footnote or secondary caption | 12 pt | 16 px |
| Body copy, table cell, image caption | 14 pt | 19 px |
| Card or diagram-node heading | 16 pt | 22 px |
| Step number or navigation marker | 20 pt | 27 px |
| Key metric | 24 pt | 32 px |

- In `artifact-tool`, `fontSize` uses CSS pixels, not PowerPoint points. Convert with `px = pt × 96 / 72`; for example, 12 pt = 16 px and 14 pt ≈ 19 px.
- Make semantic hierarchy visible, not merely compliant with the absolute minimum. Step numbers, navigation markers, and key metrics must be recognizable at whole-page A4 view and clearly larger or more prominent than nearby body text.
- Align numeric comparisons and retain nonbreaking spaces between values and units when practical.

## Components

- Use rounded rectangles with a thin cyan outline for light panels.
- Use solid deep-blue panels for goals, key results, and contrast blocks.
- Use pale-blue panels for conclusions and recommendations.
- Use simple cyan arrows in process flows. Keep connectors behind nodes.
- Crop technical images cleanly and label each image immediately below it.
- Keep tables flat: dark-blue header, light body, subtle rules, selective pale-blue highlighting.
- Avoid gradients, drop shadows, glass effects, decorative patterns, and UI-like buttons.

## Logo

Use `../assets/logo.png` without recoloring, stretching, redrawing, or placing text over it. Preserve aspect ratio and sufficient clear space.
