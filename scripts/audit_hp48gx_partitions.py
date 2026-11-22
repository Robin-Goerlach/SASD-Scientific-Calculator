#!/usr/bin/env python3
"""Validate resumable HP-48GX historical-audit checkpoints.

This checks source-index / partition integrity and the evidence required for
any claimed scan review. A PASS NEVER certifies historical functional coverage.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "docs/reference/hp48gx-operation-index-crosschecked-pages.json"
AUR = ROOT / "docs/reference/hp48gx-aur-command-index.json"
MANIFEST = ROOT / "docs/reference/hp48gx-audit-partitions.json"
ROM = ROOT / "docs/reference/hp48gx-rom-index-baseline.json"


def load(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def check() -> int:
    source, aur, rom, manifest = (load(x) for x in (SOURCE, AUR, ROM, MANIFEST))
    errors: list[str] = []
    pages = manifest["operation_index"]["pages"]
    groups = manifest["operation_index"]["groups"]
    all_items = source["items"]
    actual_pages = [p["g_page"] for p in pages]
    if actual_pages != list(range(2, 59)):
        errors.append("Exactly G-2 through G-58 must occur, in order, once")
    if len(all_items) != source["source_rows"] or len(all_items) != 696:
        errors.append("Operation Index row total differs from 696")
    if len(aur["rows"]) != 517 or len(rom["entries"]) != 517:
        errors.append("Pinned AUR TOC / ROM baseline missing names")
    known_aur = {r["printed_name"] for r in aur["rows"]}
    known_rom = {r["name"] for r in rom["entries"]}

    for p in pages:
        n = p["g_page"]
        items = [r for r in all_items if r["g_page"] == n]
        hits = sum(bool(r["exact_ocr_detected"]) for r in items)
        if p["source_rows"] != len(items) or p["ocr_token_hits"] != hits:
            errors.append(f"G-{n}: per-page source/OCR count incorrect")
        if p["ocr_without_exact_token"] != len(items) - hits:
            errors.append(f"G-{n}: missing OCR count incorrect")
        if p["original_scan_visually_checked"]:
            evidence = p.get("original_scan_evidence", {})
            if not all(evidence.get(k) for k in ("pdf_sha256", "page", "reviewed_by", "reviewed_on", "row_checklist")):
                errors.append(f"G-{n}: visual approval lacks source evidence")
        if p["stack_semantics_checked"] and not p.get("aur_stack_test_evidence"):
            errors.append(f"G-{n}: semantic approval lacks AUR/test evidence")

    seen_pages: list[int] = []
    reviewed_pages: list[int] = []
    for group in groups:
        start, end = group["range"]
        these = [p for p in pages if start <= p["g_page"] <= end]
        seen_pages.extend(p["g_page"] for p in these)
        if group["rows"] != sum(p["source_rows"] for p in these):
            errors.append(f'{group["id"]}: row total differs')
        if group["exact_ocr_token_hits"] != sum(p["ocr_token_hits"] for p in these):
            errors.append(f'{group["id"]}: token hit total differs')
        if group["cross_index_status"] == "CHECKED_AGAINST_AUR_ROM_NO_SCAN":
            reviewed_pages.extend(p["g_page"] for p in these)
            if not all(p["cross_index_checked"] for p in these):
                errors.append(f'{group["id"]}: group marked compared but some pages not marked')
            report_path = group.get("report")
            if not report_path:
                errors.append(f'{group["id"]}: compared group has no persisted report')
            else:
                target = ROOT / report_path
                if not target.is_file():
                    errors.append(f'{group["id"]}: missing report {report_path}')
                else:
                    lines = target.read_text(encoding="utf-8").splitlines()
                    actual = sum(bool(re.match(r"^\| G-\d+:(?:\d+)", line)) for line in lines)
                    if actual != group["rows"]:
                        errors.append(f'{group["id"]}: report has {actual} vs {group["rows"]} operation rows')
        elif group["cross_index_status"] == "PENDING":
            if any(p["cross_index_checked"] for p in these):
                errors.append(f'{group["id"]}: page already compared but group still pending')
        else:
            errors.append(f'{group["id"]}: unsupported cross_index_status')
        if group["scan_visual_status"] != "PENDING":
            if not all(p["original_scan_visually_checked"] for p in these):
                errors.append(f'{group["id"]}: unsupported scan approval without page evidence')

    if seen_pages != list(range(2, 59)):
        errors.append("Grouped pages have gaps, overlaps, or changed order")
    if len(reviewed_pages) != manifest["operation_index"]["source_text_cross_index_checked_pages"]:
        errors.append("Aggregate cross-index progress does not match page status")
    if manifest["operation_index"]["scan_visually_certified_pages"] != sum(
        bool(p["original_scan_visually_checked"]) for p in pages
    ):
        errors.append("Claimed scan-approved page count not supported")
    toc = manifest["advanced_reference"]["toc_groups"]
    details = manifest["advanced_reference"]["individual_command_groups"]
    if sum(x["rows"] for x in toc) != len(aur["rows"]):
        errors.append("AUR contents index partitions have coverage gaps")
    if sum(x["count"] for x in details) != len(aur["rows"]):
        errors.append("AUR detailed-command partitions have gaps")
    pocket_checked = 0
    for part in details:
        mode = part.get("independent_pocket_guide_name_check")
        if mode is None:
            continue
        if mode != "TEXT_INDEX_COMPARED_NOT_SCAN":
            errors.append(f'{part["id"]}: unsupported Pocket Guide status {mode}')
            continue
        expected = part["count"]
        report = part.get("independent_pocket_guide_report")
        if not report or not (ROOT / report).is_file():
            errors.append(f'{part["id"]}: missing Pocket Guide checkpoint report')
            continue
        report_lines = (ROOT / report).read_text(encoding="utf-8").splitlines()
        numbered = []
        for line in report_lines:
            cells = line.split(" | ")
            if line.startswith("| ") and cells[0][2:].isdigit():
                numbered.append((int(cells[0][2:]), cells))
        first, last = part["ordinal_range"]
        if [n for n, _ in numbered] != list(range(first, last + 1)):
            errors.append(f'{part["id"]}: AUR command names have missing/duplicate ordinals')
        expected_names = [r["printed_name"] for r in aur["rows"][first-1:last]]
        actual_names = [cells[1].strip("`").replace(r"\\|","|") for _, cells in numbered]
        if actual_names != expected_names:
            errors.append(f'{part["id"]}: Pocket Guide report not aligned with AUR source names')
        if part.get("pocket_guide_names_crosschecked") != expected:
            errors.append(f'{part["id"]}: wrong checkpoint name count')
        pocket_checked += len(numbered)
    if pocket_checked != manifest["advanced_reference"].get("pocket_guide_names_crosschecked", 0):
        errors.append("Global independent Pocket Guide crosscheck count not supported")

    ordinals = [n for x in details for n in range(x["ordinal_range"][0], x["ordinal_range"][1]+1)]
    if ordinals != list(range(1, len(aur["rows"])+1)):
        errors.append("AUR detailed-command ordinal ranges overlap or leave gaps")
    if manifest["operation_index"].get("preface_page_g1", {}).get("status") != "PENDING_VISUAL_CHECK":
        errors.append("G-1 legend/preface original scan must remain visibly pending")
    if manifest["release_gate"] != "HISTORICAL_COMPLETENESS_NOT_CERTIFIED":
        errors.append("Gate must remain NOT CERTIFIED until separately signed off")
    if not known_rom or not known_aur:
        errors.append("Missing primary comparison baselines")

    print(f"G pages indexed={len(pages)}; cross-index compared={len(reviewed_pages)}; "
          f"original scans signed off={manifest['operation_index']['scan_visually_certified_pages']}")
    print(f"Operation rows={len(all_items)}; AUR TOC rows={len(aur['rows'])}; ROM names={len(rom['entries'])}; independent Pocket Guide text names={pocket_checked}")
    if errors:
        for error in errors:
            print("FAIL:", error, file=sys.stderr)
        print("CHECKPOINT INTEGRITY: FAIL / HISTORICAL COMPLETENESS: NOT CERTIFIED")
        return 1
    print("CHECKPOINT INTEGRITY: PASS / HISTORICAL COMPLETENESS: NOT CERTIFIED")
    return 0


if __name__ == "__main__":
    raise SystemExit(check())
