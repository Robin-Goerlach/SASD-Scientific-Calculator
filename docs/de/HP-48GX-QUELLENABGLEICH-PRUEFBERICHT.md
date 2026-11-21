# HP 48GX – Quellenübergreifender Funktionsinventar-Abgleich (Prüfbericht)

**Prüfdatum:** 21.11.2026 · **Gerät:** Serienmäßiger HP 48GX der HP-48G-Familie, **ohne** Drittanbieter-Erweiterungskarten.  
**Berichtsstatus:** **Namensinventare aller drei Referenzen systematisch abgeglichen; keine vollständige Freigabe des historischen Befehlsverhaltens oder aller eingebauten Daten.**

## 1. Unabhängige Quellengrundlagen und Grenzen

1. Hewlett-Packard, [*HP 48G Series User's Guide*, Edition 8 (Dezember 1994)](https://www.hp.com/ctg/Manual/c00442262.pdf), **Appendix G, G-1–G-58**. Offizielles **Operation Index**, umfasst programmierbare Befehle und interaktive Bedienoperationen. Original-PDF-SHA-256: `77b25f276277e90fbbd7ca1676d7440f69a844169fec6951382255df26e0782a`.
2. Hewlett-Packard, [*HP 48G Series Advanced User's Reference*, Edition 4 (Dezember 1994)](https://www.transnull.com/files/hp48/hp48gaur.pdf), **Kapitel 3: Command Reference, Inhaltsverzeichnis Contents-3 bis Contents-16**. Original-PDF-SHA-256: `c041081c07dac1716ed7667774ed43cd618d98b0cd5ddca4755eb797a67bdb96`.
3. [saturnus, `48gx.json`](https://github.com/ractive/saturnus/blob/main/crates/saturnus-cli/data/commands/48gx.json), auf ROM-Namen und XLIB-Kennungen basierender Index. Ein mit Lizenz-/Quellenhinweis versehenes Snapshot liegt unter [`docs/reference/hp48gx-rom-index-baseline.json`](../reference/hp48gx-rom-index-baseline.json).

**Wichtig:** Die beiden HP-PDFs sind Scans ohne Textebene. Die gedruckten Indexbezeichnungen wurden gegen die unabhängig strukturierte, durchsuchbare Textdarstellung der **Originalreferenzen** übertragen. Der komplette User-Guide-Operation-Index wurde zusätzlich per Tesseract auf allen 57 Tabellenseiten verarbeitet; OCR und Textdarstellung widersprechen sich bei Spezialzeichen. **Nicht jede Original-Scan-Zeile wurde abschließend per Auge freigegeben**. Die AUR-Zusatzprüfung betraf bisher das **gesamte Inhaltsverzeichnis von Kapitel 3**, nicht jede der hunderten Einzelbefehlsseiten mit Stackdiagrammen und Randfällen.

## 2. Numerische Bilanz der verglichenen Namensverzeichnisse

| Messgröße | Ergebnis | Was die Zahl bedeutet |
| --- | ---: | --- |
| Unterschiedliche Namen im ROM-Index | 517 | Technische ROM-Kataloggrundlage mit XLIB-Kennungen |
| AUR-Command-Reference-Inhaltsverzeichnis, Zeilen | 517 | Einzelreferenzzeilen, auch `NEXT` doppelt für verschiedene Strukturen |
| AUR, unterschiedliche gedruckte Namen | 516 | Nicht alles sind gewöhnliche Programm- oder Rechenbefehle |
| AUR, nach Zeichen-/Schreibnormalisierung mit ROM übereinstimmende Namen | 507 | **Namensvergleich, nicht Verhaltensprüfung** |
| AUR-Namen ohne direkte entsprechende ROM-Namenskennung | 8 | Interaktive Befehle, alte Zugänge und eigene I/O-/Plotnamen |
| ROM-Namen ohne eigenen Eintrag im AUR-Kapitel-3-Inhaltsverzeichnis | 10 | Vor allem Syntax-Delimiter und Einheiten-Namen |
| User's Guide Appendix-G-Tabellenzeilen | 696 | **57/57** Tabellenseiten G-2–G-58, mehrfach auftretende Labels ausdrücklich beibehalten |
| Unterschiedliche User-Guide-Aufschriften | 661 | Verschiedene Drucklabels in Bedien- und Programmkontext |
| User-Guide-Zeilen ausschließlich Klasse `O` | 179 | Interaktive Bedienhandlungen (nicht mit 179 zusätzlichen XLIBs verwechseln) |
| User-Guide-Zeilen mit mindestens einem `C`, `F` oder `A` | 517 | Druckzeilen, nicht eindeutige Befehlsnamen |
| Guide-Programmnamen ohne **wörtliche** ROM-Übereinstimmung | 26 | Unicode, reservierte Variablen, Aliase, teils offene Identitäten |
| Verschiedene reine UI-Aufschriften ohne wörtliche ROM-Übereinstimmung | 143 | Zusätzlich notwendiges Menü-/Editorinventar |

**Die beiden Zahlen 517 sind zufällig identisch, aber nicht gleichbedeutend:** 517 ROM-Namen, 517 AUR-Inhaltsverzeichniszeilen und 517 Guide-Tabellenzeilen mit C/F/A sind drei verschieden definierte Mengen. Es werden keine künstlichen Summen und Kompatibilitätsprozente daraus gebildet.

## 3. Acht AUR-Namenszugänge außerhalb der 517 ROM-Namen

| AUR-Name | Originalfundstelle | Einordnung | Sachliche Bewertung |
| --- | --- | --- | --- |
| `CLUSR` | 3-52 | ALIAS_ODER_EIGENER_BEFEHL_NOCH_PRUEFEN | Eigenständiger dokumentierter historischer Name; mögliche Unterschiede zu CLVAR bei Verzeichnissen prüfen |
| `DBUG` | 3-74 | INTERAKTIVE_DEBUGGER_OPERATION | Debugger-Aktivierung, interaktiver Zustand statt gewöhnlicher Rechenfunktion |
| `GRAPH` | 3-131 | KOMPATIBILITAETSZUGANG | Historischer Kompatibilitätszugang zur Grafik-/PICTURE-Umgebung |
| `IR` | 3-157 | IO_OPERATION | Aktivierung/Anwahl der IR-Kommunikation; genaue IOPAR-/Hardwarewirkung prüfen |
| `LAST` | 3-162 | ALIAS_ODER_KOMPATIBILITAETSZUGANG | Historischer Zugang zum Last-Argument-Verhalten; Zusammenhang mit LASTARG und Flag prüfen |
| `SIMU` | 3-307 | PLOT_MODUSAKTION | Plots gleichzeitig zeichnen statt nacheinander; Flag-/Plotmoduswirkung prüfen |
| `SST` | 3-320 | DEBUGGER_BEDIENOPERATION | Debugger-Einzelschritt; keine frei kombinierbare mathematische Funktion |
| `SST↓` | 3-320 | DEBUGGER_BEDIENOPERATION | Debugger-Einzelschritt in Unterprogramme; keine Rechenfunktion |

**Wichtigster Fall:** `CLUSR` und `CLVAR` sind **beide** als separate AUR-Einträge vorhanden (3-52 / 3-53). Das vereinfachte Benutzerhandbuch beschreibt beide als Löschen von Benutzervariablen. Die genaue Behandlung von Unterverzeichnissen, insbesondere nichtleeren, **darf nicht ohne AUR-Stack-/Fehlerprüfung als semantisch identisch unterstellt werden**. `GRAPH`/ `PICTURE` und `LAST`/`LASTARG` bleiben ebenfalls getrennt nach historischem Namen erfasst. `IR`/ `SIMU` werden **nicht** wegen fehlender ROM-ID verworfen.

## 4. Zehn ROM-Katalognamen ohne eigenen AUR-TOC-Eintrag

| ROM-Name | Arbeitseinordnung | Prüfergebnis |
| --- | --- | --- |
| `_` | SYNTAKTOKEN | Einheitenzeichen/Objektbegrenzer; AUR-TOC nicht als eigener Befehlsname |
| `RULES` | UNGEKLAERTER_ROM_NAME | Undokumentierter oder kontextabhängiger ROM-Name; UI-Regelmenü separat prüfen |
| `gmol` | EINHEITENBIBLIOTHEK | Bibliothekseinheiten-Bezeichnung, kein eigener AUR-TOC-Befehl |
| `lbmol` | EINHEITENBIBLIOTHEK | Bibliothekseinheiten-Bezeichnung, kein eigener AUR-TOC-Befehl |
| `rpm` | EINHEITENBIBLIOTHEK | Bibliothekseinheiten-Bezeichnung, kein eigener AUR-TOC-Befehl |
| `dB` | EINHEITENBIBLIOTHEK | Bibliothekseinheiten-Bezeichnung, kein eigener AUR-TOC-Befehl |
| `»` | SYNTAX | User-RPL-Programm-Enddelimiter, syntaktisch, nicht als AUR-Referenzkapitel |
| `«` | SYNTAX | User-RPL-Programm-Anfangsdelimiter, syntaktisch |
| `'` | SYNTAX | Quoting-/Algebraic-Begrenzer, syntaktisch |
| `DIR` | SYNTAX | Verzeichnisobjekt-Delimiter, syntaktisch |

Die zehn ROM-Namen bleiben im technischen Katalog, auch wenn kein gleichnamiger AUR-Kapitel-3-Eintrag vorhanden ist. Das Fehlen in einem Handbuch **beweist nicht**, dass ein ROM-Einstiegspunkt undefiniert oder unbenutzbar wäre.

## 5. 26 Schreibweisen-/Namenkonflikte des Benutzerhandbuchs

Der User's Guide enthält 26 verschiedene **programmierbar klassifizierte Drucklabels**, die keinem der 517 ROM-Namen **wortgetreu** entsprechen. Ein Teil davon ist bereits durch Unicode-Normalisierung erklärbar (`COL−` versus `COL-`, `Σ−` versus `Σ-`, `BUF LEN` versus `BUFLEN`); reservierte Objekte wie `CST`, `ΣDAT`, `PPAR`, `ΣPAR`, `VPAR`, `IOPAR`, `FV`, `PMT`, `PV`, `PYR` sind keine weiteren Rechenoperationen. Der genaue Alias-/Firmwarestatus anderer Namen ist eine Einzelprüfung.

| User-Guide-Druckname | Kandidat im ROM/AUR | Stand der Einordnung |
| --- | --- | --- |
| `BUF LEN` | `BUFLEN` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `CASE / ↩CASE / ↪CASE` | `CASE` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `CLS` | `CLΣ` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `CLUSR` | `CLUSR` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `COL−` | `COL-` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `CST` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `ΣDAT` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `EQ` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `FO^` | `F0λ` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `FV` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `GRAPH` | `GRAPH` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `HMS−` | `HMS-` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `IOPAR` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `LAST` | `LAST` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `ΣPAR` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `PMT` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `PRTPAR` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `PURG` | `PURGE` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `PV` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `PYR` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `ROW−` | `ROW-` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `SCLS` | `SCLΣ` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `STO−` | `STO-` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `VPAR` | Reservierte Variable, Alias oder noch ohne bestätigte Zuordnung | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `−` | `-` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |
| `Σ−` | `Σ-` | SOURCE_RAW_DIFFERENCE; ALIAS_NORMALIZATION_OR_RESERVED_SYSTEM_VARIABLE; REVIEW_OPEN |

## 6. Selbstständige Bedienungsoperationen und Kontextüberschneidungen

Die **179 rein als O klassifizierten Originalindexzeilen** umfassen **143 unterschiedliche UI-Aufschriften, die nicht zugleich wörtlich ROM-Namen sind**. Sie sind mit Quelle und Kontext im [Vollkatalog G-2 bis G-58](HP-48GX-OPERATION-INDEX-VOLLKATALOG.md) einzeln aufgeführt. Beispiele: `AMRT` (TVM-Formular), `DBUG`, `SST`, `SST↓` (Debugger), `CIRCL`, `DOT+`, `DOT−` (PICTURE), `ISECT`, `SLOPE`, `SHADE`, `ZIN`, `ZOUT`, `ZLAST` (Grafik), `CHOOS` (Formular), `CALC` (Formular-Zwischenberechnung), `EXPND` und `AF` (symbolischer Editor).

**Kontextkollisionen** wie `TRACE` (Matrixspur versus grafische Kurvenverfolgung), `NEXT` (User-RPL-Struktur versus Debuggeraktion), `COLCT` (Programm versus interaktiver Editor) oder `ROOT` (numerischer Befehl versus Plotanalyse) behalten getrennte Quellen- und Bedienkontexte. Die Auflistung ist ein **Inventar**, keine bereits funktionierende UI.

## 7. Zusätzlich nachgewiesene Fehler und Quellenwidersprüche

- `PVARS` bezeichnet Objekte und Speicherstatus eines **Ports**, nicht die Variablen des Elternverzeichnisses. Die Kurzbeschreibung im Hauptkatalog wurde korrigiert.
- `COLΣ` legt die Statistikspalten fest, es berechnet nicht deren Summe.
- `SCLΣ` passt Plotbereichsparameter an Statistikdaten an, es skaliert die Daten **nicht direkt**.
- `TRACE` ist als RPL-Kommando die **Matrixspur**, die gleichnamige PICTURE-Bedienfunktion verfolgt eine Kurve.
- Matrixzerlegungen `→COL/COL→`, `→ROW/ROW→`, `→DIAG/DIAG→` wurden in der Übersetzung korrigiert; eine individuelle Stackvariantenprüfung bleibt offen.
- Die Kapitel-10-Zahlen des User's Guide zu eingebauten Einheiten sind intern uneinheitlich (**147** gegenüber **9 plus 141**). Kein numerischer Einheitenabnahmestempel, bis die einzelnen Definitionen verglichen wurden.
- Für die Equation Library bestätigt Anhang F **315 Gleichungen, 396 Variablen, 15 Fachgebiete**. Diese **Kontrollsummen** sind geklärt, nicht die Ausführungssemantik aller einzelnen Gleichungen.
- `RSD` (Restvektor) benötigt weiterhin eine exakte Vorzeichen- und Parameterreihenfolgenprüfung anhand der AUR und unabhängiger Tests.

## 8. Konformität, maschinelle Tests und Abnahme

Die technischen Quellen liegen als eigenständige, nachprüfbare Daten vor: 

- [Original-ROM-Baseline (517)](../reference/hp48gx-rom-index-baseline.json)
- [AUR-Command-TOC (517 Zeilen)](../reference/hp48gx-aur-command-index.json)
- [User's-Guide-Operation-Index (696 Zeilen)](../reference/hp48gx-operation-index-crosschecked-pages.json)
- [Klassifizierte Differenzen](../reference/hp48gx-historical-index-differences.json)
- [Tesseract-Rohdaten und Fehlerprotokoll](HP-48GX-OPERATION-INDEX-ROHABGLEICH.md)

**Erledigt:** Quellenbasierte Inventarisierung der **gesamten Kapitel-3-Befehlsnamensliste** und aller **57 Operation-Index-Tabellenseiten**; bilaterale Namensabgleiche sowie explizite Ausnahmeklassen; frühere Kurzbeschreibungsfehler berichtigt; strukturierte Referenzdaten auf `main` und CI-Konsistenzprüfungen.

**Nicht erledigt und daher ausdrücklich keine historische Vollständigkeitsfreigabe:**

1. Visuelle Originalscan-Abnahme **jeder** G-2–G-58-Tabelle sowie AUR-Inhaltsverzeichniszeile für Sonderzeichen, Trennzeichen und Fehltranskriptionen.
2. Die **Einzelbefehlsprüfung der AUR-Kapitel-3-Seiten** mit sämtlichen Stackargumenten, Objekttypen, Fehlermeldungen, Seiteneffekten und ROM-Revisionen.
3. Ein unabhängiger Pocket-Guide- und echter HP-48GX-/Emulator-Regressionstest für historische Grenzfälle.
4. Die **315 Einzelgleichungen**, alle Konstanten und Einheitenfaktoren samt Dimensions-/Temperaturoffsets und sämtlichen User-Menus/Shift-Kontexten einzeln gegenzutesten.

**Entscheidung:** **Quellen-Namensabgleich: erstellt und mit Einzelfundstellen nachvollziehbar. Historische Gesamtvollständigkeit: OFFEN.** Das Vorliegen dieses Inventars ist **kein** Beleg für fertig implementierte Funktionen des SASD Scientific Calculator. Die iPhone-App-V1 kann nach Projektentscheidung unabhängig davon weiterentwickelt werden.
