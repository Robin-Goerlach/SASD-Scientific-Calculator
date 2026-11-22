# HP 48GX – AUR-Teilprüfung A06 (Positionen 251–300)

**Prüfstand:** 22.11.2026 · **Referenzgerät:** serienmäßiger HP 48GX ohne Fremdkarten.  
**Quelle:** AUR-Kapitel-3-Inhaltsverzeichnis von `NUMX` bis `PVARS`; 50 Zeilen, 50 unterschiedliche Namen.  
**Prüfstatus:** Namens-/Kurzfunktionsabgleich gegen ROM-Baseline und unabhängigen Pocket-Guide-**Text**; **keine** vollständige Originalscan-/Druckglyphen-Sichtfreigabe und **keine** typvollständige AUR-Stack-/Fehlerfall-/Hardwareabnahme.

## 1. Quellen und Zuordnung

1. Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Auflage (1994), Kapitel 3, die AUR-TOC-Seiten `Contents-9` bis `Contents-11`. Die aktuelle quellgetreue Texttranskription ist in [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json) abgelegt; Original: https://literature.hpcalc.org/community/hp48g-aur-en.pdf .
2. Unabhängiger ROM-Namen-/XLIB-Datensatz für den 48GX: [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json). **50 direkte Namensentsprechungen**; in dieser Tranche keine Abweichung ohne XLIB-Namenskennung.
3. Chris Coffin und Thomas Dick, *The HP 48G/GX Pocket Guide* (Grapevine Publications, 1996), **Command Index, gedruckte S. 57 und 59** (gegenüberliegende Seiten 58 und 60 enthalten Stackdiagramme). Original-PDF: https://literature.hpcalc.org/community/hp48g-pg-en.pdf . Kontrollierbare unabhängig abrufbare HTML-Textwiedergaben: https://www.manualslib.com/manual/3743173/Hp-48g.html?page=60 und https://www.manualslib.com/manual/3743173/Hp-48g.html?page=62 . 
4. Der Original-PDF-Webzugriff erlaubte die Textextraktion (u. a. die alphabetisch folgenden Einträge `NUMX`, `NUMY`, `NΣ`, `OBJ→` bis `PERM` sowie `PEVAL` bis `PVARS`). Die separate **Bildseiten-Abfrage** scheiterte an der PDF-Dateigröße (ca. 34 MB). Dies ist **kein Scan-PASS**. Zusätzlich war der Web-OCR-Text stellenweise beschädigt, z. B. `NΣ`→`NZ` und `PROMPT`→`PRMPT`. Die ursprüngliche Druckglyphe ist nur nach Bildsichtung freizugeben.

## 2. Prüftabelle – jede AUR-Position einzeln

| AUR # | AUR-Name | AUR-Index | ROM-Name / XLIB | Pocket-Druckseite | Pocket-PDF-Textkandidat | Prüfstufe | Deutsche Funktionsbeschreibung |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 251 | `NUMX` | Contents-9 | `NUMX` / `171:6` | 57 | `NUMX` | POCKET_TEXT_NAME_FOUND | Stellt für perspektivische 3D-Plots die Zahl der x-Schritte pro y-Schritt ein; nicht lediglich eine Pixelbreite. |
| 252 | `NUMY` | Contents-9 | `NUMY` / `171:7` | 57 | `NUMY` | POCKET_TEXT_NAME_FOUND | Stellt die Zahl der y-Schritte im 3D-Betrachtungsvolumen ein. |
| 253 | `NΣ` | Contents-10 | `NΣ` / `2:288` | 57 | `NZ` | POCKET_OCR_GLYPH_AMBIGUITY | Liefert die Anzahl statistischer Datenzeilen in der reservierten Statistikvariablen ΣDAT. |
| 254 | `OBJ→` | Contents-10 | `OBJ→` / `2:169` | 57 | `OBJ→` | POCKET_TEXT_NAME_FOUND | Zerlegt Objekt in Komponenten; bei Listen, Arrays und weiteren Typen wird auch deren Anzahl bzw. Dimension abgelegt. |
| 255 | `OCT` | Contents-10 | `OCT` / `2:147` | 57 | `OCT` | POCKET_TEXT_NAME_FOUND | Schaltet die Anzeige binärer Ganzzahlen auf Oktal um, verändert nicht deren Zahlenwert. |
| 256 | `OFF` | Contents-10 | `OFF` / `2:41` | 57 | `OFF` | POCKET_TEXT_NAME_FOUND | Schaltet den Rechner aus; in Programmen abhängig vom Gerätezustand. |
| 257 | `OLDPRT` | Contents-10 | `OLDPRT` / `2:239` | 57 | `OLDPRT` | POCKET_TEXT_NAME_FOUND | Stellt die Druckerparameter in PRTPAR für das ältere Infrarotdruckermodell ein; kein allgemeiner Druckmodus. |
| 258 | `OPENIO` | Contents-10 | `OPENIO` / `2:361` | 57 | `OPENIO` | POCKET_TEXT_NAME_FOUND | Öffnet die eingestellte serielle oder Infrarot-Ein-/Ausgabeverbindung. |
| 259 | `OR` | Contents-10 | `OR` / `2:230` | 57 | `OR` | POCKET_TEXT_NAME_FOUND | Logisches oder bitweises ODER entsprechend Objekttyp und Binärwortlänge. |
| 260 | `ORDER` | Contents-10 | `ORDER` / `2:345` | 57 | `ORDER` | POCKET_TEXT_NAME_FOUND | Ordnet die Variablen im aktuellen VAR-Menü nach einer Namensliste neu. |
| 261 | `OVER` | Contents-10 | `OVER` / `2:275` | 57 | `OVER` | POCKET_TEXT_NAME_FOUND | Legt eine Kopie des Stackobjekts auf Ebene 2 auf Ebene 1; das Original bleibt erhalten. |
| 262 | `PARAMETRIC` | Contents-10 | `PARAMETRIC` / `2:223` | 57 | `PARAMETRIC` | POCKET_TEXT_NAME_FOUND | Wählt den parametrischen Plottyp. |
| 263 | `PARITY` | Contents-10 | `PARITY` / `2:371` | 57 | `PARITY` | POCKET_TEXT_NAME_FOUND | Legt die Parität der Kommunikation über die Systemvariable IOPAR fest. |
| 264 | `PARSURFACE` | Contents-10 | `PARSURFACE` / `171:9` | 57 | `PARSURFACE` | POCKET_TEXT_NAME_FOUND | Wählt eine parametrisierte 3D-Oberfläche als Plottyp. |
| 265 | `PATH` | Contents-10 | `PATH` / `2:33` | 57 | `PATH` | POCKET_TEXT_NAME_FOUND | Gibt den Verzeichnispfad vom HOME-Verzeichnis zum aktuellen Verzeichnis zurück. |
| 266 | `PCOEF` | Contents-10 | `PCOEF` / `171:83` | 57 | `PCOEF` | POCKET_TEXT_NAME_FOUND | Berechnet Polynomkoeffizienten aus angegebenen reellen oder komplexen Nullstellen. |
| 267 | `PCONTOUR` | Contents-10 | `PCONTOUR` / `171:13` | 57 | `PCONTOUR` | POCKET_TEXT_NAME_FOUND | Wählt den Plottyp Pseudokontur. |
| 268 | `PCOV` | Contents-10 | `PCOV` / `171:42` | 57 | `PCOV` | POCKET_TEXT_NAME_FOUND | Berechnet Populationskovarianz der im statistischen Datensatz verwendeten Spalten. |
| 269 | `PDIM` | Contents-10 | `PDIM` / `2:195` | 57 | `PDIM` | POCKET_TEXT_NAME_FOUND | Erzeugt ein leeres Grafikobjekt der angegebenen Dimensionen und legt es in PICT ab. |
| 270 | `PERM` | Contents-10 | `PERM` / `2:130` | 57 | `PERM` | POCKET_TEXT_NAME_FOUND | Berechnet Permutationen von n Elementen, k ausgewählt. |
| 271 | `PEVAL` | Contents-10 | `PEVAL` / `171:84` | 59 | `PEVAL` | POCKET_TEXT_NAME_FOUND | Wertet ein durch Koeffizienten gegebenes Polynom an x aus. |
| 272 | `PGDIR` | Contents-10 | `PGDIR` / `2:351` | 59 | `PGDIR` | POCKET_TEXT_NAME_FOUND | Löscht ein benanntes Verzeichnis (mit seinen Inhalten unter dokumentierten Voraussetzungen zu prüfen); nicht UPDIR. |
| 273 | `PICK` | Contents-10 | `PICK` / `2:279` | 59 | `PICK` | POCKET_TEXT_NAME_FOUND | Kopiert das durch den Zahlenparameter bezeichnete tiefere Stackobjekt auf Stackebene 1. |
| 274 | `PICT` | Contents-10 | `PICT` / `2:210` | 59 | `PICT` | POCKET_TEXT_NAME_FOUND | Legt den Inhalt der reservierten Grafikvariable PICT auf den Stack; nicht dasselbe wie PICTURE. |
| 275 | `PICTURE` | Contents-10 | `PICTURE` / `2:200` | 59 | `PICTURE` | POCKET_TEXT_NAME_FOUND | Öffnet die interaktive Grafikansicht samt zugehörigem Menü. |
| 276 | `PINIT` | Contents-10 | `PINIT` / `171:129` | 59 | `PINIT` | POCKET_TEXT_NAME_FOUND | Initialisiert die aktiven Speicherports; kein Initialisieren der Plotparameter. |
| 277 | `PIXOFF` | Contents-10 | `PIXOFF` / `2:204` | 59 | `PIXOFF` | POCKET_TEXT_NAME_FOUND | Löscht einen Bildpunkt in der Grafikvariable PICT. |
| 278 | `PIXON` | Contents-10 | `PIXON` / `2:203` | 59 | `PIXON` | POCKET_TEXT_NAME_FOUND | Setzt einen Bildpunkt in der Grafikvariable PICT. |
| 279 | `PIX?` | Contents-10 | `PIX?` / `2:205` | 59 | `PIX?` | POCKET_TEXT_NAME_FOUND | Prüft den Zustand eines Bildpunkts im PICT-Grafikobjekt. |
| 280 | `PKT` | Contents-10 | `PKT` / `2:377` | 59 | `PKT` | POCKET_TEXT_NAME_FOUND | Sendet ein selbst gewähltes Kermit-Paket an den Server und verarbeitet dessen Antwort. |
| 281 | `PMAX` | Contents-10 | `PMAX` / `2:185` | 59 | `PMAX` | POCKET_TEXT_NAME_FOUND | Legt die obere rechte Begrenzung des PICT-Koordinatenbereichs fest. |
| 282 | `PMIN` | Contents-10 | `PMIN` / `2:184` | 59 | `PMIN` | POCKET_TEXT_NAME_FOUND | Legt die untere linke Begrenzung des PICT-Koordinatenbereichs fest. |
| 283 | `POLAR` | Contents-10 | `POLAR` / `2:222` | 59 | `POLAR` | POCKET_TEXT_NAME_FOUND | Schaltet den Plottyp auf Polardarstellung um. |
| 284 | `POS` | Contents-10 | `POS` / `2:161` | 59 | `POS` | POCKET_TEXT_NAME_FOUND | Bestimmt die Position eines Elements in einer Liste bzw. einer Teilzeichenfolge in einem String. |
| 285 | `PREDV` | Contents-10 | `PREDV` / `2:303` | 59 | `PREDV` | POCKET_TEXT_NAME_FOUND | Historischer Regressionsvorhersagebefehl mit Funktion von PREDY, aber eigener ROM-Kennung. |
| 286 | `PREDX` | Contents-10 | `PREDX` / `2:305` | 59 | `PREDX` | POCKET_TEXT_NAME_FOUND | Berechnet zu einem bekannten y die geschätzte unabhängige Variable x gemäß aktuellem Fit-Modell. |
| 287 | `PREDY` | Contents-10 | `PREDY` / `2:304` | 59 | `PREDY` | POCKET_TEXT_NAME_FOUND | Berechnet zu einem bekannten x die geschätzte abhängige Variable y gemäß aktuellem Fit-Modell. |
| 288 | `PRLCD` | Contents-10 | `PRLCD` / `2:246` | 59 | `PRLCD` | POCKET_TEXT_NAME_FOUND | Druckt den Bildschirminhalt. |
| 289 | `PROMPT` | Contents-10 | `PROMPT` / `1792:28` | 59 | `PRMPT` | POCKET_OCR_GLYPH_AMBIGUITY | Schreibt einen Hinweis in den Statusbereich und hält das RPL-Programm an; fordert nicht selbst Text an. |
| 290 | `PROOT` | Contents-10 | `PROOT` / `171:82` | 59 | `PROOT` | POCKET_TEXT_NAME_FOUND | Ermittelt Nullstellen eines Polynoms aus der Koeffizientenliste bzw. -matrix. |
| 291 | `PRST` | Contents-10 | `PRST` / `2:242` | 59 | `PRST` | POCKET_TEXT_NAME_FOUND | Druckt alle Stackobjekte im normalen Format. |
| 292 | `PRSTC` | Contents-10 | `PRSTC` / `2:241` | 59 | `PRSTC` | POCKET_TEXT_NAME_FOUND | Druckt alle Stackobjekte in kompakter Form; keine erweiterte Darstellung. |
| 293 | `PRVAR` | Contents-10 | `PRVAR` / `2:244` | 59 | `PRVAR` | POCKET_TEXT_NAME_FOUND | Druckt den Inhalt angegebener Variablen. |
| 294 | `PR1` | Contents-11 | `PR1` / `2:240` | 59 | `PR1` | POCKET_TEXT_NAME_FOUND | Druckt ein Objekt im mehrzeiligen Format. |
| 295 | `PSDEV` | Contents-11 | `PSDEV` / `171:40` | 59 | `PSDEV` | POCKET_TEXT_NAME_FOUND | Ermittelt Populationsstandardabweichungen der Statistikspalten in ΣDAT. |
| 296 | `PURGE` | Contents-11 | `PURGE` / `2:343` | 59 | `PURGE` | POCKET_TEXT_NAME_FOUND | Löscht angegebene Variablen und leere Verzeichnisse; nicht beliebige nichtleere Verzeichnisse. |
| 297 | `PUT` | Contents-11 | `PUT` / `2:176` | 59 | `PUT` | POCKET_TEXT_NAME_FOUND | Ersetzt ein Element in einer Liste oder einem Array an der angegebenen Position. |
| 298 | `PUTI` | Contents-11 | `PUTI` / `2:177` | 59 | `PUTI` | POCKET_TEXT_NAME_FOUND | Ersetzt ein Listen- oder Arrayelement, liefert Container oder Namen und die weitergeschaltete Position. |
| 299 | `PVAR` | Contents-11 | `PVAR` / `171:41` | 59 | `PVAR` | POCKET_TEXT_NAME_FOUND | Ermittelt Populationsvarianzen der Statistikspalten in ΣDAT. |
| 300 | `PVARS` | Contents-11 | `PVARS` / `2:350` | 59 | `PVARS` | POCKET_TEXT_NAME_FOUND | Listet Objekte/Bibliotheken im angegebenen Port; meldet bei RAM-Port zusätzlich verfügbaren Speicher. |

## 3. Befunde und zu korrigierende Verwechslungen

- **#251–252 `NUMX`/`NUMY`:** Diese 3D-Perspektivparameter legen **die Zahl der x-Schritte je y-Schritt** bzw. die Anzahl der **y-Schritte im Betrachtungsvolumen** fest. Die bisherigen Kurztexte „Rastergröße in x/y-Richtung“ waren zu unscharf.
- **#253 `NΣ`:** Die Pocket-OCR liest `NZ`, ihr Inhalt meint die Anzahl Zeilen in `ΣDAT`. Keinen zusätzlichen `NZ`-Befehl als neue ROM-Funktion katalogisieren.
- **#254 `OBJ→`:** Objekttypabhängige Zerlegung; bei Arrays/Listen kommt auch ein Größen- oder Dimensionselement auf den Stack. Nicht als generisches `DROP` behandeln.
- **#257 `OLDPRT`:** Modifiziert `PRTPAR`, um den Infrarotdrucker vorzubereiten. Im Hauptkatalog war „alten Druckermodus auswählen“ zu ungenau und könnte ein nicht existierendes Betriebsmodus-Flag suggerieren.
- **#258 `OPENIO`:** Öffnet die Kommunikationsverbindung; die initiale Konfiguration von Parametern ist davon zu unterscheiden.
- **#269 `PDIM`:** Der unabhängige Guide beschreibt das Erzeugen eines **leeren GROB** gegebener Dimensionen im reservierten `PICT`. Nicht auf eine bloße Änderung des Plotmaßstabs verkürzen.
- **#274/275 `PICT`/`PICTURE`:** `PICT` liefert das aktuelle Grafikobjekt als Stackobjekt; `PICTURE` öffnet die interaktive grafische Oberfläche. Separat zählen.
- **#276 `PINIT`:** Initialisiert die aktiven Speicherports. Eine ganz andere Tätigkeit als das initiale Plotbild oder eine Statistikinitialisierung.
- **#281/282 `PMAX`/`PMIN`:** Begrenzen den PICT-Koordinatenraum (oben rechts bzw. unten links); nicht mit allgemeinen mathematischen Maximum-/Minimumfunktionen verwechseln.
- **#285 `PREDV`:** Der unabhängige Pocket Guide beschreibt es als **gleichwirkend mit `PREDY`**, wobei beide jedoch **eigene ROM-Namens-/XLIB-Kennungen** (`2:303` / `2:304`) besitzen. Deshalb *Funktionsalias* auf semantischer Ebene, **kein** Namensduplikat wie `NEXT` in A05.
- **#286/287 `PREDX`/`PREDY`:** Inverses Regressionsproblem (x aus y) gegenüber gewöhnlicher Vorhersage (y aus x), beide mit aktuellem Modell und `ΣDAT`.
- **#289 `PROMPT`:** Pocket Guide: zeigt Text im Statusbereich und **hält das laufende Programm an**. Dieser Befehl fordert nicht selbst eine Eingabe wie `INPUT` oder `INFORM` an. Die Pocket-OCR schreibt `PRMPT`; das unterscheidet keinen weiteren Befehl.
- **#291/292 `PRST`/`PRSTC`:** Regulärer Stackdruck gegenüber **kompaktem** Stackdruck. Der bisherige Katalog behauptete für `PRSTC` das Gegenteil.
- **#294 `PR1`:** Gibt ein Objekt **mehrzeilig** aus, nicht nur allgemein „druckt ein Objekt“.
- **#296 `PURGE`:** Löscht benannte Variablen und **leere** Verzeichnisse. Für das Entfernen eines kompletten Verzeichnisinhalts ist `PGDIR` gesondert zu bewerten.
- **#297/298 `PUT`/`PUTI`:** `PUTI` liefert zusätzlich den weitergeschalteten Index bzw. Container-/Namenkontext; die exakten Stackordnungen und Objekttypvarianten bleiben für die Verhaltensprüfung offen.
- **#299 `PVAR` vs. #300 `PVARS`:** Ersterer ermittelt Populationsvarianzen der Statistikdaten, Letzterer listet Speicherport-Objekte und ggf. freien Port-RAM. Diese sehr ähnlichen Namen dürfen nicht verwechselt werden.

## 4. Bilanz und Abnahmegrenzen

- **50/50** AUR-Textindexpositionen dokumentiert; **50 verschiedene gedruckte AUR-Namen**.
- **50/50** normierte 48GX-ROM-Namen mit passender XLIB-Kennung zugeordnet.
- **50/50** Pocket-Guide-Textpositionen im unabhängigen Index gefunden bzw. anhand unmittelbarer alphabetischer Position und Beschreibung zugeordnet; bei `NΣ` und `PROMPT` **Unsicherheiten der OCR-Zeichenform** ausdrücklich dokumentiert.
- **0** Original-AUR-/Pocket-Druckseiten visuell abgenommen, **0** komplette AUR-Stack-/Typ-/Flag-/Fehler-/Hardware-Kommandos zertifiziert.
- [x] Eigene Kurzbeschreibung für alle 50 Einträge.
- [x] Wesentliche Quellenabweichungen und Verwechslungsgefahren aufgenommen.
- [ ] Bildseitenkontrolle der Originaldokumente.
- [ ] Tiefenprüfung aller programmatischen und interaktiven Verhaltensvarianten.

**Checkpoint A06:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE` / `ORIGINAL_SCAN_NOT_SIGNED_OFF` / `AUR_STACK_NOT_SIGNED_OFF`. **Nächster Schritt A07: AUR-Positionen 301–350 (`PVIEW` bis `RR`).** Die globale historische Vollständigkeit bleibt ausdrücklich `HISTORICAL_COMPLETENESS_NOT_CERTIFIED`, kein V1.0-Blocker.
