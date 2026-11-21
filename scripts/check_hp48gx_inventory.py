#!/usr/bin/env python3
"""Structurally compare the two HP-48GX Markdown ROM inventories.

This check is NOT a historical completeness certificate. It cannot prove that
every operation from HP's manuals, menus, built-in equations or cards is listed.

Run: python3 scripts/check_hp48gx_inventory.py
"""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "docs/de/HP-48GX-FUNKTIONSKATALOG.md"
MATRIX = ROOT / "docs/de/HP-48GX-BEFEHLSABGLEICH-MATRIX.md"
EXPECTED_ROM_NAMES = 517
EXPECTED_KEY_POSITIONS = 49
ROM_ID = re.compile(r"^\d+:\d+(?:, \d+:\d+)*$")


def markdown_section(text: str, start: str, end: str) -> str:
    first = text.find(start)
    if first < 0:
        raise ValueError(f"Missing section: {start}")
    last = text.find(end, first + len(start))
    if last < 0:
        raise ValueError(f"Missing closing section: {end}")
    return text[first:last]


def inventory(section: str, id_column: int) -> dict[str, str]:
    """Parse command-name/XLIB-ID table; exclude interactive UI-only rows."""
    items: dict[str, str] = {}
    for line in section.splitlines():
        if not line.startswith("| `"):
            continue
        cells = line.split(" | ")
        if len(cells) <= id_column or not cells[0].endswith("`"):
            continue
        name = cells[0][3:-1].replace(r"\|", "|")
        xlib = cells[id_column].strip("`")
        if not ROM_ID.fullmatch(xlib):
            continue
        if name in items:
            raise ValueError(f"Duplicate ROM name {name!r}")
        items[name] = xlib
    return items


def audit() -> int:
    if not CATALOG.is_file() or not MATRIX.is_file():
        print("ERROR: Required Markdown inventory missing.", file=sys.stderr)
        return 2

    catalog = CATALOG.read_text(encoding="utf-8")
    matrix = MATRIX.read_text(encoding="utf-8")
    cat = inventory(markdown_section(catalog, "## 3. Alphabetisches Register", "## 4."), 3)
    mat = inventory(markdown_section(matrix, "## D. Vollständige technische Zuordnung", "## E."), 1)
    keyboard = markdown_section(catalog, "### 2a.2", "### 2a.3")
    key_count = sum(bool(re.match(r"^\| [1-9] /", l)) for l in keyboard.splitlines())

    errors: list[str] = []
    if len(cat) != EXPECTED_ROM_NAMES:
        errors.append(f"Main catalog has {len(cat)} instead of {EXPECTED_ROM_NAMES} ROM names")
    if len(mat) != EXPECTED_ROM_NAMES:
        errors.append(f"Evidence matrix has {len(mat)} instead of {EXPECTED_ROM_NAMES} ROM names")
    if key_count != EXPECTED_KEY_POSITIONS:
        errors.append(f"Keyboard has {key_count} instead of {EXPECTED_KEY_POSITIONS} key rows")
    for name in sorted(set(cat) - set(mat)):
        errors.append(f"Missing from evidence matrix: {name}")
    for name in sorted(set(mat) - set(cat)):
        errors.append(f"Missing from main catalog: {name}")
    for name in sorted(set(cat) & set(mat)):
        if cat[name] != mat[name]:
            errors.append(f"XLIB mismatch {name}: {cat[name]} vs {mat[name]}")
    if "Vollständigkeit ausdrücklich noch nicht abgenommen" not in catalog:
        errors.append("Mandatory warning about unverified completeness is missing")
    if "UNVERIFIED" not in matrix:
        errors.append("Evidence matrix lacks verification status")

    print(f"HP 48GX: catalog={len(cat)}, evidence_matrix={len(mat)}, keyboard_rows={key_count}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        print("STRUCTURAL CHECK: FAIL; HISTORICAL COMPLETENESS: NOT CERTIFIED")
        return 1
    print("STRUCTURAL CHECK: PASS; HISTORICAL COMPLETENESS: NOT CERTIFIED")
    print("Outstanding: complete manual index, AUR, menus, equation, units and ROM revision audit.")
    return 0


if __name__ == "__main__":
    sys.exit(audit())
