"""Regression tests for the HP-41C documentary inventory audit.

Tests intentionally damage the reference text to prove that the checker detects
missing items; success here does NOT certify historic instruction behavior.
"""
import copy
import json
import unittest
from pathlib import Path

import audit_hp41c_functions as audit


ROOT = Path(__file__).resolve().parents[1]


class InventoryAuditTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.inventory = json.loads(
            (ROOT / "docs/reference/hp41c-command-inventory.json").read_text(encoding="utf-8")
        )
        cls.markdown = (
            ROOT / "docs/de/HP-41C-FUNKTIONSKATALOG.md"
        ).read_text(encoding="utf-8")

    def test_pristine_inventory_passes(self):
        result = audit.check(self.inventory, self.markdown)
        self.assertEqual(result["status"], "PASS", result)
        self.assertEqual(result["cat3_reconstructed_count"], 117)
        self.assertEqual(result["gosmann_cat3_count"], 116)
        self.assertEqual(result["key_count"], 39)
        self.assertEqual(result["alpha_key_count"], 35)
        self.assertEqual(sum(result["xrom_by_profile"].values()), 95)

    def test_missing_base_function_fails(self):
        original = "| `ABS` |"
        self.assertIn(original, self.markdown)
        broken = self.markdown.replace(original, "| `MISSING_ABS` |", 1)
        result = audit.check(self.inventory, broken)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("ABS", result["missing_base"])

    def test_incorrect_xrom_name_fails(self):
        original = "| 25,01 | ALENG |"
        self.assertIn(original, self.markdown)
        broken = self.markdown.replace(original, "| 25,01 | BROKEN |", 1)
        result = audit.check(self.inventory, broken)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(any(row[0] == "25,01" for row in result["wrong_xrom"]))

    def test_duplicate_xrom_number_fails(self):
        original = "| 25,01 | ALENG |"
        self.assertIn(original, self.markdown)
        broken = self.markdown.replace(original, original + "\n" + original, 1)
        result = audit.check(self.inventory, broken)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn("25,01", result["duplicate_xrom"])

    def test_bad_normal_key_fails(self):
        original = "| 1 | Σ+ |"
        self.assertIn(original, self.markdown)
        broken = self.markdown.replace(original, "| 1 | INVALID |", 1)
        result = audit.check(self.inventory, broken)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(result["wrong_key_positions"])

    def test_alpha_shift_wrong_symbol_fails(self):
        original = "| 06 | `1/X` | `B` | `b` |"
        self.assertIn(original, self.markdown)
        broken = self.markdown.replace(
            original, "| 06 | `1/X` | `B` | `z` |", 1
        )
        result = audit.check(self.inventory, broken)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn([6, "shifted_alpha", "b", "z"], result["changed_alpha"])

    def test_missing_alpha_key_fails(self):
        broken = "\n".join(
            line for line in self.markdown.split("\n")
            if not line.startswith("| 05 | `Σ+` |")
        )
        self.assertNotEqual(broken, self.markdown)
        result = audit.check(self.inventory, broken)
        self.assertEqual(result["status"], "FAIL")
        self.assertIn(5, result["missing_alpha"])

    def test_gosmann_crosscheck_detects_false_reconciliation(self):
        inv = copy.deepcopy(self.inventory)
        inv["gosmann_cat3_transcription"]["page11"].append("X>Y?")
        result = audit.check(inv, self.markdown)
        self.assertEqual(result["status"], "FAIL")
        self.assertTrue(result["cat3_reconciliation"])


if __name__ == "__main__":
    unittest.main()
