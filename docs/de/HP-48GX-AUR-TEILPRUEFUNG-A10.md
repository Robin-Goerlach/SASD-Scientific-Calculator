# HP 48GX – AUR-Teilprüfung A10 (Positionen 451–500)

**Stand:** 22.11.2026 · **Gerät:** serienmäßiger HP 48GX ohne Fremdkarten.  
**AUR-Indexbereich:** `UFACT` bis `≤` (50 Indexpositionen und 50 verschiedene Namen).  
**Abnahmeebene:** AUR-Quellindex, ROM-Namensinventar und unabhängig abgerufener Pocket-Guide-**Text**; weder Originalscan-Glyphen noch vollständige AUR-Stackdiagramme, Hardwareausführung, Flags und Fehlertypen sind freigegeben.

## 1. Quellen und Methode

1. Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Ausgabe (1994), Kapitel-3-Inhaltsverzeichnis `Contents-14` bis `Contents-16`. Verbindliche wortgetreue Quelltext-**Transkription**: [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json). Original: https://literature.hpcalc.org/community/hp48g-aur-en.pdf .
2. Bestandsindex der 48GX-ROM-Namen mit wirklichen XLIB-IDs: [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json). Sämtliche 50 Namen sind normiert direkt vorhanden, inklusive getrenntem Minus-Zeichen (`−` im AUR-Text, `-` im ROM-Namen) und mehreren XLIB-IDs bei `XROOT` und `+`. Das bestätigt Namenszuordnung, nicht die historische Laufzeitsemantik.
3. Chris Coffin und Thomas Dick, *The HP 48G/GX Pocket Guide*, Grapevine Publications 1996. Unabhängiger *Command Index*, gedruckte S. **72, 74 und 76**, zugängliche HTML-Texte:
   - https://www.manualslib.com/manual/3743173/Hp-48g.html?page=74 (gedruckt 72, `UFACT` bis `WAIT`);
   - https://www.manualslib.com/manual/3743173/Hp-48g.html?page=76 (gedruckt 74, `WHILE` bis `*`);
   - https://www.manualslib.com/manual/3743173/Hp-48g.html?page=78 (gedruckt 76, `/`, `^`, `<`, `≤`).
   Original-PDF: https://literature.hpcalc.org/community/hp48g-pg-en.pdf ; bibliographischer Datensatz: https://literature.hpcalc.org/items/1739 .
4. Hewlett-Packard, *HP 48G Series User's Guide* (historisch passend), Verteilungskommandos `UTPC`/`UTPF`/`UTPN`/`UTPT`, Archiv https://literature.hpcalc.org/official/hp48gseries-ug-en.pdf . Insbesondere `UTPN` verwendet die **Varianz**, nicht die Standardabweichung, als Eingabeparameter.

**Quellenkritik:** Die ManualsLib-Webtexte sind stark beschädigte OCR. Bei `→V2`/`→V3`, `V→`, `*W`, `ΣX`, `ΣX^2`, `ΣX*Y`, `ΣY`, `ΣY^2`, `≤` und weiteren Namen wurde die Position aus Alphabetfolge und Beschreibung abgeleitet, **nicht** eine verlässliche Originaldruck-Zeichenform festgestellt. Die direkte Pixel-/Bildseitenabnahme bleibt gesonderten O-Scan-Tranchen vorbehalten. Der Pocket-Text verwendet für `XROOT` eine OCR-Variante `#RO0T`, in der die Null wie O aussieht. Es wird kein neues Kommando daraus.

## 2. Kompletter positionsweiser A10-Abgleich

| AUR # | AUR-Quelltextname | AUR-Index | ROM-Name / XLIB | Pocket-Druckseite | Pocket-OCR-Kandidat | Prüfstufe | Deutsche Arbeitsbeschreibung |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 451 | `UFACT` | Contents-14 | `UFACT` / `2:15` | 72 | `UFACT` | TEXT-/KONTEXTABGLEICH | Stellt ein Einheitenobjekt so um, dass die Einheit des zweiten Arguments als Faktor erscheint; keine bloße numerische Faktorisierung. |
| 452 | `→UNIT` | Contents-14 | `→UNIT` / `2:13` | 72 | `+INIT` | OCR-ROHFORM / GLYPHE OFFEN | Verbindet einen Zahlenwert mit dem Einheitenteil eines anderen Einheitenobjekts. |
| 453 | `UNTIL` | Contents-14 | `UNTIL` / `1792:8` | 72 | `| (OCR unleserlich)` | OCR-ROHFORM / GLYPHE OFFEN | Prüfklausel am Ende einer DO…UNTIL…END-Schleife. |
| 454 | `UPDIR` | Contents-14 | `UPDIR` / `2:35` | 72 | `IUIFOIE` | OCR-ROHFORM / GLYPHE OFFEN | Wechselt zum unmittelbar übergeordneten Verzeichnis. |
| 455 | `UTPC` | Contents-14 | `UTPC` / `2:308` | 72 | `UTPC` | TEXT-/KONTEXTABGLEICH | Obere Verteilungswahrscheinlichkeit P(χ² > x) für eine Chi-Quadrat-Verteilung mit n Freiheitsgraden. |
| 456 | `UTPF` | Contents-14 | `UTPF` / `2:310` | 72 | `UTPF` | TEXT-/KONTEXTABGLEICH | Obere Verteilungswahrscheinlichkeit P(F > x) mit Zähler- und Nennerfreiheitsgraden. |
| 457 | `UTPN` | Contents-14 | `UTPN` / `2:309` | 72 | `UTPN` | TEXT-/KONTEXTABGLEICH | Obere Verteilungswahrscheinlichkeit P(X > x) der Normalverteilung bei vorgegebenem Mittelwert und Varianz. |
| 458 | `UTPT` | Contents-15 | `UTPT` / `2:311` | 72 | `UTPT` | TEXT-/KONTEXTABGLEICH | Obere Verteilungswahrscheinlichkeit P(T > x) einer Student-t-Verteilung mit n Freiheitsgraden. |
| 459 | `UVAL` | Contents-15 | `UVAL` / `2:12` | 72 | `VAL` | OCR-ROHFORM / GLYPHE OFFEN | Liefert nur den numerischen Anteil eines Einheitenobjekts. |
| 460 | `VAR` | Contents-15 | `VAR` / `2:301` | 72 | `VPR` | OCR-ROHFORM / GLYPHE OFFEN | Berechnet die Stichprobenvarianz je Spalte der Statistikdaten in ΣDAT; nicht das VARS-Menü. |
| 461 | `VARS` | Contents-15 | `VARS` / `2:36` | 72 | `YARS` | OCR-ROHFORM / GLYPHE OFFEN | Gibt eine Liste der Variablen des aktuellen Verzeichnisses zurück. |
| 462 | `VERSION` | Contents-15 | `VERSION` / `171:15` | 72 | `VERSIOM` | OCR-ROHFORM / GLYPHE OFFEN | Gibt Firmwareversionsnummer und historische Copyrightmeldung aus. |
| 463 | `VTYPE` | Contents-15 | `VTYPE` / `2:167` | 72 | `YTYPE` | OCR-ROHFORM / GLYPHE OFFEN | Liefert den Objekttyp des Inhalts einer benannten Variablen. |
| 464 | `→V2` | Contents-15 | `→V2` / `2:181` | 72 | `WE` | OCR-ROHFORM / GLYPHE OFFEN | Konstruiert aus zwei Komponenten ein komplexes Objekt oder einen 2D-Vektor im aktuellen Koordinatenmodus. |
| 465 | `→V3` | Contents-15 | `→V3` / `2:182` | 72 | `+V3` | OCR-ROHFORM / GLYPHE OFFEN | Konstruiert aus drei Komponenten einen 3D-Vektor im aktuellen kartesischen, zylindrischen oder sphärischen Koordinatenmodus. |
| 466 | `V→` | Contents-15 | `V→` / `2:180` | 72 | `Y+` | OCR-ROHFORM / GLYPHE OFFEN | Zerlegt Vektor oder komplexes Objekt in seine Komponenten; die Anzeige hängt ggf. vom Koordinatenmodus ab. |
| 467 | `*W` | Contents-15 | `*W` / `2:190` | 72 | `#|` | OCR-ROHFORM / GLYPHE OFFEN | Vergrößert die horizontale Plot-Skalierung; genaue historische Glyphenform nur mit Originalscan bestätigen. |
| 468 | `WAIT` | Contents-15 | `WAIT` / `2:55` | 72 | `WARIT` | OCR-ROHFORM / GLYPHE OFFEN | Unterbricht Programmablauf für eine angegebene Zeit oder bis zum Tastendruck. |
| 469 | `WHILE` | Contents-15 | `WHILE` / `1792:5` | 74 | `WHILE` | TEXT-/KONTEXTABGLEICH | Leitet den Testteil einer WHILE…REPEAT…END-Schleife ein. |
| 470 | `WIREFRAME` | Contents-15 | `WIREFRAME` / `171:8` | 74 | `WIREFRAME` | TEXT-/KONTEXTABGLEICH | Wählt den 3D-Drahtgitter-Plottyp. |
| 471 | `WSLOG` | Contents-15 | `WSLOG` / `2:19` | 74 | `WSLOG` | TEXT-/KONTEXTABGLEICH | Gibt Strings zu den letzten vier Warmstarts mit Grund-Kennung und Datum/Uhrzeit zurück. |
| 472 | `ΣX` | Contents-15 | `ΣX` / `2:291` | 74 | `Zh` | OCR-ROHFORM / GLYPHE OFFEN | Summe der Werte der als unabhängig ausgewählten ΣDAT-Spalte. |
| 473 | `ΣX^2` | Contents-15 | `ΣX^2` / `2:293` | 74 | `SH'*Z` | OCR-ROHFORM / GLYPHE OFFEN | Summe der quadrierten Werte der unabhängigen ΣDAT-Spalte. |
| 474 | `XCOL` | Contents-15 | `XCOL` / `2:306` | 74 | `A0l` | OCR-ROHFORM / GLYPHE OFFEN | Setzt oder liefert je nach Verwendungsform den Spaltenbezug der unabhängigen Statistikvariablen. |
| 475 | `XMIT` | Contents-15 | `XMIT` / `2:359` | 74 | `XMIT` | TEXT-/KONTEXTABGLEICH | Sendet einen Text über die serielle Schnittstelle ohne Kermit; gibt ungesendeten Rest und Erfolgsstatus zurück. |
| 476 | `XOR` | Contents-15 | `XOR` / `2:232` | 74 | `#0R` | OCR-ROHFORM / GLYPHE OFFEN | Berechnet je nach Argumenttyp logisches oder bitweises exklusives ODER. |
| 477 | `XPON` | Contents-15 | `XPON` / `2:105` | 74 | `#PON` | OCR-ROHFORM / GLYPHE OFFEN | Ermittelt den Dezimalexponenten einer Zahl. |
| 478 | `XRECV` | Contents-15 | `XRECV` / `171:95` | 74 | `HRECY` | OCR-ROHFORM / GLYPHE OFFEN | Empfängt eine Datei via XModem und speichert sie. |
| 479 | `XRNG` | Contents-15 | `XRNG` / `2:218` | 74 | `H#RNG` | OCR-ROHFORM / GLYPHE OFFEN | Legt die x-Achsengrenzen des Plotbereichs in PPAR fest. |
| 480 | `XROOT` | Contents-15 | `XROOT` / `2:74, 2:75` | 74 | `#RO0T` | OCR-ROHFORM / GLYPHE OFFEN | Berechnet die x-te Wurzel einer Zahl; zwei XLIB-Kennungen im ROM zum gleichen Namen. |
| 481 | `XSEND` | Contents-15 | `XSEND` / `171:94` | 74 | `HSEND` | OCR-ROHFORM / GLYPHE OFFEN | Sendet eine Objektkopie über XModem. |
| 482 | `XVOL` | Contents-15 | `XVOL` / `171:0` | 74 | `YOl` | OCR-ROHFORM / GLYPHE OFFEN | Setzt die Breite des 3D-Betrachtungsvolumens in VPAR. |
| 483 | `XXRNG` | Contents-15 | `XXRNG` / `171:3` | 74 | `RARNG` | OCR-ROHFORM / GLYPHE OFFEN | Legt den x-Bereich der Eingabeebene für 3D-Plots in VPAR fest. |
| 484 | `ΣX*Y` | Contents-15 | `ΣX*Y` / `2:295` | 74 | `zax` | OCR-ROHFORM / GLYPHE OFFEN | Summiert Produkte aus unabhängiger und abhängiger ΣDAT-Spalte. |
| 485 | `ΣY` | Contents-15 | `ΣY` / `2:292` | 74 | `(unleserlich)` | OCR-ROHFORM / GLYPHE OFFEN | Summe der Werte der abhängigen ΣDAT-Spalte. |
| 486 | `ΣY^2` | Contents-15 | `ΣY^2` / `2:294` | 74 | `T2` | OCR-ROHFORM / GLYPHE OFFEN | Summe der quadrierten Werte der abhängigen ΣDAT-Spalte. |
| 487 | `YCOL` | Contents-15 | `YCOL` / `2:307` | 74 | `VCOL` | OCR-ROHFORM / GLYPHE OFFEN | Setzt oder liefert den Spaltenbezug der abhängigen Statistikvariablen. |
| 488 | `YRNG` | Contents-15 | `YRNG` / `2:219` | 74 | `YENG` | OCR-ROHFORM / GLYPHE OFFEN | Legt die y-Achsengrenzen des Plotbereichs in PPAR fest. |
| 489 | `YSLICE` | Contents-15 | `YSLICE` / `171:11` | 74 | `¥SLICE` | OCR-ROHFORM / GLYPHE OFFEN | Aktiviert den 3D-Plottyp Y-Slice. |
| 490 | `YVOL` | Contents-15 | `YVOL` / `171:1` | 74 | `WL` | OCR-ROHFORM / GLYPHE OFFEN | Setzt die Tiefe des 3D-Betrachtungsvolumens in VPAR. |
| 491 | `YYRNG` | Contents-15 | `YYRNG` / `171:4` | 74 | `YYRNG` | TEXT-/KONTEXTABGLEICH | Legt den y-Bereich der Eingabeebene für 3D-Plots in VPAR fest. |
| 492 | `ZFACTOR` | Contents-15 | `ZFACTOR` / `171:118` | 74 | `ZFACTOR` | TEXT-/KONTEXTABGLEICH | Berechnet den Realgas-Kompressibilitätsfaktor von Kohlenwasserstoffgas bei reduzierter Temperatur und reduziertem Druck. |
| 493 | `ZVOL` | Contents-15 | `ZVOL` / `171:2` | 74 | `2L` | OCR-ROHFORM / GLYPHE OFFEN | Setzt die Höhe des 3D-Betrachtungsvolumens in VPAR. |
| 494 | `+` | Contents-15 | `+` / `2:68, 2:69` | 74 | `+` | TEXT-/KONTEXTABGLEICH | Addiert zwei Objekte; unterschiedliche Objekttypkombinationen nach AUR später separat spezifizieren. |
| 495 | `−` | Contents-15 | `-` / `2:70` | 74 | `−` | TEXT-/KONTEXTABGLEICH | Subtrahiert das zweite Stackargument vom ersten (x−y entsprechend Dokumentationspositionen); Vorzeichen und Typvarianten später prüfen. |
| 496 | `*` | Contents-15 | `*` / `2:71` | 74 | `*` | TEXT-/KONTEXTABGLEICH | Multipliziert zwei Objekte unter Berücksichtigung ihrer historischen Typregeln. |
| 497 | `/` | Contents-15 | `/` / `2:72` | 76 | `#` | OCR-ROHFORM / GLYPHE OFFEN | Dividiert ein Objekt durch ein anderes; Reihenfolge, Symbolik und Nullteilung noch an AUR prüfen. |
| 498 | `^` | Contents-15 | `^` / `2:73` | 76 | `*` | OCR-ROHFORM / GLYPHE OFFEN | Potenziert das Basisobjekt mit dem Exponenten; historisches Reell-/Komplex-/Symbolverhalten später prüfen. |
| 499 | `<` | Contents-16 | `<` / `2:235` | 76 | `<` | TEXT-/KONTEXTABGLEICH | Gibt die Aussage zurück, ob das erste Argument kleiner als das zweite ist. |
| 500 | `≤` | Contents-16 | `≤` / `2:237` | 76 | `< (zweite OCR-Zeile)` | OCR-ROHFORM / GLYPHE OFFEN | Gibt die Aussage zurück, ob das erste Argument kleiner oder gleich dem zweiten ist. |

### Namens- und Abdeckungsbilanz

- **50/50** original nummerierte AUR-Quellpositionen mit 50 verschiedenen Namen dokumentiert.
- **50/50** normierte ROM-Namen direkt nachgewiesen, mit XLIB-Kennungen aus der Baseline. Zwei Mehrfach-XLIB-Namen: `XROOT` (`2:74`, `2:75`) sowie `+` (`2:68`, `2:69`).
- **50/50** Pocket-Guide-Command-Index-Positionen kontextuell gegen den unabhängigen **OCR-Text** der gedruckten S. 72/74/76 abgebildet. Dies schließt OCR-Rohzeichen ein, die nicht dem tatsächlichen Kommando entsprechen; Originalglyphen **ausdrücklich nicht** bestätigt.
- **0** AUR-Kommandos in dieser Tranche vollständig typ-, stack-, flag-, genauigkeits- und fehlergeprüft.

## 3. Technische Erkenntnisse und offene Prüffälle

- **#451 `UFACT`:** Repräsentiert das gegebene Einheitenobjekt mit einem **bestimmten Einheitenfaktor aus dem zweiten Argument**. Die bisherige Kurzformulierung „Einheitenausdruck faktorisieren“ hatte den zweiten Parameter verschwiegen. Kein Synonym zu `UBASE`.
- **#452 `→UNIT`:** Nimmt einen Zahlenwert und den **Einheitenteil eines weiteren Objekts**; führt nicht blind Stringverkettung durch.
- **#455–458 `UTPC`/`UTPF`/`UTPN`/`UTPT`:** Obere Verteilungsschwanzwahrscheinlichkeiten für χ², F, Normal und t. Bei `UTPF` zwei Freiheitsgrade, bei `UTPN` Mittelwert und **Varianz**. Der User's Guide beschreibt die Stackparameter; deren Testvektoren bleiben noch auszuarbeiten.
- **#460 `VAR` gegenüber #461 `VARS`:** Ersterer ist **Stichprobenvarianz je ΣDAT-Spalte**, letzterer ist eine **Variablennamensliste im aktuellen Verzeichnis**. Namen nicht durch Pluralisierungslogik behandeln.
- **#462 `VERSION`:** Der Pocket Guide nennt Firmwareversion und HP-Copyright-Text. Die eigene Version der SASD-App nicht als historische 48GX-ROM-Version ausgeben; ein Kompatibilitätsprofil ist nötig.
- **#464–466 `→V2`/`→V3`/`V→`:** Zusammenbau und Zerlegung im **aktuellen Koordinatenmodus**, keine starren Host-Vektorkoordinaten; der Pocket-Text führt `→V2` als möglichen komplexen Wert.
- **#467 `*W`:** Vergrößert horizontale Plotskalierung. Die Pocket-OCR stellt das Zeichen vor W als `#|` dar; **historische Glyphe aus Originalscan ungeklärt**, AUR-Rohtext unverändert.
- **#468 `WAIT`:** Zeitbegrenzter Wartezustand oder Tastendruck; darf die iPhone-Anwendung nicht ungeprüft auf dem UI-Hauptthread blockieren.
- **#471 `WSLOG`:** Historisches Warmstartprotokoll **der letzten vier Ereignisse** mit Ursache und Zeit, keine allgemeine Host-Systemlogdatei.
- **#472–473 und #484–486:** Statistiksumme `ΣX`, `ΣX^2`, `ΣX*Y`, `ΣY`, `ΣY^2` beziehen sich auf ausgewählte Spalten in `ΣDAT`; OCR setzt Σ häufig als Z um. Keine numerische Auswertung der AUR-Glyphen selbst.
- **#475 `XMIT`:** Serieller Byte-/Textversand **ohne Kermit**, gibt den nicht übertragenen Rest sowie einen Erfolgscode zurück. Anders als `XSEND` (XModem) und `SEND` (Kermit).
- **#477 `XPON`:** Dezimalexponent, nicht die Exponentialfunktion `EXP`.
- **#478/#481 `XRECV`/`XSEND`:** XModem-Dateiprotokoll, in einer historischen iOS-App nur über eine ausdrücklich konfigurierte I/O-Kompatibilitätsschicht.
- **#479/#488 `XRNG`/`YRNG`:** Grenzen der dargestellten x-/y-Achse in `PPAR`; **#483/#491 `XXRNG`/`YYRNG`** betreffen dagegen den x-/y-Eingabebereich der 3D-Fläche in `VPAR`. `XVOL`/`YVOL`/`ZVOL` geben Breite/Tiefe/Höhe des Betrachtungsvolumens an.
- **#480 `XROOT`:** Historische Baseline belegt **zwei** XLIB-Kennungen zu einem Namen. Die genaue Verteilung nach Argumenttypen und Objektkontexten muss auf AUR-Einzelseiten nachvollzogen werden; nicht zwei Befehle zählen.
- **#492 `ZFACTOR`:** Das ist der **Kompressibilitätsfaktor eines realen Kohlenwasserstoffgases** auf Basis reduzierter Temperatur/Druckwerte, kein willkürlicher Plot-z-Zoom.
- **#494–500 `+`, `−`, `*`, `/`, `^`, `<`, `≤`:** Operatornamen sind echte AUR-/ROM-Katalogpositionen. Einige unterstützen unterschiedliche Objekttypen, Rundungen und symbolische Varianten; das dokumentiert der Pocket Guide nur im Überblick. **Nicht** aus der Liste allein allgemeine IEEE-754-/Host-C++-Operatorsemantik ableiten.
- **#499/#500 `<`/`≤`:** Vergleichsoperationen, keine bloße Darstellung von Relationssymbolen; die Pocket-Web-OCR schreibt an beiden Stellen `<`.

## 4. Historische Abnahmegrenze und Übergabe

- [x] 50 Quellpositionen, 50 unterschiedliche AUR-Namen, 50 ROM-Namens-/XLIB-Zuordnungen dokumentiert.
- [x] 50 getrennte Pocket-Guide-Indextextbelege inkl. Druckseiten und OCR-Ambiguitäten dokumentiert.
- [x] 50 deutsche Arbeitsbeschreibungen sowie besonders kritische Typ-/Modellunterscheidungen ergänzt.
- [ ] Historische Originalscan-Ansicht für AUR/Pocket Guide, Glyphen- und Seitenzuordnung visuell abnehmen.
- [ ] Vollständige AUR-Stackdiagramme mit Objekttypen, Flags, numerischen Grenzwerten, Fehlerfällen und Hardwaregegenprobe.

**A10-Checkpoint:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE`, `SCAN_PENDING`, `STACK_AND_HARDWARE_PENDING`. **Nächster AUR-Namensblock: A11 (501–517; `>` bis `→` – Start/Ende am gespeicherten Quellindex exakt neu prüfen).** Der historische Gesamtkatalog ist noch **nicht** vollständig abgenommen, kein Blocker für iPhone-V1.0.
