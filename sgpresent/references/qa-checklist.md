# QA checklist

## Evidence

- Every number is supplied, calculated transparently, or explicitly labeled as an estimate.
- Units, decimal separators, dates, and precision are consistent.
- The conclusion follows from visible evidence.
- Test conditions and important limitations are present.

## Narrative

- A reader can identify the subject, question, answer, and next action in under 30 seconds.
- The page contains one main conclusion, not several competing messages.
- Headings describe content rather than generic categories where possible.

## Visual

- Canvas is portrait A4; the compact dark-blue header occupies about 9–12% of page height, while the logo, palette, and components match the references.
- Title is no more than two lines and does not collide with the logo.
- Section and column edges align to a consistent grid.
- No text is clipped or wrapped unexpectedly. Every element meets the role-based minimum in `visual-style.md`; 12 pt is reserved for secondary text, not step numbers, headings, or metrics.
- At whole-page A4 view, step numbers, navigation markers, headings, and key metrics are immediately recognizable without zooming. Passing the absolute font-size minimum alone is not sufficient.
- No unintended overlaps exist. Connectors do not cross labels or nodes.
- Images are sharp, correctly cropped, and captioned.
- Tables remain readable at full-page view and do not dominate without purpose.
- The final conclusion panel is visually prominent.

## Mandatory overflow verification

1. Run the overflow or bounds checker provided by the active presentation workflow.
2. Render the final slide to PNG after all edits.
3. Open the rendered PNG at full size and inspect every text container, including titles, table cells, captions, formulas, footnotes, and conclusion panels.
4. Also inspect the complete A4 page fitted to the screen. Reject text that technically fits but cannot be read or distinguished by role without zooming.
5. Confirm that no glyph is clipped, no text crosses a border, no line escapes its box, and no content extends beyond the A4 canvas or sits flush against an edge without intentional padding.
6. Treat unexpected wrapping, a hidden last line, text touching a frame, unusually tight bottom padding, and weak hierarchy as failures even when an automated checker reports no error.
7. Fix failures by shortening text or changing layout/container dimensions. Preserve the role-based minimums; never solve density by shrinking important text to the 12 pt emergency floor.
8. Re-run diagnostics and re-render after every fix. Do not deliver the document until both checks pass.

## Output

- PPTX remains editable.
- PNG render matches the PPTX and has no missing fonts or assets.
- Automated bounds diagnostics and full-size visual inspection both pass on the final version.
- Source files were not overwritten.
