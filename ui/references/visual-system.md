# Engineering interface visual system

## Contents

1. Character
2. Palette and state semantics
3. Typography
4. Density and geometry
5. Panels and headings
6. Header status panels
7. Buttons and toggles
8. Inputs
9. Telemetry rows
10. Tables
11. Logs
12. Plots
13. Layout and adaptation
14. Accessibility and safety
15. Prohibited patterns

## 1. Character

Design the interface as a dense engineering instrument screen: closer to SCADA,
an oscilloscope, a laboratory monitor, or an industrial control panel than to a
consumer website.

Use dark neutral surfaces, compact controls, thin borders, high information
density, visible live state, shared alignment edges, and restrained depth. Build
hierarchy with position, contrast, typography, and spacing rather than large
cards or decoration.

## 2. Palette and state semantics

| Role | Color |
| --- | --- |
| Application background | `#101315` |
| Header | `#15191b` |
| Main panel | `#181c1f` |
| Deep panel | `#161a1d` |
| Value/control surface | `#20262a` |
| Input surface | `#111518` |
| Log/plot surface | `#080b0d` |
| Main border | `#343b40` |
| Soft row border | `#252e33` |
| Control border | `#4c5860` |
| Primary text | `#e8edf1` |
| Strong heading text | `#f1f5f7` |
| Muted label text | `#9eabb5` |
| Disabled/stale text | `#87939b` |
| OK | `#65d46e` |
| OK text | `#72dc82` |
| Warning/pending | `#f2c14e` |
| Fault/alarm | `#ff6961` |
| Fault text | `#ff7777` |
| Active selection/reference | `#28c7e8` |

State meanings are fixed:

| State | Treatment |
| --- | --- |
| Normal, online, confirmed ON | Muted green |
| Warning, waiting, pending | Yellow |
| Fault, alarm, stop, destructive | Red |
| Selected, navigation, reference | Cyan |
| Valid OFF | Neutral dark |
| Unknown, stale, no data | Subdued gray |

Tint state backgrounds lightly. Let text and border carry state. Never show stale
data as green, use red for ordinary selection, or use green as decoration.

## 3. Typography

Use a neutral system sans-serif comparable to Segoe UI at about `13 px` with
line height near `1.3`. Use the closest native platform font.

- Application title: `15 px`.
- Panel heading: `12 px`, semibold.
- Buttons: `11-13 px`.
- Input and telemetry labels: `10-11 px`, muted.
- Telemetry values: `12 px`, preferably monospace or tabular digits.
- Logs, IDs, timestamps, firmware strings, and numeric streams: monospace.
- Keep letter spacing at zero; never use negative tracking.
- Do not scale font size with viewport width.
- Format precision consistently and prevent changing digits from shifting layout.

## 4. Density and geometry

- Header height: approximately `42 px`.
- Main outer padding and gap: `6 px`.
- Panel padding: `7 px`.
- Functional group padding and separation: `6 px`.
- Compact control-grid gap: `5 px`.
- Normal control height: `30 px`.
- Compact short-screen control height: `28 px`.
- Panel, row, button, and input corner radius: `2-3 px`.
- Stabilize fixed-format widgets with explicit tracks, aspect ratios, and bounds.

Compact does not mean cramped. Separate distinct functional groups more than
controls inside one group. Keep critical actions visible without scrolling.

## 5. Panels and headings

Main panels use a `#161a1d` surface, `#323a40` one-pixel border, `7 px` padding,
and at most a barely visible inner highlight.

Functional groups use a `#15191c..#191e21` dark surface, `#30383e` one-pixel
border, `3 px` radius, and approximately `6 px` spacing. Use one group per real
function. Do not put decorative cards inside cards.

Panel headings remain compact. Prefix them with a small `3 x 11 px` neutral
blue-gray (`#55707e`) rectangular marker with about `1 px` radius. Do not use a
large decorative icon.

## 6. Header status panels

Use the top row for important global states. These are informational panels, not
ordinary buttons.

- Height: `30 px`.
- Radius: `3 px`.
- Dark, lightly state-tinted surface.
- Thin border from the state color family.
- Concise single-line text.
- A `5 x 14 px` rectangular status LED on the left with `1 px` radius and a
  restrained glow.
- LED colors follow normal/warning/fault/unknown semantics.

Only top-row status panels use the rectangular LED. Tables and telemetry rows
may use smaller circular indicators when useful.

## 7. Buttons and toggles

### Normal command

Use a button about `30 px` high and at least `84 px` wide, `3 px` radius,
`#4c5860` border, `#20262b..#293137` dark face, primary text, and a restrained
one-pixel highlight/shadow. Labels may wrap to two lines to preserve a compact
matrix.

### Primary command

Use a dark muted-green face, green border, and light-green text. Limit primary
emphasis to the main safe actions in the current context.

### Dangerous command

Use a dark-red face, red border, and light-red or white text. Separate dangerous,
destructive, emergency, power, stop, reset, or actuator actions from routine
commands. Confirm irreversible actions.

### Stateful toggle

Render every device-backed toggle with four explicit states:

- ON: muted green;
- OFF: standard dark button;
- PENDING: muted yellow;
- UNKNOWN/STALE: subdued gray.

Do not show the requested state as confirmed before backend/device acknowledgement.

### Interaction

- Hover-capable devices: slightly lighten face and border.
- Pressed: use a subtle inset effect or scale near `0.97`.
- Keyboard focus: visible `2 px` cyan outline with `1 px` separation.
- Disabled: low-contrast dark face, no elevation, disabled cursor/interaction.
- Transition only relevant properties over about `100-150 ms`.
- Disable nonessential motion under reduced-motion settings.

Motion is never the only state cue.

## 8. Inputs

Inputs are visually quieter than commands: about `30 px` high, `#3b464d`
border, `3 px` radius, `#111518` face, primary text, `5 px` horizontal inset,
and a subtle recessed effect.

- Use real labels, not placeholder-only identification.
- Keep units visible in the label or stable suffix.
- Align related numeric settings in a grid.
- Use toggles for binary settings and sliders/steppers for meaningful numeric
  adjustment.
- Invalid is red; pending is yellow; accepted remains neutral unless confirmation
  itself is important.
- Validation messages must not move surrounding controls unexpectedly.

## 9. Telemetry rows

Use compact two-column rows: label on the leading side, current value and unit on
the trailing side.

- Label column near `100 px`, flexible value column.
- `2 px` vertical separation.
- `#252e33` border and `2 px` radius.
- `#181d20` base surface.
- Label: `11 px`, muted, `3 x 6 px` inset.
- Value: minimum height near `22 px`, `3 x 7 px` inset, `#20262a` surface,
  `12 px` monospace text.

Tint only the value area for OK/warning/fault. Keep labels neutral. Every changing
value needs a clear name, unit, fixed precision, stable width, and freshness when
relevant. Display `—` or `NO DATA` for unknown values; do not leave an old value
looking current.

## 10. Tables

Use tables for comparable channels or repeated devices rather than fragmenting
them into cards.

- Compact rows and muted `11 px` headers.
- `12 px` body values; numeric columns use monospace/tabular digits.
- Thin borders and dark row surfaces.
- Align numbers consistently; put shared units in headers.
- Use small circular status dots only where they improve scanning.
- Avoid horizontal scrolling at the primary supported size.

## 11. Logs

Use `#080b0d` background, `#283036` border, `#dbe6ee` text, `12 px` monospace
type, line height near `1.3`, `6 px` padding, preserved line breaks, and explicit
vertical scrolling.

Logs contain events, commands, acknowledgements, warnings, and faults. Keep
routine high-rate telemetry in value panels, plots, or files. Color only severity,
not every subsystem name.

## 12. Plots

Use a nearly black plotting surface with subtle grid lines. Keep decoration
neutral and let curve colors carry data identity.

- Give quantities with different scales separate Y axes.
- Match axis, curve, ticks, and label color.
- Place extra axes outside the plot on left and right without overlap.
- Use a running time axis for live data.
- Autoscale without permanently clipping a transient; keep a useful minimum
  range so stationary noise remains readable.
- Decouple ingestion from redraw; target `10-30 FPS` unless less is sufficient.
- Render missing samples as gaps, never misleading straight bridges.
- Keep legends compact and outside important data.
- Put graph commands in a toolbar, not over the plotted data.

Suggested data colors: cyan/light blue, green, amber/orange, restrained magenta,
and white/gray for aggregate/reference. Avoid confusing a normal curve with alarm
red.

## 13. Layout and adaptation

Let workflow determine exact placement. A useful default hierarchy is:

- top: global state and primary safety actions;
- leading side: frequent controls and settings;
- center: primary work surface, plot, image, process view, or table;
- trailing side: compact values, comparable subsystems, and warnings;
- bottom: event log or secondary detail.

Use the toolkit's grid/layout manager and explicitly shrinkable flexible tracks.
Prevent live text, loading labels, and errors from expanding a panel. Choose
breakpoints when content stops fitting, not from generic device names.

On short screens, first reduce group padding, row spacing, and telemetry height.
Do not shrink critical hit areas or primary content prematurely.

## 14. Accessibility and safety

- Prefer native semantic controls and preserve keyboard behavior.
- Label every input and icon-only command.
- Keep focus visible.
- Never use color as the sole state cue.
- Keep text readable on tinted backgrounds.
- Require confirmation for irreversible dangerous actions.
- Pending cannot look confirmed; stale cannot look live.
- Live updates must not steal focus or move controls.
- Reserve flashing for urgent states and disable it under reduced motion.

## 15. Prohibited patterns

- Marketing hero sections or landing pages instead of the actual tool.
- Oversized headings and large empty regions.
- Decorative card grids or cards nested inside cards.
- Large rounded pills for ordinary content.
- Glassmorphism, background blobs, or decorative gradients.
- Purple/blue, beige, brown, or any other one-note dominant palette.
- Colored controls without state meaning.
- Animation competing with live data.
- Text overlap, clipped critical data, or controls that resize with content.
