# HP 48GX – Teilprüfung G-44 bis G-50 (G07)

**Prüfstand 22.11.2026.** Original: HP *48G Series User's Guide*, Edition 8, Appendix G-44–G-50, PDF-Seiten 524–530. https://www.hp.com/ctg/Manual/c00442262.pdf

**Prüfebene:** 87 im Quelltext überlieferte Indexzeilen einzeln gegen getrennte [AUR-Namensquelle](../reference/hp48gx-aur-command-index.json) und [ROM-Kennungen](../reference/hp48gx-rom-index-baseline.json) abgeglichen. Diese Namensprüfung bedeutet **nicht**, dass die Originalscan-Glyphen, Stack-Semantik oder Hardwarewirkung visuell/funktional freigegeben sind.

## 1. Seiten- und OCR-Differenzbilanz

| Druckseite | PDF-Seite | Indexzeilen | Exakte OCR-Tokenfunde | Nicht exakt per OCR bestätigt | Originalscan abgenommen |
| --- | ---: | ---: | ---: | ---: | --- |
| G-44 | 524 | 14 | 11 | 3 | **Nein** |
| G-45 | 525 | 12 | 8 | 4 | **Nein** |
| G-46 | 526 | 11 | 7 | 4 | **Nein** |
| G-47 | 527 | 13 | 7 | 6 | **Nein** |
| G-48 | 528 | 11 | 10 | 1 | **Nein** |
| G-49 | 529 | 13 | 12 | 1 | **Nein** |
| G-50 | 530 | 13 | 12 | 1 | **Nein** |

**Summe:** 87 Indexzeilen, 67 exakte OCR-Token-Präsenzen. OCR-Tokenfunde sind keine überprüften Scanzeilen. Hohe Prüfpriorität: G-47.

## 2. Alle Index-Zeilen dieser Etappe

| Quell-ID | gedrucktes Label (Textübertragung) | HP-Klasse | ROM wörtlich | AUR gedruckt/normalisiert | OCR-Token exakt | Visuelle Prüfung |
| --- | --- | --- | --- | --- | --- | --- |
| G-44:01 | `SORT` | C | ja | ja | ja | **offen** |
| G-44:02 | `SPHERE` | C | ja | ja | ja | **offen** |
| G-44:03 | `SQ` | A | ja | ja | ja | **offen** |
| G-44:04 | `SR` | C | ja | ja | ja | **offen** |
| G-44:05 | `SRAD` | C | ja | ja | ja | **offen** |
| G-44:06 | `SRB` | C | ja | ja | ja | **offen** |
| G-44:07 | `SRECV` | C | ja | ja | ja | **offen** |
| G-44:08 | `SST` | O | nein | ja | ja | **offen** |
| G-44:09 | `SST↓` | O | nein | ja | nein | **offen** |
| G-44:10 | `START` | C | ja | ja | ja | **offen** |
| G-44:11 | `↩ START` | O | nein | nein | nein | **offen** |
| G-44:12 | `↪ START` | O | nein | nein | nein | **offen** |
| G-44:13 | `STD` | C | ja | ja | ja | **offen** |
| G-44:14 | `STEP` | C | ja | ja | ja | **offen** |
| G-45:01 | `STEP` | O | ja | ja | ja | **offen** |
| G-45:02 | `STEQ` | C | ja | ja | ja | **offen** |
| G-45:03 | `STIME` | C | ja | ja | ja | **offen** |
| G-45:04 | `↑STK` | O | nein | nein | nein | **offen** |
| G-45:05 | `→STK` | O | nein | nein | nein | **offen** |
| G-45:06 | `→STK` | O | nein | nein | nein | **offen** |
| G-45:07 | `STO` | C | ja | ja | ja | **offen** |
| G-45:08 | `STOALARM` | C | ja | ja | ja | **offen** |
| G-45:09 | `STOF` | C | ja | ja | ja | **offen** |
| G-45:10 | `STOKEYS` | C | ja | ja | ja | **offen** |
| G-45:11 | `STO+` | C | ja | ja | ja | **offen** |
| G-45:12 | `STO−` | C | nein | ja | nein | **offen** |
| G-46:01 | `STO*` | C | ja | ja | nein | **offen** |
| G-46:02 | `STO/` | C | ja | ja | ja | **offen** |
| G-46:03 | `STOΣ` | C | ja | ja | nein | **offen** |
| G-46:04 | `STR→` | C | ja | ja | nein | **offen** |
| G-46:05 | `→STR` | C | ja | ja | nein | **offen** |
| G-46:06 | `STREAM` | C | ja | ja | ja | **offen** |
| G-46:07 | `STS` | O | nein | nein | ja | **offen** |
| G-46:08 | `STWS` | C | ja | ja | ja | **offen** |
| G-46:09 | `SUB` | C | ja | ja | ja | **offen** |
| G-46:10 | `SUB` | O | ja | ja | ja | **offen** |
| G-46:11 | `SUB` | O | ja | ja | ja | **offen** |
| G-47:01 | `SVD` | C | ja | ja | ja | **offen** |
| G-47:02 | `SVL` | C | ja | ja | ja | **offen** |
| G-47:03 | `SWAP` | C | ja | ja | ja | **offen** |
| G-47:04 | `SYM` | O | nein | nein | ja | **offen** |
| G-47:05 | `SYSEVAL` | C | ja | ja | ja | **offen** |
| G-47:06 | `←T` | O | nein | nein | nein | **offen** |
| G-47:07 | `↪←T` | O | nein | nein | nein | **offen** |
| G-47:08 | `T→` | O | nein | nein | nein | **offen** |
| G-47:09 | `↪T→` | O | nein | nein | nein | **offen** |
| G-47:10 | `%T` | F | ja | ja | nein | **offen** |
| G-47:11 | `→TAG` | C | ja | ja | nein | **offen** |
| G-47:12 | `TAN` | A | ja | ja | ja | **offen** |
| G-47:13 | `TAIL` | C | ja | ja | ja | **offen** |
| G-48:01 | `TANH` | A | ja | ja | ja | **offen** |
| G-48:02 | `TANL` | O | nein | nein | ja | **offen** |
| G-48:03 | `TAYLR` | C | ja | ja | ja | **offen** |
| G-48:04 | `TDELTA` | F | ja | ja | ja | **offen** |
| G-48:05 | `TEACH` | C | ja | ja | ja | **offen** |
| G-48:06 | `TEXT` | C | ja | ja | ja | **offen** |
| G-48:07 | `THEN` | C | ja | ja | ja | **offen** |
| G-48:08 | `TICKS` | C | ja | ja | ja | **offen** |
| G-48:09 | `TIME` | C | ja | ja | ja | **offen** |
| G-48:10 | `→TIME` | C | ja | ja | nein | **offen** |
| G-48:11 | `TINC` | F | ja | ja | ja | **offen** |
| G-49:01 | `TLINE` | C | ja | ja | ja | **offen** |
| G-49:02 | `TLINE` | O | ja | ja | ja | **offen** |
| G-49:03 | `TMENU` | C | ja | ja | ja | **offen** |
| G-49:04 | `TOT` | C | ja | ja | ja | **offen** |
| G-49:05 | `TRACE` | C | ja | ja | ja | **offen** |
| G-49:06 | `TRACE` | O | ja | ja | ja | **offen** |
| G-49:07 | `TRANSIO` | C | ja | ja | ja | **offen** |
| G-49:08 | `TRG*` | O | nein | nein | ja | **offen** |
| G-49:09 | `→TRG` | O | nein | nein | nein | **offen** |
| G-49:10 | `TRN` | C | ja | ja | ja | **offen** |
| G-49:11 | `TRNC` | F | ja | ja | ja | **offen** |
| G-49:12 | `TRUTH` | C | ja | ja | ja | **offen** |
| G-49:13 | `TSTR` | C | ja | ja | ja | **offen** |
| G-50:01 | `TVARS` | C | ja | ja | ja | **offen** |
| G-50:02 | `TVM` | C | ja | ja | ja | **offen** |
| G-50:03 | `TVMBEG` | C | ja | ja | ja | **offen** |
| G-50:04 | `TVMEND` | C | ja | ja | ja | **offen** |
| G-50:05 | `TVMROOT` | C | ja | ja | ja | **offen** |
| G-50:06 | `TYPE` | C | ja | ja | ja | **offen** |
| G-50:07 | `TYPES` | O | nein | nein | ja | **offen** |
| G-50:08 | `UBASE` | F | ja | ja | ja | **offen** |
| G-50:09 | `UFACT` | C | ja | ja | ja | **offen** |
| G-50:10 | `→UNIT` | C | ja | ja | nein | **offen** |
| G-50:11 | `UNTIL` | C | ja | ja | ja | **offen** |
| G-50:12 | `UPDIR` | C | ja | ja | ja | **offen** |
| G-50:13 | `UTPC` | C | ja | ja | ja | **offen** |

## 3. Programmartige Quelllabels ohne wörtlichen ROM-Namen

| Label | Quelle | HP-Typ | AUR-TOC-Entsprechung | Folgeschritt |
| --- | --- | --- | --- | --- |
| `STO−` | G-45:12 | C | ja | Alias/Reservat/Unicode/echten Zusatznamen anhand Original-AUR und Scan trennen |

## 4. Prüfhinweise und Abschlussentscheidung

- Die Quelltext-Zeilen sind nach Seiten und Zeilennummern erhalten geblieben; keine gleich geschriebenen UI-Kontexte wurden wegdedupliziert.
- **Nicht geprüft:** jeder Originalscan-Pixel der genannten Seiten, HP-Befehlsklassen in der Scan-Grafik, tatsächliche Stackargumente, Flags, Grenzwerte und ROM-Varianten. Besonders Pfeile/Σ/Sonderzeichen, Tabellenumbrüche und Bildschirmmenünamen erfordern die Sichtprüfung.
- **Auditresultat:** `SOURCE_TEXT_TO_ROM_AUR_CROSS_INDEX_DONE`, `SCAN_VISUAL_PENDING`, `AUR_STACK_PENDING`. Nach `G07` folgt der nächste separat versionierte Block.

**Besondere Warnung G-48:** Die Namensquelle enthält einen bekannten Fehlersatz `TAHN`, der zu `TANH` korrigiert wurde. Der Scanvergleich des Originals steht weiterhin aus.
