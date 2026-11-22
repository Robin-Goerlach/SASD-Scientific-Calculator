# HP 48GX – historischer Funktionskatalog (Arbeitsstand, Vollständigkeitsprüfung offen)

**Projekt:** SASD Scientific Calculator · **Recherche:** 21.11.2026  
**Historisches Referenzmodell:** HP 48GX der 48G-Reihe (Grundausstattung ab Werk; keine beliebig nachgerüsteten Erweiterungskarten).  
**Status:** Historische Forschungs-/Anforderungsreferenz. **Vollständigkeit ausdrücklich noch nicht abgenommen.** **Nicht** gleichbedeutend mit vorhandener SASD-Implementierung.

**Neu: vollständiges zeilenbezogenes Originalindex-Inventar:** [HP-48GX-OPERATION-INDEX-VOLLKATALOG.md](HP-48GX-OPERATION-INDEX-VOLLKATALOG.md) – **alle 57 Tabellenseiten G-2 bis G-58**, **696 Originalindex-Zeilen**, inklusive `O/C/F/A`, Fundseite und getrennten Bedienkontexten. Daraus ergeben sich **661 unterschiedliche Drucknamen**, **179 reine O-Zeilen** und **517 Zeilen mit mindestens einer programmierbaren Funktion/Befehlsklasse**. Das ist **nicht** identisch mit 517 verschiedenen ROM-Namen, sondern eine unabhängig strukturierte Quellenmenge. Sonderzeichen und unklare Aliase bleiben in der Datei ausdrücklich gekennzeichnet. Eine vollständige AUR- und Semantikabnahme ist weiterhin offen.

**A08 (Befehle 351–400):** [AUR-Pocket-Guide-Teilprüfung A08](HP-48GX-AUR-TEILPRUEFUNG-A08.md); 50 AUR-Namen, 47 direkte ROM-Namen, `SIMU`, `SST`, `SST↓` als Sonderfälle. `SCLΣ`/`SCLS`/`SCLZ`, `RSWP`/`RSVP` und `SCATR PLOT`/`SCATRPLOT` als offene Text-/Scanfragen dokumentiert; Stack-/Originalbildprüfung weiterhin offen.

**A07 (Befehle 301–350):** [AUR-Pocket-Guide-Teilprüfung A07](HP-48GX-AUR-TEILPRUEFUNG-A07.md); alle 50 AUR-Positionen mit eigenen ROM-Namen und unabhängigem Pocket-Guide-Textnachweis, OCR-Abweichungen bei u.a. `→Qπ`, `RCLΣ`, `RKFSTEP`, `RND`, `ROW→`. Originalscans und Stack-/Fehlerfälle bleiben offen.

**A06 (Befehle 251–300):** [AUR-Pocket-Guide-Teilprüfung A06](HP-48GX-AUR-TEILPRUEFUNG-A06.md); 50 unterschiedliche AUR-Namen, 50 direkte ROM-XLIB-Zuordnungen, 50 Pocket-Guide-Textbelege. Verwechslungen bei `NΣ`/`NZ`, `PROMPT`/`PRMPT`, `PREDV`/`PREDY`, `PVAR`/`PVARS` dokumentiert; Scan-/Stackabnahme weiterhin offen.

**A05 (Befehle 201–250):** [AUR-Pocket-Guide-Teilprüfung A05](HP-48GX-AUR-TEILPRUEFUNG-A05.md); 50 AUR-Positionen mit 49 verschiedenen Befehlsnamen (Doppelindex `NEXT`), alle normiert im ROM und im Pocket-Guide-Text zugeordnet. Glyphenkonflikte bei `↑MATCH`/`↓MATCH` und `→NUM`; Originalscan-/Stackabnahme offen.

**A04 (Befehle 151–200):** [AUR-Pocket-Guide-Teilprüfung A04](HP-48GX-AUR-TEILPRUEFUNG-A04.md); 47 ROM-Namen, drei Sonderfälle `GRAPH`, `IR`, `LAST` und OCR-Differenzen bei `GRAD`, `GXOR`, Zeitkonvertierung. Kein Scan-/Stack-Abnahmestatus.

**A03 (Befehle 101–150):** [AUR-Pocket-Guide-Teilprüfung A03](HP-48GX-AUR-TEILPRUEFUNG-A03.md); 50/50 normierte ROM-Namen und Pocket-Guide-Textbelege, `ERR0`-OCR-Abweichung erfasst, `ENDSUB`-Bedeutung korrigiert; Scan-/Stack-Abnahme weiterhin offen.

**A02 (Befehle 51–100):** [AUR-Pocket-Guide-Teilprüfung A02](HP-48GX-AUR-TEILPRUEFUNG-A02.md); Kurzbeschreibungen von 12 belegten Befehlen präzisiert, Scan-/Stack-Verhalten noch offen.

**Unabhängiger Pocket-Guide-Abgleich:** [AUR-Teilprüfung A01 (erste 50 Befehle)](HP-48GX-AUR-TEILPRUEFUNG-A01.md); weitere AUR-Detailprüfungen bleiben offen.

**Etappierte Prüfung:** [Prüfstand/Teilaufgaben G-2 bis G-8](HP-48GX-TEILPRUEFUNG-G02-G08.md), [G-9 bis G-15](HP-48GX-TEILPRUEFUNG-G09-G15.md), [Semantik-Nachprüfung 01](HP-48GX-SEMANTIK-NACHPRUEFUNG-01.md) und [maschinenlesbare Fortschrittsmatrix](../reference/hp48gx-audit-partitions.json). Die Originalscan- und AUR-Stack-Freigabe ist weiterhin offen.

**Verbindlicher Vollständigkeitsnachweis:** [HP-48GX-VOLLSTAENDIGKEITSAUDIT.md](HP-48GX-VOLLSTAENDIGKEITSAUDIT.md) – Abgleich mit Appendix G des Originalhandbuchs, AUR-Kommandoreferenz, ROM-Index, Tastatur, Menüs und eingebauten Datentabellen. **Quellen- und Befehlsmatrix:** [HP-48GX-BEFEHLSABGLEICH-MATRIX.md](HP-48GX-BEFEHLSABGLEICH-MATRIX.md); dort werden alle 517 ROM-Namen mit möglichen Fundstellen, offenen Fällen und ersten gegen Anhang G geprüften Bedienoperationen erfasst. Bis dessen Kriterien erfüllt sind, gilt dieses Dokument als **Arbeitsinventar**.

> **Vollständigkeit und Grenzen:** Kapitel 2a enthält jetzt den belegten Tastatur-, Menü-, App-, Einheiten- und Equation-Library-Abgleich mit den historischen Handbüchern. Die alphabetische Tabelle in Kapitel 3 enthält **sämtliche 517 unterschiedlichen Einträge** der aus dem HP-48GX-ROM generierten *saturnus*-Befehlsnamendatei (`48gx.json`). Dazu gehören Operatoren, Konstanten und RPL-Strukturtoken; daher sind dies **nicht** 517 mathematisch unabhängige Funktionen. Die Vollständigkeit bezieht sich auf **diesen belegten ROM-Namensindex**, nicht auf sämtliche internen System-RPL-Einstiegspunkte, jede Bediensequenz oder alle Inhalte von Fremdkarten. Ergänzende interaktive Funktionen und Grenzen sind ausdrücklich dokumentiert. Alle Kurzbeschreibungen wurden neu verfasst, nicht aus Originalhandbüchern abgeschrieben.

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
- ROM-Versionen und besondere eingebaute Befehle `VERSION`, `RULES` (undokumentierte Entwicklerfunktion; vom EquationWriter-Regelmenü zu unterscheiden), `TEACH`/`CLTEACH` und `MINEHUNT`.

## 2a. Überprüfung anhand der Originalhandbücher und der vollständigen Tastatur

### 2a.1 Was mit »alle Funktionen« gemeint ist

Die Kurzanleitung des HP-48G beschreibt ausdrücklich **49 physische Tasten und mehr als tausend ausführbare Bedienoperationen** (deutsche Kurzanleitung, S. 2-10, PDF-S. 24). Die Zahl ist **keine Anzahl unterschiedlicher User-RPL-Kommandonamen**. Das englische Originalhandbuch unterscheidet `operation` (ausführbare Handlung), `command` (programmierbare Operation), `function` (als algebraische Funktion verwendbarer Befehl) und `analytic function` (Funktion mit besonderer symbolischer Behandlung). Die 517 aus dem ROM abgeleiteten Namen in Kapitel 3 sind deshalb nur **eine Ebene** einer sinnvollen Vollständigkeitsprüfung.

**Quellenlage (Modell/Edition prüfen):**

| Kennung | Quelle | Geltungsbereich | Verwendung |
| --- | --- | --- | --- |
| Q1 | Hochgeladen: `HP 48g-qsg-de.pdf`, *Serie HP 48G Kurzanleitung*, HP 00048-90127, 3. Auflage März 1994, 132 PDF-Seiten | HP-48G-Serie, einschließlich GX | Tatsächlich gesichtete deutsche Grundlagenschritte, 37 Lektionen, Bildschirm- und Menüdarstellung |
| Q2 | Hewlett-Packard, *HP 48G Series User's Guide*, 8. Ausgabe Dezember 1994, 612 Seiten | HP 48G/G+/GX | Tastaturebenen, 12 Anwendungen, Einheiten/Graphik, Appendix C–H; [Online-Original](https://literature.hpcalc.org/official/hp48gseries-ug-en.pdf) |
| Q3 | Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Ausgabe Dezember 1994, 766 Scan-Seiten | HP 48G/G+/GX | Befehlssyntax/Stackdiagramme, Gleichungsreferenz, Units, Systemflags, reservierte Variablen; [Online-Original](https://literature.hpcalc.org/community/hp48g-aur-en.pdf) |
| Q4 | Das im Projekt bereitgestellte Foto `HP 48GX_Calculator.jpg` | Physische GX-Tastatur | Sichtprüfung sämtlicher 49 Tasten und deren farbigen Beschriftungen |
| Q5 | James Donnelly et al., *The HP 48G/GX Pocket Guide*, Command Index, S. 41–77 | HP 48G/GX | unabhängige Kurzreferenz zu Befehlen und Bedientasten; [PDF](https://literature.hpcalc.org/community/hp48g-pg-en.pdf) |
| Q6 | Viktor T. Toth / Eric Rechlin und John Finseth: [HP48GX Key Locator, menu and equation inventory](https://finseth.com/hpdata/hp48gx.php) | GX-Referenz | Zweitprüfung der Shift-Belegung, Menüs, Einheiten und Titel der Equation Library |
| **X1** | Hochgeladen: `HP 48GX grafikfähiger Taschenrechner.pdf` – tatsächlicher PDF-Titel **`hp 48gII grafikfähiger Taschenrechner`**, 4. Ausgabe April **2004**, 981 PDF-Seiten | **HP 48gII, NICHT HP 48GX** | **Nicht** zur Ableitung der GX-Befehle verwenden; separate spätere Plattform mit anderem CAS/Funktionssatz |
| P1 | Hochgeladen: `HP_48GX_App-SASD_Scientific_Calculator_Repository-2026_11_21.pdf` | SASD-Projektarchiv, kein historisches Handbuch | Projektkontext, keine Primärquelle für GX-Funktionen |

Die HP-48gII-Befehle wie `DROITE`, `COLLECT`, `FACTOR`, `LNCOLLECT`, `PARTFRAC`, `ZEROS`, `DESOLVE`, `LAPLACE` oder `HESS` in der hochgeladenen 2004er Anleitung sind **nicht schon deshalb HP-48GX-Werksbefehle**. Ähnlich benannte klassische Funktionen im GX werden anhand des AUR/ROM einzeln unterschieden.

### 2a.2 Tastatur: alle **49 physischen Tasten** und die sichtbaren Mehrfachfunktionen

**Lesart:** »Links« = lavendelfarbene linke Shift-Taste; »rechts« = türkisfarbene rechte Shift-Taste. Die Taste kann in verschiedenen Kontexten eine andere Wirkung haben. Bei den sechs weißen Softkeys A–F ist der Funktionsinhalt **dynamisch** und kommt aus dem Menü, kein fest kodierter »A«-Rechenbefehl. Bei Ziffern sind die nicht gedruckten Shift-Belegungen nicht künstlich ergänzt. `–` bedeutet: keine entsprechend aufgedruckte zusätzliche Taste in der sichtbaren Ebene.

| Physische Position / Alpha | Grundtaste | Linker Shift (lavendel) | Rechter Shift (türkis) | Wirkung / Kontext |
| --- | --- | --- | --- | --- |
| 1 / A | A / Softkey A | dynamisches erstes Menüfeld | – | Menüseite / Alpha A |
| 1 / B | B / Softkey B | dynamisches zweites Menüfeld | – | Menüseite / Alpha B |
| 1 / C | C / Softkey C | dynamisches drittes Menüfeld | – | Menüseite / Alpha C |
| 1 / D | D / Softkey D | dynamisches viertes Menüfeld | – | Menüseite / Alpha D |
| 1 / E | E / Softkey E | dynamisches fünftes Menüfeld | – | Menüseite / Alpha E |
| 1 / F | F / Softkey F | dynamisches sechstes Menüfeld | – | Menüseite / Alpha F |
| 2 / G | MTH | RAD | POLAR | Mathematik-Menü / Winkelmodus |
| 2 / H | PRG | – | CHARS | Programm-Menü / 256-Zeichenkatalog |
| 2 / I | CST | – | MODES | Benutzermenü / Systemeinstellungen |
| 2 / J | VAR | – | MEMORY | Variablenmenü / Variablen-Browser |
| 2 / K | ▲ | – | STACK | Cursor aufwärts / interaktiver Stack |
| 2 / L | NXT | PREV | MENU | Nächste / vorige Menüseite; vorheriges Menü |
| 3 / M | ' | UP | HOME | Algebraisches Objekt quotieren; Verzeichnisnavigation |
| 3 / N | STO | DEF | RCL | Speichern / Funktionsdefinition / Rückruf |
| 3 / O | EVAL | →NUM | UNDO | Auswerten / numerisch / letzten Stack wiederherstellen |
| 3 / P | ◄ | PICTURE | – | Cursor links bzw. Grafikansicht |
| 3 / Q | ▼ | VIEW | – | Cursor abwärts bzw. Stackobjekt ansehen |
| 3 / R | ► | SWAP | – | Cursor rechts bzw. Stackebenen 1/2 vertauschen |
| 4 / S | SIN | ASIN | ∂ | Sinus / Arkussinus / Differenziation |
| 4 / T | COS | ACOS | ∫ | Kosinus / Arkuskosinus / Integration |
| 4 / U | TAN | ATAN | Σ | Tangens / Arkustangens / Summation |
| 4 / V | √x | x² | x√y (XROOT) | Quadratwurzel / Quadrat / n-te Wurzel |
| 4 / W | yˣ | 10ˣ | LOG | Potenz / Antilogarithmus / Zehnerlogarithmus |
| 4 / X | 1/x | eˣ | LN | Kehrwert / Exponentialfunktion / natürlicher Logarithmus |
| 5 / 1 | ENTER | EQUATION | MATRIX | Stackeingabe / EquationWriter / MatrixWriter |
| 5 / Y | +/− | EDIT | CMD | Vorzeichen / Objekteditierung / Kommandohistorie |
| 5 / Z | EEX | PURG | ARG | Exponenteneingabe / Löschen / komplexes Argument |
| 5 / – | DEL | CLEAR | – | Zeichen löschen bzw. gesamten Stack leeren |
| 5 / – | ← (Backspace) | DROP | – | Zeichen davor löschen bzw. Stackobjekt entfernen |
| 6 / – | α | USER | ENTRY | Alpha / User-Tastatur / Eingabemodus |
| 6 / – | 7 | – | SOLVE | Ziffer 7 / Gleichungslöser |
| 6 / – | 8 | – | PLOT | Ziffer 8 / Plot-Anwendung |
| 6 / – | 9 | – | SYMBOLIC | Ziffer 9 / symbolische Mathematik |
| 6 / – | ÷ | ( ) | # | Division / Klammerpaar / binäres Objektzeichen |
| 7 / – | Linke Umschalttaste | – | – | Lavendel-/linke Shift-Ebene aktivieren |
| 7 / – | 4 | – | TIME | Ziffer 4 / Uhr, Datum, Alarmverwaltung |
| 7 / – | 5 | – | STAT | Ziffer 5 / Statistik-Anwendung |
| 7 / – | 6 | – | UNITS | Ziffer 6 / Maßeinheitenkatalog |
| 7 / – | × | [ ] | _ | Multiplikation / Arrayklammern / Einheitentrenner |
| 8 / – | Rechte Umschalttaste | – | – | Türkis-/rechte Shift-Ebene aktivieren |
| 8 / – | 1 | – | I/O | Ziffer 1 / Datentransfer, serielle und IR-Schnittstelle |
| 8 / – | 2 | – | LIBRARY | Ziffer 2 / Bibliotheken, Kartenports |
| 8 / – | 3 | – | EQ LIB | Ziffer 3 / eingebaute Gleichungsbibliothek |
| 8 / – | − | « » | " " | Subtraktion / Programmbegrenzer / Zeichenkette |
| 9 / – | ON | CONT | OFF | Einschalten/Abbruch / Fortsetzen / Ausschalten |
| 9 / – | 0 | = | → | Ziffer 0 / Gleichheitszeichen / lokale Variablen |
| 9 / – | . | , | ↵ | Dezimalpunkt / Argumenttrennung / Eingabeende im Editor |
| 9 / – | SPC | π | ∠ | Leerzeichen / Pi / Winkelzeichen |
| 9 / – | + | { } | : : | Addition / Liste / weitere Trenn-/Tagzeichen |

**Tastaturebenen insgesamt:** Normaltastatur; Links-Shift; Rechts-Shift; Alpha-Großbuchstaben; Alpha-Links-Shift (Kleinbuchstaben); Alpha-Rechts-Shift (griechische/weitere Sonderzeichen). Alpha-Shift-Belegungen sind teilweise **nicht auf den physischen Tasten aufgedruckt**. Alpha einmal, Alpha zweimal (Verriegelung), Shift plus Alpha, Klein-/Großschreibung, gehaltene Alpha-Taste, Benutzer-Modus und benutzerdefinierte Tasten gehören als **Zustandsautomaten** in einen späteren Tastaturtest.

**Präzise Kontextregeln:** Die Richtungstasten `▲ ▼ ◄ ►`, `DEL` und Backspace navigieren bzw. löschen **in Eingabe/Editoren**, können aber **ohne aktiven Cursor** die Funktionen `STACK`, `VIEW`, `PICTURE`, `SWAP`, `CLEAR` und `DROP` ausführen. `ON` ist im Betrieb meist `CANCEL`. `NXT` blättert Menüseiten; mit `PREV` rückwärts und `MENU` zwischen zuletzt aktiven Menüs. Das ist aus Bild plus User's Guide Kapitel 1 und Q1, Lektionen 2–5, belegt.

### 2a.3 Die **12 eingebauten Anwendungen** (Bildschirm-/Dialogfunktionen)

| Anwendung | Aufruf über rechte Shift-Ebene | Umfasste Bedienmöglichkeiten (kein separater XLIB-Name für jede Aktion) |
| --- | --- | --- |
| CHARS | PRG | 256-Zeichen-Katalog, vier Tafeln à 64 Zeichen, Pfeiltasten, Zeichenposition, ECHO in Kommandozeile |
| EQ LIB | 3 | Themen und Problemüberschriften wählen, Gleichungen/Bildtafeln und Einheiten, Constants Library, Multiple Equation Solver, Utilities |
| I/O | 1 | Rechner-/PC-Datentransfer, Kermit, serielle Parameter, IR, Drucken, Status und Fehler |
| LIBRARY | 2 | Ports durchblättern, Bibliotheken suchen, anhängen/abhängen, Speicherkartenbezug |
| MEMORY | VAR | Variablen-Browser mit Verzeichnisnavigation, Ansehen, Bearbeiten, Kopieren, Verschieben, Umbenennen, Löschen, Backup/Restore |
| MODES | CST | Number Format, Angle Measure, Coordinate System, BEEP/CLOCK/Decimal-Mark, Systemflags, eigene Tastatur und Menüs |
| PLOT | 8 | Auswahl eines von 15 Plottypen, EQ/PPAR/VPAR-Formulare, Grenzen, Achsen, grafische Darstellung |
| SOLVE | 7 | Gleichungen, Polynomnullstellen, lineare Systeme, Differentialgleichungen und Finanz-TVM historisch |
| STACK | ▲ | Interaktiver Stack: Ebenen auswählen, Objekt ansehen/editieren, Kopien, Vertauschungen, Auswählen, Einfügen und Entfernen |
| STAT | 5 | Dateneingabe/-editor, ein- und zweidimensionale Kennzahlen, Regressions-/Fit-Analyse und statistische Plots |
| SYMBOLIC | 9 | Differenzieren, Integrieren, Taylor, Isolieren von Unbekannten, Quadratisieren, Expandieren/Collect |
| TIME | 4 | Datum/Uhrzeit, Alarm-/Terminbrowser, Wiederholung, Alarm-Bestätigung und Datum-/Zeitberechnung |

**Zusätzliche Editoren/Umgebungen:** `EQUATION` (EquationWriter), `MATRIX` (MatrixWriter), `PICTURE` (Bild-/Plot-Umgebung), Zeichenketten-Editor, Befehlszeile, der Bildschirm zum Ändern/Ansehen von Variablen sowie der interaktive Stack sind eigenständige **Oberflächenfunktionen**. Insbesondere `SOLVE`, `STAT` und `PLOT` bieten Fullscreen-Formulare und zugehörige Programm-Menüs, nicht nur eine einzelne Ergebnisfunktion.

### 2a.4 Systematische Menüinventur, einschließlich nicht programmierbarer Menüaktionen

Hier werden Menübereiche **als Navigationsräume** dokumentiert. Die voll ausgeschriebenen programmierbaren Befehlsnamen stehen in Kapitel 3; hier wird erfasst, **welche Funktionalität Anwender in den Menüs erreichen können**.

| Menü / Untermenü | Funktionen, Menügruppen und Bedienelemente |
| --- | --- |
| `MTH` | `VECTR`, `MATR`, `LIST`, `HYP`, `REAL`, `BASE`, `PROB`, `FFT`, `CMPLX`, `CONST` |
| `MTH/VECTR` | `ABS`, `DOT`, `CROSS`, `V→`, `→V2`, `→V3`, `RECT`, `CYLIN`, `SPHERE` |
| `MTH/MATR/MAKE` | `CON`, `IDN`, `TRN`, `RDM`, `RANM`, `SIZE`, `GET`, `GETI`, `PUT`, `PUTI`, `SUB`, `REPL` |
| `MTH/MATR/NORM` | `ABS`, `SNRM`, `RNRM`, `CNRM`, `SRAD`, `COND`, `RANK`, `DET`, **`TRACE` = Matrixspur** |
| `MTH/MATR/FACTR` | `RREF`, `LU`, `LQ`, `QR`, `SCHUR`, `SVD`, `SVL` |
| `MTH/MATR/COL` / `ROW` | `→COL`, `COL→`, `COL+`, `COL-`, `CSWP`; `→ROW`, `ROW→`, `ROW+`, `ROW-`, `RCI`, `RCIJ`, `RSWP` |
| `MTH/LIST` | `ΔLIST`, `ΣLIST`, `ΠLIST`, `SORT`, `REVLIST`, `ADD` |
| `MTH/HYP` | Hyperbolische und inverse Funktionen plus `EXPM`/`LNP1` |
| `MTH/PROB` | `COMB`, `PERM`, `!`, `RAND`, `RDZ`, `UTPC`, `UTPF`, `UTPN`, `UTPT`, `NDIST` |
| `MTH/REAL` | Prozent, Maximum/Minimum, Modul, Signum, Mantisse/Exponent, Ganz-/Bruchteil, Runden/Trunkieren, `FLOOR`/`CEIL`, Grad/Rad |
| `MTH/BASE` | HEX/DEC/OCT/BIN, `R→B`/`B→R`, `LOGIC`, `BIT`, `BYTE`, Wortlänge `STWS`/`RCWS` |
| `MTH/FFT` | `FFT`, `IFFT` |
| `MTH/CMPLX` | `RE`, `IM`, `C→R`, `R→C`, `ABS`, `ARG`, `SIGN`, `NEG`, `CONJ` |
| `PRG/BRCH` | `IF/THEN/ELSE/END`, `CASE`, `START/NEXT/STEP`, `FOR/NEXT/STEP`, `DO/UNTIL`, `WHILE/REPEAT`, `IFT`/`IFTE` |
| `PRG/TEST` | Relationen, Boolesch, Flags, `SAME`, `TYPE`, `LININ` |
| `PRG/TYPE` | Objektzerlegung, Arrays, Listen, Text, Tags, Einheiten, Typabfrage, `EQ→`, `CHR`/`NUM` |
| `PRG/LIST/ELEM` | `GET`, `GETI`, `PUT`, `PUTI`, `SIZE`, `POS`, `HEAD`, `TAIL` |
| `PRG/LIST/PROC` | `DOLIST`, `DOSUBS`, `NSUB`, `ENDSUB`, `STREAM`, `REVLIST`, `SORT`, `SEQ` |
| `PRG/GROB` | `→GROB`, `BLANK`, `GOR`, `GXOR`, `SUB`, `REPL`, `→LCD`, `LCD→`, `SIZE`, `ANIMATE` |
| `PRG/PICT` | `PICT`, `PDIM`, `LINE`, `TLINE`, `BOX`, `ARC`, Pixel setzen/löschen/testen, Koordinaten wandeln |
| `PRG/IN` | `INFORM`, `NOVAL`, `CHOOSE`, `INPUT`, `KEY`, `WAIT`, `PROMPT` |
| `PRG/OUT` | `PVIEW`, `TEXT`, `CLLCD`, `DISP`, `FREEZE`, `MSGBOX`, `BEEP` |
| `PRG/RUN` | **UI-only** `DBUG`, `SST`, `SST↓`, `NEXT` sowie `HALT`, `CONT`, `KILL`, `OFF` |
| `PRG/ERROR` | `DOERR`, `ERRN`, `ERRM`, `ERR0`, `LASTARG`, `IFERR`-Struktur |
| `CHAR/CHARS` | `SUB`, `REPL`, `POS`, `SIZE`, `NUM`, `CHR`, `OBJ→`, `→STR`, `HEAD`, `TAIL` |
| `MODES/FMT` | `STD`, `FIX`, `SCI`, `ENG`, Dezimaltrennzeichen, Formatdialog |
| `MODES/ANGL` | `DEG`, `RAD`, `GRAD`, `RECT`, `CYLIN`, `SPHERE` |
| `MODES/FLAG` | `SF`, `CF`, `FS?`, `FC?`, `FS?C`, `FC?C`, `STOF`, `RCLF`, `RESET`-Dialog |
| `MODES/KEYS` / `MENU` / `MISC` | `ASN`, Tastenbelegung löschen/speichern; `MENU`, `TMENU`, `RCLMENU`; Beep/Uhr/Undo- und Anzeigeoptionen |
| `MEMORY` / `DIR` / `ARITH` | `MEM`, `BYTES`, `NEWOB`, `ARCHIVE`, `RESTORE`; `PATH`, `CRDIR`, `PGDIR` (= Verzeichnis löschen), `VARS`, `TVARS`, `ORDER`; `STO±/*/÷`, `INCR`, `DECR`, `SINV`, `SNEG`, `SCONJ` |
| `STACK` | `OVER`, `ROT`, `ROLL`, `ROLLD`, `PICK`, `DEPTH`, `DUP`, `DUP2`, `DUPN`, `DROP2`, `DROPN`, `SWAP`, `DROP` |
| `SOLVE/ROOT` | `SOLVR`-Eingabemaske, `ROOT`, Eingabe-/Änderung der reservierten Variable `EQ` |
| `SOLVE/DIFFE` | `RKF`, `RRK`, `RKFSTEP`, `RRKSTEP`, `RKFERR`, `RSBERR` |
| `SOLVE/POLY` / `SYS` / `TVM` | Polynomnullstellen/-koeffizienten, LGS, LSQ/RSD; historischer TVM-Solver/Amortisation als **separat zu verwaltender SASD-Produktbereich** |
| `SYMBOLIC` | `COLCT`, `EXPAN`, `ISOL`, `QUAD`, `SHOW`, `TAYLR`, `↑MATCH`, `↓MATCH`, `→Q`, `→Qπ`, `|`, `APPLY`, `QUOTE` |
| `PLOT/PTYPE` / `3D/PTYPE` | Alle 15 im nächsten Abschnitt einzeln aufgeführten Plottypen |
| `PLOT/PPAR` | `INDEP`, `DEPND`, `XRNG`, `YRNG`, `RES`, Reset/Info, `CENTR`, `SCALE`, `*W`, `*H`, `AXES`, `ATICK` |
| `PLOT/3D/VPAR` | `XVOL`, `YVOL`, `ZVOL`, `XXRNG`, `YYRNG`, `EYEPT`, `NUMX`, `NUMY` und Parameterdialog |
| `STAT/DATA` / `ΣPAR` | Daten importieren/erfassen, `Σ+`, `Σ-`, `CLΣ`, Datenauswahl `ΣDAT`, `XCOL`/`YCOL`, Fit-Modell |
| `STAT/1VAR` | `TOT`, `MEAN`, `SDEV`, `MAXΣ`, `MINΣ`, `BINS`, `VAR`, `PSDEV`, `PVAR` |
| `STAT/FIT` / `SUMS` | `ΣLINE`, `LR`, `PREDX`, `PREDY`, `CORR`, `COV`, `PCOV`; `ΣX`, `ΣY`, `ΣX^2`, `ΣY^2`, `ΣX*Y`, `NΣ` |
| `STAT/PLOT` | `BARPLOT`, `HISTPLOT`, `SCATRPLOT` |
| `TIME` / `ALRM` | Datum, Uhrzeit, Ticks, Formatumwandlung, Intervalle, Kalenderarithmetik, Alarme suchen/setzen/löschen/quittieren |
| `I/O` / `SERIAL` | `OPENIO`, `CLOSEIO`, `XMIT`, `SRECV`, `STIME`, `SBRK`, `BUFLEN`, serielle Parameter |
| `I/O` / `IOPAR` / `SRVR` | IR/Wire, ASCII/Binary, Baud, Parität, Prüfsumme, Übersetzung, Kermit-Server, `SEND`/`RECV`, XModem |
| `I/O` / `PRINT` | `PRVAR`, `PRST`, `PRSTC`, `PRLCD`, `CR`, `PR1`, Druckparameter/-verzögerung |
| `LIBRARY` / `PORTS` | `:0:`, `:1:`, `:2:` und weitere verfügbare Ports, `PVARS`, `LIBS`, `MERGE1`, `FREE1`, `ATTACH`, `DETACH` |
| `UNITS` | 16 Untermenüs (nachstehend mit Einheitenbezeichnungen) und `CONVERT`, `UBASE`, `UFACT`, `UVAL`, `→UNIT` |
| `EQ LIB` | `EQLIB` (15 Themen), `COLIB` (Konstanten), `MES` (Mehrgleichungslöser), `UTILS` (spezielle Formeln und Spiel) |

**Regel für die Umsetzung:** Menüknöpfe wie `RESET`, `INFO`, `COPY`, `CANCL`, `EDIT`, `DBUG`, `ZOOM`, `ISECT`, `SLOPE`, `AREA` usw. werden als **Bedienaktionen** erfasst und nicht fälschlich zu neuen programmierbaren XLIB-Befehlen umdeklariert.

### 2a.5 PICTURE und Graphik: **zusätzliche interaktive Funktionen**

| Bereich | Bedienaktionen im Original (nicht alle separat programmierbar) |
| --- | --- |
| PICTURE / Grundansicht | `ZOOM`, Koordinatenanzeige `(X,Y)`, grafisches `TRACE`, `FCN`, `EDIT`, `CANCL`, Scrollen |
| Zoom | `ZFACT`, `BOXZ`, `ZIN`, `ZOUT`, `ZSQR`, `ZDFLT`, `HZIN`, `HZOUT`, `VZIN`, `VZOUT`, `CNTR`, `ZAUTO`, `ZDECI`, `ZINTG`, `ZTRIG`, `ZLAST` |
| Grafische Analyse `FCN` | `ROOT` (Nullstelle), `ISECT` (Schnittpunkt), `SLOPE` (Steigung), `AREA` (Fläche), `SHADE` (Schraffur), `EXTR` (Extremum), `F(X)` (Funktionswert), `F'` (Ableitung), `TANL` (Tangente), `NXEQ` (nächste Gleichung), `VIEW` |
| PICTURE-Editor | `DOT+`, `DOT-`, `LINE`, `TLINE`, `BOX`, `CIRCL`, `MARK`, `+/−`, `LABEL`, `DEL`, `ERASE`, `MENU`, `SUB`, `REPL`, `PICT→`, `X,Y→` |
| Plotparameter | Freie Achsenwahl, Skalierung, Achsenschnitt, benannte Kurven, Gitter, Koordinaten-/Pixelvergleich, Nachzeichnen ohne Datenverlust |

**Wichtiger Kollisionsfall:** Der ROM-Befehl **`TRACE` ist die Spur einer quadratischen Matrix**, also die Summe ihrer Diagonalelemente. Die **gleichnamige interaktive Kurvenverfolgung im Grafikmodus** ist eine *andere Operation*. Ebenso sind `ROOT` (programmierbarer numerischer Löser) und `ROOT` in `PICTURE/FCN` nicht ohne Kontext gleichzusetzen.

### 2a.6 Alle **15 Plottypen**, getrennt von den einzelnen Bedienaktionen

| Nr. | Originaltyp | Inhalt |
| --- | --- | --- |
| 1 | `FUNCTION` | y=f(x), auch mehrere Kurven |
| 2 | `CONIC` | Kegelschnitte / implizite Kurven |
| 3 | `POLAR` | Polargleichungen |
| 4 | `PARAMETRIC` | Parametrisierte Kurven |
| 5 | `TRUTH` | Boolesche/implizite Wahrheitswertbereiche |
| 6 | `DIFFEQ` | Kurven von Differentialgleichungen |
| 7 | `SLOPEFIELD` | Richtungsfeld |
| 8 | `WIREFRAME` | Räumliches Drahtgitter |
| 9 | `YSLICE` | Schnitt-Darstellung mit y |
| 10 | `PCONTOUR` | Pseudokontur |
| 11 | `GRIDMAP` | Dreidimensionale Gitternetz-Abbildung |
| 12 | `PARSURFACE` | Parametrische Fläche |
| 13 | `BAR` | Balkendiagramm |
| 14 | `HISTOGRAM` | Histogramm |
| 15 | `SCATTER` | Streudiagramm |

### 2a.7 Einheiten: sämtliche **16 historisch eingebauten Menügruppen**

Die Kurzanleitung zeigt lediglich das UNITS-Menü; die vollständige Menüaufteilung und Namen müssen aus dem **HP-48G-User's-Guide-Anhang E / AUR-Anhang B** und den historischen GX-Menüübersichten stammen. Die folgende Bestandsaufnahme enthält die im Zweitindex sichtbaren Menüsymbole; aus Kompatibilitätsgründen sind Abweichungen zwischen **Anzeigekürzel, kanonischer Eingabeschreibweise und Umrechnungsfaktor** später gesondert abzugleichen (z. B. `A` für Ångström und Ampere je Kontext, `R`/ `rad`/ `°R`; Groß-/Kleinschreibung beachten).

| Menü | Im historischen Menü sichtbare Einheitentypen / Bezeichnungen |
| --- | --- |
| LENG – Länge | `m`, `cm`, `mm`, `yd`, `ft`, `in`, `Mpc`, `pc`, `lyr`, `au`, `km`, `mi`, `nmi`, `miUS`, `chain`, `rd`, `fath`, `ftUS`, `mil`, `μm`, `Å`, `fermi` |
| AREA – Fläche | `m²`, `cm²`, `b`, `yd²`, `ft²`, `in²`, `km²`, `ha`, `a`, `mi²`, `miUS²`, `acre` |
| VOL – Volumen | `m³`, `st`, `cm³`, `yd³`, `ft³`, `in³`, `l`, `galUK`, `galC`, `galUS`, `qt`, `pt`, `ml`, `cu`, `flozUS`, `flozUK`, `tbsp`, `tsp`, `bbl`, `bu`, `pk`, `fbm` |
| TIME – Zeit und Frequenz | `yr`, `d`, `h`, `min`, `s`, `Hz` |
| SPEED – Geschwindigkeit | `m/s`, `cm/s`, `ft/s`, `kph`, `mph`, `knot`, `c`, `ga` |
| MASS – Masse/Stoffmenge | `kg`, `g`, `lb`, `oz`, `slug`, `lbt`, `ton`, `tonUK`, `t`, `ozt`, `ct`, `grain`, `u`, `mol` |
| FORCE – Kraft | `N`, `dyn`, `gf`, `kip`, `lbf`, `pdl` |
| ENRG – Energie | `J`, `erg`, `kcal`, `cal`, `Btu`, `ft·lbf`, `therm`, `MeV`, `eV` |
| POWR – Leistung | `W`, `hp` |
| PRESS – Druck | `Pa`, `atm`, `bar`, `psi`, `torr`, `mmHg`, `inHg`, `inH₂O` |
| TEMP – Temperatur | `°C`, `°F`, `K`, `°R` |
| ELEC – Elektrische/magnetische Größen | `V`, `A`, `C`, `Ω`, `F`, `W`, `Fdy`, `H`, `mho`, `S`, `T`, `Wb` |
| ANGL – Winkel | `°`, `rad`, `grad`, `arcmin`, `arcsec`, `sr` |
| LIGHT – Photometrie | `fc`, `flam`, `lx`, `ph`, `sb`, `lm`, `cd`, `lam` |
| RAD – Strahlung | `Gy`, `rad`, `rem`, `Sv`, `Bq`, `Ci`, `R` |
| VISC – Viskosität | `P`, `St` |

**Zusätzliche nicht bloß aus einem Menü-Label ableitbare Funktionen:** SI-Vorsätze, Einheitenprodukte/Quotienten/Potenzen, dimensionsbehaftete Rechnungen, dimensionsfremde Fehlermeldungen, `UBASE`, `UFACT`, `UVAL`, `CONVERT`, `→UNIT`, die besondere Temperaturbehandlung mit `TDELTA`/`TINC`, benutzerdefinierte Einheiten als Variablen und Einheitenanzeige im SOLVE/EQ-LIB-Kontext. Die obigen 148 notierten Menüpositionen enthalten teils wiederkehrende oder kontextabhängige Zeichen (z. B. `W`, `rad`). Es handelt sich um einen **Rechercheindex**, **keine abschließend verifizierte 1:1-Liste der 147 eingebauten Einheitendefinitionen und keine geprüfte numerische Tabelle** aller Umrechnungsfaktoren; solche Faktoren einschließlich Offset/Skala und Rundung erfordern gesonderte Referenztests.

### 2a.8 Equation Library: alle **15 eingebauten Themengebiete** mit ihren Problemüberschriften

Nach der Originaltabelle in *HP 48G Series User's Guide*, Anhang F, F-1 bis F-3, besitzt die eingebaute GX-Gleichungsbibliothek **exakt 315 Gleichungen mit 396 Variablen**, geordnet in 15 Fachgebiete und 102 Problemüberschriften. **Eine Problemüberschrift kann mehrere Formeln beinhalten.** Darum ist die folgende Liste eine vollständige Übersicht der in der herangezogenen GX-Themenübersicht benannten **102 Problemüberschriften**, nicht eine Abschrift der 315 urheberrechtlich geschützten Originalformeln.

| Nr. / Themengebiet | Problemüberschriften | Gleichungen | Variablen | Originaltitel der eingebauten Problemgruppen |
| --- | ---: | ---: | ---: | --- |
| 1. Stützen und Balken / Columns and Beams | 10 | 14 | 20 | `Elastic Buckling`; `Eccentric Columns`; `Simple Deflection`; `Simple Slope`; `Simple Moment`; `Simple Shear`; `Cantilever Deflection`; `Cantilever Slope`; `Cantilever Moment`; `Cantilever Shear` |
| 2. Elektrizität / Electricity | 23 | 42 | 56 | `Coulomb's Law`; `Ohm's Law and Power`; `Voltage Divider`; `Current Divider`; `Wire Resistance`; `Series and Parallel R`; `Series and Parallel C`; `Series and Parallel L`; `Capacitive Energy`; `Inductive Energy`; `RLC Current Delay`; `DC Capacitor Current`; `Capacitor Charge`; `DC Inductor Voltage`; `RC Transient`; `RL Transient`; `Resonant Frequency`; `Plate Capacitor`; `Cylindrical Capacitor`; `Solenoid Inductance`; `Toroid Inductance`; `Sinusoidal Voltage`; `Sinusoidal Current` |
| 3. Strömungslehre / Fluids | 4 | 29 | 29 | `Pressure at Depth`; `Bernoulli Equation`; `Flow with Losses`; `Flow in Full Pipes` |
| 4. Kräfte und Energie / Forces and Energy | 8 | 31 | 36 | `Linear Mechanics`; `Angular Mechanics`; `Centripetal Force`; `Hooke's Law`; `1D Elastic Collisions`; `Drag Force`; `Law of Gravitation`; `Mass-Energy Relation` |
| 5. Gase / Gases | 8 | 18 | 26 | `Ideal Gas Law`; `Ideal Gas State Change`; `Isothermal Expansion`; `Polytropic Processes`; `Isentropic Flow`; `Real Gas Law`; `Real Gas State Change`; `Kinetic Theory` |
| 6. Wärmeübertragung / Heat Transfer | 6 | 17 | 31 | `Heat Capacity`; `Thermal Expansion`; `Conduction`; `Convection`; `Conduction + Convection`; `Black Body Radiation` |
| 7. Magnetismus / Magnetism | 4 | 4 | 14 | `Straight Wire`; `Force Between Wires`; `B Field in Solenoid`; `B Field in Toroid` |
| 8. Bewegung / Motion | 7 | 22 | 24 | `Linear Motion`; `Object in Free Fall`; `Projectile Motion`; `Angular Motion`; `Circular Motion`; `Terminal Velocity`; `Escape Velocity` |
| 9. Optik / Optics | 6 | 11 | 14 | `Law of Refraction`; `Critical Angle`; `Brewster's Law`; `Spherical Reflection`; `Spherical Refraction`; `Thin Lens` |
| 10. Schwingungen / Oscillations | 5 | 17 | 17 | `Mass-Spring System`; `Simple Pendulum`; `Conical Pendulum`; `Torsional Pendulum`; `Simple Harmonic` |
| 11. Ebene Geometrie / Plane Geometry | 6 | 31 | 21 | `Circle`; `Ellipse`; `Rectangle`; `Regular Polygon`; `Circular Ring`; `Triangle` |
| 12. Räumliche Geometrie / Solid Geometry | 4 | 18 | 12 | `Cone`; `Cylinder`; `Parallelepiped`; `Sphere` |
| 13. Halbleiter / Solid State Devices | 4 | 33 | 53 | `PN Step Junctions`; `NMOS Transistors`; `Bipolar Transistors`; `JFETs` |
| 14. Spannungsanalyse / Stress Analysis | 4 | 16 | 28 | `Normal Stress`; `Shear Stress`; `Stress on an Element`; `Mohr's Circle` |
| 15. Wellen / Waves | 3 | 12 | 15 | `Transverse Waves`; `Longitudinal Waves`; `Sound Waves` |

**Kontrollsummen aus der gedruckten Quelle:** 15 Fachgebiete, **102 Problemüberschriften**, **315 einzelne Gleichungen**, **396 Variablen**. Nachweis: [HP 48G Series User's Guide, Anhang F, Seiten F-1–F-3](https://www.hp.com/ctg/Manual/c00442262.pdf). Die Summen der 15 Zeilen stimmen mit den von HP angegebenen Gesamtzahlen überein. Die 315 einzelnen Formeln sind **noch nicht** semantisch einzeln verifiziert; dies bleibt ein anderer Auditumfang.

**Equation-Library-Bedienungen:** EQLIB-Katalog öffnen, Themengebiet auswählen, Problemtyp auswählen, Gleichung/Lösungsvariable wählen, Eingabeformulare mit Einheiten öffnen, Solver ausführen, Ergebnisse auf Stack/Variablen anwenden, Variablen zurücksetzen, Bilder/Diagramme ansehen, Einheiten berücksichtigen, Konstantenbibliothek öffnen, `MES`/Mehrgleichungslöser benutzen, mathematische Hilfsfunktionen aus `UTILS` ausführen. In der Bibliothek sind **40 physikalische Konstanten** zusätzlich als historische Datensammlung dokumentiert (keine 40 neuen Befehlsnamen). Die **einzelnen Formelzeichen, Variablenwerte, Illustrationen und numerischen Konstanten** sind noch nicht als unabhängige Prüfdatensätze eingetragen. Proprietäre HP-Grafiken/ROMs werden nicht ins SASD-Repository kopiert.

### 2a.9 Reservierte Objekte, Systemvariablen und Speicherzustand

| Name / Familie | Rolle, die bei historischer Kompatibilität zu berücksichtigen ist |
| --- | --- |
| `HOME`, Unterverzeichnisse | Objekt-/Variablen-Namensraum; globaler Pfad, lokale Variablen |
| `EQ` | Aktuelle Gleichung bzw. Ausdruck für SOLVE und Plot |
| `PPAR` | 2D-Plotparameter, Bereich, Achsen, unabhängige/abhängige Variable |
| `VPAR` | 3D-Plotparameter und Betrachtungsraum |
| `ΣDAT` | Statistik-Datenmatrix |
| `ΣPAR` | Statistikparameter, Spalten, Modell |
| `PICT` | Aktueller Grafikpuffer |
| `IOPAR` | Schnittstellen-/Übertragungsparameter |
| `PRTPAR` | Druckparameter |
| `CST` | Benutzerdefinierte Menüstruktur |
| `ALRMDAT` | Alarm-/Termindatensätze |
| `IERR` | Integrationsfehler-/Genauigkeitsvariable |
| `EXPR` | Algebraischer Ausdruck in EQW-Kontext |
| `Mpar`, `MHpar` | Solver-/MINEHUNT-Kontextparameter |
| `Nmines` | MINEHUNT-Spielparameter |
| `n1`, `n2`, … sowie `s1`, `s2`, … | Hilfsnamen symbolischer Auflösungen |
| `der…` | Benutzerdefinierte Ableitungsregeln |
| `LAST CMD`, `LAST STACK`, `LAST ARG` | Rückrufhistorie mit flagabhängiger Aktivierung |
| Port `0`, Kartenport `1`, Kartenports `2` bis `33` | Interne bzw. optionale externe Speicherräume; GX-Portlayout beachten |

**Historischer Datenmodell-Testbedarf:** Objektprolog, Nibblelänge, atomare/zusammengesetzte Typen, Präzisionsformat, Typprüfung, globale/lokale Namensbindung, Wortlänge von Binärzahlen, Algebraic-Lazy-Evaluation, Flagsystem, Speicherbereinigung, Zugriffspfad für Bibliotheken, Port-Backup-Objekte und kontrolliertes Fehlerverhalten. Für `SYSEVAL`/`LIBEVAL` nur virtuelle, explizit erlaubte Kommandoregister; **keine** Host-Pointer.

### 2a.10 Numerische und programmierte Bedienfälle, die oft vergessen werden

- **Eingabe und Stack:** Stackscrollen, dynamische Tiefe, `ENTER`, `LASTARG` und `UNDO`, Zahleneingabe-/EEX-Zustand, Stack-Browser, Objekte mit und ohne Auswertung, Zwischenresultate und Fehlerzustand.
- **Editoren:** `EDIT`, `VIEW`, `CMD`, `PURG`, Cursor zu Anfang/Ende bzw. über mehrere Zeilen, Einfügen/Überschreiben, Auswahl eines Teilausdrucks, Unterausdrücke klammern/entklammern, `SUB`/`REPL`.
- **EquationWriter-Regelmenü:** `RULES` *als interaktives Untermenü im EquationWriter* eröffnet eine Vielzahl einzelner Umformungsaktionen (z. B. doppelte Negation, Inversion, Einserneutralität, Klammerung, distributive Regeln, trigonometrische Identitäten, Expandieren und Zusammenfassen). **Nicht verwechseln mit dem eingebauten RPL-Namen `RULES`**, der historisch auch als undokumentierte Entwickler-Spielerei referenziert wird; Befehl und Menüpunkt sind gesondert zu testen.
- **Grafik und numerisches Lösen:** `ROOT`, `ISECT`, `SLOPE`, `AREA`, `F(X)`, `F'`, `TANL`, `NXEQ`, vier Zoomrichtungen, Standardzoom, Spezialskalierungen und Grafikkursor nicht mit gleichnamigen Stackbefehlen verwechseln.
- **User RPL:** Programme anlegen/editieren/speichern/aufrufen, Verzweigungen, lokale Variablen, Listen über mehreren Typen auswerten, `DEBUG`-Oberfläche, `SST`/`SST↓`-/Einzelschritt und Stopp; Zwischenstände ausgeben, Tastatur oder Formular abfragen, Alarmaktionen/Softwarekeys.
- **Statistik:** Einzelwert- und Paarstatistik, Kolonnenparameter, Fit-Modellauswahl, Histogrammklassen, gewichtete/komplexe Eingabetypen, Streuung, Regressionsprognose, grafische Auswertung.
- **Basisarithmetik:** Vorzeichenbehandlung, Wortlängen von 1 bis 64 Bit, Überläufe, Schiebe-/Rotate-Befehle auf Bit-/Bytebasis, logische/bitweise Operatoren; `HEX/DEC/BIN/OCT` steuern **Anzeige**, nicht stets Konvertierung eines `real`-Objekts.
- **Datensicherung und Hardware:** Ein-/Ausschalten mit Zustandswiederherstellung, Option Alarm aufwecken, Batteriesignal, Kontrast, serielle/IR-Parameter, Druckerkompatibilität, selbsttätige Speicherbereinigung, Speicherkarten-Hotplug/Portkonfiguration unter historischen Hardwarebedingungen.
- **Sonderfälle:** Eingebaute `TEACH`/`CLTEACH`-Beispielobjekte; `MINEHUNT`; internes `RULES`; von Anwendern installierte ROM-Bibliotheken in Port 1/2 sind **nicht Bestandteil des Grundgeräts**.

### 2a.11 Korrigierte semantische Besonderheiten – verbindlich für alle späteren Tests

| Name | Richtige Unterscheidung | Fehlerquelle |
| --- | --- | --- |
| `→COL` / `COL→` | `→COL` zerlegt Array in Spalten; `COL→` baut Array aus Spalten | Bei umgekehrter Übersetzung sind Tests systematisch falsch |
| `→ROW` / `ROW→` | `→ROW` zerlegt Array in Zeilen; `ROW→` baut Array aus Zeilen | Gleiche Asymmetrie |
| `→DIAG` / `DIAG→` | `→DIAG` liefert Diagonalelemente; `DIAG→` erzeugt Diagonalmatrix | Gegenrichtung ist leicht zu verwechseln |
| `TRACE` / Grafik-`TRACE` | RPL-`TRACE` = Matrixspur; Grafik-`TRACE` = interaktive Kurvenverfolgung | Gleiche Aufschrift, zwei Kontexte |
| `PGDIR` / `UPDIR` | `PGDIR` löscht ein Verzeichnis; `UPDIR` navigiert ins Elternverzeichnis | Verwechslung ist potentiell datenzerstörend |
| `PINIT` | Speicherport initialisieren; **nicht** beliebige Plotparameter | Besonders relevant bei GX-Erweiterungskarten |
| `CKSM` | Kermit-Prüfsummeneinstellung; **nicht** abstrakte Datei-Hashfunktion | I/O-Protokollsemantik |
| `FACT` / `!` | Beide stehen im GX für Fakultät/Gamma-Zusammenhang; **nicht** Primfaktorzerlegung | Späteres CAS-Vokabular anderer Modelle |
| `RULES` (Befehl) / EquationWriter-`RULES` (Menü) | Nicht denselben internen Einstiegspunkt oder Semantik unterstellen | Benutzeroberfläche und versteckte Sonderfunktion |

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
| `→COL` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zerlegt ein Array in seine Spalten und liefert die Spaltenanzahl. | `171:67` | MTH MATRX COL |
| `→DATE` | Zeit, Kalender, Wecker | Datum setzen. | `2:22` | MENU 94 |
| `→DIAG` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Liefert die Hauptdiagonale einer Matrix als Vektor. | `171:69` | MTH MATRX |
| `→GROB` | Grafik, Diagramme und Plotparameter | Objekt als Grafikobjekt darstellen. | `2:215` | PRG GROB |
| `→HMS` | Grundrechnen, elementare Funktionen und Zahlen | Dezimalzeit in Stunden-Minuten-Sekunden-Darstellung. | `2:114` | MENU 94 |
| `→LCD` | Grafik, Diagramme und Plotparameter | Grafikobjekt auf LCD darstellen. | `2:214` | PRG GROB |
| `→LIST` | Listen, Strings, Objektkonversion | Liste aus Stackobjekten erzeugen. | `2:152` | PRG TYPE; PRG LIST |
| `→NUM` | Stack und User-RPL-Programmsteuerung | Numerische Auswertung eines symbolischen Objekts erzwingen; nicht Zeichencode wie NUM. | `2:53` | ohne Menüeintrag |
| `→Q` | Symbolische Mathematik, Solver und Differentialgleichungen | Wandelt eine Zahl in einen äquivalenten rationalen Bruch um. | `2:263` | MENU 93 |
| `→Qπ` | Symbolische Mathematik, Solver und Differentialgleichungen | Wählt zwischen einer rationalen Näherung der Zahl und einem rationalen Vielfachen von π nach kleinerem Nenner. | `2:264` | MENU 93 |
| `→ROW` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zerlegt ein Array in seine Zeilen und liefert die Zeilenanzahl. | `171:65` | MTH MATRX ROW |
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
| `ADD` | Listen, Strings, Objektkonversion | Addiert Listenelemente paarweise oder einen Einzelwert zu jedem Listenelement; dies ist von der typabhängigen Operation `+` zu unterscheiden. | `171:108` | MTH LIST |
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
| `AXES` | Grafik, Diagramme und Plotparameter | Legt Ursprung, Achsenmarkierungen und Achsenbeschriftungen im Plotparameterobjekt fest. | `2:186` | ohne Menüeintrag |
| `B→R` | Binärzahlen, Logik, Modi, Systemflags | Binäre Ganzzahl nach reell. | `2:10` | MTH BASE |
| `BAR` | Grafik, Diagramme und Plotparameter | Balkendiagramm aktivieren. | `2:227` | ohne Menüeintrag |
| `BARPLOT` | Grafik, Diagramme und Plotparameter | Balkendiagramm erstellen. | `2:316` | MENU 96 PLOT |
| `BAUD` | Schnittstellen, Drucker, Display und Tastenbelegung | Baudrate konfigurieren. | `2:370` | ohne Menüeintrag |
| `BEEP` | Schnittstellen, Drucker, Display und Tastenbelegung | Gibt einen Ton mit vorgegebener Frequenz und Dauer aus. | `2:52` | PRG OUT |
| `BESTFIT` | Statistik, Verteilungen und Regression | Bestes Fit-Modell auswählen. | `2:323` | ohne Menüeintrag |
| `BIN` | Binärzahlen, Logik, Modi, Systemflags | Binäre Anzeigeform. | `2:144` | MTH BASE |
| `BINS` | Statistik, Verteilungen und Regression | Daten für Histogramm klassieren. | `2:315` | MENU 96 1VAR |
| `BLANK` | Grafik, Diagramme und Plotparameter | Leeres Grafikobjekt erzeugen. | `2:209` | PRG GROB |
| `BOX` | Grafik, Diagramme und Plotparameter | Rechteck zeichnen. | `2:208` | PRG PICT |
| `BUFLEN` | Schnittstellen, Drucker, Display und Tastenbelegung | Bestimmt die Zeichenanzahl im seriellen Empfangspuffer und einen Status der Empfangsdaten (Stackdetails noch AUR-prüfpflichtig). | `2:374` | MENU 104 SERIAL |
| `BYTES` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Speichergröße und Prüfsumme eines Objekts ermitteln. | `2:38` | MENU 70 |
| `C→PX` | Grafik, Diagramme und Plotparameter | Benutzerkoordinaten in Pixelkoordinaten wandeln. | `2:199` | PRG PICT |
| `C→R` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Komplexe Zahl in Komponenten zerlegen. | `2:159` | MTH CMPLX; PRG TYPE |
| `CASE` | Stack und User-RPL-Programmsteuerung | Fallunterscheidung beginnen. | `1792:25` | PRG BRCH CASE |
| `CEIL` | Grundrechnen, elementare Funktionen und Zahlen | Aufrunden zur nächsten ganzen Zahl. | `2:104` | MTH REAL |
| `CENTR` | Grafik, Diagramme und Plotparameter | Plotansicht zentrieren. | `2:187` | ohne Menüeintrag |
| `CF` | Binärzahlen, Logik, Modi, Systemflags | Flag löschen. | `2:132` | PRG TEST; MENU 63 FLAG |
| `CHOOSE` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Auswahlliste anzeigen. | `171:92` | PRG IN |
| `CHR` | Listen, Strings, Objektkonversion | Zeichen aus Zeichencode erzeugen. | `2:165` | PRG TYPE; MENU 62 |
| `CKSM` | Schnittstellen, Drucker, Display und Tastenbelegung | Wählt das Prüfsummenverfahren für den Kermit-Datentransfer. | `2:369` | ohne Menüeintrag |
| `CLEAR` | Stack und User-RPL-Programmsteuerung | Stack leeren. | `2:282` | ohne Menüeintrag |
| `CLKADJ` | Zeit, Kalender, Wecker | Uhrengang anpassen. | `2:24` | MENU 94 |
| `CLLCD` | Schnittstellen, Drucker, Display und Tastenbelegung | LCD-Inhalt löschen. | `2:56` | PRG OUT |
| `CLOSEIO` | Schnittstellen, Drucker, Display und Tastenbelegung | Schließt die seriellen/IR-Schnittstellen und löscht den Eingangspuffer sowie Kermit-Fehlerinformationen. | `2:362` | MENU 104 |
| `CLTEACH` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Lehrbeispielobjekte entfernen. | `171:18` | ohne Menüeintrag |
| `CLVAR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Löscht die Variablen und leeren Unterverzeichnisse im aktuellen Verzeichnis; Fehlerverhalten bei nichtleeren Unterverzeichnissen noch gegen die AUR prüfen. | `2:346` | ohne Menüeintrag |
| `CLΣ` | Statistik, Verteilungen und Regression | Löscht den in `ΣDAT` gespeicherten Statistikdatensatz. | `2:284` | MENU 87 DATA; MENU 96 DATA |
| `CNRM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Spaltennorm einer Matrix. | `2:119` | MTH MATRX NORM |
| `COL-` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Entfernt eine Spalte bzw. bei Vektoren ein Element an einer angegebenen Position. | `171:73` | MTH MATRX COL |
| `COL→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Bildet ein Array aus vorliegenden Spaltenobjekten. | `171:68` | MTH MATRX COL |
| `COL+` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Fügt eine oder mehrere Spalten bzw. bei Vektoren Elemente an einer angegebenen Position ein. | `171:74` | MTH MATRX COL |
| `COLCT` | Symbolische Mathematik, Solver und Differentialgleichungen | Algebraischen Ausdruck zusammenfassen. | `2:333` | MENU 93 |
| `COLΣ` | Statistik, Verteilungen und Regression | Wählt abhängige und unabhängige Datenspalten in `ΣDAT` (HP User's Guide G-8 / H-4); keine Spaltensumme. | `2:312` | ohne Menüeintrag |
| `COMB` | Grundrechnen, elementare Funktionen und Zahlen | Kombinationen berechnen. | `2:129` | MTH PROB |
| `CON` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Erzeugt ein Array der angegebenen Dimensionen mit einem konstanten Wert; die Dimension kann auch als Array vorliegen. | `2:173` | MTH MATRX MAKE |
| `COND` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Konditionszahl bestimmen. | `171:49` | MTH MATRX NORM |
| `CONIC` | Grafik, Diagramme und Plotparameter | Kegelschnittplot aktivieren. | `2:221` | ohne Menüeintrag |
| `CONJ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Konjugiert eine komplexe Zahl oder ein komplexes Array. | `2:62` | MTH CMPLX |
| `CONLIB` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Konstantenbibliothek starten. | `171:32` | MENU 113 COLIB |
| `CONST` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Physikalische Konstante auswählen. | `171:33` | MENU 113 COLIB |
| `CONT` | Stack und User-RPL-Programmsteuerung | Angehaltenes Programm fortsetzen. | `2:58` | ohne Menüeintrag |
| `CONVERT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Maßeinheit umrechnen. | `2:11` | MENU 59 |
| `CORR` | Statistik, Verteilungen und Regression | Korrelationskoeffizient. | `2:289` | MENU 96 FIT |
| `COS` | Grundrechnen, elementare Funktionen und Zahlen | Kosinus. | `2:82` | ohne Menüeintrag |
| `COSH` | Grundrechnen, elementare Funktionen und Zahlen | Cosinus hyperbolicus. | `2:85` | MTH HYP |
| `COV` | Statistik, Verteilungen und Regression | Stichprobenkovarianz. | `2:290` | MENU 96 FIT |
| `CR` | Schnittstellen, Drucker, Display und Tastenbelegung | Gibt den Inhalt des Druckerpuffers aus; nicht lediglich ein Zeilenumbruch. | `2:243` | MENU 104 PRINT |
| `CRDIR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Unterverzeichnis erstellen. | `2:32` | MENU 70 DIR |
| `CROSS` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet das Kreuzprodukt geeigneter zwei- oder dreidimensionaler Vektoren; Ergebnisform je Dimension noch AUR-prüfpflichtig. | `2:122` | MTH VECTR |
| `CSWP` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Vertauscht ausgewählte Spalten einer Matrix bzw. Elemente eines Vektors. | `171:76` | MTH MATRX COL |
| `CYLIN` | Binärzahlen, Logik, Modi, Systemflags | Zylindrischer Koordinatenmodus. | `171:20` | MTH VECTR; MENU 63 ANGLE |
| `D→R` | Grundrechnen, elementare Funktionen und Zahlen | Gradmaß nach Bogenmaß umrechnen. | `2:112` | MTH REAL |
| `DARCY` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Darcy-Reibungsbeiwert berechnen. | `171:120` | MENU 113 UTILS |
| `DATE` | Zeit, Kalender, Wecker | Liefert das Systemdatum; dessen Darstellung hängt vom Datumsformat/Systemflag −42 ab. | `2:17` | MENU 94 |
| `DATE+` | Zeit, Kalender, Wecker | Tage zu Datum addieren. | `2:31` | MENU 94 |
| `dB` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Dezibel-Hilfsfunktion. | `171:128` | MENU 113 UTILS |
| `DDAYS` | Zeit, Kalender, Wecker | Tage zwischen Daten ermitteln. | `2:30` | MENU 94 |
| `DEC` | Binärzahlen, Logik, Modi, Systemflags | Dezimale Anzeigeform. | `2:145` | MTH BASE |
| `DECR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Verringert den Inhalt einer benannten Variablen um eins. | `2:332` | MENU 70 ARITH |
| `DEFINE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Benutzerdefinierte Funktion definieren. | `2:342` | ohne Menüeintrag |
| `DEG` | Binärzahlen, Logik, Modi, Systemflags | Winkelmodus Grad. | `2:135` | MENU 63 ANGLE |
| `DELALARM` | Zeit, Kalender, Wecker | Wecker löschen. | `2:28` | MENU 94 ALRM |
| `DELAY` | Schnittstellen, Drucker, Display und Tastenbelegung | Legt die Zeitverzögerung in Sekunden nach jeder an den Drucker übertragenen Zeile fest. | `2:245` | ohne Menüeintrag |
| `DELKEYS` | Schnittstellen, Drucker, Display und Tastenbelegung | Entfernt einzelne oder mehrere benutzerdefinierte Tastenbelegungen; genaue Argumentstruktur AUR-prüfpflichtig. | `2:381` | MENU 63 KEYS |
| `DEPND` | Grafik, Diagramme und Plotparameter | Abhängige Plotvariable festlegen. | `2:196` | ohne Menüeintrag |
| `DEPTH` | Stack und User-RPL-Programmsteuerung | Stacktiefe lesen. | `2:276` | MENU 73 |
| `DET` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Determinante. | `2:120` | MTH MATRX NORM |
| `DETACH` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Bibliothek abhängen. | `2:358` | MENU 110 |
| `DIAG→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Erzeugt eine Diagonalmatrix aus gegebenen Diagonalelementen. | `171:70` | MTH MATRX |
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
| `ENDSUB` | Listen, Strings, Objektkonversion | Liefert im DOSUBS-Kontext die Gesamtzahl der Teilfolgen/Durchläufe (nicht die verbleibende Anzahl). | `171:102` | PRG LIST PROC |
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
| `FACT` | Grundrechnen, elementare Funktionen und Zahlen | Fakultät einer Zahl (für geeignete Nichtganzzahlen über Gamma), synonym zu !. | `2:100` | ohne Menüeintrag |
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
| `FREEZE` | Schnittstellen, Drucker, Display und Tastenbelegung | LCD-Statusbereich (1), Stack/Eingabe (2), Softkeys (4) per Bitmaske einfrieren. | `2:51` | PRG OUT |
| `FS?` | Binärzahlen, Logik, Modi, Systemflags | Testen ob Flag gesetzt ist. | `2:133` | PRG TEST; MENU 63 FLAG |
| `FS?C` | Binärzahlen, Logik, Modi, Systemflags | Flag testen und löschen. | `2:142` | PRG TEST; MENU 63 FLAG |
| `FUNCTION` | Grafik, Diagramme und Plotparameter | Funktionsplot aktivieren. | `2:220` | ohne Menüeintrag |
| `GET` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element an einer Position lesen. | `2:178` | MTH MATRX MAKE; PRG LIST ELEM |
| `GETI` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element lesen; auch Container und weitergeschalteten Index zurückgeben. | `2:179` | MTH MATRX MAKE; PRG LIST ELEM |
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
| `LIBS` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Dem aktuellen Verzeichnis angehängte Bibliotheken auflisten. | `2:356` | MENU 110 |
| `LINE` | Grafik, Diagramme und Plotparameter | Linie zeichnen. | `2:206` | PRG PICT |
| `LINFIT` | Statistik, Verteilungen und Regression | Lineares Fit-Modell wählen. | `2:319` | ohne Menüeintrag |
| `LININ` | Symbolische Mathematik, Solver und Differentialgleichungen | Prüft, ob ein algebraischer Ausdruck hinsichtlich einer angegebenen Variablen linear ist. | `171:28` | PRG TEST |
| `LIST→` | Listen, Strings, Objektkonversion | Liste in Stackobjekte zerlegen. | `2:158` | ohne Menüeintrag |
| `LN` | Grundrechnen, elementare Funktionen und Zahlen | Natürlicher Logarithmus. | `2:94` | ohne Menüeintrag |
| `LNP1` | Grundrechnen, elementare Funktionen und Zahlen | Berechnet ln(1+x) mit besonderer Genauigkeit. | `2:97` | MTH HYP |
| `LOG` | Grundrechnen, elementare Funktionen und Zahlen | Zehnerlogarithmus. | `2:95` | ohne Menüeintrag |
| `LOGFIT` | Statistik, Verteilungen und Regression | Logarithmisches Fit-Modell wählen. | `2:320` | ohne Menüeintrag |
| `LQ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | LQ-Faktorisierung. | `171:61` | MTH MATRX FACTR |
| `LR` | Statistik, Verteilungen und Regression | Regressionskoeffizienten des aktuell gewählten Fit-Modells berechnen. | `2:302` | MENU 96 FIT |
| `LSQ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Ausgleichsrechnung nach kleinsten Quadraten. | `171:54` | MTH MATRX; MENU 74 SYS |
| `LU` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | LU-Zerlegung. | `171:59` | MTH MATRX FACTR |
| `MANT` | Grundrechnen, elementare Funktionen und Zahlen | Mantisse einer Zahl. | `2:111` | MTH REAL |
| `MAX` | Grundrechnen, elementare Funktionen und Zahlen | Maximum zweier Zahlen. | `2:106` | MTH REAL |
| `MAXR` | Grundrechnen, elementare Funktionen und Zahlen | Konstante: größter darstellbarer reeller Wert. | `2:64` | MTH CONST |
| `MAXΣ` | Statistik, Verteilungen und Regression | Spaltenmaxima der in ΣDAT gespeicherten Statistikdaten ermitteln. | `2:296` | MENU 96 1VAR |
| `MCALC` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Solver-Variable zur Berechnung markieren. | `171:115` | MENU 113 MES |
| `MEAN` | Statistik, Verteilungen und Regression | Mittelwerte der Statistikspalten in ΣDAT ermitteln. | `2:297` | MENU 96 1VAR |
| `MEM` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Freien Benutzerspeicher abfragen. | `2:344` | MENU 70 |
| `MENU` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Menü auswählen. | `2:348` | MENU 63 MENU |
| `MERGE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Kartenspeicher in Benutzerspeicher einbinden. | `2:354` | ohne Menüeintrag |
| `MERGE1` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Geeigneten Port-1-Speicher einbinden. | `171:22` | MENU 110 |
| `MIN` | Grundrechnen, elementare Funktionen und Zahlen | Minimum zweier Zahlen. | `2:107` | MTH REAL |
| `MINEHUNT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Integriertes Minehunt-Spiel. | `171:117` | MENU 113 UTILS |
| `MINIT` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Mehrgleichungslöser initialisieren. | `171:112` | MENU 113 MES |
| `MINR` | Grundrechnen, elementare Funktionen und Zahlen | Konstante: kleinster positiver reeller Wert. | `2:65` | MTH CONST |
| `MINΣ` | Statistik, Verteilungen und Regression | Spaltenminima der in ΣDAT gespeicherten Statistikdaten ermitteln. | `2:298` | MENU 96 1VAR |
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
| `NSUB` | Listen, Strings, Objektkonversion | Liest den aktuellen Teilfolgenzähler im Kontext von DOSUBS. | `171:101` | PRG LIST PROC |
| `NUM` | Listen, Strings, Objektkonversion | Zeichencode des ersten Zeichens einer Zeichenkette ermitteln; nicht mit →NUM verwechseln. | `2:164` | PRG TYPE; MENU 62 |
| `NUMX` | Grafik, Diagramme und Plotparameter | Anzahl der x-Schritte je y-Schritt für perspektivische 3D-Plots einstellen. | `171:6` | ohne Menüeintrag |
| `NUMY` | Grafik, Diagramme und Plotparameter | Anzahl der y-Schritte im 3D-Betrachtungsvolumen einstellen. | `171:7` | ohne Menüeintrag |
| `NΣ` | Statistik, Verteilungen und Regression | Anzahl der Datenzeilen der Statistikdaten in ΣDAT ermitteln. | `2:288` | MENU 96 SUMS |
| `OBJ→` | Listen, Strings, Objektkonversion | Objekt zerlegen. | `2:169` | PRG TYPE; PRG LIST; MENU 62 |
| `OCT` | Binärzahlen, Logik, Modi, Systemflags | Oktale Anzeigeform. | `2:147` | MTH BASE |
| `OFF` | Schnittstellen, Drucker, Display und Tastenbelegung | Gerät ausschalten. | `2:41` | PRG RUN |
| `OLDPRT` | Schnittstellen, Drucker, Display und Tastenbelegung | Druckparameter PRTPAR für ältere Infrarotdrucker vorbereiten. | `2:239` | ohne Menüeintrag |
| `OPENIO` | Schnittstellen, Drucker, Display und Tastenbelegung | Serielle oder Infrarot-I/O-Verbindung öffnen. | `2:361` | MENU 104 SERIAL |
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
| `PDIM` | Grafik, Diagramme und Plotparameter | Leeres GROB vorgegebener Dimensionen erzeugen und in PICT ablegen. | `2:195` | PRG PICT |
| `PERM` | Grundrechnen, elementare Funktionen und Zahlen | Permutationen/Variationen berechnen. | `2:130` | MTH PROB |
| `PEVAL` | Symbolische Mathematik, Solver und Differentialgleichungen | Polynom aus Koeffizienten auswerten. | `171:84` | MENU 74 POLY |
| `PGDIR` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Löscht (purge) ein Verzeichnis; nicht mit UPDIR/Elternverzeichniswechsel verwechseln. | `2:351` | MENU 70 DIR |
| `PICK` | Stack und User-RPL-Programmsteuerung | Stackelement aus bestimmter Tiefe kopieren. | `2:279` | MENU 73 |
| `PICT` | Grafik, Diagramme und Plotparameter | Auf Grafikobjekt-Bildspeicher zugreifen. | `2:210` | PRG PICT |
| `PICTURE` | Grafik, Diagramme und Plotparameter | Interaktive Grafikansicht öffnen. | `2:200` | MENU 96 PLOT |
| `PINIT` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Initialisiert einen Speicherport für geeignete RAM-/Erweiterungskarten. | `171:129` | MENU 110 |
| `PIX?` | Grafik, Diagramme und Plotparameter | Pixel prüfen. | `2:205` | PRG PICT |
| `PIXOFF` | Grafik, Diagramme und Plotparameter | Pixel löschen. | `2:204` | PRG PICT |
| `PIXON` | Grafik, Diagramme und Plotparameter | Pixel setzen. | `2:203` | PRG PICT |
| `PKT` | Schnittstellen, Drucker, Display und Tastenbelegung | Ein-/Ausgabepaket verarbeiten. | `2:377` | MENU 104 SRVR |
| `PMAX` | Grafik, Diagramme und Plotparameter | Obere rechte Grenze des PICT-Koordinatenraums festlegen. | `2:185` | ohne Menüeintrag |
| `PMIN` | Grafik, Diagramme und Plotparameter | Untere linke Grenze des PICT-Koordinatenraums festlegen. | `2:184` | ohne Menüeintrag |
| `POLAR` | Grafik, Diagramme und Plotparameter | Polarplot aktivieren. | `2:222` | ohne Menüeintrag |
| `POS` | Listen, Strings, Objektkonversion | Position eines Teilobjekts suchen. | `2:161` | PRG LIST ELEM; MENU 62 |
| `PR1` | Schnittstellen, Drucker, Display und Tastenbelegung | Objekt im mehrzeiligen Format drucken. | `2:240` | MENU 104; MENU 104 PRINT |
| `PREDV` | Statistik, Verteilungen und Regression | Vorhersage von y aus x wie PREDY (historisch funktionsgleicher Name mit eigener XLIB-Kennung). | `2:303` | ohne Menüeintrag |
| `PREDX` | Statistik, Verteilungen und Regression | x-Wert mittels Regression vorhersagen. | `2:305` | MENU 96 FIT |
| `PREDY` | Statistik, Verteilungen und Regression | y-Wert mittels Regression vorhersagen. | `2:304` | MENU 96 FIT |
| `PRLCD` | Schnittstellen, Drucker, Display und Tastenbelegung | LCD-Anzeige drucken. | `2:246` | MENU 104 PRINT |
| `PROMPT` | Stack und User-RPL-Programmsteuerung | Hinweistext im Statusbereich anzeigen und laufendes Programm anhalten, keine direkte Eingabe wie INPUT. | `1792:28` | PRG IN |
| `PROOT` | Symbolische Mathematik, Solver und Differentialgleichungen | Nullstellen eines Polynoms. | `171:82` | MENU 74 POLY |
| `PRST` | Schnittstellen, Drucker, Display und Tastenbelegung | Stack drucken. | `2:242` | MENU 104 PRINT |
| `PRSTC` | Schnittstellen, Drucker, Display und Tastenbelegung | Stack in kompaktem Format ausdrucken (Gegenstück zu PRST). | `2:241` | MENU 104 PRINT |
| `PRVAR` | Schnittstellen, Drucker, Display und Tastenbelegung | Variablen drucken. | `2:244` | MENU 104 PRINT |
| `PSDEV` | Statistik, Verteilungen und Regression | Standardabweichung der Grundgesamtheit. | `171:40` | MENU 96 1VAR |
| `PURGE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Benannte Variablen und leere Verzeichnisse löschen; für Verzeichnisinhalte PGDIR unterscheiden. | `2:343` | ohne Menüeintrag |
| `PUT` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element an einer Position ersetzen. | `2:176` | MTH MATRX MAKE; PRG LIST ELEM |
| `PUTI` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Element ersetzen, Container/Namensbezug und weitergeschaltete Position zurückgeben. | `2:177` | MTH MATRX MAKE; PRG LIST ELEM |
| `PVAR` | Statistik, Verteilungen und Regression | Populationsvarianz. | `171:41` | MENU 96 1VAR |
| `PVARS` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Listet Backupobjekte und Bibliotheken eines Speicherports; gibt zusätzlich dessen Speicherart oder freien Speicher zurück (User's Guide 28-4). | `2:350` | MENU 110 |
| `PVIEW` | Grafik, Diagramme und Plotparameter | PICT mit einer angegebenen Benutzerkoordinate in der linken oberen Ecke anzeigen. | `2:202` | PRG PICT; PRG OUT |
| `PWRFIT` | Statistik, Verteilungen und Regression | Potenz-Fit-Modell wählen. | `2:322` | ohne Menüeintrag |
| `PX→C` | Grafik, Diagramme und Plotparameter | Pixelkoordinaten in Benutzerkoordinaten wandeln. | `2:198` | PRG PICT |
| `QR` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | QR-Zerlegung mit Permutationsmatrix: A·P = Q·R (drei Ergebnisarrays). | `171:60` | MTH MATRX FACTR |
| `QUAD` | Symbolische Mathematik, Solver und Differentialgleichungen | Ausdruck nach einer Variablen über quadratische Taylorentwicklung zweiter Ordnung lösen. | `2:337` | MENU 93 |
| `QUOTE` | Symbolische Mathematik, Solver und Differentialgleichungen | Verhindert unmittelbare Auswertung. | `2:257` | MENU 93 |
| `R→B` | Binärzahlen, Logik, Modi, Systemflags | Reelle Zahl nach binärer Ganzzahl. | `2:9` | MTH BASE |
| `R→C` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Aus zwei reellen Komponenten komplexe Zahl bilden. | `2:153` | MTH CMPLX; PRG TYPE |
| `R→D` | Grundrechnen, elementare Funktionen und Zahlen | Bogenmaß nach Gradmaß umrechnen. | `2:113` | MTH REAL |
| `RAD` | Binärzahlen, Logik, Modi, Systemflags | Winkelmodus Radiant. | `2:136` | MENU 63 ANGLE |
| `RAND` | Grundrechnen, elementare Funktionen und Zahlen | Pseudozufallszahl erzeugen. | `2:127` | MTH PROB |
| `RANK` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Matrixrang ermitteln. | `171:53` | MTH MATRX NORM |
| `RANM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zufallsmatrix erzeugen. | `171:64` | MTH MATRX MAKE |
| `RATIO` | Symbolische Mathematik, Solver und Differentialgleichungen | Algebraische Darstellung des Divisionsoperators in symbolischen Ausdrücken. | `2:268` | ohne Menüeintrag |
| `RCEQ` | Symbolische Mathematik, Solver und Differentialgleichungen | Gespeicherte Gleichung EQ abrufen. | `2:249` | MENU 74 ROOT; MENU 84 |
| `RCI` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeile mit Faktor multiplizieren. | `171:77` | MTH MATRX ROW |
| `RCIJ` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Vielfaches einer Zeile zu anderer Zeile addieren. | `171:78` | MTH MATRX ROW |
| `RCL` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Variable in Stack zurückrufen. | `2:340` | ohne Menüeintrag |
| `RCLALARM` | Zeit, Kalender, Wecker | Alarm einschließlich Aktion und Zeit-/Intervallangaben abrufen. | `2:26` | MENU 94 ALRM |
| `RCLF` | Binärzahlen, Logik, Modi, Systemflags | Flagsatz lesen. | `2:150` | MENU 63 FLAG |
| `RCLKEYS` | Schnittstellen, Drucker, Display und Tastenbelegung | Benutzer-Tastenbelegung lesen. | `2:382` | MENU 63 KEYS |
| `RCLMENU` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Aktuelles Menü lesen. | `2:349` | MENU 63 MENU |
| `RCLΣ` | Statistik, Verteilungen und Regression | Statistikdatensatz zurückrufen. | `2:285` | MENU 87 DATA; MENU 96 DATA |
| `RCWS` | Binärzahlen, Logik, Modi, Systemflags | Wortbreite binärer Ganzzahlen abfragen. | `2:149` | MTH BASE |
| `RDM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Array redimensionieren; benannte Arrays ggf. direkt verändern statt zurückzugeben. | `2:172` | MTH MATRX MAKE |
| `RDZ` | Grundrechnen, elementare Funktionen und Zahlen | Zufallsgenerator initialisieren. | `2:128` | MTH PROB |
| `RE` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Realteil. | `2:154` | MTH CMPLX |
| `RECN` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Datei empfangen und benennen. | `2:365` | MENU 104 |
| `RECT` | Binärzahlen, Logik, Modi, Systemflags | Kartesischer Koordinatenmodus. | `171:19` | MTH VECTR; MENU 63 ANGLE |
| `RECV` | Schnittstellen, Drucker, Display und Tastenbelegung | Bereits benannte Daten/Datei über Kermit empfangen; von RECN unterscheiden. | `2:366` | MENU 104 |
| `REPEAT` | Stack und User-RPL-Programmsteuerung | Wiederholung in WHILE-Schleife. | `1792:6` | PRG BRCH WHILE |
| `REPL` | Listen, Strings, Objektkonversion | Teilbereich eines Strings, Arrays, einer Liste oder eines Grafikobjekts ersetzen. | `2:157` | MTH MATRX MAKE; PRG LIST; PRG GROB; MENU 62 |
| `RES` | Grafik, Diagramme und Plotparameter | Plotauflösung einstellen. | `2:188` | ohne Menüeintrag |
| `RESTORE` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Backup wiederherstellen. | `2:353` | MENU 70 |
| `REVLIST` | Listen, Strings, Objektkonversion | Liste umkehren. | `171:109` | MTH LIST; PRG LIST PROC |
| `RKF` | Symbolische Mathematik, Solver und Differentialgleichungen | Runge-Kutta-Fehlberg-Verfahren für Anfangswertprobleme. | `171:43` | MENU 74 DIFFEQ |
| `RKFERR` | Symbolische Mathematik, Solver und Differentialgleichungen | Fehlerabschätzung des RKF-Verfahrens. | `171:45` | MENU 74 DIFFEQ |
| `RKFSTEP` | Symbolische Mathematik, Solver und Differentialgleichungen | Runge-Kutta-Fehlberg-Einzelschritt. | `171:44` | MENU 74 DIFFEQ |
| `RL` | Binärzahlen, Logik, Modi, Systemflags | Bits nach links rotieren. | `2:1` | MTH BASE BIT |
| `RLB` | Binärzahlen, Logik, Modi, Systemflags | Bits um ein Byte nach links rotieren. | `2:2` | MTH BASE BYTE |
| `RND` | Grundrechnen, elementare Funktionen und Zahlen | Auf Dezimalstellen, signifikante Stellen oder aktuelles Anzeigeformat runden (je Parameter). | `2:108` | MTH REAL |
| `RNRM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeilennorm einer Matrix. | `2:118` | MTH MATRX NORM |
| `ROLL` | Stack und User-RPL-Programmsteuerung | Oberste n Stackobjekte um eine Position nach oben rotieren; n wird verbraucht. | `2:280` | MENU 73 |
| `ROLLD` | Stack und User-RPL-Programmsteuerung | Oberste n Stackobjekte um eine Position nach unten rotieren; n wird verbraucht. | `2:281` | MENU 73 |
| `ROOT` | Symbolische Mathematik, Solver und Differentialgleichungen | Numerische Nullstelle bestimmen. | `2:251` | MENU 74 ROOT |
| `ROT` | Stack und User-RPL-Programmsteuerung | Drei Stackelemente rotieren. | `2:274` | MENU 73 |
| `ROW-` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Gewählte Arrayzeile entfernen und reduzierte Matrix sowie entfernte Zeile zurückgeben. | `171:71` | MTH MATRX ROW |
| `ROW→` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Bildet ein Array aus vorliegenden Zeilenobjekten. | `171:66` | MTH MATRX ROW |
| `ROW+` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeile einfügen. | `171:72` | MTH MATRX ROW |
| `rpm` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Einheit Umdrehungen je Minute. | `171:127` | MENU 113 UTILS |
| `RR` | Binärzahlen, Logik, Modi, Systemflags | Bits nach rechts rotieren. | `2:3` | MTH BASE BIT |
| `RRB` | Binärzahlen, Logik, Modi, Systemflags | Bits um ein Byte nach rechts rotieren. | `2:4` | MTH BASE BYTE |
| `RREF` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Reduzierte Zeilenstufenform. | `171:63` | MTH MATRX FACTR |
| `RRK` | Symbolische Mathematik, Solver und Differentialgleichungen | Numerisches Verfahren für steife Differentialgleichungen. | `171:46` | MENU 74 DIFFEQ |
| `RRKSTEP` | Symbolische Mathematik, Solver und Differentialgleichungen | Nächsten DGL-Lösungsschritt mit RKF-/RRK-Verfahrenswahl und Toleranz ermitteln. | `171:47` | MENU 74 DIFFEQ |
| `RSBERR` | Symbolische Mathematik, Solver und Differentialgleichungen | Rosenbrock-Schrittkorrektur und absolute Fehlerabschätzung berechnen. | `171:48` | MENU 74 DIFFEQ |
| `RSD` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet laut HP Operation Index G-40 den Rest z−y·x aus drei Arrays; bei z=B, y=A, x=X entspricht das B−A·X. AUR-Stackreihenfolge noch nachzuprüfen. | `2:123` | MTH MATRX; MENU 74 SYS |
| `RSWP` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Zeilen vertauschen. | `171:75` | MTH MATRX ROW |
| `RULES` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Undokumentierter ROM-Eintrag mit historischem Entwickler-Namensrätsel; EQW-RULES ist ein separates Menü. | `2:335` | ohne Menüeintrag |
| `SAME` | Binärzahlen, Logik, Modi, Systemflags | Vollständige Objektgleichheit prüfen. | `2:228` | PRG TEST |
| `SBRK` | Schnittstellen, Drucker, Display und Tastenbelegung | Serielles Break-Signal senden. | `2:376` | MENU 104 SERIAL |
| `SCALE` | Grafik, Diagramme und Plotparameter | Horizontalen und vertikalen Plotmaßstab in den ersten PPAR-Parametern festlegen. | `2:194` | ohne Menüeintrag |
| `SCATRPLOT` | Grafik, Diagramme und Plotparameter | Streudiagramm erstellen. | `2:318` | MENU 96 PLOT |
| `SCATTER` | Grafik, Diagramme und Plotparameter | Streudiagramm aktivieren. | `2:225` | ohne Menüeintrag |
| `SCHUR` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Schur-Zerlegung einer quadratischen Matrix in Transformations- und Dreiecks-/Quasidreiecksform. | `171:62` | MTH MATRX FACTR |
| `SCI` | Binärzahlen, Logik, Modi, Systemflags | Wissenschaftliches Format. | `2:139` | MENU 63 FMT |
| `SCLΣ` | Statistik, Verteilungen und Regression | Passt den Plotbereich in PPAR an die Statistikdaten in ΣDAT an (nicht die Datenmatrix selbst verändern); AUR-Einzelprüfung offen. | `2:313` | ohne Menüeintrag |
| `SCONJ` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Konjugiert den Inhalt einer benannten Variablen und speichert das Ergebnis dort. | `2:326` | MENU 70 ARITH |
| `SDEV` | Statistik, Verteilungen und Regression | Stichprobenstandardabweichung. | `2:299` | MENU 96 1VAR |
| `SEND` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Objekt senden. | `2:363` | MENU 104 |
| `SEQ` | Listen, Strings, Objektkonversion | Liste durch wiederholte Objektauswertung über benannte Indexvariable, Grenzen und Schrittweite erzeugen. | `171:98` | PRG LIST PROC |
| `SERVER` | Schnittstellen, Drucker, Display und Tastenbelegung | Kermit-Servermodus starten. | `2:368` | MENU 104 SRVR |
| `SF` | Binärzahlen, Logik, Modi, Systemflags | Flag setzen. | `2:131` | PRG TEST; MENU 63 FLAG |
| `SHOW` | Symbolische Mathematik, Solver und Differentialgleichungen | Implizite Vorkommen einer Variablen in einem symbolischen Ausdruck explizit darstellen. | `2:338` | MENU 93 |
| `SIDENS` | Einheiten, Equation Library, Anwendungen und Sonderbefehle | Temperaturabhängige Dichte von Silizium berechnen. | `171:122` | MENU 113 UTILS |
| `SIGN` | Grundrechnen, elementare Funktionen und Zahlen | Vorzeichenfunktion. | `2:78` | MTH REAL; MTH CMPLX |
| `SIN` | Grundrechnen, elementare Funktionen und Zahlen | Sinus. | `2:81` | ohne Menüeintrag |
| `SINH` | Grundrechnen, elementare Funktionen und Zahlen | Sinus hyperbolicus. | `2:84` | MTH HYP |
| `SINV` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Ersetzt den Inhalt einer benannten Variablen durch dessen Inverses. | `2:324` | MENU 70 ARITH |
| `SIZE` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Objekttypabhängig Größe, Dimensionen oder Elementanzahl ermitteln. | `2:160` | MTH MATRX MAKE; PRG LIST ELEM; PRG GROB; MENU 62 |
| `SL` | Binärzahlen, Logik, Modi, Systemflags | Bitverschiebung nach links. | `2:5` | MTH BASE BIT |
| `SLB` | Binärzahlen, Logik, Modi, Systemflags | Byteverschiebung nach links. | `2:6` | MTH BASE BYTE |
| `SLOPEFIELD` | Grafik, Diagramme und Plotparameter | Richtungsfeld aktivieren. | `171:12` | ohne Menüeintrag |
| `SNEG` | Variable, Verzeichnisse, RAM und ROM-Bibliotheken | Negiert den Inhalt einer benannten Variablen und speichert das Ergebnis dort. | `2:325` | MENU 70 ARITH |
| `SNRM` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet die Spektralnorm eines Arrays. | `171:52` | MTH MATRX NORM |
| `SOLVEQN` | Symbolische Mathematik, Solver und Differentialgleichungen | Equation-Library-Gleichung über Themen-/Gleichungsnummer starten, optional Abbildung in PICT. | `171:35` | MENU 113 EQLIB |
| `SORT` | Listen, Strings, Objektkonversion | Liste sortieren. | `171:110` | MTH LIST; PRG LIST PROC |
| `SPHERE` | Binärzahlen, Logik, Modi, Systemflags | Sphärischer Koordinatenmodus. | `171:21` | MTH VECTR; MENU 63 ANGLE |
| `SQ` | Grundrechnen, elementare Funktionen und Zahlen | Quadrat. | `2:80` | ohne Menüeintrag |
| `SR` | Binärzahlen, Logik, Modi, Systemflags | Bitverschiebung nach rechts. | `2:7` | MTH BASE BIT |
| `SRAD` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet den Spektralradius einer quadratischen Matrix. | `171:51` | MTH MATRX NORM |
| `SRB` | Binärzahlen, Logik, Modi, Systemflags | Byteverschiebung nach rechts. | `2:8` | MTH BASE BYTE |
| `SRECV` | Schnittstellen, Drucker, Display und Tastenbelegung | Zeichenfolge bis zur angeforderten Länge aus seriellem Empfangspuffer lesen, mit Statusinformation. | `2:360` | MENU 104 SERIAL |
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
| `TRACE` | Komplexe Zahlen, Vektoren, Matrizen und Transformationen | Berechnet die Matrixspur als Summe der Diagonalelemente; nicht Grafik-TRACE. | `171:50` | MTH MATRX NORM |
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
| `ΣLINE` | Statistik, Verteilungen und Regression | Ausgleichsfunktion der Statistikdaten für das aktuell gewählte Fit-Modell ermitteln. | `2:314` | MENU 96 FIT |
| `ΣLIST` | Listen, Strings, Objektkonversion | Liste aufsummieren. | `171:104` | MTH LIST |
| `ΣX` | Statistik, Verteilungen und Regression | Summe der x-Werte. | `2:291` | MENU 96 SUMS |
| `ΣX*Y` | Statistik, Verteilungen und Regression | Summe der Produkte x mal y. | `2:295` | MENU 96 SUMS |
| `ΣX^2` | Statistik, Verteilungen und Regression | Summe der x-Quadrate. | `2:293` | MENU 96 SUMS |
| `ΣY` | Statistik, Verteilungen und Regression | Summe der y-Werte. | `2:292` | MENU 96 SUMS |
| `ΣY^2` | Statistik, Verteilungen und Regression | Summe der y-Quadrate. | `2:294` | MENU 96 SUMS |


**Korrektur anhand der Originalquelle (21.11.2026):** `PVARS` ist **keine** Auflistung der Variablen des Elternverzeichnisses. Nach dem *User's Guide*, 28-4, liest `PVARS` die Backup-/Bibliotheksobjekte **eines Speicherports** und meldet dessen Speicherstatus. `SCLΣ` verändert dagegen die **Plotparameter** für statistische Daten, nicht die Datensätze. In beiden Fällen ist das vereinfachte frühere Beschreibungsmuster potenziell irreführend. Exakte Stack-Typen und Fehlervarianten sind noch gesondert zu prüfen.

## 3a. Zusätzliche dokumentierte Operationen und Namen **außerhalb der 517 direkten ROM-Indexnamen**

**Quelle:** *HP 48G Series User's Guide*, Anhang G, *Operation Index*, und die *Advanced User's Reference*. Die vollständige quellengestützte Prüfung mit weiteren **143 ausgewählten kontextabhängigen Bedienaktionen** steht in der [Befehlsabgleich-Matrix](HP-48GX-BEFEHLSABGLEICH-MATRIX.md), Abschnitte C.1–C.3. Die nachfolgenden Namen **sind kein zusätzlicher, belegter XLIB-Zahlenraum**; manche sind Aliase, nur dialoggebunden oder reservierte Systemvariablen.

| Name | Typ / Status | Bedeutung | Originalfundstelle |
| --- | --- | --- | --- |
| `CLUSR` | Im offiziellen Operation Index ausdrücklich als programmierbares `C` dokumentiert; ROM-Zuordnung offen | Historischer Kompatibilitätsname für `CLVAR` (Pocket Guide S. 43 nennt dieselbe Funktion); genaue AUR-Stackdetails und ROM-Revisionsunterschiede noch zu prüfen. | User's Guide G-7 |
| `ECHO` | Nichtprogrammierbare Stack-Browser-Aktion `O` | Kopiert markiertes Stackobjekt in die Eingabezeile | User's Guide G-14 |
| `DINV` | Nichtprogrammierbare EquationWriter-Regel `O` | Doppelte Invertierung als Umformungsregel | User's Guide 20-20 / Operation Index G-12 |
| `EXTR` | Nichtprogrammierbare Grafik-Analyseaktion `O` | Extremum in der Grafik suchen | User's Guide, G-16 / Kapitel 22 |
| `GRAPH` | Historischer programmierbarer Befehlszugang, separat nachzuprüfen | Aktiviert die Grafik-Umgebung; dokumentierter älterer Zugang neben `PICTURE` | User's Guide G-18/19, AUR Command Reference / Index |
| `IR` | Dokumentierte I/O-Bedienoperation ohne separate ROM-Namenskennung | Übertragungsweg zwischen Infrarot und serieller Schnittstelle umschalten | AUR Index, Pocket Guide Command Index S. 54, A04 |
| `LAST` | Historischer Kompatibilitätsalias ohne eigene ROM-Namenskennung | Entspricht `LASTARG`: Argumente des zuletzt ausgeführten Befehls wiederherstellen; nicht LASTSTACK | User's Guide G-23, AUR Index |
| `SIMU` | Interaktive PLOT-FLAG-Aktion ohne eigene ROM-XLIB-Namenskennung | Gleichzeitiges Zeichnen mehrerer Kurven ein-/ausschalten; genaue Flagsemantik offen | AUR-Index 378, Pocket Guide S. 68, A08 |
| `SCLS` | HP-User's-Guide-Textform; AUR/ROM `SCLΣ`, Pocket-OCR `SCLZ` – Originalglyphen offen | PPAR-Plotgrenzen an ΣDAT-Streudiagramm anpassen; tatsächliche Eingabeschreibweise noch nicht visuell freigegeben | User's Guide G-41 |
| `CST` | Reservierter Variablenname | Benutzerdefiniertes Menüobjekt | G-9 |
| `ΣDAT` | Reservierter Variablenname | Statistikdatenmatrix | G-10 |
| `IOPAR` | Reservierter Variablenname | Parameter der Ein-/Ausgabe | G-22 |
| `PPAR` | Reservierter Variablenname | 2D-Plotparameter | G-31 |
| `VPAR` | Reservierter Variablenname | 3D-Plotparameter | G-51 |
| `PRTPAR` | Reservierter Variablenname | Druckparameter | G-32 |
| `FV`, `PMT`, `PV`, `PYR` | Reservierte Namen der eingebauten TVM-Anwendung | Zukunftswert, Zahlung, Gegenwartswert und Zahlungen/Jahr | G-17, G-32–33 |
| `SOLVE` | Interaktive Aktion | Lösen des im Formular ausgewählten Problems | G-42 |
| `DBUG`, `SST`, `SST↓`, Debugger-`NEXT` | Nichtprogrammierbare Programmierhilfen | Starten, Fortsetzen und Einzelschritt der Programmuntersuchung | G-11, G-28, G-43 |
| `EDIT` | Kontextabhängige Editieraktion | Objekt oder Teilausdruck bearbeiten | G-14 und AUR-Verweise |
| `←A`, `A→`, `AF`, `←D`, `D→`, `←T`, `T→`, `TRG*`, `→TRG`, `1/()` | Nichtprogrammierbare EquationWriter-Regeln | Algebraische Umformungen mit ausgewähltem Teilausdruck | G-2, G-10, G-47, G-49, G-57 |
| `BOXZ`, `ZIN`, `ZOUT`, `ZLAST`, `SLOPE`, `ISECT`, `SHADE`, Plot-`TRACE` | Interaktive PICTURE-/Plotaktionen | Zoom, grafische Analyse und Kurvenverfolgung | G-5, G-22, G-41, G-49, G-54 |

**Prüfstatus:** `LAST` ist auf Namens- und Kurzfunktionsebene als Alias zu `LASTARG` unabhängig belegt; Detailfehlerfälle bleiben offen. Diese Handbucheinträge **erweitern die Referenz**, ohne die 517 technischen ROM-Namen stillschweigend umzubenennen. Ob `GRAPH`, `LAST`, `SCLS` oder die Variablenzugriffe tatsächlich als unabhängige User-RPL-Programmelemente gelten, ist mit Einzelreferenz, realem Gerät oder unabhängigem Emulator zu verifizieren. Die G-Seiten sind handbuchbezogene Fundstellen, nicht behauptete komplette AUR-Stackdiagramme.

## 4. Was nicht fälschlich mitgezählt werden darf

1. **Nichtprogrammierbare Tasten und Dialogfolgen:** `DBUG`, `SST`, `SST↓`, Editor- und Navigationsaktionen, Hotkeys, Untermenüs, Reset-/Selbsttestsequenzen; sie müssen als UI-Bedieninventar, nicht als ROM-Befehlsnameneinträge geprüft werden.
2. **ROM-eigene Datentabellen:** Die rund 147 Einheiten, 300+ Formeln, Konstanten und eingebauten Beispiele sind kein Synonym für 147 oder 300 neue RPL-Befehlsnamen. Eine hundertprozentige historische Emulation verlangt zusätzliche, getrennte Kataloge der **Einheitenbezeichnungen, Einzelformeln, Konstantenwerte und Sonderbilder**. Die **16 Einheiten-Menügruppen und 102 Gleichungs-Problemüberschriften** wurden jetzt zusätzlich inventarisiert, aber die mehr als 300 Einzelformeln, die vollständigen Einheitenwerte und die historischen Konstanten-/Bilddaten **nicht einzeln rekonstruiert**; eine Behauptung absoluter Vollständigkeit über alle internen ROM-Daten wäre daher falsch.
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
