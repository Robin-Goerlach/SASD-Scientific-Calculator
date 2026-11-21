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
