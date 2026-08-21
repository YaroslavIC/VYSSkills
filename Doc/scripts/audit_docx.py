#!/usr/bin/env python3
"""Audit high-risk KZCOT DOCX package rules."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZipFile

from lxml import etree


W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
PKG_REL = "http://schemas.openxmlformats.org/package/2006/relationships"
NS = {"w": W}


def q(name: str) -> str:
    return f"{{{W}}}{name}"


def audit(path: Path) -> list[str]:
    errors: list[str] = []
    with ZipFile(path) as z:
        names = set(z.namelist())
        required = {"word/document.xml", "word/styles.xml", "word/settings.xml"}
        missing = sorted(required - names)
        if missing:
            return [f"Missing required part: {name}" for name in missing]

        for name in names:
            if not name.endswith(".rels"):
                continue
            root = etree.fromstring(z.read(name))
            for rel in root.findall(f"{{{PKG_REL}}}Relationship"):
                if rel.get("TargetMode") == "External":
                    errors.append(f"External relationship in {name}: {rel.get('Target')}")

        settings = etree.fromstring(z.read("word/settings.xml"))
        if settings.xpath(".//w:updateFields", namespaces=NS):
            errors.append("word/settings.xml contains w:updateFields")

        explicit_fonts: set[str] = set()
        for name in names:
            if not (name.startswith("word/") and name.endswith(".xml")):
                continue
            root = etree.fromstring(z.read(name))
            for fonts in root.xpath(".//w:rFonts", namespaces=NS):
                for attr in ("asciiTheme", "hAnsiTheme", "eastAsiaTheme", "cstheme"):
                    value = fonts.get(q(attr))
                    if value:
                        errors.append(f"Theme font {attr}={value} in {name}")
                for attr in ("ascii", "hAnsi", "eastAsia", "cs"):
                    value = fonts.get(q(attr))
                    if value and not value.startswith("+"):
                        explicit_fonts.add(value)
        disallowed = sorted(font for font in explicit_fonts if font != "Times New Roman")
        if disallowed:
            errors.append("Non-Times fonts: " + ", ".join(disallowed))

        styles = etree.fromstring(z.read("word/styles.xml"))
        expected_styles = {
            "Heading1": ("32", True),
            "Heading2": ("28", True),
            "Heading3": ("24", True),
            "Caption": ("24", False),
        }
        for style_id, (expected_size, require_bold) in expected_styles.items():
            matches = styles.xpath(
                f".//w:style[@w:styleId='{style_id}']", namespaces=NS
            )
            if not matches:
                errors.append(f"Missing required style {style_id}")
                continue
            rpr = matches[0].find(q("rPr"))
            if rpr is None:
                errors.append(f"Style {style_id} has no explicit run properties")
                continue
            color = rpr.find(q("color"))
            color_value = color.get(q("val"), "").upper() if color is not None else ""
            if color_value not in {"000000", "00000000"}:
                errors.append(
                    f"Style {style_id} color is {color_value or 'inherited'}, expected black"
                )
            size = rpr.find(q("sz"))
            size_value = size.get(q("val")) if size is not None else None
            if size_value != expected_size:
                errors.append(
                    f"Style {style_id} size is {size_value or 'inherited'}, "
                    f"expected {expected_size} half-points"
                )
            if require_bold and rpr.find(q("b")) is None:
                errors.append(f"Style {style_id} is not explicitly bold")

        document = etree.fromstring(z.read("word/document.xml"))
        section = document.xpath(".//w:sectPr", namespaces=NS)[-1]
        page_size = section.find(q("pgSz"))
        page_margin = section.find(q("pgMar"))
        if page_size is None or (page_size.get(q("w")), page_size.get(q("h"))) != ("11906", "16838"):
            errors.append("Page size is not A4 portrait")
        if page_margin is None:
            errors.append("Page margins are missing")
        else:
            for side in ("top", "right", "bottom", "left"):
                value = page_margin.get(q(side))
                if value not in {"1134", "1135"}:
                    errors.append(f"{side} margin is {value}, expected about 1134 twips (2 cm)")

        for index, paragraph in enumerate(document.xpath(".//w:tbl//w:p[.//w:t]", namespaces=NS), 1):
            ind = paragraph.find("./w:pPr/w:ind", namespaces=NS)
            first = ind.get(q("firstLine")) if ind is not None else None
            left = ind.get(q("left")) if ind is not None else None
            if first not in {"0", None} or left not in {"0", None}:
                errors.append(f"Table paragraph {index} has nonzero indent")

        for index, paragraph in enumerate(
            document.xpath(".//w:body/w:p[.//w:t]", namespaces=NS), 1
        ):
            text = "".join(paragraph.xpath(".//w:t/text()", namespaces=NS)).strip()
            if not (text.startswith("Таблица ") or text.startswith("Рисунок ")):
                continue
            ppr = paragraph.find(q("pPr"))
            jc = ppr.find(q("jc")) if ppr is not None else None
            alignment = jc.get(q("val")) if jc is not None else "inherited"
            expected = {"right", "end"} if text.startswith("Таблица ") else {"center"}
            if alignment not in expected:
                kind = "Table title" if text.startswith("Таблица ") else "Figure caption"
                errors.append(
                    f"{kind} paragraph {index} alignment is {alignment}, "
                    f"expected {sorted(expected)}"
                )
            for rpr in paragraph.xpath(".//w:rPr", namespaces=NS):
                color = rpr.find(q("color"))
                value = color.get(q("val"), "").upper() if color is not None else ""
                if value and value not in {"000000", "00000000"}:
                    errors.append(
                        f"Caption paragraph {index} contains non-black color {value}"
                    )

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("docx", type=Path)
    args = parser.parse_args()
    errors = audit(args.docx)
    if errors:
        print("KZCOT DOCX audit: FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print("KZCOT DOCX audit: PASSED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
