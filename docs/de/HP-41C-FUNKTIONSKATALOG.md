# HP-41C – vollständiger Katalog der Grundfunktionen und Bedienmöglichkeiten

**Projekt:** SASD Scientific Calculator · **Recherche-/Dokumentationsstand:** 2026-11-21  
**Historisches Referenzmodell:** HP-41C (ab 1979), ohne eingesteckte Funktionsmodule.  
**Dokumentstatus:** recherchierte **Spezifikation/Referenz**, keine Behauptung über bereits implementierte SASD-Funktionen.

> **Abgrenzung:** Diese Liste soll das **gesamte ab Werk vorhandene Funktions- und Bedienrepertoire des HP-41C** erfassen. Sie enthält die Standardbefehle (einschließlich nur über `XEQ` erreichbarer Befehle), Tastaturfunktionen, programmbezogene Bedienhandlungen und die für die korrekte Nachbildung wesentlichen Betriebszustände. Sie enthält **nicht** pauschal sämtliche Funktionen beliebiger Steckmodule, Software-Pacs oder späterer HP-41CX-Erweiterungen. Erweiterungen stehen am Ende ausdrücklich getrennt. Die originale HP-Dokumentation spricht von **über 130 Standardfunktionen/Operationen, 68 davon unmittelbar über Funktionstasten**. Diese historische Zählung ist nicht identisch mit der Anzahl unterschiedlicher Mnemonics in einer Tabelle: Tasten, Varianten, programmierbare Instruktionen und Bedienaktionen werden unterschiedlich gezählt.

## 1. Schreibweise und Geltungsbereich

- `X` und `Y` sind die obersten beiden Ebenen des vierstufigen UPN/RPN-Stacks; bei binären Funktionen ist meist `Y op X` gemeint.
- **Mnemonic** bezeichnet den am HP-41C sichtbaren Funktionsnamen oder die übliche historische Schreibweise. `SQRT` entspricht der Taste `√x`; `E^X` der Taste `eˣ`; `ST+` entspricht `STO +`. Nicht jeder Name ist direkt auf einer Taste aufgedruckt.
- `n`, `nn`, `nnn`: numerischer Funktionsparameter; `Rnn`: Datenregister; `IND`: indirekte Parametrierung über einen Registerinhalt.
- Befehle mit ähnlichen Bezeichnungen sind **nicht** zusammengefasst, wenn ihr Effekt verschieden ist (zum Beispiel `CLD`/`CLX`/`CLA` oder `FS?`/`FS?C`).
- Bei zahlreichen Funktionen bestehen Unterschiede zwischen **direkter Tastaturausführung**, **XEQ-Ausführung** und **Programmablauf**. Das Verhalten gehört zur Spezifikation, auch wenn es nicht nochmals als eigener mathematischer Befehl aufgelistet wird.

## 2. Vollständige Standardfunktionsliste nach Sachgebieten

### 2.1 Grundrechenarten, Potenzen, Logarithmen, Zahlentheorie

| HP-41C-Funktion | Bedeutung / Wirkung |
| --- | --- |
| `+` | Addition `Y + X`. |
| `−` | Subtraktion `Y − X`. |
| `×` (`*`) | Multiplikation `Y × X`. |
| `÷` (`/`) | Division `Y / X`; Division durch null erzeugt eine Fehlerbedingung. |
| `1/X` | Kehrwert `1/X`. |
| `X↑2` (`X²`) | Quadrat von `X`. |
| `Y↑X` (`Y^X`) | Potenz `Y` hoch `X`. |
| `SQRT` (`√x`) | Quadratwurzel. |
| `10↑X` (`10^X`) | Zehnerpotenz. |
| `E↑X` (`E^X`) | Natürliche Exponentialfunktion `e^X`. |
| `E↑X−1` (`E^X-1`) | Numerisch günstige Berechnung von `e^X − 1` für kleine `X`. |
| `LOG` | Dekadischer Logarithmus `log10(X)`. |
| `LN` | Natürlicher Logarithmus. |
| `LN1+X` | Numerisch günstige Berechnung von `ln(1 + X)` für kleine `X`. |
| `PI` (`π`) | Legt den internen Näherungswert von π in den Stack. |
| `ABS` | Absolutbetrag. |
| `SIGN` | Historische HP-41C-Funktion: negative Zahl ergibt −1; Null und positive Zahl ergeben +1; ALPHA-Daten ergeben 0. Original-X wird in LAST X gespeichert. **Achtung: nicht die gewöhnliche mathematische Signumfunktion!** |
| `INT` | Ganzzahliger Anteil von `X`; historische Abschneide-/Vorzeichenregeln beachten. |
| `FRC` | Gebrochener Anteil von `X`; passend zur historischen `INT`-Definition. |
| `MOD` | Rest der Division `Y mod X`. |
| `RND` | Rundet `X` entsprechend der aktuellen Anzeigeeinstellung (nicht bloß Anzeigeformatierung). |
| `FACT` | Fakultät einer nichtnegativen ganzen Zahl bis 69; **normal programmierbar (1 Byte)**. |
| `%` | Prozentwert: `X` Prozent von `Y`. |
| `%CH` | Prozentuale Änderung von `Y` nach `X`. |

### 2.2 Trigonometrie und Winkelmodi

| HP-41C-Funktion | Bedeutung / Wirkung |
| --- | --- |
| `SIN` | Sinus im aktiven Winkelmodus. |
| `COS` | Kosinus im aktiven Winkelmodus. |
| `TAN` | Tangens im aktiven Winkelmodus. |
| `ASIN` (`SIN⁻¹`) | Arkussinus. |
| `ACOS` (`COS⁻¹`) | Arkuskosinus. |
| `ATAN` (`TAN⁻¹`) | Arkustangens. |
| `DEG` | Winkelmodus Grad (360° pro Kreis). |
| `RAD` | Winkelmodus Radiant. |
| `GRAD` | Winkelmodus Neugrad/Gon (400 gon pro Kreis). |
| `D-R` | Grad → Radiant, als explizite Umrechnung. |
| `R-D` | Radiant → Grad, als explizite Umrechnung. |

**Wichtig:** `DEG`/`RAD`/`GRAD` ändern den **Modus**; `D-R`/`R-D` rechnen den **Wert** um. Letztere sind unabhängig davon als eigene Funktionen zu erfassen.

### 2.3 Koordinaten-, Zeit-/Winkel- und Zahlensystemumrechnung

| HP-41C-Funktion | Bedeutung / Wirkung |
| --- | --- |
| `R-P` | Rechtwinklige Koordinaten `(x,y)` → Polarkoordinaten `(r,θ)`; Ergebnis auf Stackebenen X/Y. |
| `P-R` | Polarkoordinaten `(r,θ)` → rechtwinklige Koordinaten `(x,y)`. |
| `HMS` | Dezimalstunden oder Dezimalgrad → `hh.mmss…`-/Grad-Minuten-Sekunden-Format. |
| `HR` | `hh.mmss…` → Dezimalstunden bzw. Dezimalgrad. |
| `HMS+` | Addition zweier Zeiten/Winkel im H.MMSS-Format mit Überträgen. |
| `HMS−` | Subtraktion zweier Zeiten/Winkel im H.MMSS-Format mit Überträgen. |
| `OCT` | Dezimalzahl → oktale Darstellung. |
| `DEC` | Oktale Darstellung → Dezimalzahl. |

**Nicht verwechseln:** `DEC` bedeutet beim HP-41C **Oktal-nach-Dezimal**, nicht Wechsel zu einem allgemeinen Dezimal-Eingabemodus. Eine eingebaute Binär-/Hexadezimal-Konvertierung gehört **nicht** zum Grundumfang.

### 2.4 Statistik

| HP-41C-Funktion | Bedeutung / Wirkung |
| --- | --- |
| `Σ+` | Fügt einen Datenpunkt (X bzw. X/Y) den Statistik-Akkumulatoren hinzu. |
| `Σ−` | Entfernt/korrigiert einen bereits akkumulierten Datenpunkt. |
| `CLΣ` | Löscht die sechs Statistikregister des aktuell festgelegten Blocks. |
| `ΣREG nn` | Legt die Position des Statistikregisterblocks `Rnn … R(nn+5)` fest. |
| `MEAN` | Berechnet Mittelwerte der akkumulierten X- und Y-Daten. |
| `SDEV` | Berechnet Stichproben-Standardabweichungen der akkumulierten X- und Y-Daten. |

**Beachtenswert:** Die historische Statistik verwendet einen **sechs Register umfassenden Akkumulatorblock** (Anzahl, Summen, Quadratsummen und Produkt-Summe). Eine eingebaute lineare Regressions-/Korrelationsfunktion ist **nicht** Teil dieses Grundkatalogs; entsprechende Routinen sind als Anwenderprogramm oder Erweiterung möglich.

### 2.5 Stack und Zahlenübernahme

| HP-41C-Funktion / Taste | Bedeutung / Wirkung |
| --- | --- |
| `ENTER↑` (`ENTER`) | Kopiert X nach Y, verschiebt Stackebenen und beeinflusst das Stack-Lift-Verhalten. |
| `X<>Y` (`x↔y`) | Vertauscht X und Y. |
| `RDN` (`R↓`) | Rollt den vierstufigen Stack nach unten. |
| `R↑` | Rollt den vierstufigen Stack nach oben. |
| `LASTX` | Ruft den für bestimmte Rechenoperationen gesicherten vorherigen X-Wert zurück. |
| `CLX` | Löscht X; verändert dabei auch die nachfolgende Stack-Lift-Regel. |
| `CLST` | Löscht die vier Stackregister X, Y, Z und T. |
| `X<> nn` (`X<>`) | Vertauscht X mit einem adressierten Daten- oder Spezialregister; **programmierbare Registeroperation** (normale Form 2 Bytes). |
| `CHS` | Wechselt das Vorzeichen der eingegebenen Zahl bzw. des Exponenten im Eingabekontext. |
| `EEX` | Beginnt die Eingabe eines dezimalen Exponenten. |
| `0` bis `9`, Dezimalpunkt | Zahleneingabe; Ziffern und Dezimalpunkt sind **Eingabetasten**, keine zusätzlichen mathematischen XEQ-Funktionen. |

**Stack-Semantik:** Fester automatischer **Vier-Ebenen-Stack** `T/Z/Y/X`, getrenntes `LAST X`. Binäre Funktionen nehmen X und Y ab, lassen T nachrücken/duplizieren nach den historischen Stack-Drop-Regeln. Ein dynamischer, unbegrenzter moderner Stack ist **keine** voll kompatible HP-41C-Nachbildung.

### 2.6 Datenregister, Speicherung und indirekte Adressierung

| HP-41C-Funktion | Bedeutung / Wirkung |
| --- | --- |
| `STO nn` | Speichert X in Register `Rnn`. |
| `ST+ nn` (`STO + nn`) | Addiert X zum Inhalt von `Rnn` und speichert das Ergebnis dort. |
| `ST− nn` (`STO − nn`) | Subtrahiert X vom Inhalt von `Rnn`. |
| `ST× nn` (`STO × nn` / `ST*`) | Multipliziert den Inhalt von `Rnn` mit X. |
| `ST÷ nn` (`STO ÷ nn` / `ST/`) | Dividiert den Inhalt von `Rnn` durch X. |
| `RCL nn` | Ruft den Wert eines Registers in den Stack zurück. |
| `CLRG` | Löscht die aktuell zugeordneten allgemeinen Datenregister. |
| `VIEW nn` | Zeigt einen Registerinhalt an, ohne ihn normal in X zu laden. |
| `SIZE nnn` | Stellt die Zahl der als Datenregister reservierten Register ein (gemeinsamer Programm-/Datenspeicher). |
| `IND` (Parameterform) | Registerindirekte Adressierung: Parameter wird aus einem anderen Register ermittelt; **kein** eigenständiger Rechenbefehl. |
| `STO`/`RCL` mit `.X/.Y/.Z/.T/.L` | Zugriff auf spezielle Stackregister bzw. LAST X, soweit für die jeweilige Adressform unterstützt. |
| `R100 … R318` | Erweiterte Hauptspeicherregister, **nur** wenn entsprechender Speicher vorhanden ist, üblicherweise **indirekt** adressiert. |

Indirekte Parameter sind insbesondere für `FIX`, `SCI`, `ENG`, `DSE`, `ISG`, `TONE`, `ΣREG`, Flagfunktionen, `CAT`, `STO`, `ST±/×/÷`, `RCL`, `X<>`, `ASTO`, `ARCL`, `VIEW`, `GTO` und `XEQ` dokumentiert. **Nicht** alle Funktionen besitzen alle Parameterformen.

### 2.7 ALPHA-Modus, Text und Zeichenketten

| HP-41C-Funktion / Taste | Bedeutung / Wirkung |
| --- | --- |
| `ALPHA` | Schaltet zwischen Normal- und ALPHA-Tastatur um. |
| `AON` | Schaltet den ALPHA-Modus ausdrücklich ein. |
| `AOFF` | Schaltet den ALPHA-Modus ausdrücklich aus. |
| `APPEND` | Hängt bei der Eingabe Text an, statt den bisherigen ALPHA-Inhalt zu ersetzen. |
| `CLA` | Löscht das ALPHA-Register. |
| `ASHF` | Verschiebt den ALPHA-Registerinhalt um sechs Zeichen nach links. |
| `ASTO nn` | Speichert die ersten sechs Zeichen des ALPHA-Registers in einem Datenregister. |
| `ARCL nn` | Hängt den Inhalt eines Datenregisters (Zahl oder ALPHA-Daten) an den ALPHA-Inhalt an. |
| `AVIEW` | Zeigt den ALPHA-Inhalt an; auch als Programmausgabe. |
| ALPHA-Zeicheneingabe | Buchstaben, Ziffern und Sonderzeichen der historischen ALPHA-Tastatur sowie Zeichenfolgen als Programmzeilen. |
| `X=Y?` / `X≠Y?` mit Text | Die beiden Gleichheitsvergleiche können auch ALPHA-Daten vergleichen; dies ist keine allgemeine Zeichenkettenbibliothek. |

Das **ALPHA-Register** fasst **bis zu 24 Zeichen**, das Display zeigt **bis zu 12 Zeichen gleichzeitig** und rollt längere Inhalte. Zeichen im ALPHA-Register, als Datenregisterinhalt und als Programmliteral sind semantisch zu unterscheiden.

### 2.8 Anzeige, Zahlenformat, Meldungen und Ton

| HP-41C-Funktion | Bedeutung / Wirkung |
| --- | --- |
| `FIX n` | Festkomma-Anzeige mit `n` Nachkommastellen (0–9). |
| `SCI n` | Wissenschaftliche Exponentialanzeige. |
| `ENG n` | Technische Exponentialanzeige mit Exponenten als Vielfache von drei. |
| `CLD` | Löscht eine angezeigte Meldung; **nicht** dasselbe wie `CLX`. |
| `BEEP` | Erzeugt einen Signalton, soweit die akustische Ausgabe aktiviert ist. |
| `TONE n` | Erzeugt eine der Tonhöhen (Parameter 0–9). |
| `VIEW nn` | Registerinhalt als Anzeige/Meldung (siehe Abschnitt 2.6). |
| `AVIEW` | ALPHA-Inhalt als Anzeige/Meldung (siehe Abschnitt 2.7). |
| `PSE` | Kurzzeitige Unterbrechung eines laufenden Programms; zeigt Zwischenstand an. |

**Weitere Anzeigefunktionen/Zustände:** Dezimaltrennzeichen und Tausendergruppierung über Flags 28/29; Statusanzeigen `BAT`, `USER`, `GRAD`/`RAD`, `SHIFT`, `PRGM`, `ALPHA` sowie Flag-Anzeigen 00–04; numerische Anzeige mit interner 10-stelliger Mantisse und zweistelligem Zehnerexponenten.

### 2.9 Programmierung, Programmsteuerung und Editor

| HP-41C-Funktion / Bedienung | Bedeutung / Wirkung |
| --- | --- |
| `PRGM` | Wechselt in den Modus zur Programmeingabe/-ansicht; selbst keine gewöhnliche Recheninstruktion. |
| `LBL nn` / `LBL "NAME"` | Definiert lokale numerische bzw. globale ALPHA-Programmmarken; weitere lokale ALPHA-Marken A–J/a–e. |
| `GTO label` | Springt zu einer Marke, ohne Rücksprungadresse abzulegen. |
| `XEQ label` / `XEQ FUNKTION` | Führt Unterprogramm oder benannte Funktion aus; Unterprogrammaufruf mit Rückkehr. |
| `RTN` | Rückkehr aus einem Unterprogramm. |
| `END` | Begrenzt Programmblöcke; beendet entsprechende Ausführung/Rückkehr. |
| `STOP` (Taste `R/S`) | Hält ein laufendes Programm an; `R/S` startet bzw. setzt es fort. |
| `PSE` | Programm-Pause mit Zwischenanzeige. |
| `PROMPT` | Zeigt eine ALPHA-Nachricht an, stoppt und erwartet Benutzereingabe. |
| `ISG nn` | Inkrementiert einen kodierten Zähler und überspringt nächste Zeile, wenn Grenzwert überschritten. |
| `DSE nn` | Dekrementiert einen kodierten Zähler und überspringt nächste Zeile bei Erreichen/Unterschreiten des Grenzwerts. |
| `SST` | Einzelschritt: Programmanweisung anzeigen bzw. ausführen, je nach Modus. |
| `BST` | Einen Programmschritt rückwärts bewegen/anzeigen. |
| `DEL nnn` | Löscht `nnn` Programmschritte ab aktueller Position (inklusive aktueller Zeile). |
| `CLP label` | Löscht ein durch globale Marke bestimmtes Programm aus dem bearbeitbaren Speicher. |
| `COPY label` | Kopiert ein im ROM-/Peripheriekatalog vorhandenes **kopierbares Programm** in den Anwenderprogrammspeicher; funktioniert nur, wenn solche Quelle vorhanden ist. |
| `PACK` | Verdichtet bzw. reorganisiert Programmspeicher und beseitigt freigewordene Bereiche. |
| `GTO . nnn` | Positioniert den Programmeditor auf Zeile `nnn` (Bedienfunktion, kein normaler bedingungsloser Programmsprung). |
| `GTO ..` | Positioniert ans Ende des Programmspeichers und kann das Packen auslösen. |
| Rücktaste (`←`) | Korrigiert Eingaben; im Programmeditor löscht sie je nach Zustand die aktuelle Anweisung. |
| `XEQ IND nn` / `GTO IND nn` | Indirekter Aufruf/Sprung über einen in einem Register gehaltenen Zielparameter. |
| Lokal- und Global-Labels | Labelsuche, Vor-/Rückwärtssuche mit Umlauf im Programm, globaler Programmkatalog. |
| Programmzeilen mit ALPHA-Literalen | Text in Programmen speichern und zur Laufzeit anzeigen/verwenden. |
| Programmunterbrechung | Stopps durch `STOP`, `R/S`, `PROMPT`, Fehler und Tastaturbedienung; Fortsetzung nach historischem Zustand. |

**Programmbesonderheiten:** Die Kontrollzahl von `ISG`/`DSE` hat die historische Struktur `iiiii.fffcc` (Zähler/Grenze/Schrittweite); ein Schrittwert `00` bedeutet Schrittweite 1. Tests arbeiten mit dem Prinzip **„Do if true“**: bei falscher Bedingung wird **die folgende Programmzeile übersprungen**. Das Original besitzt eine begrenzte Rücksprungtiefe (im Grundhandbuch **sechs** ausstehende Rücksprünge).

### 2.10 Alle zehn numerischen/ALPHA-Vergleichsbedingungen

| HP-41C-Funktion | Wahr, wenn ... |
| --- | --- |
| `X=0?` | X gleich null ist. |
| `X≠0?` | X ungleich null ist. |
| `X<0?` | X negativ ist. |
| `X≤0?` | X kleiner oder gleich null ist. |
| `X>0?` | X positiv ist. |
| `X=Y?` | X und Y gleich sind; auch auf vergleichbare ALPHA-Daten anwendbar. |
| `X≠Y?` | X und Y ungleich sind; auch auf vergleichbare ALPHA-Daten anwendbar. |
| `X<Y?` | X kleiner Y ist. |
| `X≤Y?` | X kleiner oder gleich Y ist. |
| `X>Y?` | X größer Y ist. |

**Kein `X≥0?` oder `X≥Y?` als zusätzlicher eingebauter Grundbefehl:** solche Bedingungen lassen sich über die vorhandenen Tests und Kontrollfluss ausdrücken.

### 2.11 Flags: vollständiger Standardbefehlsatz

| HP-41C-Funktion | Bedeutung / zulässige Nummern |
| --- | --- |
| `SF nn` | Benutzer-Flag setzen; `00–29`. |
| `CF nn` | Benutzer-Flag löschen; `00–29`. |
| `FS? nn` | Prüfen, ob Flag gesetzt ist; `00–55`. |
| `FC? nn` | Prüfen, ob Flag gelöscht ist; `00–55`. |
| `FS?C nn` | Zustand „gesetzt?“ prüfen und Benutzer-Flag anschließend löschen; `00–29`. |
| `FC?C nn` | Zustand „gelöscht?“ prüfen und Benutzer-Flag anschließend löschen; `00–29`. |

**Alle 56 Flags sind funktional relevant.** Flags 00–29 sind vom Nutzer veränderbar; Flags 30–55 bilden Systemzustände ab und sind regulär nur abfragbar. Besonders zu berücksichtigen:

| Flag(s) | Historische Bedeutung |
| --- | --- |
| 00–04 | Benutzerflags mit sichtbarer Statusmarkierung. |
| 05–10 | Allgemeine Benutzerflags. |
| 11 | Automatischer Programmstart beim Einschalten. |
| 12–13 | Druckoptionen (Doppelbreite/Kleinbuchstaben). |
| 14 | Kartenschreiber-/Überschreibverhalten (nur bei entsprechender Hardware). |
| 15–20 | Weitere Benutzerflags. |
| 21 | Druckerfreigabe bzw. angenommene Druckeranwesenheit. |
| 22–23 | Numerische bzw. ALPHA-Dateneingabe. |
| 24 | Bereichsfehlerbehandlung. |
| 25 | Einmaliges Übergehen bestimmter Fehler. |
| 26 | Akustische Ausgabe aktiv. |
| 27 | USER-Modus. |
| 28 | Dezimalpunkt-/Dezimalkomma-Format. |
| 29 | Zifferngruppierung. |
| 30–35 | Katalog-/Peripherieinterne Zustände. |
| 36–39 | Stellenanzahl der numerischen Anzeige. |
| 40–41 | Anzeigeformat FIX/SCI/ENG. |
| 42–43 | Winkelmodus GRAD/RAD; beide aus bedeutet DEG. |
| 44 | Dauerbetrieb (automatisches Abschalten unterdrückt). |
| 45–47 | Interne Eingabe-/Tastenzustände. |
| 48 | ALPHA-Modus. |
| 49 | Batterieschwäche. |
| 50 | Nachricht/Anzeige einer Meldung. |
| 51–52 | Einzelschritt-/Programmmodusstatus. |
| 53 | Peripherie-I/O bereit. |
| 54 | Pause läuft. |
| 55 | Physische Druckeranwesenheit. |

Systemflags dürfen bei einer späteren kompatiblen Implementierung nicht mit frei manipulierbaren Anwenderflags verwechselt werden. **Flags ≠ separate XEQ-Funktionen**; die Tabelle beschreibt benötigte Zustandssemantik.

### 2.12 Tastatur, Benutzerbelegung, Kataloge, Stromversorgung

| HP-41C-Funktion / Taste | Bedeutung / Wirkung |
| --- | --- |
| `USER` | Schaltet benutzerdefinierte Tastaturbelegung ein oder aus. |
| `ASN` | Weist einer Taste eine interne Funktion oder ein Anwender-/Modulprogramm zu; Zuweisung kann zurückgenommen werden. |
| `CAT` / `CATALOG 1` | Verzeichnis der Anwenderprogramm-Marken und Programmenden. |
| `CATALOG 2` | Verzeichnis von Funktionen/Programmen **angeschlossener** Module und Peripheriegeräte. Ohne Erweiterung kein eingebauter Modulfunktionsbestand. |
| `CATALOG 3` | Alphabetischer Katalog der eingebauten Standardfunktionen. |
| `SHIFT` (goldene Umschaltfunktion) | Ruft die zweite Tastenbelegung auf; Status und Bedienzeitpunkt beachten. |
| `ON` | Ein-/Ausschalten. |
| `OFF` | Programmierbarer Ausschaltbefehl. |
| `ON` als „Continuous On“ | Spezielle Einschalt-/Dauerbetriebs-Bedienfolge; unterdrückt zeitweilig automatische Abschaltung. |
| `PRGM` | Programmmodus umschalten (siehe Abschnitt 2.9). |
| `ALPHA` | ALPHA-Tastenebene (siehe Abschnitt 2.7). |
| `←` | Rückschritt/Korrektur im jeweiligen Eingabekontext. |
| `R/S` | Lauf/Stop-Umschaltung bei Anwenderprogrammen. |

Die **drei Kataloge** haben unterschiedliche Datenquellen. Insbesondere bedeutet `CAT 2` **nicht**, dass ein nackter HP-41C bereits Uhren-, Datei-, Druck-, Matrix- oder Kommunikationsfunktionen beherrscht.

### 2.13 Basisbefehl mit optionaler Peripheriewirkung

| HP-41C-Funktion | Bedeutung / Voraussetzung |
| --- | --- |
| `ADV` | Papiervorschub **an einem angeschlossenen kompatiblen Drucker**. Der Befehl ist im Grundfunktionsindex vorhanden, die Wirkung setzt externe Hardware voraus. |

## 3. Funktionsübergreifende Fähigkeiten, die eine reine Mnemonic-Liste nicht abdeckt

1. **RPN-Eingabemodell:** Vierstufiger Stack, LAST X, automatisches Stack-Lift/Drop, Zahleneingabestatus, Fehler- und Eingabekorrektur, `T`-Replikation.
2. **Numerisches Modell:** Dezimale interne Zahlendarstellung (10-stellige Mantisse, Exponent von −99 bis +99), Rundungs-/Überlauf-/Unterlaufregeln, Winkelmodi, Anzeige vs. gespeicherter Wert; Genauigkeit von `LN1+X`/`E^X-1` ist ausdrücklich relevant.
3. **Speicher:** Ungetrennter **Hauptspeicher für Programm und Daten**, im unveränderten HP-41C **63 frei aufteilbare Register à 7 Byte** (63 × 7 = 441 Byte nomineller Nutzspeicher; tatsächliche Programmbelegung hängt von Verwaltung/END/Format ab). Bei vier 82106A-Speichermodulen sind maximal **319** frei aufteilbare Hauptspeicherregister möglich. Nicht alle sind unmittelbar mit zweistelliger Registeradresse zugänglich. Der HP-41CV besitzt die große Kapazität ab Werk, **keinen zusätzlichen Grundbefehlsatz**.
4. **ALPHA:** 24-Zeichen-Register, 12-stellige Anzeige, ALPHA-Daten in Registern, Kombination von Text und Zahlen, Vergleich einiger ALPHA-Objekte, ALPHA-Programmliterale.
5. **Programme:** FOCAL-artige Tastaturprogrammierung, Zeilen, kurze und lange Label-/Adressformen, Unterprogramme, Editor, Kataloge, Key Assignments, byteabhängige Programmlänge und Speicherverdichtung.
6. **Parameter:** Direkte und indirekte Register-/Label-/Flagadressierung, Spezialregister X/Y/Z/T/LAST X, Grenzen und Fehlermeldungen bei nicht existierenden Registern oder Labels.
7. **Kontrollfluss:** Zeilensprung bei falsch ausgewertetem Test, rückkehrende Unterprogramme, Schleifenzählformat, RUN/STOP und Wiederanlauf, begrenzte Rücksprungverschachtelung.
8. **Persistenz („Continuous Memory“):** Rechnerzustand bleibt im Original beim gewöhnlichen Ausschalten erhalten; Speicherverlust, Batteriestatus und Einschaltverhalten sind gesondert zu modellieren.
9. **Fehler und Meldungen:** u. a. `DATA ERROR`/`ALPHA DATA`, `NONEXISTENT`, `OUT OF RANGE`, `MEMORY LOST`, `PACKING`, `TRY AGAIN`, `YES` und `NO`. Fehlerbehandlung ist teils flagabhängig.
10. **Status-/Peripheriegrenzen:** `ADV`, Druckerflags, Katalog 2, `COPY` und Schnittstellen zu optionalen Geräten sind Bestandteil der Grundarchitektur, jedoch **keine Belege für ohne Hardware verfügbare Druck-/Dateifunktionen**.
11. **Tastaturmatrix:** Normale, SHIFT-, USER- und ALPHA-Ebene; lokale Labels auf USER-Tasten; Tastenhaltedauer und Abbruch/NULL-Verhalten. Eine reine Liste von XEQ-Mnemonics ist darum keine vollständige Tastaturspezifikation.
12. **Programmierbarkeit:** **Nicht jede Bedienfunktion ist als gewöhnliche Programmzeile speicherbar**, etwa Editor-, Katalog-, Speicherverwaltungs- und Tastaturaktionen. Für vollständige Nachbildung diese Klassen separat testen.

## 4. Bewusst **nicht** dem nackten HP-41C zugerechnete Erweiterungen

Die folgende Tabelle ist eine **Abgrenzungs- und Forschungsübersicht**, keine vollständige Sammlung aller Befehle jedes jemals erschienenen Moduls.

| Ergänzung oder Modell | Funktionsbereiche | Einordnung |
| --- | --- | --- |
| **HP-41CV** | Größerer interner Hauptspeicher, bis 319 Register | Gleiche eingebauten Standardfunktionen wie HP-41C. |
| **Speichermodul 82106A / Quad Memory 82170A** | Mehr Programm-/Datenhauptspeicher | Kapazitätsausbau, kein eigener Mathematik-Befehlskatalog. |
| **Time Module 82182A** | Echtzeituhr, Datum, Alarme, Stoppuhr und Zeitfunktionen | **Optionales Modul** für C/CV; beim CX weitgehend integriert. |
| **Extended Functions/Memory (82180A u. a.)** | Erweiterte Speicher-/Dateifunktionen, spezielle Daten- und Programmbefehle | **Nicht** im Grundgerät; CX integriert die wesentlichen Extended-Funktionen/-Speicher. |
| **HP-41CX** | CV-Grundbestand plus eingebaute Zeit-/Extended-Funktionen und CX-spezifische Ergänzungen | **Späteres Modell**, kein ursprünglicher 41C-Befehl. |
| **Drucker 82143A** | Papierausgabe, Druckformatierung, weitere Druckbefehle | **Peripherieabhängige** Funktionen über Geräte-ROM. |
| **Kartenleser 82104A / Barcode-Wand 82153A** | Programm-/Dateneingabe bzw. Kartenlesen/-schreiben | Zusätzliche Hardware und ihre Befehle. |
| **HP-IL und weitere Schnittstellen** | Kommunikation mit Massenspeichern, Druckern, Messgeräten | **Spätere/optionale Schnittstellen**. |
| **Mathematik-, Statistik-, Advantage-, Navigations- und weitere Application-Pacs** | Je nach Modul z. B. Matrizen, komplexe Zahlen, spezielle Statistik, numerische Verfahren | Kein einheitlicher Basisbefehlssatz; pro Modul/Revision separat inventarisieren. |
| **PPC-ROM und andere Drittanbieter-ROMs** | Zusätzliche Programme und teilweise interne Befehle | **Fremderweiterungen** mit eigener Herkunft/Lizenz. |
| **Synthetic Programming / Byte Grabber / interne ROM-Aufrufe** | Nicht regulär dokumentierte Byte-/Status-/Maschinenzustandsoperationen | Historische Spezialtechniken, **keine** regulären Standardfunktionen aus Katalog 3. |

## 5. Test- und Implementierungshinweise für SASD

Diese Referenz ist ein **Soll-Katalog**, kein Umsetzungsauftrag für die erste iPhone-Version und keine bestandene Kompatibilitätsprüfung.

| Zielbereich | Projektzuordnung | Verifikation |
| --- | --- | --- |
| Alltags-RPN, Grundrechenarten, wichtige Wissenschaftsfunktionen | **M1/M2**, ausgewählter K1-Teil | Rechner-Tests, Stack-Tests, Zustandswiederherstellung |
| Modellgetreue HP-41C-Stacks, ALPHA, alle Basismnemonics, Flags, Registernummern | **K1/K2** je nach Programmbezug; Umsetzung schrittweise | Einzelbefehlsmatrix, Referenzbeispiele |
| FOCAL-Programmierung, Label, Sprünge, Schleifen, Unterprogramme, Byteprogramme | **M3 / K2** | Historische Programmfixtures und Zustandstests |
| Synthetische Programmierung, optionale Modulkompatibilität | **M4 / K3**, getrennte Komponenten | Quell-/Versionsprofil und streng begrenzte Tests |
| Nut-CPU-/ROM-/OS-Emulation | **M5 / K4 optional** | Eigenständige Forschung, keine V1.0-Abhängigkeit |

Für spätere Konformitätstests pro Befehl festhalten: **Mnemonic**, Modell/Modulprofil, erlaubte Argumentformen, Eingangsstack, Ausgangsstack, LAST X, Stack Lift, Flag-/ALPHA-/Register-Seiteneffekte, Fehlerfall, Programmkodierung, Speicherverbrauch, Quelle und Testergebnis. **„Im Katalog aufgelistet“ ist nicht „implementiert“.**

## 6. Vollständigkeitsprüfung und bekannte Grenzen

**Abgleich durchgeführt gegen** das Originalhandbuch HP-41C (Funktionsindex S. 267–270, Vergleichsfunktionen S. 170–171, SIGN S. 85), das HP-41C/41CV Operating Manual (Funktionsindex S. 59–68), die Tastaturübersicht sowie die vier hochgeladenen deutschsprachigen Fachbücher; außerdem HP-82180A-/HP-82182A-Modulhandbücher und CX-XROM-Tabellen. Insbesondere wurden nicht offensichtlich auf der Tastatur liegende Befehle wie `ABS`, `ASHF`, `BEEP`, `CLD`, `COPY`, `DSE`, `E^X-1`, `FC?C`, `FS?C`, `FRC`, `LN1+X`, `MOD`, `OCT`, `PACK`, `PROMPT`, `R↑`, `RND`, `SIGN`, `ΣREG` und `TONE` kontrolliert.

**Grenzen dieser Fassung:** Sie ist eine **vollständigkeitsorientierte Liste des standardmäßigen Anwenderfunktionsumfangs**, **keine** zeilengetreue Abschrift jedes historisch möglichen Tastenkodes, jedes Programmspeicher-Byteformats, jeder versteckten Systemroutine oder aller späteren Steckmodulbefehle. Die unterschiedlichen historischen Zählweisen von „130+ Funktionen“ wurden nicht künstlich mit einer Zeilenzahl gleichgesetzt. Falls einzelne gerätespezifische Bediensequenzen oder Modellrevisionen abweichen, muss der jeweilige Punkt anhand einer konkret bezeichneten Handbuchrevision bzw. eines echten Gerätes gesondert geprüft werden. **Die Quellen sind Verweise; ihr urheberrechtlich geschützter Wortlaut und ihre Abbildungen werden nicht übernommen.**


## 7. Tastatur vollständig abgeglichen: 39 Tasten und drei sichtbare Ebenen

Die Original-Handbuchzeichnung und das hochgeladene Foto wurden Taste für Taste abgeglichen. **Das Foto zeigt einen HP-41CX**, nicht das ursprüngliche C-Modell; seine Standardtastatur ist für die Grundbelegung trotzdem eine geeignete Vergleichsquelle. Die aufgedruckte SHIFT-Belegung ist eine Bedienbeschriftung; die Anzeige-/Programmmnemonics sind teils anders geschrieben.

| Reihe | Normal | Gold SHIFT | Blau ALPHA |
| --- | --- | --- | --- |
| Kopf | ON | — | — |
| Kopf | USER | — | — |
| Kopf | PRGM | — | — |
| Kopf | ALPHA | — | — |
| 1 | Σ+ | Σ− | A |
| 1 | 1/X | Y↑X | B |
| 1 | √X (SQRT) | X² | C |
| 1 | LOG | 10↑X | D |
| 1 | LN | E↑X | E |
| 2 | X<>Y | CLΣ | F |
| 2 | R↓ (RDN) | % | G |
| 2 | SIN | ASIN | H |
| 2 | COS | ACOS | I |
| 2 | TAN | ATAN | J |
| 3 | SHIFT | — | — |
| 3 | XEQ | ASN | K |
| 3 | STO | LBL | L |
| 3 | RCL | GTO | M |
| 3 | SST | BST | — |
| 4 | ENTER↑ | CATALOG | N |
| 4 | CHS | ISG | O |
| 4 | EEX | RTN | P |
| 4 | ← | CL X/A | — |
| 5 | − | X=Y? | Q |
| 5 | 7 | SF | R |
| 5 | 8 | CF | S |
| 5 | 9 | FS? | T |
| 6 | + | X≤Y? | U |
| 6 | 4 | BEEP | V |
| 6 | 5 | P→R | W |
| 6 | 6 | R→P | X |
| 7 | × | X>Y? | Y |
| 7 | 1 | FIX | Z |
| 7 | 2 | SCI | = |
| 7 | 3 | ENG | ? |
| 8 | ÷ | X=0? | : |
| 8 | 0 | π | SPACE |
| 8 | . | LAST X | , |
| 8 | R/S | VIEW | — |

Die ALPHA-Spalte nennt die **einfachen** ALPHA-Tasten. Auch SHIFT-ALPHA-Zeichen, Ziffern, Sonderzeichen, APPEND, Korrektur- und Eingabezustände gehören zur Gesamtbedienung. Tastaturbelegungen können im USER-Modus mit ASN ersetzt werden; der Rechner kennt außerdem lokale A–J-/a–e-Labels und globale ALPHA-Labels.

**Foto- und Tastatur-Kontrolle:** Aufgedruckt und daher kein Modul: Σ−, Y↑X, X², 10↑X, E↑X, CLΣ, %, ASIN/ACOS/ATAN, ASN, LBL, GTO, BST, CATALOG, ISG, RTN, X=Y?, SF, CF, FS?, X≤Y?, BEEP, P→R, R→P, X>Y?, FIX, SCI, ENG, X=0?, π, LAST X, VIEW. Nicht aufgedruckte Standardbefehle werden über XEQ oder USER-Zuweisung angesprochen.

## 8. Korrigierter Kreuzcheck gegen Original-Funktionsindex

**Quellen:** HP-41C Owner's Handbook and Programming Guide, **Funktionsindex S. 267–270**, Bedingungen **S. 170–171**, SIGN **S. 85**; HP-41C/41CV Operating Manual, **Function Index S. 59–68**. Nicht jede Web-Abschrift ordnet mehrspaltige Hinweise korrekt zu. Der detaillierte Index mit der Spalte **Bytes** löst unter anderem die missverständlichen „not programmable“-Angaben auf.

| Befehl / Streitfrage | Korrektes historisches Verhalten |
| --- | --- |
| **SIGN** | Für negative X-Werte −1; für **0 und positive Werte +1**; für ALPHA-Daten 0. Der vorige X-Wert bleibt in LAST X. |
| **FACT** | Fakultät ganzzahlig 0–69; **programmierbar, 1 Byte** (HP Operating Manual S. 62). |
| **X<> nn** | Registertausch X gegen ein Daten-/Spezialregister, **programmierbar**, normaler Registerparameter 2 Bytes; **nicht** X<>Y. |
| **Vergleiche** | Exakt zehn: X=0?, X≠0?, X<0?, X≤0?, X>0?, X=Y?, X≠Y?, X<Y?, X≤Y?, X>Y?. |
| **X<0?** | Im Originalhandbuch S. 171 vorhanden; in manchen Indexdarstellungen unvollständig erfasst. |
| **X≥0? / X≥Y?** | **Keine** zusätzlichen Standardbefehle. |
| **CLX / CLA / CLD / CLST / CLRG / CLΣ** | Sechs verschiedene Löschwirkungen (X / ALPHA / Meldung / Stack / Datenregister / Statistikblock). |
| **RND** | Verändert die gespeicherte Zahl nach dem aktuell eingestellten Anzeigeformat, nicht bloß die Anzeige. |
| **DEC / OCT** | Oktal→Dezimal und Dezimal→Oktal, keine allgemeine HEX/BIN-Basisumschaltung. |
| **STOP / R/S** | STOP ist eine Programminstruktion; R/S ist die Start-/Stopptaste, ihr Laufzeitverhalten ist speziell. |
| **APPEND** | Eingabezustand, keine frei ausführbare XEQ-Funktion. |
| **ASN / PASN** | ASN ist eine nicht programmierbare Grundgeräte-Zuweisung; PASN ist ein eigener programmierbarer X-Functions-Befehl. |
| **SIZE / PSIZE** | SIZE als nicht programmierbare Grundgeräte-Speicheraufteilung; PSIZE nur als Extended-Funktion programmierbar. |
| **AON / AOFF** | Explizite Programmbefehle zum Schalten von ALPHA; ALPHA ist eine Betriebs-/Eingabetaste. |
| **CAT 2** | Zeigt ausschließlich die tatsächlich zugeschalteten Module/Peripheriefunktionen; diese gehören nicht zum Grundgerät. |

**Nicht als normale Programmanweisung speicherbare Bedienaktionen:** ON-/USER-/ALPHA-/PRGM-/SHIFT-Tasten, Katalognavigation, ASN, CLP, COPY, DEL, PACK, SIZE, Editorpositionierung GTO . und GTO .., SST/BST als Editoraktionen, Korrektur- und APPEND-Eingaben. **Sehr wohl programmierbar:** FACT, X<> Register, ENTER, STOP, die vier Rechenarten und die mathematischen Funktionen. Bei „ausführbar über XEQ“, „assignierbar“, „programmierbar“ und „physische Taste“ handelt es sich um **vier getrennte Eigenschaften**.

**Weitere zwingende historische Semantik:** vierstufiger Stack T/Z/Y/X, getrenntes LAST X, Stack-Lift/Drop, 56-Bit-/7-Byte-Register, ALPHA bis 24 Zeichen (12 gleichzeitig sichtbar), 56 Flags, drei Kataloge, indirekte Argumente, Hauptspeicher zu Beginn **17 Daten- und 46 Programmregister**. Es gibt **63 frei zuteilbare Register** im Grund-41C; physisch ist auch der permanente .END.-Marker zu berücksichtigen. Bis vier normale Speichermodule: **319** Hauptregister; HP-41CV besitzt die 319 ab Werk. Hauptregister R100+ sind **nicht** dasselbe wie das Extended Memory des nachfolgenden Moduls.

## 9. HP 82180A: vollständige Liste seiner **47** Extended Functions

**Nur mit eingestecktem HP-82180A-Modul** am HP-41C/CV; beim HP-41CX integriert. Der Modulcode ist **XROM 25**. Die Modul-Funktionsnummern 01–47 sind lückenlos aufgeführt. HP 82180A stellt außerdem 127 **gesonderte Extended-Memory-Register** bereit; je HP 82181A X-Memory-Modul kommen 238 hinzu, bis maximal 603. Das ist **nicht** der normale Hauptspeicher.

| XROM | Mnemonic | Bedeutung / Voraussetzung |
| --- | --- | --- |
| 25,01 | ALENG | Länge der ALPHA-Zeichenfolge in X. |
| 25,02 | ANUM | In ALPHA enthaltene Zahl finden und numerisch in X übernehmen. |
| 25,03 | APPCHR | ALPHA-Zeichenfolge am Ende des aktuellen Textdatensatzes anhängen. |
| 25,04 | APPREC | ALPHA-Zeichenfolge als neuen Datensatz hinten an die Arbeits-Textdatei anhängen. |
| 25,05 | ARCLREC | Nächsten Teil eines Textdateisatzes an ALPHA anhängen. |
| 25,06 | AROT | ALPHA-Zeichen zyklisch um den Betrag in X drehen (Vorzeichen bestimmt Richtung). |
| 25,07 | ATOX | Linkes ALPHA-Zeichen entfernen und Zeichenkode in X ablegen. |
| 25,08 | CLFL | Inhalt der angegebenen Daten-/Textdatei löschen, Datei selbst behalten. |
| 25,09 | CLKEYS | Sämtliche USER-Tastenbelegungen aufheben. |
| 25,10 | CRFLAS | ASCII-/Textdatei in Extended Memory neu anlegen. |
| 25,11 | CRFLD | Datendatei in Extended Memory neu anlegen. |
| 25,12 | DELCHR | Gewählte Anzahl Zeichen ab dem Dateizeichenzeiger löschen. |
| 25,13 | DELREC | Aktuellen Textdateisatz löschen. |
| 25,14 | EMDIR | Dateiverzeichnis des Extended Memory anzeigen und freien Platz ermitteln. |
| 25,15 | FLSIZE | Größe der angegebenen Datei in Registern nach X. |
| 25,16 | GETAS | ASCII-Datei aus angeschlossenem HP-IL-Massenspeicher in Extended Memory übernehmen. |
| 25,17 | GETKEY | Bis ungefähr zehn Sekunden auf eine Taste warten, Tastenkode bzw. 0 nach X. |
| 25,18 | GETP | Programmdatei aus Extended Memory als letztes Hauptspeicherprogramm laden/ersetzen. |
| 25,19 | GETR | Gesamte Datendatei ab Hauptregister 00 einlesen. |
| 25,20 | GETREC | Bis zu 24 Zeichen aus aktuellem Textdatensatz in ALPHA laden. |
| 25,21 | GETRX | Gewählten Teil der Arbeits-Datendatei in Hauptdatenregister einlesen. |
| 25,22 | GETSUB | Extended-Memory-Programm an Hauptprogrammspeicher anhängen. |
| 25,23 | GETX | Aktuelles Register der Arbeits-Datendatei nach X holen. |
| 25,24 | INSCHR | ALPHA-Zeichen vor der aktuellen Textdatei-Zeichenposition einfügen. |
| 25,25 | INSREC | Neuen Textdatensatz vor dem aktuellen Satz einfügen. |
| 25,26 | PASN | Programmgesteuert Funktion/Programm einer Taste zuweisen. |
| 25,27 | PCLPS | Benanntes Hauptspeicherprogramm und alle folgenden Programme löschen. |
| 25,28 | POSA | Zeichen oder Teilstring in ALPHA finden; Position bzw. −1 liefern. |
| 25,29 | POSFL | In Arbeits-Textdatei nach Zeichenfolge aus ALPHA suchen. |
| 25,30 | PSIZE | Speicheraufteilung programmgesteuert über X festlegen. |
| 25,31 | PURFL | Benannte Extended-Memory-Datei löschen und Platz freigeben. |
| 25,32 | RCLFLAG | Kodierte Zustände der Flags 00–43 nach X holen. |
| 25,33 | RCLPT | Positionszeiger der Arbeitsdatei nach X holen. |
| 25,34 | RCLPTA | Positionszeiger einer benannten Datei nach X holen. |
| 25,35 | REGMOVE | Block von Hauptdatenregistern an andere Position kopieren. |
| 25,36 | REGSWAP | Zwei Hauptdatenregister-Blöcke vertauschen. |
| 25,37 | SAVEAS | ASCII-Datei aus Extended Memory auf HP-IL-Massenspeicher sichern. |
| 25,38 | SAVEP | Hauptspeicher-Programm in Extended-Memory-Programmdatei sichern. |
| 25,39 | SAVER | Alle Hauptdatenregister in Datendatei sichern. |
| 25,40 | SAVERX | Gewählten Hauptdatenregister-Block in Arbeits-Datendatei sichern. |
| 25,41 | SAVEX | Wert aus X in aktuellen Datendatei-Registereintrag schreiben. |
| 25,42 | SEEKPT | Satz-/Zeichen-/Registerzeiger der Arbeitsdatei setzen. |
| 25,43 | SEEKPTA | Zeiger einer namentlich angegebenen Datei setzen. |
| 25,44 | SIZE? | Anzahl zugeordneter Hauptspeicher-Datenregister nach X. |
| 25,45 | STOFLAG | Zuvor kodiert gelesene Flagzustände wiederherstellen. |
| 25,46 | X<>F | X mit kodierten Flags 00–07 austauschen. |
| 25,47 | XTOA | Zeichenkode aus X als Zeichen an ALPHA anhängen. |

Die Operationen GETAS und SAVEAS benötigen zusätzlich den betreffenden HP-IL-Massenspeicher. Viele Extended-Memory-Befehle arbeiten mit einem Arbeitsdateizeiger, Dateinamen im ALPHA-Register oder kodierten Parametern in X. REGMOVE/REGSWAP benutzen Blockadressformate, SAVERX/GETRX Registerbereiche und SEEKPT/SEEKPTA Daten-/Satz-/Zeichenzeiger. Bei fehlendem Modul darf die SASD-Nachbildung diese Befehle nicht als „ab Werk vorhanden“ anbieten.

**Quellenabgleich:** Keith Jarett, *Erweiterte Funktionen des HP-41 – leicht gemacht*, Kapitel 1–4 und alphabetisches X-Funktionen-Verzeichnis auf Buchseite 220; HP 82180A Extended Functions/Memory Module Owner's Manual, XROM- und Funktionsindex. **Gezählt: 47/47.**

## 10. HP-41CX: vollständige Liste seiner **14 zusätzlichen** Extended-Funktionen

Diese Befehle gehören **nicht** zum normalen HP-41C, auch nicht zum alleinigen 82180A-Modul. **25,48 ist die CX-ROM-Kennung und keine 15. Benutzerfunktion.**

| XROM | Mnemonic | Bedeutung / Voraussetzung |
| --- | --- | --- |
| 25,49 | ASROOM | In der angegebenen ASCII-Datei freie Bytezahl in X. |
| 25,50 | CLRGX | Datenregisterblock gemäß kodierter Anfangs-/End-/Schritt-Adresse in X löschen. |
| 25,51 | ED | Eingebauten interaktiven Extended-Memory-Texteditor starten. |
| 25,52 | EMDIRX | n-te Extended-Memory-Datei abfragen: Dateiname nach ALPHA, Typkennung nach X. |
| 25,53 | EMROOM | Noch freie Extended-Memory-Register direkt nach X. |
| 25,54 | GETKEYX | Zeitbegrenzte Tasteneingabe: X liefert Zeichenkode, Y Tastenkode, auch SHIFT. |
| 25,55 | RESZFL | Größe einer Extended-Memory-Datei verändern. |
| 25,56 | ΣREG? | Anfangsregister des Statistikblocks nach X. |
| 25,57 | X=NN? | X gleich Wert eines über Y adressierten Registers? |
| 25,58 | X≠NN? | X ungleich Wert eines über Y adressierten Registers? |
| 25,59 | X<NN? | X kleiner als Wert eines über Y adressierten Registers? |
| 25,60 | X<=NN? | X kleiner/gleich Wert eines über Y adressierten Registers? |
| 25,61 | X>NN? | X größer als Wert eines über Y adressierten Registers? |
| 25,62 | X>=NN? | X größer/gleich Wert eines über Y adressierten Registers? |

Die sechs *NN*-Vergleiche prüfen **X gegen einen über den Wert in Y adressierten Registerinhalt**, also **nicht** gegen Y als reine Zahl. Auch ALPHA-Daten lassen sich nach den dafür dokumentierten Regeln vergleichen. GETKEYX weicht von GETKEY erheblich ab: zeitliches Eingabefenster, separater Tastencode in Y und Zeichenkode in X. Diese Eigenschaften sind wichtige K3-/K2-Testfälle.

**Quellen:** Jarett, Kapitel 4G, S. 72–77; HP-41CX-XROM-Tabelle des HP 82210A Emulator Application Card Owner's Manual, Anhang C. **Gezählt: 14/14 (25,49–25,62).**

## 11. HP 82182A Time Module: **29 Modulbefehle** plus **5 CX-exklusive Funktionen**

Das originale Grundgerät besitzt **keine eingebaute Echtzeituhr, Datums-/Alarm-Engine oder Stoppuhr**. Erst das optionale HP-82182A-Time-Modul bietet XROM-26-Funktionen. Dagegen sind rein mathematische Uhrzeitumrechnungen HMS/HR/HMS+/HMS− bereits Teil des Grundgeräts und mit einer Echtzeituhr nicht zu verwechseln.

| XROM | Mnemonic | Bedeutung / Voraussetzung |
| --- | --- | --- |
| 26,01 | ADATE | Datum aus X formatiert an ALPHA anhängen. |
| 26,02 | ALMCAT | Alarme auflisten; spezieller Alarm-Katalogmodus. |
| 26,03 | ALMNOW | Ältesten überfälligen Programmalarm aktivieren. |
| 26,04 | ATIME | Uhrzeit aus X im eingestellten Format an ALPHA anhängen. |
| 26,05 | ATIME24 | Uhrzeit aus X im 24-Stunden-Format an ALPHA anhängen. |
| 26,06 | CLK12 | 12-Stunden-Uhrformat setzen. |
| 26,07 | CLK24 | 24-Stunden-Uhrformat setzen. |
| 26,08 | CLKT | Zeit ohne Datum auf Uhranzeige darstellen. |
| 26,09 | CLKTD | Zeit und Datum auf Uhranzeige darstellen. |
| 26,10 | CLOCK | Uhransicht anzeigen (auch spezielle ON-Bedienfolge). |
| 26,11 | CORRECT | Uhr stellen und Gangabweichungsfaktor automatisch korrigieren. |
| 26,12 | DATE | Aktuelles Datum in X. |
| 26,13 | DATE+ | Anzahl Tage zu einem Datum addieren. |
| 26,14 | DDAYS | Anzahl Tage zwischen zwei Datumswerten. |
| 26,15 | DMY | Datumsformat Tag–Monat–Jahr aktivieren. |
| 26,16 | DOW | Wochentag eines Datums bestimmen. |
| 26,17 | MDY | Datumsformat Monat–Tag–Jahr aktivieren. |
| 26,18 | RCLAF | Uhr-Gangkorrekturfaktor lesen. |
| 26,19 | RCLSW | Stoppuhrwert nach X. |
| 26,20 | RUNSW | Stoppuhr starten. |
| 26,21 | SETAF | Uhr-Gangkorrekturfaktor setzen. |
| 26,22 | SETDATE | Kalenderdatum der Uhr setzen. |
| 26,23 | SETIME | Uhrzeit setzen. |
| 26,24 | SETSW | Stoppuhr-Startwert setzen. |
| 26,25 | STOPSW | Stoppuhr stoppen. |
| 26,26 | SW | Interaktiven Stoppuhrmodus mit eigener Tastaturbelegung aktivieren. |
| 26,27 | T+X | Uhrzeit um signierten Wert aus X verstellen. |
| 26,28 | TIME | Aktuelle Uhrzeit nach X. |
| 26,29 | XYZALM | Alarm aus Stackdatum, Zeit, Wiederholungsintervall und ALPHA-Aktion anlegen. |

Die folgenden **fünf** Befehle sind zusätzlich **HP-41CX-spezifisch**, nicht Teil des ursprünglichen Time-Moduls für 41C/41CV:

| XROM | Mnemonic | Bedeutung / Voraussetzung |
| --- | --- | --- |
| 26,31 | CLALMA | ALPHA-Alarm löschen. |
| 26,32 | CLALMX | Durch X spezifizierten Alarm löschen. |
| 26,33 | CLRALMS | Alarme gesammelt löschen. |
| 26,34 | RCLALM | Gespeicherte Alarmparameter zurückrufen. |
| 26,35 | SWPT | Stoppuhr-Zeiger-/Datensatzfunktion (CX). |

**26,00 und 26,30** sind Kennungen/Modulüberschriften, keine separaten Anwenderbefehle. Alarmverzeichnis und Stoppuhr besitzen darüber hinaus **modusspezifische Tastaturaktionen** (Alarme löschen/ansehen, Vor/Zurück, Start/Stop, Split und Tastenzeiger); diese sind nicht mit neuen ROM-Mnemonics gleichzusetzen. Quellen: HP 82182A Time Module Owner's Manual / Quick Reference und HP 82210A XROM-Tabelle. **Gezählt: 29+5.**

## 12. Originale **HP-41C-Standard-Programmsammlung**: alle zehn enthaltenen Programme

Die vom Nutzer hochgeladene HP-Standard-Programmsammlung (August 1979) enthält **zehn** erst einzugebende Anwenderprogramme. Sie sind *Rechnerfähigkeiten durch Programme*, **keine zehn zusätzlichen CAT-3-Befehle**.

| Nr. | Programm | Aufgabe / Grenzen |
| --- | --- | --- |
| 1 | UPN-Lehrgang | Stack/Stackbewegung sichtbar machen; Grundgerät. |
| 2 | Kalenderrechnungen | Datum, Tagesdifferenz und Wochentag über Anwenderprogramm; keine Uhr im Grundgerät. |
| 3 | Wortratespiel | ALPHA-gestütztes Ratespiel; Grundgerät. |
| 4 | Arithmetik-Lehrgang | Rechenübungen mit Feedback; Grundgerät. |
| 5 | Hexadezimal-Dezimal-Umwandlung | Konvertierungsprogramm; keine eingebaute HEX-Taste. |
| 6 | Finanztechnische Berechnungen | Finanzmathematik als Programm; kein Basis-Finanz-ROM. |
| 7 | Nullstellenbestimmung | Numerische Nullstellensuche als Programm; kein eingebauter SOLVE. |
| 8 | Kurvenanpassung | Vier Kurventypen fitten, zusätzliche Statistikroutine. |
| 9 | Vektor-Operationen | Vektor-/Komplexzahlrechnungen über Programm. |
| 10 | Black Jack | Spiel; laut HP-Einleitung **zusätzliches Speichermodul nötig**. |

**Quellenseiten:** beigefügte *HP-41C Standard-Programmsammlung*, PDF-Seite 5 (Einleitung: Black Jack braucht ein zusätzliches Speichermodul) und PDF-Seite 6 (Inhaltsverzeichnis). Die historischen Programmlistings und Barcodes werden **nicht** ohne Rechteprüfung ins öffentliche Repository kopiert. **Gezählt: 10/10.**

## 13. Karl-Heinz Gosmann: Hauptthemen seines **HP-41C/CV Anwenderhandbuchs** (1983)

Gosmann nennt **26 vollständige Anwenderprogramme** (Titelblatt des hochgeladenen PDFs). Das Inhaltsverzeichnis bildet Themen und Kapitel, **nicht eine Liste von 26 verschiedenen Firmwarebefehlen**. Alle dort erkennbaren Hauptthemen:

| Gedruckte Seiten | Themen |
| --- | --- |
| 1–20 | Manuelles Rechnen, Anzeige/Löschen, Stack, LAST X, ALPHA, Speicher, Kataloge, USER-Modus. |
| 21–52 | FOCAL-Programme, lokale/globale Marken, Programmeditor, Steuerung, ISG/DSE, Bedingungen, Unterprogramme, Flags, indirekte Adressierung. |
| 53–69 | Interne Struktur, 56-Bit-Register, synthetisches Programmieren, Hexcode-Tabelle, Byte Jumper und ROM-Direktzugriffe. |
| 70–81 | Drucker 82143A, Plotten zweier Variablen, Biorhythmus, Wortratespiel, Kalender. |
| 82–98 | Sortieren, Primfaktorzerlegung, numerische Integration, 4×4-Matrizen, Fourier-Analyse. |
| 99–117 | Bode-Diagramme, Butterworth-/Tschebyscheff-Filterentwurf, aktive Filter, Eingangsimpedanzen verlustbehafteter Leitungen. |
| 118–171 | Barcode-Theorie, Typen, Prüfsummen, Herstellung, Barcode-Tastatur und Programmlistings. |

**Quellennachweis:** Datei *hp41-anwenderhandbuch.pdf*, Inhaltsverzeichnis auf PDF-Seiten 9–10, Hauptspeicherkonfiguration auf PDF-Seite 14, Flagübersicht im Kapitel 2.9.1. Die 26 Programme sind als **Anwenderprogramme**, nicht als ROM-Kommandos, klassifiziert.

## 14. John S. Dearing: **alle 26 Kapitel** mit Tipps und Routinen

Das bereitgestellte Buch *Tricks, Tips und Routinen für Taschenrechner der Serie HP-41* dokumentiert sehr viele kleine und größere Anwender-/synthetische Programme. Verlagsangabe: **über 350 Tipps/Routinen**. Der Inhalt ist kein Standard-CAT-3-Katalog. Die vollständige Themenstruktur des Buchs:

| Kapitel | Themenbereich |
| --- | --- |
| 1 | Elementare Funktionen und Operationen |
| 2 | Tipps zum Programmieren |
| 3 | Startbedingungen und Eingabeaufforderungen |
| 4 | Die Anzeige |
| 5 | Behandlung von ALPHA-Ketten |
| 6 | Flags und Töne |
| 7 | Umgang mit dem Stapel |
| 8 | Speicher und Vorhang |
| 9 | Datenregister |
| 10 | Block-Operationen |
| 11 | Matrizen und Datenverarbeitung |
| 12 | Sortieren |
| 13 | Zufallszahlen |
| 14 | Gebrochene Zahlen und Rundungsrechnung |
| 15 | Arithmetik und Algebra |
| 16 | Geometrie, Trigonometrie und Analysis |
| 17 | Zahlensysteme |
| 18 | Maßeinheiten und Abkürzungen |
| 19 | Statistik und Kombinatorik |
| 20 | Uhr, Kalender und Finanzen |
| 21 | Kartenleser und Lesestift |
| 22 | Der Drucker |
| 23 | Schrift-Fahnen |
| 24 | Gleichungen nach verschiedenen Variablen auflösen |
| 25 | Synthetisches Laden von Bytes |
| 26 | Kryptographie |

Die Teile **21–23** setzen oft externe Lese-/Druckhardware voraus, **25** betrifft synthetische Byte-/Statusmethoden; Matrizen, Zufallszahlen, Gleichungslösung, Binär-/Hexadezimalrechnung usw. sind in dieser Quelle vielfach **Anwenderprogramme**, nicht nachträglich dem nackten HP-41C zuzuschreibende Funktionen. Beispiel aus Kapitel 1: indirekt aufzurufende ALPHA-Labels sind auf sechs Zeichen begrenzt, und R/S kann einen laufenden Programmlauf trotz USER-Belegung stoppen. Quelle: hochgeladenes Buch, PDF-S. 6–7 (Inhaltsverzeichnis) und Kapitel 1.

## 15. Abschließende Abgrenzung und SASD-Kompatibilitätsprüfplan

**Was dieser Hauptkatalog nun exakt leistet:**

- **HP-41C/CV-Grundgerät:** alle belegten Standard-Mnemonics, mathematischen Funktionen, zehn Vergleichsbedingungen, Flagbefehle und Bedien-/Tastaturaktionen der dokumentierten Grundausstattung; physische **39-Tasten-Matrix** mit Grund-/SHIFT-/ALPHA-Schicht.
- **82180A:** vollständige **47 nummerierte XROM-25-Funktionen** samt Voraussetzungen.
- **HP-41CX exklusiv:** vollständige **14 nummerierte Extended-Funktionen**.
- **82182A:** vollständige **29 nummerierte XROM-26-Time-Funktionen**, plus **5 gesonderte CX-Time-Funktionen**.
- **Historische Software:** alle **10** HP-Standardprogramme, **26 Kapitel** der Dearing-Routinensammlung und sämtliche im Gosmann-Inhaltsverzeichnis benannten Anwendungsfelder sauber als **nicht eingebaute** Programme klassifiziert.
- **Nicht behauptet:** vollständige Einzelinventur **jedes** je erschienenen Application-Pacs (Math/Stat, PPC, Advantage, CCD, HP-IL, Card Reader, Drucker usw.), **aller** >350 Einzelroutinen oder **aller** synthetischen 256 Bytecode-Muster. Dafür braucht es eigene modul- und ROM-revisionsbezogene Kataloge. Die Vermischung wäre keine Vollständigkeit, sondern eine falsche HP-41C-Kompatibilitätsaussage.

Für die spätere ausführbare SASD-Konformitätsmatrix **je Eintrag** erfassen: Modell/ROM-Modul, Mnemonic, Code-/XROM-Nummer, direkte/indirekte Argumenttypen, Tastatur-/XEQ-/Programmfähigkeit, Stack vor/nach der Ausführung, LAST X, Register/ALPHA, Flags, Zahlengenauigkeit, Fehler/Seiteneffekte, Quellenstellen und goldene Testwerte. **Keine Funktion wird allein durch ihre Erwähnung in dieser Datei als implementiert oder bestanden eingestuft.**

### Zusätzliche überprüfte Quellen für diese Revision

- Vom Projekt bereitgestellt: *hp41-anwenderhandbuch.pdf* (Gosmann, 1983); *hp41-standard-Programmsammlung-de.pdf* (HP, August 1979); *Tricks, Tips und Routinen fuer Taschenrechenr der Serie HP-41.pdf* (Dearing, 1984); *Erweiterte Funktionen des HP 41 - leicht gemacht.pdf* (Jarett, 1986); Foto *HP-41CX_Programmable_Scientific_Calculator.jpg*.
- HP-41C Original-Funktionsindex: https://archived.hpcalc.org/greendyk/hp41c-manual/267.html , https://archived.hpcalc.org/greendyk/hp41c-manual/268.html , https://archived.hpcalc.org/greendyk/hp41c-manual/269.html , https://archived.hpcalc.org/greendyk/hp41c-manual/270.html
- HP-41C Vergleiche: https://archived.hpcalc.org/greendyk/hp41c-manual/170.html , https://archived.hpcalc.org/greendyk/hp41c-manual/171.html ; SIGN: https://archived.hpcalc.org/greendyk/hp41c-manual/85.html
- HP-41C/CV detaillierter Function Index: https://literature.hpcalc.org/community/hp41c41cv-om-en.pdf
- HP 82180A Extended Functions: https://literature.hpcalc.org/community/hp82180a-om-en.pdf
- HP 82182A Time Module: https://literature.hpcalc.org/community/hp82182a-om-en.pdf ; Übersicht: https://qrg41.fjk.ch/hp82182a.html
- HP 82210A, Anhang C, XROM-Tabellen für Extended Functions, CX und Time: https://literature.hpcalc.org/community/hp82210a-om-en.pdf


## 16. Quellen

1. Hewlett-Packard, *The HP-41C Owner's Handbook and Programming Guide*, 1979 (Original, weblesbar):  
   https://archived.hpcalc.org/greendyk/hp41c-manual/-1.html
2. Hewlett-Packard, *HP-41C/41CV Operating Manual: A Guide for the Experienced User*, insbesondere **Function Index S. 59–68** und **Flags S. 52–54**:  
   https://literature.hpcalc.org/community/hp41c41cv-om-en.pdf
3. Hewlett-Packard, *HP-41CV Quick Reference Guide*, insbesondere **Function Set S. 9–15** (kleine, bildlich nachprüfbare PDF-Fassung):  
   https://manuals.plus/m/76f0af4eadecf640eaea71244a6db774ef26fd661e2d39a3a775bc097bca6361.pdf
4. Hewlett-Packard, *HP Journal*, März 1980, **HP-41C Calculator – Specifications**:  
   https://hparchive.com/Journals/HPJ-1980-03.pdf
5. *HP-41C Bedienungs- und Programmierhandbuch* (deutsche Originalausgabe, Verzeichniseintrag):  
   https://literature.hpcalc.org/items/872
6. Projektinterne Planung: [Historische Series-41-Kompatibilität](../en/HISTORICAL-41.md), [Quellen-/Lizenzregeln](../en/REFERENCE-SOURCES.md), [Kompatibilitätsstufen](../en/COMPATIBILITY.md).

**Rechtehinweis:** Produkt-/Funktionsnamen dienen ausschließlich der sachlichen Beschreibung der historischen Referenz. Dies ist eine eigenständig formulierte Funktionsübersicht, keine Übernahme der Handbuchtexte, ROMs, Programmsammlungen oder Bilder.
