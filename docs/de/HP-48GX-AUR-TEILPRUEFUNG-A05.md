# HP 48GX – AUR-Teilprüfung A05 (Positionen 201–250)

**Prüfstand:** 22.11.2026 · **Referenz:** serienmäßiger HP 48GX (ohne Fremdkarten).  
**Umfang:** AUR-Inhaltsindex `LINE` bis `→NUM`.  
**Prüfziel dieser Tranche:** **50 gedruckte AUR-Indexpositionen** (darin **49 unterschiedliche Namen**) positionsgetreu gegen den stock-48GX-ROM-Index und unabhängig zugänglichen Pocket-Guide-Text abgleichen. Die Inhaltsindex-Tabelle wiederholt `NEXT` auf den Positionen 244 und 245; diese beiden Nachweise dürfen nicht als zwei unterschiedliche Funktionen ausgegeben werden.

**Freigabegrenze:** Nur Indexnamen, Funktionskurzbeschreibungen und eindeutige ROM-Zuordnung abgeglichen. **Keine** visuelle Originalscan-Abnahme (AUR oder Pocket Guide), **keine** vollständigen AUR-Stackdiagramme, Geräteausführung, Genauigkeits- oder Fehlerfalldokumentation.

## 1. Quellen und belegte Grenzen

1. Hewlett-Packard, *HP 48G Series Advanced User's Reference*, **4. Auflage, Dezember 1994**, Kapitel 3, AUR-Inhaltsverzeichnisse `Contents-8` (Positionen 201–211) und `Contents-9` (212–250). Historische Indexdaten unverändert: [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json). Original: https://literature.hpcalc.org/community/hp48g-aur-en.pdf (72 MB, Originalscan aktuell nicht bildlich abrufbar).
2. *The HP 48G/GX Pocket Guide* von **Chris Coffin und Thomas Dick**, Grapevine Publications, 1996. Eigenständige Namens- und Kurzfunktionsbeschreibung: **Command Index, gedruckte S. 54, 56 und 58**, https://literature.hpcalc.org/community/hp48g-pg-en.pdf ; zugängliche OCR-Webansichten https://www.manualslib.com/manual/3743173/Hp-48g.html?page=56 , https://www.manualslib.com/manual/3743173/Hp-48g.html?page=58 und https://www.manualslib.com/manual/3743173/Hp-48g.html?page=60 . Das Titelblatt des unabhängig indizierten PDFs nennt ausdrücklich diese beiden Autoren. Frühere Berichte A01–A04 mit dem Autorennamen „James Donnelly“ sind **bibliographisch zu korrigieren**.
3. ROM-basierter Namensindex mit XLIB-IDs: [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json). Der Index beweist Namensvorkommen im originalen ROM, nicht alle Verhaltensvarianten. Zusätzliche Gegendarstellung: https://finseth.com/hpdata/hp48gx.php (48GX-Funktionsübersicht).

**Quellenkritik:** Die 34-MB-Pocket-PDF ist als strukturierter Text sichtbar, jedoch ließ sich ihre Original-PDF-Bildseite im Webzugriff wegen Größenbegrenzung nicht als Bild prüfen. Insbesondere gibt der extrahierte Pocket-Text zweimal `MMATCH` wieder, während das ROM `↑MATCH` und `↓MATCH` als verschiedene Befehle führt. Im Pocket-Text erscheint `△LIST` (andere Delta-Glyphe) und `+NUM` anstelle `→NUM`. Die *Schreibform* wird dadurch **nicht** als visuell geprüft markiert.

## 2. Alle 50 AUR-Positionen, unverändert mit Originalnamen

| AUR # | AUR-Originaltextname | AUR-TOC | ROM-Name/XLIB | Pocket-Druckseite | Pocket-Text-/OCR-Kandidat | Prüfung | Deutsche Kurzbeschreibung |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 201 | `LINE` | Contents-8 | `LINE` · `2:206` | 54 | `LINE` | Pocket-Textname bestätigt | Linie zeichnen. |
| 202 | `ΣLINE` | Contents-8 | `ΣLINE` · `2:314` | 54 | `ΣLINE` | Pocket-Textname bestätigt | Gibt die aus den Statistikdaten bestimmte Ausgleichsfunktion des aktuell gewählten Regressionsmodells zurück – nicht zwingend eine Gerade. |
| 203 | `LINFIT` | Contents-8 | `LINFIT` · `2:319` | 54 | `LINFIT` | Pocket-Textname bestätigt | Wählt die lineare Form als Regressionsmodell. |
| 204 | `LININ` | Contents-8 | `LININ` · `171:28` | 54 | `LININ` | Pocket-Textname bestätigt | Prüft, ob der angegebene algebraische Ausdruck bezüglich einer Variablen linear ist. |
| 205 | `LIST→` | Contents-8 | `LIST→` · `2:158` | 54 | `LIST→` | Pocket-Textname bestätigt | Legt die einzelnen Listenelemente in ihrer Reihenfolge auf den Stack und zusätzlich die Elementanzahl. |
| 206 | `→LIST` | Contents-8 | `→LIST` · `2:152` | 54 | `→LIST` | Pocket-Textname bestätigt | Verbraucht die Elementanzahl n und baut aus n Stackobjekten eine Liste. |
| 207 | `ΣLIST` | Contents-8 | `ΣLIST` · `171:104` | 56 | `ΣLIST` | Pocket-Textname bestätigt | Liste aufsummieren. |
| 208 | `ΔLIST` | Contents-8 | `ΔLIST` · `171:100` | 56 | `△LIST` | Pocket-OCR-Symbol unsicher | Wertet die Differenzen aufeinanderfolgender Elemente einer Liste aus (exakte Reihenfolge später testen). |
| 209 | `ΠLIST` | Contents-8 | `ΠLIST` · `171:106` | 56 | `ΠLIST` | Pocket-Textname bestätigt | Fasst Listenelemente zu ihrem Produkt zusammen. |
| 210 | `LN` | Contents-8 | `LN` · `2:94` | 56 | `LN` | Pocket-Textname bestätigt | Natürlicher Logarithmus. |
| 211 | `LNP1` | Contents-8 | `LNP1` · `2:97` | 56 | `LNP1` | Pocket-Textname bestätigt | Berechnet ln(1+x) auch für sehr kleines x numerisch genauer als LN(1+x). |
| 212 | `LOG` | Contents-9 | `LOG` · `2:95` | 56 | `LOG` | Pocket-Textname bestätigt | Zehnerlogarithmus. |
| 213 | `LOGFIT` | Contents-9 | `LOGFIT` · `2:320` | 56 | `LOGFIT` | Pocket-Textname bestätigt | Wählt das logarithmische Regressionsmodell. |
| 214 | `LQ` | Contents-9 | `LQ` · `171:61` | 56 | `LQ` | Pocket-Textname bestätigt | LQ-Faktorisierung mit Permutationsmatrix: P·A = L·Q (L untere Trapezform, Q orthogonal). |
| 215 | `LR` | Contents-9 | `LR` · `2:302` | 56 | `LR` | Pocket-Textname bestätigt | Berechnet Regressionskoeffizienten für das aktuell ausgewählte Fit-Modell; nicht ausschließlich lineare Regression. |
| 216 | `LSQ` | Contents-9 | `LSQ` · `171:54` | 56 | `LSQ` | Pocket-Textname bestätigt | Ermittelt eine Minimum-Norm-Lösung eines über-/unterbestimmten linearen Systems. |
| 217 | `LU` | Contents-9 | `LU` · `171:59` | 56 | `LU` | Pocket-Textname bestätigt | Zerlegt A in Permutations-, untere und obere Dreiecksmatrix, sodass P·A = L·U. |
| 218 | `MANT` | Contents-9 | `MANT` · `2:111` | 56 | `MANT` | Pocket-Textname bestätigt | Mantisse einer Zahl. |
| 219 | `↑MATCH` | Contents-9 | `↑MATCH` · `2:265` | 56 | `MMATCH` | Pocket-OCR-Symbol unsicher | Musterersetzung eines Teilausdrucks, beginnend beim innersten Ausdruck. |
| 220 | `↓MATCH` | Contents-9 | `↓MATCH` · `2:266` | 56 | `MMATCH` | Pocket-OCR-Symbol unsicher | Musterersetzung eines Teilausdrucks, beginnend beim äußersten Ausdruck. |
| 221 | `MAX` | Contents-9 | `MAX` · `2:106` | 56 | `MAX` | Pocket-Textname bestätigt | Maximum zweier Zahlen. |
| 222 | `MAXR` | Contents-9 | `MAXR` · `2:64` | 56 | `MAXR` | Pocket-Textname bestätigt | Größter positiver darstellbarer reeller Maschinenwert (bzw. symbolische Konstante). |
| 223 | `MAXΣ` | Contents-9 | `MAXΣ` · `2:296` | 56 | `MAXΣ` | Pocket-Textname bestätigt | Liefert je Daten-/Statistikspalte das Maximum aus ΣDAT. |
| 224 | `MCALC` | Contents-9 | `MCALC` · `171:115` | 56 | `MCALC` | Pocket-Textname bestätigt | Kennzeichnet MES-Variablen als vom Solver zu berechnen (nicht vom Benutzer vorgegeben). |
| 225 | `MEAN` | Contents-9 | `MEAN` · `2:297` | 56 | `MEAN` | Pocket-Textname bestätigt | Liefert Spaltenmittelwerte der Statistikdaten in ΣDAT. |
| 226 | `MEM` | Contents-9 | `MEM` · `2:344` | 56 | `MEM` | Pocket-Textname bestätigt | Liefert die aktuell verfügbaren freien Bytes des Nutzerspeichers. |
| 227 | `MENU` | Contents-9 | `MENU` · `2:348` | 56 | `MENU` | Pocket-Textname bestätigt | Aktiviert ein Menü anhand seiner Kennung/Nummer. |
| 228 | `MERGE` | Contents-9 | `MERGE` · `2:354` | 56 | `MERGE` | Pocket-Textname bestätigt | Bindet geeigneten RAM aus Karten-Port 1 in den Benutzerspeicher ein. |
| 229 | `MERGE1` | Contents-9 | `MERGE1` · `171:22` | 56 | `MERGE1` | Pocket-Textname bestätigt | Port-1-RAM einbinden wie MERGE, jedoch ohne Stackargument. |
| 230 | `MIN` | Contents-9 | `MIN` · `2:107` | 56 | `MIN` | Pocket-Textname bestätigt | Minimum zweier Zahlen. |
| 231 | `MINEHUNT` | Contents-9 | `MINEHUNT` · `171:117` | 56 | `MINEHUNT` | Pocket-Textname bestätigt | Startet das eingebaute Minehunt-Spiel. |
| 232 | `MINIT` | Contents-9 | `MINIT` · `171:112` | 56 | `MINIT` | Pocket-Textname bestätigt | Richtet die MES-Parameterstruktur ein. |
| 233 | `MINR` | Contents-9 | `MINR` · `2:65` | 56 | `MINR` | Pocket-Textname bestätigt | Kleinster positiver darstellbarer, nicht nullgleicher reeller Maschinenwert. |
| 234 | `MINΣ` | Contents-9 | `MINΣ` · `2:298` | 56 | `MINΣ` | Pocket-Textname bestätigt | Liefert je Daten-/Statistikspalte das Minimum aus ΣDAT. |
| 235 | `MITM` | Contents-9 | `MITM` · `171:113` | 56 | `MITM` | Pocket-Textname bestätigt | Ändert Titel und Reihenfolge der Variablen im Multiple Equation Solver. |
| 236 | `MOD` | Contents-9 | `MOD` · `2:110` | 56 | `MOD` | Pocket-Textname bestätigt | Liefert x−y·floor(x/y), nicht generell den Rest einer auf null gerundeten Ganzzahldivision. |
| 237 | `MROOT` | Contents-9 | `MROOT` · `171:116` | 56 | `MROOT` | Pocket-Textname bestätigt | Bestimmt eine Unbekannte über den Multiple Equation Solver. |
| 238 | `MSGBOX` | Contents-9 | `MSGBOX` · `171:93` | 56 | `MSGBOX` | Pocket-Textname bestätigt | Zeigt eine Meldung als Dialogfenster. |
| 239 | `MSOLVR` | Contents-9 | `MSOLVR` · `171:36, 171:111` | 56 | `MSOLVR` | Pocket-Textname bestätigt | Ruft den Mehrgleichungslöser auf; zwei ROM-XLIB-Kennungen zum selben Namen dokumentiert. |
| 240 | `MUSER` | Contents-9 | `MUSER` · `171:114` | 56 | `MUSER` | Pocket-Textname bestätigt | Kennzeichnet MES-Variablen als vom Benutzer vorgegebene Werte. |
| 241 | `NDIST` | Contents-9 | `NDIST` · `171:39` | 58 | `NDIST` | Pocket-Textname bestätigt | Normalverteilungs-Wahrscheinlichkeitsdichte für Mittelwert, Varianz und x. |
| 242 | `NEG` | Contents-9 | `NEG` · `2:60` | 58 | `NEG` | Pocket-Textname bestätigt | Vorzeichenwechsel. |
| 243 | `NEWOB` | Contents-9 | `NEWOB` · `2:39` | 58 | `NEWOB` | Pocket-Textname bestätigt | Erzeugt eine neue, unabhängige Version eines Objekts zur Speicherverwaltung. |
| 244 | `NEXT` | Contents-9 | `NEXT` · `1792:11` | 58 | `NEXT` | AUR-TOC-Dublette: 1 ROM-Name und 1 Pocket-Namenreferenz | Beendet START- bzw. FOR-Zählschleife; im AUR-Textinventar zweimal mit identischem Namen und Seitenverweis erfasst, eine ROM-Kennung. |
| 245 | `NEXT` | Contents-9 | `NEXT` · `1792:11` | 58 | `NEXT` | AUR-TOC-Dublette: 1 ROM-Name und 1 Pocket-Namenreferenz | Beendet START- bzw. FOR-Zählschleife; im AUR-Textinventar zweimal mit identischem Namen und Seitenverweis erfasst, eine ROM-Kennung. |
| 246 | `NOT` | Contents-9 | `NOT` · `2:231` | 58 | `NOT` | Pocket-Textname bestätigt | Logische/bitweise Negation. |
| 247 | `NOVAL` | Contents-9 | `NOVAL` · `171:91` | 58 | `NOVAL` | Pocket-Textname bestätigt | Spezialobjekt für ein zunächst leeres/nicht belegtes Feld in INFORM. |
| 248 | `NSUB` | Contents-9 | `NSUB` · `171:101` | 58 | `NSUB` | Pocket-Textname bestätigt | Position der gerade bearbeiteten Teilliste innerhalb von DOSUBS. |
| 249 | `NUM` | Contents-9 | `NUM` · `2:164` | 58 | `NUM` | Pocket-Textname bestätigt | Liefert den Zeichencode des ersten Zeichens einer Zeichenkette; nicht numerische Auswertung. |
| 250 | `→NUM` | Contents-9 | `→NUM` · `2:53` | 58 | `+NUM` | Pocket-OCR-Symbol unsicher | Erzwingt numerische Auswertung eines symbolischen Objekts; nicht mit NUM verwechseln. |

### Zähl- und Vergleichsbilanz

- **50/50 AUR-TOC-Positionen** einzeln berichtet; **49 verschiedene AUR-Namen**, weil der Index zwei unmittelbar aufeinanderfolgende `NEXT`-Zeilen hat.
- **50/50** normierte ROM-Zuordnungen nach Indexposition, aber **49/49 verschiedene ROM-Namen**. Bei `MSOLVR` enthält *ein* Name zwei XLIB-Kennungen (`171:36` und `171:111`).
- Im unabhängigen Pocket-Guide-Namenindex sind **49/49 verschiedene A05-Namen** kontextuell auffindbar. Die doppelte AUR-TOC-Position `NEXT` verwendet **denselben** Pocket-Namensbeleg. Daher: **50/50 Quellenpositionen zuordenbar, nur 49 verschiedene Pocket-Einträge**; kein Aufblasen der angeblich verfügbaren Befehlszahl.
- Keiner der 50 Namen wird im bestehenden Katalog gelöscht oder aufgrund einer OCR-Glyphe in einen neuen Befehl umbenannt.

## 3. Kritische Funktionsunterschiede und offene Deltas

- **#244–245 `NEXT`:** AUR-Quelltext besitzt denselben Namen **zweimal** mit derselben AUR-PDF-Seitenreferenz. Beide zeigen auf das **eine** ROM-Kommando `1792:11`, während der Pocket Guide `NEXT` einmal für **START**- und **FOR**-Schleifen nennt. Der gedruckte AUR-Seitenaufbau bleibt bis zur Sichtprüfung offen: Ein Doppel-Eintrag ist keine zweite Funktion.
- **#219/220 `↑MATCH`/`↓MATCH`:** getrennte ROM-Kommandos `2:265` und `2:266`. Die Pocket-OCR zeichnet beide als `MMATCH` auf. Bei der ersten Variante beginnt die Ersetzung beim **innersten**, bei der zweiten beim **äußersten** passenden Teilausdruck. Vor Freigabe der tatsächlichen Originalglyphen benötigen wir die gescannten Seiten.
- **#202 `ΣLINE`:** Der Pocket Guide sagt, es berechne die beste Anpassung mit dem **gewählten Fit-Modell**. Die bisherige Formulierung „Regressionsgerade“ war zu eng: logarithmisches, exponentielles und weitere Modelle dürfen nicht unbemerkt ausgeschlossen werden.
- **#215 `LR`:** Die Regressionskoeffizienten beziehen sich auf das **aktuell eingestellte Modell**; nicht automatisch eine lineare Gerade.
- **#205/206 `LIST→`/`→LIST`:** Die Zerlegung legt die Elemente sowie ein Größenargument ab; der Umkehrbefehl verbraucht die Zahl `n`. Die Stackreihenfolge muss in der späteren AUR-Verhaltensprüfung exakt belegt werden.
- **#214 `LQ` und #217 `LU`:** Der unabhängige Guide dokumentiert Faktorisierungen in **drei** Matrizen jeweils inklusive Permutation (`P·A=L·Q` bzw. `P·A=L·U`); diese Ergebnisse nicht auf nur zwei Matrizen reduzieren.
- **#223/225/234 `MAXΣ`/`MEAN`/`MINΣ`:** beziehen sich auf **Statistikspalten in `ΣDAT`**, nicht ein einzelnes skalares Maximum bzw. Minimum ohne Dimension.
- **#224/240 `MCALC`/`MUSER`:** markieren im Multiple Equation Solver Werte für Solver-Berechnung bzw. Benutzereingabe; nicht mit `MROOT` (Lösen nach einer Variable) gleichsetzen.
- **#228/229 `MERGE`/`MERGE1`:** richten sich an historischen **Port-1-RAM**, nicht an Speicherverwaltung des Host-Betriebssystems.
- **#236 `MOD`:** Der Guide definiert `x mod y = x - y·floor(x/y)`; für negative Zahlen nicht zwangsläufig identisch mit einem hostsprachlichen `%`-Operator.
- **#238 `MSGBOX`:** interaktives Meldungsfenster gehört in den Bedienkatalog, auch wenn es als ROM-Kommando vorhanden ist.
- **#241 `NDIST`:** Normalverteilungsdichte; die genaue Eingabereihenfolge der Parameter Mittelwert, Varianz und Wert `x` bleibt für Verhaltensstufe V offen.
- **#247 `NOVAL`:** Platzhalterobjekt für nicht belegte Eingabefelder bei `INFORM`, nicht gewöhnlicher Zahlenwert.
- **#248 `NSUB`:** Zähl-/Teilfolgenposition im `DOSUBS`-Kontext; bei der Verhaltensprüfung zusammen mit `ENDSUB` behandeln.
- **#249/250 `NUM`/`→NUM`:** `NUM` liefert den Zeichencode des ersten Stringzeichens, `→NUM` fordert eine numerische Berechnung; zwei vollkommen unterschiedliche Funktionen.

## 4. Abschluss der A05-Namens-Tranche

- [x] Exakt 50 AUR-TOC-Positionen mit Quellnamen, Indexseiten und ROM-Kennungen gespeichert.
- [x] AUR-Dublette `NEXT` identifiziert (49 unterschiedliche Befehlsnamen), ohne sie stillschweigend zu entfernen.
- [x] 49 verschiedene Namen unabhängig im Pocket-Guide-Text belegt, einschließlich zwei getrennt interpretierter MATCH-Symbole.
- [x] Für jede AUR-Position eine eigenständig formulierte Kurzbeschreibung dokumentiert und die wichtigsten Bedeutungsfallen erkannt.
- [ ] Alle Original-PDF-Bildseiten visuell mit Fundseitenhash und Druckglyphen kontrolliert.
- [ ] 49 Einzelbefehle inkl. aller Stackvarianten/Objekttypen/Flags/Fehler an AUR bzw. Hardware abgenommen.

**A05-Status:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE`, `SCAN_PENDING`, `STACK_AND_HARDWARE_PENDING`. Nächster AUR-Namensblock: **A06 (251–300: `NUMX` bis `PVARS`)**. Historische Gesamtvollständigkeit weiterhin nicht freigegeben; keine Abhängigkeit zur ersten iPhone-Rechner-Version.
