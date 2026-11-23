# HP-41C Time Module (HP 82182A) – vollständiger Funktionskatalog und Nachbildungs-Spezifikation

**Dokument-ID:** SASD-SCI-HP41-TIME-001  
**Stand:** 2026-11-23 · **Revision:** 1.0 · **Sprache:** Deutsch  
**Historisches Referenzprodukt:** Hewlett-Packard HP 82182A Time Module für HP-41C/HP-41CV  
**Projekt:** [SASD Scientific Calculator](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator)  
**Dokumentstatus:** **Recherchierte Funktions-/Verhaltensspezifikation, zur Implementierung vorbereitet – nicht implementiert, nicht vollständig verifiziert**  
**Geplanter Einsatz:** Optionales historisches Erweiterungsprofil der HP-41-Familie, **nicht** Bestandteil oder Abnahmevoraussetzung der ersten iPhone-Classic-RPN-Version.

> Dieses Dokument beschreibt sämtliche **29 öffentlich dokumentierten Time-Module-XROM-Befehle** von `26,01` bis `26,29` sowie die **nicht selbstständigen, kontextabhängigen Alarmkatalog-, Stoppuhr- und Uhr-Anzeigeaktionen**. Die fünf zusätzlichen HP-41CX-Zeitbefehle werden gesondert abgegrenzt. Ziel ist eine **unabhängig entwickelte Nachbildung des beobachtbaren Verhaltens**, nicht die Kopie des historischen ROMs. Alle als „offen“ bezeichneten Details müssen vor einer historischen Kompatibilitätsaussage durch das originale Handbuch und eine Referenzumgebung nachgewiesen werden.

## 1. Gegenstand und Abgrenzung

Das Time Module erweitert die HP-41-Grundmaschine um eine **laufende Echtzeituhr**, Kalender-/Zeitoperationen, Stoppuhr mit Zeitablage in Datenregistern, akustische/Melde-/Steueralarme, periodische Erinnerungen und zeitabhängige Programmausführung. Das ist **kein gewöhnliches Mathematikpaket**: Ein großer Teil der Semantik betrifft Zustandsübergänge, Tastenmodi, die reale Uhr und Nebenwirkungen in der gemeinsamen HP-41-Maschine.

- **Zum Modul gehörend:** XROM `26,01`…`26,29`; Modulstatus/-speicher, Zeitkorrektur, Alarmqueue, kontextabhängige interaktive Bedienung, Timer-/Stoppuhrzustand.
- **Nicht gesonderte XROM-Befehle:** spezielle Tasten innerhalb des Stoppuhr- und Alarmkatalogmodus; `ON`-Uhranzeige; im Handbuch abgedruckte Anwenderprogramme.
- **Nicht zum ursprünglichen HP 82182A gehörend:** fünf spätere HP-41CX-Zusatzbefehle `26,31`…`26,35`. `26,00` und `26,30` sind ROM-/Gruppenkennungen, keine zusätzlichen Endbenutzerfunktionen.
- **Nicht enthalten:** HP-41-Grundbefehle wie `HMS`/`HMS+`/`HMS−` oder beliebige Drittanbieterprogramme, andere ROMs, ein universeller HP-41/48-Interpreter und ein Nut-CPU-Emulator.
- **Rechte:** historische Namen ausschließlich zur sachlichen Referenz. Keine fremden ROMs, Programmlistings, gescannten Handbuchseiten oder Drittmarken-Grafiken in dieses Repository übernehmen. Eigene Algorithmen, Modellierung, Beispiele und Tests sind erlaubt, sofern etwaige Rechte gesondert geprüft sind.

Die vorhandene [Grundfunktionsliste](HP-41C-FUNKTIONSKATALOG.md) und die [Stat-Pac-Spezifikation](HP-41C-STAT-PAC.md) bleiben getrennte Kataloge. Kompatibilitätsgrade [K1–K4](../en/COMPATIBILITY.md) unterscheiden sich von den [Release-Meilensteinen M0–M5](../../ROADMAP.md).

### 1.1 Status / Evidenzniveau

| Kennzeichen | Bedeutung |
| --- | --- |
| **QRC-BELEG** | Befehl, Eingabe oder Tastenaktion wird auf der **gesichteten Original-Kurzinformationskarte** beschrieben. |
| **HP-HANDBUCH** | Detail oder Rahmenbedingung steht im originalen HP-Benutzerhandbuch, z. B. benannter Abschnitt/gedruckte Seite. |
| **XROM-BELEG** | Modulnummer und Befehlsnummer sind durch die gedruckte HP-XROM-Liste belegt. |
| **REFERENZ-MODELL** | Eigene abgeleitete technische Formulierung für Tests/Entwicklung; kein Nachweis identischer ROM-Implementierung. |
| **OFFEN** | Exakte Zahlendarstellung, Flags, Stack-/ALPHA-Seiteneffekt, Fehlerwortlaut, Timing oder Grenzregel noch nicht vollständig überprüft. |
| **GEPLANT** | Es wurde **keine** entsprechende SASD-Implementierung ausgeführt oder als historisch kompatibel getestet. |

**Quellenlage:** Die beiden Original-QRC-Seiten (DE/EN) wurden mit ihren Abbildungen verglichen. Das deutsche Handbuch ist im Archiv als lesbarer Scan/Text auffindbar; einzelne einschlägige Passagen (Kalendergrenzen, Alarmverhalten, XROM-Liste) wurden abgeglichen. Eine **vollständige Seite-für-Seite-Extraktion sämtlicher Befehls-, Fehler- und Stack-Effekte ist noch ausstehend**. Eine vorhandene PDF-Datei bedeutet nicht, dass alle Einträge bereits historisch verifiziert sind.

## 2. Bibliografie / Primärquellen

| Quellen-ID | Historische Quelle | Verfügbare PDF / Verwendungszweck |
| --- | --- | --- |
| **HP-TM-DE** | HP 82182A *Time Modul – Benutzerhandbuch*, `82182-90003`, Februar 1983 | [Deutsches Original-PDF](https://literature.hpcalc.org/community/hp82182a-om-de.pdf); Seiten zu Uhr/Kalender 13–25, Stoppuhr 27–37, Alarmen 39–55, Kompensation 57–59, Fehleranhang B ab 67, Programmierung/XROM 71–79 und überfälligen Alarmen ab 81. |
| **HP-TM-EN** | HP 82182A *Time Module Owner’s Manual*, `82182-90001`, Revision D, September 1982 | [Englisches Original-PDF](https://literature.hpcalc.org/community/hp82182a-om-en.pdf); unabhängige Sprach-/Revisionsgegenprüfung, 96 Scan-Seiten. |
| **HP-TM-QDE** | HP 82182A *Kurzinformations-Karte*, `82182-90006`, Mai 1982 | [Deutsche Original-Kurzkarte](https://literature.hpcalc.org/community/hp82182a-qrc-de.pdf), 2 Scan-Seiten. Gut für 29 Namen und das kontextabhängige Tastenfeld. |
| **HP-TM-QEN** | HP 82182A *Quick Reference Card*, `82182-90002`, November 1981 | [Englische Original-Kurzkarte](https://literature.hpcalc.org/community/hp82182a-qrc-en.pdf), 2 Scan-Seiten. Gut für Input-/Output-Formate. |
| **HP-EMU-APP** | HP 82210A *HP-41CV Emulator Application Card Owner's Manual* | [Original-PDF](https://literature.hpcalc.org/community/hp82210a-om-en.pdf), Anhang C „Time Functions“, gedruckte S. 140: XROM-Tabelle einschließlich nur im HP-41CX vorhandener Nummern. |
| **HP-TM-VASM** | HP 82182A Time Module VASM-Listing | [Archivlink](https://literature.hpcalc.org/community/hp82182a-vasm-remake.pdf) nur für historische **Recherche**; rechtliche Nutzung/Weitergabe gesondert klären. |
| **QREF** | HP-41 QREF Time Module | [Kompakte Vergleichsquelle](https://qrg41.fjk.ch/hp82182a.html), keine maßgebliche Primärquelle. |
| **FND-DB** | HP-41 Function Database | [Funktionsdatenbank](https://calc.fjk.ch/db/hp41fn.php); zusätzliche Modul-/Nummernüberprüfung. |

**Quellenpriorität:** HP-TM-QDE/QEN + HP-TM-DE/EN + HP-EMU-APP für historische Aussagen; QREF/FND-DB für unabhängige Plausibilität. **Die PDF-Handbücher werden verlinkt, nicht im Repository gespeichert.** Gedruckte Seitenzahlen sind nicht zwangsläufig identisch mit PDF-Viewer-Seiten.

## 3. Vollständige XROM-Befehlsliste – Original-HP-82182A

**Vollständigkeitskriterium:** Jeder Integer `n` in `26,n` für `n = 01 … 29` muss **genau einmal** vorkommen. Die Kategorie ist eine SASD-Dokumentationshilfe, keine historische CAT-Klassifikation. Alle 29 Zeilen: **XROM-BELEG + GEPLANT**.

| ID | XROM | Originalbefehl | Bereich | Eingabe / Ergebnis / Kernverhalten |
| --- | --- | --- | --- | --- |
| TM-01 | `26,01` | `ADATE` | ALPHA | Datum aus **X** im aktuellen MDY/DMY-Format formatiert an ALPHA anhängen; Anzeigestellenzahl beachten. |
| TM-02 | `26,02` | `ALMCAT` | Alarm | Katalog anstehender/überfälliger Alarme; `R/S` hält Auflistung an, aktiviert eigene Katalog-Tastenbelegung. |
| TM-03 | `26,03` | `ALMNOW` | Alarm | Ältesten überfälligen **Programm-/Funktionsalarm** aktivieren. |
| TM-04 | `26,04` | `ATIME` | ALPHA | Zeitwert in **X** im aktiven 12-/24-h-Format an ALPHA anhängen. |
| TM-05 | `26,05` | `ATIME24` | ALPHA | Zeitwert in **X** unabhängig vom aktiven Anzeigeformat in 24-h-Form an ALPHA anhängen. |
| TM-06 | `26,06` | `CLK12` | Format | 12-Stunden-Uhranzeige aktivieren. |
| TM-07 | `26,07` | `CLK24` | Format | 24-Stunden-Uhranzeige aktivieren. |
| TM-08 | `26,08` | `CLKT` | Format | Uhranzeige auf ausschließlich Uhrzeit stellen. |
| TM-09 | `26,09` | `CLKTD` | Format | Uhranzeige auf Uhrzeit **mit Datum** stellen. |
| TM-10 | `26,10` | `CLOCK` | Uhr | Laufende Uhranzeige aufrufen; Bedienalternative über `ON` ist kein weiterer XROM-Befehl. |
| TM-11 | `26,11` | `CORRECT` | Uhrkorrektur | Uhrzeit wie `SETIME` setzen **und** Gang-/Kompensationsfaktor automatisch nachführen. |
| TM-12 | `26,12` | `DATE` | Uhr/Kalender | Aktuelles Datum nach **X**; bei Tastaturausführung zusätzlich Datum und Wochentag anzeigen. |
| TM-13 | `26,13` | `DATE+` | Kalender | `Y` = Datum, `X` = Zahl Tage; Ergebnis neues Datum nach Addition. |
| TM-14 | `26,14` | `DDAYS` | Kalender | `Y` und `X` als Daten; vorzeichenbehaftete Differenz **Datum X minus Datum Y** in Tagen. |
| TM-15 | `26,15` | `DMY` | Format | Tag-Monat-Jahr; **Flag 31 setzen**. |
| TM-16 | `26,16` | `DOW` | Kalender | Datum aus **X** in Wochentagsnummer ersetzen: `0` = Sonntag, …, `6` = Samstag. |
| TM-17 | `26,17` | `MDY` | Format | Monat-Tag-Jahr; **Flag 31 löschen**. |
| TM-18 | `26,18` | `RCLAF` | Uhrkorrektur | Aktuellen Accuracy-/Kompensationsfaktor nach **X** holen. |
| TM-19 | `26,19` | `RCLSW` | Stoppuhr | Aktuellen Stoppuhrwert nach **X** holen (außerhalb Stoppuhrmodus). |
| TM-20 | `26,20` | `RUNSW` | Stoppuhr | Stoppuhr starten/fortsetzen (außerhalb Stoppuhrmodus). |
| TM-21 | `26,21` | `SETAF` | Uhrkorrektur | Accuracy-Faktor aus **X** einstellen; dokumentierter Bereich `−99.9 ≤ x ≤ 99.9`. |
| TM-22 | `26,22` | `SETDATE` | Uhr/Kalender | Echtzeituhr auf das als Datum kodierte **X** setzen. |
| TM-23 | `26,23` | `SETIME` | Uhr/Kalender | Echtzeituhr auf die als Uhrzeit kodierte Zahl in **X** setzen. |
| TM-24 | `26,24` | `SETSW` | Stoppuhr | Stoppuhrstartwert aus **X** setzen; `−99.595999 ≤ t ≤ 99.595999` (historische Zeitkodierung). |
| TM-25 | `26,25` | `STOPSW` | Stoppuhr | Stoppuhr anhalten (außerhalb Stoppuhrmodus). |
| TM-26 | `26,26` | `SW` | Stoppuhr | Interaktiven Stoppuhrmodus mit eigener Tastaturbelegung aktivieren. |
| TM-27 | `26,27` | `T+X` | Uhr/Kalender | Uhr um die Zeitspanne **X** im vorzeichenbehafteten `±HHHH.MMSShh`-Format verschieben; Datumsübertritt berücksichtigen. |
| TM-28 | `26,28` | `TIME` | Uhr | Aktuelle Uhrzeit im **24-Stunden-Format** nach **X**; Tastaturaufruf zeigt Uhrzeit zusätzlich an. |
| TM-29 | `26,29` | `XYZALM` | Alarm | Alarm anlegen; **X** Uhrzeit, **Y** Datum, **Z** Wiederholungsintervall; ALPHA spezifiziert Alarmtyp/Text oder Programm/Funktion. |

**Überprüfbare Gesamtzahl:** 29 Befehle, XROM-IDs ohne Lücke von `26,01` bis `26,29`. **`26,00` bezeichnet die Modul-ROM-Gruppe** und ist keine dreißigste Anwenderfunktion.

### 3.1 Thematische Zählung (ohne Doppelzählung)

| Funktionaler Hauptbereich | Aufrufnamen | Anzahl |
| --- | --- | ---: |
| ALPHA-Funktionen | `ADATE`, `ATIME`, `ATIME24` | 3 |
| Alarmbefehle | `ALMCAT`, `ALMNOW`, `XYZALM` | 3 |
| reine Formate/Anzeigeoptionen | `CLK12`, `CLK24`, `CLKT`, `CLKTD`, `DMY`, `MDY` | 6 |
| Uhr-/Kalender- und Gangkorrekturbefehle | `CLOCK`, `CORRECT`, `DATE`, `DATE+`, `DDAYS`, `DOW`, `RCLAF`, `SETAF`, `SETDATE`, `SETIME`, `T+X`, `TIME` | 12 |
| Stoppuhr | `RCLSW`, `RUNSW`, `SETSW`, `STOPSW`, `SW` | 5 |
| **Gesamt** | | **29** |

## 4. Zahlen- und Datumskodierung

Für eine historisch korrekte HP-41-Nachbildung genügt **kein** normales Host-`datetime`-Objekt. Der Rechner überträgt Datums- und Zeitwerte zwischen **echter laufender Uhr** und numerischen 41er-X-/Y-/Z-Registern.

### 4.1 Datumswerte: MDY und DMY

| Modus | HP-numerischer Wert bei `FIX 6` | Beispiel 1. Januar 1900 | Flag 31 |
| --- | --- | --- | --- |
| `MDY` | `MM.DDYYYY` | `1.011900` | gelöscht |
| `DMY` | `DD.MMYYYY` | `1.011900` | gesetzt |

Die beiden Beispieldaten sind wegen gleicher Monat-/Tageszahl **nicht geeignet**, um die Modi zu unterscheiden. Besser: **17. Juli 1982** ist im MDY-Modus `7.171982` und im DMY-Modus `17.071982`. In beiden Fällen hängt das Jahr in der historischen Darstellung an die Monats-/Tageskomponente an.

**Aus den Original-Kurzkarten:** Eingabedaten müssen positiv sein; nicht benutzte Stellen **rechts der Jahreszahl** dürfen keine von null verschiedenen Ziffern enthalten. Der aktive Anzeigezustand (`FIX` u. a.) beeinflusst die Ausgabe; Parser und Wertebereich müssen trotzdem getrennt bleiben.

**Wichtig:** Diese Zahl ist **keine** Unix-Zeit, keine ISO-8601-Zeichenkette und kein normaler dezimaler Bruchteil. Ohne dezimale/BCD-kompatible Konvertierung kann eine direkte `double`-Interpretation zu fehlerhaften Kalendertagen führen.

### 4.2 Unterschiedliche gültige Bereiche

- **Echtzeituhr und `SETDATE`:** **01.01.1900 bis 31.12.2199** (HP-TM-DE, gedruckte S. 14 und Fehleranhang).
- **Reine Kalenderfunktionen:** **15.10.1582 bis 10.09.4320** (HP-TM-DE, gedruckte S. 23–25). Gregorianische Kalenderarithmetik.
- **`T+X`:** darf das aktuelle Uhrdatum nicht außerhalb des Uhr-Bereichs bewegen; bei Überschreiten dokumentiert HP **`OUT OF RANGE`**.
- **`DATE+`:** darf das Ergebnisdatum nicht außerhalb des größeren Kalenderbereichs bewegen; bei Überschreiten dokumentiert HP **`OUT OF RANGE`**.

Das ist ein **absichtlicher** historischer Unterschied. Bei der technischen Modellierung also keine künstliche Gleichsetzung der Bereiche.

### 4.3 Uhrzeitwerte

HP verwendet für Uhrzeiten Zahlendarstellungen wie `HH.MMSS…`, nicht die reelle Dezimalzahl der Tagesstunden. Die Kurzinformationskarte nennt für `SETIME`:

- `0.000000` bis `11.595999`: Vormittag/A.M. (einschließlich Mitternacht);
- `12.000000` bis `23.595999`: Nachmittag/P.M.;
- `−1.000000` bis `−11.595999`: weitere im Original unterstützte P.M.-Kodierung.

Der genaue Umgang mit `12:00`, `−0`, zulässigen Minuten-/Sekundenfeldern und Hundertstelsekunden ist im späteren Parser **pro Aufruf** zu prüfen. **`CLK12`/`CLK24` verändern die Darstellung**, nicht automatisch die numerische Kodierung aller Befehle.

Für `T+X` beschreibt die QRC einen Zeit-**Versatz** im Format `±HHHH.MMSShh`; dieser kann größer als ein Tag sein und den Uhrkalendertag ändern. Der Sekunden-/Hundertstelanteil ist kein Dezimalbruch von Stunden.

### 4.4 Zeitquelle, Sommerzeit und Zeitzonen

Im historischen Gerät gibt es eine **lokale Echtzeituhr** mit manuell gesetztem Datum/Uhrzeit und Gangkompensation, keinen für alle historischen Einsätze definierten ISO/IANA-Zeitzonenservice. Eine moderne SASD-Bibliothek darf optional moderne Zeitzonen anbieten, **muss** im historischen Profil aber unabhängig bleiben von automatischer Betriebssystem-DST-Verstellung. **OFFEN:** konkretes Verhalten des historischen Moduls bei der Reihenfolge manueller Zeitsprünge und Alarmen sowie eventuelle Rollover-Grenzen.

Für deterministische Tests sind nötig:

1. **injizierbare simulierte Kalenderzeit** (steuerbar und zurücksetzbar);
2. **monotone Tick-Quelle** für laufende Stoppuhr;
3. klar getrennte **angezeigte/lokale Rechnerzeit** und **Hostzeit**;
4. definierte Behandlung von Zeitkorrektur, Vor-/Rückstellen und Wiederanlauf.

## 5. Uhr- und Kalenderbefehle im Detail

### 5.1 `CLK12`, `CLK24`, `CLKT`, `CLKTD`, `CLOCK`

| Kommando | Eingabe | Primärer Zustandseffekt | Ausgaben/offene Tests |
| --- | --- | --- | --- |
| `CLK12` | keine | Uhranzeigeformat `12h` | AM/PM/12:00, Stackeffekt OFFEN |
| `CLK24` | keine | Uhranzeigeformat `24h` | 00–23 Uhr, Stackeffekt OFFEN |
| `CLKT` | keine | Uhr bei Aktivierung nur Zeit | Displayformatprüfung |
| `CLKTD` | keine | Uhr bei Aktivierung Zeit + Datum | Displaybreite, Datumsmodus |
| `CLOCK` | keine | Uhranzeige aktivieren | Anzeige aktualisiert sich; Abbruch durch Tastatur, `ON`-Alternative |

Das Original beschreibt zusätzlich einen **nicht regulär programmierbaren `ON`-Weg** zur Uhranzeige. Diesen nicht in einen erfundenen `26,30`-Befehl verwandeln. Die Tastenwirkung ist vom Rechnerzustand abhängig und muss in den HP-41-Keyboard-Adapter.

### 5.2 `SETDATE`, `SETIME`, `DATE`, `TIME`

| Befehl | Wert in X bei Aufruf | Wirkung |
| --- | --- | --- |
| `SETDATE` | MDY-/DMY-Datumszahl | Reale Modul-Uhr auf dieses Datum stellen; nur Uhr-Datumsbereich. |
| `SETIME` | zulässiger HP-Uhrzeitwert | Uhrzeit einstellen, **ohne** die automatische Neukalibrierung von `CORRECT`. |
| `DATE` | keiner; X wird ersetzt | Aktuelles Uhrdatum gemäß Datumsmodus ins X-Register. Tastaturaufruf zeigt zusätzlich Wochentag. |
| `TIME` | keiner; X wird ersetzt | Aktuelle Uhrzeit im 24-h-Numerikformat ins X-Register. Tastaturaufruf zeigt sie zusätzlich. |

**OFFEN je Aufruf:** exaktes Stack-Lift-/LAST-X-Verhalten; Bildschirmtext unter `FIX`/`SCI`/`ENG` und bei ALPHA-Eingabestatus; Datum/Uhrzeit bei gleichzeitig anstehenden Alarmen; historische Fehlerpriorität.

### 5.3 `DATE+`, `DDAYS`, `DOW`

- **`DATE+`:** Zahl **X** = ganzzahlige Tagesänderung, **Y** = ursprüngliches gültiges Datum. **SASD-Referenzmodell:** Datum plus Zahl Kalendertage, Monats-/Jahreswechsel und Schalttage inklusive. Das tatsächliche historische Verhalten bei **nichtganzzahligen** Tagen ist **OFFEN**.
- **`DDAYS`:** **X − Y** als Kalendertagszahl. Beispiel für den üblichen Referenzfall: `DDAYS(29.11.1982,17.07.1982)=+135`, umgekehrt `−135`.
- **`DOW`:** ersetzt X durch `0` Sonntag, `1` Montag, …, `6` Samstag. Das Ergebnis muss über den ganzen historischen Kalenderbereich dem **gregorianischen** Kalender entsprechen.
- Alle drei **sind nicht abhängig vom Gangkorrekturfaktor**. Bei ihrer Ausführung soll nicht die laufende Uhr verstellt werden.

**Beispiel aus HP-TM-DE, Kalenderarithmetik:** 17. Juli 1982 + 135 Tage = **29. November 1982**. Dieses Beispiel ist als **Quellenvorschlag** für einen späteren manuellen Original-Trace vorgesehen, noch kein geprüfter SASD-Testlauf.

### 5.4 `DMY`, `MDY`

Diese Befehle beeinflussen die numerische Datumseingabe/-ausgabe, nicht die gespeicherte absolute Zeit. Das Original führt die Kopplung an das **Flag 31** ausdrücklich auf. Prüfen: Wirkung auf `ADATE`, `DATE`, `SETDATE`, `DOW`, `DATE+`, `DDAYS`, `XYZALM` und Alarmkatalog-Datum, ohne die Chronologie zu verändern.

## 6. ALPHA-Funktionen

| Befehl | Inhalt X | Erwartete Wirkung | Details vor historischer Abnahme |
| --- | --- | --- | --- |
| `ADATE` | Datumszahl | **An vorhandenen ALPHA-Text anhängen**, nicht pauschal ALPHA löschen | MDY/DMY, Jahrdarstellung, `FIX`-Stellenzahl, Länge/Abschneidung, Flag 31, X/Stack. |
| `ATIME` | Zeitwert | Im aktuellen `CLK12`-/`CLK24`-Format an ALPHA anhängen | Leerzeichen, AM/PM, lokale Darstellung, Trunkierung, X/Stack. |
| `ATIME24` | Zeitwert | Im 24-Stunden-Format an ALPHA anhängen | unabhängig von `CLK12`, Sekundenbruchteile, Trunkierung, X/Stack. |

Die Original-QRC sagt **Trunkierung nach eingestellter Anzahl von Anzeigeziffern**. Die exakten Zeichenbytes und die Begrenzung des 41er-ALPHA-Registers dürfen nicht aus einer modernen String-Bibliothek abgeleitet werden. Bei dieser Gruppe ist der primäre Effekt eine **Text- und Registermutation**, nicht eine reine numerische Berechnung.

## 7. Gangkorrektur / Accuracy Factor

| Befehl | Wirkung | Spezifische Anforderungen |
| --- | --- | --- |
| `SETAF` | Accuracy-/Kompensationsfaktor aus X setzen | QRC-Grenzen **`−99.9 ≤ x ≤ 99.9`**; Einheit/Intervall, historische interne Speicherung **OFFEN**. |
| `RCLAF` | Faktor nach X lesen | Darstellung, Korrektur der laufenden Zeit, Stackeffekt **OFFEN**. |
| `CORRECT` | `SETIME` ausführen und **automatisch** den Kompensationsfaktor neu bestimmen | Abhängigkeit von vorheriger Setz-/Korrekturhistorie, Uhrdrift, Rundung, gültiges Korrekturintervall **OFFEN**. |

Ein reines `datetime.now()` plus Kalenderformatierung würde diese Befehle **nicht** nachbilden. Geplantes virtuelles Zeitmodell:

~~~text
HistoricalClock {
  local_calendar_date;
  local_time_of_day_with_subsecond_precision;
  reference_host_instant_or_simulated_tick;
  accuracy_factor;
  last_set_or_correction_metadata;
  display_mode_12_or_24;
  display_content_time_or_time_date;
  date_mode_MDY_or_DMY_and_flag_31;
}
~~~

Dies ist ein **Designvorschlag**, nicht das originale ROM-RAM-Layout. Reale Uhrdrift und automatische Gangkorrektur sind separat zu modellieren/testen, statt sie implizit der Hostuhr zu überlassen.

## 8. Vollständiges Stoppuhrmodell

Die Stoppuhr ist **eine andere Zeitbasis und Bedienoberfläche** als die Kalenderuhr. Das Original beschreibt eine laufende Stoppuhr, einstellbare Start-/Rückrufwerte, Zwischenzeiten und Zugriff auf HP-41-Register.

### 8.1 Die fünf öffentlichen Befehle

- **`SW`:** in den interaktiven Stoppuhrmodus wechseln und Tasten umbelegen.
- **`RUNSW`:** Stoppuhr außerhalb des interaktiven Modus starten/fortführen.
- **`STOPSW`:** Stoppuhr außerhalb dieses Modus anhalten.
- **`SETSW`:** historischen Stoppuhrstartwert in `−99.595999 … +99.595999` setzen. **OFFEN:** exakte Annahme von Vorzeichen-/Sonderwerten und Overflow-Grenzen.
- **`RCLSW`:** aktuelle Stoppuhrzeit in X abrufen. Der Wert muss auch nach Start/Stop konsistent zum Laufzustand sein.

Laut HP-QRC gelten die vier `RUNSW`/`STOPSW`/`SETSW`/`RCLSW`-Aufrufe **außerhalb** des Stoppuhrmodus. Das ist **nicht** gleichbedeutend mit beliebig erlaubten Aufrufen während des aktiven `SW`-Dialogs.

### 8.2 Vollständige zusätzliche Tastenbelegung im `SW`-Modus

**Quelle:** Original-QRC DE/EN, jeweils Seite 1. Diese Aktionen sind **keine** eigenen XROM-Namen.

| Taste/Kombination | Historische Bedienwirkung | Testpflicht |
| --- | --- | --- |
| `nn` (Zifferntasten) | Registeradresse `Rnn` oder `Dnn` bestimmen | Reihenfolge, Nullauffüllung, erlaubte Adressräume. |
| `←` | **Angehaltene** Stoppuhr löschen/rücksetzen | Laufend vs. gestoppt, Zeigererhalt. |
| `SHIFT + ←` | Stoppuhrmodus verlassen | Speicherzustand, laufende Zeit und Anzeigezustand erhalten? |
| `SST` | Nächstes `Rnn/Dnn` auswählen | Grenzen, Pointer-Wrap, aktive Ansicht. |
| `SHIFT + BST` | Vorheriges `Rnn/Dnn` auswählen | Grenzen, Pointer-Wrap, aktive Ansicht. |
| `ENTER↑` | Zwischenzeit erfassen/speichern | Wert, Registerschreibeffekt, automatische Zeigerfortschaltung. |
| `R/S` | Stoppuhr starten/anhalten | Fortsetzen ohne Verlust kumulierter Zeit. |
| `EEX` | Registerzeiger ein-/ausblenden | Anzeige- und Zustandseffekt. |
| `CHS` | Zeitdifferenzansicht ein-/ausschalten | Differenzbasis, erstes Zwischenzeitereignis. |
| `RCL` | Zwischenzeit-Rückrufansicht ein-/ausschalten | Speicher-/Rückrufzeiger getrennt führen. |
| `SHIFT + EEX` | Dreistelligen Registerzeiger ein-/ausschalten | Adressierbarkeit, Anzeigeformat. |

Die im Handbuch besprochenen **Speicher- und Rückrufzeiger** sind potenziell **getrennte Zustände**: Nach dem Umschalten zwischen Live-/Rückrufanzeige soll der jeweilige zuletzt benutzte Zeiger erhalten bleiben. In der deutschen Originalbeschreibung werden außerdem Speicherregister bis `R(318)` und `Dnn` besprochen. **OFFEN:** wie dieses Adressierungsmodell je 41C/41CV/41CX und Speichererweiterung konkret umzusetzen ist.

### 8.3 Zwischenzeit und Differenz

Die Begriffe sind **nicht** austauschbar:

- **elapsed time:** seit Start/`SETSW` vergangene Stoppuhrzeit;
- **split time:** Wert bei `ENTER↑` als Zwischenzeit festhalten;
- **split difference:** Differenz zwischen ausgewählten Zwischenzeiten;
- **recall:** gespeicherte `Rnn`-/`Dnn`-Werte nach eigenem Zeiger anzeigen;
- **running vs halted:** unabhängiger Laufzustand; `SW`-Dialog kann verlassen werden, ohne den Zeitmesser zwangsläufig zu löschen.

Die Untersekunden- und Obergrenzen müssen nach einer festgehaltenen Referenz-Zeitquelle geprüft werden. Ein kurzer Unit-Test darf **keine echte Sekunde schlafen** müssen: Tickquellen injizieren und vorspulen.

## 9. Vollständiges Alarmmodell

### 9.1 `XYZALM` – Alarm anlegen

Das Modul liest die Parameter aus dem historischen **HP-41-RPN-Stack und ALPHA-Register**:

| Speicher | Historische Bedeutung | Sonderwert |
| --- | --- | --- |
| **X** | Alarmuhrzeit | Eingabe im historischen Zeitformat |
| **Y** | Alarmdatum | **0** = aktuelles Datum |
| **Z** | Wiederholungsintervall | **0** = keine Wiederholung |
| **ALPHA** | leer, Nachricht, auszuführendes Label oder Funktion mit Steuerkennzeichen | Zwei Arten steuernder Alarme über **ein** oder **zwei** spezielle ALPHA-Pfeilzeichen |

Die QRC unterscheidet:
1. **Akustischen Alarm** ohne ALPHA-Nachricht;
2. **Meldealarm** mit ALPHA-Nachricht;
3. **Unterbrechenden Steueralarm** mit Doppel-Pfeilkennung vor Programm-Label/Funktion;
4. **Nichtunterbrechenden Steueralarm** mit einfacher Pfeilkennung.

Die Steuerkennzeichen werden im Modell **als historische ALPHA-Sonderzeichen** mit eigener Codierung geführt, **nicht** als frei erfundene Unicode-Normalisierung. Eine im Alarm benannte externe Funktion muss nach HP-QRC eine **programmierbare Gerätefunktion** sein. Ein bloßer String mit einem Hostfunktionsnamen ist deshalb keine zulässige Ausführungsberechtigung.

**OFFEN:** Grenzwerte/Zeitauflösung des Wiederholungsintervalls, genaue Bytekodierung der Pfeile, Labels-/Funktionserkennung, Stapelwirkung, Anzeigereaktionen, Reihenfolge bei mehreren gleichzeitigen Alarmen, Speicherbedarf pro Alarm.

### 9.2 `ALMCAT` – Alarmkatalog und eigene Tasten

Nach `ALMCAT` läuft eine Katalogdarstellung. **`R/S` unterbricht die Liste**; anschließend gelten die folgenden **nicht programmierbaren** Interaktionsaktionen (Original-QRC):

| Taste | Katalogaktion |
| --- | --- |
| `SHIFT + C` | ausgewählten Alarm löschen |
| `D` | Alarmdatum anzeigen |
| `T` | Alarmuhrzeit anzeigen |
| `M` | Nachricht / Label / Funktion anzeigen |
| `R` | Wiederholungsintervall anzeigen |
| `SHIFT + T` | aktuelle Uhrzeit anzeigen |
| `SST` | nächsten Alarm wählen |
| `SHIFT + BST` | vorherigen Alarm wählen |
| `←` | Alarmkatalogmodus verlassen |
| `SHIFT + R` | ausgewählten Alarm mit seinem Wiederholungsintervall neu einstellen |
| `R/S` | automatische Katalogausgabe fortsetzen |

Im Katalogmodus wird **ALPHA nicht wie eine normale Eingabetaste** verwendet. **OFFEN:** genaue Tastenzuordnung bei Hardwarevariante/SHIFT-Anzeige, Displaytexte, Randverhalten bei leerem Katalog, Sortierregeln für fällige/überfällige Alarme, Speicherfolgen beim Löschen.

### 9.3 `ALMNOW` – fällige Steueralarme

`ALMNOW` aktiviert ausdrücklich den **ältesten überfälligen Programm- oder Funktionsalarm**, nicht jede überfällige akustische Nachricht. Zu modellieren sind wenigstens:
- Alter und Sortierung der überfälligen Steueralarme;
- der aktuelle Rechnerzustand (ON/OFF, Tastatureingabe, laufendes FOCAL-Programm, `ALMCAT`);
- **unterbrechende** versus **nichtunterbrechende** Steueralarme;
- Programm-/Funktionsaufrufe einschließlich eigener Stacks/Programmzeiger-Semantik;
- wiederholte, nicht quittierte und bereits „aktivierte überfällige“ Alarme.

Die Originalbeschreibung diskutiert dazu besondere **ON-/Alarm-Bedingungen** in Anhang D (gedruckt ab Seite 81). Für korrekte Wiederholung und Steuerung darf der Scheduler nicht einfach „falls fällig: Callback aufrufen“ sein.

### 9.4 Alarmquittierung, Überfälligkeit, Zeitänderungen

Das deutsche Handbuch beschreibt bei einem akustischen Alarm eine blinkende Anzeige und Quittierung mit **`←`**; wird nicht rechtzeitig quittiert, kann ein Alarm **überfällig** bleiben und weiter verwaltet werden. **OFFEN:** exakte Zahl der Signaltöne, Alarmzustand, Überfälligkeit und Taste je Alarmart/Referenzrevision; einen vereinfachten UX-Alarm daher **nicht** als historisch korrekt darstellen.

Bei Uhrzeit-/Datumsänderung durch `SETIME`, `SETDATE`, `CORRECT` oder `T+X` darf die Alarmverwaltung **nicht** blind unverändert nach Host-Systemzeit weiterlaufen. Zeitänderungen bei bereits programmierten Alarmen sind im Originalhandbuch gesondert erläutert.

**Speicherbedarf:** Im deutschen Original-Anhang B wird ein Grenzfall beschrieben, in dem bereits **253 Register zur Alarmspeicherung** belegt sind. Das ist **keine** Angabe „maximal 253 Alarme“: Alarme belegen unterschiedlich viele Speicherregister. Die genaue historische Kapazitäts-/Komprimierungsregel ist vor Fidelity-Abnahme aus dem Handbuch zu rekonstruieren.

### 9.5 Alarm und Hostsystem – zwingende Sicherheitsgrenze

Ein historischer Steueralarm **darf niemals Host-Befehle, Shellskripte, Betriebssystemaufrufe, Netzwerkzugriffe oder beliebige Speicheradressen** direkt ausführen. Er darf ausschließlich eine **explizit freigegebene virtuelle HP-41-Funktion/ein simuliertes FOCAL-Label** im gesicherten Series-41-Profil adressieren. Das gilt auch bei geladenen historischen Programmdateien. Externe Benachrichtigungen, Hintergrundausführung und iOS-Notification-Permissions sind **eigene moderne Produktentscheidungen** und keine automatisch historisch erforderliche Berechtigung.

## 10. Historische Programmierung und XROM-Identifikation

Das HP-Handbuch erläutert im Anhang C die Programmierbarkeit der Modulbefehle und ihre Darstellung ohne eingestecktes Modul.

- **Modulkennung:** 26.
- **Funktionskennungen:** 01 bis 29.
- **Wenn Modul vorhanden:** der Rechner zeigt Programmschritte mit den Funktionsnamen an.
- **Wenn Modul entfernt:** vormals eingefügte Kommandos erscheinen als XROM-Kennung; über `XEQ` nachträglich programmierte Namen können sich anders verhalten (Suche nach ALPHA-Name/Label). **Exaktes Byteschema/Zeichencodierung bei späterem FOCAL-Decoding prüfen.**
- **Nicht programmierbar:** die speziellen kontextabhängigen Tasten während `SW` und angehaltenem `ALMCAT` sowie bestimmte Uhranzeigeaktionen des `ON`-Tastenpfads.

### 10.1 Vier gedruckte Anwenderprogramme (keine ROM-Befehle)

| Name | Gedruckter Original-Handbuchbereich | Aufgabe |
| --- | --- | --- |
| `SETALM` | Anhang C, ab S. 71 | Interaktive Alarmprogrammierung mittels Anwenderprogramm. |
| `ALMREL` | S. 72–73 | Alarm relativ zur aktuellen Uhrzeit planen. |
| `ADOW` | S. 73–74 | Wochentag aus Datumswert ermitteln und als ALPHA-Text bereitstellen. |
| `SPLITS` | S. 74–75 | Aufgezeichnete Zwischenzeiten gesammelt ausgeben. |

Sie sind eine **spätere Integrations-Testklasse**, nicht vier weitere `26,xx`-Funktionen. Original-Programmlistings und Barcode-Grafiken nur **verlinken**, nicht unautorisiert übernehmen. Für SASD eigene unabhängige Test- und Demonstrationsprogramme schreiben, wenn der historische FOCAL-Interpreter bereitsteht.

## 11. HP-41CX – ausdrücklich getrennte Zusatzfunktionen

Die offizielle HP-XROM-Tabelle im `HP-EMU-APP`-Handbuch weist die folgenden **fünf CX-only**-Befehle aus. Sie dürfen **nicht** als Teil des originalen HP-82182A-Steckmodul-Umfangs gerechnet werden:

| XROM | HP-41CX-Befehl | Vorläufige Rolle | Status |
| --- | --- | --- | --- |
| `26,30` | `-CX TIME` | **Gruppen-/ROM-Kennung, kein Befehl** | separat |
| `26,31` | `CLALMA` | Alarm anhand ALPHA-bezogener Auswahl löschen | CX-only, Details OFFEN |
| `26,32` | `CLALMX` | Alarm anhand X-bezogener Auswahl löschen | CX-only, Details OFFEN |
| `26,33` | `CLRALMS` | Alarme löschen | CX-only, Details OFFEN |
| `26,34` | `RCLALM` | Alarmdaten abrufen | CX-only, Details OFFEN |
| `26,35` | `SWPT` | Stoppuhr-Zeigerfunktion | CX-only, Details OFFEN |

Diese Kurzbeschreibungen sind **Funktionshinweise**, keine vollständige Parametrisierung. Eine CX-Nachbildung benötigt eine **eigene** Prüfung gegen das HP-41CX-Originalhandbuch und konkrete ROM-Revisionen. Die Tatsache, dass XROM-IDs benachbart sind, bedeutet nicht, dass sie auf einem 41C + Steckmodul verfügbar wären.

## 12. Fehlerfälle und Nebenwirkungen – Pflichtmatrix

| Konstellation | Erwartete Verhaltenklasse | Historische Details |
| --- | --- | --- |
| ungültiges Datum, negative Eingabe, nichtnullige Stellen hinter dem Jahr | Eingabe-/Datenfehler | Original-Handbuch Anhang B; genaue Fehleranzeige je Befehl ergänzen. |
| Uhrdatum außerhalb 1900–2199 (`SETDATE`, `T+X`) | Fehler bzw. `OUT OF RANGE` | Für `T+X` explizit belegt; Zustand bei Fehler prüfen. |
| Kalenderdatum außerhalb 1582-10-15…4320-09-10 (`DATE+`, `DOW`, `DDAYS`) | Wertebereichsfehler | `OUT OF RANGE` für `DATE+` explizit belegt; übrige Wortlaute offen. |
| ungültige Zeitminute/Sekunde oder ungültige Uhr-/Intervallkodierung | Eingabefehler | Uhrzeitformate für `SETIME`, `SETSW`, `XYZALM`, `T+X` gesondert prüfen. |
| `SETAF` außerhalb `[−99.9,+99.9]` | Eingabefehler | genauen Fehler-/Mutationseffekt ergänzen. |
| `RCLSW`/`RUNSW`/`STOPSW`/`SETSW` während `SW`-Dialog | Kontextfehler/abweichende Tastenzuordnung | auf echtem Profil prüfen. |
| Alarmqueue voll / zu wenig historische Register | Speicherfehler | Anhang B; Alarm-Eintrag darf nicht halb angelegt werden. |
| Alarm für Vergangenheit oder Gleichzeitigkeit | fällig/überfällig/abgewiesen je Regel | Alarmarten und `ALMCAT`-Sortierung prüfen. |
| Uhr manuell zurück-/vorgestellt mit aktiven Alarmen | Ereignisumordnung | historischer Zeitregel-Trace erforderlich. |
| Aufruf eines nicht vorhandenen Labels/Funktionsmoduls durch Steueralarm | kontrollierter virtueller Programmfehler | keine Host-Ausführung, Fehlerzustand protokollieren. |
| mehrfach aufeinanderfolgende Alarme während Programm läuft | Unterbrechung/Aufschub/Priorisierung | Handbuch Anhang D, Tests mit Unterbrechung. |
| Speicherverlust/Unterspannung/Modulentfernung | historische Zustandsänderung | Handbuch Anhang A; Hostpersistenzentscheidung separat. |

**Moderne Stabilitätsregel:** Der SASD-Hostzustand darf bei Fehlern nicht zerstört werden. Das **historische** Fehler- und Registerverhalten muss auf der virtuellen 41-Maschine separat modelliert werden. Beide Regeln sind vereinbar, wenn die Komponenten sauber isoliert sind.

## 13. Teststrategie und Beispielprüfungen

**Zurzeit: keine der folgenden Prüfungen als historische Konformitäts- oder Integrationstests ausgeführt.** Die Werte sind eigene mathematische/kalendertheoretische Testideen; historische Anzeigepräzision und Stackeffekte müssen erst aufgezeichnet werden.

### 13.1 Katalog-/Dispatch-Abnahmetests

| ID | Prüfung | Erwartetes Ergebnis |
| --- | --- | --- |
| TM-CAT-001 | `26,01…26,29` auf eindeutige Namen abbilden | 29 verschiedene Befehle, keine Nummer fehlt. |
| TM-CAT-002 | `26,00` und `26,30` abfragen | Module-/Gruppenkennung, keine öffentliche Aufruf-Funktion. |
| TM-CAT-003 | `26,31…26,35` auf HP-41C/41CV ohne CX-only ROM | nicht verfügbar / ausdrücklich anderes Profil. |
| TM-CAT-004 | `CLOCK` und Uhranzeige über `ON` | gleicher sichtbarer Uhrmodus, aber `ON` kein zusätzliches XROM. |
| TM-CAT-005 | FOCAL-Kommandos bei vorhandenem/fehlendem Modul | Name/XROM-Verhalten gemäß ursprünglichem Modell. |

### 13.2 Deterministische funktionale Referenzvektoren

| Test-ID | Befehle / Anfangszustand | Prüferwartung / Evidenzstatus |
| --- | --- | --- |
| TM-DATE-001 | `MDY`, `SETDATE` mit `7.171982`; `DATE` | 17.07.1982 als Datum; **historisches Displayformat noch prüfen**. |
| TM-DATE-002 | `DMY`, `SETDATE` mit `17.071982`; `DATE` | Gleiches absolutes Datum, Flag 31 gesetzt. |
| TM-DATE-003 | `DATE+`: Y=17.07.1982, X=135 | **29.11.1982**, wie im originalen HP-Beispiel; Anzeige/Stack offen. |
| TM-DATE-004 | `DDAYS`: Y=17.07.1982, X=29.11.1982 | **+135** Tage; bei Umkehr **−135**. |
| TM-DATE-005 | `DOW` für 17.07.1982 | **6 = Samstag** nach gregorianischem Kalender. |
| TM-DATE-006 | `DOW` für 01.01.1900 | **1 = Montag** nach gregorianischem Kalender. |
| TM-DATE-007 | `DATE+` über 28.02.2000 → 29.02.2000 | Schaltjahr 2000; genaues Anzeigeformat offen. |
| TM-DATE-008 | `DATE+` über 28.02.1900 → 01.03.1900 | Kein Schaltjahr 1900. |
| TM-DATE-009 | `SETDATE` 31.12.2199 plus `T+X` über Mitternacht | Dokumentierter Wertebereichsfehler; keine unkontrollierte Host-Zeitmutation. |
| TM-DATE-010 | `DATE+` über 10.09.4320 hinaus | `OUT OF RANGE`; Kalendergrenze getrennt vom Uhrlimit. |
| TM-TIME-001 | `CLK12`/`CLK24` am selben simulierten Zeitpunkt 13:05 | Unterschiedliche Darstellung bei identischem Zeitpunkt, Formatzeichen offen. |
| TM-TIME-002 | `CLKT`/`CLKTD` am selben Zeitpunkt | Zeit-only gegenüber Zeit-plus-Datum. |
| TM-TIME-003 | `SETIME` 23:59:59, danach `T+X` mit +2 Sekunden | Folgetag 00:00:01; numerische Eingabekodierung definieren. |
| TM-TIME-004 | `CORRECT` vs. `SETIME` mit identischem Sollwert | Selbe neue Uhrzeit; nur `CORRECT` verändert den Accuracy-Factor nach historischer Regel. |
| TM-TIME-005 | `SETAF` = −99.9 und +99.9, danach `RCLAF` | Beide zulässige Grenzwerte rücklesbar, genaue Speicherung offen. |
| TM-ALPHA-001 | `ALPHA` = „Datum:“; `ADATE` | Datum wird **angehängt**, Präzision/Format abhängig von Flag 31. |
| TM-ALPHA-002 | Uhrwert und `ATIME` in `CLK12` vs. `ATIME24` | 12-/24h-Ausgabe unterschiedlich, 24h-Aufruf unabhängig vom Modus. |
| TM-SW-001 | `SETSW` = 0; `RUNSW`; simulierter Tick +90 s; `STOPSW`; `RCLSW` | 1 min 30 s ab Start, historisches Zahlenformat noch prüfen. |
| TM-SW-002 | `SW`; `R/S` starten; `ENTER↑` zu t=10 s und t=25 s | Zwei Zwischenzeiten werden korrekt gespeichert, Zeiger vorrücken. |
| TM-SW-003 | `SW`; zwei Zwischenzeiten; `CHS` / `RCL` | Differenz 15 s und unabhängige Rückrufzeiger. |
| TM-SW-004 | Stoppuhr anhalten, `←`, dann `SHIFT+←` | Stoppuhr löschen und Modus verlassen; exakt persistente Pointer prüfen. |
| TM-ALM-001 | `XYZALM` mit Z=0, Y=0, X=10:05, simulierte Uhr 10:00 | Einmaliger Alarm am aktuellen Datum, bis Fälligkeit nicht aktiv. |
| TM-ALM-002 | `XYZALM` mit Z≠0 | Periodischer Alarm bleibt bis zur historischen Wiederholungs-/Quittierregel verwaltet. |
| TM-ALM-003 | Anstehender Alarm; `ALMCAT`, `R/S`, `D/T/M/R` | Kein neuer XROM-Befehl; alle Anzeigen beziehen sich auf gewählten Eintrag. |
| TM-ALM-004 | Zwei überfällige Steueralarme; `ALMNOW` | Der **älteste** passende Alarm wird ausgelöst, kein beliebiger der Queue. |
| TM-ALM-005 | Uhr bei vorhandenem Alarm vor-/zurückstellen | Ereignis-/Katalogfolge entsprechend dem HP-Referenztrace. |
| TM-ALM-006 | Unterbrechender und nichtunterbrechender Steueralarm bei laufendem 41-Programm | Getrennte Kontrollfluss-Semantik; keine direkte Hostaktion. |
| TM-STATE-001 | Speichern/Wiederherstellen mitten in `SW`, `ALMCAT` und mit überfälligem Alarm | Gleicher virtueller Zustand ohne Doppelaktivierung und ohne Alarmverlust. |

**Beispiele mit fester Host-Zeit dürfen nicht als Tests von `TIME`/`DATE` eingesetzt werden.** Für `TIME` und `DATE` muss die simulierte Uhr fest eingefroren und in kontrollierten Schritten vorgerückt werden.

### 13.3 Golden-Trace-Format (Vorlage, noch leer)

~~~yaml
case_id: HP41-TIME-TM-XX-001
xrom: "26,XX"
mnemonic: "..."
historical_target: "HP-41C+HP 82182A"
reference: "real-device | emulator-with-authorized-rom"
reference_revision: null
source_id: "HP-TM-DE"
source_print_page: null
source_pdf_scan_page: null
fixture_rights: "independently-recorded"
clock:
  simulated_local_time: "1982-07-17T10:00:00"
  tick_advance_ms: 0
input:
  register_x: null
  register_y: null
  register_z: null
  alpha: ""
  flag31: false
  keyboard_sequence: []
expected:
  screen_frames: []
  stack_x_y_z_t: []
  last_x: null
  alpha: null
  data_register_delta: []
  flags: []
  alarm_queue: []
  stopwatch_state: null
  error: null
sasd_commit: null
verified_at: null
status: planned
~~~

Ein späteres golden fixture muss eindeutig zwischen **eigenständig berechnetem Fachreferenzwert** und **am Originalgerät tatsächlich beobachtetem Verhalten** unterscheiden. Fehlende Referenzstände niemals mit geratenen Werten auffüllen.

## 14. Empfohlene Architektur für die unabhängige Nachbildung

Ein sinnvoller, **nur vorgeschlagener** Modulzuschnitt (keine bestehenden Klassen/Verzeichnisse werden damit behauptet):

~~~text
portable / shared:
  CalendarMath                 # proleptic Gregorian and strict historical window
  DateSerialCodec              # MM.DDYYYY / DD.MMYYYY, strict BCD/decimal policy
  TimeOfDayCodec               # HH.MMSS[hh], legal fields and signed offsets
  VirtualClock                 # injected local clock and tick source
  StopwatchModel               # independent elapsed time and lap storage
  AlarmScheduler               # pending, due, activated, overdue, recurrence
  AccuracyFactorModel          # historical compensation, not host NTP

calculators / series41:
  Series41State                # four-level stack, LAST X, alpha, flags, registers
  FocalExecutionContext        # program pointer, execution/interruption rules
  TimeModuleProfile            # module presence, revision, profile capability
  TimeModuleXromDispatch       # 26,01...26,29
  TimeModuleKeyboardModes      # CLOCK, SW and halted ALMCAT interactions
  TimeModuleRegisterAdapter    # virtual HP-41 data registers
  TimeModuleSnapshotCodec      # versioned, validated state without host pointers

native frontends / diagnostics:
  DisplayProjection            # time/date and HP-41 screen messages
  KeyboardProjection           # input routed through historical 41 state
  FixtureRunner                # source-linked emulator/device comparison
~~~

### 14.1 Entwurfsbedingungen

1. **Unabhängige Zeitdomänen:** „echte“ Uhr, Stoppuhrmonotonicität und eingegebene numerische Datumswerte dürfen nicht vermischt werden.
2. **HP-41-Registersemantik:** Ein 41er-Register besitzt historisch 56 Bit Rohinhalt; der aktuelle generische C++-`double`-RPN-Stack gilt **nicht** als fertige 41er-Abbildung.
3. **Getrennte Rechen- und Bedienebene:** Reine Kalenderalgorithmen können wiederverwendet werden; `SW`/`ALMCAT` und `XYZALM` gehören zur 41-spezifischen Zustandsmaschine.
4. **Ausschließlich kontrollierter virtueller Programmaufruf:** Alarm-triggerbare Funktionen werden registriert und gemäß erlaubtem Modell ausgeführt, niemals über Host-Funktionszeiger oder beliebige Betriebssystemkommandos.
5. **Sichere Persistenz:** Mit laufenden virtuellen Timern umgehen, veraltete Zustände migrieren, ausstehende Alarme nicht durch unbeabsichtigtes Wiederherstellen duplizieren.
6. **Offlinefähigkeit:** Grundberechnungen, Stoppuhr und rein lokale Alarmverwaltung benötigen keinen Server, keine Cloud oder Netzwerkanmeldung.
7. **Revisionsprofile:** Original 82182A, HP-41C/41CV und spätere CX-Funktionen im Manifest getrennt ausweisen.
8. **Keine künstliche Produktverpflichtung:** iOS-Betriebssystem-Benachrichtigungen und Ausführung im Hintergrund können ein **späteres, separat geprüftes** Thema sein; die historische Dokumentation ordnet keine automatisch verfügbaren iOS-Privilegien an.
9. **Fehlerbehandlung:** Moderne Eingabevalidierung darf nicht unbemerkt HP-spezifische Fehleranzeigen, Stack-Lift- und Registernebenwirkungen überschreiben; K1/K2 nur mit Tests.
10. **Komponentenreife:** Wiederverwendung aus SASD Math Toolkit nur bei einer tatsächlich vorhandenen, stabilen, C++-fähigen und lizenzkompatiblen API.

### 14.2 Zustandsübergänge, die später als Tests zu formalisieren sind

~~~text
ClockDisplay:        Normal -> CLOCK -> CLOCK_ACTIVE -> Normal
Stopwatch:           STOPPED <-> RUNNING
StopwatchKeyboard:   NORMAL -> SW_ACTIVE -> NORMAL
StopwatchView:       LIVE <-> SPLIT_RECALL
Alarm:               PENDING -> DUE -> ACKNOWLEDGED/REMOVED
                                    -> OVERDUE/REPEATING
AlarmCatalog:        NORMAL -> LISTING -> PAUSED -> LISTING/NORMAL
ProgramControl:      RUNNING -> interrupt/defer -> controlled virtual call
~~~

**Nicht als historisch endgültige Zustandsgraphen missverstehen.** Der Alarmautomat muss vor Implementierungsabnahme aus Anhang D und am Original beobachteten Traces verfeinert werden; reale Alarmtypen unterscheiden sich.

## 15. Offene Detailprüfungen und konkrete nächste Arbeit

| Priorität | Prüfauftrag | Abnahmekriterium |
| --- | --- | --- |
| P1 | Für **alle 29** Befehle gedruckte HP-Seiten, Stack-Lift/Drop, LAST X, Anzeigen, Eingabemodi und Flags erfassen. | 29 ausgefüllte Einzeltraces, mit Quellenstelle und Revisionsstand. |
| P1 | Alarmzustandsgraph aus Handbuch Abschnitt 4 / Anhang D inklusive Quittierung, Wiederholung, Überfälligkeit und ON-Bedingungen spezifizieren. | Statechart, deterministische Zustandsübergangstests, mehrere gleichzeitige Alarme. |
| P1 | `SW`- und `ALMCAT`-Keyboard-Wirkung vollständig pro Taste und Shift-Zustand protokollieren. | Original-Trace pro Interaktion, keine fehlende Kontexttaste. |
| P1 | HP-Datums-/Zeit-Kodierung und strenge Feldgrenzen der verschiedenen Befehle festlegen. | Umkehrbare Parser-/Formatter-Tests inkl. 1582, 1900, 2000, 2199, 4320. |
| P1 | `SETIME` vs. `CORRECT`/`SETAF` inklusive Accuracy-Formel, Sekundenauflösung und Grenzfehler differenzieren. | dokumentierte reale Eingabe-Ausgabe-Paare. |
| P1 | Gemeinsame historische Register-/Programmspeicherbelegung, `Rnn/Dnn`-Zeiger, Alarmkapazität und Modul-/Gerätevarianten prüfen. | fehlerfreie virtuelle Speicherzugriffe, reproduzierbare Grenztests. |
| P2 | Gedruckte HP-Fehlerliste aus Anhang B pro Befehl auswerten. | konsistenter Fehlerkatalog mit Fehlermeldung, Trigger und Seiteneffekten. |
| P2 | `SETALM`, `ALMREL`, `ADOW`, `SPLITS` als **eigene** kompatible FOCAL-Tests neu schreiben. | rechtlich saubere, unabhängig erstellte Testprogramme. |
| P2 | HP-41CX-Zusatzbefehle `26,31…35` gesondert aus 41CX-Manual prüfen. | separate CX-Funktions-/Quellenliste. |
| P2 | Sachlich zulässige historische Testberichte/ROM-Revisionen für Geräte- und Emulatortests dokumentieren. | „supported/partial/unsupported/untested“ mit Commit und Geräteprofil. |
| P3 | Optionales mobiles UI für Stoppuhr/Alarm entwerfen, ohne V1-Keymap umzudefinieren. | eigener Produktbeschluss; Classic-V1-Release unberührt. |

### 15.1 Priorisierte Umsetzung (kein Veröffentlichungstermin)

| Stufe | Ziel | Abhängigkeit |
| --- | --- | --- |
| **T0 – Inventar** | Dieses Dokument, 29 XROM-Befehle, Quellen- und Prüfungsmatrix. | keine |
| **T1 – Reine Kalenderkernfunktionen** | Datumsparser, Kalenderarithmetik, `DOW`, `DDAYS`, `DATE+`; unabhängige Unit-Tests. | Datums-/Numerikentscheidung |
| **T2 – Virtuelle Uhr/Codec** | `TIME`, `DATE`, `SETIME`, `SETDATE`, `T+X`, `CLOCK`, `CLK12/24`, `CLKT/CLKTD`, `SETAF`, `RCLAF`, `CORRECT`. | T1 und simulierte Zeitquelle |
| **T3 – Stoppuhr** | fünf XROM-Befehle, `SW`-Tasten, Zeiger und Zwischenzeitspeicher. | virtuelle Register-/Tastenadapter |
| **T4 – Alarmverwaltung** | `XYZALM`, `ALMCAT`, `ALMNOW`, Quittierung, Wiederholung und Zustandswiederherstellung. | historischer FOCAL-/Interruptvertrag |
| **T5 – Historisches Fidelity-Gate** | sämtliche 29 Aufrufe, Zustandsabläufe, Fehlermeldungen und Originalbeispiele gegen legitimierte Referenz testen. | T1–T4 |
| **T6 – optionale CX-Erweiterung** | fünf CX-only-Zeitbefehle, eigenständige Profil- und Abnahmeunterlagen. | CX-Quellen, gesonderter Scope |

Dieses Forschungsdokument **autorisiert keine Änderung an Classic RPN V1**, keine Integration proprietärer ROMs und keine automatische Hochstufung eines Kompatibilitätsgrades. Die bindende Projektpriorität bleibt eine getestete, klassische iPhone-RPN-Anwendung.

## 16. Formale Abnahmeliste der späteren historischen Nachbildung

- [ ] **Genau 29 öffentliche Time-Module-Befehle** `26,01…26,29` mit eindeutigen Namen und Referenz-ID erfasst.
- [ ] Header `26,00` / `26,30` und fünf CX-only-Befehle getrennt.
- [ ] Alle QRC-Tastenzuordnungen von `SW` und `ALMCAT` getestet; `ON` korrekt als Sonderbedienung.
- [ ] Datumsbereiche, MDY/DMY, Flag 31, 12-/24h, ALPHA-Formatierung, Stunden/Minuten/Sekunden/Fraction parsergetreu.
- [ ] Kalenderwerte mit gregorianischen Prüfreferenzen einschließlich Randjahren getestet.
- [ ] Uhrzeiteinstellung, `T+X` und Gangkorrektur mit kontrollierter Tickquelle getestet.
- [ ] Stoppuhr-Registerzeiger, Zeitdifferenz, Zwischenzeit und Rückruf bis zur dokumentierten Speichergrenze geprüft.
- [ ] Akustische, Melde-, unterbrechende, nichtunterbrechende, einmalige und periodische Alarme inklusive Überfälligkeit nachvollzogen.
- [ ] Keine Host-Befehlsausführung durch historischen Programmalarm möglich.
- [ ] Persistenz/Restore mit offenen Alarmen, Stoppuhr und aktuellen Programmzeigern getestet.
- [ ] Original-Testtraces mit nachvollziehbarer Quelle, Gerät/ROM-Version, Test-ID und Commit vorhanden.
- [ ] Historische und moderne Abweichungen öffentlich und explizit dokumentiert.
- [ ] Fremde Manual-/ROM-/VASM-/Barcode-Inhalte nicht unautorisiert in Releases enthalten.
- [ ] Keine Blockade oder Regression der ersten iPhone-Classic-RPN-Version.

## 17. Pflege, Status und Verweise

**Erfasst am 23.11.2026:** Namen/XROM-Schema und QRC-Tastaturbelegung aus HP-Originalquellen; historische Rahmenbedingungen aus deutscher HP-Dokumentation und CX-Zuordnung aus gedruckter HP-XROM-Tabelle. Die **Dokumentation ist umfangreich, aber nicht bereits eine vollständig geprüfte ROM-Verhaltensspezifikation**; offene Details sind im Text kenntlich gemacht. Es gibt **keine implementierten oder ausgeführten Time-Module-Golden-Tests**, weshalb eine 100%-Kompatibilitätsbehauptung unzulässig wäre.

- [HP-41C Grundfunktionskatalog](HP-41C-FUNKTIONSKATALOG.md)
- [HP-41C Stat Pac](HP-41C-STAT-PAC.md)
- [HP-41 Historical Compatibility Plan](../en/HISTORICAL-41.md)
- [Compatibility Evidence Rules](../en/COMPATIBILITY.md)
- [AGENTS.md](../../AGENTS.md)
- [Roadmap](../../ROADMAP.md)
- [Historisches Original-Handbuch, Deutsch (externes PDF)](https://literature.hpcalc.org/community/hp82182a-om-de.pdf)
