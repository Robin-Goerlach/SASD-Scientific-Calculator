#!/usr/bin/env python3
"""Read-only probe of the original HP 48G/GX User's Guide PDF layout.

No full manual text or scanned pages are copied into the repository.
Intended for reproducible Operation Index (Appendix G) extraction research.
"""
from __future__ import annotations

import re
import sys
import fitz


def main(path: str) -> None:
    doc = fitz.open(path)
    print("pages", len(doc))
    matched = []
    for i, page in enumerate(doc):
        text = page.get_text("text")
        labels = re.findall(r"(?:Operation Index\s+G\s*[-–]\s*(\d{1,2})|G\s*[-–]\s*(\d{1,2})\s+Operation Index)", text, re.I)
        if labels:
            nums = sorted({int(a or b) for a, b in labels if 1 <= int(a or b) <= 58})
            if nums:
                matched.append((i, nums))
    print("indexed operation pages:", len(matched))
    for i, nums in matched:
        print("page", i + 1, "index-labels", nums)
    focus = next((i for i, nums in matched if 2 in nums), None)
    if focus is None:
        print("ERROR: no G-2 page found")
        sys.exit(2)
    page = doc[focus]
    print("G-2 dimensions", page.rect)
    for x0, y0, x1, y1, text, num, kind in page.get_text("blocks")[:22]:
        print(f"BLOCK x={x0:.1f} y={y0:.1f} width={x1-x0:.1f}: {text[:105]!r}")
    print("G-2 first 100 positioned words:")
    words = sorted(page.get_text("words"), key=lambda w: (round(w[1]/4), w[0]))
    for word in words[:100]:
        print(f"xy=({word[0]:.1f},{word[1]:.1f}) text={word[4]!r}")


if __name__ == "__main__":
    main(sys.argv[1])
