---
name: ui
description: Design, implement, or review dense engineering, scientific, laboratory, SCADA, telemetry, diagnostics, and operator-control interfaces across desktop, web, embedded, and native GUI toolkits. Use when Codex is asked to build or restyle a technical application, dashboard, control panel, data-acquisition UI, live plot screen, device monitor, calibration tool, or status console that needs compact high-information layout, consistent operational states, readable numeric data, and restrained industrial visual design.
---

# UI

Create compact engineering interfaces that prioritize operation, live data, and
clear state over decoration. Apply the visual language independently of the
programming language or GUI toolkit.

## Required workflow

1. Inspect the target application's real workflow, supported viewport, input
   methods, existing component system, and safety-critical actions.
2. Read [references/visual-system.md](references/visual-system.md) before
   designing or editing the interface.
3. Inspect [assets/engineering-ui-reference.png](assets/engineering-ui-reference.png)
   as a visual density and hierarchy reference. Copy its design principles, not
   its subject-specific controls or layout.
4. Identify the primary work surface, frequent controls, global states,
   comparable telemetry, warnings, and event log. Let the target workflow
   determine their positions.
5. Define shared palette, typography, spacing, and component-state tokens before
   styling individual widgets.
6. Implement complete states for buttons, toggles, inputs, status panels,
   telemetry rows, tables, plots, and logs that the application actually uses.
7. Render and inspect the real interface at its smallest and largest supported
   sizes. Test normal, hover where available, focus, pressed, disabled, pending,
   stale, warning, and fault states.
8. Apply [references/qa-checklist.md](references/qa-checklist.md) and revise until
   the relevant checks pass.

## Core rules

- Preserve the application's behavior, safety logic, and established framework.
- Treat the reference as a visual system, never as a fixed screen template.
- Keep the interface dense, dark, neutral, and work-focused.
- Reserve green, yellow, red, and cyan for explicit state meanings.
- Distinguish confirmed, requested/pending, stale, valid OFF, and fault states.
- Use compact aligned rows for changing values and tables for comparable data.
- Make numeric values stable, scannable, unit-bearing, and honest about freshness.
- Keep dangerous actions visible, clearly separated, and difficult to trigger by
  accident.
- Use nearly square corners, thin borders, restrained depth, and minimal motion.
- Never let live text, hover, loading labels, or errors resize stable controls.
- Never bridge missing plot samples with a misleading continuous line.
- Do not create a marketing landing page when the user needs an operational tool.

## Platform adaptation

Translate the visual tokens into the native facilities of the chosen stack:

- PySide/PyQt or Qt/C++: palettes, style sheets, layouts, delegates, and painters;
- Tkinter: ttk styles, frames, grid geometry, and Canvas drawing;
- .NET: resources, styles, templates, grids, and custom drawing;
- web: design tokens, semantic HTML, CSS layout, and canvas/SVG where appropriate;
- embedded/native: theme constants, layout primitives, and hardware-appropriate
  drawing APIs.

Prefer native controls when they can be themed consistently and retain keyboard,
focus, and accessibility behavior. Build custom widgets only when the domain
requires a specialized instrument, plot, or process visualization.

## Delivery

- Implement when the user asks for changes; remain read-only for a review request.
- Report the target sizes and states actually verified.
- Call out any unverified platform behavior, missing data state, or safety state.
- Keep unrelated application logic and files unchanged.
