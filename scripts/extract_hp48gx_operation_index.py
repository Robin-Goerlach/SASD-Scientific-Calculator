#!/usr/bin/env python3
"""Unverified name/label OCR of the HP 48G Series User's Guide, Appendix G.

Original scans remain temporary and are never published. Only name-level
OCR candidates, source pages and confidence metadata are retained.
"""
from __future__ import annotations
import argparse
import csv
from difflib import get_close_matches
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import fitz

SHA256 = "77b25f276277e90fbbd7ca1676d7440f69a844169fec6951382255df26e0782a"
DPI = 235

def run_ocr(page):
    png = page.get_pixmap(matrix=fitz.Matrix(DPI/72, DPI/72), alpha=False).tobytes("png")
    proc = subprocess.run(["tesseract", "stdin", "stdout", "--psm", "3", "tsv"], input=png,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, timeout=90)
    result = proc.stdout.decode("utf-8", errors="replace")
    words = []
    for w in csv.DictReader(io.StringIO(result), delimiter="\t"):
        if not (w.get("text") or "").strip():
            continue
        try:
            words.append(dict(word=w["text"].strip(), x=int(w["left"]), y=int(w["top"]),
                              conf=float(w.get("conf") or 0),
                              line=(int(w["block_num"]), int(w["par_num"]), int(w["line_num"]))))
        except (KeyError, ValueError):
            continue
    return words

def page_candidates(words, g, max_y, valid):
    groups = {}
    for w in words:
        groups.setdefault(w["line"], []).append(w)
    rows = []
    for group in groups.values():
        group.sort(key=lambda x: x["x"])
        h = group[0]
        if not 145 <= h["x"] <= 345 or not 220 <= h["y"] < max_y - 150:
            continue
        name = h["word"].strip("|¦")
        if not name or name.casefold() in {"name", "name,", "or", "label", "c", "f", "a", "o", "0", "1", "2", "3"}:
            continue
        adjacent = any(w["x"] >= 350 for w in group)
        if not adjacent and len(name) < 3:
            continue
        rows.append(dict(g_page=g, pdf_page=480+g, name_ocr=name,
                         y=h["y"], confidence=round(h["conf"], 1),
                         adjacent_description=adjacent,
                         exact_rom_match=name in valid,
                         rom_match_suggestions=[] if name in valid else get_close_matches(name.upper(), valid, n=2, cutoff=.76),
                         status="OCR_UNVERIFIED"))
    return sorted(rows, key=lambda r: r["y"])

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--baseline",required=True)
    ap.add_argument("--output",required=True)
    ap.add_argument("--report",required=True)
    a=ap.parse_args()
    raw=Path(a.pdf).read_bytes()
    checksum=hashlib.sha256(raw).hexdigest()
    if checksum!=SHA256: raise SystemExit("Source digest mismatch: "+checksum)
    valid={x["name"] for x in json.loads(Path(a.baseline).read_text())['entries']}
    pdf=fitz.open(stream=raw,filetype='pdf')
    if len(pdf)!=612: raise SystemExit("Wrong source page count")
    pages=[]
    all_rows=[]
    for g in range(2,59):
        p=pdf[479+g]  # G-1 is 1-based PDF page 481
        rows=page_candidates(run_ocr(p),g,round(p.rect.height*DPI/72),valid)
        pages.append(dict(g=g,pdf_page=480+g,candidates=len(rows)))
        all_rows.extend(rows)
        print('G-%02d candidates %d' % (g,len(rows)),flush=True)
    too_short=[x for x in pages if x['candidates']<3]
    if too_short: raise SystemExit('OCR coverage problem: '+str(too_short))
    found={x['name_ocr'] for x in all_rows if x['exact_rom_match']}
    unfamiliar=[x for x in all_rows if not x['exact_rom_match']]
    result=dict(schema=1,source='https://www.hp.com/ctg/Manual/c00442262.pdf',
                source_sha256=checksum,model='HP 48GX / 48G series',
                edition='HP 48G Series User\x27s Guide, December 1994, edition 8',
                page_range='G-2–G-58 / PDF 482–538',
                note='Unverified OCR candidate names, not a human-checked full operation index',
                candidates=len(all_rows),unique_exact_rom_names=len(found),
                unmatched_ocr_candidates=len(unfamiliar),page_summary=pages,rows=all_rows)
    Path(a.output).parent.mkdir(parents=True,exist_ok=True)
    Path(a.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=['# HP 48GX: Rohabgleich des Operation Index', '',
           '**STATUS: AUTOMATISCHE TEXTERKENNUNG – KEINE HISTORISCHE VOLLSTÄNDIGKEITSFREIGABE.**', '',
           'Quelle: HP 48G Series User\x27s Guide (Dezember 1994, Edition 8), Appendix G.',
           'SHA256: '+checksum,'',
           '- Alle 57 Index-Tabellenseiten G-2 bis G-58 maschinell verarbeitet.',
           '- OCR-Kandidaten: '+str(len(all_rows)),
           '- Als ROM-Namen exakt erkannte unterschiedliche Namen: '+str(len(found)),
           '- Nicht exakt zugeordneten OCR-Kandidaten: '+str(len(unfamiliar)), '',
           '| Druckseite | PDF-Seite | Unverifizierte Namenskandidaten |',
           '| --- | ---: | ---: |']
    lines.extend('| G-'+str(x['g'])+' | '+str(x['pdf_page'])+' | '+str(x['candidates'])+' |' for x in pages)
    lines.extend(['','## Noch nicht abgeglichene OCR-Tokens', ''])
    for g in range(2,59):
        vals=[x['name_ocr'] for x in unfamiliar if x['g_page']==g]
        if vals:lines.append('G-'+str(g)+': '+', '.join(vals))
    lines.extend(['','Jeder Kandidat benötigt eine Sichtprüfung der gescannten Originalzeile,',
                  'insbesondere bei Sonderzeichen, Shift-Ebenen und Bedienaktionen (Typ O).',
                  'Keine Prozentquote darf als historische Funktionsabdeckung ausgegeben werden.'])
    Path(a.report).parent.mkdir(parents=True,exist_ok=True)
    Path(a.report).write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('SUMMARY candidates=%d exact=%d unmatched=%d' % (len(all_rows),len(found),len(unfamiliar)))

if __name__=='__main__':main()
