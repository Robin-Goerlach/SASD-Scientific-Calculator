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
| `SIGN` | Vorzeichenfunktion: −1, 0 oder +1. |
| `INT` | Ganzzahliger Anteil von `X`; historische Abschneide-/Vorzeichenregeln beachten. |
| `FRC` | Gebrochener Anteil von `X`; passend zur historischen `INT`-Definition. |
| `MOD` | Rest der Division `Y mod X`. |
| `RND` | Rundet `X` entsprechend der aktuellen Anzeigeeinstellung (nicht bloß Anzeigeformatierung). |
| `FACT` | Fakultät einer zulässigen nichtnegativen ganzen Zahl; historischer Wertebereich beachten. |
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
| `X<> nn` (`X<>`) | Vertauscht den Inhalt von X mit einem gewählten Speicherregister. |
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

**Abgleich durchgeführt gegen** das HP-41C-Bedienungs-/Programmierhandbuch (1979), dessen Funktionsindex, das HP-41C/41CV-Operating-Manual (**Function Index**, Seiten 59–68) und die HP-41CV-Quick-Reference (**Function Set**, Seiten 9–15). Insbesondere wurden nicht offensichtlich auf der Tastatur liegende Befehle wie `ABS`, `ASHF`, `BEEP`, `CLD`, `COPY`, `DSE`, `E^X-1`, `FC?C`, `FS?C`, `FRC`, `LN1+X`, `MOD`, `OCT`, `PACK`, `PROMPT`, `R↑`, `RND`, `SIGN`, `ΣREG` und `TONE` kontrolliert.

**Grenzen dieser Fassung:** Sie ist eine **vollständigkeitsorientierte Liste des standardmäßigen Anwenderfunktionsumfangs**, **keine** zeilengetreue Abschrift jedes historisch möglichen Tastenkodes, jedes Programmspeicher-Byteformats, jeder versteckten Systemroutine oder aller späteren Steckmodulbefehle. Die unterschiedlichen historischen Zählweisen von „130+ Funktionen“ wurden nicht künstlich mit einer Zeilenzahl gleichgesetzt. Falls einzelne gerätespezifische Bediensequenzen oder Modellrevisionen abweichen, muss der jeweilige Punkt anhand einer konkret bezeichneten Handbuchrevision bzw. eines echten Gerätes gesondert geprüft werden. **Die Quellen sind Verweise; ihr urheberrechtlich geschützter Wortlaut und ihre Abbildungen werden nicht übernommen.**

## 7. Quellen

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
