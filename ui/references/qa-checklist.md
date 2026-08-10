# Engineering UI QA checklist

## Workflow and hierarchy

- The primary operator task is visible immediately.
- Global state and safety actions remain visible without scrolling.
- Controls are grouped by real function and ordered by operational importance.
- The central area is assigned to the application's primary work surface.
- Comparable data uses aligned rows or tables rather than separate cards.

## Visual system

- Neutral dark surfaces dominate the screen.
- Green, yellow, red, cyan, and gray follow the defined state semantics.
- Panels and controls use compact `2-3 px` corners and restrained depth.
- Headings, labels, values, logs, and plots follow the typography hierarchy.
- Spacing is dense but functional; shared edges align.
- No marketing, glass, decorative blobs, or oversized card treatment appears.

## States and behavior

- Buttons have normal, focus, pressed, disabled, and hover states where relevant.
- Device-backed toggles distinguish ON, OFF, pending, and stale/unknown.
- Pending commands do not look confirmed.
- Stale and missing data do not look live or equal to a valid zero.
- Dangerous actions are separated and confirmed when irreversible.
- Live updates do not move controls or steal focus.

## Data display

- Every live value has a clear label, unit, stable precision, and freshness where
  needed.
- Numeric values do not shift the surrounding layout.
- Long values wrap or elide intentionally without hiding critical information.
- Tables align comparable values and remain visible at the target size.
- Logs contain events rather than high-rate telemetry spam.
- Missing plot samples appear as gaps, not straight connecting lines.
- Plot curves and their axes share color and do not overlap other scales.

## Adaptation and accessibility

- Verify the smallest and largest supported window or display.
- Verify long labels, large numbers, localization, and 200% zoom where supported.
- Verify keyboard-only operation and visible focus.
- Verify reduced-motion behavior.
- Verify that text and controls do not overlap or leave the usable screen.
- Verify sufficient text contrast in every status state.

## Delivery

- Inspect the rendered application, not source code alone.
- Record the viewports, platforms, and interaction states tested.
- Report unverified behavior and unresolved safety or stale-data states.
- Preserve application behavior and unrelated files.
