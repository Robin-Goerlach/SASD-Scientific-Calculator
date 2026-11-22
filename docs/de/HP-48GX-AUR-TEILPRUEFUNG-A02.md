# HP 48GX – AUR-Teilprüfung A02 (Kommandos 51–100)

**Prüfstand:** 22.11.2026 · **Modell:** serienmäßiger HP 48GX (ohne fremde Erweiterungskarten)  
**Prüfumfang:** AUR-Inhaltsverzeichnis-Zeilen **51–100**, von `CLΣ` bis `→DIAG`.  
**Status:** *AUR-TOC ↔ ROM* sowie unabhängiger *Pocket-Guide-Textindex* abgeglichen; **Original-PDF-Scan, vollständige AUR-Stackdiagramme, Fehlerfälle und Geräteausführung noch nicht freigegeben**.

## Quellen

- Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Auflage 1994, **Kapitel 3, S. 3-52–3-85**; gedruckte Referenzseiten aus dem AUR-Inhaltsverzeichnis: https://www.transnull.com/files/hp48/hp48gaur.pdf
- James Donnelly, *HP 48G/GX Pocket Guide*, **Command Index, gedruckte S. 44, 46 und 48**. Textreproduktion mit teilweise deutlich beschädigten OCR-Glyphen: https://www.manualslib.com/manual/3743173/Hp-48g.html?page=46 ; https://www.manualslib.com/manual/3743173/Hp-48g.html?page=48 ; https://www.manualslib.com/manual/3743173/Hp-48g.html?page=50
- Separat versionierte Namensinventare: [AUR](../reference/hp48gx-aur-command-index.json) und [ROM-Index](../reference/hp48gx-rom-index-baseline.json). Die Original-Romanzeichen und XLIB-Kennungen werden nicht aus fehlerhaften OCR-Glyphen neu definiert.

**Quellenkritik:** Im Webseiten-Textbild sind beispielsweise `CLΣ` zu `CLE`, `COL→` zu `COL+` und `→DIAG` zu `+DIAG` verstümmelt. Die Spalte „Pocket-OCR“ ist **wörtlich der maschinelle Rohkandidat**, nicht die behauptete Druckvorlage. Abgleich bedeutet hier: plausible Stelle im unabhängigen Index anhand Nachbarbefehlen und Kurzbeschreibung identifiziert; **keine** visuelle Freigabe der tatsächlichen Glyphen. `DBUG` fehlt erwartungsgemäß im Pocket-Guide-Index programmierbarer Befehle, wird aber von AUR ausdrücklich aufgeführt.

## 1. Vollständiger 50-Einträge-Abgleich A02

| AUR # | Name im AUR | AUR-Referenz | ROM-Kennung vorhanden | Pocket-Guide-Druckseite | Pocket-OCR (ROH) | Zuordnungsstatus |
| ---: | --- | --- | --- | ---: | --- | --- |
| 51 | `CLΣ` | 3-52 | ja | 44 | `CLE` | OCR-/Schreibform prüfen |
| 52 | `CLTEACH` | 3-52 | ja | 44 | `CLTEACH` | wörtlich übereinstimmend |
| 53 | `CLUSR` | 3-52 | nein (AUR-Sondername) | 44 | `CLUSRE` | OCR-/Schreibform prüfen |
| 54 | `CLVAR` | 3-53 | ja | 44 | `CLYAR` | OCR-/Schreibform prüfen |
| 55 | `CNRM` | 3-53 | ja | 44 | `CHRM` | OCR-/Schreibform prüfen |
| 56 | `→COL` | 3-54 | ja | 46 | `+LOL` | OCR-/Schreibform prüfen |
| 57 | `COL+` | 3-54 | ja | 46 | `COL+` | wörtlich übereinstimmend |
| 58 | `COL−` | 3-55 | ja | 46 | `COL-` | OCR-/Schreibform prüfen |
| 59 | `COL→` | 3-56 | ja | 46 | `COL+` | OCR-/Schreibform prüfen |
| 60 | `COLCT` | 3-56 | ja | 46 | `COLLT` | OCR-/Schreibform prüfen |
| 61 | `COLΣ` | 3-57 | ja | 46 | `COLE` | OCR-/Schreibform prüfen |
| 62 | `COMB` | 3-58 | ja | 46 | `COMB` | wörtlich übereinstimmend |
| 63 | `CON` | 3-59 | ja | 46 | `CON` | wörtlich übereinstimmend |
| 64 | `COND` | 3-60 | ja | 46 | `COND` | wörtlich übereinstimmend |
| 65 | `CONIC` | 3-61 | ja | 46 | `CONIC` | wörtlich übereinstimmend |
| 66 | `CONJ` | 3-62 | ja | 46 | `COMJ` | OCR-/Schreibform prüfen |
| 67 | `CONLIB` | 3-63 | ja | 46 | `COMLIB` | OCR-/Schreibform prüfen |
| 68 | `CONST` | 3-63 | ja | 46 | `CONST` | wörtlich übereinstimmend |
| 69 | `CONT` | 3-64 | ja | 46 | `CONT` | wörtlich übereinstimmend |
| 70 | `CONVERT` | 3-65 | ja | 46 | `COMVERT` | OCR-/Schreibform prüfen |
| 71 | `CORR` | 3-65 | ja | 46 | `CORR,` | OCR-/Schreibform prüfen |
| 72 | `COS` | 3-66 | ja | 46 | `COS` | wörtlich übereinstimmend |
| 73 | `COSH` | 3-67 | ja | 46 | `COSH` | wörtlich übereinstimmend |
| 74 | `COV` | 3-67 | ja | 46 | `COV` | wörtlich übereinstimmend |
| 75 | `CR` | 3-68 | ja | 46 | `CR` | wörtlich übereinstimmend |
| 76 | `CRDIR` | 3-69 | ja | 46 | `CROIR` | OCR-/Schreibform prüfen |
| 77 | `CROSS` | 3-69 | ja | 46 | `CROSS` | wörtlich übereinstimmend |
| 78 | `CSWP` | 3-70 | ja | 46 | `CSWP` | wörtlich übereinstimmend |
| 79 | `CYLIN` | 3-70 | ja | 46 | `CYLIM` | OCR-/Schreibform prüfen |
| 80 | `C→PX` | 3-71 | ja | 46 | `C+P¥` | OCR-/Schreibform prüfen |
| 81 | `C→R` | 3-71 | ja | 46 | `C+R` | OCR-/Schreibform prüfen |
| 82 | `DARCY` | 3-72 | ja | 46 | `DARCY` | wörtlich übereinstimmend |
| 83 | `DATE` | 3-73 | ja | 46 | `DATE` | wörtlich übereinstimmend |
| 84 | `→DATE` | 3-73 | ja | 48 | `*DATE` | OCR-/Schreibform prüfen |
| 85 | `DATE+` | 3-74 | ja | 48 | `ORTE+` | OCR-/Schreibform prüfen |
| 86 | `DBUG` | 3-74 | nein (AUR-Sondername) | – | `—` | AUR-only (Debugger) |
| 87 | `DDAYS` | 3-75 | ja | 48 | `DORYS` | OCR-/Schreibform prüfen |
| 88 | `DEC` | 3-75 | ja | 48 | `OEC` | OCR-/Schreibform prüfen |
| 89 | `DECR` | 3-76 | ja | 48 | `DECR` | wörtlich übereinstimmend |
| 90 | `DEFINE` | 3-77 | ja | 48 | `DEFINE` | wörtlich übereinstimmend |
| 91 | `DEG` | 3-78 | ja | 48 | `DEG` | wörtlich übereinstimmend |
| 92 | `DELALARM` | 3-78 | ja | 48 | `DELALARM` | wörtlich übereinstimmend |
| 93 | `DELAY` | 3-79 | ja | 48 | `DELAY` | wörtlich übereinstimmend |
| 94 | `DELKEYS` | 3-80 | ja | 48 | `DELKEYS` | wörtlich übereinstimmend |
| 95 | `DEPND` | 3-81 | ja | 48 | `DEPMD` | OCR-/Schreibform prüfen |
| 96 | `DEPTH` | 3-82 | ja | 48 | `DEPTH` | wörtlich übereinstimmend |
| 97 | `DET` | 3-82 | ja | 48 | `DET` | wörtlich übereinstimmend |
| 98 | `DETACH` | 3-84 | ja | 48 | `DETACH` | wörtlich übereinstimmend |
| 99 | `DIAG→` | 3-84 | ja | 48 | `OIAG` | OCR-/Schreibform prüfen |
| 100 | `→DIAG` | 3-85 | ja | 48 | `+DIAG` | OCR-/Schreibform prüfen |

## 2. Ergebnisse der unabhängigen Kurzfunktionsprüfung

Die nachfolgenden Beobachtungen stammen aus der **tatsächlich eingesehenen** Pocket-Guide-Textwiedergabe und sollen nicht als gesicherte AUR-Stackdiagramme verstanden werden.

| Originalname | Belegbare Ergänzung / anzupassende Kurzbeschreibung |
| --- | --- |
| `CLΣ` | Statistikdaten in ΣDAT löschen; aus Text-Scan als `CLE` fehlinterpretiert |
| `CLUSR` | AUR und User Guide enthalten alten Namen, Pocket Guide identifiziert ihn als CLVAR-Alias |
| `CLVAR` | Löscht auch leere Unterverzeichnisse, nicht nur benannte Variablen; nichtleere Verzeichnisse noch separat prüfen |
| `→COL` | Zerlegt Array in Spalten und gibt die Anzahl zurück |
| `COL+` | Kann eine oder mehrere Spalten einfügen; Typ und Position beachten |
| `COL→` | Baut Array aus gegebenen Spalten und Anzahl auf; Pocket-Texterkennung verwechselt `→` mit `+` |
| `COLΣ` | Legt statistische X- und Y-Spalten fest, berechnet keine Spaltensumme |
| `CON` | Anzahl und Typ der Dimensionen: Dimension kann selbst als Array vorliegen |
| `CONJ` | Konjugiert komplexe Zahl ODER komplexes Array |
| `CONST` | Liefert Wert einer ausgewählten physikalischen Konstante |
| `CR` | Gibt Inhalt des Druckerpuffers aus; nicht lediglich ein Zeilenumbruchszeichen |
| `CROSS` | Vektorprodukt bei zwei- oder dreidimensionalen Vektoren; exakte Ausgabeform AUR prüfen |
| `CSWP` | Bei Vektoren entspricht Spaltentausch einem Elementtausch |
| `DATE` | Ausgabeformat hängt von Systemflag -42 ab |
| `DBUG` | AUR nennt Debugger-Bedienoperation, Pocket Guide führt sie nicht unter den programmierbaren Kommandos |
| `DELAY` | Druckausgabe-Verzögerung je Zeile in Sekunden |
| `DELKEYS` | Entfernt benutzerdefinierte Tastenbelegungen (Einzel-/Gesamtlöschung); genaue Argumente offen |
| `DIAG→` | Erzeugt Matrix aus Diagonale eines Arrays; Gegenrichtung zu →DIAG |
| `→DIAG` | Extrahiert Hauptdiagonale aus einer Matrix, nicht Matrix-Erzeugung |

## 3. Ergebnis und konkrete offene Abweichungen

- **50/50 AUR-Namenseinträge** mit gedruckter Kapitel-3-Referenzseite verknüpft. **49/50** sind in den drei eingesehenen Pocket-Guide-Textseiten anhand Kontext und Kurzbeschreibung zuordenbar; `DBUG` ist eine nicht gewöhnlich programmierbare Debugger-Bedienung und deshalb dort nicht im Kommandonamenindex zu erwarten.
- **48/50** haben eine direkte normierte ROM-Namensentsprechung; **`CLUSR` und `DBUG` sind zwei AUR-Namen ohne eigene 517er-ROM-Namenkennung**. Dies ist ein Namensvergleich, kein Ausführbarkeitsbeweis. Dies ist kein Beweis, dass die Befehle auf dem 48GX nicht erreichbar sind; sie sind über Alias-/UI-Kontexte zu untersuchen.
- **`CLUSR`**: Pocket Guide nennt ausdrücklich `CLVAR` als identische Kurzfunktion. Dokumentation als historischer Alias/Kompatibilitätsname möglich, aber Versionen und Fehlerfälle nicht als getestet ausgeben.
- **`COLΣ`**: Wählt die Statistikspalten, **keine** Summenberechnung. `CR` druckt den Inhalt des aktuellen Druckerpuffers und ist nicht ausschließlich ein Zeilenumbruch. `DIAG→` und `→DIAG` gehen in entgegengesetzte Richtungen.
- **OCR-Aufschriften** und die einzelnen AUR-Stackdiagramme **dürfen nicht** als visuell abgenommen gekennzeichnet werden. Besonders wichtig sind überladene Array-Funktionen, benutzerdefinierte Tastenbelegung und serielle Druckpufferwirkungen.

**Abnahmestatus A02:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE` / `POCKET_ORIGINAL_SCAN_NOT_SIGNED_OFF` / `AUR_COMMAND_STACK_NOT_SIGNED_OFF`. Nächster Namensblock: **A03 (101–150)**. In der separaten Tiefenprüfung werden alle 50 Einzelreferenzen mit typabhängigen Stackdiagrammen und Fehlerfällen abgearbeitet.
