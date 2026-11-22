# HP 48GX – Teilprüfung G-2 bis G-8 (Checkpoint G01)

**Bearbeitungsstand:** 22.11.2026 · **Modell:** HP 48GX, Basisgerät, ohne Fremdkarten  
**Quelle:** HP, *48G Series User's Guide*, 8. Aufl. Dezember 1994, Anhang G, Seiten G-2–G-8. PDF: https://www.hp.com/ctg/Manual/c00442262.pdf  
**Quelldatei:** [hp48gx-operation-index-crosschecked-pages.json](../reference/hp48gx-operation-index-crosschecked-pages.json)  
**Zusätzliche unabhängige Namensquellen:** [AUR-Kapitel-3-Inhaltsverzeichnis](../reference/hp48gx-aur-command-index.json), [ROM-Baseline](../reference/hp48gx-rom-index-baseline.json)  
**Checkpoint-Matrix:** [hp48gx-audit-partitions.json](../reference/hp48gx-audit-partitions.json)

> **Prüfaussage:** Für alle **85 indexierten Zeilen** aus G-2 bis G-8 wurde hier der Datenbestand gegen die unabhängigen AUR-TOC- und ROM-Namensinventare abgeglichen. Die Originalscan-Seiten wurden **nicht** erneut zeilenweise visuell inspiziert. Daher bedeutet „ROM exakt“, „AUR vorhanden“ oder „OCR-Treffer“ **nicht** „historische Bedienung vollständig verifiziert“. Der Bearbeitungsabschnitt ist als **Quellenindex-Abgleich** abgeschlossen, **nicht** als visuell abgenommene historische Kommandobeschreibung.

## 1. Abdeckung und Risikoprofil

| Gedruckte Seite | PDF-Seite (1-basiert) | Indexzeilen | Exakte OCR-Worttreffer | Ohne exakten OCR-Worttreffer | Scan visuell freigegeben |
| --- | ---: | ---: | ---: | ---: | --- |
| G-2 | 482 | 13 | 9 | 4 | **Nein** |
| G-3 | 483 | 10 | 9 | 1 | **Nein** |
| G-4 | 484 | 14 | 13 | 1 | **Nein** |
| G-5 | 485 | 12 | 10 | 2 | **Nein** |
| G-6 | 486 | 10 | 4 | 6 | **Nein** |
| G-7 | 487 | 14 | 13 | 1 | **Nein** |
| G-8 | 488 | 12 | 7 | 5 | **Nein** |

**Gesamt G01:** 85 indexierte Zeilen; 65 exakte OCR-Tokenfunde, 20 ohne exakte OCR-Bestätigung. Diese OCR-Funde betreffen **Token**, keine validierte Textzeile mit richtiger Klasse/Funktion. Besonders riskant: G-6 und G-8 mit weniger als 60 % exakten Tokenfunden.

## 2. Nachvollziehbarer Zeilenabgleich

**Legende:** `ja` bei ROM oder AUR bedeutet nur wörtliche Gleichheit des Labels oder dessen normierter AUR-Kandidaten. Ein Name kann im UI verfügbar sein, ohne eine ROM-XLIB-Kennung zu besitzen. Für `CASE` enthält eine einzelne gedruckte G-6-Zeile mehrere Bedienvarianten; sie muss in der späteren UI-Matrix getrennt werden.

| Index-ID | Aufschrift in der Textübertragung | HP-Klasse | ROM exakt | AUR-TOC gleich/normalisiert | OCR-Token exakt | Quellstatus |
| --- | --- | --- | --- | --- | --- | --- |
| G-2:01 | `←A` | O | nein | nein | nein | **Scan offen** |
| G-2:02 | `↪A←` | O | nein | nein | nein | **Scan offen** |
| G-2:03 | `A→` | O | nein | nein | nein | **Scan offen** |
| G-2:04 | `↪A→` | O | nein | nein | nein | **Scan offen** |
| G-2:05 | `ABS` | F | ja | ja | ja | **Scan offen** |
| G-2:06 | `ACK` | C | ja | ja | ja | **Scan offen** |
| G-2:07 | `ACKALL` | C | ja | ja | ja | **Scan offen** |
| G-2:08 | `ACOS` | A | ja | ja | ja | **Scan offen** |
| G-2:09 | `ACOSH` | A | ja | ja | ja | **Scan offen** |
| G-2:10 | `ADD` | C | ja | ja | ja | **Scan offen** |
| G-2:11 | `AF` | O | nein | nein | ja | **Scan offen** |
| G-2:12 | `ALOG` | A | ja | ja | ja | **Scan offen** |
| G-2:13 | `AMORT` | O | ja | ja | ja | **Scan offen** |
| G-3:01 | `AMORT` | C | ja | ja | ja | **Scan offen** |
| G-3:02 | `AMRT` | O | nein | nein | ja | **Scan offen** |
| G-3:03 | `AND` | C/F | ja | ja | ja | **Scan offen** |
| G-3:04 | `ANIMATE` | C | ja | ja | ja | **Scan offen** |
| G-3:05 | `APPLY` | F | ja | ja | ja | **Scan offen** |
| G-3:06 | `ARC` | C | ja | ja | ja | **Scan offen** |
| G-3:07 | `ARCHIVE` | C | ja | ja | ja | **Scan offen** |
| G-3:08 | `AREA` | O | nein | nein | ja | **Scan offen** |
| G-3:09 | `ARG` | F | ja | ja | ja | **Scan offen** |
| G-3:10 | `ARRY→` | C | ja | ja | nein | **Scan offen** |
| G-4:01 | `→ARRY` | C | ja | ja | nein | **Scan offen** |
| G-4:02 | `ASIN` | A | ja | ja | ja | **Scan offen** |
| G-4:03 | `ASINH` | A | ja | ja | ja | **Scan offen** |
| G-4:04 | `ASN` | C | ja | ja | ja | **Scan offen** |
| G-4:05 | `ASR` | C | ja | ja | ja | **Scan offen** |
| G-4:06 | `ATAN` | A | ja | ja | ja | **Scan offen** |
| G-4:07 | `ATANH` | A | ja | ja | ja | **Scan offen** |
| G-4:08 | `ATICK` | C | ja | ja | ja | **Scan offen** |
| G-4:09 | `ATTACH` | C | ja | ja | ja | **Scan offen** |
| G-4:10 | `AUTO` | C | ja | ja | ja | **Scan offen** |
| G-4:11 | `AXES` | C | ja | ja | ja | **Scan offen** |
| G-4:12 | `BAR` | C | ja | ja | ja | **Scan offen** |
| G-4:13 | `BARPLOT` | C | ja | ja | ja | **Scan offen** |
| G-4:14 | `BAUD` | C | ja | ja | ja | **Scan offen** |
| G-5:01 | `BEEP` | C | ja | ja | ja | **Scan offen** |
| G-5:02 | `BEG` | O | nein | nein | ja | **Scan offen** |
| G-5:03 | `BESTFIT` | C | ja | ja | ja | **Scan offen** |
| G-5:04 | `BIN` | C | ja | ja | ja | **Scan offen** |
| G-5:05 | `BINS` | C | ja | ja | ja | **Scan offen** |
| G-5:06 | `BLANK` | C | ja | ja | ja | **Scan offen** |
| G-5:07 | `BOX` | C | ja | ja | ja | **Scan offen** |
| G-5:08 | `BOX` | O | ja | ja | ja | **Scan offen** |
| G-5:09 | `BOXZ` | O | nein | nein | ja | **Scan offen** |
| G-5:10 | `BUF LEN` | C | nein | nein | nein | **Scan offen** |
| G-5:11 | `BYTES` | C | ja | ja | ja | **Scan offen** |
| G-5:12 | `B→PV` | O | nein | nein | nein | **Scan offen** |
| G-6:01 | `B→R` | C | ja | ja | nein | **Scan offen** |
| G-6:02 | `CALC` | O | nein | nein | ja | **Scan offen** |
| G-6:03 | `CANCL` | O | nein | nein | ja | **Scan offen** |
| G-6:04 | `CASE / ↩CASE / ↪CASE` | C/O/O | nein | nein | nein | **Scan offen** |
| G-6:05 | `CEIL` | F | ja | ja | nein | **Scan offen** |
| G-6:06 | `CENTR` | C | ja | ja | nein | **Scan offen** |
| G-6:07 | `CF` | C | ja | ja | nein | **Scan offen** |
| G-6:08 | `%CH` | F | ja | ja | ja | **Scan offen** |
| G-6:09 | `✓CHK` | O | nein | nein | nein | **Scan offen** |
| G-6:10 | `CHOOS` | O | nein | nein | ja | **Scan offen** |
| G-7:01 | `CHOOSE` | C | ja | ja | ja | **Scan offen** |
| G-7:02 | `CHR` | C | ja | ja | ja | **Scan offen** |
| G-7:03 | `CIRCL` | O | nein | nein | ja | **Scan offen** |
| G-7:04 | `CKSM` | C | ja | ja | ja | **Scan offen** |
| G-7:05 | `CLEAR` | C | ja | ja | ja | **Scan offen** |
| G-7:06 | `CLK` | O | nein | nein | ja | **Scan offen** |
| G-7:07 | `CLKADJ` | C | ja | ja | ja | **Scan offen** |
| G-7:08 | `CLLCD` | C | ja | ja | ja | **Scan offen** |
| G-7:09 | `CLOSEIO` | C | ja | ja | ja | **Scan offen** |
| G-7:10 | `CLS` | C | nein | nein | nein | **Scan offen** |
| G-7:11 | `CLUSR` | C | nein | ja | ja | **Scan offen** |
| G-7:12 | `CLVAR` | C | ja | ja | ja | **Scan offen** |
| G-7:13 | `CNCT` | O | nein | nein | ja | **Scan offen** |
| G-7:14 | `CNRM` | C | ja | ja | ja | **Scan offen** |
| G-8:01 | `CNTR` | O | nein | nein | ja | **Scan offen** |
| G-8:02 | `→COL` | C | ja | ja | nein | **Scan offen** |
| G-8:03 | `+COL` | O | nein | nein | ja | **Scan offen** |
| G-8:04 | `COL+` | C | ja | ja | ja | **Scan offen** |
| G-8:05 | `−COL` | O | nein | nein | nein | **Scan offen** |
| G-8:06 | `COL−` | C | nein | ja | nein | **Scan offen** |
| G-8:07 | `COL→` | C | ja | ja | nein | **Scan offen** |
| G-8:08 | `COLΣ` | C | ja | ja | nein | **Scan offen** |
| G-8:09 | `COLCT` | C | ja | ja | ja | **Scan offen** |
| G-8:10 | `COLCT` | O | ja | ja | ja | **Scan offen** |
| G-8:11 | `COLCT` | O | ja | ja | ja | **Scan offen** |
| G-8:12 | `COMB` | F | ja | ja | ja | **Scan offen** |

## 3. Überprüfungswürdige Abweichungen – keine stillschweigende Gleichsetzung

| Originalaufschrift | G-Seite | Klasse | Grund / Prüfauftrag |
| --- | --- | --- | --- |
| `BUF LEN` | G-5 | C | Mutmaßlich typographischer Abstand gegenüber ROM \`BUFLEN\`; Originalscan/AUR-Einzelreferenz prüfen. |
| `CASE / ↩CASE / ↪CASE` | G-6 | C/O/O | Eine Zeile mit gemischten C/O/O-Typen; programmierbare \`CASE\`-Struktur und zwei Editor-Tastenaktionen getrennt erfassen. |
| `CLS` | G-7 | C | Kann ein durch Scan/Schriftwechsel verfälschtes \`CLΣ\` sein; griechisches Sigma anhand Scan prüfen. |
| `CLUSR` | G-7 | C | Eigenständiger Name im AUR (3-52), neben \`CLVAR\` (3-53); nicht ohne semantische Einzelprüfung als Alias deklarieren. |
| `COL−` | G-8 | C | Unicode-Minus statt ASCII-Hyphen in ROM \`COL-\`; Eingabezeichen bzw. gedruckte Glyphen prüfen. |

## 4. Konkretes Ergebnis und nächste Teilprüfung

- `G01` ist **für den systematischen ROM/AUR-Namensabgleich aller 85 gespeicherten Indexzeilen dokumentiert**. Keine neu erfundenen Befehlskennungen; historisch nicht programmierbare `O`-Aktionen bleiben eigene Kontexte.
- **Originalscan-Freigabe von G-2–G-8 bleibt offen.** Es fehlt derzeit eine unabhängige Originalbild-Prüfung insbesondere bei verschachtelten Pfeilen, griechischen Zeichen und gemischten Klassen wie `CASE`.
- **AUR-Stackwirkung** von `CLUSR`/`CLVAR` und `CLΣ` sowie Druckweise `BUF LEN` bleibt offen.
- **Nächster atomarer Prüfblock**: `G02` (G-9–G-15), dann die nächsten G-Blöcke, parallel separate `A01`–`A11`-Einzelbefehlsabschnitte. Je Block eigener Commit und Fortschrittsnachweis.

**Gate für historische Vollständigkeit: weiterhin NO_GO.** Technische Indexkonsistenz ist keine vollständige Funktionalitätsprüfung.
