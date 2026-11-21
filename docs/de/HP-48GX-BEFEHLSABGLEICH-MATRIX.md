# HP 48GX – unabhängiger Befehls-/Operationsabgleich (Prüfmatrix)

**Erstellt:** 21.11.2026 · **Status:** Teilprüfung, keine Gesamtfreigabe · **Referenzgerät:** HP 48GX ohne optionale Karten  
**Hauptkatalog:** [HP-48GX-FUNKTIONSKATALOG.md](HP-48GX-FUNKTIONSKATALOG.md) · **Auditregeln:** [HP-48GX-VOLLSTAENDIGKEITSAUDIT.md](HP-48GX-VOLLSTAENDIGKEITSAUDIT.md).

> **Unbedingt beachten:** Die hier aufgeführten Seitenverweise aus dem saturnus-Datensatz `manuals.json` sind **automatisch aus einem Sekundärindex übernommene Fundstellen-HINWEISE, KEIN Nachweis einer manuellen vollständigen Buchprüfung**. Für echte Abnahme muss die betreffende AUR-Seite im originalen PDF nachgeprüft und die Semantik je Fall kontrolliert werden. Bei unbekannter Seitenposition ist die Funktion nicht automatisch falsch/fehlend.

## A. Quellen und Abgrenzung

- **U:** Hewlett-Packard, *HP 48G Series User's Guide*, 8. Ausgabe, Dez. 1994, 00048-90126; **Appendix G: Operation Index, G-1 bis G-58**: https://www.hp.com/ctg/Manual/c00442262.pdf
- **A:** Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Ausgabe, Dez. 1994, 00048-90136, **Kapitel 3**: https://literature.hpcalc.org/community/hp48g-aur-en.pdf
- **P:** James Donnelly, *HP 48G/GX Pocket Guide*, Command Index ab S. 41: https://literature.hpcalc.org/community/hp48g-pg-en.pdf
- **R:** saturnus: aus ROM gewonnene Namen + Kennungen: https://github.com/ractive/saturnus/blob/main/crates/saturnus-cli/data/commands/48gx.json
- **S:** saturnus: für mehrere HP-Modelle gesammelter, **nicht unabhängiger** manueller Seitenverweis-Index: https://github.com/ractive/saturnus/blob/main/crates/saturnus-cli/data/commands/manuals.json
- **V:** saturnus: zusammengetragene Kurzreferenz; modellübergreifend, **nicht gleichzusetzen mit AUR**: https://github.com/ractive/saturnus/blob/main/crates/saturnus-cli/data/commands/reference.json

**Fundseitenzählung:** Die `U`-/`A`-Spalten nennen PDF-Seitennummern aus Quelle S (bei Quelle U entspricht Appendix G nicht dem Beginn des PDFs); sie sind **noch nicht** mit den gedruckten Seiten abgeglichen. Direkt geprüfte G-Nachweise werden im Abschnitt C ausdrücklich mit der **gedruckten Appendix-G-Seite** geführt.

**Quellenstand:** Exakt `517` Namenseinträge aus Quelle R. `reference.json` enthält für alle `517` Namen einen Beschreibungsschlüssel; das ist **kein zweiter unabhängiger Vollständigkeitsbeweis**, da die Referenz aus demselben Projekt stammt.

## B. Rechnerischer Baseline-Vergleich ohne Schönfärberei

| Aussage | Anzahl | Bedeutung |
| --- | ---: | --- |
| Datensätze in `48gx.json` | **517** | ROM-basiertes Quelldateninventar |
| Eindeutige ROM-Befehlsnamen | **517** | Kein Namensduplikat in der Quelle |
| Mit mindestens einem AUR-Fundstellenhinweis in `manuals.json` | **464** | **Hinweis**, nicht AUR-Einzelnachweis |
| Mit mindestens einem User's-Guide-Fundstellenhinweis in `manuals.json` | **204** | **Hinweis**, nicht Appendix-G-Einzelnachweis |
| Hinweise aus beiden Büchern | **197** | Fundstellen überlappen |
| Mindestens einer der beiden Hinweise | **471** | Noch nicht gleichbedeutend mit vollständig geprüft |
| Ohne Fundstellenhinweis in beiden Büchern | **46** | Offene Einträge, nicht automatisch Fehlfunktionen |

Alle `517` Zeilen in Abschnitt D behalten zunächst Status **`UNVERIFIED`**. Einzelne Einträge des Originalhandbuchs aus dem Operation Index werden separat in C aufgeführt; diese Einträge beweisen ihre Präsenz dort, **nicht** das Fehlen anderer Operationen.

## C. Erste direkt gegen den Original-Operation-Index geprüfte Bedienaktionen

Die folgenden Namen/Bedienkontexte wurden in einer ersten quellengebundenen Sichtprüfung aus dem offiziellen HP-User's-Guide, Appendix G, G-2 bis G-16, festgestellt; **dies sind ausdrücklich nur Stichproben und ausgewählte Fälle innerhalb dieses Abschnitts, kein vollständiger G-2–G-16-Abgleich**. Gleiche sichtbare Bezeichnungen erhalten separate Kontextschlüssel. Die Deutschtexte sind eigenständige Kurzbeschreibungen.

| Gedruckte G-Seite | Name / Kontext | Umfeld | Bedeutung | Kategorie | Prüfvermerk |
| --- | --- | --- | --- | --- | --- |
| G-2 | ←A | EquationWriter/RULES | Assoziiert einen Term nach links | O | eigene interaktive Bedienung |
| G-2 | ↪←A | EquationWriter/RULES | Wiederholt Assoziation links bis keine Änderung möglich ist | O | von ←A getrennt |
| G-2 | A→ | EquationWriter/RULES | Assoziiert einen Term nach rechts | O | eigene interaktive Bedienung |
| G-2 | ↪A→ | EquationWriter/RULES | Wiederholt Assoziation rechts | O | von A→ getrennt |
| G-2 | AF | EquationWriter/RULES | Addiert Brüche symbolisch | O | eigener UI-Menüeintrag |
| G-3 | AMRT | TVM/interaktiver Solver | Amortisationsrechnung aus interaktivem TVM-Eingabedialog | O | von programmierbarem AMORT unterscheiden |
| G-4 | BEG | TVM | Umschalter Zahlungen am Periodenanfang/-ende | O | gegen TVMBEG/TVMEND abgrenzen |
| G-5 | BOXZ | PICTURE/ZOOM | Zoom durch Aufziehen eines Rechtecks | O | vom programmierbaren BOX unterscheiden |
| G-5 | B→PV | TVM | Überträgt Restschuld nach PV | O | aus AMORT-Programmkontext abgrenzen |
| G-5 | CALC | Eingabeformulare | Zwischenrechnung mit temporärem Stackzugriff | O | kein User-RPL-Befehl |
| G-5 | CANCL | Eingabeformulare | Bricht Formulareingabe ab | O | mit ON/CANCEL-Taste vergleichen |
| G-5 | ↩CASE | PRG/BRCH | Fügt CASE-Programmgerüst ein | O | Programmstruktur-Eingabehilfe |
| G-5 | ↪CASE | PRG/BRCH | Fügt Variante des CASE-Programmgerüsts ein | O | Programmstruktur-Eingabehilfe |
| G-6 | ✓CHK | Eingabeformulare | Aktiviert/deaktiviert Kontrollkästchen | O | Dialogzustand |
| G-6 | CHOOS | Eingabeformulare | Öffnet Werteauswahlliste für Eingabefeld | O | nicht CHOOSE-Befehl |
| G-6 | CIRCL | PICTURE/EDIT | Zeichnet Kreis vom markierten Mittelpunkt zum Cursor | O | nicht ARC |
| G-7 | CLK | MODES/MISC | Schaltet Uhranzeige um | O | nicht CLKADJ |
| G-7 | CNCT | PLOT/FLAG | Verbindet beziehungsweise trennt aufeinanderfolgende Plotpunkte | O | Plotflag-Bedienung |
| G-8 | CNTR | PICTURE/ZOOM | Zentriert Grafik auf Cursor | O | nicht CENTR |
| G-8 | +COL | MatrixWriter | Fügt eine neue Spalte in der Matrix hinzu | O | nicht COL+ User-RPL |
| G-8 | −COL | MatrixWriter | Löscht die aktuelle Matrixspalte | O | nicht COL− User-RPL |
| G-8 | COLCT (EQW) | EquationWriter/RULES | Fasst markierten Teilausdruck zusammen | O | von COLCT Programm unterscheiden |
| G-8 | COLCT (SYMBOLIC) | SYMBOLIC | Fasst Ausdruck im Eingabefeld zusammen | O | abweichender Kontext |
| G-9 | COPY | MEMORY | Kopiert markiertes Objekt im Browser | O | UI-Aktion |
| G-10 | ←D | EquationWriter/RULES | Distributivgesetz nach links | O | UI-Aktion |
| G-10 | ↪←D | EquationWriter/RULES | Mehrfache Distribution nach links | O | UI-Aktion |
| G-10 | D→ | EquationWriter/RULES | Distributivgesetz nach rechts | O | UI-Aktion |
| G-10 | ↪D→ | EquationWriter/RULES | Mehrfache Distribution nach rechts | O | UI-Aktion |
| G-11 | DBUG | PRG/RUN | Debugging vor erster Anweisung starten | O | nicht als RPL-Opcode |
| G-11 | →DEF | EquationWriter/RULES | Trigonometrische/hyperbolische Funktionen in Exponential-/Logarithmenform umformen | O | UI-Aktion |
| G-12 | DNEG | EquationWriter/RULES | Doppelte Negation auflösen | O | UI-Aktion |
| G-12 | ↩DO | PRG/BRCH | Schleifen-Programmgerüst einfügen | O | nicht DO als programmierbares Token |
| G-13 | DOT+ | PICTURE/EDIT | Setzt beim Bewegen des Cursors Pixel | O | UI-Aktion |
| G-13 | DOT− | PICTURE/EDIT | Löscht beim Bewegen des Cursors Pixel | O | UI-Aktion |
| G-13 | DRAW (Dialog) | PLOT | Zeichnet den im Eingabedialog gewählten Plot | O | von DRAW RPL getrennt |
| G-14 | DRPN | STACK/BROWSER | Entfernt Objekte ab Cursorposition abwärts | O | von DROPN unterscheiden |
| G-14 | DUPN (Stackbrowser) | STACK/BROWSER | Kopiert Stackobjekte im markierten Abschnitt | O | von DUPN RPL unterscheiden |
| G-15 | EEX | Zahleneingabe | Beginnt Exponenteneingabe / springt in Exponentenfeld | O | Kontextzustand |
| G-16 | ERASE | PLOT | Löscht aktuelles PICT-Objekt | O | Ergebnis/Seitenwirkung beachten |
| G-16 | EXIT | EquationWriter | Verlässt Optionsansicht | O | Dialogaktion |
| G-16 | EXPND | SYMBOLIC | Expandiert Ausdruck im aktiven Formularfeld | O | nicht EXPAN Befehl |

### C.1 Quellenspezifische mögliche Lücken und Mehrdeutigkeiten

| Befund | Original-Quelle | Differenz und Prüfbedarf |
| --- | --- | --- |
| `CST` wird im Operation Index G-9 als eigener Eintrag geführt, fehlt aber als isolierter ROM-Namensschlüssel aus R | U G-9, S. 30-1 | Prüfen, ob User-Variable/programmierbare Tastaturhilfe, UI-Eintrag oder separates ROM-Kommando |
| `ΣDAT` erscheint im Operation Index G-10, ist im ROM-JSON nicht als eigener Name geführt | U G-10, S. 21-1 | Reservierte Systemvariable und deren über Menüs zugängliche Bedienung als eigene Typfamilie behandeln |
| `CLUSR` erscheint als Text im Operation Index G-7, zusätzlich `CLVAR`; ROM-Namensliste führt `CLVAR` | U G-7 | Nicht blind als neuen Befehl übernehmen: mögliche Scan-/Index-/ROM-Abweichung, Quelle A untersuchen |
| `COLΣ` | U G-8 / H-4 | **Katalogfehler:** Setzt die unabhängige und abhängige Statistikspalte; berechnet nicht die Spaltensumme |
| `TRACE` | AUR und U G | Programmierbares `TRACE` = Matrixspur; Plot-/PICTURE-Trace = interaktive Kurvenverfolgung, getrennte IDs |
| `AMORT` | U G-2/G-3 | Im Index als interaktive Operation **und** als programmierbarer Befehl gelistet; Kontexte getrennt nachweisen |
| `COLCT` | U G-8 | In symbolischem RPL, EquationWriter und SYMBOLIC-Eingabefeld separat vorhanden; gleicher Name, unterschiedliche Bedienung |
| `BOX`, `DUPN`, `DRAW` | U G-4/G-13/G-14 | Programmierbare und interaktive Varianten im Operation Index ausdrücklich getrennt |
| `BUF LEN` / `BUFLEN` | U G-5 | Druckweise / ROM-Schlüssel als möglichen Alias erfassen, nicht doppelt zählen |
| `CLS` / `CLΣ` | U G-6 | Zeichenerkennung mit griechischem Sigma und Modellstand anhand AUR prüfen, statt als zwei verschiedene Befehle zu zählen |

## C.2 Weiterer quellengebundener Abgleich aus dem Operation Index (G-17 bis G-58)

**Status:** Gezielt geprüfte **einzelne** Einträge, keine lückenlose Abzeichnung der 58 Appendix-G-Seiten. Die Seitenkennungen sind gedruckte G-Seiten; die Beschreibungen sind selbst verfasst. Gleich lautende Einträge mit unterschiedlichen Bedienkontexten erscheinen mehrfach.

| G-Seite | Operation | Kontext | Wirkung / Abgrenzung |
| --- | --- | --- | --- |
| G-17 | FM | MODES/Beep/Uhr/Dezimalzeichen | Schaltet Punkt/Komma für Dezimalzahlen um |
| G-18 | F(X) | PICTURE/FCN | Wertet die aktuelle Plotfunktion an Cursorposition aus |
| G-18 | F′ | PICTURE/FCN | Zeigt die Ableitung am Cursor |
| G-18 | ↩ FOR | PRG/BRCH | Fügt FOR/NEXT-Programmgerüst ein |
| G-18 | ↪ FOR | PRG/BRCH | Fügt FOR/STEP-Programmgerüst ein |
| G-19 | GO↓ | MatrixWriter | Cursorbewegung in Richtung nächster Matrixzeile konfigurieren |
| G-19 | GO→ | MatrixWriter | Cursorbewegung in Richtung nächster Matrixspalte konfigurieren |
| G-20 | HZIN | PICTURE/ZOOM | Horizontale Vergrößerung |
| G-20 | HZOUT | PICTURE/ZOOM | Horizontale Verkleinerung |
| G-20 | ↩ IF | PRG/BRCH | IF-Struktur-Gerüst eingeben |
| G-21 | INFO | PLOT/EQ LIB | Anzeigen von Hilfe/Information im aktuellen Dialog |
| G-21 | INFO? | PLOT | Infoanzeige umschalten |
| G-21 | INS | Texteditor | Eingabemodus Einfügen/Umschreiben |
| G-22 | ISECT | PICTURE/FCN | Schnittpunkt zweier gezeichneter Kurven |
| G-22 | KEEP | MEMORY/Browser | Markierte Selektion/Objekt beibehalten |
| G-23 | LEVEL | STACK/Browser | Stackebene gezielt auswählen |
| G-24 | LINE | PICTURE/EDIT | Interaktiv Linie zwischen Markierung und Cursor zeichnen |
| G-25 | L* | EquationWriter/RULES | Linke distributive Umformung |
| G-26 | ←M | EquationWriter/RULES | Multiplikativen Term nach links verschieben |
| G-26 | M→ | EquationWriter/RULES | Multiplikativen Term nach rechts verschieben |
| G-26 | MARK | PICTURE/EDIT | Markierung im Bildeditor setzen |
| G-26 | MENU | PICTURE | Grafik-Softkeys ein-/ausblenden |
| G-27 | MOVE | MEMORY | Markierte Variablen in anderes Verzeichnis verschieben |
| G-28 | NEW | MEMORY | Neue benannte Variable/Objekt erstellen |
| G-28 | NEW | TIME/Alarmbrowser | Neuen Alarm anlegen |
| G-28 | NEXT | PRG/RUN/Debugger | Nächste auszuführende RPL-Struktur ansehen |
| G-29 | NXEQ | PICTURE/FCN | Zur nächsten Gleichung der EQ-Liste wechseln |
| G-30 | OK | Dialog | Formular bestätigen bzw. Hauptaktion ausführen |
| G-30 | OPTS | PLOT | Plotoptionen des aktuellen Plottyps öffnen |
| G-31 | PICK | STACK/Browser | Markiertes Stackobjekt an Level 1 kopieren |
| G-31 | PICT→ | PICTURE/EDIT | Aktuelles Bildobjekt auf Stack legen |
| G-32 | PRED | STAT/FIT | Wert mittels aktuellem Regressionsmodell vorhersagen |
| G-32 | PRINT | I/O | Objekt über interaktiven Druckdialog ausgeben |
| G-33 | PURG | MEMORY/TIME/EQ LIB | Markierte Daten/Alarme/Variablen im Dialog löschen |
| G-35 | RCL | MEMORY/Browser | Markiertes Objekt auf Stack zurückrufen |
| G-36 | RECV | I/O/Transfer | Interaktiven Empfang vorbereiten |
| G-37 | REPL | PICTURE/EDIT | Grafikbereich durch Grafikobjekt ersetzen |
| G-37 | REPL | EquationWriter | Symbolisches Substitutionsmuster anwenden |
| G-37 | RESET | PLOT | Aktuelle Formularfelder/Plotparameter zurücksetzen |
| G-38 | ROLL | STACK/Browser | Stackobjekte im Dialog rollen |
| G-39 | ROOT | PICTURE/FCN | Nullstelle des aktuellen Funktionsgraphen suchen |
| G-39 | +ROW | MatrixWriter | Matrixzeile hinzufügen |
| G-39 | −ROW | MatrixWriter | Matrixzeile löschen |
| G-41 | SEND | I/O/Transfer | Objekt per eingestelltem Verfahren aus Dialog senden |
| G-41 | SHADE | PICTURE/FCN | Fläche zwischen Kurve und Achse/zweiter Kurve schraffieren |
| G-42 | SIMU | PLOT/FLAG | Kurven simultan oder nacheinander darstellen |
| G-42 | SLOPE | PICTURE/FCN | Kurvensteigung an Cursor bestimmen |
| G-43 | SST | PRG/RUN/Debugger | Einzelschritt im angehaltenen Programm |
| G-43 | SST↓ | PRG/RUN/Debugger | Einzelschritt auch in Unterprogramme |
| G-44 | ↩ START | PRG/BRCH | START/NEXT-Gerüst einfügen |
| G-44 | ↪ START | PRG/BRCH | START/STEP-Gerüst einfügen |
| G-44 | STEP | SYMBOLIC/Differentiation | Symbolischen Einzelschritt der Ableitung ausführen |
| G-44 | ↑STK | MatrixWriter/EquationWriter | Interaktiven Stack aus Editor öffnen |
| G-44 | →STK | MatrixWriter | Markiertes Matrixelement auf Stack kopieren |
| G-44 | →STK | EQ LIB | Ausgewählte Gleichungen auf Stack kopieren |
| G-45 | SUB | PICTURE/EDIT | Ausgewählten Teil des Bildspeichers auf Stack kopieren |
| G-46 | SUB | EquationWriter | Unterausdruck auf Stack kopieren |
| G-47 | SYM | MODES/MISC | Numerische/symbolische Auswertung von Konstanten schalten |
| G-47 | ←T | EquationWriter/RULES | Term nach links verschieben |
| G-47 | ↪←T | EquationWriter/RULES | Linksumformung wiederholen |
| G-47 | T→ | EquationWriter/RULES | Term nach rechts verschieben |
| G-47 | ↪T→ | EquationWriter/RULES | Rechtsumformung wiederholen |
| G-48 | TANL | PICTURE/FCN | Tangente am Cursor zeichnen und Gleichung ausgeben |
| G-48 | TLINE | PICTURE/EDIT | Pixel entlang einer markierten Linie toggeln |
| G-49 | TRACE | PICTURE | Kurvenverfolgung umschalten; verschieden von Matrix-TRACE |
| G-49 | TRG* | EquationWriter/RULES | Trigonometrische/hyperbolische Summenformeln expandieren |
| G-49 | →TRG | EquationWriter/RULES | Exponentialausdrücke in trigonometrische umschreiben |
| G-50 | TYPES | Eingabeformular | Erlaubte Objekttypen des aktuellen Eingabefelds anzeigen |
| G-51 | VEC | MatrixWriter | Vektor-/Array-Eingabemodus wechseln |
| G-51 | VIEW | Stack/PICTURE | Stackobjekt, Menüinformation oder Plot anzeigen |
| G-51 | VZIN | PICTURE/ZOOM | Vertikal hineinzoomen |
| G-51 | VZOUT | PICTURE/ZOOM | Vertikal herauszoomen |
| G-52 | ↩ WHILE | PRG/BRCH | WHILE/REPEAT/END-Gerüst einfügen |
| G-52 | WID→ | MatrixWriter | Breite der Matrixspalten vergrößern |
| G-52 | ←WID | MatrixWriter | Breite der Matrixspalten verkleinern |
| G-53 | (X,Y) | PICTURE | Aktuelle Cursorposition an-/ausblenden |
| G-53 | X,Y→ | PICTURE | Cursorposition als komplexen Wert auf Stack legen |
| G-54 | ZAUTO | PICTURE/ZOOM | Grafik automatisch skalieren |
| G-54 | ZDECI | PICTURE/ZOOM | Horizontale Dezimalskalierung |
| G-54 | ZDFLT | PICTURE/ZOOM | Standard-Plotparameter wählen |
| G-54 | ZFACT | PICTURE/ZOOM | Zoomfaktoren-Dialog öffnen |
| G-54 | ZIN | PICTURE/ZOOM | Hineinzoomen |
| G-54 | ZINTG | PICTURE/ZOOM | Horizontale Ganzzahls-Skalierung |
| G-54 | ZLAST | PICTURE/ZOOM | Vorherigen Zoombereich wiederherstellen |
| G-54 | ZOOM | PICTURE/ZOOM | Mit Markierungsrechteck zoomen |
| G-54 | ZOUT | PICTURE/ZOOM | Herauszoomen |
| G-54 | ZSQR | PICTURE/ZOOM | Seitenverhältnis winkelrichtig einstellen |
| G-55 | ZTRIG | PICTURE/ZOOM | Trigonometrisch sinnvoll skalieren |
| G-55 | +/− | PICTURE | Cursordarstellung umschalten |
| G-55 | +1−1 | EquationWriter/RULES | Neutrale Addition/Subtraktion mit 1 |
| G-55 | −() | EquationWriter/RULES | Doppelte Negation verteilen |
| G-55 | *1 | EquationWriter/RULES | Multiplikation mit 1 |
| G-55 | /1 | EquationWriter/RULES | Division durch 1 |
| G-56 | ^1 | EquationWriter/RULES | Potenzierung mit 1 |
| G-57 | 1/() | EquationWriter/RULES | Inversion zweifach verteilen |
| G-57 | (()) | EquationWriter/RULES | Benachbarte Ausdrücke klammern |
| G-57 | (← | EquationWriter/RULES | Linken Unterausdruck erweitern |
| G-57 | ↪(← | EquationWriter/RULES | Linken Unterausdruck wiederholt erweitern |
| G-57 | →() | EquationWriter/RULES | Präfixfunktion distributiv anwenden |
| G-57 | →) | EquationWriter/RULES | Rechten Unterausdruck erweitern |
| G-57 | ↪→) | EquationWriter/RULES | Rechten Unterausdruck wiederholt erweitern |
| G-58 | ←→ | EquationWriter/RULES | Reihenfolge der Argumente vertauschen |

**Beleg:** [Hewlett-Packard, HP 48G Series User's Guide, Appendix G (G-1–G-58)](https://www.hp.com/ctg/Manual/c00442262.pdf), Einzelseiten wie in Tabelle angegeben. Diese Tabelle erweitert Abschnitt C.1 und ist kein über alle Operationen abgeschlossenes G-Inventar.

## C.3 Originalhandbuch-Einträge, die der 517er-ROM-Namensindex nicht direkt enthält

**Das Fehlen eines Namens im ROM-Index bedeutet nicht automatisch, dass eine Funktion fehlt.** Einige Namen sind reservierte Variablen, Aliase oder Menütasten; andere wie `GRAPH` benötigen eine echte Gegenprüfung am AUR. Die Klassifikation des Handbuchs wird hier als solche genannt, nicht mit einer eigenständigen ROM-Kennung verwechselt.

| Name | Fundstelle | Handbuch-Klasse | Bedeutung | Zu klären |
| --- | --- | --- | --- | --- |
| `GRAPH` | G-18/G-19; AUR | C | Programmierbarer Wechsel in die Grafikansicht; in 517er ROM-Namensliste nicht enthalten | Wahrscheinlicher echter fehlender Namenszugang; AUR/ROM-Aufruf prüfen |
| `LAST` | G-23 | C | Im Guide benannter Abruf der letzten Argumente | Alias zu LASTARG prüfen |
| `CST` | G-9 | C laut Index | Reservierte Variable für benutzerdefinierte Menüs | Kein eigener XLIB-Befehl; Variable/Programmzugriff separat |
| `ΣDAT` | G-10 | C laut Index | Statistischer Datencontainer | Reservierte Variable, nicht mit Σ-Kommandos doppelt zählen |
| `IOPAR` | G-22 | C laut Index | Schnittstellen-Parameterobjekt | Reservierte Variable; Zugriff ggf. im Menü und über Namen |
| `PPAR` | G-31 | C laut Index | Plot-Parameterobjekt | Reservierte Variable, kein automatischer ROM-Befehl |
| `PRTPAR` | G-32 | C laut Index | Drucker-Parameterobjekt | Reservierte Variable, kein automatischer ROM-Befehl |
| `FV` | G-17 | C laut Index | Future-Value-Solvervariable | Finanzfunktion vorhanden; kein zusätzlicher Scientific-V1-Scope |
| `PMT` | G-32 | C laut Index | Payment-Solvervariable | Finanzfunktion vorhanden; kein zusätzlicher Scientific-V1-Scope |
| `PV` | G-33 | C laut Index | Present-Value-Solvervariable | Finanzfunktion vorhanden; kein zusätzlicher Scientific-V1-Scope |
| `PYR` | G-33 | C laut Index | Payments-per-year-Solvervariable | Finanzfunktion vorhanden; kein zusätzlicher Scientific-V1-Scope |
| `VPAR` | G-51 | C laut Index | 3D-Plot-Parameterobjekt | Reservierte Variable, nicht mit WVOL etc verwechseln |
| `SCLS` | G-41 | C laut Index | Autoskalierung der Statistik-Daten für Scatterplots | Fehlender Name gegenüber ROM-Satz; AUR- und Klassenprüfung nötig |
| `EDIT` | G-14; AUR-Hinweis | O/C prüfen | Interaktive Objektbearbeitung | Nicht vorschnell als eigener User-RPL-Befehl zählen |
| `SOLVE` | G-42 | O | Interaktiver Solver-Softkey | Kein selbständiger ROM-Befehl nur weil UI-Name |
| `DBUG` | G-11; AUR | O | Interaktiven Debugger starten | Nichtprogrammierbar trotz AUR-Beschreibung |

**Provenienz:** [Original Operation Index G-1 bis G-58](https://www.hp.com/ctg/Manual/c00442262.pdf); für `GRAPH` zusätzlicher [AUR Command Reference](https://literature.hpcalc.org/community/hp48g-aur-en.pdf). Die im Handbuch als `C` markierten Bedienungen reservierter Variablennamen müssen noch als **Name/RCL/Menü-Operation** statt als zusätzliche maschinennahe XLIB-Befehle klassifiziert werden. Keine neuen ROM-Kommandonummern erfinden.

## D. Vollständige technische Zuordnung der ROM-Namenseinträge

**Status-Legende:** `UNVERIFIED` = ROM-Name erfasst, aber keine unabhängige AUR- und G-Operation-Index-Einzelabnahme. Die Zahl nach `AUR` bzw. `UG` ist eine automatische **PDF-Fundseitenposition aus dem Sekundärindex**, nicht eine gedruckte Buchseite und nicht extern verifiziert. `—` heißt **kein Seitenhinweis in dieser Datenquelle**, nicht »nicht im Handbuch«.

| ROM-Name | ROM-Kennung | AUR-Fundstellenhinweis (PDF-Seite) | UG-Fundstellenhinweis (PDF-Seite) | Status |
| --- | --- | ---: | ---: | --- |
| `_` | `2:267` | — | — | UNVERIFIED |
| `-` | `2:70` | — | 577 | UNVERIFIED |
| `!` | `2:99` | 576 | — | UNVERIFIED |
| `'` | `1792:20, 1792:21` | — | — | UNVERIFIED |
| `«` | `1792:18` | — | — | UNVERIFIED |
| `»` | `1792:17, 1792:19` | — | — | UNVERIFIED |
| `*` | `2:71` | 564 | — | UNVERIFIED |
| `*H` | `2:189` | — | — | UNVERIFIED |
| `*W` | `2:190` | — | 569 | UNVERIFIED |
| `/` | `2:72` | 565 | — | UNVERIFIED |
| `%` | `2:124` | 580 | — | UNVERIFIED |
| `%CH` | `2:126` | 211 | — | UNVERIFIED |
| `%T` | `2:125` | 503 | — | UNVERIFIED |
| `^` | `2:73` | — | — | UNVERIFIED |
| `→` | `1792:4, 1792:16` | — | 577 | UNVERIFIED |
| `→ARRY` | `2:170` | 184 | — | UNVERIFIED |
| `→COL` | `171:67` | 218 | — | UNVERIFIED |
| `→DATE` | `2:22` | 237 | 543 | UNVERIFIED |
| `→DIAG` | `171:69` | 249 | — | UNVERIFIED |
| `→GROB` | `2:215` | 297 | 117 | UNVERIFIED |
| `→HMS` | `2:114` | 306 | — | UNVERIFIED |
| `→LCD` | `2:214` | 328 | 118 | UNVERIFIED |
| `→LIST` | `2:152` | 333 | 44 | UNVERIFIED |
| `→NUM` | `2:53` | 371 | — | UNVERIFIED |
| `→Q` | `2:263` | 415 | — | UNVERIFIED |
| `→Qπ` | `2:264` | — | — | UNVERIFIED |
| `→ROW` | `171:65` | 446 | — | UNVERIFIED |
| `→STR` | `2:162` | 498 | — | UNVERIFIED |
| `→TAG` | `2:383` | 505 | — | UNVERIFIED |
| `→TIME` | `2:23` | 511 | — | UNVERIFIED |
| `→UNIT` | `2:13` | 526 | 132 | UNVERIFIED |
| `→V2` | `2:181` | 533 | — | UNVERIFIED |
| `→V3` | `2:182` | 534 | — | UNVERIFIED |
| `↑MATCH` | `2:265` | — | — | UNVERIFIED |
| `↓MATCH` | `2:266` | — | — | UNVERIFIED |
| `∂` | `2:247, 2:248` | — | — | UNVERIFIED |
| `+` | `2:68, 2:69` | 560 | — | UNVERIFIED |
| `<` | `2:235` | 567 | 574 | UNVERIFIED |
| `=` | `2:59` | — | 136 | UNVERIFIED |
| `≠` | `2:234` | — | — | UNVERIFIED |
| `==` | `2:233` | — | 576 | UNVERIFIED |
| `>` | `2:236` | 570 | 575 | UNVERIFIED |
| `\|` | `2:255, 2:256` | — | 257 | UNVERIFIED |
| `√` | `2:79` | — | — | UNVERIFIED |
| `∫` | `2:252, 2:253` | — | — | UNVERIFIED |
| `≤` | `2:237` | — | — | UNVERIFIED |
| `≥` | `2:238` | — | — | UNVERIFIED |
| `ABS` | `2:61` | 169 | — | UNVERIFIED |
| `ACK` | `2:21` | 170 | — | UNVERIFIED |
| `ACKALL` | `2:20` | 170 | — | UNVERIFIED |
| `ACOS` | `2:88` | 166 | — | UNVERIFIED |
| `ACOSH` | `2:91` | 173 | — | UNVERIFIED |
| `ADD` | `171:108` | 175 | — | UNVERIFIED |
| `ALOG` | `2:96` | 176 | — | UNVERIFIED |
| `AMORT` | `171:89` | 176 | — | UNVERIFIED |
| `AND` | `2:229` | 177 | — | UNVERIFIED |
| `ANIMATE` | `171:24` | 178 | — | UNVERIFIED |
| `APPLY` | `2:258, 2:259` | 179 | — | UNVERIFIED |
| `ARC` | `2:216` | 181 | — | UNVERIFIED |
| `ARCHIVE` | `2:352` | 182 | — | UNVERIFIED |
| `ARG` | `2:77` | 183 | — | UNVERIFIED |
| `ARRY→` | `2:171` | 183 | — | UNVERIFIED |
| `ASIN` | `2:87` | 185 | — | UNVERIFIED |
| `ASINH` | `2:90` | 187 | — | UNVERIFIED |
| `ASN` | `2:379` | 188 | — | UNVERIFIED |
| `ASR` | `2:0` | 189 | — | UNVERIFIED |
| `ATAN` | `2:89` | 190 | — | UNVERIFIED |
| `ATANH` | `2:92` | 192 | — | UNVERIFIED |
| `ATICK` | `171:16` | 194 | — | UNVERIFIED |
| `ATTACH` | `2:357` | 195 | — | UNVERIFIED |
| `AUTO` | `2:192` | 196 | — | UNVERIFIED |
| `AXES` | `2:186` | 197 | — | UNVERIFIED |
| `B→R` | `2:10` | 206 | — | UNVERIFIED |
| `BAR` | `2:227` | 198 | — | UNVERIFIED |
| `BARPLOT` | `2:316` | 200 | — | UNVERIFIED |
| `BAUD` | `2:370` | 200 | — | UNVERIFIED |
| `BEEP` | `2:52` | 201 | — | UNVERIFIED |
| `BESTFIT` | `2:323` | 201 | — | UNVERIFIED |
| `BIN` | `2:144` | 202 | — | UNVERIFIED |
| `BINS` | `2:315` | 202 | — | UNVERIFIED |
| `BLANK` | `2:209` | 203 | — | UNVERIFIED |
| `BOX` | `2:208` | 204 | — | UNVERIFIED |
| `BUFLEN` | `2:374` | 204 | — | UNVERIFIED |
| `BYTES` | `2:38` | 205 | — | UNVERIFIED |
| `C→PX` | `2:199` | 235 | 117 | UNVERIFIED |
| `C→R` | `2:159` | 235 | — | UNVERIFIED |
| `CASE` | `1792:25` | 206 | — | UNVERIFIED |
| `CEIL` | `2:104` | 208 | — | UNVERIFIED |
| `CENTR` | `2:187` | 208 | — | UNVERIFIED |
| `CF` | `2:132` | 209 | — | UNVERIFIED |
| `CHOOSE` | `171:92` | 210 | — | UNVERIFIED |
| `CHR` | `2:165` | 212 | — | UNVERIFIED |
| `CKSM` | `2:369` | 213 | — | UNVERIFIED |
| `CLEAR` | `2:282` | 214 | — | UNVERIFIED |
| `CLKADJ` | `2:24` | 214 | — | UNVERIFIED |
| `CLLCD` | `2:56` | 215 | — | UNVERIFIED |
| `CLOSEIO` | `2:362` | 215 | — | UNVERIFIED |
| `CLTEACH` | `171:18` | 216 | — | UNVERIFIED |
| `CLVAR` | `2:346` | 217 | — | UNVERIFIED |
| `CLΣ` | `2:284` | — | — | UNVERIFIED |
| `CNRM` | `2:119` | 217 | — | UNVERIFIED |
| `COL-` | `171:73` | 219 | — | UNVERIFIED |
| `COL→` | `171:68` | 220 | — | UNVERIFIED |
| `COL+` | `171:74` | 218 | — | UNVERIFIED |
| `COLCT` | `2:333` | 220 | — | UNVERIFIED |
| `COLΣ` | `2:312` | — | — | UNVERIFIED |
| `COMB` | `2:129` | 222 | — | UNVERIFIED |
| `CON` | `2:173` | 223 | — | UNVERIFIED |
| `COND` | `171:49` | 224 | — | UNVERIFIED |
| `CONIC` | `2:221` | 225 | — | UNVERIFIED |
| `CONJ` | `2:62` | 226 | — | UNVERIFIED |
| `CONLIB` | `171:32` | 227 | — | UNVERIFIED |
| `CONST` | `171:33` | 227 | — | UNVERIFIED |
| `CONT` | `2:58` | 228 | — | UNVERIFIED |
| `CONVERT` | `2:11` | 229 | — | UNVERIFIED |
| `CORR` | `2:289` | 229 | — | UNVERIFIED |
| `COS` | `2:82` | — | — | UNVERIFIED |
| `COSH` | `2:85` | 231 | — | UNVERIFIED |
| `COV` | `2:290` | — | — | UNVERIFIED |
| `CR` | `2:243` | 232 | — | UNVERIFIED |
| `CRDIR` | `2:32` | 233 | — | UNVERIFIED |
| `CROSS` | `2:122` | 233 | 160 | UNVERIFIED |
| `CSWP` | `171:76` | — | — | UNVERIFIED |
| `CYLIN` | `171:20` | 234 | — | UNVERIFIED |
| `D→R` | `2:112` | 263 | — | UNVERIFIED |
| `DARCY` | `171:120` | 236 | — | UNVERIFIED |
| `DATE` | `2:17` | 237 | — | UNVERIFIED |
| `DATE+` | `2:31` | 238 | 194 | UNVERIFIED |
| `dB` | `171:128` | — | — | UNVERIFIED |
| `DDAYS` | `2:30` | 239 | 194 | UNVERIFIED |
| `DEC` | `2:145` | 239 | 188 | UNVERIFIED |
| `DECR` | `2:332` | 240 | 543 | UNVERIFIED |
| `DEFINE` | `2:342` | 241 | 71 | UNVERIFIED |
| `DEG` | `2:135` | 242 | — | UNVERIFIED |
| `DELALARM` | `2:28` | 242 | — | UNVERIFIED |
| `DELAY` | `2:245` | 243 | 372 | UNVERIFIED |
| `DELKEYS` | `2:381` | 244 | — | UNVERIFIED |
| `DEPND` | `2:196` | 245 | — | UNVERIFIED |
| `DEPTH` | `2:276` | 246 | — | UNVERIFIED |
| `DET` | `2:120` | 246 | — | UNVERIFIED |
| `DETACH` | `2:358` | 248 | — | UNVERIFIED |
| `DIAG→` | `171:70` | 248 | — | UNVERIFIED |
| `DIFFEQ` | `171:14` | 250 | — | UNVERIFIED |
| `DIR` | `1792:27` | — | — | UNVERIFIED |
| `DISP` | `2:50` | 252 | — | UNVERIFIED |
| `DO` | `1792:7` | 253 | 420 | UNVERIFIED |
| `DOERR` | `2:42` | 254 | — | UNVERIFIED |
| `DOLIST` | `171:107` | 255 | 202 | UNVERIFIED |
| `DOSUBS` | `171:99` | 256 | — | UNVERIFIED |
| `DOT` | `2:121` | 258 | 160 | UNVERIFIED |
| `DRAW` | `2:191` | 258 | — | UNVERIFIED |
| `DRAX` | `2:193` | 259 | — | UNVERIFIED |
| `DROP` | `2:272` | 259 | 41 | UNVERIFIED |
| `DROP2` | `2:273` | 260 | — | UNVERIFIED |
| `DROPN` | `2:277` | 260 | — | UNVERIFIED |
| `DTAG` | `2:384` | 261 | — | UNVERIFIED |
| `DUP` | `2:269` | 261 | — | UNVERIFIED |
| `DUP2` | `2:270` | 262 | — | UNVERIFIED |
| `DUPN` | `2:278` | 262 | 44 | UNVERIFIED |
| `e` | `2:66` | 263 | — | UNVERIFIED |
| `EGV` | `171:55` | 264 | — | UNVERIFIED |
| `EGVL` | `171:56` | 265 | — | UNVERIFIED |
| `ELSE` | `1792:2` | 265 | — | UNVERIFIED |
| `END` | `1792:3, 1792:22, 1792:23` | 266 | 416 | UNVERIFIED |
| `ENDSUB` | `171:102` | 266 | 203 | UNVERIFIED |
| `ENG` | `2:140` | 267 | — | UNVERIFIED |
| `EQ→` | `2:168` | 268 | 544 | UNVERIFIED |
| `EQNLIB` | `171:34` | 268 | — | UNVERIFIED |
| `ERASE` | `2:197` | 269 | — | UNVERIFIED |
| `ERR0` | `2:43` | — | — | UNVERIFIED |
| `ERRM` | `2:45` | 269 | 544 | UNVERIFIED |
| `ERRN` | `2:44` | 270 | 545 | UNVERIFIED |
| `EVAL` | `2:46` | 271 | — | UNVERIFIED |
| `EXP` | `2:93` | 272 | — | UNVERIFIED |
| `EXPAN` | `2:334` | 273 | 258 | UNVERIFIED |
| `EXPFIT` | `2:321` | 274 | — | UNVERIFIED |
| `EXPM` | `2:98` | 274 | — | UNVERIFIED |
| `EYEPT` | `171:5` | 275 | 545 | UNVERIFIED |
| `F0λ` | `171:121` | — | — | UNVERIFIED |
| `FACT` | `2:100` | 276 | — | UNVERIFIED |
| `FANNING` | `171:119` | 277 | — | UNVERIFIED |
| `FC?` | `2:134` | 278 | 56 | UNVERIFIED |
| `FC?C` | `2:143` | 278 | 56 | UNVERIFIED |
| `FFT` | `171:37` | 279 | 164 | UNVERIFIED |
| `FINDALARM` | `2:27` | 280 | — | UNVERIFIED |
| `FINISH` | `2:367` | 281 | 379 | UNVERIFIED |
| `FIX` | `2:138` | 281 | — | UNVERIFIED |
| `FLOOR` | `2:103` | 282 | — | UNVERIFIED |
| `FOR` | `1792:10` | 283 | 419 | UNVERIFIED |
| `FP` | `2:102` | 285 | — | UNVERIFIED |
| `FREE` | `2:355` | 285 | — | UNVERIFIED |
| `FREE1` | `171:23` | 286 | 404 | UNVERIFIED |
| `FREEZE` | `2:51` | 287 | — | UNVERIFIED |
| `FS?` | `2:133` | 288 | 56 | UNVERIFIED |
| `FS?C` | `2:142` | 289 | — | UNVERIFIED |
| `FUNCTION` | `2:220` | 289 | 301 | UNVERIFIED |
| `GET` | `2:178` | 291 | 171 | UNVERIFIED |
| `GETI` | `2:179` | 293 | 205 | UNVERIFIED |
| `gmol` | `171:125` | — | — | UNVERIFIED |
| `GOR` | `2:211` | 294 | 117 | UNVERIFIED |
| `GRAD` | `2:137` | 295 | — | UNVERIFIED |
| `GRIDMAP` | `171:10` | 296 | 334 | UNVERIFIED |
| `GXOR` | `2:212` | 298 | 117 | UNVERIFIED |
| `HALT` | `1792:14` | 300 | 415 | UNVERIFIED |
| `HEAD` | `171:96` | 300 | — | UNVERIFIED |
| `HEX` | `2:146` | 301 | 187 | UNVERIFIED |
| `HISTOGRAM` | `2:226` | 301 | 318 | UNVERIFIED |
| `HISTPLOT` | `2:317` | 303 | — | UNVERIFIED |
| `HMS-` | `2:117` | — | — | UNVERIFIED |
| `HMS→` | `2:115` | 304 | — | UNVERIFIED |
| `HMS+` | `2:116` | 303 | — | UNVERIFIED |
| `HOME` | `2:34` | 306 | 70 | UNVERIFIED |
| `i` | `2:67` | 307 | 136 | UNVERIFIED |
| `IDN` | `2:174` | 307 | — | UNVERIFIED |
| `IF` | `1792:0` | 308 | 416 | UNVERIFIED |
| `IFERR` | `1792:13` | 310 | 421 | UNVERIFIED |
| `IFFT` | `171:38` | 311 | 164 | UNVERIFIED |
| `IFT` | `2:48` | 312 | 547 | UNVERIFIED |
| `IFTE` | `2:47` | 313 | 547 | UNVERIFIED |
| `IM` | `2:155` | 314 | — | UNVERIFIED |
| `INCR` | `2:331` | 314 | 547 | UNVERIFIED |
| `INDEP` | `2:183` | 315 | 548 | UNVERIFIED |
| `INFORM` | `171:90` | 316 | 86 | UNVERIFIED |
| `INPUT` | `2:378` | 318 | — | UNVERIFIED |
| `INV` | `2:76` | 320 | — | UNVERIFIED |
| `IP` | `2:101` | — | — | UNVERIFIED |
| `ISOL` | `2:336` | 322 | 256 | UNVERIFIED |
| `KERRM` | `2:373` | 323 | 548 | UNVERIFIED |
| `KEY` | `2:57` | 323 | 548 | UNVERIFIED |
| `KGET` | `2:364` | 324 | — | UNVERIFIED |
| `KILL` | `2:40` | 325 | — | UNVERIFIED |
| `LABEL` | `2:201` | 326 | — | UNVERIFIED |
| `LASTARG` | `2:54` | 327 | 41 | UNVERIFIED |
| `lbmol` | `171:126` | — | — | UNVERIFIED |
| `LCD→` | `2:213` | 327 | 118 | UNVERIFIED |
| `LIBEVAL` | `171:30` | 329 | 549 | UNVERIFIED |
| `LIBS` | `2:356` | 329 | 549 | UNVERIFIED |
| `LINE` | `2:206` | 330 | 116 | UNVERIFIED |
| `LINFIT` | `2:319` | 331 | — | UNVERIFIED |
| `LININ` | `171:28` | 332 | 549 | UNVERIFIED |
| `LIST→` | `2:158` | 333 | — | UNVERIFIED |
| `LN` | `2:94` | 336 | — | UNVERIFIED |
| `LNP1` | `2:97` | 338 | — | UNVERIFIED |
| `LOG` | `2:95` | 338 | — | UNVERIFIED |
| `LOGFIT` | `2:320` | 340 | — | UNVERIFIED |
| `LQ` | `171:61` | 340 | 185 | UNVERIFIED |
| `LR` | `2:302` | 341 | 550 | UNVERIFIED |
| `LSQ` | `171:54` | 342 | 180 | UNVERIFIED |
| `LU` | `171:59` | 343 | 185 | UNVERIFIED |
| `MANT` | `2:111` | 343 | — | UNVERIFIED |
| `MAX` | `2:106` | — | — | UNVERIFIED |
| `MAXR` | `2:64` | 347 | — | UNVERIFIED |
| `MAXΣ` | `2:296` | 348 | — | UNVERIFIED |
| `MCALC` | `171:115` | 349 | — | UNVERIFIED |
| `MEAN` | `2:297` | 349 | — | UNVERIFIED |
| `MEM` | `2:344` | 350 | — | UNVERIFIED |
| `MENU` | `2:348` | 351 | — | UNVERIFIED |
| `MERGE` | `2:354` | 354 | — | UNVERIFIED |
| `MERGE1` | `171:22` | — | 404 | UNVERIFIED |
| `MIN` | `2:107` | 355 | — | UNVERIFIED |
| `MINEHUNT` | `171:117` | 356 | — | UNVERIFIED |
| `MINIT` | `171:112` | 357 | 355 | UNVERIFIED |
| `MINR` | `2:65` | 357 | 136 | UNVERIFIED |
| `MINΣ` | `2:298` | 358 | — | UNVERIFIED |
| `MITM` | `171:113` | 358 | 355 | UNVERIFIED |
| `MOD` | `2:110` | 359 | — | UNVERIFIED |
| `MROOT` | `171:116` | 359 | 552 | UNVERIFIED |
| `MSGBOX` | `171:93` | 360 | 552 | UNVERIFIED |
| `MSOLVR` | `171:36, 171:111` | 361 | — | UNVERIFIED |
| `MUSER` | `171:114` | 361 | — | UNVERIFIED |
| `NDIST` | `171:39` | 362 | — | UNVERIFIED |
| `NEG` | `2:60` | 363 | — | UNVERIFIED |
| `NEWOB` | `2:39` | 364 | 552 | UNVERIFIED |
| `NEXT` | `1792:11` | 365 | 418 | UNVERIFIED |
| `NOT` | `2:231` | 365 | — | UNVERIFIED |
| `NOVAL` | `171:91` | 367 | — | UNVERIFIED |
| `NSUB` | `171:101` | 367 | 203 | UNVERIFIED |
| `NUM` | `2:164` | 368 | 553 | UNVERIFIED |
| `NUMX` | `171:6` | 371 | 553 | UNVERIFIED |
| `NUMY` | `171:7` | 372 | 553 | UNVERIFIED |
| `NΣ` | `2:288` | 372 | — | UNVERIFIED |
| `OBJ→` | `2:169` | 373 | 554 | UNVERIFIED |
| `OCT` | `2:147` | 374 | — | UNVERIFIED |
| `OFF` | `2:41` | 375 | — | UNVERIFIED |
| `OLDPRT` | `2:239` | 375 | — | UNVERIFIED |
| `OPENIO` | `2:361` | 376 | — | UNVERIFIED |
| `OR` | `2:230` | 377 | — | UNVERIFIED |
| `ORDER` | `2:345` | 378 | 554 | UNVERIFIED |
| `OVER` | `2:275` | 379 | 48 | UNVERIFIED |
| `PARAMETRIC` | `2:223` | 379 | 307 | UNVERIFIED |
| `PARITY` | `2:371` | 381 | 555 | UNVERIFIED |
| `PARSURFACE` | `171:9` | 382 | — | UNVERIFIED |
| `PATH` | `2:33` | 383 | 555 | UNVERIFIED |
| `PCOEF` | `171:83` | 384 | — | UNVERIFIED |
| `PCONTOUR` | `171:13` | 385 | — | UNVERIFIED |
| `PCOV` | `171:42` | 386 | 555 | UNVERIFIED |
| `PDIM` | `2:195` | 387 | 116 | UNVERIFIED |
| `PERM` | `2:130` | 388 | — | UNVERIFIED |
| `PEVAL` | `171:84` | 388 | — | UNVERIFIED |
| `PGDIR` | `2:351` | 389 | 555 | UNVERIFIED |
| `PICK` | `2:279` | 390 | 48 | UNVERIFIED |
| `PICT` | `2:210` | 390 | 116 | UNVERIFIED |
| `PICTURE` | `2:200` | 391 | 110 | UNVERIFIED |
| `PINIT` | `171:129` | 392 | 402 | UNVERIFIED |
| `PIX?` | `2:205` | 393 | 117 | UNVERIFIED |
| `PIXOFF` | `2:204` | 392 | 116 | UNVERIFIED |
| `PIXON` | `2:203` | 393 | 116 | UNVERIFIED |
| `PKT` | `2:377` | 394 | 381 | UNVERIFIED |
| `PMAX` | `2:185` | 395 | — | UNVERIFIED |
| `PMIN` | `2:184` | 395 | — | UNVERIFIED |
| `POLAR` | `2:222` | 396 | 304 | UNVERIFIED |
| `POS` | `2:161` | 398 | — | UNVERIFIED |
| `PR1` | `2:240` | 405 | — | UNVERIFIED |
| `PREDV` | `2:303` | 398 | 556 | UNVERIFIED |
| `PREDX` | `2:305` | 399 | 556 | UNVERIFIED |
| `PREDY` | `2:304` | 400 | 556 | UNVERIFIED |
| `PRLCD` | `2:246` | 401 | — | UNVERIFIED |
| `PROMPT` | `1792:28` | 402 | 557 | UNVERIFIED |
| `PROOT` | `171:82` | 402 | — | UNVERIFIED |
| `PRST` | `2:242` | 403 | — | UNVERIFIED |
| `PRSTC` | `2:241` | 404 | — | UNVERIFIED |
| `PRVAR` | `2:244` | 404 | — | UNVERIFIED |
| `PSDEV` | `171:40` | 406 | 557 | UNVERIFIED |
| `PURGE` | `2:343` | 407 | — | UNVERIFIED |
| `PUT` | `2:176` | 408 | — | UNVERIFIED |
| `PUTI` | `2:177` | 410 | — | UNVERIFIED |
| `PVAR` | `171:41` | 411 | 557 | UNVERIFIED |
| `PVARS` | `2:350` | 412 | 392 | UNVERIFIED |
| `PVIEW` | `2:202` | 413 | 557 | UNVERIFIED |
| `PWRFIT` | `2:322` | 414 | — | UNVERIFIED |
| `PX→C` | `2:198` | 414 | — | UNVERIFIED |
| `QR` | `171:60` | 417 | 185 | UNVERIFIED |
| `QUAD` | `2:337` | 417 | 256 | UNVERIFIED |
| `QUOTE` | `2:257` | 418 | 558 | UNVERIFIED |
| `R→B` | `2:9` | 456 | — | UNVERIFIED |
| `R→C` | `2:153` | 457 | — | UNVERIFIED |
| `R→D` | `2:113` | 458 | — | UNVERIFIED |
| `RAD` | `2:136` | 420 | — | UNVERIFIED |
| `RAND` | `2:127` | 420 | — | UNVERIFIED |
| `RANK` | `171:53` | 421 | 173 | UNVERIFIED |
| `RANM` | `171:64` | 421 | — | UNVERIFIED |
| `RATIO` | `2:268` | 422 | 558 | UNVERIFIED |
| `RCEQ` | `2:249` | 423 | 558 | UNVERIFIED |
| `RCI` | `171:77` | 424 | 183 | UNVERIFIED |
| `RCIJ` | `171:78` | 424 | 183 | UNVERIFIED |
| `RCL` | `2:340` | 425 | 97 | UNVERIFIED |
| `RCLALARM` | `2:26` | 426 | 559 | UNVERIFIED |
| `RCLF` | `2:150` | 426 | — | UNVERIFIED |
| `RCLKEYS` | `2:382` | 427 | 435 | UNVERIFIED |
| `RCLMENU` | `2:349` | 428 | 559 | UNVERIFIED |
| `RCLΣ` | `2:285` | — | — | UNVERIFIED |
| `RCWS` | `2:149` | 429 | 188 | UNVERIFIED |
| `RDM` | `2:172` | 430 | — | UNVERIFIED |
| `RDZ` | `2:128` | 431 | — | UNVERIFIED |
| `RE` | `2:154` | 431 | — | UNVERIFIED |
| `RECN` | `2:365` | 432 | 559 | UNVERIFIED |
| `RECT` | `171:19` | 433 | 158 | UNVERIFIED |
| `RECV` | `2:366` | 433 | — | UNVERIFIED |
| `REPEAT` | `1792:6` | 434 | 420 | UNVERIFIED |
| `REPL` | `2:157` | 434 | — | UNVERIFIED |
| `RES` | `2:188` | 435 | 560 | UNVERIFIED |
| `RESTORE` | `2:353` | 437 | 394 | UNVERIFIED |
| `REVLIST` | `171:109` | 438 | — | UNVERIFIED |
| `RKF` | `171:43` | 438 | 560 | UNVERIFIED |
| `RKFERR` | `171:45` | 440 | — | UNVERIFIED |
| `RKFSTEP` | `171:44` | 441 | 561 | UNVERIFIED |
| `RL` | `2:1` | 442 | 191 | UNVERIFIED |
| `RLB` | `2:2` | 442 | 191 | UNVERIFIED |
| `RND` | `2:108` | 443 | — | UNVERIFIED |
| `RNRM` | `2:118` | 444 | 172 | UNVERIFIED |
| `ROLL` | `2:280` | 444 | 48 | UNVERIFIED |
| `ROLLD` | `2:281` | 445 | 48 | UNVERIFIED |
| `ROOT` | `2:251` | 445 | 561 | UNVERIFIED |
| `ROT` | `2:274` | 446 | 48 | UNVERIFIED |
| `ROW-` | `171:71` | 448 | — | UNVERIFIED |
| `ROW→` | `171:66` | 448 | — | UNVERIFIED |
| `ROW+` | `171:72` | 447 | — | UNVERIFIED |
| `rpm` | `171:127` | — | — | UNVERIFIED |
| `RR` | `2:3` | 449 | 191 | UNVERIFIED |
| `RRB` | `2:4` | 449 | 191 | UNVERIFIED |
| `RREF` | `171:63` | 450 | — | UNVERIFIED |
| `RRK` | `171:46` | 450 | — | UNVERIFIED |
| `RRKSTEP` | `171:47` | 452 | — | UNVERIFIED |
| `RSBERR` | `171:48` | 454 | — | UNVERIFIED |
| `RSD` | `2:123` | 455 | — | UNVERIFIED |
| `RSWP` | `171:75` | 456 | — | UNVERIFIED |
| `RULES` | `2:335` | — | — | UNVERIFIED |
| `SAME` | `2:228` | 458 | 562 | UNVERIFIED |
| `SBRK` | `2:376` | 459 | 386 | UNVERIFIED |
| `SCALE` | `2:194` | 459 | 562 | UNVERIFIED |
| `SCATRPLOT` | `2:318` | 460 | — | UNVERIFIED |
| `SCATTER` | `2:225` | 461 | 320 | UNVERIFIED |
| `SCHUR` | `171:62` | 462 | — | UNVERIFIED |
| `SCI` | `2:139` | — | — | UNVERIFIED |
| `SCLΣ` | `2:313` | 464 | — | UNVERIFIED |
| `SCONJ` | `2:326` | 464 | — | UNVERIFIED |
| `SDEV` | `2:299` | 464 | — | UNVERIFIED |
| `SEND` | `2:363` | 465 | 379 | UNVERIFIED |
| `SEQ` | `171:98` | 466 | — | UNVERIFIED |
| `SERVER` | `2:368` | 467 | — | UNVERIFIED |
| `SF` | `2:131` | 468 | — | UNVERIFIED |
| `SHOW` | `2:338` | 469 | — | UNVERIFIED |
| `SIDENS` | `171:122` | 469 | 563 | UNVERIFIED |
| `SIGN` | `2:78` | 470 | — | UNVERIFIED |
| `SIN` | `2:81` | 471 | — | UNVERIFIED |
| `SINH` | `2:84` | 472 | — | UNVERIFIED |
| `SINV` | `2:324` | 473 | — | UNVERIFIED |
| `SIZE` | `2:160` | 473 | 69 | UNVERIFIED |
| `SL` | `2:5` | 474 | 191 | UNVERIFIED |
| `SLB` | `2:6` | 475 | 191 | UNVERIFIED |
| `SLOPEFIELD` | `171:12` | 476 | 325 | UNVERIFIED |
| `SNEG` | `2:325` | 477 | 564 | UNVERIFIED |
| `SNRM` | `171:52` | 478 | — | UNVERIFIED |
| `SOLVEQN` | `171:35` | 478 | 564 | UNVERIFIED |
| `SORT` | `171:110` | 479 | — | UNVERIFIED |
| `SPHERE` | `171:21` | 480 | — | UNVERIFIED |
| `SQ` | `2:80` | 480 | — | UNVERIFIED |
| `SR` | `2:7` | 481 | 191 | UNVERIFIED |
| `SRAD` | `171:51` | 481 | 173 | UNVERIFIED |
| `SRB` | `2:8` | 482 | 191 | UNVERIFIED |
| `SRECV` | `2:360` | 482 | 386 | UNVERIFIED |
| `START` | `1792:9` | 485 | 418 | UNVERIFIED |
| `STD` | `2:141` | 486 | — | UNVERIFIED |
| `STEP` | `1792:12` | 487 | — | UNVERIFIED |
| `STEQ` | `2:250` | 488 | — | UNVERIFIED |
| `STIME` | `2:375` | 488 | 386 | UNVERIFIED |
| `STO` | `2:341` | 489 | 69 | UNVERIFIED |
| `STO-` | `2:328` | 494 | — | UNVERIFIED |
| `STO*` | `2:330` | — | — | UNVERIFIED |
| `STO/` | `2:329` | 495 | — | UNVERIFIED |
| `STO+` | `2:327` | 493 | 565 | UNVERIFIED |
| `STOALARM` | `2:25` | 490 | 564 | UNVERIFIED |
| `STOF` | `2:151` | 491 | — | UNVERIFIED |
| `STOKEYS` | `2:380` | 492 | 434 | UNVERIFIED |
| `STOΣ` | `2:283` | — | — | UNVERIFIED |
| `STR→` | `2:163` | 497 | — | UNVERIFIED |
| `STREAM` | `171:103` | 497 | 203 | UNVERIFIED |
| `STWS` | `2:148` | 499 | — | UNVERIFIED |
| `SUB` | `2:156` | — | — | UNVERIFIED |
| `SVD` | `171:57` | 18 | — | UNVERIFIED |
| `SVL` | `171:58` | 502 | — | UNVERIFIED |
| `SWAP` | `2:271` | 502 | 40 | UNVERIFIED |
| `SYSEVAL` | `2:49` | 503 | 566 | UNVERIFIED |
| `TAIL` | `171:97` | 505 | — | UNVERIFIED |
| `TAN` | `2:83` | 506 | — | UNVERIFIED |
| `TANH` | `2:86` | 507 | — | UNVERIFIED |
| `TAYLR` | `2:339` | 507 | 253 | UNVERIFIED |
| `TDELTA` | `171:123` | 508 | 566 | UNVERIFIED |
| `TEACH` | `171:17` | 509 | — | UNVERIFIED |
| `TEXT` | `2:217` | 509 | — | UNVERIFIED |
| `THEN` | `1792:1, 1792:24, 1792:26` | 510 | 416 | UNVERIFIED |
| `TICKS` | `2:18` | 510 | 196 | UNVERIFIED |
| `TIME` | `2:16` | 511 | — | UNVERIFIED |
| `TINC` | `171:124` | 512 | 567 | UNVERIFIED |
| `TLINE` | `2:207` | 513 | 116 | UNVERIFIED |
| `TMENU` | `2:347` | 514 | — | UNVERIFIED |
| `TOT` | `2:300` | 515 | 567 | UNVERIFIED |
| `TRACE` | `171:50` | 515 | 173 | UNVERIFIED |
| `TRANSIO` | `2:372` | 516 | 567 | UNVERIFIED |
| `TRN` | `2:175` | 517 | — | UNVERIFIED |
| `TRNC` | `2:109` | 517 | — | UNVERIFIED |
| `TRUTH` | `2:224` | 519 | 314 | UNVERIFIED |
| `TSTR` | `2:29` | 520 | — | UNVERIFIED |
| `TVARS` | `2:37` | 521 | 568 | UNVERIFIED |
| `TVM` | `171:85` | 521 | 219 | UNVERIFIED |
| `TVMBEG` | `171:86` | 522 | — | UNVERIFIED |
| `TVMEND` | `171:87` | 522 | — | UNVERIFIED |
| `TVMROOT` | `171:88` | 522 | 568 | UNVERIFIED |
| `TYPE` | `2:166` | 523 | 568 | UNVERIFIED |
| `UBASE` | `2:14` | 524 | 124 | UNVERIFIED |
| `UFACT` | `2:15` | 525 | 127 | UNVERIFIED |
| `UNTIL` | `1792:8` | 526 | 420 | UNVERIFIED |
| `UPDIR` | `2:35` | 527 | — | UNVERIFIED |
| `UTPC` | `2:308` | 527 | — | UNVERIFIED |
| `UTPF` | `2:310` | 528 | — | UNVERIFIED |
| `UTPN` | `2:309` | 529 | — | UNVERIFIED |
| `UTPT` | `2:311` | 529 | — | UNVERIFIED |
| `UVAL` | `2:12` | 530 | 132 | UNVERIFIED |
| `V→` | `2:180` | 535 | — | UNVERIFIED |
| `VAR` | `2:301` | 531 | 569 | UNVERIFIED |
| `VARS` | `2:36` | 531 | 569 | UNVERIFIED |
| `VERSION` | `171:15` | 532 | — | UNVERIFIED |
| `VTYPE` | `2:167` | 532 | 569 | UNVERIFIED |
| `WAIT` | `2:55` | 537 | 570 | UNVERIFIED |
| `WHILE` | `1792:5` | 538 | 420 | UNVERIFIED |
| `WIREFRAME` | `171:8` | 539 | 329 | UNVERIFIED |
| `WSLOG` | `2:19` | 541 | 570 | UNVERIFIED |
| `XCOL` | `2:306` | 544 | 571 | UNVERIFIED |
| `XMIT` | `2:359` | 545 | 386 | UNVERIFIED |
| `XOR` | `2:232` | 546 | 190 | UNVERIFIED |
| `XPON` | `2:105` | 547 | — | UNVERIFIED |
| `XRECV` | `171:95` | 548 | 571 | UNVERIFIED |
| `XRNG` | `2:218` | 548 | 571 | UNVERIFIED |
| `XROOT` | `2:74, 2:75` | 549 | — | UNVERIFIED |
| `XSEND` | `171:94` | 550 | 571 | UNVERIFIED |
| `XVOL` | `171:0` | 550 | 572 | UNVERIFIED |
| `XXRNG` | `171:3` | 551 | 572 | UNVERIFIED |
| `YCOL` | `2:307` | 553 | 573 | UNVERIFIED |
| `YRNG` | `2:219` | 554 | 573 | UNVERIFIED |
| `YSLICE` | `171:11` | 555 | 332 | UNVERIFIED |
| `YVOL` | `171:1` | 556 | 573 | UNVERIFIED |
| `YYRNG` | `171:4` | 557 | 573 | UNVERIFIED |
| `ZFACTOR` | `171:118` | 557 | 573 | UNVERIFIED |
| `ZVOL` | `171:2` | 558 | 574 | UNVERIFIED |
| `ΔLIST` | `171:100` | — | — | UNVERIFIED |
| `π` | `2:63` | — | — | UNVERIFIED |
| `ΠLIST` | `171:106` | — | — | UNVERIFIED |
| `Σ` | `2:254` | 717 | — | UNVERIFIED |
| `Σ-` | `2:287` | — | — | UNVERIFIED |
| `Σ+` | `2:286` | 584 | — | UNVERIFIED |
| `ΣLINE` | `2:314` | — | — | UNVERIFIED |
| `ΣLIST` | `171:104` | 334 | — | UNVERIFIED |
| `ΣX` | `2:291` | — | — | UNVERIFIED |
| `ΣX*Y` | `2:295` | — | — | UNVERIFIED |
| `ΣX^2` | `2:293` | — | — | UNVERIFIED |
| `ΣY` | `2:292` | — | — | UNVERIFIED |
| `ΣY^2` | `2:294` | — | — | UNVERIFIED |

## E. Abschlussbedingungen und aktueller Abnahmestand

- [ ] **Alle 58 Seiten** des Operation Index G-1–G-58 lückenlos als separate strukturelle Liste erfasst, nach PDF-Seiten und Einträgen geprüft.
- [ ] Aus allen `O`-Operationen und `C/F/A`-Einträgen kontextgetrennte Katalog-IDs gebildet; Namenskollisionen bewusst geklärt.
- [ ] Jede AUR-Command-Reference-Einheit erfasst, alle Argument-/Resultat-Typfälle und ROM-Revisionsunterschiede geprüft.
- [ ] Pocket-Guide-Index vollständig unabhängig abgeglichen; jede Differenz dokumentiert.
- [ ] 49 Tasten und alle gültigen Shift/Alpha/User-Kontexte, Softkeys, Editoren, Menüs, Dialoge vollständig geprüft.
- [ ] 15 Plottypen einschließlich editorabhängiger Analysemenüs, Daten und Parameter geprüft.
- [ ] Einheiten, Konstanten und alle einzelnen Equation-Library-Formeln katalogisiert und mit Quellen verifiziert.
- [ ] Automatische ID-/Referenz-/Delta-Checks sowie risikogewichtete Gerätetests durchgeführt.
- [ ] **0 ungeklärte Abweichungen**, 0 unbelegte Funktionen, 0 unzulässige HP-48gII-Funktionen.
  
**ERGEBNIS DES AKTUELLEN DURCHLAUFS: NO GO – nicht vollständig verifiziert.** Die Abschnitte C.1 und C.2 umfassen 143 quellengebundene Stichproben-/Kontextzeilen, nicht das vollständige Operationsverzeichnis. Diese Prüfmatrix ist eine nachprüfbare **Arbeitsgrundlage**, kein Qualitätszertifikat. Der menschliche Sichtabgleich der Originalseiten ist weiterhin erforderlich; die im Browser abrufbaren PDF-Ausschnitte reichen nicht für den unbeaufsichtigten, vollständigen Druckseiten-Abgleich. Die bereitgestellte **deutsche Kurzanleitung** umfasst 132 PDF-Seiten und behauptet ausdrücklich **nicht**, alle Operationen zu behandeln.

### Warum keine automatischen Prozentwerte?

`471 / 517` würde nur eine **Fundstellenhinweis-Quote** eines modellübergreifenden Sekundärindex darstellen, **keine** bestätigte Befehlsabdeckung. Für die über 1000 möglichen Kombinationen aus Bedienung, Menüs und Kontexten existiert hier noch keine gesicherte unabhängige Gesamtmenge. Die laufende C++-Implementierung und die iPhone-V1-Freigabe sind hiervon getrennte Themen.
