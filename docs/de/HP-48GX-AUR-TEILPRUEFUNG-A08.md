# HP 48GX – AUR-Teilprüfung A08 (Positionen 351–400)

**Prüfstand:** 22.11.2026 · **Gerät:** serienmäßiger HP 48GX (ohne Fremdkarten).  
**Bereich:** AUR-Kapitel-3-Inhaltsverzeichnis, AUR-Positionen **351–400** von `RRB` bis `STEP`.  
**Freigabeebene:** Namens-/Kurzbeschreibungstext-Vergleich; **keine** Originalscan-Sichtabnahme, **keine** Prüfung sämtlicher Stackdiagramme, Objekttypen, Flags, Fehlerfälle oder realer Hardwareausführung.

## 1. Ausgangsdaten und unabhängige Quellen

1. Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Ausgabe (1994), TOC-Seiten `Contents-12` und `Contents-13`. Verbindliche, nicht veränderte Textpositionen: [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json); Original: https://literature.hpcalc.org/community/hp48g-aur-en.pdf .
2. [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json), stock-HP-48GX-XLIB-Namensinventar. **47** der 50 AUR-Textpositionen besitzen direkte normierte ROM-Namen. Das Fehlen einer solchen Kennung bei drei Bedienaktionen ist **kein** Nachweis dafür, dass diese am Gerät nicht erreichbar wären.
3. Chris Coffin und Thomas Dick, *The HP 48G/GX Pocket Guide*, gedruckter **Command Index S. 64, 66 und 68** (Stacktabellen auf Folgeseiten) und RUN-Menüübersicht gedruckte S. 28–30. Text-PDF: https://literature.hpcalc.org/community/hp48g-pg-en.pdf ; OCR-Wiedergaben: https://www.manualslib.com/manual/3743173/Hp-48g.html?page=66 ; https://www.manualslib.com/manual/3743173/Hp-48g.html?page=68 ; https://www.manualslib.com/manual/3743173/Hp-48g.html?page=70 . Der Pocket Guide führt `SIMU` als interaktive PLOT-FLAG-Aktion, `SST` in der RUN-Menüübersicht, und `SST+` in der Debugger-Erläuterung; die Unterscheidung zum in der AUR-Baseline genannten `SST↓` muss am Original überprüft werden.
4. Hewlett-Packard, *HP 48G Series User's Guide*, Appendix G, gedruckte S. **G-41**: `SCLS` als eingabefähiger Statistik-Skalierungsbefehl. Textzugang: https://www.hp.com/ctg/Manual/c00442262.pdf . Der im AUR-TOC-/ROM-Index gespeicherte Name ist dagegen `SCLΣ`; die Pocket-PDF-Textextraktion gibt `SCLZ` aus. Dies bleibt **offene Quellen-/Glyphendiskrepanz**, keine stillschweigende Alias-Freigabe.
5. Unabhängige, ältere 48GX-Funktionsübersicht (für die mathematischen Gruppen und die ROM-/Menüabgrenzung): https://finseth.com/hpdata/hp48gx.php .

**Originalscan-Sperre:** Die Pocket-PDF-Originalbildseiten waren wegen der großen Datei über die Web-Screenshot-Schnittstelle nicht zugänglich. Die Tabelle dokumentiert **Text- und Kontextabgleich**, keine geprüften Druckglyphen. Besonders `RSWP`/`RSVP`, `SCATRPLOT`/`SCATR PLOT`, `SCLΣ`/`SCLS`/`SCLZ` sowie `SST↓`/`SST+` dürfen bis zur visuellen Prüfung nicht vorschnell gleichgesetzt oder als zusätzliche ROM-Kommandos erfunden werden.

## 2. Positionsweise Quellvergleichstabelle (50 Positionen)

| AUR # | AUR-Quelltextname | AUR-TOC | ROM-Name und XLIB | Pocket-Druckseite | Pocket-Suchtext/Beleg | Art der unabhängigen Zuordnung | Selbst verfasste deutsche Kurzbeschreibung |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 351 | `RRB` | Contents-12 | `RRB` / `2:4` | 64 | `RRB` | Command-Index-Text | Rotiert ein binäres Wort um genau ein Byte nach rechts. |
| 352 | `RREF` | Contents-12 | `RREF` / `171:63` | 64 | `RREF` | Command-Index-Text | Berechnet die reduzierte Zeilenstufenform einer Matrix. |
| 353 | `RRK` | Contents-12 | `RRK` / `171:46` | 66 | `RRK` | Command-Index-Text | Löst das Anfangswertproblem einer Differentialgleichung mit Rosenbrock- und Runge-Kutta-Verfahrenswahl; genaue Methodenselektion später prüfen. |
| 354 | `RRKSTEP` | Contents-12 | `RRKSTEP` / `171:47` | 66 | `RRKSTEP` | Command-Index-Text | Berechnet einen Folgeschritt des DGL-Lösers und wählt dabei RKF oder RRK anhand der Eingaben. |
| 355 | `RSBERR` | Contents-12 | `RSBERR` / `171:48` | 66 | `RSBERR` | Command-Index-Text | Ermittelt Lösungskorrektur und absolute Fehlerabschätzung für einen Rosenbrock-Schritt. |
| 356 | `RSD` | Contents-12 | `RSD` / `2:123` | 66 | `RSD` | Command-Index-Text | Berechnet den Residualvektor B−A·Z aus drei Arrays; Quellnotation/Stackordnung gesondert zu prüfen. |
| 357 | `RSWP` | Contents-12 | `RSWP` / `171:75` | 66 | `RSVP` | Command-Index-Text | Vertauscht zwei bestimmte Arrayzeilen i und j; Vektoren werden im Kontext als Spaltenmatrizen behandelt. |
| 358 | `R→B` | Contents-12 | `R→B` / `2:9` | 66 | `R→B` | Command-Index-Text | Konvertiert einen ganzzahligen reellen Wert in ein Binärzahl-Objekt. |
| 359 | `R→C` | Contents-12 | `R→C` / `2:153` | 66 | `R→C` | Command-Index-Text | Setzt zwei reelle Komponenten zu einem komplexen Objekt zusammen, auch Array-Varianten. |
| 360 | `R→D` | Contents-12 | `R→D` / `2:113` | 66 | `R→D` | Command-Index-Text | Konvertiert einen Winkel von Radiant zu Grad. |
| 361 | `SAME` | Contents-12 | `SAME` / `2:228` | 66 | `SAME` | Command-Index-Text | Prüft vollständige Objektgleichheit einschließlich symbolischer Objektstrukturen. |
| 362 | `SBRK` | Contents-12 | `SBRK` / `2:376` | 66 | `SBRK` | Command-Index-Text | Sendet einen BREAK-Zustand über die serielle Schnittstelle. |
| 363 | `SCALE` | Contents-12 | `SCALE` / `2:194` | 66 | `SCALE` | Command-Index-Text | Setzt horizontale und vertikale Plot-Skalierung, wirkt auf die ersten beiden PPAR-Parameter. |
| 364 | `SCATR PLOT` | Contents-12 | `SCATRPLOT` / `2:318` | 66 | `SCATRPLOT` | Command-Index-Text | Zeichnet ein Streudiagramm aus ΣDAT; AUR-Quelltext enthält ein Leerzeichen, ROM-Name SCATRPLOT. |
| 365 | `SCATTER` | Contents-12 | `SCATTER` / `2:225` | 66 | `SCATTER` | Command-Index-Text | Wählt den Streudiagramm-Plottyp, ohne dadurch das Diagramm bereits zu zeichnen. |
| 366 | `SCHUR` | Contents-12 | `SCHUR` / `171:62` | 66 | `SCHUR` | Command-Index-Text | Berechnet für eine quadratische Matrix eine Schur-Zerlegung A=Q·T·Qᵀ (bei reellen Daten); komplexe Variante/Stackformen offen. |
| 367 | `SCI` | Contents-12 | `SCI` / `2:139` | 66 | `SCI` | Command-Index-Text | Stellt wissenschaftliche Zahlenanzeige mit gewählter Stellenzahl ein. |
| 368 | `SCLΣ` | Contents-12 | `SCLΣ` / `2:313` | 66 | `SCLZ` | Command-Index-Text | Passt die Plotparameter PPAR für Statistik-Streudiagramme an ΣDAT an; Quellen nennen auch SCLS bzw. OCR SCLZ. |
| 369 | `SCONJ` | Contents-12 | `SCONJ` / `2:326` | 66 | `SCONJ` | Command-Index-Text | Ersetzt den Inhalt einer benannten Variablen durch sein komplex Konjugiertes. |
| 370 | `SDEV` | Contents-12 | `SDEV` / `2:299` | 66 | `SDEV` | Command-Index-Text | Gibt Stichproben-Standardabweichungen der Statistikspalten in ΣDAT zurück. |
| 371 | `SEND` | Contents-12 | `SEND` / `2:363` | 66 | `SEND` | Command-Index-Text | Sendet eine Kopie eines Objekts oder einer Variablen über Kermit. |
| 372 | `SEQ` | Contents-12 | `SEQ` / `171:98` | 66 | `SEQ` | Command-Index-Text | Erzeugt eine Ergebnisliste durch wiederholtes Auswerten eines Objekts mit einer laufenden Indexvariablen und Schrittweite. |
| 373 | `SERVER` | Contents-12 | `SERVER` / `2:368` | 66 | `SERVER` | Command-Index-Text | Schaltet das Gerät in den Kermit-Servermodus. |
| 374 | `SF` | Contents-12 | `SF` / `2:131` | 66 | `SF` | Command-Index-Text | Setzt das angegebene System- oder Benutzerflag. |
| 375 | `SHOW` | Contents-12 | `SHOW` / `2:338` | 66 | `SHOW` | Command-Index-Text | Macht implizite Vorkommen einer angegebenen Variablen in einem symbolischen Ausdruck explizit. |
| 376 | `SIDENS` | Contents-13 | `SIDENS` / `171:122` | 66 | `SIDENS` | Command-Index-Text | Berechnet die intrinsische Trägerdichte von Silizium aus der Temperatur. |
| 377 | `SIGN` | Contents-13 | `SIGN` / `2:78` | 68 | `SIGN` | Command-Index-Text | Gibt das Vorzeichen eines Werts zurück. |
| 378 | `SIMU` | Contents-13 | — | 68 | `SIMU` | Command-Index-Text | Interaktive PLOT-FLAG-Aktion zum Umschalten gleichzeitiger Kurvendarstellung; eigene ROM-XLIB-Kennung nicht im Namensindex. |
| 379 | `SIN` | Contents-13 | `SIN` / `2:81` | 68 | `SIN` | Command-Index-Text | Berechnet den Sinus. |
| 380 | `SINH` | Contents-13 | `SINH` / `2:84` | 68 | `SINH` | Command-Index-Text | Berechnet den hyperbolischen Sinus. |
| 381 | `SINV` | Contents-13 | `SINV` / `2:324` | 68 | `SINV` | Command-Index-Text | Ersetzt den Wert einer benannten Variablen durch ihren Kehrwert. |
| 382 | `SIZE` | Contents-13 | `SIZE` / `2:160` | 68 | `SIZE` | Command-Index-Text | Ermittelt typabhängig Dimensionen, Länge oder Elementanzahl eines Objekts. |
| 383 | `SL` | Contents-13 | `SL` / `2:5` | 68 | `SL` | Command-Index-Text | Verschiebt Binärbits um eine Position nach links. |
| 384 | `SLB` | Contents-13 | `SLB` / `2:6` | 68 | `SLB` | Command-Index-Text | Verschiebt Binärbits um acht Positionen nach links. |
| 385 | `SLOPEFIELD` | Contents-13 | `SLOPEFIELD` / `171:12` | 68 | `SLOPEFIELD` | Command-Index-Text | Wählt den Plottyp Richtungsfeld. |
| 386 | `SNEG` | Contents-13 | `SNEG` / `2:325` | 68 | `SNEG` | Command-Index-Text | Ersetzt den Inhalt einer Variablen durch dessen negativen Wert. |
| 387 | `SNRM` | Contents-13 | `SNRM` / `171:52` | 68 | `SNRM` | Command-Index-Text | Berechnet die Spektralnorm eines Arrays. |
| 388 | `SOLVEQN` | Contents-13 | `SOLVEQN` / `171:35` | 68 | `SOLVEQN` | Command-Index-Text | Startet eine Gleichung der eingebauten Equation Library anhand von Themen- und Gleichungsnummer; optionales Zeichnen in PICT. |
| 389 | `SORT` | Contents-13 | `SORT` / `171:110` | 68 | `SORT` | Command-Index-Text | Sortiert die Elemente einer Liste aufsteigend. |
| 390 | `SPHERE` | Contents-13 | `SPHERE` / `171:21` | 68 | `SPHERE` | Command-Index-Text | Wählt die sphärische Koordinatendarstellung. |
| 391 | `SQ` | Contents-13 | `SQ` / `2:80` | 68 | `SQ` | Command-Index-Text | Berechnet das Quadrat eines Werts. |
| 392 | `SR` | Contents-13 | `SR` / `2:7` | 68 | `SR` | Command-Index-Text | Verschiebt ein Binärwort um ein Bit nach rechts. |
| 393 | `SRAD` | Contents-13 | `SRAD` / `171:51` | 68 | `SRAD` | Command-Index-Text | Berechnet den Spektralradius einer quadratischen Matrix. |
| 394 | `SRB` | Contents-13 | `SRB` / `2:8` | 68 | `SRB` | Command-Index-Text | Verschiebt ein Binärwort um ein Byte nach rechts. |
| 395 | `SRECV` | Contents-13 | `SRECV` / `2:360` | 68 | `SRECV` | Command-Index-Text | Liest bis zu n Zeichen aus dem seriellen Empfangspuffer; zusätzlich Fehler-/Statusinformation. |
| 396 | `SST` | Contents-13 | — | — | `SST (RUN-Menü)` | RUN-Menü/Debugger, nicht im Pocket-Command-Index | Debugger-Bedienaktion: das nächste Programmelement in Einzelschritten ausführen; kein direkter ROM-Namenseintrag. |
| 397 | `SST↓` | Contents-13 | — | — | `SST+ / SST↓ (Menütext ungeklärt)` | RUN-Menü/Debugger, nicht im Pocket-Command-Index | Debugger-Bedienaktion für Einzelschritt mit Unterprogrammbehandlung; Pocket-Guide-Menü nennt SST+, konkrete Glyphen-/Funktionsdifferenz später am AUR-Original prüfen. |
| 398 | `START` | Contents-13 | `START` / `1792:9` | 68 | `START` | Command-Index-Text | Beginnt eine Zählschleife ohne eigene benannte Indexvariable. |
| 399 | `STD` | Contents-13 | `STD` / `2:141` | 68 | `STD` | Command-Index-Text | Aktiviert das Standard-Anzeigeformat. |
| 400 | `STEP` | Contents-13 | `STEP` / `1792:12` | 68 | `STEP` | Command-Index-Text | Schließt eine Zählschleife mit explizit angegebener Schrittweite. |

**Bilanz:** **50/50** AUR-TOC-Quellpositionen und **50 verschiedene Namen** erfasst. **47/50** haben einen direkt passenden normierten ROM-Namen/XLIB-Schlüssel. **48/50** AUR-Namen sind im Pocket-Guide-*Command Index*-Text kontextuell zuordenbar (die 47 ROM-Namen plus `SIMU`); **`SST` und `SST↓` fehlen in diesem programmierbaren Befehlsindex**, sind aber als Debugger-Bedienkontexte (mit abweichender `SST+`-Bezeichnung) im Pocket Guide beschrieben. **0** Scan-/Stack-Kommandos vollständig abgenommen.

## 3. Differenzregister und historische Trennungen

- **A08-364 `SCATR PLOT` vs. `SCATRPLOT`:** Die eingefrorene AUR-Textposition enthält ein Leerzeichen, der ROM-Name `SCATRPLOT` hat `2:318`. Im Pocket Guide wird `SCATRPLOT` als Ausführung des Streudiagramms bezeichnet, getrennt vom Plottyp `SCATTER`. Das Original der AUR-Indexglyphe ist noch zu prüfen.
- **A08-368 `SCLΣ` vs. `SCLS` vs. `SCLZ`:** Direkter ROM-Namensbeleg `SCLΣ` (`2:313`), HP User's Guide Appendix G enthält Textform `SCLS`, Pocket-PDF-Suchtext zeigt `SCLZ`. Wirkung: PPAR für Statistikstreudiagramm passend skalieren. **Originalbild der AUR- und User-Guide-Seiten sowie konkrete Eingabezeichenfolgen getrennt freigeben**, da historisch exakte Schreibweise kritisch ist.
- **A08-357 `RSWP`:** unabhängiger Pocket-Text hat `RSVP` als beschädigte Rohform, beschreibt aber eindeutig das Vertauschen zweier Zeilen einer Matrix; `RSWP` ist mit `171:75` im ROM belegt.
- **A08-378 `SIMU`:** dokumentierter UI-Softkey für gleichzeitig gezeichnete Plots; kein separater gleichnamiger ROM-Namen-XLIB-Eintrag. Kontext PLOT → FLAG; programmierbares Verhalten/Flagwirkung nur nach AUR-Detailprüfung bestätigen.
- **A08-396/397 `SST` / `SST↓`:** AUR-Namensindex nennt zwei Debugger-Einträge, die nicht im Command Index des Pocket Guides stehen. Dessen RUN-Menü und Programmiertext beschreiben jedoch `SST` und `SST+` für unterschiedliche Einzelschritte. **`SST↓` gegen `SST+` bleibt eine Glyphen-/Menükontext-Frage**, nicht zwei zusätzlich erfundene ROM-Einstiegspunkte. Keine eigenständigen XLIB-IDs erfinden.
- **A08-353–355 `RRK`, `RRKSTEP`, `RSBERR`:** Differentialgleichungs-Schätzer, Folgeschritt und Fehlerschätzung sind drei eigenständige Operatoren. Die Auswahllogik zwischen Rosenbrock- und RKF-Verfahren verlangt spätere Stack-/Fehlertests.
- **A08-356 `RSD`:** Pocket-Guide-Text nennt ausdrücklich den Residualausdruck `B−A·Z` aus drei Arrays, möglicherweise Vektoren. Keine wortwörtlich falsche Gleichsetzung mit `A·Z−B`.
- **A08-361 `SAME`:** Typ- und Objektgleichheit unterscheidet sich von arithmetischer Vergleichsauswertung symbolischer Ausdrücke.
- **A08-363 `SCALE`:** aktualisiert zwei horizontale/vertikale Maßstäbe in `PPAR`, nicht blind Pixelauflösung oder physische Bildschirmabmessungen.
- **A08-366 `SCHUR`:** Matrixzerlegung mit orthogonaler/unitärer Transformation und Dreiecks- oder Quasidreiecksstruktur; exakte Ergebnistypen und Konjugationsregel sind in V zu prüfen.
- **A08-369 `SCONJ`, A08-381 `SINV`, A08-386 `SNEG`:** *benannte* Speicherobjekte werden durch transformierte Inhalte ersetzt; kein bloßer Funktionswert auf einem nackten Stackargument.
- **A08-370 `SDEV`:** Stichprobenstandardabweichungen je Statistikspalte, nicht die Grundgesamtheitsabweichung `PSDEV`.
- **A08-372 `SEQ`:** erzeugt eine Liste wiederholter Auswertungsergebnisse über explizit festgelegte Indexvariable, Start, Ende und Schrittweite; nicht mit syntaktischen `FOR`/`STEP`-Markern gleichsetzen.
- **A08-375 `SHOW`:** macht im symbolischen Ausdruck implizite Vorkommen eines angegebenen Namens ausdrücklich sichtbar, nicht allgemeine Bildschirm-Textanzeige.
- **A08-376 `SIDENS`:** physikalische Silizium-Eigenschaft aus Temperatur, nicht als allgemeine Umrechnungseinheit ohne Parameter behandeln.
- **A08-388 `SOLVEQN`:** aufrufbarer Teil der **eingebauten** Equation Library, deren einzelne 315 Formeln in den späteren E-Tranchen geprüft werden.
- **A08-395 `SRECV`:** serieller *Zeichenpuffer*-Empfang, nicht der Kermit-Dateiempfang `RECV`.
- **A08-398/400 `START`/`STEP`:** Kontrollstrukturanfang und -abschluss mit expliziter Schrittweite; keine unabhängigen mathematischen Funktionen.

## 4. Freigabe-/Übergabestatus

- [x] Alle 50 AUR-Indexpositionen 351–400 mit Namen, Indexseiten, ROM-Schlüssel (wenn vorhanden), Quellenstatus und deutscher Arbeitsbeschreibung dokumentiert.
- [x] Drei Sonderfälle ohne eigene ROM-Namenskennung separat klassifiziert.
- [x] 48 unabhängige Pocket-Guide-Command-Index-Textzuordnungen positionsgenau festgehalten; zwei nur im UI-/Debugger-Kontext nachweisbar.
- [x] Kritische OCR-/Glyphen-Unterschiede und wichtige historische Bedeutungen erläutert.
- [ ] Original AUR/Pocket/User-Guide-PDF-Bilder visuell gegen die Quellpositionen prüfen.
- [ ] Vollständige Stackdiagramme, Objekttypen, Systemflags, Fehlerfälle und Hardwareverhalten prüfen.

**Checkpoint A08:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE` (48 von 50 Einträgen mit Pocket-Command-Index-Nachweis, zwei UI/DebUG-Index-Sonderfälle); `ORIGINAL_SCAN_NOT_SIGNED_OFF`; `AUR_STACK_NOT_SIGNED_OFF`. **Nächster Namensblock A09: Positionen 401–450 (`STEQ` bis `UBASE`).** Gesamtfreigabe `HISTORICAL_COMPLETENESS_NOT_CERTIFIED`; kein Blocker für iPhone V1.0.
