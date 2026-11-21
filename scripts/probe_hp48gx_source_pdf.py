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


    idx=482
    p=doc[idx]
    png=p.get_pixmap(matrix=fitz.Matrix(220/72,220/72),alpha=False).tobytes("png")
    result=subprocess.run(["tesseract","stdin","stdout","--psm","3","tsv"],input=png,stdout=subprocess.PIPE,stderr=subprocess.PIPE,timeout=45,check=True).stdout.decode("utf-8",errors="replace")
    import csv, io
    lines={}
    for rec in csv.DictReader(io.StringIO(result),delimiter="\t"):
        token=rec.get("text","").strip()
        if not token:continue
        key=(rec["block_num"],rec["par_num"],rec["line_num"])
        lines.setdefault(key,[]).append((int(rec["left"]),int(rec["top"]),token))
    print("TSV-PAGE",idx+1,"rect",p.rect,"lines",len(lines))
    for group in sorted(lines.values(),key=lambda arr:min(t[1] for t in arr))[:75]:
        group=sorted(group)
        print("TSV",min(t[1] for t in group),min(t[0] for t in group),repr(" ".join(x[2] for x in group)[:160]))

if __name__=="__main__":main(sys.argv[1])
