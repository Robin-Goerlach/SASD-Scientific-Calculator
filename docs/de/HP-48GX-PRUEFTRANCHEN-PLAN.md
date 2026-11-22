# HP 48GX – kleine, wiederaufnehmbare Prüfpakete und Aufwand

**Stand:** 22.11.2026 · **Umfang:** Historischer Funktionskatalog des **serienmäßigen HP 48GX**, ohne Fremdkarten.  
**Verbindliche Fortschrittsquelle:** [`hp48gx-audit-partitions.json`](../reference/hp48gx-audit-partitions.json) · **Zentrales Issue:** [#9](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/9).

> Ein `PASS` des GitHub-CI bedeutet lediglich **Datenkonsistenz**. Historische Katalogvollständigkeit ist erst dann nachgewiesen, wenn sämtliche Quellseiten und eingebauten Datensätze inklusive historischer Modellabgrenzung geprüft und keine offenen Differenzen unbereinigt sind. **Zeitüberschreitungen verhindern keine Arbeitserhaltung:** jede Tranche umfasst ihren eigenen Markdown-Bericht + Checkpoint-Update + erfolgreichen Konsistenztest.

## 1. Zwei verschiedene Abnahmeziele

- **I – Vollständiger historischer Funktions- und Datenkatalog:** Jede dokumentierte User-RPL-Funktion, jede interaktive Operation, jede Taste/Shift-/Menüaktion, jede eingebaute Gleichung, Einheit und Konstante ist mit Identität, Originalfundstelle, Kontext und Gültigkeitsprofil nachgewiesen. Hier müssen keine einzelnen RPL-Stackdiagramme bis ins letzte Fehlerdetail implementiert sein.
- **V – Verhaltens-/Kompatibilitätsspezifikation:** Für jeden passenden Befehl werden Stack-Ein-/Ausgang, Objekttypen, Flags, Nebenwirkungen, Zahlengenauigkeit und Fehlerfälle einzeln gegen AUR/Hardware geprüft. **Das ist mehr Aufwand als eine vollständige Funktionsliste und kein V1.0-Blocker.**

## 2. Noch offene, klein bemessene Tranchen

| Serie | Ziel | Aufteilung | Restliche Prüfpakete zum Stand 22.11.2026 | Wichtigste Freigabe |
| --- | --- | --- | ---: | --- |
| A09–A11 | AUR-Namensindex + unabhängiger Pocket-Guide-Kurznachweis | Je 50 AUR-Positionen, letzter Block 17 | **3** | Alle 517 AUR-TOC-Einträge in den Einzelberichten, Abweichungen kategorisiert |
| S01–S09 | **Originalscan-Bildprüfung** des HP-Operation-Index, einschließlich Legende G-1 | Je etwa sieben Originalseiten | **9** | Jede der 58 gedruckten Seiten visuell, Zeile für Zeile, mit Quellenhash/Scanbeleg |
| E01–E13 | Jede der **315** original eingebauten Equation-Library-Formeln als Funktions-Metadatensatz | Ca. 25 Formeln je Paket | **13** | Nummerierung/Formeln/Variablen inkl. 396 Variablen gezählt und nachvollziehbar referenziert; lizenzgerechte Beschreibung |
| U01–U06 | Einheitenkatalog, inklusive Aufklärung des Widerspruchs »147« vs. »9+141« | Ca. 25 Definitionen pro Paket | **6** | Alle tatsächlichen Unit-IDs, Dimensionen und nötigen Umrechnungen erfasst |
| K01–K04 | 49 Tasten, alle Shift-/Alpha-/User-Kontexte; Menüs/Editoren, Flags, reservierte Variablen, Ports/ROM-Profile | Vier getrennte Themenpakete | **4** | Explizite Kontext-/Erreichbarkeitsliste und Modell-/Revisionsfilter |
| F01–F02 | Dreiquellen-Bilanz, Lückenbereinigung, Quellen-Sichtfreigabe, Finalreport | Zwei Integrationspakete | **2** | Null unbegründete Deltas, dokumentiertes Abnahmesiegel für **I** oder offener Mangelbericht |
| **Summe I** | **Vollständigkeit der Funktionsliste und eingebauten Daten** | | **37 weitere kleine Prüfpakete** | Kein geschönter 100-%-Status |
| V01–V21 | Einzelne AUR-Befehlsreferenzen, Objekttypen/Stack, Flags, Fehler- und Sonderfälle | Ca. 25 der 517 AUR-Namenseinträge je Paket | **zusätzlich 21** | AUR-Stackdiagramme je Befehl mit Quellenbeleg, gegebenenfalls Originalgerät/Emulator |
| **Summe I + V** | **Katalog plus technische Verhaltens-/Konformitätsreferenz** | | **ca. 58 weitere Prüfpakete** | Jeweils getrennte Freigaben |

**Wichtig:** Das sind **Planungsgrößen, keine zugesagten Ausführungszeiten**. Je Chat können mehrere Pakete abgeschlossen werden; bei komplexen Scans auch nur eins. Die Paketanzahl kann bei neuen Quellwidersprüchen steigen oder durch Zusammenlegen leichter Teile sinken.

## 3. Was bereits überprüfbar erledigt ist

- **G01–G09:** Alle 696 übernommenen Operation-Index-Quelltextzeilen G-2 bis G-58 sind in neun separaten Reports gegen AUR/ROM-Namen verglichen (gespeicherte Checkpoint-Stufe **Quellindexvergleich**). **0** Originalscan-Seiten visuell abgenommen.
- **A01:** AUR-Namen 1–50; unabhängiger Pocket-Guide-Textabgleich dokumentiert.
- **A02:** AUR-Namen **51–100**; 48 direkte ROM-Namenszuordnungen, zwei Sonderfälle (`CLUSR` und `DBUG`), **49** Zuordnungen im unabhängigen Pocket-Guide-Textindex, Debugger-Bedienaktion `DBUG` dort nicht enthalten. [Bericht](HP-48GX-AUR-TEILPRUEFUNG-A02.md).
- **A03:** AUR-Namen **101–150**, alle 50 normierten ROM-Namen zugeordnet. **50/50** Pocket-Guide-Nachweise in kombinierter Web-OCR/PDF-Textsicht; `ENDSUB` fehlt in Web-OCR, ist im PDF-Text nachgewiesen. `ERRO` versus `ERR0` bleibt ein OCR-Glyphenfall; `ENDSUB`-Kurzbeschreibung auf Gesamtzahl berichtigt. [Bericht](HP-48GX-AUR-TEILPRUEFUNG-A03.md).
- **A04:** 151–200, 47 direkte ROM-Namen, drei separate Sonderfälle (`GRAPH`, `IR`, `LAST`). 50/50 Kontexttreffer im Pocket-Guide-Text; OCR-Deltas bei `GRAD`, `GXOR`, `HMS→`/`→HMS` und Minuszeichen. [Bericht](HP-48GX-AUR-TEILPRUEFUNG-A04.md).
- **A05:** AUR-Positionen 201–250 dokumentiert: 50 Quellindexpositionen, **49 verschiedene Namen** wegen zwei `NEXT`-Indexzeilen, 50 normierte ROM-Zuordnungen auf Positionsebene und 49 eigenständige Pocket-Namensbelege (Doppel-`NEXT` nur einmal). [Bericht](HP-48GX-AUR-TEILPRUEFUNG-A05.md). Differenzen u.a. `↑MATCH`/`↓MATCH` in Pocket-OCR beide `MMATCH`; `ΣLINE`/`LR` auf aktives Fit-Modell präzisiert.
- **A06:** AUR-Positionen 251–300 (`NUMX` bis `PVARS`), 50 verschiedene Namen, 50/50 ROM-XLIB-Namen und unabhängige Pocket-Guide-Textpositionen. OCR-Quellenunterschiede bei `NΣ`/`NZ` sowie `PROMPT`/`PRMPT`; Kurzfunktionen `PROMPT`, `PRSTC`, `OLDPRT`, `PREDV`, `NUMX`/`NUMY` u. a. im Hauptkatalog korrigiert. [Bericht](HP-48GX-AUR-TEILPRUEFUNG-A06.md).
- **A07:** AUR-Positionen 301–350 (`PVIEW` bis `RR`), 50 verschiedene Namen, 50/50 direkte ROM-XLIB-Namenszuordnungen und 50/50 Kontextbelege aus dem unabhängigen Pocket-Guide-Text (gedruckte S. 60, 62, 64). OCR-Abweichungen bei Pfeilen, Sigma, `RKFSTEP` und Zeilenoperatoren; Beschreibungen u.a. von `QR`, `QUAD`, `PVIEW`, `RND`, `ROLL`, `ROLLD`, `ROW-` im Hauptkatalog präzisiert. [Bericht](HP-48GX-AUR-TEILPRUEFUNG-A07.md).
- **A08:** 351–400 (`RRB`–`STEP`), 50 AUR-Positionen, **47 direkte ROM-Namenseinträge**, drei UI-/Debugger-Sonderfälle `SIMU`, `SST`, `SST↓`. **48/50** im unabhängigen Pocket-Guide-Command-Index-Text; `SST` und `SST↓` nur in RUN-Menü/Debugger-Darstellung. Quellenkonflikt `SCLΣ`/`SCLS`/`SCLZ` sowie `SCATR PLOT`/`SCATRPLOT` und `SST↓`/`SST+` offen. [Bericht](HP-48GX-AUR-TEILPRUEFUNG-A08.md).
- Insgesamt **400 AUR-Indexpositionen** aus A01–A08 dokumentiert; **397** mit unabhängiger Pocket-Guide-*Command-Index*-Textzuordnung (`DBUG`, `SST`, `SST↓` ausgenommen). Originalscan- und vollständige AUR-Stackfreigaben unverändert 0.
- Kurzbeschreibungen aus A02 für `CLVAR`, `CLΣ`, `COL±`, `CON`, `CONJ`, `CR`, `CROSS`, `CSWP`, `DATE`, `DELAY` und `DELKEYS` im Hauptkatalog präzisiert.

## 4. Priorisierung und Übergabe bei Zeitüberschreitung

1. **Nächste Tranche:** **A09 (401–450)**. Vorher immer neu die [Fortschrittsdatei](../reference/hp48gx-audit-partitions.json) lesen, nicht auf Chattext verlassen.
2. Vor jedem Commit alle Quelllabels und Sonderfälle in einer Einzeltabelle vollständig erfassen; nicht nur Trefferquoten speichern.
3. Bei jeder Tranche **zuerst Bericht speichern**, anschließend **Fortschritts-JSON aktualisieren**, danach GitHub Actions Ergebnis prüfen. Ohne erfolgreichen Bericht keine `CHECKED`-Markierung.
4. **Quellensperre:** Eine visuelle Abnahme des Originalscans darf erst nach tatsächlicher Bildsichtprüfung mit verifizierbarer PDF-Seite/Hash und dokumentierter Zeile erfolgen. Der online durchsuchbare PDF-Text oder eine Tesseract-Zeile reicht dafür nicht. Falls Web-/Download-Zugriff auf Originalbilder zu groß oder blockiert ist: diese Teilprüfung bleibt `BLOCKED_SOURCE_IMAGE_ACCESS`; niemals `PASS` vortäuschen.
5. **Verhaltensprüfung V** kann nach ausreichend vollständig belegter Liste I durchgeführt werden; AUR-Stackdiagramme und reale HP-48GX-Rundung brauchen später separate Testfälle.
6. Bei einem Timeout **nicht versprechen, unbeaufsichtigt weiterzuarbeiten**. Alle tatsächlich abgeschlossenen Pakete bleiben per Git-Commit erhalten; beim nächsten Chat erfolgt die Fortsetzung exakt ab `next_partition`.

**Produktentscheidung:** Release-M1/M2 (klassischer iPhone-RPN-Rechner, offline, stabil, ohne Abonnement) wird durch diese langfristige historische Forschung **nicht** blockiert.
