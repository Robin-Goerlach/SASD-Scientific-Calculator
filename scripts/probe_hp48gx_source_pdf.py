#!/usr/bin/env python3
"""Probe original 1994 HP 48G Series User's Guide without publishing PDF contents."""
from __future__ import annotations
import re
import subprocess
import sys
import fitz

def ocr(page, dpi=135):
    png=page.get_pixmap(matrix=fitz.Matrix(dpi/72,dpi/72),alpha=False).tobytes("png")
    return subprocess.run(["tesseract","stdin","stdout","--psm","6"],input=png,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=45,check=True).stdout.decode("utf-8",errors="replace")

def main(path):
    doc=fitz.open(path)
    print("pages",len(doc),"toc",doc.get_toc()[:55])
    print("PDF-text characters total",sum(len(p.get_text("text")) for p in doc))
    for idx in range(410,min(612,len(doc)),12):
        t=ocr(doc[idx])
        lines=[x.strip() for x in t.splitlines() if x.strip()]
        g=re.findall(r"(?:Operation Index|G-\d+|H-\d+|Index)",t,re.I)
        print("SAMPLE",idx+1,"markers",g[:10],"head",repr(" ".join(lines[:4])[:170]),"tail",repr(" ".join(lines[-3:])[:170]))
    for idx in [510,526,542,558,574,590]:
        if idx >= len(doc):continue
        t=ocr(doc[idx],185)
        print("FOCUS",idx+1,repr(t[:500]),"FOOTER",repr(t[-180:]))

if __name__=="__main__":main(sys.argv[1])
