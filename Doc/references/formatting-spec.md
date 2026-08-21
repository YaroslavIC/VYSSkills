# KZCOT DOCX formatting specification

## Page and body

- File format: DOCX.
- Page: A4, portrait.
- Margins: 2 cm on every side.
- Typeface: Times New Roman only; remove theme-font attributes.
- Body: 12 pt, black, justified, single spacing, 0 pt before/after.
- First-line indent: 1.25 cm.
- Enable automatic hyphenation and widow/orphan control.

## Branding and page numbering

- First page: embed `assets/first_page.jpg`, width 3 cm, preserve aspect ratio.
- Later pages: embed `assets/next-pages.png`, width 1.5 cm, preserve aspect ratio.
- Place both logos in the upper-left header area exactly 2 cm from the physical left edge. Set header paragraph left and first-line indents explicitly to 0.
- Show the page number on the first page.
- Place odd-page numbers at the bottom right and even-page numbers at the bottom left (outer edge).
- Do not add textual headers.

## Numbered headings

- Use real multilevel numbering linked to Heading 1–3: `1`, `1.1`, `1.1.1`.
- Do not type heading numbers manually.
- Set every heading explicitly to black (`#000000`); do not inherit blue or accent colors from Word themes.
- Heading 1: Times New Roman 16 pt, black, bold, centered; 12 pt before, 6 pt after.
- Heading 2: Times New Roman 14 pt, black, bold, centered; 6 pt before and after.
- Heading 3: Times New Roman 12 pt, black, bold, centered; 6 pt before and after.
- When a separate document title is used, set it explicitly to Times New Roman 16 pt, black, bold, and centered unless the user provides another approved title treatment.
- Use no first-line indent. Keep every heading with the following paragraph. Do not force Heading 1 onto a new page.
- Do not place a period after a heading number or at the end of a heading.
- Disable hyphenation inside headings.

## Figures and charts

- Center figures in the text flow and keep each figure with its caption.
- Put the caption below: `Рисунок 1 — Описание рисунка`.
- Center figure captions; use Times New Roman 12 pt, black, and no paragraph indent. Never inherit the blue color of Word's built-in Caption style.
- Use automatic continuous numbering throughout the document.
- Put chart and figure legends above the graphic, centered, horizontally in one row. Use Times New Roman 10 pt.

## Tables

- Put the title before the table, aligned right: `Таблица 1 — Название`.
- Format the table title as Times New Roman 12 pt, black, without a paragraph indent. Never center it and never inherit the blue color of Word's built-in Caption style.
- Use automatic continuous numbering.
- Use Times New Roman 12 pt by default; use 10 pt only when necessary for dense content.
- Set first-line and left paragraph indents inside every cell explicitly to 0.
- Center header-row text horizontally and vertically.
- In the first content column, align text left horizontally and center vertically.
- In all columns to the right, center text horizontally and vertically.
- Repeat the header row on continued pages and prohibit splitting a row across pages.
- Keep the title with the first table rows.

## Equations and footnotes

- Create editable Office Math equations, not images or plain-text imitations.
- Center equations and place the continuous number `(1)` at the right margin.
- Force Times New Roman on equation runs and remove theme-font attributes.
- Use true Word footnotes at the bottom of the corresponding page.
- Number footnotes continuously with Arabic numerals.
- Format footnote text as Times New Roman 10 pt, single spaced, without a first-line indent.

## Bibliography

- Place `Список литературы` at the end.
- Order sources by first mention and number them continuously.
- Use textual references `[1]` and `[1, с. 25]`.
- Format descriptions under ГОСТ Р 7.0.100–2018, references under ГОСТ Р 7.0.5–2008, and online documents with ГОСТ Р 7.0.108–2022.
- Use Times New Roman 12 pt, single spacing, and a 1.25 cm hanging indent.

## Forbidden defaults and audit conditions

- No automatic landscape sections.
- No TOC, list of figures, list of tables, or textual running headers by default.
- No external relationships to logos or local source files.
- No `<w:updateFields>` in settings.
- No `asciiTheme`, `hAnsiTheme`, `eastAsiaTheme`, or `cstheme` on used text.
- No visible font other than Times New Roman.
- No theme/accent color on headings or captions. Heading 1–3 and Caption text must be explicitly black.
- No centered table title and no left/right-aligned figure caption.
