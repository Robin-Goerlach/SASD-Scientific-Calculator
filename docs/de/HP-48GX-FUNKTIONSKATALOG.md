# HP 48GX – vollständiger ROM-Befehls- und Funktionskatalog

**Projekt:** SASD Scientific Calculator · **Recherche:** 21.11.2026  
**Historisches Referenzmodell:** HP 48GX der 48G-Reihe (Grundausstattung ab Werk; keine beliebig nachgerüsteten Erweiterungskarten).  
**Status:** Historische Forschungs-/Anforderungsreferenz. **Nicht** gleichbedeutend mit vorhandener SASD-Implementierung.

> **Vollständigkeit und Grenzen:** Die alphabetische Tabelle in Kapitel 3 enthält **sämtliche 517 unterschiedlichen Einträge** der aus dem HP-48GX-ROM generierten *saturnus*-Befehlsnamendatei (`48gx.json`). Dazu gehören Operatoren, Konstanten und RPL-Strukturtoken; daher sind dies **nicht** 517 mathematisch unabhängige Funktionen. Die Vollständigkeit bezieht sich auf **diesen belegten ROM-Namensindex**, nicht auf sämtliche internen System-RPL-Einstiegspunkte, jede Bediensequenz oder alle Inhalte von Fremdkarten. Ergänzende interaktive Funktionen und Grenzen sind ausdrücklich dokumentiert. Alle Kurzbeschreibungen wurden neu verfasst, nicht aus Originalhandbüchern abgeschrieben.

## 1. Modell, Funktionsumfang und Abgrenzung

- **Hardware:** Saturn-basierter Taschenrechner mit 128 KiB internem RAM, 131 × 64 Pixel monochromer Anzeige, Alpha-Tastatur, Akustik, vierpoliger serieller Schnittstelle, Infrarot, zwei Kartenslots. Der 48GX ist **nicht** identisch mit 48SX, 48G, 48G+ oder 49/50g.
- **Speicherkarten:** Geeignete Karten bis 128 KiB in Slot 1 können in den Hauptspeicher integriert werden; Slot 2 unterstützt entsprechend organisierte Karten bis 4 MiB in 128-KiB-Portsegmenten. Speicher- und Bibliothekszuordnung hängen vom Kartentyp, Port und ROM-Stand ab.
- **Objektbasierter, dynamischer RPN-Stack:** Reelle und komplexe Zahlen, binäre Ganzzahlen, Vektoren, Matrizen, Listen, Strings, algebraische Ausdrücke und Gleichungen, Programmkörper, Namen, Variablen, Einheiten, Grafikobjekte (GROBs), Bibliotheken, Verzeichnisse und Sicherungsobjekte. Ein universeller `double`-Stack oder die HP-41C-Vier-Ebenen-Semantik wäre historisch falsch.
- **Präzision und Semantik:** Reelle Zahlen intern mit zwölf Dezimalstellen, IEEE-Double-Ersatz reicht nicht für bitgenaue historische Ergebnisse. Stackordnung, Objektkoerzierung, symbolisches Verhalten, Modus-Flags, Rundung, Alarm-/I/O-Zustand und Fehler sind zum Nachbau einzeln zu spezifizieren.
- **Programme:** User-RPL, algebraische und stackorientierte Auswertung, lokale Variable, Schleifen, Fallunterscheidungen, Fehlerbehandlung, Programm- und Systemobjekte. `SYSEVAL` und `LIBEVAL` sind im Original vorhanden, aber keine Erlaubnis zu direkten Host-Speicherzugriffen.
- **Alle ROM-Einträge alphabetisch:** Kapitel 3 enthält exakt die extrahierten Namen, ihre ROM-Kennung (`Library:Command`) und verfügbare Menüpfade; nichts wird als neuer Befehl erfunden.

## 2. Funktionsbereiche, die eine reine Kommandoliste nicht erfasst

### 2.1 Bedienoberfläche, Tastatur, Anzeige und Editoren

- Ein- und Ausschalten, automatische Abschaltung, Kontrasteinstellung, Statusbereich, Annunciatoren, Speicher- und Fehlerhinweise, Menütasten und mehrstufige Untermenüs.
- Direkte Zahleneingabe mit Exponent, Vorzeichen, Dezimaltrennzeichen; Alpha-/Sonderzeicheneingabe; Objektbegrenzer, Kommandozeile, Insert/Replace, Cursor, Undo und Wiedervorlage vorheriger Kommandozeilen.
- Freies Navigieren im mehrstufigen Stack, `ENTER`, interaktive Stackbearbeitung, Wiederherstellen des letzten Stacks, `LASTARG`, Löschen und Verschieben von Objekten.
- Numerische, symbolische und algebraische Eingabe/Auswertung; Anzeige im Standard-, FIX-, SCI- oder ENG-Modus; Winkel DEG/RAD/GRAD; Rechteck-/Zylinder-/Kugelkoordinaten; Benutzer- und Systemflags.
- **EquationWriter:** zweidimensionale Formeleingabe, Klammerung, Brüche, Wurzeln, Exponenten, Teilformeln bearbeiten.
- **MatrixWriter:** tabellarische Erfassung und Bearbeitung reeller/komplexer Arrays.
- **Variable Browser:** Variablen, Verzeichnisse, Typen und Inhalte anzeigen, bearbeiten, kopieren, verschieben, löschen.
- **Picture/Plot Editor:** Pixel setzen/löschen, Linien, Bögen, Rechtecke, Bildspeicher, Bildschirmkoordinaten, Zoom, Trace, grafische Analysen und Speichern von Grafikobjekten.
- **Dialoge:** Eingabeformulare, Auswahllisten, benutzerdefinierte Menüs/Softkeys und Tastenbelegungen. Debugger mit **nichtprogrammierbaren** Bedienoperationen wie `DBUG`, `SST`, `SST↓` und Menüblättern mit `NEXT` (nicht identisch mit dem RPL-Schleifenwort).

### 2.2 Mathematik und interaktive Anwendungen

- **Reelle/komplexe Analysis:** Grundrechenarten, Potenzen/Wurzeln, Trigonometrie und Hyperbolik, Logarithmen, Grenzfall-genauere Funktionen, Kombinatorik, Prozentrechnung, Umrechnungen.
- **Symbolische Mathematik:** Ableiten, Integration, Taylorpolynome, algebraische Manipulationen, Umformungen, Gleichungen auflösen und Substitution.
- **Solver:** Numerischer Nullstellenlöser (`SOLVR`-Benutzeroberfläche), Polynomlöser, Mehrgleichungslöser, Lösungen linearer Systeme; numerische steife und nichtsteife Differentialgleichungen.
- **Matrizen/Vektoren:** Vektorprodukte, Fourier-Transformation, lineare Algebra, Eigenwerte/-vektoren, Singulärwerte, Rang/Kondition, QR/LU/LQ/Schur, kleinste Quadrate.
- **Statistik:** Dateneditor, ein-/mehrdimensionale Statistik, Summen, Histogramme, Regressionsmodelle, Wahrscheinlichkeitsverteilungen, Vorhersagen.
- **Maßeinheiten:** Rechnen mit Einheitenobjekten, dimensionsbewusste Umwandlung, Vorsätze, Temperaturen und nutzerdefinierte Einheiten; **147** eingebaute Einheitendefinitionen (Daten, keine 147 zusätzlichen Kommandos).
- **Equation Library:** ab Werk vorhanden, **über 300 Gleichungen** aus **15 Themengebieten** und über 100 Problemüberschriften; Variable-/Einheitenzuordnung, Bilder, Konstantenbibliothek, ein- und mehrdimensionale Lösungsansichten; **Minehunt** als integriertes Programm. Die 300 Formeln sind Datenbestände und nicht in die 517 Funktionsnamen einzurechnen.
- **Historische Finanzfunktionen:** `TVM`, `TVMBEG`, `TVMEND`, `TVMROOT`, `AMORT` sind **tatsächlich enthalten**. Dies ist eine historische Bestandsaufnahme; ein Finanzrechner bleibt gemäß Projektentscheidung ein getrenntes SASD-Produkt.

### 2.3 Grafik – alle Plotklassen

Funktionsplot, Polarplot, parametrischer Plot, Kegelschnitte, Wahrheitstabelle/-plot, Streudiagramm, Histogramm, Balkendiagramm, Differentialgleichungsplot, Richtungsfelder, Drahtgitter (Wireframe), Pseudokontur, Y-Schnitt, Gridmap und parametrische Fläche; Fenstergrenzen, Achsen, Beschriftung, Achsenskalierung, Cursor/Trace, Zoomen, Pixel-/Benutzerkoordinaten und 3D-Betrachtungspunkte.

### 2.4 Organisation, Hardware, Programme und Verbindungen

- Verzeichnisbaum unter HOME, Namen/Variablen, Bibliotheken und Speicherkartenports, Backupobjekte, Restore und Speicherfreigabe; lokale Variablen, User-RPL-Steuerstrukturen und anpassbare Menüs/Tasten.
- Uhr, Datum, Sekundenbasis, Alarm-/Terminverwaltung und Zeitberechnungen.
- Serielle Rechner-zu-Rechner-/PC-Übertragung über Kermit und XModem, Infrarotkommunikation zu anderen Rechnern und kompatiblen Druckern, druckbare Stackinhalte und Bildschirmbilder.
- Eingebaute Test-/Wartungsfunktionen (Tastatur, Display/Hardware, RAM-/Port- und Schnittstellentests), Kontrasteinstellungen und definierte Resetabläufe. Nicht alles ist als User-RPL-Mnemonic vorhanden.
- ROM-Versionen und besondere eingebaute Befehle `VERSION`, `RULES` (Umformungsregeln), `TEACH`/`CLTEACH` und `MINEHUNT`.

## 3. Alphabetisches Register sämtlicher 517 belegten ROM-Befehle

**Spalten:** Die Kategorie ist eine redaktionelle Einordnung, nicht notwendigerweise die HP-Menüstruktur. Die ROM-Kennung ist `Bibliotheksnummer:Kommandonummer` (mehrere Varianten mit Komma). Der Menüpfad folgt der aus der ROM-Menüstruktur abgeleiteten saturnus-Quelle. Wenn die Kurzbeschreibung noch unsicher ist, wird das ausdrücklich kenntlich gemacht. Bei typabhängigen Operationen ersetzt eine Kurzbeschreibung **nicht** das vollständige AUR-Stackdiagramm.

| ROM-Befehl | Bereich | Kurzbeschreibung | ROM-Kennung | ROM-Menüzuordnung |
| --- | --- | --- | --- | --- |
| `_` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Eingabezeichen/Begrenzer zum Kennzeichnen eines Einheitenobjekts. | `2:267` | ohne Menüeintrag |
| `-` | Grundrechnen, elementare Funktionen und Zahlen | Subtraktion. | `2:70` | ohne Menüeintrag |
| `!` | Grundrechnen, elementare Funktionen und Zahlen | Fakultät beziehungsweise Gamma-Funktion. | `2:99` | MTH PROB |
| `'` | Stack und User-RPL-Programmsteuerung | Name/algebraischen Ausdruck quotieren. | `1792:20, 1792:21` | ohne Menüeintrag |
| `«` | Stack und User-RPL-Programmsteuerung | RPL-Programmobjekt beginnen. | `1792:18` | ohne Menüeintrag |
| `»` | Stack und User-RPL-Programmsteuerung | RPL-Programmobjekt beenden. | `1792:17, 1792:19` | ohne Menüeintrag |
| `*` | Grundrechnen, elementare Funktionen und Zahlen | Multiplikation. | `2:71` | ohne Menüeintrag |
| `*H` | Grafik, Diagramme und Plotparameter | Vertikale Plot-Skalierung ändern. | `2:189` | ohne Menüeintrag |
| `*W` | Grafik, Diagramme und Plotparameter | Horizontale Plot-Skalierung ändern. | `2:190` | ohne Menüeintrag |
| `/` | Grundrechnen, elementare Funktionen und Zahlen | Division. | `2:72` | MENU 74 SYS |
| `%` | Grundrechnen, elementare Funktionen und Zahlen | Prozentwert. | `2:124` | MTH REAL |
| `%CH` | Grundrechnen, elementare Funktionen und Zahlen | Prozentuale Änderung. | `2:126` | MTH REAL |
| `%T` | Grundrechnen, elementare Funktionen und Zahlen | Prozentualer Anteil am Ganzen. | `2:125` | MTH REAL |
| `^` | Grundrechnen, elementare Funktionen und Zahlen | Potenzierung. | `2:73` | ohne Menüeintrag |
| `→` | Stack und User-RPL-Programmsteuerung | Lokale Variablen binden. | `1792:4, 1792:16` | ohne Menüeintrag |
| `→ARRY` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Array aus Stackelementen bilden. | `2:170` | PRG TYPE |
| `→COL` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Aus Spalten ein Array bilden. | `171:67` | MTH MATRX COL |
| `→DATE` | Zeit, Kalender, Wecker | Datum setzen. | `2:22` | MENU 94 |
| `→DIAG` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Diagonalmatrix bilden. | `171:69` | MTH MATRX |
| `→GROB` | Grafik, Diagramme und Plotparameter | Objekt als Grafikobjekt darstellen. | `2:215` | PRG GROB |
| `→HMS` | Grundrechnen, elementare Funktionen und Zahlen | Dezimalzeit in Stunden-Minuten-Sekunden-Darstellung. | `2:114` | MENU 94 |
| `→LCD` | Grafik, Diagramme und Plotparameter | Grafikobjekt auf LCD darstellen. | `2:214` | PRG GROB |
| `→LIST` | Listen, Strings, Objektkonversion | Liste aus Stackobjekten erzeugen. | `2:152` | PRG TYPE; PRG LIST |
| `→NUM` | Stack und User-RPL-Programmsteuerung | Numerische Auswertung erzwingen. | `2:53` | ohne Menüeintrag |
| `→Q` | Symbolische Mathematik, Solver und Differentialgleichungen | Wandelt eine Zahl in einen äquivalenten rationalen Bruch um. | `2:263` | MENU 93 |
| `→Qπ` | Symbolische Mathematik, Solver und Differentialgleichungen | Wählt zwischen einer rationalen Näherung der Zahl und einem rationalen Vielfachen von π nach kleinerem Nenner. | `2:264` | MENU 93 |
| `→ROW` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Aus Zeilen ein Array bilden. | `171:65` | MTH MATRX ROW |
| `→STR` | Listen, Strings, Objektkonversion | Objekt in Text umwandeln. | `2:162` | PRG TYPE; MENU 62 |
| `→TAG` | Listen, Strings, Objektkonversion | Objekt mit Text-Tag versehen. | `2:383` | PRG TYPE |
| `→TIME` | Zeit, Kalender, Wecker | Uhrzeit setzen. | `2:23` | MENU 94 |
| `→UNIT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Zahlenwert mit Einheit verbinden. | `2:13` | PRG TYPE; MENU 59 |
| `→V2` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zweidimensionalen Vektor aufbauen. | `2:181` | MTH VECTR |
| `→V3` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Dreidimensionalen Vektor aufbauen. | `2:182` | MTH VECTR |
| `↑MATCH` | Symbolische Mathematik, Solver und Differentialgleichungen | Musterabgleich mit Ersetzung vom Teilausdruck aus. | `2:265` | MENU 93 |
| `↓MATCH` | Symbolische Mathematik, Solver und Differentialgleichungen | Musterabgleich mit Ersetzung vom Gesamtausdruck aus. | `2:266` | MENU 93 |
| `∂` | Symbolische Mathematik, Solver und Differentialgleichungen | Symbolische Differentiation. | `2:247, 2:248` | ohne Menüeintrag |
| `+` | Grundrechnen, elementare Funktionen und Zahlen | Addition. | `2:68, 2:69` | ohne Menüeintrag |
| `<` | Binärzahlen, Logik, Modi, Systemflags | Kleiner-Vergleich. | `2:235` | PRG TEST |
| `=` | Binärzahlen, Logik, Modi, Systemflags | Algebraischer Gleichheitsoperator. | `2:59` | ohne Menüeintrag |
| `≠` | Binärzahlen, Logik, Modi, Systemflags | Ungleichheitsvergleich. | `2:234` | PRG TEST |
| `==` | Binärzahlen, Logik, Modi, Systemflags | Gleichheitsvergleich. | `2:233` | PRG TEST |
| `>` | Binärzahlen, Logik, Modi, Systemflags | Größer-Vergleich. | `2:236` | PRG TEST |
| `\|` | Symbolische Mathematik, Solver und Differentialgleichungen | Algebraische Substitution unter einer Bedingung. | `2:255, 2:256` | MENU 93 |
| `√` | Grundrechnen, elementare Funktionen und Zahlen | Quadratwurzel. | `2:79` | ohne Menüeintrag |
| `∫` | Symbolische Mathematik, Solver und Differentialgleichungen | Integration. | `2:252, 2:253` | ohne Menüeintrag |
| `≤` | Binärzahlen, Logik, Modi, Systemflags | Kleiner-gleich-Vergleich. | `2:237` | PRG TEST |
| `≥` | Binärzahlen, Logik, Modi, Systemflags | Größer-gleich-Vergleich. | `2:238` | PRG TEST |
| `ABS` | Grundrechnen, elementare Funktionen und Zahlen | Betrag beziehungsweise Norm. | `2:61` | MTH VECTR; MTH MATRX NORM; MTH REAL; MTH CMPLX |
| `ACK` | Zeit, Kalender, Wecker | Ältesten fälligen Alarm quittieren. | `2:21` | MENU 94 ALRM |
| `ACKALL` | Zeit, Kalender, Wecker | Alle fälligen Alarme quittieren. | `2:20` | MENU 94 ALRM |
| `ACOS` | Grundrechnen, elementare Funktionen und Zahlen | Arkuskosinus. | `2:88` | ohne Menüeintrag |
| `ACOSH` | Grundrechnen, elementare Funktionen und Zahlen | Inverser Cosinus hyperbolicus. | `2:91` | MTH HYP |
| `ADD` | Listen, Strings, Objektkonversion | Addiert zwei Listen elementweise. | `171:108` | MTH LIST |
| `ALOG` | Grundrechnen, elementare Funktionen und Zahlen | 10 hoch x. | `2:96` | ohne Menüeintrag |
| `AMORT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Tilgungsrechnung. | `171:89` | MENU 74 TVM; MENU 74 TVM SOLVR |
| `AND` | Binärzahlen, Logik, Modi, Systemflags | Logisches/bitweises UND. | `2:229` | MTH BASE LOGIC; PRG TEST |
| `ANIMATE` | Grafik, Diagramme und Plotparameter | Grafikobjektfolge animieren. | `171:24` | PRG GROB |
| `APPLY` | Symbolische Mathematik, Solver und Differentialgleichungen | Algebraischen Funktionsaufruf zusammensetzen. | `2:258, 2:259` | MENU 93 |
| `ARC` | Grafik, Diagramme und Plotparameter | Kreisbogen zeichnen. | `2:216` | PRG PICT |
| `ARCHIVE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | HOME-Verzeichnisbaum als Backup sichern. | `2:352` | MENU 70 |
| `ARG` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Winkel einer komplexen Zahl. | `2:77` | MTH CMPLX |
| `ARRY→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Array in Stackelemente zerlegen. | `2:171` | ohne Menüeintrag |
| `ASIN` | Grundrechnen, elementare Funktionen und Zahlen | Arkussinus. | `2:87` | ohne Menüeintrag |
| `ASINH` | Grundrechnen, elementare Funktionen und Zahlen | Inverser Sinus hyperbolicus. | `2:90` | MTH HYP |
| `ASN` | Schnittstellen, Drucker, Display und Tastenbelegung | Funktion/Objekt einer Taste zuordnen. | `2:379` | MENU 63 KEYS |
| `ASR` | Binärzahlen, Logik, Modi, Systemflags | Arithmetisch nach rechts schieben. | `2:0` | MTH BASE BIT |
| `ATAN` | Grundrechnen, elementare Funktionen und Zahlen | Arkustangens. | `2:89` | ohne Menüeintrag |
| `ATANH` | Grundrechnen, elementare Funktionen und Zahlen | Inverser Tangens hyperbolicus. | `2:92` | MTH HYP |
| `ATICK` | Grafik, Diagramme und Plotparameter | Achsenticks festlegen. | `171:16` | ohne Menüeintrag |
| `ATTACH` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Bibliothek anhängen. | `2:357` | MENU 110 |
| `AUTO` | Grafik, Diagramme und Plotparameter | Plotbereich automatisch bestimmen. | `2:192` | ohne Menüeintrag |
| `AXES` | Grafik, Diagramme und Plotparameter | Position der Plotachsen festlegen. | `2:186` | ohne Menüeintrag |
| `B→R` | Binärzahlen, Logik, Modi, Systemflags | Binäre Ganzzahl nach reell. | `2:10` | MTH BASE |
| `BAR` | Grafik, Diagramme und Plotparameter | Balkendiagramm aktivieren. | `2:227` | ohne Menüeintrag |
| `BARPLOT` | Grafik, Diagramme und Plotparameter | Balkendiagramm erstellen. | `2:316` | MENU 96 PLOT |
| `BAUD` | Schnittstellen, Drucker, Display und Tastenbelegung | Baudrate konfigurieren. | `2:370` | ohne Menüeintrag |
| `BEEP` | Schnittstellen, Drucker, Display und Tastenbelegung | Ton erzeugen. | `2:52` | PRG OUT |
| `BESTFIT` | Statistik, Verteilungen und Regression | Bestes Fit-Modell auswählen. | `2:323` | ohne Menüeintrag |
| `BIN` | Binärzahlen, Logik, Modi, Systemflags | Binäre Anzeigeform. | `2:144` | MTH BASE |
| `BINS` | Statistik, Verteilungen und Regression | Daten für Histogramm klassieren. | `2:315` | MENU 96 1VAR |
| `BLANK` | Grafik, Diagramme und Plotparameter | Leeres Grafikobjekt erzeugen. | `2:209` | PRG GROB |
| `BOX` | Grafik, Diagramme und Plotparameter | Rechteck zeichnen. | `2:208` | PRG PICT |
| `BUFLEN` | Schnittstellen, Drucker, Display und Tastenbelegung | Länge des Eingabepuffers. | `2:374` | MENU 104 SERIAL |
| `BYTES` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Speichergröße und Prüfsumme eines Objekts ermitteln. | `2:38` | MENU 70 |
| `C→PX` | Grafik, Diagramme und Plotparameter | Benutzerkoordinaten in Pixelkoordinaten wandeln. | `2:199` | PRG PICT |
| `C→R` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Komplexe Zahl in Komponenten zerlegen. | `2:159` | MTH CMPLX; PRG TYPE |
| `CASE` | Stack und User-RPL-Programmsteuerung | Fallunterscheidung beginnen. | `1792:25` | PRG BRCH CASE |
| `CEIL` | Grundrechnen, elementare Funktionen und Zahlen | Aufrunden zur nächsten ganzen Zahl. | `2:104` | MTH REAL |
| `CENTR` | Grafik, Diagramme und Plotparameter | Plotansicht zentrieren. | `2:187` | ohne Menüeintrag |
| `CF` | Binärzahlen, Logik, Modi, Systemflags | Flag löschen. | `2:132` | PRG TEST; MENU 63 FLAG |
| `CHOOSE` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Auswahlliste anzeigen. | `171:92` | PRG IN |
| `CHR` | Listen, Strings, Objektkonversion | Zeichen aus Zeichencode erzeugen. | `2:165` | PRG TYPE; MENU 62 |
| `CKSM` | Schnittstellen, Drucker, Display und Tastenbelegung | Prüfsumme erzeugen. | `2:369` | ohne Menüeintrag |
| `CLEAR` | Stack und User-RPL-Programmsteuerung | Stack leeren. | `2:282` | ohne Menüeintrag |
| `CLKADJ` | Zeit, Kalender, Wecker | Uhrengang anpassen. | `2:24` | MENU 94 |
| `CLLCD` | Schnittstellen, Drucker, Display und Tastenbelegung | LCD-Inhalt löschen. | `2:56` | PRG OUT |
| `CLOSEIO` | Schnittstellen, Drucker, Display und Tastenbelegung | Ein-/Ausgabe schließen. | `2:362` | MENU 104 |
| `CLTEACH` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Lehrbeispielobjekte entfernen. | `171:18` | ohne Menüeintrag |
| `CLVAR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variablen löschen. | `2:346` | ohne Menüeintrag |
| `CLΣ` | Statistik, Verteilungen und Regression | Statistische Daten löschen. | `2:284` | MENU 87 DATA; MENU 96 DATA |
| `CNRM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Spaltennorm einer Matrix. | `2:119` | MTH MATRX NORM |
| `COL-` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Spalte entfernen. | `171:73` | MTH MATRX COL |
| `COL→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Array in Spalten zerlegen. | `171:68` | MTH MATRX COL |
| `COL+` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Spalte einfügen. | `171:74` | MTH MATRX COL |
| `COLCT` | Symbolische Mathematik, Solver und Differentialgleichungen | Algebraischen Ausdruck zusammenfassen. | `2:333` | MENU 93 |
| `COLΣ` | Statistik, Verteilungen und Regression | Spaltensumme. | `2:312` | ohne Menüeintrag |
| `COMB` | Grundrechnen, elementare Funktionen und Zahlen | Kombinationen berechnen. | `2:129` | MTH PROB |
| `CON` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Mit einem konstanten Wert gefülltes Array bilden. | `2:173` | MTH MATRX MAKE |
| `COND` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Konditionszahl bestimmen. | `171:49` | MTH MATRX NORM |
| `CONIC` | Grafik, Diagramme und Plotparameter | Kegelschnittplot aktivieren. | `2:221` | ohne Menüeintrag |
| `CONJ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Komplexe Konjugation. | `2:62` | MTH CMPLX |
| `CONLIB` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Konstantenbibliothek starten. | `171:32` | MENU 113 COLIB |
| `CONST` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Physikalische Konstante auswählen. | `171:33` | MENU 113 COLIB |
| `CONT` | Stack und User-RPL-Programmsteuerung | Angehaltenes Programm fortsetzen. | `2:58` | ohne Menüeintrag |
| `CONVERT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Maßeinheit umrechnen. | `2:11` | MENU 59 |
| `CORR` | Statistik, Verteilungen und Regression | Korrelationskoeffizient. | `2:289` | MENU 96 FIT |
| `COS` | Grundrechnen, elementare Funktionen und Zahlen | Kosinus. | `2:82` | ohne Menüeintrag |
| `COSH` | Grundrechnen, elementare Funktionen und Zahlen | Cosinus hyperbolicus. | `2:85` | MTH HYP |
| `COV` | Statistik, Verteilungen und Regression | Stichprobenkovarianz. | `2:290` | MENU 96 FIT |
| `CR` | Schnittstellen, Drucker, Display und Tastenbelegung | Zeilenumbruch beim Drucken. | `2:243` | MENU 104 PRINT |
| `CRDIR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Unterverzeichnis erstellen. | `2:32` | MENU 70 DIR |
| `CROSS` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Kreuzprodukt. | `2:122` | MTH VECTR |
| `CSWP` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Spalten vertauschen. | `171:76` | MTH MATRX COL |
| `CYLIN` | Binärzahlen, Logik, Modi, Systemflags | Zylindrischer Koordinatenmodus. | `171:20` | MTH VECTR; MENU 63 ANGLE |
| `D→R` | Grundrechnen, elementare Funktionen und Zahlen | Gradmaß nach Bogenmaß umrechnen. | `2:112` | MTH REAL |
| `DARCY` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Darcy-Reibungsbeiwert berechnen. | `171:120` | MENU 113 UTILS |
| `DATE` | Zeit, Kalender, Wecker | Aktuelles Datum lesen. | `2:17` | MENU 94 |
| `DATE+` | Zeit, Kalender, Wecker | Tage zu Datum addieren. | `2:31` | MENU 94 |
| `dB` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Dezibel-Hilfsfunktion. | `171:128` | MENU 113 UTILS |
| `DDAYS` | Zeit, Kalender, Wecker | Tage zwischen Daten ermitteln. | `2:30` | MENU 94 |
| `DEC` | Binärzahlen, Logik, Modi, Systemflags | Dezimale Anzeigeform. | `2:145` | MTH BASE |
| `DECR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Verringert den Inhalt einer benannten Variablen um eins. | `2:332` | MENU 70 ARITH |
| `DEFINE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Benutzerdefinierte Funktion definieren. | `2:342` | ohne Menüeintrag |
| `DEG` | Binärzahlen, Logik, Modi, Systemflags | Winkelmodus Grad. | `2:135` | MENU 63 ANGLE |
| `DELALARM` | Zeit, Kalender, Wecker | Wecker löschen. | `2:28` | MENU 94 ALRM |
| `DELAY` | Schnittstellen, Drucker, Display und Tastenbelegung | Druckverzögerung einstellen. | `2:245` | ohne Menüeintrag |
| `DELKEYS` | Schnittstellen, Drucker, Display und Tastenbelegung | Benutzer-Tastenbelegung entfernen. | `2:381` | MENU 63 KEYS |
| `DEPND` | Grafik, Diagramme und Plotparameter | Abhängige Plotvariable festlegen. | `2:196` | ohne Menüeintrag |
| `DEPTH` | Stack und User-RPL-Programmsteuerung | Stacktiefe lesen. | `2:276` | MENU 73 |
| `DET` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Determinante. | `2:120` | MTH MATRX NORM |
| `DETACH` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Bibliothek abhängen. | `2:358` | MENU 110 |
| `DIAG→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Matrixdiagonale extrahieren. | `171:70` | MTH MATRX |
| `DIFFEQ` | Grafik, Diagramme und Plotparameter | Differentialgleichungsplot aktivieren. | `171:14` | ohne Menüeintrag |
| `DIR` | Stack und User-RPL-Programmsteuerung | Verzeichnisobjekt beginnen. | `1792:27` | ohne Menüeintrag |
| `DISP` | Schnittstellen, Drucker, Display und Tastenbelegung | Objekt in LCD-Zeile anzeigen. | `2:50` | PRG OUT |
| `DO` | Stack und User-RPL-Programmsteuerung | DO-Schleife beginnen. | `1792:7` | PRG BRCH DO |
| `DOERR` | Stack und User-RPL-Programmsteuerung | Fehler auslösen. | `2:42` | PRG ERROR |
| `DOLIST` | Listen, Strings, Objektkonversion | Programm auf Listenelemente anwenden. | `171:107` | PRG LIST PROC |
| `DOSUBS` | Listen, Strings, Objektkonversion | Teilfolgen verarbeiten. | `171:99` | PRG LIST PROC |
| `DOT` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Skalarprodukt. | `2:121` | MTH VECTR |
| `DRAW` | Grafik, Diagramme und Plotparameter | Aktuelles Diagramm zeichnen. | `2:191` | ohne Menüeintrag |
| `DRAX` | Grafik, Diagramme und Plotparameter | Koordinatenachsen zeichnen. | `2:193` | ohne Menüeintrag |
| `DROP` | Stack und User-RPL-Programmsteuerung | Oberstes Stackelement löschen. | `2:272` | ohne Menüeintrag |
| `DROP2` | Stack und User-RPL-Programmsteuerung | Zwei oberste Stackelemente löschen. | `2:273` | MENU 73 |
| `DROPN` | Stack und User-RPL-Programmsteuerung | Mehrere Stackelemente löschen. | `2:277` | MENU 73 |
| `DTAG` | Listen, Strings, Objektkonversion | Text-Tag entfernen. | `2:384` | PRG TYPE |
| `DUP` | Stack und User-RPL-Programmsteuerung | Stackelement duplizieren. | `2:269` | MENU 73 |
| `DUP2` | Stack und User-RPL-Programmsteuerung | Oberste zwei Stackelemente duplizieren. | `2:270` | MENU 73 |
| `DUPN` | Stack und User-RPL-Programmsteuerung | Mehrere Stackelemente duplizieren. | `2:278` | MENU 73 |
| `e` | Grundrechnen, elementare Funktionen und Zahlen | Symbolische Eulersche Zahl. | `2:66` | MTH CONST |
| `EGV` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Eigenvektoren. | `171:55` | MTH MATRX |
| `EGVL` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Eigenwerte. | `171:56` | MTH MATRX |
| `ELSE` | Stack und User-RPL-Programmsteuerung | Alternativzweig beginnen. | `1792:2` | PRG BRCH IF; PRG ERROR IFERR |
| `END` | Stack und User-RPL-Programmsteuerung | Kontrollstruktur abschließen. | `1792:3, 1792:22, 1792:23` | PRG BRCH IF; PRG BRCH CASE; PRG BRCH DO; PRG BRCH WHILE; PRG ERROR IFERR |
| `ENDSUB` | Listen, Strings, Objektkonversion | Verarbeitung von Teilfolgen beenden. | `171:102` | PRG LIST PROC |
| `ENG` | Binärzahlen, Logik, Modi, Systemflags | Technisches Format. | `2:140` | MENU 63 FMT |
| `EQ→` | Listen, Strings, Objektkonversion | Zerlegt eine Gleichung in die linke und rechte Seite. | `2:168` | PRG TYPE |
| `EQNLIB` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Eingebaute Gleichungsbibliothek öffnen. | `171:34` | MENU 113 EQLIB |
| `ERASE` | Grafik, Diagramme und Plotparameter | Bildspeicher löschen. | `2:197` | ohne Menüeintrag |
| `ERR0` | Stack und User-RPL-Programmsteuerung | Letzten Fehler löschen. | `2:43` | PRG ERROR |
| `ERRM` | Stack und User-RPL-Programmsteuerung | Letzte Fehlermeldung lesen. | `2:45` | PRG ERROR |
| `ERRN` | Stack und User-RPL-Programmsteuerung | Letzte Fehlernummer lesen. | `2:44` | PRG ERROR |
| `EVAL` | Stack und User-RPL-Programmsteuerung | Objekt auswerten. | `2:46` | ohne Menüeintrag |
| `EXP` | Grundrechnen, elementare Funktionen und Zahlen | e hoch x. | `2:93` | ohne Menüeintrag |
| `EXPAN` | Symbolische Mathematik, Solver und Differentialgleichungen | Algebraischen Ausdruck expandieren. | `2:334` | MENU 93 |
| `EXPFIT` | Statistik, Verteilungen und Regression | Exponentielles Fit-Modell wählen. | `2:321` | ohne Menüeintrag |
| `EXPM` | Grundrechnen, elementare Funktionen und Zahlen | Berechnet exp(x) minus 1 mit besonderer Genauigkeit. | `2:98` | MTH HYP |
| `EYEPT` | Grafik, Diagramme und Plotparameter | Standpunkt für 3D-Betrachtung. | `171:5` | ohne Menüeintrag |
| `F0λ` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Schwarzkörper-Strahlungsanteil berechnen. | `171:121` | MENU 113 UTILS |
| `FACT` | Grundrechnen, elementare Funktionen und Zahlen | Fakultät berechnen; synonym zu !, keine Primfaktorzerlegung. | `2:100` | ohne Menüeintrag |
| `FANNING` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Fanning-Reibungsbeiwert berechnen. | `171:119` | MENU 113 UTILS |
| `FC?` | Binärzahlen, Logik, Modi, Systemflags | Testen ob Flag gelöscht ist. | `2:134` | PRG TEST; MENU 63 FLAG |
| `FC?C` | Binärzahlen, Logik, Modi, Systemflags | Flag testen und löschen. | `2:143` | PRG TEST; MENU 63 FLAG |
| `FFT` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Schnelle Fourier-Transformation. | `171:37` | MTH FFT |
| `FINDALARM` | Zeit, Kalender, Wecker | Wecker suchen. | `2:27` | MENU 94 ALRM |
| `FINISH` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Servermodus verlassen. | `2:367` | MENU 104 SRVR |
| `FIX` | Binärzahlen, Logik, Modi, Systemflags | Festkommaformat. | `2:138` | MENU 63 FMT |
| `FLOOR` | Grundrechnen, elementare Funktionen und Zahlen | Abrunden zur nächsten ganzen Zahl. | `2:103` | MTH REAL |
| `FOR` | Stack und User-RPL-Programmsteuerung | Zählschleife mit benannter Zählvariable. | `1792:10` | PRG BRCH FOR |
| `FP` | Grundrechnen, elementare Funktionen und Zahlen | Gebrochener Anteil. | `2:102` | MTH REAL |
| `FREE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Eingebundenen Kartenspeicher freigeben. | `2:355` | ohne Menüeintrag |
| `FREE1` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Eingebundenen Port-1-Speicher freigeben. | `171:23` | MENU 110 |
| `FREEZE` | Schnittstellen, Drucker, Display und Tastenbelegung | LCD-Bereiche einfrieren. | `2:51` | PRG OUT |
| `FS?` | Binärzahlen, Logik, Modi, Systemflags | Testen ob Flag gesetzt ist. | `2:133` | PRG TEST; MENU 63 FLAG |
| `FS?C` | Binärzahlen, Logik, Modi, Systemflags | Flag testen und löschen. | `2:142` | PRG TEST; MENU 63 FLAG |
| `FUNCTION` | Grafik, Diagramme und Plotparameter | Funktionsplot aktivieren. | `2:220` | ohne Menüeintrag |
| `GET` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element an einer Position lesen. | `2:178` | MTH MATRX MAKE; PRG LIST ELEM |
| `GETI` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element lesen und Index erhöhen. | `2:179` | MTH MATRX MAKE; PRG LIST ELEM |
| `gmol` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Mol-Einheit auf Gramm-Basis. | `171:125` | MENU 113 UTILS |
| `GOR` | Grafik, Diagramme und Plotparameter | Grafikobjekte per OR überlagern. | `2:211` | PRG GROB |
| `GRAD` | Binärzahlen, Logik, Modi, Systemflags | Winkelmodus Gon. | `2:137` | MENU 63 ANGLE |
| `GRIDMAP` | Grafik, Diagramme und Plotparameter | 3D-Gitterabbildung aktivieren. | `171:10` | ohne Menüeintrag |
| `GXOR` | Grafik, Diagramme und Plotparameter | Grafikobjekte per XOR überlagern. | `2:212` | PRG GROB |
| `HALT` | Stack und User-RPL-Programmsteuerung | Programmausführung anhalten. | `1792:14` | PRG RUN |
| `HEAD` | Listen, Strings, Objektkonversion | Erstes Listenelement. | `171:96` | PRG LIST ELEM; MENU 62 |
| `HEX` | Binärzahlen, Logik, Modi, Systemflags | Hexadezimale Anzeigeform. | `2:146` | MTH BASE |
| `HISTOGRAM` | Grafik, Diagramme und Plotparameter | Histogramm aktivieren. | `2:226` | ohne Menüeintrag |
| `HISTPLOT` | Grafik, Diagramme und Plotparameter | Histogramm erstellen. | `2:317` | MENU 96 PLOT |
| `HMS-` | Grundrechnen, elementare Funktionen und Zahlen | Zeitwerte im H.MMSS-Format subtrahieren. | `2:117` | MENU 94 |
| `HMS→` | Grundrechnen, elementare Funktionen und Zahlen | Stunden-Minuten-Sekunden nach Dezimalzeit. | `2:115` | MENU 94 |
| `HMS+` | Grundrechnen, elementare Funktionen und Zahlen | Zeitwerte im H.MMSS-Format addieren. | `2:116` | MENU 94 |
| `HOME` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | HOME-Verzeichnis wählen. | `2:34` | ohne Menüeintrag |
| `i` | Grundrechnen, elementare Funktionen und Zahlen | Symbolische imaginäre Einheit. | `2:67` | MTH CONST |
| `IDN` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Einheitsmatrix erzeugen. | `2:174` | MTH MATRX MAKE |
| `IF` | Stack und User-RPL-Programmsteuerung | Bedingte Programmverzweigung beginnen. | `1792:0` | PRG BRCH IF |
| `IFERR` | Stack und User-RPL-Programmsteuerung | Fehlerbehandlungsstruktur beginnen. | `1792:13` | PRG ERROR IFERR |
| `IFFT` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Inverse schnelle Fourier-Transformation. | `171:38` | MTH FFT |
| `IFT` | Stack und User-RPL-Programmsteuerung | Objekt bedingt ausführen. | `2:48` | PRG BRCH |
| `IFTE` | Stack und User-RPL-Programmsteuerung | Bedingt zwischen zwei Objekten auswählen. | `2:47` | PRG BRCH |
| `IM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Imaginärteil. | `2:155` | MTH CMPLX |
| `INCR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Erhöht den Inhalt einer benannten Variablen um eins. | `2:331` | MENU 70 ARITH |
| `INDEP` | Grafik, Diagramme und Plotparameter | Unabhängige Plotvariable festlegen. | `2:183` | ohne Menüeintrag |
| `INFORM` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Eingabeformular anzeigen. | `171:90` | PRG IN |
| `INPUT` | Stack und User-RPL-Programmsteuerung | Eingabe in der Kommandozeile anfordern. | `2:378` | PRG IN |
| `INV` | Grundrechnen, elementare Funktionen und Zahlen | Kehrwert bzw. Matrixinverse. | `2:76` | ohne Menüeintrag |
| `IP` | Grundrechnen, elementare Funktionen und Zahlen | Ganzzahliger Anteil. | `2:101` | MTH REAL |
| `ISOL` | Symbolische Mathematik, Solver und Differentialgleichungen | Gleichung nach einer Variablen auflösen. | `2:336` | MENU 93 |
| `KERRM` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Fehler lesen. | `2:373` | MENU 104 |
| `KEY` | Stack und User-RPL-Programmsteuerung | Tastenzustand lesen. | `2:57` | PRG IN |
| `KGET` | Schnittstellen, Drucker, Display und Tastenbelegung | Daten von Kermit-Server anfordern. | `2:364` | MENU 104 SRVR |
| `KILL` | Stack und User-RPL-Programmsteuerung | Angehaltenes Programm beenden. | `2:40` | PRG RUN |
| `LABEL` | Grafik, Diagramme und Plotparameter | Achsenbeschriftungen setzen. | `2:201` | ohne Menüeintrag |
| `LASTARG` | Stack und User-RPL-Programmsteuerung | Letzte Argumente wiederherstellen. | `2:54` | PRG ERROR |
| `lbmol` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Mol-Einheit auf Pfund-Basis. | `171:126` | MENU 113 UTILS |
| `LCD→` | Grafik, Diagramme und Plotparameter | LCD-Daten als Grafikobjekt lesen. | `2:213` | PRG GROB |
| `LIBEVAL` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Bibliotheksfunktion per XLIB-ID ausführen. | `171:30` | ohne Menüeintrag |
| `LIBS` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Bibliotheken auflisten. | `2:356` | MENU 110 |
| `LINE` | Grafik, Diagramme und Plotparameter | Linie zeichnen. | `2:206` | PRG PICT |
| `LINFIT` | Statistik, Verteilungen und Regression | Lineares Fit-Modell wählen. | `2:319` | ohne Menüeintrag |
| `LININ` | Symbolische Mathematik, Solver und Differentialgleichungen | Prüft, ob ein algebraischer Ausdruck hinsichtlich einer angegebenen Variablen linear ist. | `171:28` | PRG TEST |
| `LIST→` | Listen, Strings, Objektkonversion | Liste in Stackobjekte zerlegen. | `2:158` | ohne Menüeintrag |
| `LN` | Grundrechnen, elementare Funktionen und Zahlen | Natürlicher Logarithmus. | `2:94` | ohne Menüeintrag |
| `LNP1` | Grundrechnen, elementare Funktionen und Zahlen | Berechnet ln(1+x) mit besonderer Genauigkeit. | `2:97` | MTH HYP |
| `LOG` | Grundrechnen, elementare Funktionen und Zahlen | Zehnerlogarithmus. | `2:95` | ohne Menüeintrag |
| `LOGFIT` | Statistik, Verteilungen und Regression | Logarithmisches Fit-Modell wählen. | `2:320` | ohne Menüeintrag |
| `LQ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | LQ-Faktorisierung. | `171:61` | MTH MATRX FACTR |
| `LR` | Statistik, Verteilungen und Regression | Lineare Regression. | `2:302` | MENU 96 FIT |
| `LSQ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Ausgleichsrechnung nach kleinsten Quadraten. | `171:54` | MTH MATRX; MENU 74 SYS |
| `LU` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | LU-Zerlegung. | `171:59` | MTH MATRX FACTR |
| `MANT` | Grundrechnen, elementare Funktionen und Zahlen | Mantisse einer Zahl. | `2:111` | MTH REAL |
| `MAX` | Grundrechnen, elementare Funktionen und Zahlen | Maximum zweier Zahlen. | `2:106` | MTH REAL |
| `MAXR` | Grundrechnen, elementare Funktionen und Zahlen | Konstante: größter darstellbarer reeller Wert. | `2:64` | MTH CONST |
| `MAXΣ` | Statistik, Verteilungen und Regression | Größter statistischer Datenwert. | `2:296` | MENU 96 1VAR |
| `MCALC` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Solver-Variable zur Berechnung markieren. | `171:115` | MENU 113 MES |
| `MEAN` | Statistik, Verteilungen und Regression | Mittelwert. | `2:297` | MENU 96 1VAR |
| `MEM` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Freien Benutzerspeicher abfragen. | `2:344` | MENU 70 |
| `MENU` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Menü auswählen. | `2:348` | MENU 63 MENU |
| `MERGE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Kartenspeicher in Benutzerspeicher einbinden. | `2:354` | ohne Menüeintrag |
| `MERGE1` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Geeigneten Port-1-Speicher einbinden. | `171:22` | MENU 110 |
| `MIN` | Grundrechnen, elementare Funktionen und Zahlen | Minimum zweier Zahlen. | `2:107` | MTH REAL |
| `MINEHUNT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Integriertes Minehunt-Spiel. | `171:117` | MENU 113 UTILS |
| `MINIT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Mehrgleichungslöser initialisieren. | `171:112` | MENU 113 MES |
| `MINR` | Grundrechnen, elementare Funktionen und Zahlen | Konstante: kleinster positiver reeller Wert. | `2:65` | MTH CONST |
| `MINΣ` | Statistik, Verteilungen und Regression | Kleinster statistischer Datenwert. | `2:298` | MENU 96 1VAR |
| `MITM` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Titel und Menü des Mehrgleichungslösers anpassen. | `171:113` | MENU 113 MES |
| `MOD` | Grundrechnen, elementare Funktionen und Zahlen | Modulo/Divisionsrest. | `2:110` | MTH REAL |
| `MROOT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Solver-Unbekannte bestimmen. | `171:116` | MENU 113 MES |
| `MSGBOX` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Meldungsfenster anzeigen. | `171:93` | PRG OUT |
| `MSOLVR` | Symbolische Mathematik, Solver und Differentialgleichungen | Mehrgleichungslöser aufrufen. | `171:36, 171:111` | MENU 113 EQLIB; MENU 113 MES |
| `MUSER` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Solver-Variable als Benutzervorgabe markieren. | `171:114` | MENU 113 MES |
| `NDIST` | Statistik, Verteilungen und Regression | Dichte der Normalverteilung. | `171:39` | MTH PROB |
| `NEG` | Grundrechnen, elementare Funktionen und Zahlen | Vorzeichenwechsel. | `2:60` | MTH CMPLX |
| `NEWOB` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Neue Objektkopie erstellen. | `2:39` | MENU 70 |
| `NEXT` | Stack und User-RPL-Programmsteuerung | Zählschleife wiederholen. | `1792:11` | PRG BRCH START; PRG BRCH FOR |
| `NOT` | Binärzahlen, Logik, Modi, Systemflags | Logische/bitweise Negation. | `2:231` | MTH BASE LOGIC; PRG TEST |
| `NOVAL` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Wert fehlt/ist nicht festgelegt. | `171:91` | PRG IN |
| `NSUB` | Listen, Strings, Objektkonversion | Anzahl von Teilfolgen. | `171:101` | PRG LIST PROC |
| `NUM` | Listen, Strings, Objektkonversion | Zeichencode ermitteln. | `2:164` | PRG TYPE; MENU 62 |
| `NUMX` | Grafik, Diagramme und Plotparameter | Rastergröße in x-Richtung. | `171:6` | ohne Menüeintrag |
| `NUMY` | Grafik, Diagramme und Plotparameter | Rastergröße in y-Richtung. | `171:7` | ohne Menüeintrag |
| `NΣ` | Statistik, Verteilungen und Regression | Zahl der Datenpunkte. | `2:288` | MENU 96 SUMS |
| `OBJ→` | Listen, Strings, Objektkonversion | Objekt zerlegen. | `2:169` | PRG TYPE; PRG LIST; MENU 62 |
| `OCT` | Binärzahlen, Logik, Modi, Systemflags | Oktale Anzeigeform. | `2:147` | MTH BASE |
| `OFF` | Schnittstellen, Drucker, Display und Tastenbelegung | Gerät ausschalten. | `2:41` | PRG RUN |
| `OLDPRT` | Schnittstellen, Drucker, Display und Tastenbelegung | Alten Druckermodus auswählen. | `2:239` | ohne Menüeintrag |
| `OPENIO` | Schnittstellen, Drucker, Display und Tastenbelegung | Ein-/Ausgabe initialisieren. | `2:361` | MENU 104 SERIAL |
| `OR` | Binärzahlen, Logik, Modi, Systemflags | Logisches/bitweises ODER. | `2:230` | MTH BASE LOGIC; PRG TEST |
| `ORDER` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Reihenfolge im Variablenmenü festlegen. | `2:345` | MENU 70 DIR |
| `OVER` | Stack und User-RPL-Programmsteuerung | Zweites Stackelement kopieren. | `2:275` | MENU 73 |
| `PARAMETRIC` | Grafik, Diagramme und Plotparameter | Parametrischen Plot aktivieren. | `2:223` | ohne Menüeintrag |
| `PARITY` | Schnittstellen, Drucker, Display und Tastenbelegung | Parität einstellen. | `2:371` | ohne Menüeintrag |
| `PARSURFACE` | Grafik, Diagramme und Plotparameter | Parametrische 3D-Oberfläche aktivieren. | `171:9` | ohne Menüeintrag |
| `PATH` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Verzeichnispfad lesen. | `2:33` | MENU 70 DIR |
| `PCOEF` | Symbolische Mathematik, Solver und Differentialgleichungen | Polynomkoeffizienten aus Nullstellen bestimmen. | `171:83` | MENU 74 POLY |
| `PCONTOUR` | Grafik, Diagramme und Plotparameter | Pseudokontur-Plot aktivieren. | `171:13` | ohne Menüeintrag |
| `PCOV` | Statistik, Verteilungen und Regression | Populationskovarianz. | `171:42` | MENU 96 FIT |
| `PDIM` | Grafik, Diagramme und Plotparameter | Bildspeicher/Plotbereich dimensionieren. | `2:195` | PRG PICT |
| `PERM` | Grundrechnen, elementare Funktionen und Zahlen | Permutationen/Variationen berechnen. | `2:130` | MTH PROB |
| `PEVAL` | Symbolische Mathematik, Solver und Differentialgleichungen | Polynom aus Koeffizienten auswerten. | `171:84` | MENU 74 POLY |
| `PGDIR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Elternverzeichnis auswählen. | `2:351` | MENU 70 DIR |
| `PICK` | Stack und User-RPL-Programmsteuerung | Stackelement aus bestimmter Tiefe kopieren. | `2:279` | MENU 73 |
| `PICT` | Grafik, Diagramme und Plotparameter | Auf Grafikobjekt-Bildspeicher zugreifen. | `2:210` | PRG PICT |
| `PICTURE` | Grafik, Diagramme und Plotparameter | Interaktive Grafikansicht öffnen. | `2:200` | MENU 96 PLOT |
| `PINIT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Plot-/Bibliotheksparameter initialisieren. | `171:129` | MENU 110 |
| `PIX?` | Grafik, Diagramme und Plotparameter | Pixel prüfen. | `2:205` | PRG PICT |
| `PIXOFF` | Grafik, Diagramme und Plotparameter | Pixel löschen. | `2:204` | PRG PICT |
| `PIXON` | Grafik, Diagramme und Plotparameter | Pixel setzen. | `2:203` | PRG PICT |
| `PKT` | Schnittstellen, Drucker, Display und Tastenbelegung | Ein-/Ausgabepaket verarbeiten. | `2:377` | MENU 104 SRVR |
| `PMAX` | Grafik, Diagramme und Plotparameter | Obere Plotgrenze. | `2:185` | ohne Menüeintrag |
| `PMIN` | Grafik, Diagramme und Plotparameter | Untere Plotgrenze. | `2:184` | ohne Menüeintrag |
| `POLAR` | Grafik, Diagramme und Plotparameter | Polarplot aktivieren. | `2:222` | ohne Menüeintrag |
| `POS` | Listen, Strings, Objektkonversion | Position eines Teilobjekts suchen. | `2:161` | PRG LIST ELEM; MENU 62 |
| `PR1` | Schnittstellen, Drucker, Display und Tastenbelegung | Druckt ein Objekt. | `2:240` | MENU 104; MENU 104 PRINT |
| `PREDV` | Statistik, Verteilungen und Regression | Regressionswert vorhersagen. | `2:303` | ohne Menüeintrag |
| `PREDX` | Statistik, Verteilungen und Regression | x-Wert mittels Regression vorhersagen. | `2:305` | MENU 96 FIT |
| `PREDY` | Statistik, Verteilungen und Regression | y-Wert mittels Regression vorhersagen. | `2:304` | MENU 96 FIT |
| `PRLCD` | Schnittstellen, Drucker, Display und Tastenbelegung | LCD-Anzeige drucken. | `2:246` | MENU 104 PRINT |
| `PROMPT` | Stack und User-RPL-Programmsteuerung | Benutzereingabe anfordern. | `1792:28` | PRG IN |
| `PROOT` | Symbolische Mathematik, Solver und Differentialgleichungen | Nullstellen eines Polynoms. | `171:82` | MENU 74 POLY |
| `PRST` | Schnittstellen, Drucker, Display und Tastenbelegung | Stack drucken. | `2:242` | MENU 104 PRINT |
| `PRSTC` | Schnittstellen, Drucker, Display und Tastenbelegung | Stack mit erweitertem Inhalt drucken. | `2:241` | MENU 104 PRINT |
| `PRVAR` | Schnittstellen, Drucker, Display und Tastenbelegung | Variablen drucken. | `2:244` | MENU 104 PRINT |
| `PSDEV` | Statistik, Verteilungen und Regression | Standardabweichung der Grundgesamtheit. | `171:40` | MENU 96 1VAR |
| `PURGE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Benannte Objekte löschen. | `2:343` | ohne Menüeintrag |
| `PUT` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element an einer Position ersetzen. | `2:176` | MTH MATRX MAKE; PRG LIST ELEM |
| `PUTI` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element ersetzen und Index erhöhen. | `2:177` | MTH MATRX MAKE; PRG LIST ELEM |
| `PVAR` | Statistik, Verteilungen und Regression | Populationsvarianz. | `171:41` | MENU 96 1VAR |
| `PVARS` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variablen des Elternverzeichnisses auflisten. | `2:350` | MENU 110 |
| `PVIEW` | Grafik, Diagramme und Plotparameter | Grafikbereich anzeigen. | `2:202` | PRG PICT; PRG OUT |
| `PWRFIT` | Statistik, Verteilungen und Regression | Potenz-Fit-Modell wählen. | `2:322` | ohne Menüeintrag |
| `PX→C` | Grafik, Diagramme und Plotparameter | Pixelkoordinaten in Benutzerkoordinaten wandeln. | `2:198` | PRG PICT |
| `QR` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | QR-Faktorisierung. | `171:60` | MTH MATRX FACTR |
| `QUAD` | Symbolische Mathematik, Solver und Differentialgleichungen | Quadratische Gleichung bearbeiten. | `2:337` | MENU 93 |
| `QUOTE` | Symbolische Mathematik, Solver und Differentialgleichungen | Verhindert unmittelbare Auswertung. | `2:257` | MENU 93 |
| `R→B` | Binärzahlen, Logik, Modi, Systemflags | Reelle Zahl nach binärer Ganzzahl. | `2:9` | MTH BASE |
| `R→C` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Aus zwei reellen Komponenten komplexe Zahl bilden. | `2:153` | MTH CMPLX; PRG TYPE |
| `R→D` | Grundrechnen, elementare Funktionen und Zahlen | Bogenmaß nach Gradmaß umrechnen. | `2:113` | MTH REAL |
| `RAD` | Binärzahlen, Logik, Modi, Systemflags | Winkelmodus Radiant. | `2:136` | MENU 63 ANGLE |
| `RAND` | Grundrechnen, elementare Funktionen und Zahlen | Pseudozufallszahl erzeugen. | `2:127` | MTH PROB |
| `RANK` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Matrixrang ermitteln. | `171:53` | MTH MATRX NORM |
| `RANM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zufallsmatrix erzeugen. | `171:64` | MTH MATRX MAKE |
| `RATIO` | Symbolische Mathematik, Solver und Differentialgleichungen | Interne Präfixform des Divisionsoperators in EquationWriter. | `2:268` | ohne Menüeintrag |
| `RCEQ` | Symbolische Mathematik, Solver und Differentialgleichungen | Gespeicherte Gleichung EQ abrufen. | `2:249` | MENU 74 ROOT; MENU 84 |
| `RCI` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeile mit Faktor multiplizieren. | `171:77` | MTH MATRX ROW |
| `RCIJ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Vielfaches einer Zeile zu anderer Zeile addieren. | `171:78` | MTH MATRX ROW |
| `RCL` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variable in Stack zurückrufen. | `2:340` | ohne Menüeintrag |
| `RCLALARM` | Zeit, Kalender, Wecker | Wecker abrufen. | `2:26` | MENU 94 ALRM |
| `RCLF` | Binärzahlen, Logik, Modi, Systemflags | Flagsatz lesen. | `2:150` | MENU 63 FLAG |
| `RCLKEYS` | Schnittstellen, Drucker, Display und Tastenbelegung | Benutzer-Tastenbelegung lesen. | `2:382` | MENU 63 KEYS |
| `RCLMENU` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Aktuelles Menü lesen. | `2:349` | MENU 63 MENU |
| `RCLΣ` | Statistik, Verteilungen und Regression | Statistikdatensatz zurückrufen. | `2:285` | MENU 87 DATA; MENU 96 DATA |
| `RCWS` | Binärzahlen, Logik, Modi, Systemflags | Wortbreite binärer Ganzzahlen abfragen. | `2:149` | MTH BASE |
| `RDM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Dimension eines Arrays ändern. | `2:172` | MTH MATRX MAKE |
| `RDZ` | Grundrechnen, elementare Funktionen und Zahlen | Zufallsgenerator initialisieren. | `2:128` | MTH PROB |
| `RE` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Realteil. | `2:154` | MTH CMPLX |
| `RECN` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Datei empfangen und benennen. | `2:365` | MENU 104 |
| `RECT` | Binärzahlen, Logik, Modi, Systemflags | Kartesischer Koordinatenmodus. | `171:19` | MTH VECTR; MENU 63 ANGLE |
| `RECV` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Objekt empfangen. | `2:366` | MENU 104 |
| `REPEAT` | Stack und User-RPL-Programmsteuerung | Wiederholung in WHILE-Schleife. | `1792:6` | PRG BRCH WHILE |
| `REPL` | Listen, Strings, Objektkonversion | Teilbereich ersetzen. | `2:157` | MTH MATRX MAKE; PRG LIST; PRG GROB; MENU 62 |
| `RES` | Grafik, Diagramme und Plotparameter | Plotauflösung einstellen. | `2:188` | ohne Menüeintrag |
| `RESTORE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Backup wiederherstellen. | `2:353` | MENU 70 |
| `REVLIST` | Listen, Strings, Objektkonversion | Liste umkehren. | `171:109` | MTH LIST; PRG LIST PROC |
| `RKF` | Symbolische Mathematik, Solver und Differentialgleichungen | Runge-Kutta-Fehlberg-Verfahren für Anfangswertprobleme. | `171:43` | MENU 74 DIFFEQ |
| `RKFERR` | Symbolische Mathematik, Solver und Differentialgleichungen | Fehlerabschätzung des RKF-Verfahrens. | `171:45` | MENU 74 DIFFEQ |
| `RKFSTEP` | Symbolische Mathematik, Solver und Differentialgleichungen | Runge-Kutta-Fehlberg-Einzelschritt. | `171:44` | MENU 74 DIFFEQ |
| `RL` | Binärzahlen, Logik, Modi, Systemflags | Bits nach links rotieren. | `2:1` | MTH BASE BIT |
| `RLB` | Binärzahlen, Logik, Modi, Systemflags | Bits um ein Byte nach links rotieren. | `2:2` | MTH BASE BYTE |
| `RND` | Grundrechnen, elementare Funktionen und Zahlen | Rundet einen Zahlenwert. | `2:108` | MTH REAL |
| `RNRM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeilennorm einer Matrix. | `2:118` | MTH MATRX NORM |
| `ROLL` | Stack und User-RPL-Programmsteuerung | Stackelement nach oben rollen. | `2:280` | MENU 73 |
| `ROLLD` | Stack und User-RPL-Programmsteuerung | Stackelement nach unten rollen. | `2:281` | MENU 73 |
| `ROOT` | Symbolische Mathematik, Solver und Differentialgleichungen | Numerische Nullstelle bestimmen. | `2:251` | MENU 74 ROOT |
| `ROT` | Stack und User-RPL-Programmsteuerung | Drei Stackelemente rotieren. | `2:274` | MENU 73 |
| `ROW-` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeile entfernen. | `171:71` | MTH MATRX ROW |
| `ROW→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Array in Zeilen zerlegen. | `171:66` | MTH MATRX ROW |
| `ROW+` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeile einfügen. | `171:72` | MTH MATRX ROW |
| `rpm` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Einheit Umdrehungen je Minute. | `171:127` | MENU 113 UTILS |
| `RR` | Binärzahlen, Logik, Modi, Systemflags | Bits nach rechts rotieren. | `2:3` | MTH BASE BIT |
| `RRB` | Binärzahlen, Logik, Modi, Systemflags | Bits um ein Byte nach rechts rotieren. | `2:4` | MTH BASE BYTE |
| `RREF` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Reduzierte Zeilenstufenform. | `171:63` | MTH MATRX FACTR |
| `RRK` | Symbolische Mathematik, Solver und Differentialgleichungen | Numerisches Verfahren für steife Differentialgleichungen. | `171:46` | MENU 74 DIFFEQ |
| `RRKSTEP` | Symbolische Mathematik, Solver und Differentialgleichungen | Einzelschritt des Verfahrens für steife DGL. | `171:47` | MENU 74 DIFFEQ |
| `RSBERR` | Symbolische Mathematik, Solver und Differentialgleichungen | Fehlerabschätzung für steife DGL. | `171:48` | MENU 74 DIFFEQ |
| `RSD` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet den Restvektor einer Matrixgleichung (A·X − B). | `2:123` | MTH MATRX; MENU 74 SYS |
| `RSWP` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeilen vertauschen. | `171:75` | MTH MATRX ROW |
| `RULES` | Symbolische Mathematik, Solver und Differentialgleichungen | Öffnet das Menü der algebraischen Umformungsregeln für den ausgewählten Teilausdruck. | `2:335` | ohne Menüeintrag |
| `SAME` | Binärzahlen, Logik, Modi, Systemflags | Vollständige Objektgleichheit prüfen. | `2:228` | PRG TEST |
| `SBRK` | Schnittstellen, Drucker, Display und Tastenbelegung | Serielles Break-Signal senden. | `2:376` | MENU 104 SERIAL |
| `SCALE` | Grafik, Diagramme und Plotparameter | Grafikmaßstab setzen. | `2:194` | ohne Menüeintrag |
| `SCATRPLOT` | Grafik, Diagramme und Plotparameter | Streudiagramm erstellen. | `2:318` | MENU 96 PLOT |
| `SCATTER` | Grafik, Diagramme und Plotparameter | Streudiagramm aktivieren. | `2:225` | ohne Menüeintrag |
| `SCHUR` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Schur-Zerlegung. | `171:62` | MTH MATRX FACTR |
| `SCI` | Binärzahlen, Logik, Modi, Systemflags | Wissenschaftliches Format. | `2:139` | MENU 63 FMT |
| `SCLΣ` | Statistik, Verteilungen und Regression | Statistische Daten skalieren. | `2:313` | ohne Menüeintrag |
| `SCONJ` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Konjugiert den Inhalt einer benannten Variablen und speichert das Ergebnis dort. | `2:326` | MENU 70 ARITH |
| `SDEV` | Statistik, Verteilungen und Regression | Stichprobenstandardabweichung. | `2:299` | MENU 96 1VAR |
| `SEND` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Objekt senden. | `2:363` | MENU 104 |
| `SEQ` | Listen, Strings, Objektkonversion | Folge generieren. | `171:98` | PRG LIST PROC |
| `SERVER` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Servermodus starten. | `2:368` | MENU 104 SRVR |
| `SF` | Binärzahlen, Logik, Modi, Systemflags | Flag setzen. | `2:131` | PRG TEST; MENU 63 FLAG |
| `SHOW` | Symbolische Mathematik, Solver und Differentialgleichungen | Symbolische Umformung anzeigen. | `2:338` | MENU 93 |
| `SIDENS` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Temperaturabhängige Dichte von Silizium berechnen. | `171:122` | MENU 113 UTILS |
| `SIGN` | Grundrechnen, elementare Funktionen und Zahlen | Vorzeichenfunktion. | `2:78` | MTH REAL; MTH CMPLX |
| `SIN` | Grundrechnen, elementare Funktionen und Zahlen | Sinus. | `2:81` | ohne Menüeintrag |
| `SINH` | Grundrechnen, elementare Funktionen und Zahlen | Sinus hyperbolicus. | `2:84` | MTH HYP |
| `SINV` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Ersetzt den Inhalt einer benannten Variablen durch dessen Inverses. | `2:324` | MENU 70 ARITH |
| `SIZE` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Größe/Dimension ermitteln. | `2:160` | MTH MATRX MAKE; PRG LIST ELEM; PRG GROB; MENU 62 |
| `SL` | Binärzahlen, Logik, Modi, Systemflags | Bitverschiebung nach links. | `2:5` | MTH BASE BIT |
| `SLB` | Binärzahlen, Logik, Modi, Systemflags | Byteverschiebung nach links. | `2:6` | MTH BASE BYTE |
| `SLOPEFIELD` | Grafik, Diagramme und Plotparameter | Richtungsfeld aktivieren. | `171:12` | ohne Menüeintrag |
| `SNEG` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Negiert den Inhalt einer benannten Variablen und speichert das Ergebnis dort. | `2:325` | MENU 70 ARITH |
| `SNRM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet die Spektralnorm eines Arrays. | `171:52` | MTH MATRX NORM |
| `SOLVEQN` | Symbolische Mathematik, Solver und Differentialgleichungen | Gleichung aus der Equation Library lösen. | `171:35` | MENU 113 EQLIB |
| `SORT` | Listen, Strings, Objektkonversion | Liste sortieren. | `171:110` | MTH LIST; PRG LIST PROC |
| `SPHERE` | Binärzahlen, Logik, Modi, Systemflags | Sphärischer Koordinatenmodus. | `171:21` | MTH VECTR; MENU 63 ANGLE |
| `SQ` | Grundrechnen, elementare Funktionen und Zahlen | Quadrat. | `2:80` | ohne Menüeintrag |
| `SR` | Binärzahlen, Logik, Modi, Systemflags | Bitverschiebung nach rechts. | `2:7` | MTH BASE BIT |
| `SRAD` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet den Spektralradius einer quadratischen Matrix. | `171:51` | MTH MATRX NORM |
| `SRB` | Binärzahlen, Logik, Modi, Systemflags | Byteverschiebung nach rechts. | `2:8` | MTH BASE BYTE |
| `SRECV` | Schnittstellen, Drucker, Display und Tastenbelegung | Seriellen Empfang steuern. | `2:360` | MENU 104 SERIAL |
| `START` | Stack und User-RPL-Programmsteuerung | Zählschleife ohne benannte Zählvariable. | `1792:9` | PRG BRCH START |
| `STD` | Binärzahlen, Logik, Modi, Systemflags | Standardformat. | `2:141` | MENU 63 FMT |
| `STEP` | Stack und User-RPL-Programmsteuerung | Zählschleife mit Schrittweite wiederholen. | `1792:12` | PRG BRCH START; PRG BRCH FOR |
| `STEQ` | Symbolische Mathematik, Solver und Differentialgleichungen | Gleichung EQ setzen. | `2:250` | MENU 74 ROOT; MENU 84 |
| `STIME` | Schnittstellen, Drucker, Display und Tastenbelegung | I/O-Zeitlimit einstellen. | `2:375` | MENU 104 SERIAL |
| `STO` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Objekt unter Variablennamen speichern. | `2:341` | ohne Menüeintrag |
| `STO-` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variable per Subtraktion aktualisieren. | `2:328` | MENU 70 ARITH |
| `STO*` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variable per Multiplikation aktualisieren. | `2:330` | MENU 70 ARITH |
| `STO/` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variable per Division aktualisieren. | `2:329` | MENU 70 ARITH |
| `STO+` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variable per Addition aktualisieren. | `2:327` | MENU 70 ARITH |
| `STOALARM` | Zeit, Kalender, Wecker | Wecker speichern. | `2:25` | MENU 94 ALRM |
| `STOF` | Binärzahlen, Logik, Modi, Systemflags | Flagsatz speichern. | `2:151` | MENU 63 FLAG |
| `STOKEYS` | Schnittstellen, Drucker, Display und Tastenbelegung | Benutzer-Tastenbelegung speichern. | `2:380` | MENU 63 KEYS |
| `STOΣ` | Statistik, Verteilungen und Regression | Statistikdatensatz speichern. | `2:283` | MENU 87 DATA; MENU 96 DATA |
| `STR→` | Listen, Strings, Objektkonversion | Text als RPL-Objekt interpretieren. | `2:163` | ohne Menüeintrag |
| `STREAM` | Listen, Strings, Objektkonversion | Sequenz von Listenelementen verarbeiten. | `171:103` | PRG LIST PROC |
| `STWS` | Binärzahlen, Logik, Modi, Systemflags | Wortbreite binärer Ganzzahlen setzen. | `2:148` | MTH BASE |
| `SUB` | Listen, Strings, Objektkonversion | Teilbereich extrahieren. | `2:156` | MTH MATRX MAKE; PRG LIST; PRG GROB; MENU 62 |
| `SVD` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Singulärwertzerlegung. | `171:57` | MTH MATRX FACTR |
| `SVL` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Singulärwerte. | `171:58` | MTH MATRX FACTR |
| `SWAP` | Stack und User-RPL-Programmsteuerung | Oberste Stackelemente vertauschen. | `2:271` | ohne Menüeintrag |
| `SYSEVAL` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | System-Einstiegspunkt aufrufen. | `2:49` | ohne Menüeintrag |
| `TAIL` | Listen, Strings, Objektkonversion | Restliste ohne erstes Element. | `171:97` | PRG LIST ELEM; MENU 62 |
| `TAN` | Grundrechnen, elementare Funktionen und Zahlen | Tangens. | `2:83` | ohne Menüeintrag |
| `TANH` | Grundrechnen, elementare Funktionen und Zahlen | Tangens hyperbolicus. | `2:86` | MTH HYP |
| `TAYLR` | Symbolische Mathematik, Solver und Differentialgleichungen | Taylorpolynom berechnen. | `2:339` | MENU 93 |
| `TDELTA` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Hilfsfunktion für Temperaturdifferenzen. | `171:123` | MENU 113 UTILS |
| `TEACH` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Lehrbeispielobjekte laden. | `171:17` | ohne Menüeintrag |
| `TEXT` | Schnittstellen, Drucker, Display und Tastenbelegung | Aktiviert die normale Stackdarstellung beim nächsten Display-Refresh. | `2:217` | PRG OUT |
| `THEN` | Stack und User-RPL-Programmsteuerung | Wahr-Zweig beginnen. | `1792:1, 1792:24, 1792:26` | PRG BRCH IF; PRG BRCH CASE; PRG ERROR IFERR |
| `TICKS` | Zeit, Kalender, Wecker | Interne Zeitbasis lesen. | `2:18` | MENU 94 |
| `TIME` | Zeit, Kalender, Wecker | Aktuelle Zeit lesen. | `2:16` | MENU 94 |
| `TINC` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Hilfsfunktion für Temperaturänderungen. | `171:124` | MENU 113 UTILS |
| `TLINE` | Grafik, Diagramme und Plotparameter | Linie invertierend zeichnen. | `2:207` | PRG PICT |
| `TMENU` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Temporäres Menü erzeugen. | `2:347` | MENU 63 MENU |
| `TOT` | Statistik, Verteilungen und Regression | Summe der statistischen Werte. | `2:300` | MENU 96 1VAR |
| `TRACE` | Grafik, Diagramme und Plotparameter | Plot-/Programmverfolgung aktivieren. | `171:50` | MTH MATRX NORM |
| `TRANSIO` | Schnittstellen, Drucker, Display und Tastenbelegung | I/O-Übertragungsart wählen. | `2:372` | ohne Menüeintrag |
| `TRN` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Matrix transponieren. | `2:175` | MTH MATRX MAKE |
| `TRNC` | Grundrechnen, elementare Funktionen und Zahlen | Schneidet einen Zahlenwert ab. | `2:109` | MTH REAL |
| `TRUTH` | Grafik, Diagramme und Plotparameter | Wahrheitswertplot aktivieren. | `2:224` | ohne Menüeintrag |
| `TSTR` | Zeit, Kalender, Wecker | Zeit in Text formatieren. | `2:29` | MENU 94 |
| `TVARS` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variablen nach Typ auflisten. | `2:37` | MENU 70 DIR |
| `TVM` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Zeitwert-des-Geldes-Gleichungslöser. | `171:85` | ohne Menüeintrag |
| `TVMBEG` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Zahlungsmodus Periodenbeginn. | `171:86` | ohne Menüeintrag |
| `TVMEND` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Zahlungsmodus Periodenende. | `171:87` | ohne Menüeintrag |
| `TVMROOT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | TVM-Unbekannte bestimmen. | `171:88` | MENU 74 TVM |
| `TYPE` | Listen, Strings, Objektkonversion | Objekttyp abfragen. | `2:166` | PRG TEST; PRG TYPE |
| `UBASE` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Einheit in Basiseinheiten ausdrücken. | `2:14` | MENU 59 |
| `UFACT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Einheitenausdruck faktorisieren. | `2:15` | MENU 59 |
| `UNTIL` | Stack und User-RPL-Programmsteuerung | DO-Schleifenbedingung. | `1792:8` | PRG BRCH DO |
| `UPDIR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | In übergeordnetes Verzeichnis wechseln. | `2:35` | ohne Menüeintrag |
| `UTPC` | Statistik, Verteilungen und Regression | Chi-Quadrat-Verteilung: obere Verteilungswahrscheinlichkeit. | `2:308` | MTH PROB |
| `UTPF` | Statistik, Verteilungen und Regression | F-Verteilung: obere Verteilungswahrscheinlichkeit. | `2:310` | MTH PROB |
| `UTPN` | Statistik, Verteilungen und Regression | Normalverteilung: obere Verteilungswahrscheinlichkeit. | `2:309` | MTH PROB |
| `UTPT` | Statistik, Verteilungen und Regression | Student-t-Verteilung: obere Verteilungswahrscheinlichkeit. | `2:311` | MTH PROB |
| `UVAL` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Zahlenwert aus Einheitenobjekt ermitteln. | `2:12` | MENU 59 |
| `V→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Vektor in Komponenten zerlegen. | `2:180` | MTH VECTR |
| `VAR` | Statistik, Verteilungen und Regression | Stichprobenvarianz. | `2:301` | MENU 96 1VAR |
| `VARS` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variablen auflisten. | `2:36` | MENU 70 DIR |
| `VERSION` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | ROM-Version anzeigen. | `171:15` | ohne Menüeintrag |
| `VTYPE` | Listen, Strings, Objektkonversion | Typ eines Variablenwertes abfragen. | `2:167` | PRG TYPE |
| `WAIT` | Stack und User-RPL-Programmsteuerung | Auf Zeitablauf oder Taste warten. | `2:55` | PRG IN |
| `WHILE` | Stack und User-RPL-Programmsteuerung | WHILE-Schleife beginnen. | `1792:5` | PRG BRCH WHILE |
| `WIREFRAME` | Grafik, Diagramme und Plotparameter | 3D-Drahtgitter aktivieren. | `171:8` | ohne Menüeintrag |
| `WSLOG` | Zeit, Kalender, Wecker | Liefert Protokoll der letzten vier Warmstarts mit Zeitpunkt und Ursachenkennung. | `2:19` | ohne Menüeintrag |
| `XCOL` | Statistik, Verteilungen und Regression | x-Datenspalte auswählen. | `2:306` | ohne Menüeintrag |
| `XMIT` | Schnittstellen, Drucker, Display und Tastenbelegung | Daten seriell ohne Kermit senden. | `2:359` | MENU 104 SERIAL |
| `XOR` | Binärzahlen, Logik, Modi, Systemflags | Logisches/bitweises exklusives ODER. | `2:232` | MTH BASE LOGIC; PRG TEST |
| `XPON` | Grundrechnen, elementare Funktionen und Zahlen | Zehnerexponent einer Zahl. | `2:105` | MTH REAL |
| `XRECV` | Schnittstellen, Drucker, Display und Tastenbelegung | Datei via XModem empfangen. | `171:95` | MENU 104 |
| `XRNG` | Grafik, Diagramme und Plotparameter | Horizontaler Wertebereich. | `2:218` | ohne Menüeintrag |
| `XROOT` | Grundrechnen, elementare Funktionen und Zahlen | n-te Wurzel. | `2:74, 2:75` | ohne Menüeintrag |
| `XSEND` | Schnittstellen, Drucker, Display und Tastenbelegung | Datei via XModem senden. | `171:94` | MENU 104 |
| `XVOL` | Grafik, Diagramme und Plotparameter | 3D-Volumen: x-Bereich. | `171:0` | ohne Menüeintrag |
| `XXRNG` | Grafik, Diagramme und Plotparameter | 3D-x-Bereich einstellen. | `171:3` | ohne Menüeintrag |
| `YCOL` | Statistik, Verteilungen und Regression | y-Datenspalte auswählen. | `2:307` | ohne Menüeintrag |
| `YRNG` | Grafik, Diagramme und Plotparameter | Vertikaler Wertebereich. | `2:219` | ohne Menüeintrag |
| `YSLICE` | Grafik, Diagramme und Plotparameter | Y-Schnitt-Plot aktivieren. | `171:11` | ohne Menüeintrag |
| `YVOL` | Grafik, Diagramme und Plotparameter | 3D-Volumen: y-Bereich. | `171:1` | ohne Menüeintrag |
| `YYRNG` | Grafik, Diagramme und Plotparameter | 3D-y-Bereich einstellen. | `171:4` | ohne Menüeintrag |
| `ZFACTOR` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Berechnet den Realgas-Kompressibilitätsfaktor Z aus reduzierter Temperatur und reduziertem Druck. | `171:118` | MENU 113 UTILS |
| `ZVOL` | Grafik, Diagramme und Plotparameter | 3D-Volumen: z-Bereich. | `171:2` | ohne Menüeintrag |
| `ΔLIST` | Listen, Strings, Objektkonversion | Differenzen benachbarter Listenelemente. | `171:100` | MTH LIST |
| `π` | Grundrechnen, elementare Funktionen und Zahlen | Symbolische Kreiszahl. | `2:63` | MTH CONST |
| `ΠLIST` | Listen, Strings, Objektkonversion | Liste multiplizieren. | `171:106` | MTH LIST |
| `Σ` | Symbolische Mathematik, Solver und Differentialgleichungen | Summation einer Folge. | `2:254` | ohne Menüeintrag |
| `Σ-` | Statistik, Verteilungen und Regression | Punkt aus Statistikdatensatz entfernen. | `2:287` | MENU 87 DATA; MENU 96 DATA |
| `Σ+` | Statistik, Verteilungen und Regression | Statistischen Datensatz um einen Punkt ergänzen. | `2:286` | MENU 87 DATA; MENU 96 DATA |
| `ΣLINE` | Statistik, Verteilungen und Regression | Regressionsgerade aus Summendaten. | `2:314` | MENU 96 FIT |
| `ΣLIST` | Listen, Strings, Objektkonversion | Liste aufsummieren. | `171:104` | MTH LIST |
| `ΣX` | Statistik, Verteilungen und Regression | Summe der x-Werte. | `2:291` | MENU 96 SUMS |
| `ΣX*Y` | Statistik, Verteilungen und Regression | Summe der Produkte x mal y. | `2:295` | MENU 96 SUMS |
| `ΣX^2` | Statistik, Verteilungen und Regression | Summe der x-Quadrate. | `2:293` | MENU 96 SUMS |
| `ΣY` | Statistik, Verteilungen und Regression | Summe der y-Werte. | `2:292` | MENU 96 SUMS |
| `ΣY^2` | Statistik, Verteilungen und Regression | Summe der y-Quadrate. | `2:294` | MENU 96 SUMS |

## 4. Was nicht fälschlich mitgezählt werden darf

1. **Nichtprogrammierbare Tasten und Dialogfolgen:** `DBUG`, `SST`, `SST↓`, Editor- und Navigationsaktionen, Hotkeys, Untermenüs, Reset-/Selbsttestsequenzen; sie müssen als UI-Bedieninventar, nicht als ROM-Befehlsnameneinträge geprüft werden.
2. **ROM-eigene Datentabellen:** Die rund 147 Einheiten, 300+ Formeln, Konstanten und eingebauten Beispiele sind kein Synonym für 147 oder 300 neue RPL-Befehlsnamen. Eine hundertprozentige historische Emulation verlangt zusätzliche, getrennte Kataloge der **Einheitenbezeichnungen, Einzelformeln, Konstantenwerte und Sonderbilder**. Diese Werte sind hier **nicht einzeln aufgeschrieben**; eine Behauptung absoluter Vollständigkeit über alle internen ROM-Daten wäre daher falsch.
3. **Erweiterungskarten/Fremdsoftware:** Software- und RAM-Module sind in der GX-Hardware möglich, jedoch nicht serienmäßig installiert. Das Periodensystem und Tetris der älteren HP-48SX-Equation-Library-Karte zählen **nicht** automatisch zum HP-48GX-ROM.
4. **System- und Maschinenebene:** Interne System-RPL-Entry-Points, Saturn-CPU-Befehle, ROM-Routinen und ROM-Images bilden einen eigenen Forschungsumfang. `SYSEVAL` und `LIBEVAL` erscheinen als Benutzerschnittstellen, nicht als vollständige Liste der aufrufbaren Systemfunktionen.
5. **ROM-Revisionsunterschiede:** Historische ROM-Stände (K/L/M/P/R) und ihre Fehler sind getrennte Testprofile. Eine Namensliste allein ist kein Anspruch auf identisches Verhalten bei allen Revisionen.

## 5. Bezug zur SASD-Roadmap und Testplanung

| Bereich | Zielebene | Status |
| --- | --- | --- |
| Basiswissenschaft, bedienbarer RPN-Stack, Zustand, Tests, offline iPhone | M1/M2, Kernrechner zuerst | **geplant / nach gesondertem Code- und Testnachweis** |
| User-RPL, Objekte, Variablen, Programme, ausgewählte historische Befehle | M3 | **geplant, kein V1-Blocker** |
| Virtuelle historische RPL-Systemobjekte und ausgewählte System-RPL-Aufrufe | M4 | **geplant; sicher gekapselte virtuelle Speicherzugriffe** |
| Saturn-CPU-/ROM-Forschung | M5 | **optional, kein V1-Blocker** |

Für eine echte Nachimplementierung ist **pro Befehl** gesondert zu dokumentieren: akzeptierte Objekttypen, Anzahl und Reihenfolge der Stackargumente, Resultate, Fehlertypen, Flags, Rundung, Seiteneffekte, ROM-Profil, Persistenz und unabhängige Konformitätstests. **Keine** der 517 Tabellenzeilen behauptet eine fertige SASD-Implementierung.

## 6. Originalquellen, Rechte und Reproduzierbarkeit

1. Hewlett-Packard, **_HP 48G Series User’s Guide_**, 8. Ausgabe, Dezember 1994, PN 00048-90126 – Bedienung, Menüs, Gleichungsbibliothek, Anhänge zu Einheiten, Flags und Gleichungen: https://literature.hpcalc.org/official/hp48gseries-ug-en.pdf
2. Hewlett-Packard, **_HP 48G Series Advanced User’s Reference_**, 4. Ausgabe, Dezember 1994, PN 00048-90136 – alphabetische User-RPL-Befehlsreferenz und Stackdiagramme: https://literature.hpcalc.org/items/370
3. James Donnelly, **_The HP 48G/GX Pocket Guide_**, Command Index ab S. 41 – kompakte Befehlssammlung: https://literature.hpcalc.org/community/hp48g-pg-en.pdf
4. ractive/saturnus, **aus dem HP-48GX-ROM generierter Katalog `48gx.json`** – Quelle für exakt die 517 Kommandonamen, XLIB-Kennungen und Menüzugänge dieser Tabelle: https://github.com/ractive/saturnus/blob/main/crates/saturnus-cli/data/commands/48gx.json
5. saturnus, **HP-48GX-Gerätereferenz** und Beschreibung eingebauter Anwendungen: https://ractive.ch/saturnus/docs/48gx/
6. **HP48 FAQ**, insbesondere Informationen zu G/GX-Erweiterungen und ROM-Versionen: https://www.hpcalc.org/hp48/docs/faq/
7. Ergänzende historische Referenzen und technische Notizen: https://www.hpcalc.org/hp48/docs/

**Validierung:** Anzahl der ROM-JSON-Einträge = 517; Anzahl eindeutiger Namen = 517; Tabellenzeilen zu ROM-Befehlen = 517. Die ROM-Namen wurden **nicht** um moderne Funktionen ergänzt. Unbekannte Ergebnisse und alternative Stacktypen bleiben Gegenstand der späteren AUR-basierten Einzelprüfung. Keine fremden ROM-Images, grafischen Assets oder wörtlichen Handbuchabschnitte sind im Repository abgelegt.
