# HP 48GX – AUR-Teilprüfung A04 (Positionen 151–200)

**Stand:** 22.11.2026 · **Gerät:** serienmäßiger HP 48GX ohne Fremdkarten.  
**Umfang:** `FREEZE` bis `LIBS`, 50 AUR-Indexeinträge.  
**Status:** AUR-TOC–ROM–Pocket-Guide-**Textvergleich abgeschlossen**; weder Originalscan-Glyphen noch alle AUR-Stackdiagramme, typabhängige Fehlerfälle und Gerätesemantik sind vollständig geprüft.

## 1. Originalquellen, Abgrenzung und Methode

- Hewlett-Packard: *HP 48G Series Advanced User's Reference*, 4. Auflage 1994, Kapitel 3 und Inhaltsverzeichnis `Contents-7/8`, https://literature.hpcalc.org/community/hp48g-aur-en.pdf . Der festgeschriebene Quelltextindex steht in [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json).
- Aus dem 48GX-ROM ausgelesener und versionierter [Namens- und XLIB-Index](../reference/hp48gx-rom-index-baseline.json). Ein ROM-Namensindex ist nicht die vollständige Menge der interaktiven Bedienoperationen oder historischen Kompatibilitätsnamen.
- Chris Coffin und Thomas Dick: *The HP 48G/GX Pocket Guide*, Command Index, gedruckte S. 52 und 54, https://literature.hpcalc.org/community/hp48g-pg-en.pdf ; ergänzende Textansichten https://www.manualslib.com/manual/3743173/Hp-48g.html?page=54 und https://www.manualslib.com/manual/3743173/Hp-48g.html?page=56 .
- Unabhängige 48GX-Grafikmenüübersicht für den Fall `GXOR`: https://finseth.com/hpdata/hp48gx.php .

Die Pocket-Guide-PDF ist in der Webansicht nur **textuell** auslesbar; der Versuch, Originalbildseiten abzurufen, scheiterte an der Dateigröße. Alle aus dem PDF-Text erkannten Druckglyphen bleiben **nicht visuell freigegeben**. Die Kurzbeschreibungen sind eigene Zusammenfassungen des Pocket-Texts oder Arbeitsbeschreibungen des bestehenden Hauptkatalogs; sie ersetzen keine verifizierten AUR-Befehlsspezifikationen.

## 2. Vollständiger 50-Positionen-Abgleich

| AUR # | AUR-Name | AUR-TOC-Seite | ROM/XLIB | Pocket-Druckseite | Pocket-Textkandidat | Klasse | Arbeitsbeschreibung |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 151 | `FREEZE` | Contents-7 | `FREEZE` · `2:51` | 52 | `FREEZE` | Textname zugeordnet | Einzelne Displaybereiche mit Maske 1 (Status), 2 (Stack/Eingabe), 4 (Menüs) einfrieren. |
| 152 | `FS?` | Contents-7 | `FS?` · `2:133` | 52 | `FS?` | Textname zugeordnet | Testen ob Flag gesetzt ist. |
| 153 | `FS?C` | Contents-7 | `FS?C` · `2:142` | 52 | `FS?C` | Textname zugeordnet | Flag testen und löschen. |
| 154 | `FUNCTION` | Contents-7 | `FUNCTION` · `2:220` | 52 | `FUNCTION` | Textname zugeordnet | Funktionsplot aktivieren. |
| 155 | `GET` | Contents-7 | `GET` · `2:178` | 52 | `GET` | Textname zugeordnet | Element an einer Position lesen. |
| 156 | `GETI` | Contents-7 | `GETI` · `2:179` | 52 | `GETI` | Textname zugeordnet | Liest Element und liefert Container sowie nächste Position für weitere Lesezugriffe. |
| 157 | `GOR` | Contents-7 | `GOR` · `2:211` | 52 | `GOR` | Textname zugeordnet | Grafikobjekte per OR überlagern. |
| 158 | `GRAD` | Contents-7 | `GRAD` · `2:137` | 52 | `GROB` | Pocket-OCR-Form abweichend | Winkelmaß Gon auswählen, nicht mit GROB zu verwechseln. |
| 159 | `GRAPH` | Contents-7 | — | 52 | `GRAPH` | AUR/Pocket-Sondername; kein ROM-XLIB | Picture-/Grafikumgebung aufrufen, historischer AUR-Bedienbefehl ohne eigene XLIB-Kennung. |
| 160 | `GRIDMAP` | Contents-7 | `GRIDMAP` · `171:10` | 52 | `GRIDMAP` | Textname zugeordnet | 3D-Gitterabbildung aktivieren. |
| 161 | `→GROB` | Contents-7 | `→GROB` · `2:215` | 52 | `→GROB` | Textname zugeordnet | Objekt als Grafikobjekt darstellen. |
| 162 | `GXOR` | Contents-7 | `GXOR` · `2:212` | 52 | `GYOR` | Pocket-OCR-Form abweichend | Überlagert Pixel von GROBs per XOR, nicht per OR (AUR-Detailprüfung offen). |
| 163 | `*H` | Contents-7 | `*H` · `2:189` | 52 | `*H` | Textname zugeordnet | Vertikale Plot-Skalierung ändern. |
| 164 | `HALT` | Contents-7 | `HALT` · `1792:14` | 52 | `HALT` | Textname zugeordnet | Programmausführung anhalten. |
| 165 | `HEAD` | Contents-7 | `HEAD` · `171:96` | 52 | `HEAD` | Textname zugeordnet | Erstes Objekt einer Liste bzw. erstes Zeichen eines Strings extrahieren. |
| 166 | `HEX` | Contents-7 | `HEX` · `2:146` | 52 | `HEX` | Textname zugeordnet | Hexadezimale Anzeigeform. |
| 167 | `HISTOGRAM` | Contents-7 | `HISTOGRAM` · `2:226` | 52 | `HISTOGRAM` | Textname zugeordnet | Histogramm als Plottyp auswählen. |
| 168 | `HISTPLOT` | Contents-7 | `HISTPLOT` · `2:317` | 52 | `HISTPLOT` | Textname zugeordnet | Histogramm der konfigurierten Statistikdaten zeichnen. |
| 169 | `HMS+` | Contents-7 | `HMS+` · `2:116` | 52 | `HMS+` | Textname zugeordnet | Zeitwerte im H.MMSS-Format addieren. |
| 170 | `HMS−` | Contents-7 | `HMS-` · `2:117` | 52 | `HMS−` | AUR/ROM-Glyphennormalisierung | Zeitwerte im H.MMSS-Format subtrahieren. |
| 171 | `HMS→` | Contents-8 | `HMS→` · `2:115` | 52 | `HMS÷` | Pocket-OCR-Form abweichend | Zeitformat HH.MMSS in Dezimalstunden umwandeln. |
| 172 | `→HMS` | Contents-8 | `→HMS` · `2:114` | 52 | `÷HMS` | Pocket-OCR-Form abweichend | Dezimalstunden in HH.MMSS-Zeitdarstellung umwandeln. |
| 173 | `HOME` | Contents-8 | `HOME` · `2:34` | 52 | `HOME` | Textname zugeordnet | HOME-Verzeichnis wählen. |
| 174 | `i` | Contents-8 | `i` · `2:67` | 52 | `i` | Textname zugeordnet | Symbolische imaginäre Einheit. |
| 175 | `IDN` | Contents-8 | `IDN` · `2:174` | 52 | `IDN` | Textname zugeordnet | Identitätsmatrix anhand einer Dimension bzw. quadratischen Matrix erzeugen. |
| 176 | `IF` | Contents-8 | `IF` · `1792:0` | 52 | `IF` | Textname zugeordnet | Bedingte Programmverzweigung beginnen. |
| 177 | `IFERR` | Contents-8 | `IFERR` · `1792:13` | 52 | `IFERR` | Textname zugeordnet | Fehlerbehandlungsstruktur beginnen. |
| 178 | `IFFT` | Contents-8 | `IFFT` · `171:38` | 52 | `IFFT` | Textname zugeordnet | Inverse schnelle Fourier-Transformation. |
| 179 | `IFT` | Contents-8 | `IFT` · `2:48` | 52 | `IFT` | Textname zugeordnet | Objekt nur bei wahrer Bedingung auswerten; sonst verwerfen. |
| 180 | `IFTE` | Contents-8 | `IFTE` · `2:47` | 54 | `IFTE` | Textname zugeordnet | Abhängig von Bedingung eines von zwei Objekten auswerten. |
| 181 | `IM` | Contents-8 | `IM` · `2:155` | 54 | `IM` | Textname zugeordnet | Imaginärteil. |
| 182 | `INCR` | Contents-8 | `INCR` · `2:331` | 54 | `INCR` | Textname zugeordnet | Erhöht den Inhalt einer benannten Variablen um eins. |
| 183 | `INDEP` | Contents-8 | `INDEP` · `2:183` | 54 | `INDEP` | Textname zugeordnet | Unabhängige Plotvariable festlegen. |
| 184 | `INFORM` | Contents-8 | `INFORM` · `171:90` | 54 | `INFORM` | Textname zugeordnet | Konfigurierbares interaktives Eingabeformular mit mehreren Feldern anzeigen. |
| 185 | `INPUT` | Contents-8 | `INPUT` · `2:378` | 54 | `INPUT` | Textname zugeordnet | Eingabe in der Kommandozeile anfordern. |
| 186 | `INV` | Contents-8 | `INV` · `2:76` | 54 | `INV` | Textname zugeordnet | Kehrwert bzw. Matrixinverse. |
| 187 | `IP` | Contents-8 | `IP` · `2:101` | 54 | `IP` | Textname zugeordnet | Ganzzahligen Anteil bilden, nicht gleich FLOOR bei negativen Zahlen. |
| 188 | `IR` | Contents-8 | — | 54 | `IR` | AUR/Pocket-Sondername; kein ROM-XLIB | Übertragungsweg seriell/infrared umschalten, kein Kermit-Transferbefehl. |
| 189 | `ISOL` | Contents-8 | `ISOL` · `2:336` | 54 | `ISOL` | Textname zugeordnet | Gleichung nach einer Variablen auflösen. |
| 190 | `KERRM` | Contents-8 | `KERRM` · `2:373` | 54 | `KERRM` | Textname zugeordnet | Kermit-Fehler lesen. |
| 191 | `KEY` | Contents-8 | `KEY` · `2:57` | 54 | `KEY` | Textname zugeordnet | Tastenzustand lesen. |
| 192 | `KGET` | Contents-8 | `KGET` · `2:364` | 54 | `KGET` | Textname zugeordnet | Daten von Kermit-Server anfordern. |
| 193 | `KILL` | Contents-8 | `KILL` · `2:40` | 54 | `KILL` | Textname zugeordnet | Angehaltenes Programm beenden. |
| 194 | `LABEL` | Contents-8 | `LABEL` · `2:201` | 54 | `LABEL` | Textname zugeordnet | Achsenbeschriftungen setzen. |
| 195 | `LAST` | Contents-8 | — | 54 | `LASTARG or LAST` | AUR/Pocket-Sondername; kein ROM-XLIB | Historischer Alias von LASTARG; liefert frühere Argumente, nicht den letzten Stack. |
| 196 | `LASTARG` | Contents-8 | `LASTARG` · `2:54` | 54 | `LASTARG` | Textname zugeordnet | Letzte Argumente wiederherstellen. |
| 197 | `LCD→` | Contents-8 | `LCD→` · `2:213` | 54 | `LCD→` | Textname zugeordnet | Aktuelles LCD als GROB mit 131×64 Pixeln erfassen. |
| 198 | `→LCD` | Contents-8 | `→LCD` · `2:214` | 54 | `→LCD` | Textname zugeordnet | GROB auf das Display zeichnen. |
| 199 | `LIBEVAL` | Contents-8 | `LIBEVAL` · `171:30` | 54 | `LIBEVAL` | Textname zugeordnet | Bibliotheksfunktion per XLIB-ID ausführen. |
| 200 | `LIBS` | Contents-8 | `LIBS` · `2:356` | 54 | `LIBS` | Textname zugeordnet | Dem aktuellen Verzeichnis angehängte Bibliotheken anzeigen. |

## 3. Befunde und Nacharbeit

**Bilanz: 50/50 AUR-Indexpositionen und 50/50 kontextuelle Pocket-Guide-Textzuordnungen.** **47/50** AUR-Namen besitzen eine eigene normierte ROM-XLIB-Zuordnung, **3** sind separat geführte Dokumentations-/Bedien- oder Aliasfälle. „Textzuordnung“ heißt **nicht**, dass jede PDF-Glyphe korrekt extrahiert oder jeder Befehl auf Hardware ausgeführt wurde.

### AUR-Namen ohne eigene ROM-Namenskennung

- **#159 `GRAPH`:** im Pocket Guide als eintippbarer Zugang zur interaktiven Picture-/Grafikumgebung beschrieben; keine eigene XLIB-Namenskennung im Inventar. Darf nicht als fehlende Funktion interpretiert werden. Exakte Einbindung und Ausführbarkeit später prüfen.
- **#188 `IR`:** schaltet die Infrarot-/serielle I/O-Auswahl um. Nicht identisch mit `KGET` und anderen Transferbefehlen; AUR-/Pocket-Name, kein separater XLIB-Name.
- **#195 `LAST`:** der Pocket Guide nennt `LASTARG or LAST`. Historischer Kompatibilitätsname, dieselbe Bedeutung wie `LASTARG` (ROM `2:54`): vorherige **Argumente**, nicht der vorherige Stackzustand.

### Auflösbare und offene Quell-Unterschiede

- **#158 `GRAD`:** Pocket-PDF-Text schreibt `GROB`, obwohl die Wirkung eindeutig der Winkelmodus Gon ist; `GROB` ist ein anderer Objekttyp. Originalbildvergleich nötig.
- **#162 `GXOR`:** PDF-OCR `GYOR` und eine OR-ähnliche Kurzbeschreibung, während ROM `GXOR` (`2:212`) und das unabhängige Menü diesen Namen stützen. Die XOR-Semantik ist in der späteren AUR-Verhaltensprüfung festzuhalten.
- **#170 `HMS−` gegenüber ROM `HMS-`:** typographische Minuszeichen-Differenz, kein neuer Befehl.
- **#171/172 `HMS→`/`→HMS`:** OCR `HMS÷`/`÷HMS`. Die Quellen beschreiben Umrechnungen zwischen Zeitformat und Dezimalstunden, keine Division.
- **#155/156 `GET`/`GETI`:** `GETI` gibt nicht nur ein Element, sondern zusätzlich Position/Container für weiteres Iterieren zurück.
- **#167/168 `HISTOGRAM`/`HISTPLOT`:** Plottyp auswählen vs. Histogramm erzeugen.
- **#179/180 `IFT`/`IFTE`:** ein bedingt auszuführendes Objekt vs. alternative Ausdrücke.
- **#187 `IP`/`FLOOR`:** Ganzzahlanteil vs. Abrundung.
- **#199 `LIBEVAL`:** Bibliothekseinstieg anhand XLIB auf dem historischen Rechner. In SASD nur als emulierte Bibliotheksfunktion, **nicht** als Host-Codeberechtigung.
- **#200 `LIBS`:** dem aktuellen Verzeichnis angehängte Bibliotheken, nicht pauschal alle vorhandenen Bibliotheken.

## 4. Prüffortschritt

- [x] 50 AUR-Positionen mit Originalnamen und Indexseite in einer separaten Tabelle.
- [x] 47 ROM-Namen und ihre XLIB-Kennungen nachgewiesen; 3 fehlende eigene XLIB-Namen gesondert klassifiziert.
- [x] 50 Pocket-Guide-Textpositionen kontextuell zugeordnet, OCR-/Aliasunsicherheiten ausdrücklich gelistet.
- [x] 50 deutsche Arbeits-Kurzbeschreibungen dokumentiert.
- [ ] Original-PDF-Bildseiten visuell gegen Druckzeichen prüfen.
- [ ] AUR-Stackdiagramme, Objekttypen, Flags, Fehlerfälle und Hardwareausführung einzeln belegen.

**A04-Abschlussstatus:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE` / `ORIGINAL_SCAN_NOT_SIGNED_OFF` / `AUR_STACK_NOT_SIGNED_OFF`. Nächste AUR-Namen-Tranche **A05 (201–250: `LINE` bis `→NUM`)**. Gesamt-Vollständigkeitsfreigabe weiterhin `HISTORICAL_COMPLETENESS_NOT_CERTIFIED`.

**Bibliographische Quellenkorrektur (22.11.2026):** Der tatsächlich verlinkte *HP 48G/GX Pocket Guide* wurde von **Chris Coffin und Thomas Dick** verfasst (Grapevine Publications, 1996); der früher irrtümlich genannte Autor James Donnelly ist bei diesem konkreten Buchtitel falsch. Korrigiert wurde ausschließlich der Quellennachweis, nicht der behauptete Status der historisch geprüften Befehle. Quelle: https://literature.hpcalc.org/items/1739 .
