#!/usr/bin/env python3
"""Check documented HP-41C command presence, not ROM/behavior compatibility.

Requires Python >= 3.9, standard library only. Run from any working directory:
    python3 tools/audit_hp41c_functions.py
    python3 tools/audit_hp41c_functions.py --json
"""
import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INVENTORY = ROOT / "docs/reference/hp41c-command-inventory.json"
CATALOG = ROOT / "docs/de/HP-41C-FUNKTIONSKATALOG.md"
HEADING = re.compile(r"(?m)^## (\d+)\. ")
BACKTICK = re.compile(r"\x60([^\x60]+)\x60")
XROM_ROW = re.compile(r"^\|\s*(\d{2},\d{2})\s*\|\s*([^|]+?)\s*\|")


def section(text, num):
    heads = list(HEADING.finditer(text))
    for i, match in enumerate(heads):
        if int(match.group(1)) == num:
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            return text[match.end():end]
    raise ValueError(f"Missing numbered section: {num}")


def command_tokens(s):
    """Only first cells of section 2 tables count, never mentions in prose."""
    tokens = set()
    for line in s.splitlines():
        if line.startswith("|"):
            cell = line.split("|")[1]
            tokens.update(m.group(1).strip() for m in BACKTICK.finditer(cell))
    return tokens


def matched(aliases, tokens):
    """Only explicitly listed aliases and their operand-suffixed forms."""
    return any(
        alias == token or token.startswith(alias + " ")
        for alias in aliases for token in tokens
    )


def xrom_rows(s):
    rows = {}
    for line in s.splitlines():
        match = XROM_ROW.match(line)
        if match:
            rows.setdefault(match.group(1), []).append(match.group(2).strip().strip(chr(96)))
    return rows


def keys(s):
    result = []
    for line in s.splitlines():
        if re.match(r"^\|\s*(?:Kopf|[1-8])\s*\|", line):
            cells = line.strip().strip("|").split("|")
            result.append(cells[1].strip())
    return result


def key_equal(expected, actual):
    return (
        expected == actual
        or expected == "SQRT" and "SQRT" in actual
        or expected == "RDN" and "RDN" in actual
        or expected == "BACKSPACE" and actual.startswith("←")
    )


def check(inv, md):
    baseline = inv["base_index"]
    xrom = inv["xrom_index"]
    keypad = inv["keyboard"]
    if len({r["name"] for r in baseline}) != len(baseline):
        raise ValueError("Duplicate baseline command")
    if len({r["xrom"] for r in xrom}) != len(xrom):
        raise ValueError("Duplicate XROM ID")
    if len({r["position"] for r in keypad}) != len(keypad):
        raise ValueError("Duplicate keyboard position")
    # Independent CAT-3 cross-check: 117 reconstructed vs 116 printed by Gosmann.
    # The one documented Gosmann omission is X>Y?, confirmed by the HP original.
    cat3 = inv["reconstructed_cat3"]["commands"]
    gosmann = inv["gosmann_cat3_transcription"]
    gosmann_names = gosmann["page9"] + gosmann["page10"] + gosmann["page11"]
    cat3_errors = []
    if len(cat3) != 117 or len(set(cat3)) != 117:
        cat3_errors.append("Expected 117 unique reconstructed CAT-3 names")
    if len(gosmann_names) != 116 or len(set(gosmann_names)) != 116:
        cat3_errors.append("Expected 116 unique Gosmann source names")
    if set(cat3) - set(gosmann_names) != {"X>Y?"}:
        cat3_errors.append("Gosmann vs HP difference must be exactly X>Y?")
    if set(gosmann_names) - set(cat3):
        cat3_errors.append("Unexpected Gosmann-only names")
    omitted_controls = set(inv["reconstructed_cat3"]["excluded_index_controls"])
    if set(cat3) != {record["name"] for record in baseline} - omitted_controls:
        cat3_errors.append("Reconstructed CAT-3 not consistent with main index")
    tokens = command_tokens(section(md, 2))
    missing_base = [r["name"] for r in baseline if not matched(r["aliases"], tokens)]
    xsections = {n: xrom_rows(section(md, n)) for n in (9, 10, 11)}
    profiles = {
        "HP82180A": 9,
        "HP41CX-EXTENDED": 10,
        "HP82182A-TIME": 11,
        "HP41CX-TIME": 11,
    }
    missing_xrom, wrong_xrom, duplicate_xrom = [], [], []
    for record in xrom:
        code = record["xrom"]
        actual = xsections[profiles[record["profile"]]].get(code, [])
        if not actual:
            missing_xrom.append(code)
        elif len(actual) != 1:
            duplicate_xrom.append(code)
        elif actual[0] != record["name"]:
            wrong_xrom.append([code, record["name"], actual[0]])
    unexpected_xrom = sorted({
        code for listing in xsections.values() for code in listing
        if code not in {record["xrom"] for record in xrom}
        and code not in inv["reserved_xrom_headers"]
    })
    actual_keys = keys(section(md, 7))
    missing_keys, wrong_keys = [], []
    for item in keypad:
        position = item["position"]
        if position > len(actual_keys):
            missing_keys.append(position)
        elif not key_equal(item["normal"], actual_keys[position - 1]):
            wrong_keys.append([position, item["normal"], actual_keys[position - 1]])
    problems = {
        "cat3_reconciliation": cat3_errors,
        "missing_base": missing_base,
        "missing_xrom": missing_xrom,
        "wrong_xrom": wrong_xrom,
        "duplicate_xrom": duplicate_xrom,
        "unexpected_xrom": unexpected_xrom,
        "missing_key_positions": missing_keys,
        "wrong_key_positions": wrong_keys,
    }
    passed = not any(problems.values()) and len(actual_keys) == len(keypad)
    return {
        "status": "PASS" if passed else "FAIL",
        "scope": "Textual inventory ONLY; not a ROM, CAT 3 or behavioral test",
        "cat3_reconstructed_count": len(cat3),
        "gosmann_cat3_count": len(gosmann_names),
        "base_count": len(baseline),
        "key_count": len(keypad),
        "xrom_by_profile": dict(Counter(r["profile"] for r in xrom)),
        "actual_key_rows": len(actual_keys),
        **problems,
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    inv = json.loads(INVENTORY.read_text(encoding="utf-8"))
    md = CATALOG.read_text(encoding="utf-8")
    result = check(inv, md)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(f"HP-41C textual inventory audit: {result['status']}")
        print(f"Baseline: {result['base_count']}; keypad: {result['key_count']}")
        print("XROM: " + ", ".join(f"{k}={v}" for k,v in result["xrom_by_profile"].items()))
        for key in ("cat3_reconciliation", "missing_base", "missing_xrom", "wrong_xrom", "duplicate_xrom",
                    "unexpected_xrom", "missing_key_positions", "wrong_key_positions"):
            if result[key]:
                print(f"ERROR {key}: {result[key]}")
        print("This does NOT prove actual historic-device behavior or CAT 3 ROM contents.")
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
