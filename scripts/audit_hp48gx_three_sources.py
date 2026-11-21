#!/usr/bin/env python3
"""Verify reproducible three-source HP 48GX reference inventory consistency.

Never certifies the historical device's full behavior or every manual page.
"""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "docs" / "reference"


def load(name: str):
    with (ROOT / name).open(encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    rom = load("hp48gx-rom-index-baseline.json")
    aur = load("hp48gx-aur-command-index.json")
    guide = load("hp48gx-operation-index-crosschecked-pages.json")
    diffs = load("hp48gx-historical-index-differences.json")
    errors = []

    rom_names = {r["name"] for r in rom["entries"]}
    if len(rom["entries"]) != 517 or len(rom_names) != 517:
        errors.append("ROM baseline must have 517 distinct names")
    if len(aur["rows"]) != 517:
        errors.append("AUR Contents-3..16 must have 517 indexed rows")
    if len({r["printed_name"] for r in aur["rows"]}) != 516:
        errors.append("AUR distinct printed names changed")
    if len(guide["items"]) != 696 or guide["page_scope"] != list(range(2, 59)):
        errors.append("Guide must cover all 57 G-2..G-58 pages with 696 rows")

    aur_in_rom = {r["rom_normalized_candidate"] for r in aur["rows"] if r["rom_normalized_candidate"] in rom_names}
    aur_extra = {r["printed_name"] for r in aur["rows"] if r["rom_normalized_candidate"] not in rom_names}
    rom_only = rom_names - {r["rom_normalized_candidate"] for r in aur["rows"]}
    guide_prog = {r["label"] for r in guide["items"] if r["hp_class"] != "O" and r["label"] not in rom_names}
    guide_ui = {r["label"] for r in guide["items"] if r["hp_class"] == "O" and r["label"] not in rom_names}

    checks = {
        "aur matched unique ROM": (len(aur_in_rom), 507),
        "AUR names not in ROM": (len(aur_extra), 8),
        "ROM names not in AUR": (len(rom_only), 10),
        "Guide raw programmable names not in ROM": (len(guide_prog), 26),
        "Guide pure UI names not in ROM": (len(guide_ui), 143),
        "Guide pure UI rows": (sum(r["hp_class"] == "O" for r in guide["items"]), 179),
    }
    for what, (actual, expected) in checks.items():
        print(f"{what}: {actual}")
        if actual != expected:
            errors.append(f"{what} expected {expected}, got {actual}")
    if aur_extra != {x["name"] for x in diffs["aur_extra"]}:
        errors.append("AUR external-name exception register is inconsistent")
    if rom_only != {x["name"] for x in diffs["rom_no_aur"]}:
        errors.append("ROM-only name register is inconsistent")
    if guide_prog != {x["label"] for x in diffs["ug_program_label_differences"]}:
        errors.append("Guide aliases/reserved-names exception register inconsistent")
    if guide_ui != set(diffs["ug_ui_labels_not_in_rom"]):
        errors.append("Guide UI-only label set incomplete")
    for key, val in diffs["counts"].items():
        # Exact source counters, sourced values only
        expected = {
            "rom_names": len(rom_names),
            "aur_rows": len(aur["rows"]),
            "aur_unique_names": len({r["printed_name"] for r in aur["rows"]}),
            "aur_rom_mapped_unique": len(aur_in_rom),
            "aur_source_names_not_in_rom": len(aur_extra),
            "rom_names_not_in_aur_toc": len(rom_only),
            "ug_source_rows": len(guide["items"]),
            "ug_distinct_printed_labels": len({r["label"] for r in guide["items"]}),
            "ug_pure_ui_rows": sum(r["hp_class"] == "O" for r in guide["items"]),
            "ug_program_and_mixed_rows": sum(r["hp_class"] != "O" for r in guide["items"]),
            "ug_program_raw_label_not_in_rom": len(guide_prog),
            "ug_ui_raw_label_not_in_rom": len(guide_ui),
        }[key]
        if val != expected:
            errors.append(f"Report summary inconsistent for {key}: {val} != {expected}")
    if not all(x["verification"] != "CERTIFIED" for x in diffs["aur_extra"]):
        errors.append("Historical semantics were incorrectly declared certified")
    if errors:
        for e in errors:
            print("ERROR", e)
        print("THREE-SOURCE INTEGRITY: FAIL | HISTORICAL FUNCTIONAL COMPLETENESS: NOT CERTIFIED")
        return 1
    print("THREE-SOURCE INTEGRITY: PASS | HISTORICAL FUNCTIONAL COMPLETENESS: NOT CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
