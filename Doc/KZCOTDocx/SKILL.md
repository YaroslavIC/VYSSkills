---
name: kzcot-docx
description: Create, reformat, and audit Russian Microsoft Word .docx documents using the approved KZCOT corporate layout, branding, headings, tables, figures, equations, footnotes, page numbering, and bibliography rules. Use when the user invokes $kzcot-docx, asks for KZCOT or Kuzbass-COT Word formatting, requests a new corporate DOCX, or asks to bring an existing DOCX into the KZCOT standard.
---

# KZCOT DOCX

Use the `documents` skill for DOCX generation and render verification. Read [formatting-spec.md](references/formatting-spec.md) before creating or reformatting a document.

## Workflow

1. Preserve the user's content and meaningful structure when reformatting an existing document.
2. Use `assets/first_page.jpg` at 3 cm width on the first page and `assets/next-pages.png` at 1.5 cm width on all later pages.
3. Apply the complete specification through Word styles, real multilevel numbering, real fields, editable Office Math equations, and true footnotes.
4. Keep all pages A4 portrait with 2 cm margins. Use landscape orientation only when the user explicitly requests it.
5. Do not add a table of contents, lists of figures/tables, or textual running headers unless the user explicitly requests them.
6. Do not add `<w:updateFields>` to `word/settings.xml`. It causes Word to ask about updating linked data even when the document contains no external links.
7. Remove theme-font attributes from every used style and run. Set `ascii`, `hAnsi`, `eastAsia`, and `cs` explicitly to `Times New Roman`.
8. Set zero first-line and left paragraph indents explicitly inside every table cell, caption, header, footer, equation-layout cell, and bibliography entry override. Do not rely on inherited values.
9. Never rely on the visual defaults of Word's built-in `Heading` or `Caption` styles. Explicitly set heading and caption font family, size, black color, bold state, paragraph alignment, and spacing in the generated DOCX. Table titles must be black and right-aligned; figure captions must be black and centered.
10. Run `scripts/audit_docx.py OUTPUT.docx` and resolve every reported error, including heading/caption color, size, and alignment failures.
11. Render the final DOCX to page images and inspect every page. Explicitly compare the rendered headings and captions against `references/formatting-spec.md`; reject blue/theme-colored text, incorrect sizes, centered table titles, or non-centered figure captions. Iterate until no clipping, overlap, unwanted font/color, broken table, detached heading, or misplaced header/footer remains.

## Output rules

- Produce a new `.docx`; do not overwrite a user's source file unless explicitly requested.
- Keep logos embedded in the DOCX package, never linked to local files or URLs.
- Preserve editable Word structures instead of flattening tables, equations, fields, or footnotes into images.
- Confirm the page count and verify headings directly in Word when Word is available.
