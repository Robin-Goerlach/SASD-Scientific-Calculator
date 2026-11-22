# HP 48GX – Teilprüfung G-58 bis G-58 (G09)

**Prüfstand 22.11.2026.** Original: HP *48G Series User's Guide*, Edition 8, Appendix G-58–G-58, PDF-Seiten 538–538. https://www.hp.com/ctg/Manual/c00442262.pdf

**Prüfebene:** 13 im Quelltext überlieferte Indexzeilen einzeln gegen getrennte [AUR-Namensquelle](../reference/hp48gx-aur-command-index.json) und [ROM-Kennungen](../reference/hp48gx-rom-index-baseline.json) abgeglichen. Diese Namensprüfung bedeutet **nicht**, dass die Originalscan-Glyphen, Stack-Semantik oder Hardwarewirkung visuell/funktional freigegeben sind.

## 1. Seiten- und OCR-Differenzbilanz

| Druckseite | PDF-Seite | Indexzeilen | Exakte OCR-Tokenfunde | Nicht exakt per OCR bestätigt | Originalscan abgenommen |
| --- | ---: | ---: | ---: | ---: | --- |
| G-58 | 538 | 13 | 1 | 12 | **Nein** |

**Summe:** 13 Indexzeilen, 1 exakte OCR-Token-Präsenzen. OCR-Tokenfunde sind keine überprüften Scanzeilen. Hohe Prüfpriorität: G-58.

## 2. Alle Index-Zeilen dieser Etappe

| Quell-ID | gedrucktes Label (Textübertragung) | HP-Klasse | ROM wörtlich | AUR gedruckt/normalisiert | OCR-Token exakt | Visuelle Prüfung |
| --- | --- | --- | --- | --- | --- | --- |
| G-58:01 | `Σ+` | C | ja | ja | nein | **offen** |
| G-58:02 | `Σ−` | C | nein | ja | nein | **offen** |
| G-58:03 | `√` | A | ja | ja | nein | **offen** |
| G-58:04 | `\|` | F | ja | ja | nein | **offen** |
| G-58:05 | `1/()` | O | nein | nein | nein | **offen** |
| G-58:06 | `(())` | O | nein | nein | ja | **offen** |
| G-58:07 | `(←` | O | nein | nein | nein | **offen** |
| G-58:08 | `↪ (←` | O | nein | nein | nein | **offen** |
| G-58:09 | `→()` | O | nein | nein | nein | **offen** |
| G-58:10 | `→)` | O | nein | nein | nein | **offen** |
| G-58:11 | `↪ →)` | O | nein | nein | nein | **offen** |
| G-58:12 | `←→` | O | nein | nein | nein | **offen** |
| G-58:13 | `→` | C | ja | ja | nein | **offen** |

## 3. Programmartige Quelllabels ohne wörtlichen ROM-Namen

| Label | Quelle | HP-Typ | AUR-TOC-Entsprechung | Folgeschritt |
| --- | --- | --- | --- | --- |
| `Σ−` | G-58:2 | C | ja | Alias/Reservat/Unicode/echten Zusatznamen anhand Original-AUR und Scan trennen |

## 4. Prüfhinweise und Abschlussentscheidung

- Die Quelltext-Zeilen sind nach Seiten und Zeilennummern erhalten geblieben; keine gleich geschriebenen UI-Kontexte wurden wegdedupliziert.
- **Nicht geprüft:** jeder Originalscan-Pixel der genannten Seiten, HP-Befehlsklassen in der Scan-Grafik, tatsächliche Stackargumente, Flags, Grenzwerte und ROM-Varianten. Besonders Pfeile/Σ/Sonderzeichen, Tabellenumbrüche und Bildschirmmenünamen erfordern die Sichtprüfung.
- **Auditresultat:** `SOURCE_TEXT_TO_ROM_AUR_CROSS_INDEX_DONE`, `SCAN_VISUAL_PENDING`, `AUR_STACK_PENDING`. Nach `G09` folgt der nächste separat versionierte Block.
