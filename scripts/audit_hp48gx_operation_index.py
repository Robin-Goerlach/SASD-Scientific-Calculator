#!/usr/bin/env python3
"""Check integrity of the source-indexed historical HP 48GX Operation Index.

This is NOT a certificate that the original manual was visually reviewed,
or that all AUR command semantics or built-in equation data are complete.
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"docs/reference/hp48gx-operation-index-crosschecked-pages.json"
BASE=ROOT/"docs/reference/hp48gx-rom-index-baseline.json"
MD=ROOT/"docs/de/HP-48GX-OPERATION-INDEX-VOLLKATALOG.md"

def audit():
    src=json.loads(SRC.read_text(encoding="utf-8"))
    base=json.loads(BASE.read_text(encoding="utf-8"))
    manual=MD.read_text(encoding="utf-8")
    errors=[]
    pages=src["page_scope"];items=src["items"]
    if pages!=list(range(2,59)): errors.append("Operation Index G-2..G-58 not contiguous")
    if len(items)!=src["source_rows"]: errors.append("Invalid source_rows count")
    if len(items)!=696: errors.append("Count changed from reviewed 696 source-text rows")
    if len(base["entries"])!=517: errors.append("Pinned ROM name count changed")
    if len(src["page_counts"])!=57: errors.append("Page summary must have 57 pages")
    names_by_page={}
    for row in items:
        g=row["g_page"]
        names_by_page.setdefault(g,[]).append(row)
        if row["pdf_page"] != g+480: errors.append(f"Bad PDF page for G-{g}")
        if not row["label"].strip():errors.append(f"Missing source label for G-{g}")
        if row["hp_class"] not in ("O","C","F","A","C/F","C/O","C/O/O"):
            errors.append(f"Unrecognized HP category on G-{g}: {row['hp_class']}")
        if row["source_status"] not in ("SOURCE_TEXT_CHECKED_NOT_SCAN_SIGNED_OFF","SOURCE_TEXT_NORMALIZED_FROM_TAHN_ERROR_UNVERIFIED_SCAN"):
            errors.append(f"Unknown verification marker on G-{g}")
        if not isinstance(row["exact_ocr_detected"],bool):errors.append("Invalid OCR flag")
    for g in range(2,59):
        found=names_by_page.get(g,[])
        summary=next((p for p in src["page_counts"] if p["g_page"]==g),None)
        if summary is None:errors.append(f"No summary G-{g}");continue
        if len(found)!=summary["source_rows"]: errors.append(f"Count inconsistent at G-{g}")
        if [x["index_row"] for x in found]!=list(range(1,len(found)+1)):errors.append(f"Missing/duplicate row sequence at G-{g}")
        if summary["exact_rows_detected"]!=sum(x["exact_ocr_detected"] for x in found):errors.append(f"Wrong independent OCR tally G-{g}")
        if g==57 and any(x["exact_ocr_detected"] for x in found):
            errors.append("G-57 is transcription fallback and must not have independent OCR positives")
    md_rows=[x for x in manual.splitlines() if x.startswith("| G-")]
    if len(md_rows)!=len(items): errors.append(f"Markdown rows = {len(md_rows)} vs index = {len(items)}")
    if "nicht visuell auf jeder Scan-Seite abgenommen" not in manual:
        errors.append("Missing explicit original-scan verification warning")
    print(f"HP 48GX Operation Index source: {len(pages)}/57 table pages, {len(items)} rows, {len(md_rows)} Markdown rows")
    if errors:
        for e in errors: print("FAIL:",e)
        print("INTEGRITY FAIL; HISTORICAL COMPLETENESS NOT CERTIFIED")
        return 1
    print("INTEGRITY PASS; HISTORICAL COMPLETENESS NOT CERTIFIED")
    return 0

if __name__=="__main__":
    raise SystemExit(audit())
