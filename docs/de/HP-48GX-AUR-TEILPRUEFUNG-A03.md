# HP 48GX – AUR-Teilprüfung A03 (Einträge 101–150)

**Prüfstand:** 22.11.2026 · **Modell:** serienmäßiger HP 48GX (ohne Fremdkarten).  
**Gegenstand:** 50 Namenseinträge des AUR-Kapitel-3-Inhaltsverzeichnisses von `DIFFEQ` bis `FREE1`.  
**Status:** Quelltext-/Namenabgleich gegen normierte ROM-Namen und unabhängigen Pocket Guide. **Keine visuelle Abnahme der AUR-/Pocket-Originalscans, keine vollständige Einzelbefehls-/Stack-/Fehlerfallprüfung, keine reale Geräteausführung.**

## Quellen und Beleggrenzen

1. Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Auflage (Dezember 1994), Kapitel 3; im Repository getrennt fixierter AUR-Inhaltsverzeichnis-Datensatz [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json). Original: https://literature.hpcalc.org/community/hp48g-aur-en.pdf (große Scan-Datei; die in der JSON vorhandenen PDF-Seiten sind **Hinweise**, keine eigene Sichtfreigabe).
2. Unabhängiges Kommandonameninventar aus dem Stock-48GX-ROM: [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json) mit XLIB-Kennungen. Eine gleiche Zeichenfolge ist ein Namensbeleg und **kein** Beweis der typgenauen Ausführung.
3. James Donnelly, *The HP 48G/GX Pocket Guide*, **Command Index gedruckte S. 48, 50 und 52**. PDF-Textindex: https://literature.hpcalc.org/community/hp48g-pg-en.pdf . Kontrollierte Web-Texterfassung (Bildseitenzählung 50, 52, 54): https://www.manualslib.com/manual/3743173/Hp-48g.html?page=50 , https://www.manualslib.com/manual/3743173/Hp-48g.html?page=52 , https://www.manualslib.com/manual/3743173/Hp-48g.html?page=54 .
4. Zusatzquelle für `ENDSUB`: der durchsuchbare Pocket-Guide-PDF-Text benennt ihn ausdrücklich als Zähler der DOSUBS-Teilfolgen. Die alternative ManualsLib-Web-OCR überspringt diese Zeile. Zusätzlich: https://literature.hpcalc.org/community/hp48g-pb.pdf (Donnelly, *HP 48 Pocket Book*, selbständige Kurzbeschreibung).

**Quellenkritik:** Die Pocket-Webfassung ist stark fehlerhaft: `DUP2`→`OUPZ`, `ERR0`→`ERRA`, `F0λ`→`Féx`, `FREE1`→`FREEL`. Die Spalte „Pocket-Textform“ ist ein *Rohkandidat*, keine bestätigte originale Druckglyphe. AUR-Quelltext hat bei `ERRO` einen mutmaßlichen Buchstaben-/Ziffernkonflikt zum ROM-Namen `ERR0` (siehe Differenzliste).

## 1. Alle 50 Positionen: AUR ↔ ROM ↔ Pocket-Guide-Text

| AUR # | AUR-Quelltextname | AUR-Inhaltsübersicht | Normierter ROM-Name / XLIB | Pocket-Druckseite | Pocket-Textform (OCR) | Belegstatus |
| ---: | --- | --- | --- | ---: | --- | --- |
| 101 | `DIFFEQ` | Contents-6 (PDF-Hinweis 250) | `DIFFEQ` / `171:14` | 48 | `DIFFED` | OCR-Glyphe unsicher |
| 102 | `DISP` | Contents-6 (PDF-Hinweis 252) | `DISP` / `2:50` | 48 | `DISP` | Textindex zugeordnet |
| 103 | `DO` | Contents-6 (PDF-Hinweis 253) | `DO` / `1792:7` | 48 | `00` | OCR-Glyphe unsicher |
| 104 | `DOERR` | Contents-6 (PDF-Hinweis 254) | `DOERR` / `2:42` | 48 | `DOERR` | Textindex zugeordnet |
| 105 | `DOLIST` | Contents-6 (PDF-Hinweis 255) | `DOLIST` / `171:107` | 48 | `DDLIST` | OCR-Glyphe unsicher |
| 106 | `DOSUBS` | Contents-6 (PDF-Hinweis 256) | `DOSUBS` / `171:99` | 48 | `00SUBS` | OCR-Glyphe unsicher |
| 107 | `DOT` | Contents-6 (PDF-Hinweis 258) | `DOT` / `2:121` | 48 | `00T` | OCR-Glyphe unsicher |
| 108 | `DRAW` | Contents-6 (PDF-Hinweis 258) | `DRAW` / `2:191` | 48 | `ORAW` | OCR-Glyphe unsicher |
| 109 | `DRAX` | Contents-6 (PDF-Hinweis 259) | `DRAX` / `2:193` | 48 | `ORAY` | OCR-Glyphe unsicher |
| 110 | `DROP` | Contents-6 (PDF-Hinweis 259) | `DROP` / `2:272` | 48 | `OROP` | OCR-Glyphe unsicher |
| 111 | `DROPN` | Contents-6 (PDF-Hinweis 260) | `DROPN` / `2:277` | 48 | `DROPN` | Textindex zugeordnet |
| 112 | `DROP2` | Contents-6 (PDF-Hinweis 260) | `DROP2` / `2:273` | 48 | `OROPE` | OCR-Glyphe unsicher |
| 113 | `DTAG` | Contents-6 (PDF-Hinweis 261) | `DTAG` / `2:384` | 48 | `OTAG` | OCR-Glyphe unsicher |
| 114 | `DUP` | Contents-6 (PDF-Hinweis 261) | `DUP` / `2:269` | 48 | `OUP` | OCR-Glyphe unsicher |
| 115 | `DUPN` | Contents-6 (PDF-Hinweis 262) | `DUPN` / `2:278` | 50 | `DUPN` | Textindex zugeordnet |
| 116 | `DUP2` | Contents-6 (PDF-Hinweis 262) | `DUP2` / `2:270` | 50 | `OUPZ` | OCR-Glyphe unsicher |
| 117 | `D→R` | Contents-6 (PDF-Hinweis 263) | `D→R` / `2:112` | 50 | `0+R` | OCR-Glyphe unsicher |
| 118 | `e` | Contents-6 (PDF-Hinweis 263) | `e` / `2:66` | 50 | `£` | OCR-Glyphe unsicher |
| 119 | `EGV` | Contents-6 (PDF-Hinweis 264) | `EGV` / `171:55` | 50 | `EGY` | OCR-Glyphe unsicher |
| 120 | `EGVL` | Contents-6 (PDF-Hinweis 265) | `EGVL` / `171:56` | 50 | `EGML` | OCR-Glyphe unsicher |
| 121 | `ELSE` | Contents-6 (PDF-Hinweis 265) | `ELSE` / `1792:2` | 50 | `ELSE` | Textindex zugeordnet |
| 122 | `END` | Contents-6 (PDF-Hinweis 266) | `END` / `1792:3, 1792:22, 1792:23` | 50 | `EMD` | OCR-Glyphe unsicher |
| 123 | `ENDSUB` | Contents-6 (PDF-Hinweis 266) | `ENDSUB` / `171:102` | 50 | `ENDSUB` | PDF-Suchtext (Web-OCR-Lücke) |
| 124 | `ENG` | Contents-6 (PDF-Hinweis 267) | `ENG` / `2:140` | 50 | `ENG` | Textindex zugeordnet |
| 125 | `EQ→` | Contents-6 (PDF-Hinweis 268) | `EQ→` / `2:168` | 50 | `EQ+` | OCR-Glyphe unsicher |
| 126 | `EQNLIB` | Contents-6 (PDF-Hinweis 268) | `EQNLIB` / `171:34` | 50 | `EONL IB` | OCR-Glyphe unsicher |
| 127 | `ERASE` | Contents-6 (PDF-Hinweis 269) | `ERASE` / `2:197` | 50 | `ERASE` | Textindex zugeordnet |
| 128 | `ERRM` | Contents-6 (PDF-Hinweis 269) | `ERRM` / `2:45` | 50 | `EREM` | OCR-Glyphe unsicher |
| 129 | `ERRN` | Contents-6 (PDF-Hinweis 270) | `ERRN` / `2:44` | 50 | `EREN` | OCR-Glyphe unsicher |
| 130 | `ERRO` | Contents-7 | `ERR0` / `2:43` | 50 | `ERRA` | Normierung: 0/O; Originalscan offen |
| 131 | `EVAL` | Contents-7 (PDF-Hinweis 271) | `EVAL` / `2:46` | 50 | `EVAL` | Textindex zugeordnet |
| 132 | `EXP` | Contents-7 (PDF-Hinweis 272) | `EXP` / `2:93` | 50 | `EXP` | Textindex zugeordnet |
| 133 | `EXPAN` | Contents-7 (PDF-Hinweis 273) | `EXPAN` / `2:334` | 50 | `EXPAN` | Textindex zugeordnet |
| 134 | `EXPFIT` | Contents-7 (PDF-Hinweis 274) | `EXPFIT` / `2:321` | 50 | `EXPFIT` | Textindex zugeordnet |
| 135 | `EXPM` | Contents-7 (PDF-Hinweis 274) | `EXPM` / `2:98` | 50 | `ExPM` | OCR-Glyphe unsicher |
| 136 | `EYEPT` | Contents-7 (PDF-Hinweis 275) | `EYEPT` / `171:5` | 50 | `EYEPT` | Textindex zugeordnet |
| 137 | `F0λ` | Contents-7 | `F0λ` / `171:121` | 50 | `Féx` | OCR-Glyphe unsicher |
| 138 | `FACT` | Contents-7 (PDF-Hinweis 276) | `FACT` / `2:100` | 50 | `FACT` | Textindex zugeordnet |
| 139 | `FANNING` | Contents-7 (PDF-Hinweis 277) | `FANNING` / `171:119` | 50 | `FAMNING` | OCR-Glyphe unsicher |
| 140 | `FC?` | Contents-7 (PDF-Hinweis 278) | `FC?` / `2:134` | 50 | `FLC?` | OCR-Glyphe unsicher |
| 141 | `FC?C` | Contents-7 (PDF-Hinweis 278) | `FC?C` / `2:143` | 50 | `FC?C` | Textindex zugeordnet |
| 142 | `FFT` | Contents-7 (PDF-Hinweis 279) | `FFT` / `171:37` | 50 | `FFT` | Textindex zugeordnet |
| 143 | `FINDALARM` | Contents-7 (PDF-Hinweis 280) | `FINDALARM` / `2:27` | 50 | `F INDALARM` | OCR-Glyphe unsicher |
| 144 | `FINISH` | Contents-7 (PDF-Hinweis 281) | `FINISH` / `2:367` | 50 | `FINISH` | Textindex zugeordnet |
| 145 | `FIX` | Contents-7 (PDF-Hinweis 281) | `FIX` / `2:138` | 50 | `FI%` | OCR-Glyphe unsicher |
| 146 | `FLOOR` | Contents-7 (PDF-Hinweis 282) | `FLOOR` / `2:103` | 50 | `FLOOR` | Textindex zugeordnet |
| 147 | `FOR` | Contents-7 (PDF-Hinweis 283) | `FOR` / `1792:10` | 52 | `FOR.` | OCR-Glyphe unsicher |
| 148 | `FP` | Contents-7 (PDF-Hinweis 285) | `FP` / `2:102` | 52 | `FP` | Textindex zugeordnet |
| 149 | `FREE` | Contents-7 (PDF-Hinweis 285) | `FREE` / `2:355` | 52 | `FREE` | Textindex zugeordnet |
| 150 | `FREE1` | Contents-7 (PDF-Hinweis 286) | `FREE1` / `171:23` | 52 | `FREEL` | OCR-Glyphe unsicher |

**Bilanz:** 50/50 nummerierte AUR-TOC-Einträge; **50/50** gegen *normierte* ROM-Namenseinträge mit XLIB-Kennung eindeutig zuordenbar. **50/50** Pocket-Guide-Namen in der Gesamtschau der unabhängigen HTML-OCR und des separat indizierten Original-PDF-Texts nachvollziehbar; für `ENDSUB` **nur der PDF-Suchtext**, nicht die unvollständige ManualsLib-Web-OCR. Ziffern und Sonderzeichen sind nicht visuell freigegeben. Diese Zählung misst Quellen-*Namensabgleich*, nicht 50 erfolgreich ausgeführte Kommandos.

## 2. Eigenständige deutsche Kurzbedeutungen (keine Stackdiagramme)

| AUR # | Normierter Name | Funktionskurzbeschreibung |
| ---: | --- | --- |
| 101 | `DIFFEQ` | Aktiviert den Plottyp für Differentialgleichungen. |
| 102 | `DISP` | Zeigt ein Objekt in einer angegebenen Displayzeile. |
| 103 | `DO` | Beginn einer DO-Schleife in User-RPL. |
| 104 | `DOERR` | Erzeugt einen Fehler mit Nummer oder benutzerdefiniertem Text. |
| 105 | `DOLIST` | Wendet ein Programm elementweise auf eine oder mehrere Listen an. |
| 106 | `DOSUBS` | Wendet ein Programm auf aufeinanderfolgende Teilfolgen einer Liste an. |
| 107 | `DOT` | Berechnet das Skalarprodukt zweier Vektoren/Arrays. |
| 108 | `DRAW` | Zeichnet den eingerichteten Plot in PICT. |
| 109 | `DRAX` | Zeichnet die Achsen im Grafikbild. |
| 110 | `DROP` | Entfernt oberstes Stackobjekt. |
| 111 | `DROPN` | Entfernt n Stackobjekte und das zugehörige n-Argument vom Stack. |
| 112 | `DROP2` | Entfernt die zwei obersten Stackobjekte. |
| 113 | `DTAG` | Entfernt den Benennungs-Tag eines getaggten Objekts. |
| 114 | `DUP` | Kopiert das oberste Stackobjekt. |
| 115 | `DUPN` | Kopiert n oberste Stackobjekte; das n-Argument wird verbraucht. |
| 116 | `DUP2` | Kopiert die zwei obersten Stackobjekte. |
| 117 | `D→R` | Wandelt Winkel von Grad in Radiant um. |
| 118 | `e` | Symbolische Eulersche Zahl. |
| 119 | `EGV` | Ermittelt Eigenwerte und rechte Eigenvektoren einer quadratischen Matrix. |
| 120 | `EGVL` | Ermittelt Eigenwerte einer quadratischen Matrix. |
| 121 | `ELSE` | Kennzeichnet den alternativen Zweig einer Verzweigung. |
| 122 | `END` | Beendet eine passende RPL-Kontrollstruktur. |
| 123 | `ENDSUB` | Liefert im DOSUBS-Kontext die Gesamtzahl der Teilfolgen/Durchläufe. |
| 124 | `ENG` | Stellt die Engineering-Zahlenanzeige ein. |
| 125 | `EQ→` | Zerlegt eine Gleichung in linke und rechte Seite. |
| 126 | `EQNLIB` | Öffnet die eingebaute Gleichungsbibliothek. |
| 127 | `ERASE` | Löscht den PICT-Bildinhalt unter Beibehaltung seiner Abmessungen. |
| 128 | `ERRM` | Liefert den Text des letzten Fehlers. |
| 129 | `ERRN` | Liefert die Nummer des letzten Fehlers. |
| 130 | `ERR0` | Setzt die letzten Fehlerdaten zurück (primär Fehlernummer; genaue Nebenwirkungen separat prüfen). |
| 131 | `EVAL` | Wertet ein Objekt bzw. einen Namen aus. |
| 132 | `EXP` | Berechnet die Exponentialfunktion e hoch x. |
| 133 | `EXPAN` | Expandiert einen algebraischen Ausdruck. |
| 134 | `EXPFIT` | Wählt das exponentielle Regressionsmodell. |
| 135 | `EXPM` | Berechnet exp(x) - 1 numerisch stabil für kleine x. |
| 136 | `EYEPT` | Setzt den Betrachtungsstandpunkt für perspektivische 3D-Plots; speichert ihn in YPAR. |
| 137 | `F0λ` | Berechnet den Anteil der Schwarzkörperstrahlung bis zu einer vorgegebenen Wellenlänge. |
| 138 | `FACT` | Berechnet die Fakultätsfunktion. |
| 139 | `FANNING` | Berechnet den Fanning-Reibungsfaktor aus Rauheit und Reynolds-Zahl. |
| 140 | `FC?` | Prüft, ob ein Flag gelöscht ist. |
| 141 | `FC?C` | Prüft und löscht ein Flag. |
| 142 | `FFT` | Berechnet eine diskrete Fourier-Transformation. |
| 143 | `FINDALARM` | Sucht den nächsten Alarm nach einer übergebenen Zeitangabe. |
| 144 | `FINISH` | Beendet den Kermit-Servermodus. |
| 145 | `FIX` | Stellt die Anzahl der angezeigten Dezimalstellen ein. |
| 146 | `FLOOR` | Liefert die größte ganze Zahl kleiner oder gleich dem Argument. |
| 147 | `FOR` | Beginn einer FOR-Zählschleife. |
| 148 | `FP` | Liefert den Nachkommaanteil einer reellen Zahl. |
| 149 | `FREE` | Trennt zuvor zusammengeführten Speicher von einem Port. |
| 150 | `FREE1` | Trennt zuvor zusammengeführten Speicher von Port 1. |

## 3. Dokumentierte Differenzen und semantische Hinweise

- **A03-130:** `ERRO` steht als Kandidat im gespeicherten AUR-TOC-Text, während Stock-ROM und Pocket Guide `ERR0` (Ziffer **Null**) ergeben. Im AUR-Quellindex **nicht stillschweigend überschreiben**; als `OCR_GLYPH_AMBIGUITY_PENDING_AUR_SCAN` führen. Kein zweiter `ERRO`-Befehl erfinden.
- **A03-123, `ENDSUB`:** In der ManualsLib-Web-OCR auf gedruckter S. 50 fehlt die Zeile, im unabhängig indizierten Original-Pocket-Guide-PDF-Text steht `ENDSUB` mit Bezug zu `DOSUBS`. Das ist eine **Darstellungs-/OCR-Lücke**; nicht als nicht existierendes Kommando werten. `ENDSUB` gibt die **Gesamtzahl** der DOSUBS-Teilfolgen zurück, nicht die Restanzahl.
- **A03-111 und A03-115:** `DROPN` verbraucht neben den n zu löschenden Stackobjekten auch sein Zählargument. `DUPN` verbraucht sein Zählargument und verdoppelt die n obersten Objekte, nicht beliebig n-mal ein einziges Objekt.
- **A03-119/120:** `EGV` liefert Eigenwerte **und** rechte Eigenvektoren; `EGVL` nur Eigenwerte.
- **A03-125:** `EQ→` zerlegt eine Gleichung in *beide* Seiten; die OCR-Texterkennung liest das Pfeilsymbol als Plus.
- **A03-127:** `ERASE` löscht die Grafik **PICT** bei gleicher Dimension; kein allgemeiner Displayspeicher-Reset.
- **A03-135:** `EXPM` ist die numerisch günstigere Berechnung von `exp(x)-1` nahe Null.
- **A03-136:** `EYEPT` gehört zum perspektivischen 3D-Plot; der Pocket Guide erwähnt das Ablegen der Koordinaten in `YPAR`.
- **A03-144:** `FINISH` beendet den **Kermit-Servermodus**; kein allgemeines RPL-`END`.
- **A03-149/150:** `FREE` trennt zusammengeführten Speicher eines benannten Ports; `FREE1` ist die auf Port 1 bezogene Variante. Beide sind nicht mit `MEM` oder Freigabe des Host-RAM gleichzusetzen.
- **A03-137:** `F0λ` und die teils beschädigten Symbolglyphen bedürfen visueller Gegenprüfung. Kein normalisierter Name allein darf hier als Druckseitenbeweis gelten.
- **Kompatibilitätsgrenze:** Die hochgeladene Datei mit Titel `HP 48GX grafikfähiger Taschenrechner.pdf` ist in Wahrheit ein Handbuch des **HP 48gII** (2004) und wird hier **nicht** als Primärbeleg für die 48GX-ROM-Funktionen verwendet.

## 4. Konkreter Abschluss dieser Tranche

- [x] AUR-TOC-Positionen 101–150 positionsgetreu erfasst; Original-Quellnamen im JSON unverändert.
- [x] Normierten ROM-Namen und XLIB für alle 50 Positionen geprüft.
- [x] Unabhängigen Pocket-Guide-Textabgleich für die gesamten 50 Namen dokumentiert; Quelle/Defizit bei `ENDSUB` offengelegt.
- [x] Funktionskurzbeschreibung je Eintrag als eigenständige Zusammenfassung festgehalten.
- [ ] Gedruckte AUR- und Pocket-Originalglyphen visuell Seite für Seite freigegeben.
- [ ] 50 vollständige AUR-Stackdiagramme, Objekttypen, Flags, Fehlerfälle, Gerätesemantik und Hardwareausführung geprüft.

**Checkpoint A03:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE` / `ORIGINAL_SCAN_NOT_SIGNED_OFF` / `AUR_STACK_NOT_SIGNED_OFF`. **Nächster Namenblock: A04 (151–200).** Die 58 Seiten des Appendix G, die Gleichungen und Einheiten verbleiben in ihren eigenen Tranchen; das historische Gesamt-Abnahmeziel bleibt `NO_GO`.
