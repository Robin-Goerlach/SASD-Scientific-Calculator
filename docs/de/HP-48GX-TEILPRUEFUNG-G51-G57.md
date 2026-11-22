# HP 48GX – Teilprüfung G-51 bis G-57 (G08)

**Prüfstand 22.11.2026.** Original: HP *48G Series User's Guide*, Edition 8, Appendix G-51–G-57, PDF-Seiten 531–537. https://www.hp.com/ctg/Manual/c00442262.pdf

**Prüfebene:** 84 im Quelltext überlieferte Indexzeilen einzeln gegen getrennte [AUR-Namensquelle](../reference/hp48gx-aur-command-index.json) und [ROM-Kennungen](../reference/hp48gx-rom-index-baseline.json) abgeglichen. Diese Namensprüfung bedeutet **nicht**, dass die Originalscan-Glyphen, Stack-Semantik oder Hardwarewirkung visuell/funktional freigegeben sind.

## 1. Seiten- und OCR-Differenzbilanz

| Druckseite | PDF-Seite | Indexzeilen | Exakte OCR-Tokenfunde | Nicht exakt per OCR bestätigt | Originalscan abgenommen |
| --- | ---: | ---: | ---: | ---: | --- |
| G-51 | 531 | 11 | 10 | 1 | **Nein** |
| G-52 | 532 | 13 | 5 | 8 | **Nein** |
| G-53 | 533 | 12 | 10 | 2 | **Nein** |
| G-54 | 534 | 10 | 5 | 5 | **Nein** |
| G-55 | 535 | 12 | 12 | 0 | **Nein** |
| G-56 | 536 | 13 | 6 | 7 | **Nein** |
| G-57 | 537 | 13 | 0 | 13 | **Nein** |

**Summe:** 84 Indexzeilen, 48 exakte OCR-Token-Präsenzen. OCR-Tokenfunde sind keine überprüften Scanzeilen. Hohe Prüfpriorität: G-52, G-54, G-56, G-57.

## 2. Alle Index-Zeilen dieser Etappe

| Quell-ID | gedrucktes Label (Textübertragung) | HP-Klasse | ROM wörtlich | AUR gedruckt/normalisiert | OCR-Token exakt | Visuelle Prüfung |
| --- | --- | --- | --- | --- | --- | --- |
| G-51:01 | `UTPF` | C | ja | ja | ja | **offen** |
| G-51:02 | `UTPN` | C | ja | ja | ja | **offen** |
| G-51:03 | `UTPT` | C | ja | ja | ja | **offen** |
| G-51:04 | `UVAL` | F | ja | ja | ja | **offen** |
| G-51:05 | `VAR` | C | ja | ja | ja | **offen** |
| G-51:06 | `VARS` | C | ja | ja | ja | **offen** |
| G-51:07 | `VEC` | O | nein | nein | ja | **offen** |
| G-51:08 | `VIEW` | O | nein | nein | ja | **offen** |
| G-51:09 | `↪ VIEW` | O | nein | nein | nein | **offen** |
| G-51:10 | `VIEW` | O | nein | nein | ja | **offen** |
| G-51:11 | `VPAR` | C | nein | nein | ja | **offen** |
| G-52:01 | `VTYPE` | C | ja | ja | ja | **offen** |
| G-52:02 | `VZIN` | O | nein | nein | ja | **offen** |
| G-52:03 | `VZOUT` | O | nein | nein | ja | **offen** |
| G-52:04 | `→V2` | O | ja | ja | nein | **offen** |
| G-52:05 | `→V3` | C | ja | ja | nein | **offen** |
| G-52:06 | `V→` | C | ja | ja | nein | **offen** |
| G-52:07 | `*W` | C | ja | ja | nein | **offen** |
| G-52:08 | `WAIT` | C | ja | ja | ja | **offen** |
| G-52:09 | `WHILE` | C | ja | ja | ja | **offen** |
| G-52:10 | `↩ WHILE` | O | nein | nein | nein | **offen** |
| G-52:11 | `WID→` | O | nein | nein | nein | **offen** |
| G-52:12 | `←WID` | O | nein | nein | nein | **offen** |
| G-52:13 | `WIREFRAME` | C | ja | ja | nein | **offen** |
| G-53:01 | `WSLOG` | C | ja | ja | ja | **offen** |
| G-53:02 | `ΣX` | C | ja | ja | nein | **offen** |
| G-53:03 | `ΣX^2` | C | ja | ja | nein | **offen** |
| G-53:04 | `XCOL` | C | ja | ja | ja | **offen** |
| G-53:05 | `XMIT` | C | ja | ja | ja | **offen** |
| G-53:06 | `XOR` | F | ja | ja | ja | **offen** |
| G-53:07 | `XPON` | F | ja | ja | ja | **offen** |
| G-53:08 | `XRECV` | C | ja | ja | ja | **offen** |
| G-53:09 | `XRNG` | C | ja | ja | ja | **offen** |
| G-53:10 | `XROOT` | A | ja | ja | ja | **offen** |
| G-53:11 | `XSEND` | C | ja | ja | ja | **offen** |
| G-53:12 | `XVOL` | C | ja | ja | ja | **offen** |
| G-54:01 | `XXRNG` | C | ja | ja | ja | **offen** |
| G-54:02 | `ΣX*Y` | C | ja | ja | nein | **offen** |
| G-54:03 | `(X,Y)` | O | nein | nein | nein | **offen** |
| G-54:04 | `X,Y→` | O | nein | nein | nein | **offen** |
| G-54:05 | `ΣY` | C | ja | ja | nein | **offen** |
| G-54:06 | `ΣY^2` | C | ja | ja | nein | **offen** |
| G-54:07 | `YCOL` | C | ja | ja | ja | **offen** |
| G-54:08 | `YRNG` | C | ja | ja | ja | **offen** |
| G-54:09 | `YSLICE` | C | ja | ja | ja | **offen** |
| G-54:10 | `YVOL` | C | ja | ja | ja | **offen** |
| G-55:01 | `YYRNG` | C | ja | ja | ja | **offen** |
| G-55:02 | `ZAUTO` | O | nein | nein | ja | **offen** |
| G-55:03 | `ZDECI` | O | nein | nein | ja | **offen** |
| G-55:04 | `ZDFLT` | O | nein | nein | ja | **offen** |
| G-55:05 | `ZFACT` | O | nein | nein | ja | **offen** |
| G-55:06 | `ZFACTOR` | F | ja | ja | ja | **offen** |
| G-55:07 | `ZIN` | O | nein | nein | ja | **offen** |
| G-55:08 | `ZINTG` | O | nein | nein | ja | **offen** |
| G-55:09 | `ZLAST` | O | nein | nein | ja | **offen** |
| G-55:10 | `ZOOM` | O | nein | nein | ja | **offen** |
| G-55:11 | `ZOUT` | O | nein | nein | ja | **offen** |
| G-55:12 | `ZSQR` | O | nein | nein | ja | **offen** |
| G-56:01 | `ZTRIG` | O | nein | nein | ja | **offen** |
| G-56:02 | `ZVOL` | C | ja | ja | ja | **offen** |
| G-56:03 | `+` | A | ja | ja | ja | **offen** |
| G-56:04 | `+/−` | O | nein | nein | nein | **offen** |
| G-56:05 | `+1−1` | O | nein | nein | nein | **offen** |
| G-56:06 | `−` | A | nein | ja | nein | **offen** |
| G-56:07 | `−()` | O | nein | nein | nein | **offen** |
| G-56:08 | `*` | A | ja | ja | ja | **offen** |
| G-56:09 | `*1` | O | nein | nein | nein | **offen** |
| G-56:10 | `/` | A | ja | ja | ja | **offen** |
| G-56:11 | `/1` | O | nein | nein | ja | **offen** |
| G-56:12 | `^` | A | ja | ja | nein | **offen** |
| G-56:13 | `^1` | O | nein | nein | nein | **offen** |
| G-57:01 | `<` | F | ja | ja | nein | **offen** |
| G-57:02 | `≤` | F | ja | ja | nein | **offen** |
| G-57:03 | `>` | F | ja | ja | nein | **offen** |
| G-57:04 | `≥` | F | ja | ja | nein | **offen** |
| G-57:05 | `=` | A | ja | ja | nein | **offen** |
| G-57:06 | `==` | F | ja | ja | nein | **offen** |
| G-57:07 | `≠` | F | ja | ja | nein | **offen** |
| G-57:08 | `!` | F | ja | ja | nein | **offen** |
| G-57:09 | `∫` | A | ja | ja | nein | **offen** |
| G-57:10 | `∂` | A | ja | ja | nein | **offen** |
| G-57:11 | `%` | A | ja | ja | nein | **offen** |
| G-57:12 | `π` | F | ja | ja | nein | **offen** |
| G-57:13 | `Σ` | F | ja | ja | nein | **offen** |

## 3. Programmartige Quelllabels ohne wörtlichen ROM-Namen

| Label | Quelle | HP-Typ | AUR-TOC-Entsprechung | Folgeschritt |
| --- | --- | --- | --- | --- |
| `VPAR` | G-51:11 | C | nein | Alias/Reservat/Unicode/echten Zusatznamen anhand Original-AUR und Scan trennen |
| `−` | G-56:6 | A | ja | Alias/Reservat/Unicode/echten Zusatznamen anhand Original-AUR und Scan trennen |

## 4. Prüfhinweise und Abschlussentscheidung

- Die Quelltext-Zeilen sind nach Seiten und Zeilennummern erhalten geblieben; keine gleich geschriebenen UI-Kontexte wurden wegdedupliziert.
- **Nicht geprüft:** jeder Originalscan-Pixel der genannten Seiten, HP-Befehlsklassen in der Scan-Grafik, tatsächliche Stackargumente, Flags, Grenzwerte und ROM-Varianten. Besonders Pfeile/Σ/Sonderzeichen, Tabellenumbrüche und Bildschirmmenünamen erfordern die Sichtprüfung.
- **Auditresultat:** `SOURCE_TEXT_TO_ROM_AUR_CROSS_INDEX_DONE`, `SCAN_VISUAL_PENDING`, `AUR_STACK_PENDING`. Nach `G08` folgt der nächste separat versionierte Block.

**Besondere Warnung G-57:** Für die 13 Symbol-/Operatorzeilen liegen **null** unabhängig bestätigte OCR-Tokenfunde vor. Die manuelle Textübertragung aus dem Index darf nicht als Sichtabnahme der Originalglyphen ausgegeben werden.
