#!/usr/bin/env python3
"""Report basic page/layout signals of a candidate 1994 HP 48G Series AUR PDF."""
from __future__ import annotations
import argparse
import hashlib
import fitz
from pathlib import Path

p=argparse.ArgumentParser();p.add_argument("pdf");args=p.parse_args()
raw=Path(args.pdf).read_bytes();doc=fitz.open(stream=raw,filetype="pdf")
print("PDF SHA-256",hashlib.sha256(raw).hexdigest())
print("PAGES",len(doc),"BYTES",len(raw))
print("METADATA",doc.metadata)
for i in [0,1,2,5,7,10,13,16,19,22,25,28,31,34,38,45,50,100]:
 if i>=len(doc):continue
 page=doc[i]
 text=page.get_text("text")
 print("PAGE",i+1,"chars",len(text),"blocks",len(page.get_text("blocks")),"START",repr(text[:200].replace("\n"," | ")))
print("TOC",doc.get_toc()[:25])

import subprocess

print("OCR CHECK – front matter / contents")
for index in range(1,min(26,len(doc))):
    if index not in [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]:
        continue
    page=doc[index]
    png=page.get_pixmap(matrix=fitz.Matrix(160/72,160/72),alpha=False).tobytes("png")
    cp=subprocess.run(["tesseract","stdin","stdout","--psm","6"],input=png,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=60,check=True)
    txt=cp.stdout.decode("utf-8","replace")
    lines=[s.strip() for s in txt.splitlines() if s.strip()]
    print("OCR_PAGE",index+1,"lines",len(lines),"TOP",repr(" | ".join(lines[:4])[:320]),"LAST",repr(" | ".join(lines[-3:])[:180]),flush=True)
