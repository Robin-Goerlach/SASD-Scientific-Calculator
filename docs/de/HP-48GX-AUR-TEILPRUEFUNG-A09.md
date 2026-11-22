# HP 48GX – AUR-Teilprüfung A09 (Positionen 401–450)

**Stand:** 22.11.2026 · **Referenzgerät:** serienmäßiger HP 48GX ohne Fremdkarten.  
**Gegenstand:** 50 AUR-TOC-Positionen von `STEQ` bis `UBASE`.  
**Status dieser Tranche:** Positionsgenauer **Namens- und Kurzfunktions-Textabgleich**, noch **keine** bildliche Originalscan-Freigabe, keine vollständige AUR-Stack-/Flag-/Fehlerfallprüfung und keine Geräteausführung. Ein korrekter ROM-Indexname belegt nicht bereits eine kompatible Implementation.

## 1. Quellen und Zuverlässigkeit

1. Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Ausgabe (1994), Kapitel-3-Inhaltsverzeichnis `Contents-13` und `Contents-14`; im Repository als Original-TOC-**Texttranskription** [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json). Referenz-Original: https://literature.hpcalc.org/community/hp48g-aur-en.pdf . Die sekundären PDF-Seitenhinweise sind Locator-Hilfen, **keine** belegte Sichtprüfung. Der sehr auffällige PDF-Hinweis `18` bei **#417 `SVD`** wird als Datenqualitätsfrage gesondert markiert.
2. Aus der Stock-48GX-ROM-Namensliste abgeleitete XLIB-IDs: [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json). Für alle 50 gedruckten AUR-Namen eine direkte normierte Zuordnung.
3. Chris Coffin und Thomas Dick, *The HP 48G/GX Pocket Guide* (Grapevine, April 1996), **Command Index gedruckte Seiten 68, 70 und 72**. Unabhängig zugängliche **Web-OCR-Texte** der betreffenden Blattseiten: https://www.manualslib.com/manual/3743173/Hp-48g.html?page=70 (gedruckte S. 68), https://www.manualslib.com/manual/3743173/Hp-48g.html?page=72 (S. 70), https://www.manualslib.com/manual/3743173/Hp-48g.html?page=74 (S. 72). Bibliographischer Eintrag: https://literature.hpcalc.org/items/1739 .
4. Weitere, ausdrücklich **sekundäre** Kontrolle: James Donnelly, *HP 48 Pocket Book*, https://literature.hpcalc.org/community/hp48g-pb.pdf , das u. a. `TRUTH`, `TSTR`, `TVMROOT` und `UBASE` beschreibt. Dieses Buch ist **nicht** mit dem Guide von Coffin/Dick zu verwechseln.

**OCR-Freigabegrenze:** Der Webtext enthält massive Zeichenverwechslungen bei `STO−`/`STO/`, `STO*`, `STOΣ`, `STR→`, `→STR`, `SVD`, `%T`, `→TAG`, `TAIL`, `→TIME`, `TMENU`, `UBASE` und zahlreichen weiteren Namen. Die 50 Textpositionen sind **kontextuell** anhand alphabetischer Folge und Funktionsbeschreibung zugeordnet, nicht zeichengenau am Original abgenommen. Bis zur Sichtkontrolle gehören die Pocket-Rohformen **nicht** als angebliche neue ROM-Namen in den Katalog.

## 2. AUR-Quellpositionen mit unabhängigem Namen-/Textabgleich

| AUR # | AUR-Quelltextname | AUR-TOC-Seite | ROM-Name / XLIB | Pocket-Druckseite | AUR-PDF-Hinweis (ungeprüft) | Pocket-Web-OCR-Text | Textstatus | Funktionsbeschreibung (eigene Formulierung) |
| ---: | --- | --- | --- | --- | ---: | --- | --- | --- |
| 401 | `STEQ` | Contents-13 | `STEQ` / `2:250` | 68 | 488 | `STER` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Legt ein Objekt als aktuell zu verwendende Gleichung in der reservierten Variable EQ ab. |
| 402 | `STIME` | Contents-13 | `STIME` / `2:375` | 68 | 488 | `STIME` | KONTEXTUELLER_POCKET_TREFFER | Stellt die Zeitüberschreitung für SRECV und WAIT ein; keine Einstellung der Systemuhr. |
| 403 | `STO` | Contents-13 | `STO` / `2:341` | 68 | 489 | `STO` | KONTEXTUELLER_POCKET_TREFFER | Speichert ein Objekt unter dem angegebenen Variablennamen. |
| 404 | `STOALARM` | Contents-13 | `STOALARM` / `2:25` | 68 | 490 | `STORLARM` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Speichert einen Alarm mit Zeitpunkt und zugehöriger Aktion. |
| 405 | `STOF` | Contents-13 | `STOF` / `2:151` | 68 | 491 | `STOF` | KONTEXTUELLER_POCKET_TREFFER | Stellt einen vollständigen Flagsatz aus dem übergebenen Objekt wieder her. |
| 406 | `STOKEYS` | Contents-13 | `STOKEYS` / `2:380` | 68 | 492 | `STOKEYS` | KONTEXTUELLER_POCKET_TREFFER | Legt benutzerdefinierte Tastenbelegungen fest. |
| 407 | `STO+` | Contents-13 | `STO+` / `2:327` | 68 | 493 | `ST+` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Addiert zu einem benannten Variablenwert ein Objekt und speichert das Ergebnis zurück. |
| 408 | `STO−` | Contents-13 | `STO-` / `2:328` | 68 | 494 | `ST0-` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Subtrahiert ein Objekt vom benannten Wert (oder umgekehrte Operandform) und speichert das Ergebnis. |
| 409 | `STO*` | Contents-13 | `STO*` / `2:330` | 68 | — | `5T0#` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Multipliziert einen benannten Variablenwert mit dem Objekt und speichert das Ergebnis. |
| 410 | `STO/` | Contents-13 | `STO/` / `2:329` | 68 | 495 | `ST0-` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Dividiert den benannten Wert durch ein Objekt (oder umgekehrte Operandform) und speichert das Ergebnis. |
| 411 | `STOΣ` | Contents-13 | `STOΣ` / `2:283` | 68 | — | `STOZ` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Speichert das übergebene Objekt als Statistikdaten in ΣDAT. |
| 412 | `STREAM` | Contents-13 | `STREAM` / `171:103` | 70 | 497 | `STREAM` | KONTEXTUELLER_POCKET_TREFFER | Reduziert eine Liste schrittweise: wertet ein Programm mit aktuellem Listenelement und vorherigem Ergebnis aus; am Anfang mit den ersten zwei Listenelementen. |
| 413 | `STR→` | Contents-13 | `STR→` / `2:163` | 70 | 497 | `5TRE+` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Parst eine Zeichenkette als Objekt; der Pocket Guide vergleicht das Ergebnis mit OBJ→ auf einer Zeichenkette. |
| 414 | `→STR` | Contents-13 | `→STR` / `2:162` | 70 | 498 | `+5TR` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Wandelt ein Objekt in seine textuelle Zeichenkettendarstellung um. |
| 415 | `STWS` | Contents-13 | `STWS` / `2:148` | 70 | 499 | `STHS` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Setzt die aktive Binärwortbreite in Bits. |
| 416 | `SUB` | Contents-13 | `SUB` / `2:156` | 70 | — | `SUB` | KONTEXTUELLER_POCKET_TREFFER | Extrahiert einen Abschnitt aus Liste, Zeichenkette oder GROB anhand Start- und Endposition. |
| 417 | `SVD` | Contents-14 | `SVD` / `171:57` | 70 | 18 | `S0` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Führt eine Singulärwertzerlegung einer Matrix durch und liefert zugehörige Faktoren einschließlich Singulärwerten. |
| 418 | `SVL` | Contents-14 | `SVL` / `171:58` | 70 | 502 | `SVL` | KONTEXTUELLER_POCKET_TREFFER | Liefert die Singulärwerte einer Matrix; nicht die gesamte SVD-Zerlegung. |
| 419 | `SWAP` | Contents-14 | `SWAP` / `2:271` | 70 | 502 | `ShAP` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Vertauscht die beiden obersten Stackobjekte. |
| 420 | `SYSEVAL` | Contents-14 | `SYSEVAL` / `2:49` | 70 | 503 | `SYSEVAL` | KONTEXTUELLER_POCKET_TREFFER | Wertet einen System-Einstiegspunkt des historischen HP-Betriebssystems aus; nur in sicherer historischer Emulation, nie als Host-Codeaufruf. |
| 421 | `%T` | Contents-14 | `%T` / `2:125` | 70 | 503 | `&1` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Berechnet, wie viel Prozent der erste Zahlenwert durch den zweiten repräsentiert wird. |
| 422 | `→TAG` | Contents-14 | `→TAG` / `2:383` | 70 | 505 | `+TAG` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Erzeugt ein markiertes Objekt aus Inhalt und angegebenem Tag-/Namenstext. |
| 423 | `TAIL` | Contents-14 | `TAIL` / `171:97` | 70 | 505 | `TRIL` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Liefert Liste oder Zeichenkette ohne das erste Element bzw. Zeichen. |
| 424 | `TAN` | Contents-14 | `TAN` / `2:83` | 70 | 506 | `THAN` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Berechnet den Tangens im eingestellten Winkelmodus. |
| 425 | `TANH` | Contents-14 | `TANH` / `2:86` | 70 | 507 | `THMH` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Berechnet den hyperbolischen Tangens. |
| 426 | `TAYLR` | Contents-14 | `TAYLR` / `2:339` | 70 | 507 | `TAYLR` | KONTEXTUELLER_POCKET_TREFFER | Berechnet das Taylorpolynom der angegebenen Ordnung eines algebraischen Ausdrucks in einer Variablen. |
| 427 | `TDELTA` | Contents-14 | `TDELTA` / `171:123` | 70 | 508 | `TOELTA` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Berechnet eine Temperaturdifferenz aus zwei Temperaturwerten. |
| 428 | `TEACH` | Contents-14 | `TEACH` / `171:17` | 70 | 509 | `TEACH` | KONTEXTUELLER_POCKET_TREFFER | Erzeugt ein EXAMPLES-Unterverzeichnis mit Lehr-/Beispielobjekten. |
| 429 | `TEXT` | Contents-14 | `TEXT` / `2:217` | 70 | 509 | `TEXT` | KONTEXTUELLER_POCKET_TREFFER | Schaltet bei der nächsten Aktualisierung zur normalen Stackdarstellung zurück. |
| 430 | `THEN` | Contents-14 | `THEN` / `1792:1, 1792:24, 1792:26` | 70 | 510 | `THEN` | KONTEXTUELLER_POCKET_TREFFER | Beginnt den Wahr-Zweig in einer IF-/CASE-/IFERR-Kontrollstruktur je Kontext. |
| 431 | `TICKS` | Contents-14 | `TICKS` / `2:18` | 70 | 510 | `TICKS` | KONTEXTUELLER_POCKET_TREFFER | Liefert die interne Systemzeit in Einheiten von 1/8192 Sekunde. |
| 432 | `TIME` | Contents-14 | `TIME` / `2:16` | 70 | 511 | `TIME` | KONTEXTUELLER_POCKET_TREFFER | Liest die aktuelle Systemuhrzeit im Format HH.MMSSs. |
| 433 | `→TIME` | Contents-14 | `→TIME` / `2:23` | 70 | 511 | `+TIME` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Stellt die Systemuhr anhand einer Uhrzeit im Format HH.MMSSs. |
| 434 | `TINC` | Contents-14 | `TINC` / `171:124` | 70 | 512 | `TINC` | KONTEXTUELLER_POCKET_TREFFER | Berechnet neue Temperatur aus Ausgangstemperatur und Temperaturänderung. |
| 435 | `TLINE` | Contents-14 | `TLINE` / `2:207` | 70 | 513 | `TLINE` | KONTEXTUELLER_POCKET_TREFFER | Invertiert sämtliche Pixel entlang einer Linie zwischen zwei Koordinaten im Grafikobjekt PICT. |
| 436 | `TMENU` | Contents-14 | `TMENU` / `2:347` | 70 | 514 | `THENLU` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Zeigt ein angegebenes Menü vorübergehend, ohne den Inhalt der reservierten Menüvariable CST zu verändern. |
| 437 | `TOT` | Contents-14 | `TOT` / `2:300` | 70 | 515 | `T0T` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Berechnet Summen je Spalte der Statistikdaten in ΣDAT. |
| 438 | `TRACE` | Contents-14 | `TRACE` / `171:50` | 70 | 515 | `TRACE` | KONTEXTUELLER_POCKET_TREFFER | Berechnet die Matrixspur als Summe der Hauptdiagonale; nicht das interaktive Nachfahren einer Plotkurve. |
| 439 | `TRANSIO` | Contents-14 | `TRANSIO` / `2:372` | 70 | 516 | `TRANSIO` | KONTEXTUELLER_POCKET_TREFFER | Wählt die Zeichenübersetzung bei I/O-Übertragung; nicht die physische Schnittstelle. |
| 440 | `TRN` | Contents-14 | `TRN` / `2:175` | 70 | 517 | `TRN` | KONTEXTUELLER_POCKET_TREFFER | Transponiert eine Matrix. |
| 441 | `TRNC` | Contents-14 | `TRNC` / `2:109` | 70 | 517 | `TRNC` | KONTEXTUELLER_POCKET_TREFFER | Schneidet eine reelle Zahl abhängig vom Parameter auf Dezimalstellen, signifikante Stellen oder aktuelle Anzeigevorgabe ab. |
| 442 | `TRUTH` | Contents-14 | `TRUTH` / `2:224` | 70 | 519 | `TRUTH` | KONTEXTUELLER_POCKET_TREFFER | Aktiviert einen Plottyp zur Darstellung wahrer/falscher Bedingungen. |
| 443 | `TSTR` | Contents-14 | `TSTR` / `2:29` | 72 | 520 | `TSTR` | KONTEXTUELLER_POCKET_TREFFER | Erzeugt aus Datums- und Uhrzeitwerten einen String einschließlich Wochentagsangabe. |
| 444 | `TVARS` | Contents-14 | `TVARS` / `2:37` | 72 | 521 | `TYARS` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Listet Variablen der angegebenen Objekttypen aus dem aktuellen Verzeichnis auf. |
| 445 | `TVM` | Contents-14 | `TVM` / `171:85` | 72 | 521 | `TVM` | KONTEXTUELLER_POCKET_TREFFER | Öffnet das Menü des Time-Value-of-Money-Finanzsolvers; löst nicht automatisch eine Unbekannte. |
| 446 | `TVMBEG` | Contents-14 | `TVMBEG` / `171:86` | 72 | 522 | `TYMBEG` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Aktiviert Zahlungszeitpunkte am Anfang einer Zahlungsperiode. |
| 447 | `TVMEND` | Contents-14 | `TVMEND` / `171:87` | 72 | 522 | `TYMEND` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Aktiviert Zahlungszeitpunkte am Ende einer Zahlungsperiode. |
| 448 | `TVMROOT` | Contents-14 | `TVMROOT` / `171:88` | 72 | 522 | `TWMROOT` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Berechnet die gesuchte Variable des TVM-Solvers. |
| 449 | `TYPE` | Contents-14 | `TYPE` / `2:166` | 72 | 523 | `TYPE` | KONTEXTUELLER_POCKET_TREFFER | Gibt die numerische Typkennung eines Objekts zurück. |
| 450 | `UBASE` | Contents-14 | `UBASE` / `2:14` | 72 | 524 | `LEASE` | OCR-FORM_ABWEICHEND_SCAN_OFFEN | Wandelt ein Einheitenobjekt in entsprechende SI-Basiseinheiten um. |

**Zählbilanz:** **50/50** individuelle AUR-TOC-Positionen, **50/50** unterschiedliche AUR-Namen, **50/50** direkte ROM-Namenszuordnungen, **50/50** kontextuelle unabhängige Pocket-Guide-Textbelege. Mehrere Texte sind OCR-beschädigt; die numerischen Fundseiten dienen dem Textabgleich und nicht als Originalscan-Abnahme. `THEN` hat im ROM-Inventar **mehrere XLIB-Kennungen** (`1792:1`, `1792:24`, `1792:26`) für unterschiedliche Kontrollkontexte, **nicht mehrere verschiedene Namen**.

## 3. Wichtige technische Befunde und Korrekturen

### Befehle, die leicht verwechselt werden

- **#402 `STIME`:** Der Pocket Guide bezeichnet ausdrücklich einen Timeout für **SRECV/WAIT**. Dies ist **nicht** die Systemuhr; dafür `TIME` (lesen) und `→TIME` (setzen) verwenden.
- **#407–410 `STO+`, `STO−`, `STO*`, `STO/`:** Veränderung eines **benannten Variableninhalts** und anschließende Speicherung. Die OCR verunstaltet sowohl das Minus- als auch das Divisionssymbol zu `ST0-`. Nicht aus dem Text einen Doppelbefehl ableiten. Bei der V-Prüfung die Operand-Reihenfolge beider Stackvarianten einzeln testen.
- **#411 `STOΣ`:** Speichert die Statistikdaten in `ΣDAT`, vom Pocket-Webtext als `STOZ` fehlinterpretiert. `Σ` darf nicht durch Z ersetzt werden.
- **#412 `STREAM`:** Verarbeitet Listen **iterativ mit vorherigem Ergebnis**, beginnend mit zwei Start-Listenelementen. Das ist keine beliebige parallelisierte Sequenzverarbeitung und von `SEQ` zu unterscheiden.
- **#413/414 `STR→`/`→STR`:** Text als RPL-Objekt lesen/interpretieren gegenüber Objekt in Textdarstellung umwandeln. `STR→` kann fehlerhaften Eingabetext treffen; Parser-Fehlerbehandlung später separat testen.
- **#417 `SVD` / #418 `SVL`:** Singulärwertzerlegung mit Faktoren/Matrizen versus bloße Liste der Singulärwerte. Die AUR-PDF-Seitenhilfe `18` zu `SVD` ist offensichtlich **auffällig**, aber ohne Originalbildkontrolle **nicht** überschreiben.
- **#420 `SYSEVAL`:** Historischer Betriebssystem-Einstiegspunkt. Für die SASD-Implementation **kein** beliebiger Host-Codeaufruf; strikt isolierter, kompatibilitätsbeschränkter Emulationspfad oder bewusst noch nicht implementiert.
- **#421 `%T`:** Berechnet den Prozentsatz, den ein Wert von einem anderen bildet. Nicht mit `%CH` (prozentuale Änderung) verwechseln.
- **#422 `→TAG`:** Erstellt ein getaggtes Objekt; die OCR zeigt `+TAG`.
- **#423 `TAIL`:** Entfernt das erste Listen-/Stringelement und liefert den **Rest**; nicht nur ein Texteditor-DELETE.
- **#427/434 `TDELTA`/`TINC`:** Temperaturdifferenz aus zwei Temperaturen gegenüber neuer Temperatur aus Anfangswert und Differenz. Aus der Temperatureinheit einen allgemeinen arithmetischen Differenzbefehl abzuleiten wäre falsch.
- **#428 `TEACH`:** Erzeugt ein `EXAMPLES`-Unterverzeichnis für Lernbeispiele; nicht einfach Daten auf den Stack legen.
- **#429 `TEXT`:** Rückkehr zur Text-/Stackdarstellung beim nächsten Display-Refresh; nicht gleich `PROMPT` oder `DISP`.
- **#430 `THEN`:** Ein syntaktisches Kontrollwort mit drei XLIB-IDs (`1792:1`, `1792:24`, `1792:26`) in der Baseline, je nach Kontrollstruktur. Eine AUR-TOC-Position bleibt eine Befehlsfamilie.
- **#431 `TICKS`:** Die historische Zeitbasis ist **8192 Ticks je Sekunde**; keine willkürliche Millisekunden- oder Nanosekunden-Hostzeit.
- **#432/433 `TIME`/`→TIME`:** Die Uhrzeit hat das alte `HH.MMSSs`-Format. Nicht mit Unix-Zeitstempeln oder dem Timeout `STIME` mischen.
- **#435 `TLINE`:** Toggelt einzelne Pixel entlang der Linie im `PICT`-Bild. Nicht bloß `LINE` gleichsetzen.
- **#436 `TMENU`:** Zeigt ein Menü **ohne Änderung der User-Custom-Menu-Variable `CST`**; kein Synonym für dauerhaftes `MENU`.
- **#437 `TOT`:** Summiert **jede Statistikdaten-Spalte** in `ΣDAT`, keine beliebige Summation der gesamten Matrix zu einem Einzelwert.
- **#438 `TRACE`:** Matrixspur ist eine numerische Operation und von der interaktiven **Plot-Nachführung** namens `TRACE` zu unterscheiden.
- **#439 `TRANSIO`:** Zeichenumsetzung der I/O-Übertragung, nicht `IR`-Schnittstellenwahl.
- **#441 `TRNC`:** Schneidet je nach Parameter auf Dezimalstellen oder signifikante Stellen ab; nicht `RND`-Runden. Exakte Parametergrenzen und Spezialwert zum aktuellen Displayformat sind V-Abnahmegegenstand.
- **#443 `TSTR`:** Formatiert **Datum und Uhrzeit einschließlich Wochentag**, nicht nur die Zeit.
- **#444 `TVARS`:** Nur Variablen der ausgewählten Typen **im aktuellen Verzeichnis**.
- **#445–448 `TVM`, `TVMBEG`, `TVMEND`, `TVMROOT`:** Menü öffnen, Zahlungsbeginnmodus, Zahlungsendemodus, **eine** gesuchte TVM-Variable tatsächlich lösen – vier unterschiedliche historische Funktionen.
- **#450 `UBASE`:** Einheitenobjekt in SI-Basiseinheiten umwandeln, nicht den bloßen Zahlenwert ohne Maßeinheit liefern.

## 4. Abnahme und Fortsetzung

- [x] 50 Quellindexpositionen mit gedrucktem Namen aus der AUR-Baseline übernommen.
- [x] 50 direkte ROM-Namen samt ihren XLIB-Kennungen, inklusive Mehrfach-XLIB bei `THEN`, abgeglichen.
- [x] 50 unabhängige Pocket-Guide-Textkontexte auf den gedruckten Seiten 68, 70 und 72 zugeordnet.
- [x] 50 funktionsbezogene deutsche Arbeitsbeschreibungen und differenzierte Quellenprobleme dokumentiert.
- [ ] AUR und Pocket Guide: visuelle Original-PDF-Prüfung sämtlicher relevanter Druckseiten und Glyphen.
- [ ] Stackdiagramme, Systemflags, numerische Genauigkeit, Ausnahmefälle und Gerätelaufzeit im Einzelverfahren vollständig prüfen.
- [ ] AUR-Hilfsseite `SVD` als ungewöhnlichen Index-Locator mit Originalscan validieren.

**A09-Namenscheckpoint:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE`; `ORIGINAL_SCAN_NOT_SIGNED_OFF`; `AUR_STACK_NOT_SIGNED_OFF`. **Nächster Block A10 (451–500: `UFACT` bis `→V3`).** Historischer Vollständigkeitsstatus weiterhin `HISTORICAL_COMPLETENESS_NOT_CERTIFIED` (nicht V1.0-blockierend).
