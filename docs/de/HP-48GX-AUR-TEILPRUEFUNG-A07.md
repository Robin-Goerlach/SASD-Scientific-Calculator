# HP 48GX – AUR-Teilprüfung A07 (Befehle 301–350)

**Stand:** 22.11.2026 · **Modell:** serienmäßiger HP 48GX ohne Fremdkarten.  
**Umfang:** AUR-Command-Reference-Inhaltsverzeichnis, Positionen 301–350: `PVIEW` bis `RR`.  
**Abnahmeebene:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE` – Abgleich von **50 AUR-Quelltextpositionen** mit **50 verschiedenen ROM-Namen** und **50 kontextuell nachgewiesenen Pocket-Guide-Indexpositionen**. **Kein** Originalscan-PASS, kein AUR-Stackdiagramm-/Hardware-PASS.

## 1. Prüfbasis und Quellenabgrenzung

- Hewlett-Packard, *HP 48G Series Advanced User's Reference*, vierte Ausgabe Dezember 1994, Kapitel 3; die bereits im Repository eingefrorenen Quellindexpositionen `Contents-11` und `Contents-12` sind in [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json) erhalten. Original-PDF: https://literature.hpcalc.org/community/hp48g-aur-en.pdf .
- Gerätebezogene ROM-Namens-/XLIB-Baseline: [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json). XLIB-Treffer belegen den **Namen**, keine typvollständige Ausführbarkeit oder identische Rundung.
- Chris Coffin und Thomas Dick, *The HP 48G/GX Pocket Guide* (Grapevine Publications, April 1996), **Command Index gedruckte Seiten 60, 62 und 64**, HTML-Reproduktionen: https://www.manualslib.com/manual/3743173/Hp-48g.html?page=62 , https://www.manualslib.com/manual/3743173/Hp-48g.html?page=64 und https://www.manualslib.com/manual/3743173/Hp-48g.html?page=66 . Verlags-/Autorennachweis: https://literature.hpcalc.org/items/1739 .
- Die webzugänglichen HTML-Seiten sind **OCR-Text**, keine verlustfreien Originalabbildungen. Gedruckte PDF-Originalglyphen, insbesondere Pfeile, griechische Buchstaben, Minuszeichen und Spezialzeichen, sind **nicht visuell abgenommen**. Die abweichenden OCR-Kandidaten in der Tabelle dürfen nicht in eigenständige ROM-Namen umgedeutet werden.

## 2. Positionsvollständiger Abgleich

| AUR # | AUR-Quelltextname | AUR-Indexseite | ROM-Name / XLIB | Pocket-Druckseite | Pocket-Web-OCR-Rohform | Namensstatus | Eigenständige deutsche Arbeitsbeschreibung |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 301 | `PVIEW` | Contents-11 | `PVIEW` / `2:202` | 60 | `PVIEW` | Text-Namensstelle zugeordnet | Zeigt PICT mit einer angegebenen Benutzerkoordinate in der linken oberen Displayecke. |
| 302 | `PWRFIT` | Contents-11 | `PWRFIT` / `2:322` | 60 | `PURFIT` | OCR-/Glyphenform offen; kontextuell zugeordnet | Wählt das Potenzmodell für die Regressionsanpassung aus. |
| 303 | `PX→C` | Contents-11 | `PX→C` / `2:198` | 62 | `Pi=+C` | OCR-/Glyphenform offen; kontextuell zugeordnet | Wandelt Bildpunktkoordinaten des PICT in Benutzerkoordinaten um. |
| 304 | `→Q` | Contents-11 | `→Q` / `2:263` | 62 | `+)` | OCR-/Glyphenform offen; kontextuell zugeordnet | Sucht eine rationale Darstellung des gegebenen Ausdrucks bzw. Zahlenwertes. |
| 305 | `→Qπ` | Contents-11 | `→Qπ` / `2:264` | 62 | `0T` | OCR-/Glyphenform offen; kontextuell zugeordnet | Rationalisiert einen Ausdruck mit einem π-Faktor; genaue Kriterien der Formwahl separat prüfen. |
| 306 | `QR` | Contents-11 | `QR` / `171:60` | 62 | `QR` | Text-Namensstelle zugeordnet | Zerlegt eine Matrix A unter Berücksichtigung der Permutation P in Q und R (A·P = Q·R). |
| 307 | `QUAD` | Contents-11 | `QUAD` / `2:337` | 62 | `QUARD` | OCR-/Glyphenform offen; kontextuell zugeordnet | Löst symbolisch nach einer Variablen, nachdem der Ausdruck mittels Taylorentwicklung zweiten Grades in eine quadratische Form gebracht wurde. |
| 308 | `QUOTE` | Contents-11 | `QUOTE` / `2:257` | 62 | `RIOTE` | OCR-/Glyphenform offen; kontextuell zugeordnet | Gibt einen Ausdruck ohne dessen unmittelbare Auswertung weiter. |
| 309 | `RAD` | Contents-11 | `RAD` / `2:136` | 62 | `RAD` | Text-Namensstelle zugeordnet | Wählt Bogenmaß als Winkelmodus. |
| 310 | `RAND` | Contents-11 | `RAND` / `2:127` | 62 | `RAND` | Text-Namensstelle zugeordnet | Erzeugt eine Pseudozufallszahl aus dem eingestellten Generatorzustand. |
| 311 | `RANK` | Contents-11 | `RANK` / `171:53` | 62 | `RANK` | Text-Namensstelle zugeordnet | Berechnet den Rang einer Matrix. |
| 312 | `RANM` | Contents-11 | `RANM` / `171:64` | 62 | `RANM` | Text-Namensstelle zugeordnet | Erzeugt eine Zufallsmatrix mit vorgegebenen Dimensionen. |
| 313 | `RATIO` | Contents-11 | `RATIO` / `2:268` | 62 | `RATIO` | Text-Namensstelle zugeordnet | Repräsentiert symbolisch den Divisionsoperator in algebraischen Ausdrücken. |
| 314 | `RCEQ` | Contents-11 | `RCEQ` / `2:249` | 62 | `RCEQ` | Text-Namensstelle zugeordnet | Ruft den Inhalt der reservierten Gleichungsvariable EQ ab. |
| 315 | `RCI` | Contents-11 | `RCI` / `171:77` | 62 | `RCI` | Text-Namensstelle zugeordnet | Multipliziert eine ausgewählte Zeile eines Arrays mit einem Faktor; Vektoren werden wie Spaltenmatrizen behandelt. |
| 316 | `RCIJ` | Contents-11 | `RCIJ` / `171:78` | 62 | `RCIJ` | Text-Namensstelle zugeordnet | Multipliziert die Zeile i eines Arrays mit einem Faktor und addiert das Ergebnis zu Zeile j. |
| 317 | `RCL` | Contents-11 | `RCL` / `2:340` | 62 | `RCL` | Text-Namensstelle zugeordnet | Legt das Objekt einer benannten Variablen auf den Stack. |
| 318 | `RCLALARM` | Contents-11 | `RCLALARM` / `2:26` | 62 | `RCLALARM` | Text-Namensstelle zugeordnet | Ruft einen Alarm einschließlich auszuführender Aktion und Zeit-/Intervallangaben ab. |
| 319 | `RCLF` | Contents-11 | `RCLF` / `2:150` | 62 | `RCLF` | Text-Namensstelle zugeordnet | Liefert den gespeicherten Flagsatz. |
| 320 | `RCLKEYS` | Contents-11 | `RCLKEYS` / `2:382` | 62 | `RCLKEYS` | Text-Namensstelle zugeordnet | Liest die benutzerdefinierten Tastenbelegungen. |
| 321 | `RCLMENU` | Contents-11 | `RCLMENU` / `2:349` | 62 | `RCLMENU` | Text-Namensstelle zugeordnet | Gibt die Nummer bzw. Kennung des aktuellen Menüs zurück. |
| 322 | `RCLΣ` | Contents-11 | `RCLΣ` / `2:285` | 62 | `RCLE` | OCR-/Glyphenform offen; kontextuell zugeordnet | Lädt den Statistikdatensatz ΣDAT auf den Stack. |
| 323 | `RCWS` | Contents-11 | `RCWS` / `2:149` | 62 | `RCWS` | Text-Namensstelle zugeordnet | Gibt die aktuell eingestellte Wortlänge binärer Ganzzahlen zurück. |
| 324 | `RDM` | Contents-11 | `RDM` / `2:172` | 62 | `ROM` | OCR-/Glyphenform offen; kontextuell zugeordnet | Redimensioniert ein Array; bei benannter Matrix erfolgt eine Änderung an der Variable statt Stackresultat. |
| 325 | `RDZ` | Contents-11 | `RDZ` / `2:128` | 62 | `ROZ` | OCR-/Glyphenform offen; kontextuell zugeordnet | Setzt den Startzustand (Seed) des Pseudozufallsgenerators für RAND. |
| 326 | `RE` | Contents-11 | `RE` / `2:154` | 62 | `RE` | Text-Namensstelle zugeordnet | Liefert den Realteil einer komplexen Zahl. |
| 327 | `RECN` | Contents-11 | `RECN` / `2:365` | 62 | `RECN` | Text-Namensstelle zugeordnet | Empfängt eine Kermit-Datei und vergibt bzw. übernimmt beim Empfang einen Namen. |
| 328 | `RECT` | Contents-11 | `RECT` / `171:19` | 62 | `RECT` | Text-Namensstelle zugeordnet | Wählt die kartesische Koordinatendarstellung. |
| 329 | `RECV` | Contents-11 | `RECV` / `2:366` | 62 | `RECY` | OCR-/Glyphenform offen; kontextuell zugeordnet | Empfängt eine über Kermit bereits benannte Datei bzw. ein entsprechend benanntes Objekt. |
| 330 | `REPEAT` | Contents-11 | `REPEAT` / `1792:6` | 62 | `REPEAT` | Text-Namensstelle zugeordnet | Markiert den Wiederholungsteil einer WHILE-REPEAT-END-Struktur in User-RPL. |
| 331 | `REPL` | Contents-11 | `REPL` / `2:157` | 62 | `REPL` | Text-Namensstelle zugeordnet | Ersetzt einen Teil eines Strings, Arrays, einer Liste oder eines GROB ab einer bestimmten Position. |
| 332 | `RES` | Contents-11 | `RES` / `2:188` | 62 | `RES` | Text-Namensstelle zugeordnet | Legt die Plot-Auflösung fest. |
| 333 | `RESTORE` | Contents-11 | `RESTORE` / `2:353` | 62 | `RESTORE` | Text-Namensstelle zugeordnet | Stellt ein gesichertes HOME-Verzeichnis aus einem Backupobjekt wieder her. |
| 334 | `REVLIST` | Contents-11 | `REVLIST` / `171:109` | 62 | `REVLIST` | Text-Namensstelle zugeordnet | Kehrt die Reihenfolge von Listenelementen um. |
| 335 | `RKF` | Contents-12 | `RKF` / `171:43` | 62 | `RKF` | Text-Namensstelle zugeordnet | Berechnet die Lösung eines Differentialgleichungs-Anfangswertproblems mit Runge-Kutta-Fehlberg (4/5). |
| 336 | `RKFERR` | Contents-12 | `RKFERR` / `171:45` | 64 | `RKFERR` | Text-Namensstelle zugeordnet | Schätzt den absoluten Fehler eines Runge-Kutta-Fehlberg-Schritts. |
| 337 | `RKFSTEP` | Contents-12 | `RKFSTEP` / `171:44` | 64 | `REFSTER` | OCR-/Glyphenform offen; kontextuell zugeordnet | Berechnet einen nächsten Runge-Kutta-Fehlberg-Schritt unter vorgegebenen Parametern und Toleranz. |
| 338 | `RL` | Contents-12 | `RL` / `2:1` | 64 | `RL` | Text-Namensstelle zugeordnet | Rotiert ein binäres Wort um ein Bit nach links. |
| 339 | `RLB` | Contents-12 | `RLB` / `2:2` | 64 | `FLE` | OCR-/Glyphenform offen; kontextuell zugeordnet | Rotiert ein binäres Wort um ein Byte (acht Bits) nach links. |
| 340 | `RND` | Contents-12 | `RND` / `2:108` | 64 | `RMO` | OCR-/Glyphenform offen; kontextuell zugeordnet | Rundet nach vorgegebener Dezimalstellen- oder signifikanter Stellenzahl bzw. Anzeigeformat. |
| 341 | `RNRM` | Contents-12 | `RNRM` / `2:118` | 64 | `RHEM` | OCR-/Glyphenform offen; kontextuell zugeordnet | Berechnet die Zeilennorm eines Arrays. |
| 342 | `ROLL` | Contents-12 | `ROLL` / `2:280` | 64 | `ROLL` | Text-Namensstelle zugeordnet | Rotiert die obersten n Stackobjekte um eine Position nach oben, nachdem n verbraucht wurde. |
| 343 | `ROLLD` | Contents-12 | `ROLLD` / `2:281` | 64 | `FOLLD` | OCR-/Glyphenform offen; kontextuell zugeordnet | Rotiert die obersten n Stackobjekte um eine Position nach unten, nachdem n verbraucht wurde. |
| 344 | `ROOT` | Contents-12 | `ROOT` / `2:251` | 64 | `ROOT` | Text-Namensstelle zugeordnet | Sucht numerisch eine Nullstelle, ausgehend von einem oder mehreren Startwerten. |
| 345 | `ROT` | Contents-12 | `ROT` / `2:274` | 64 | `FOT` | OCR-/Glyphenform offen; kontextuell zugeordnet | Rotiert die obersten drei Stackobjekte. |
| 346 | `→ROW` | Contents-12 | `→ROW` / `171:65` | 64 | `+ROW` | OCR-/Glyphenform offen; kontextuell zugeordnet | Zerlegt ein Array in einzelne Zeilen und gibt zusätzlich die Anzahl der Zeilen zurück. |
| 347 | `ROW+` | Contents-12 | `ROW+` / `171:72` | 64 | `ROk+` | OCR-/Glyphenform offen; kontextuell zugeordnet | Fügt eine Zeile an einer angegebenen Stelle eines Arrays ein. |
| 348 | `ROW−` | Contents-12 | `ROW-` / `171:71` | 64 | `ROW-` | OCR-/Glyphenform offen; kontextuell zugeordnet | Entfernt eine ausgewählte Zeile aus einem Array und gibt das reduzierte Array und die entfernte Zeile zurück. |
| 349 | `ROW→` | Contents-12 | `ROW→` / `171:66` | 64 | `ROk` | OCR-/Glyphenform offen; kontextuell zugeordnet | Erzeugt ein Array aus gegebenen Zeilenobjekten und ihrer Anzahl. |
| 350 | `RR` | Contents-12 | `RR` / `2:3` | 64 | `RR` | Text-Namensstelle zugeordnet | Rotiert ein binäres Wort um ein Bit nach rechts. |

**Ergebnis:** 50/50 positionsbezogene AUR-Namen, 50/50 unterschiedliche ROM-Namen und 50/50 unabhängige Pocket-Guide-Textzuordnungen, jedoch unterschiedliche **Güte der Namen-Glyphen**. Die OCR-Version ist nicht originalgetreu genug für eine Freigabe als bestätigter Druck. Die ROM-Kennungen sind den gespeicherten Baselines entnommen; sie sind keine neu erfundenen System-RPL-Adressen.

## 3. Inhaltliche Unterschiede und offene Prüfpunkte

### Besonderheiten aus dem Pocket Guide

- **#301 `PVIEW`:** Stellt das vorhandene `PICT`-Grafikobjekt so dar, dass die angegebene Benutzerkoordinate oben links erscheint. Nicht bloß allgemeine „Grafikbereich anzeigen“-Aktion.
- **#303 `PX→C`:** Bildpunktkoordinaten → Benutzerkoordinaten, nicht umgekehrt; im Pocket-Text stark verstümmelter Namenskandidat `Pi=+C`.
- **#304/305 `→Q`/`→Qπ`:** Rationale Umformung ohne bzw. mit π-Faktor. In der OCR erscheinen Symbole als `+)` und `0T`. Die Entscheidungskriterien für exakte rational-symbolische Ergebnisse bleiben der Einzelseitenprüfung vorbehalten.
- **#306 `QR`:** Der Pocket Guide beschreibt `A·P = Q·R` einschließlich einer Permutationsmatrix `P`; nur „QR-Faktorisierung“ lässt dieses dritte Ausgabeelement offen. **Keine** Implementierung als beliebige Zweimatrizen-Variante ohne Stackbeleg freigeben.
- **#307 `QUAD`:** Löst einen algebraischen Ausdruck nach einer Variablen durch **Taylor-Approximation zweiter Ordnung** zu einer quadratischen Gleichung; nicht bloß eine universelle quadratische Formel.
- **#313 `RATIO`:** Algebraische Operatorform der Division, kein eigenständiger numerischer Quotientenbefehl.
- **#315/316 `RCI`/`RCIJ`:** Zeilenoperationen mit Multiplikationsfaktor und ggf. Addition zu einer anderen Zeile; Vektoren im Guide als Spaltenmatrizen behandelt.
- **#318 `RCLALARM`:** Liefert den Alarm mit Aktion und Zeit-/Intervallinformationen, teilweise in `1/8192`-Sekunden-Ticks. Argument- und Ergebnisdetails gehören zur Verhaltensprüfung V.
- **#322 `RCLΣ`:** Abruf von `ΣDAT`, aber Pocket-OCR gibt `RCLE` zurück; kein zusätzliches Kommando `RCLE`.
- **#324 `RDM`:** Array-Redimensionierung; bei *benanntem* Array ist das Rückgabe-/Änderungsverhalten anders als bei namenloser Matrix.
- **#325 `RDZ`:** Setzt Zufallsgenerator-Seed; nicht „RDM“ und nicht ein zweiter Zufallsgenerator.
- **#327 `RECN` und #329 `RECV`:** Erstes empfängt und benennt Kermit-Dateien, das zweite empfängt bereits benannte Daten. Beides nicht als ein und denselben Aufruf zusammenziehen.
- **#330 `REPEAT`:** RPL-`WHILE`-Schleifenteil. Nicht mit `FOR`/`NEXT` verwechseln.
- **#331 `REPL`:** Teilersetzung in Strings, Arrays, Listen **und GROBs**.
- **#335–337 `RKF`, `RKFERR`, `RKFSTEP`:** Runge-Kutta-Fehlberg-Lösung, absolute Fehlerschätzung und nächster Schritt sind getrennte Aufrufe. Pocket-Web-OCR schreibt den letzten Namen `REFSTER`.
- **#338/339 `RL`/`RLB`:** Rotation um **ein Bit** bzw. **ein Byte**.
- **#340 `RND`:** Unterschied zwischen Anzahl Dezimalstellen, signifikanten Stellen und dem aktuellen Anzeigeformat. Im Pocket Guide wird ein spezieller Wert `n=12` für das aktuelle Format genannt; Grenzwerte/Flags müssen später anhand AUR präzisiert werden.
- **#342/343 `ROLL`/`ROLLD`:** Operationen auf den obersten `n` Stackobjekten nach Verbrauch des Zählarguments; nicht mit `ROT` auf den obersten drei Elementen identisch.
- **#346–349 `→ROW`, `ROW+`, `ROW−`, `ROW→`:** Arrayzerlegung in Zeilen **plus Zeilenanzahl**, Einfügen, Entfernen **mit Rückgabe der entfernten Zeile**, Wiederaufbau aus Zeilenobjekten. Nicht gegenseitig vertauschen.
- **#350 `RR`:** Rotiert ein Binärwort um ein Bit nach rechts; **nicht** `RRB` (Byte-Rotation), das erst in A08 folgt.

### Konkrete Quellen- und Zähldifferenzen

- In dieser AUR-Tranche gibt es **keinen** historischen Namen ohne direkten ROM-Indexnamen und **keine** doppelte AUR-Indexposition.
- Die Pocket-OCR verwischt u. a. `→Q`, `→Qπ`, `RCLΣ`, `RDM`, `RDZ`, `RECV`, `RKFSTEP`, `RLB`, `RND`, `ROT`, `→ROW` und `ROW→`; sämtliche Namen werden in der Tabelle **anhand ihrer Quelle und Nachbarzeilen** zugeordnet und benötigen später Bildsichtkontrolle.
- Einzelne Beschreibungen im bestehenden Katalog waren zu kurz, beispielsweise `QR`, `QUAD`, `ROLL`, `ROW−`; im Hauptkatalog präzisieren, ohne das Fehlerverhalten zu erfinden.

## 4. Abnahmegrenze

- [x] **50** AUR-TOC-Positionen positionsgenau dokumentiert; **50 verschiedene** Namen.
- [x] Für alle **50** ein Eintrag im eingefrorenen ROM-Index mit tatsächlicher XLIB-Kennung.
- [x] Alle **50** auf den Pocket-Guide-Textseiten 60/62/64 kontextuell zugeordnet; OCR-Unsicherheiten getrennt ausgewiesen.
- [x] Selbst verfasste deutsche Arbeitsbeschreibung je Name und die wichtigsten konzeptuellen Unterschiede erfasst.
- [ ] Originale AUR-/Pocket-Guide-Druckseiten **visuell** zeilen- und glyphengenau geprüft.
- [ ] Stackdiagramme, Objekttypen, Flags, Nebenwirkungen, Rundung, Fehlerfälle, reale Geräteausführung **pro Befehl** geprüft.

**A07-Checkpoint:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE`, `ORIGINAL_SCAN_NOT_SIGNED_OFF`, `AUR_STACK_NOT_SIGNED_OFF`. **Nächster AUR-Block: A08 (351–400, `RRB` bis `STEP`).** Vollständige historische Freigabe weiterhin **NO_GO**, kein Blocker für die erste iPhone-Rechner-Version.
