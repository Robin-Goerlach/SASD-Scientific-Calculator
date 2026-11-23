# HP-41C Stat Pac – Funktionsinventar und Nachbildungs-Spezifikation

**Dokument-ID:** SASD-SCI-HP41-STAT-001  
**Stand:** 2026-11-23 · **Sprache:** Deutsch · **Version:** 1.0 (Recherche-/Planungsstand)  
**Historisches Ziel:** Hewlett-Packard HP-41C *Stat Pac* (Statistik-Anwendungsmodul), mit gesonderter Prüfung auf HP-41CV/41CX  
**Repository:** [SASD Scientific Calculator](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator)  
**Status:** **Dokumentiert / geplant / noch nicht implementiert oder historisch zertifiziert**  
**Zielrelease:** späterer historischer HP-41-Funktions-/Programmtrack; **kein Blocker für die iPhone-Classic-V1.0**.

> **Wichtig:** Dieses Dokument bildet das vollständige **öffentlich dokumentierte Funktionsinventar** des historischen HP-41C Stat Pac ab: **14 Programmgruppen und 24 benannte XEQ-Einstiegspunkte** aus den HP-Original-Kurzanleitungen. Es ist eine **eigenständig formulierte Entwicklungsgrundlage**, kein Abdruck des Handbuchs und noch **keine byte- oder numerisch nachgewiesene ROM-Reimplementierung**. Unbestätigte Details sind ausdrücklich mit `OFFEN` gekennzeichnet. Eine vollständige, abnahmefähige Nachbildung erfordert zusätzlich eine systematische Auswertung der Benutzeranweisungen im 80-seitigen Originalhandbuch, Referenzdurchläufe und Tests aller Seiteneffekte.

## 1. Zweck, Geltungsbereich und Statuswörter

Das Modul ergänzt den bereits vorhandenen [Katalog des serienmäßigen HP-41C](HP-41C-FUNKTIONSKATALOG.md). Es ist **kein** Teil der ab Werk vorhandenen 41C-Befehle. Diese Datei ist das zukünftige Lasten-/Spezifikationsinventar für eine unabhängige Implementierung im SASD Scientific Calculator, einschließlich dokumentierter Bedienung, numerischer Funktionen, Register- und Stackzustände sowie Fehlerfällen.

Die historischen Namen dienen hier ausschließlich der technischen Identifizierung des zu untersuchenden Drittanbieterprodukts; SASD wird nicht als Hewlett-Packard-Produkt ausgegeben.

| Begriff | Bedeutung in dieser Datei |
| --- | --- |
| **QRC-bestätigt** | Name, Eingabeschema, Größe oder Tastenfolge ist auf einer HP-Original-Kurzanleitung ablesbar. |
| **Handbuchbelegt** | Spezifisches Detail wurde in einem konkret bezeichneten Abschnitt des HP-Originalhandbuchs gefunden. |
| **Mathematisches Modell** | Unabhängig formulierte fachliche Spezifikation, **noch keine Behauptung**, dass die historische ROM-Routine diese numerische Methode exakt so verwendet. |
| **OFFEN** | Originalverhalten, Ausnahmefall, Rundung, Ausgabe oder Variantenunterschied muss noch überprüft werden. |
| **GEPLANT** | Vorgesehener SASD-Implementierungsumfang ohne Implementierungs- oder Testergebnis. |
| **GETESTET** | Nur zulässig mit Test-ID, konkreter Quelle/Fixture, Gerät/Emulator, Version und Commit. **Zurzeit kein Eintrag dieses Dokuments GETESTET.** |

Unbedingt unterscheiden: **14 thematische Programmeinheiten** ≠ **24 XEQ-Aufrufe** ≠ Anzahl möglicher interner ROM-Labels, Rückgabewerte, mathematischer Teiloperationen oder ROM-Bytes. Zahlen zu **30 ROM-Marken** aus Sekundärangaben sind **nicht unabhängig bestätigt** und werden **nicht** als gesicherte Modul-Schnittstelle übernommen.

### 1.1 Nicht enthalten

- Andere HP-41-Pacs, das Math Pac, das Advantage Pac, das Time Module, HP-41CX-Systemerweiterungen und reine Grundgerät-Funktionen.
- `RAND`/`SEED` als angebliche Funktionen **dieses** Original-Stat-Pac: auf der geprüften Original-Kurzanleitung **nicht enthalten**; Drittanbietererweiterungen sind getrennt zu führen.
- Historische ROM-Binärdateien, proprietäre Maschinenprogramme und unverändert übernommene Handbuchseiten.
- Behauptete vollständige 41C-, FOCAL-, Synthetic- oder Nut-CPU-Kompatibilität.

## 2. Primär- und Vergleichsquellen

| ID | Quelle | Ausweis / Umfang | Verwendung |
| --- | --- | --- | --- |
| **HP-ST-EN** | [HP-41 Stat Pac – englisches Originalhandbuch (PDF)](https://literature.hpcalc.org/community/hp41-pac-stat-en.pdf) | HP `00041-90030`, Rev. E, August 1984, 80 Seiten | Primärquelle für Erläuterungen, Formeln, Benutzeranweisungen, Ergebnisfolgen, Beispiele und Anhänge. |
| **HP-ST-DE** | [HP-41 Stat Pac – deutsches Originalhandbuch (PDF)](https://literature.hpcalc.org/community/hp41-pac-stat-de.pdf) | HP `00041-90031`, 80 Seiten; Ausgabestand gesondert zu überprüfen | Deutsche Terminologie; Gegenprüfung der Programmbeschreibungen. |
| **HP-QRC-EN** | [HP-41C Stat Pac Quick Reference Card (PDF)](https://literature.hpcalc.org/community/hp41-pac-stat-qrc-en.pdf) | HP `00041-90061`, Juni 1979, 2 Seiten | **Durch Sichtprüfung bestätigt:** 14 Gruppen, 24 Aufrufe, `SIZE` und grobe Tastenfolgen. |
| **HP-QRC-DE** | [HP-41C Kurzanleitung Statistik-Paket (PDF)](https://literature.hpcalc.org/community/hp41-pac-stat-qrc-de.pdf) | HP `00041-90062`, Dezember 1979, 2 Seiten | Gegenprüfung der Namen, deutschen Begriffe und Eingabemuster. |
| **SASD-41-BASE** | [41C-Grundfunktionskatalog](HP-41C-FUNKTIONSKATALOG.md) | SASD-Dokumentation | Abgrenzung zu `Σ+`, `Σ−`, `MEAN`, `SDEV`, `ΣREG` etc. |
| **SASD-41-PLAN** | [Series-41-Kompatibilitätsplanung](../en/HISTORICAL-41.md) | SASD-Architekturziel | Isolation von historischem Stack, Registerbild, FOCAL und Moduladapter. |
| **SASD-COMPAT** | [Evidenz- und Kompatibilitätsregeln](../en/COMPATIBILITY.md) | SASD-Qualitätskriterien | K1–K4, Quellenqualität und Nachweis gegen echte Referenzen. |

Ergänzende **Vergleichs- und Werkzeugquellen**, ausdrücklich **keine** Ersatz-Primärquellen: [HP Calculator Literature Archive](https://literature.hpcalc.org/), [V41](https://hp.giesselink.com/v41.htm), [Emu41](https://www.jeffcalc.hp41.eu/emu41/index.html), [HP-41 Module Database](https://calc.fjk.ch/db/hp41mod.php). Ob konkrete Emulatoren die benötigte Stat-Pac-ROM-Version rechtmäßig und korrekt ausführen, ist vor Einsatz zu klären.

**Quellenregel:** Bei Differenzen zwischen deutschem OCR-Text und Originalabbildung gilt die **sichtbar gedruckte Vorlage**, nicht eine automatische Texterkennung. Beispielsweise wird die Aufrufmarke `ΣMLRXYZ` in der englischen und deutschen Originalabbildung verwendet; eine OCR-Variante `ΣMLRYZ` ist keine zusätzliche Funktion. Entsprechendes gilt für `ΣANOCOV` (nicht die künstliche Trennung `ΣANO COV`).

### 2.1 Noch ausstehende vertiefte Quellenprüfung

Die beiden 80-seitigen Scans sind als Originalquellen **gefunden**, aber für diese Dokumentfassung **nicht Seite für Seite vollständig gegen sämtliche Details ausgewertet**. Deshalb beschränkt sich die Einstufung `QRC-bestätigt` auf die tatsächlich geprüften Karten; Formeln ohne expliziten Handbuchabgleich heißen unten **mathematisches Modell**. Keine nicht beobachteten HP-Beispielwerte oder ROM-Grenzen werden als gesicherte Fakten ausgegeben.

Für die Implementierungsfreigabe je Aufruf sind aus **HP-ST-EN und HP-ST-DE** nachzutragen: gedruckte Seitenzahl, Ergebnisreihenfolge mit Displaytext, Datenregister-/Flagschema, Stackwirkung, Fehlermeldungen, genaue Definition von Stichproben-/Populationsformeln, Grenzwerte und mindestens ein vollständig nachgespielter Originalfall.

## 3. Vollständiger öffentlicher XEQ-Katalog

**Alle 24 Aufrufe sind QRC-bestätigt; alle SASD-Implementierungsstände sind GEPLANT.**

| ID | Gruppe | Historischer `XEQ`-Name | Kurzfunktion | `SIZE` |
| --- | --- | --- | --- | ---: |
| ST-01 | Basisstatistik | `ΣBSTAT` | Zwei Variablen, ungruppierte Wertepaare | 012 |
| ST-02 | Basisstatistik | `ΣBSTG` | Zwei Variablen, Häufigkeiten/Gruppen | 012 |
| ST-03 | Momente | `ΣMMTUG` | Ungewichtete Momente, Schiefe, Kurtosis-/Exzessgröße | 012 |
| ST-04 | Momente | `ΣMMTGD` | Momente mit Häufigkeiten | 012 |
| ST-05 | Varianzanalyse | `ΣAOVONE` | Einfaktorielle ANOVA | 020 |
| ST-06 | Varianzanalyse | `ΣAOVTWO` | Zweifaktorielle ANOVA ohne Wiederholungen | 018 |
| ST-07 | Kovarianzanalyse | `ΣANOCOV` | Einfaktorielle ANCOVA | 026 |
| ST-08 | Kurvenanpassung | `ΣLIN` | Linearer Fit | 016 |
| ST-09 | Kurvenanpassung | `ΣEXP` | Exponentieller Fit | 016 |
| ST-10 | Kurvenanpassung | `ΣLOG` | Logarithmischer Fit | 016 |
| ST-11 | Kurvenanpassung | `ΣPOW` | Potenz-Fit | 016 |
| ST-12 | Multiple Regression | `ΣMLRXY` | Zwei Prädiktoren, Zielvariable `t` | 045 |
| ST-13 | Multiple Regression | `ΣMLRXYZ` | Drei Prädiktoren, Zielvariable `t` | 045 |
| ST-14 | Polynomregression | `ΣPOLYP` | Quadratisches Polynom | 045 |
| ST-15 | Polynomregression | `ΣPOLYC` | Kubisches Polynom | 045 |
| ST-16 | t-Statistik | `ΣPTST` | Gepaarter t-Test | 015 |
| ST-17 | t-Statistik | `ΣTSTAT` | Unabhängiger Zweistichproben-t-Test | 015 |
| ST-18 | Chi-Quadrat | `ΣXSQEV` | Anpassungstest mit individuellen Erwartungswerten | 008 |
| ST-19 | Chi-Quadrat | `ΣEEFXSQ` | Anpassungstest bei gleicher Erwartungshäufigkeit | 008 |
| ST-20 | Kontingenztabelle | `ΣCTKK` | 2 × k-Tabelle | 015 |
| ST-21 | Kontingenztabelle | `ΣCTKKK` | 3 × k-Tabelle | 015 |
| ST-22 | Rangstatistik | `ΣSPEAR` | Spearman-Rangkorrelation | 003 |
| ST-23 | Normalverteilung | `ΣNORMD` | Dichte, obere Restwahrscheinlichkeit, Quantil | 019 |
| ST-24 | Chi-Quadrat-Verteilung | `ΣCHISQD` | Dichte und untere Verteilungsfunktion | 007 |

**Prüfsumme des Inventars:** 2 + 2 + 1 + 1 + 1 + 4 + 2 + 2 + 2 + 2 + 2 + 1 + 1 + 1 = **24 Aufrufe in 14 Gruppen**.

### 3.1 Bedeutung von `SIZE`

Die historische Karte bezeichnet `SIZE 012` usw. als **minimale HP-41-Datenregister-Konfiguration** für die jeweilige Programmroutine, **nicht** als ROM-Größe, Bytezahl, Anzahl der Benutzerdaten oder Anzahl der Ergebniswerte. Die Erfordernisse können durch konkurrierende Programme, Registerbelegung und `ΣREG` beeinflusst werden: **OFFEN: exakte Wechselwirkung pro Programm**.

## 4. Bedientasten und allgemeiner Ablauf

Die HP-Kurzanleitung unterscheidet für die meisten Programme die Phasen **Initialisierung → Dateneingabe → Korrektur → Ergebnisse → Wiederinitialisierung**.

- Aufruf eines der oben stehenden Modulprogramme: `XEQ` gefolgt von dem historischen Programmnamen; die Eingabe des führenden `Σ` ist je nach echter Tastatur-/ALPHA-Bedienung zu erfassen.
- **A**: im jeweils angegebenen Programm typischerweise Datensatz hinzufügen oder Initialisierung auslösen, aber **kein universeller A-Befehl**.
- **C**: vorhandenen Datensatz gemäß dem pro Programm vorgeschriebenen Eingabeschema korrigieren/abziehen; bei den Verteilungsprogrammen eine andere Funktion.
- **E**: Ergebnisberechnung beginnen oder eine programmspezifische Verteilungsoperation ausführen.
- **R/S**: bei mehrteiligen Verfahren Ergebnisanzeige fortsetzen oder programmatisch zur nächsten Eingabephase wechseln.
- **Neuinitialisierung:** Die Kurzanleitung kennzeichnet für zahlreiche Programme die Kombination aus einer **Shift-Taste** und **A**; die genaue Tastenbelegung und resultierende Registerlöschung sind **OFFEN**. Für `ΣNORMD` und `ΣCHISQD` zeigt die Karte keine solche allgemeine Neuinitialisierung.
- **Stack/Eingabe:** `x ENTER↑ y A` ist ein **historischer Tastendialog** und nicht gleichbedeutend mit einem modernen API-Aufruf `add(x,y)`: erst der Programmstatus legt fest, wo Werte gelesen werden.

> **Implementierungsgebot:** HP-41-Pac-Tastenfolgen sind eine **eigene Zustandsmaschine**. Historische Verhaltenskompatibilität darf nicht allein durch das Bereitstellen mathematischer Funktionen oder UI-Schaltflächen behauptet werden.

### 4.1 Verifizierte Eingabeschemata der Kurzanleitung

| Gruppe / Aufrufe | Datenaufnahme mit A | Korrektur mit C | Ergebnisstart | Wiederholung/Prognose |
| --- | --- | --- | --- | --- |
| `ΣBSTAT` | `x ENTER↑ y A` | `x ENTER↑ y C` | `E` | `R/S` mehrfach |
| `ΣBSTG` | `x ENTER↑ y ENTER↑ f A` | gleicher Datensatz, `C` | `E` | `R/S` mehrfach |
| `ΣMMTUG` | `x A` | `x C` | `E` | fünfmal `R/S` |
| `ΣMMTGD` | `x ENTER↑ f A` | gleiches Paar, `C` | `E` | fünfmal `R/S` |
| `ΣAOVONE` | `xᵢⱼ A` | `xᵢₘ C` | `E` | `R/S`; mehrere Steuerphasen |
| `ΣAOVTWO` | `xᵢⱼ A`, zeilen- oder spaltenweise | `xᵢⱼ C` | `E` | `R/S`; phasenabhängig |
| `ΣANOCOV` | `xᵢⱼ ENTER↑ yᵢⱼ A` | gleiches Paar, `C` | `E` | `R/S`; phasenabhängig |
| `ΣLIN` / `ΣEXP` / `ΣLOG` / `ΣPOW` | `x ENTER↑ y A` | gleiches Paar, `C` | `E` | `R/S`, danach `x R/S` → Prognose |
| `ΣMLRXY` | `x ENTER↑ y ENTER↑ t A` | gleiches Tripel, `C` | `E` | `R/S`, `x ENTER↑ y R/S` → `t` |
| `ΣMLRXYZ` | `x ENTER↑ y ENTER↑ z ENTER↑ t A` | gleiches Quadrupel, `C` | `E` | `R/S`, `x ENTER↑ y ENTER↑ z R/S` → `t` |
| `ΣPOLYP` / `ΣPOLYC` | `x ENTER↑ y A` | gleiches Paar, `C` | `E` | `R/S`, `x R/S` → Prognose |
| `ΣPTST` | `x ENTER↑ y A` | gleiches Paar, `C` | `E` | `R/S` mehrfach |
| `ΣTSTAT` | `x A`, `R/S` → weitere erste Stichprobe; `y A` → zweite | `x C` / `y C` phasenabhängig | `d E` | `R/S` |
| `ΣXSQEV` | `O ENTER↑ E A` | gleiches Paar, `C` | `E` | — |
| `ΣEEFXSQ` | `O A` | `O C` | `E` | `R/S` |
| `ΣCTKK` | `x₁ⱼ ENTER↑ x₂ⱼ A` | gleiches Paar, `C` | `E` | fünfmal `R/S` |
| `ΣCTKKK` | `x₁ⱼ ENTER↑ x₂ⱼ ENTER↑ x₃ⱼ A` | gleiches Tripel, `C` | `E` | fünfmal `R/S` |
| `ΣSPEAR` | `R ENTER↑ S A` | gleiches Rangpaar, `C` | `E` | `R/S` |
| `ΣNORMD` | keine Datenaufnahmephase | keine Datenkorrekturphase | `x C` → Dichte; `x E` → `Q(x)`; `Q A` → `x` | — |
| `ΣCHISQD` | `ν A` (Freiheitsgrade) | keine Datenkorrekturphase | `x C` → Dichte; `x E` → `P(x)` | — |

**Grenze dieser Tabelle:** Wo die Karte nur mehrere `R/S` zeigt, ist die exakte Programmschrittfolge noch **nicht** vollständig beschrieben. Die genaue Reihenfolge ist in den betreffenden HP-Handbuchabschnitten zu protokollieren, statt sie aus einer typischen modernen Statistik-API zu erraten.

## 5. Mathematische Begriffe und Konventionen

Im Folgenden gelten bei ungewichteten Daten `n` Beobachtungen `(xᵢ,yᵢ)`; bei Häufigkeiten `fᵢ` und `N = Σ fᵢ`. Es sind mathematische Referenzformeln für die **spätere Implementierungs- und Testarbeit**. Die historische Rundung, Akkumulationsreihenfolge, Dezimalpräzision und Sonderfallbehandlung sind eigenständig zu ermitteln.

### 5.1 Basisstatistik (ST-01, ST-02)

**ST-01 – `ΣBSTAT`, ungruppiert (SIZE 012)**

- **Eingabe:** geordnete Beobachtungspaare `(xᵢ,yᵢ)`; `A` addiert, `C` korrigiert.
- **Zu rekonstruierende Ausgaben:** Mittelwerte, Summen/Quadrat- und Produktsummen, Stichproben- und Populationsstandardabweichungen, Kovarianzen, Pearson-Korrelationskoeffizient und Variationskoeffizienten. **OFFEN:** sämtliche historischen Displaytexte und deren genaue Ausgabeordnung.
- **Referenzformeln:** `x̄ = Σxᵢ/n`, `ȳ = Σyᵢ/n`; `Sxx = Σxᵢ² − (Σxᵢ)²/n`; `Syy` analog; `Sxy = Σxᵢyᵢ − (Σxᵢ)(Σyᵢ)/n`; `sₓ = √(Sxx/(n−1))`; `σₓ = √(Sxx/n)`; `r = Sxy/√(Sxx·Syy)`; Stichprobenkovarianz `Sxy/(n−1)`. Die alternative Populationskovarianz `Sxy/n` ist getrennt zu behandeln.
- **Randfälle:** `n=0/1`, `Sxx=0`, `Syy=0`, sehr große Eingaben und instabile Subtraktion großer Summen.

**ST-02 – `ΣBSTG`, gruppiert/gewichtet (SIZE 012)**

- **Eingabe:** Tripel `(xᵢ,yᵢ,fᵢ)`, wobei `fᵢ` eine Häufigkeit ist.
- **Referenzformeln:** `N = Σfᵢ`, `x̄ = Σfᵢxᵢ/N`, `ȳ = Σfᵢyᵢ/N`, `Sxy = Σfᵢxᵢyᵢ − (Σfᵢxᵢ)(Σfᵢyᵢ)/N`; weitere Größen entsprechend gewichtet.
- **Offen:** Erlaubte Häufigkeiten (ganzzahlig/nichtganzzahlig, null/negativ), Verwendung von `N` bzw. Zahl der Klassen als Stichprobenumfang, Ergebnisfolge, Korrektur nicht vorhandener Tripel.

### 5.2 Momente und Schiefe (ST-03, ST-04)

**ST-03 – `ΣMMTUG`, ungruppiert (SIZE 012)**

- **Eingabe:** Einzelwerte `xᵢ`.
- **QRC-/Handbuch-Ausgabe:** `XBAR`, `M2`, `M3`, `M4`, `GM1`, `GM2`; Beginn mit `E`, danach fünfmal `R/S`.
- **Referenz:** `mₖ = (1/n) Σ(xᵢ−x̄)^k` für `k=2,3,4`; standardisierte Schiefe `γ₁ = m₃/m₂^(3/2)`.
- **Wichtig – Exzesskonvention OFFEN:** Englisch nennt die letzte Größe *kurtosis*, Deutsch *Exzess*. Es ist **explizit gegen die Originalformel zu prüfen**, ob `GM2` als `m₄/m₂²` oder `m₄/m₂²−3` berechnet wird. Diese Varianten sind nicht austauschbar.

**ST-04 – `ΣMMTGD`, gruppiert (SIZE 012)**

- **Eingabe:** Wert und Häufigkeit `(xᵢ,fᵢ)`.
- **Referenz:** `mₖ = Σ fᵢ(xᵢ−x̄)^k/N`; dieselben sechs Ergebniskategorien wie ST-03.
- **Offen:** Häufigkeits- und Nullvarianzregeln, `GM2`-Definition, historisches Abziehen eines zuvor erfassten Wertes.

### 5.3 Varianz- und Kovarianzanalyse (ST-05 bis ST-07)

**ST-05 – `ΣAOVONE`, einfaktorielle ANOVA (SIZE 020)**

- **Eingabe:** Beobachtungen nach Gruppe; die mehrfachen `R/S`-Schritte nach einer Aufnahme dienen der historisch festgelegten Gruppensteuerung. **OFFEN:** exakter Phasenautomat.
- **Modell:** `xᵢⱼ = μ + αᵢ + εᵢⱼ`, `k` Gruppen, `N` Beobachtungen.
- **Berechnungen:** Gruppenmittelwerte und -streuungen, `SS_between = Σ nᵢ (x̄ᵢ−x̄)²`, `SS_within = ΣΣ(xᵢⱼ−x̄ᵢ)²`, `SS_total = SS_between+SS_within`, Freiheitsgrade `k−1` und `N−k`, `F = (SS_between/(k−1))/(SS_within/(N−k))`.
- **Offen:** Gedruckte Ergebnisliste/Displaytexte, Freiheitsgradgrenzen, Gruppenanzahl, Reihenfolge der Zwischenwerte.

**ST-06 – `ΣAOVTWO`, zweifaktorielle ANOVA ohne Wiederholungen (SIZE 018)**

- **Eingabe:** Matrix `xᵢⱼ`, **entweder zeilenweise oder spaltenweise** nach Originalbenutzeranweisung; kein repliziertes Zellendesign.
- **Referenz bei `r` Zeilen, `c` Spalten:** `SS_total = ΣΣ(xᵢⱼ−x̄)²`; `SS_row = cΣ(x̄ᵢ·−x̄)²`; `SS_col = rΣ(x̄·ⱼ−x̄)²`; `SS_error = SS_total−SS_row−SS_col`. Freiheitsgrade `r−1`, `c−1`, `(r−1)(c−1)`. Je ein F-Quotient gegenüber `MS_error`.
- **Besonderheit:** Bei einer Beobachtung pro Zelle ist die Interaktion nicht separat schätzbar. **OFFEN:** genaues HP-Modell und Randbedingungen.

**ST-07 – `ΣANOCOV`, einfaktorielle ANCOVA (SIZE 026)**

- **Eingabe:** Gruppen mit Wertepaaren (Kovariate `xᵢⱼ`, Antwort `yᵢⱼ`); nach Eingabe folgen gruppenbezogene `R/S`-Phasen.
- **Mathematisches Modell:** `yᵢⱼ = μ + αᵢ + β(xᵢⱼ−x̄) + εᵢⱼ` mit gemeinsamer Steigung als prüfbare Modellannahme.
- **Berechnungen:** Gesamte, gruppenbezogene und innerhalb der Gruppen liegende Quadratsummen für X/Y (`TSSX/ASSX/WSSX` und `TSSY/ASSY/WSSY`), Produktsummen (`TSP/ASP/WSP`), unkorrigierte F-Statistiken und nach Kovariatenkorrektur berechnete Quadratsummen/Mittlere Quadratsummen/F-Statistik.
- **Referenzansatz:** `SS_yy,adj = SS_yy − SS_xy²/SS_xx` in der jeweiligen Zerlegung, jedoch **nicht** ohne Prüfung auf das exakte HP-ANCOVA-Testschema übertragen.
- **Offen:** Reihenfolge der beschrifteten Ergebnisse, gemeinsame Steigung, Freiheitsgrade, Null-/Singularitätsfälle.

### 5.4 Einfache Kurvenanpassungen (ST-08 bis ST-11; SIZE 016)

Alle vier Routinen nehmen `(x,y)`-Paare auf (`A`), korrigieren mit `C` und starten Ergebnisse mit `E`; `R/S` zeigt weitere Resultate bzw. nimmt für eine Vorhersage einen neuen `x`-Wert entgegen. Typische Ausgaben sind Modellparameter und Anpassungsgüte, **OFFEN:** exakte historische Ausgabefolge und `R²`-Definition je transformiertem Modell.

| ID | Aufruf | Modell | Übliche Linearisierung für die mathematische Referenz | Für den Referenztest kritisch |
| --- | --- | --- | --- | --- |
| ST-08 | `ΣLIN` | `y=a+bx` | OLS direkt auf `(x,y)` | Vertikale Linie, konstantes y, `Sxx=0`. |
| ST-09 | `ΣEXP` | `y=a·exp(bx)` | `ln(y)=ln(a)+bx` | `y>0`; Fit im Lograum ist nicht identisch mit nichtlinearer OLS im Originalraum. |
| ST-10 | `ΣLOG` | `y=a+b·ln(x)` | `u=ln(x)` | `x>0`. |
| ST-11 | `ΣPOW` | `y=a·x^b` | `ln(y)=ln(a)+b ln(x)` | Üblicherweise `x>0` und `y>0`, genaues HP-Domain-Verhalten offen. |

**Referenz für ST-08:** `b=Sxy/Sxx`, `a=ȳ−bx̄`, `ŷ(x)=a+bx` und `R²=r²` bei gewöhnlicher einfacher OLS-Regression mit Konstante.

**OFFEN:** Ob alle vier Aufrufe tatsächlich obige Transformationsverfahren verwenden, welche Fehler `x≤0`/`y≤0` erzeugen, welche Größe als Gütemaß ausgegeben wird und ob eine historische Näherung bei extremen Werten abweicht.

### 5.5 Multiple Regression (ST-12, ST-13; SIZE 045)

**ST-12 – `ΣMLRXY`**

- **Eingabe:** `(xᵢ,yᵢ,tᵢ)`.
- **Modell:** `t = a + bx + cy`; `(a,b,c)` als Koeffizienten von `(XᵀX)β=Xᵀt`.
- **Ausgaben:** Modellparameter, Anpassungsgröße(n) und Vorhersage `t̂` für `(x,y)`. Exakte historische Reihenfolge **OFFEN**.
- **Spezialfälle:** zu wenige Beobachtungen, perfekte Kollinearität, konstante Prädiktoren, degenerierte Normalgleichungen.

**ST-13 – `ΣMLRXYZ`**

- **Eingabe:** `(xᵢ,yᵢ,zᵢ,tᵢ)`.
- **Modell:** `t = a + bx + cy + dz`.
- **Ausgaben:** vier Koeffizienten, Gütewert(e), Vorhersage `t̂` für `(x,y,z)`; Anzeige- und Speicherfolge **OFFEN**.
- **Numerische Regel:** In der modernen, wiederverwendbaren SASD-Numerik dürfen QR-/SVD-Lösungen sinnvoll sein; **historischer HP-Verhaltensmodus** muss jedoch unabhängig gegen Referenzergebnisse und Singularitätsreaktionen getestet werden.

### 5.6 Polynomregression (ST-14, ST-15; SIZE 045)

**ST-14 – `ΣPOLYP`**

- **Eingabe:** `(xᵢ,yᵢ)`.
- **Modell:** `y=a+bx+cx²`. Drei Koeffizienten, Fit-/Prognosephase; genaue historische Ergebnisfolge **OFFEN**.
- **Sonderfälle:** weniger als drei unabhängige Stützstellen, doppelte x-Werte, Singularität, schlecht konditionierte Daten.

**ST-15 – `ΣPOLYC`**

- **Eingabe:** `(xᵢ,yᵢ)`.
- **Modell:** `y=a+bx+cx²+dx³`. Vier Koeffizienten, Fit-/Prognosephase; genaue historische Ergebnisfolge **OFFEN**.
- **Sonderfälle:** weniger als vier unabhängige Stützstellen, Singularität, stark skalierte x-Werte.
- **Beide:** Die Originalbeschreibung erwähnt die Lösung von Gleichungssystemen; **OFFEN:** präzise Pivotierungs-/Abbruchregel der tatsächlich verwendeten ROM-Version, das historische Fehlerdisplay und Zwischenwerte.

### 5.7 t-Statistik (ST-16, ST-17; SIZE 015)

**ST-16 – `ΣPTST`, gepaarte Stichproben**

- **Eingabe:** zusammengehörige Paare `(xᵢ,yᵢ)`, Korrektur des gesamten Paares.
- **Mathematisches Modell:** `dᵢ=xᵢ−yᵢ`; `t=(d̄−d₀)/(s_d/√n)` bei Hypothesen-Differenz `d₀`; Freiheitsgrade `n−1`.
- **Offen:** Ob `d₀` im historischen Programm fest null ist oder separat eingegeben wird; Richtungsdefinition der Differenzen; Reihenfolge von Mittelwert, Varianz, `t`, Freiheitsgrad.
- **QRC:** `E`, danach wiederholt `R/S`.

**ST-17 – `ΣTSTAT`, unabhängige Stichproben**

- **Eingabe:** erst X-Stichprobe mit `A` und `R/S`, dann Y-Stichprobe mit `A`; nach Datenabschluss vor `E` ein hypothesierter Unterschied `d`.
- **Referenzannahme:** klassischer Zweistichproben-t-Test mit **gleicher unbekannter Varianz** (pooled), **nicht** automatisch Welch.
- **Modell:** `s_p²=((n_x−1)s_x²+(n_y−1)s_y²)/(n_x+n_y−2)`; `t=((x̄−ȳ)−d)/(s_p√(1/n_x+1/n_y))`; `ν=n_x+n_y−2`.
- **Offen:** exakte statistische Konvention der HP-Routine und deren Displayfolge; insbesondere Korrektur und Umschalten zwischen zwei Datensätzen.

### 5.8 Anpassungs-/Chi-Quadrat-Tests (ST-18, ST-19; SIZE 008)

**ST-18 – `ΣXSQEV`, individuelle erwartete Häufigkeiten**

- **Eingabe:** pro Klasse beobachtet `Oᵢ` und erwartet `Eᵢ`, mit `A` und `C`.
- **Referenz:** `χ² = Σ (Oᵢ−Eᵢ)²/Eᵢ`.
- **Ausgabe laut QRC:** ein Ergebnisschritt über `E`.
- **Offen:** Fehlverhalten bei `Eᵢ≤0`, Konsistenz von `ΣO` und `ΣE`, Klassenanzahl, automatische Freiheitsgrade oder Signifikanz (in der Kurzanleitung nicht als eigene Ausgaben ausgewiesen).

**ST-19 – `ΣEEFXSQ`, gleiche erwartete Häufigkeit**

- **Eingabe:** nur beobachtete Klassenhäufigkeiten `Oᵢ`.
- **Referenz:** Für `k` Klassen `N=ΣOᵢ`, `E=N/k` und `χ²=Σ(Oᵢ−N/k)²/(N/k)`. Das ist die naheliegende Gleich-Erwartungs-Variante.
- **QRC-Ausgabe:** `E` und `R/S` (mindestens zwei Ergebnis-/Anzeigephasen).
- **Offen:** welcher der beiden Schritte `E` oder `χ²` liefert, Grenzen bei `N=0`, Korrektur/Neuberechnung.

### 5.9 Kontingenztabellen (ST-20, ST-21; SIZE 015)

**ST-20 – `ΣCTKK`, zwei Reihen × k Spalten**

- **Eingabe je Spalte:** `(n₁ⱼ,n₂ⱼ)`.
- **Referenz:** `eᵢⱼ=(rᵢcⱼ)/N` mit Zeilen-/Spaltensummen; `χ²=ΣΣ(nᵢⱼ−eᵢⱼ)²/eᵢⱼ`, Freiheitsgrade `(2−1)(k−1)=k−1`.
- **Ergebnisse:** Chi-Quadrat-Größe, Pearsons Kontingenzkoeffizient und Summen-/Zwischenergebnisse; genaue HP-Reihenfolge **OFFEN**.
- **Referenz-Koeffizient:** `C=√(χ²/(χ²+N))`.

**ST-21 – `ΣCTKKK`, drei Reihen × k Spalten**

- **Eingabe je Spalte:** `(n₁ⱼ,n₂ⱼ,n₃ⱼ)`.
- **Referenz:** derselbe Chi-Quadrat-Unabhängigkeitstest für 3×k, Freiheitsgrade `2(k−1)`; Koeffizient `C` analog.
- **Offen für beide:** Anwendung bei Nullerwartungen, Festlegung der Korrekturroutine, konkrete Reihenfolge von sechs `E`-/`R/S`-Ausgaben und Speicherung der Summen.

### 5.10 Rangkorrelation (ST-22; SIZE 003)

**ST-22 – `ΣSPEAR`**

- **Eingabe:** **bereits zugeordnete** Rangpaare `(Rᵢ,Sᵢ)`. Die Kurzanleitung enthält **keinen separaten automatischen Ranking-Befehl**.
- **Mathematisches Modell ohne Bindungen:** `dᵢ=Rᵢ−Sᵢ` und `r_s=1−6Σdᵢ²/[n(n²−1)]`. Allgemein mit Rangbindungen: Pearson-Korrelation der geeigneten (etwa mittleren) Ränge.
- **Ausgaben laut QRC:** zwei Schritte, `E` und `R/S`; Korrelationskoeffizient und approximative Testgröße. **OFFEN:** genaue Approximationsformel und Umgang mit gebundenen Rängen.
- **Abgrenzung:** Eine moderne automatische Rangsortierung darf **nicht** ohne eigene Spezifikation zum historischen `XEQ ΣSPEAR` hinzuerfunden werden.

### 5.11 Wahrscheinlichkeitsverteilungen (ST-23, ST-24)

**ST-23 – `ΣNORMD`, Normal- und inverse Normalverteilung (SIZE 019)**

Das Modul beschreibt die **Standardnormalverteilung** (Mittelwert 0, Streuung 1), nicht eine allgemein parametrisierte Normalverteilung.

- `x C` → Dichte `f(x) = exp(−x²/2)/√(2π)`.
- `x E` → **obere** Restwahrscheinlichkeit `Q(x)=∫_x^∞ f(t)dt = 1−Φ(x)`.
- `q A` → Umkehrung `x=Q⁻¹(q)=Φ⁻¹(1−q)`.
- **Beispiel der Originalbeschreibung (auf gerundeter Anzeige):** Für `x=1.18` ungefähr `f(x)=0.20`, `Q(x)=0.12`; bei `q=0.95` ungefähr `x=−1.65`.
- **Kritische Tests:** `x=0`, Symmetrie `Q(−x)=1−Q(x)`, sehr große `|x|`, `0<q<1`, Endpunkte `q=0/1`, Monotonie, Rundungsverhalten.

**ST-24 – `ΣCHISQD`, Chi-Quadrat-Verteilung (SIZE 007)**

- `ν A` → Zahl der Freiheitsgrade vorgeben.
- `x C` → Dichte `f(x)=x^(ν/2−1)e^(−x/2)/(2^(ν/2)Γ(ν/2))` für `x>0` und `ν>0`.
- `x E` → **untere** Verteilungsfunktion `P(x)=γ(ν/2,x/2)/Γ(ν/2)`.
- **Nicht verwechseln:** `P(x)` hier ist die untere Wahrscheinlichkeit, während `Q(x)` bei `ΣNORMD` die obere Restwahrscheinlichkeit ist.
- **Offen:** ganzzahlige `ν`-Pflicht, maximal zulässige Freiheitsgrade und möglicher historischer Überlauf, Grenzwerte bei `x=0`, Exaktheit der benutzten Gamma-Näherung und Anzeigeformat.

## 6. Abgeleitete technische Anforderungsmatrix

Alle folgenden Merkmale sind **GEPLANT** und im Nachbildungsprofil separat nachzuweisen.

| ID | Anforderung | Akzeptanznachweis |
| --- | --- | --- |
| SP-REQ-01 | Genau die 24 öffentlichen `XEQ`-Namen aus Abschnitt 3 erkennen; unterschiedliche Namen nicht zusammenführen. | Katalogtests; Referenz-`CAT` bzw. XROM-Abgleich. |
| SP-REQ-02 | Die 14 Programmgruppen getrennt initialisieren. | Frischer Zustand je Einstiegspunkt, kein Datenleck aus vorheriger Routine. |
| SP-REQ-03 | Historische Dateneingabe über Stack und `A/C/E/R/S` je Aufruf abbilden. | Sequenztests mit Stack- und Display-Snapshots nach jedem Tastendruck. |
| SP-REQ-04 | `SIZE` 003/007/008/012/015/016/018/019/020/026/045 respektieren. | Tests unterhalb und oberhalb der historischen Registergrenze. |
| SP-REQ-05 | Exaktes Anzeigeprotokoll einschließlich Resultatlabel, Reihenfolge, Rundung und `R/S` liefern. | HP-Handbuchbeispiel + Gerät/Emulator-Trace pro Aufruf. |
| SP-REQ-06 | `C`-Korrektur so verarbeiten, dass die historische Aggregat- und Phasenlogik erhalten bleibt. | Vorwärts-Aufnahme, Korrektur, Neuaufnahme, Ergebnisgleichheit. |
| SP-REQ-07 | Bei nichtlinearen Modellen gültige und ungültige Domains unterscheiden. | `x≤0`/`y≤0`/`n=0`/Singularität-Tests je Programm. |
| SP-REQ-08 | Exakte historische Statistik-Konventionen abbilden (Stichprobe/Population, Schiefe/Exzess, t-Test und Tail-Seite). | Fachformel-Tests und gegengeprüfte Originalausgaben. |
| SP-REQ-09 | Modulprofil und Programmzustand bei Suspend/Restore versionssicher serialisieren. | Neustart mitten in Datenerfassung und Ergebnisausgabe. |
| SP-REQ-10 | Historisches Modul opt-in und isoliert von modernem RPN/ALG/48-RPL halten. | Architekturtests; keine Änderung des Classic-V1-Stacks. |
| SP-REQ-11 | Keine proprietäre ROM-Datei oder fremde Programmlistings einbinden. | Lizenz-/Artifact-Audit. |
| SP-REQ-12 | Nur nach nachgewiesenen Referenztests einen konkreten Kompatibilitätsgrad behaupten. | Evidenzmatrix mit Commit, Referenz, Abdeckung, Datum und bekannten Abweichungen. |

### 6.1 Empfohlene Modulgrenzen (nicht implementiert)

~~~text
portable math / numerical algorithms (SASD-owned, reusable, no HP register semantics)
  └─ statistics: moments, regression, ANOVA/ANCOVA, tests, distributions
         ↕ model-specific numeric adaptation
Series 41 historical domain (FOCAL, virtual registers, X/Y/Z/T, flags, key phases)
  └─ application module adapter: stat-pac
         ├─ public XEQ label table (24 entries)
         ├─ independent state machine per programme
         ├─ accumulator and register view
         ├─ display/result sequencing
         └─ error/limits/provenance-tested behavior
Native iOS / desktop UI / CLI (only presentation and key dispatch)
~~~

**Kein** gemeinsamer universalhistorischer Interpreter für HP-41 und HP-48. Kein direktes Ausführen von fremdem ROM-Code, keine Umdeutung historischer Datenregister zu `double` ohne Konvertierungs- und Fidelity-Policy. Eine moderne stabile Algorithmik darf vom historischen Verhaltensadapter abweichen, sofern das ausdrücklich kenntlich gemacht und separat getestet wird. Gemeinsame C++-Funktionen mit dem SASD Math Toolkit nur nutzen, wenn tatsächlich eine geeignete, versionierte und lizenzkompatible Schnittstelle verfügbar ist.

### 6.2 Modellzustand des Stat-Pac-Adapters – Entwurf

~~~text
StatPacState {
  module_profile, module_revision, entry_point;
  phase;                     // initialized | input | correction | output | prediction | error
  data_register_view;        // historical register mapping is still TBD
  internal_accumulators;     // needed for modern algorithm, not a claim of ROM register layout
  output_cursor;             // R/S result order and repeated result handling
  last_display;              // exact label and displayed value after each step
  key_sequence_context;      // A, C, E, R/S and argument capture
  calculator_41_state_ref;   // owned by the Series-41 model, not duplicated
}
~~~

Das ist **keine** verbindliche ABI oder Persistenzstruktur. Erst nach Ablauf-/Referenzprüfung entscheiden, ob und wie die Zustände intern getrennt werden. Historische Stack-/Speicherseiteneffekte gehören dem 41-Modell; funktionale Statistikdaten dem Modul.

## 7. Prüfvektoren für die eigenständige Mathematik

Die folgenden **selbst konstruierten** Referenzen dienen als frühe mathematische Sanity-Checks. Sie sind **keine bestätigten historischen HP-Displayausgaben**. Gerundete Resultate aus Originalhandbüchern dürfen **erst nach Gegenprüfung** in Golden-Tests übernommen werden.

| Test-ID | Aufrufe | Eingaben | Erwartetes mathematisches Ergebnis |
| --- | --- | --- | --- |
| MATH-01 | `ΣBSTAT` | (1,2), (2,4), (3,6) | `x̄=2`, `ȳ=4`, `sₓ=1`, `sᵧ=2`, `r=1`. |
| MATH-02 | `ΣBSTG` | (1,2,f=2), (3,6,f=1) | `N=3`, `x̄=5/3`, `ȳ=10/3`. |
| MATH-03 | `ΣMMTUG` | 1, 2, 3 | `x̄=2`, `m₂=2/3`, `m₃=0`, `m₄=2/3`, `γ₁=0`; `GM2` weiter offen. |
| MATH-04 | `ΣMMTGD` | (1,f=1), (2,f=1), (3,f=1) | Entsprechende gewichtete Momente wie MATH-03. |
| MATH-05 | `ΣAOVONE` | Gruppen [1,2,3] und [4,5,6] | `SS_between=13.5`, `SS_within=4`, `F(1,4)=13.5`. |
| MATH-06 | `ΣAOVTWO` | Matrix [[1,2],[3,4]] | Zeilen-SS=4, Spalten-SS=1, Gesamt-SS=5, Rest-SS=0; `F` ist bei `MS_error=0` gesondert zu behandeln. |
| MATH-07 | `ΣANOCOV` | Zwei Gruppen mit gleicher linearer Steigung, unterschiedlichen Mittelwerten | Gruppeneffekt und Kovariateneffekt getrennt berechnen; Referenzzahlen nach unabhängiger Rechnung ergänzen. |
| MATH-08 | `ΣLIN` | (0,1),(1,3),(2,5) | `a=1`, `b=2`, `ŷ(3)=7`, `R²=1`. |
| MATH-09 | `ΣEXP` | (0,2),(1,2e),(2,2e²) | `a=2`, `b=1`, `ŷ(3)=2e³` (mathematisch exakt). |
| MATH-10 | `ΣLOG` | (1,1),(e,3),(e²,5) | `a=1`, `b=2`. |
| MATH-11 | `ΣPOW` | (1,2),(2,8),(3,18) | `a=2`, `b=2`, `ŷ(4)=32`. |
| MATH-12 | `ΣMLRXY` | Nichtkollineare Punkte aus `t=1+2x+3y` | `a=1,b=2,c=3`; mindestens drei linear unabhängige Designzeilen. |
| MATH-13 | `ΣMLRXYZ` | Nichtkollineare Punkte aus `t=1+2x+3y+4z` | `a=1,b=2,c=3,d=4`; mindestens vier unabhängige Designzeilen. |
| MATH-14 | `ΣPOLYP` | `y=1+2x+3x²`, verschiedene x | `a=1,b=2,c=3`. |
| MATH-15 | `ΣPOLYC` | `y=1+2x+3x²+4x³`, verschiedene x | `a=1,b=2,c=3,d=4`. |
| MATH-16 | `ΣPTST` | Paardifferenzen 1, 2, 3 bei `d₀=0` | `d̄=2`, `s_d=1`, `t=2√3`, `ν=2`. |
| MATH-17 | `ΣTSTAT` | X=[1,2,3], Y=[2,3,4], `d=0` | `s_p²=1`, `t=−√(3/2)`, `ν=4` für Konvention `x̄−ȳ`. |
| MATH-18 | `ΣXSQEV` | `O=[30,20]`, `E=[25,25]` | `χ²=2`. |
| MATH-19 | `ΣEEFXSQ` | `O=[30,20]` | `E=25` pro Klasse, `χ²=2`. |
| MATH-20 | `ΣCTKK` | 2×2-Tabelle [[10,20],[20,10]] | Pearson-`χ²=20/3≈6.666667`, **ohne** Kontinuitätskorrektur. |
| MATH-21 | `ΣCTKKK` | 3×2-Tabelle mit gleichen Verhältnissen in allen Zeilen | `χ²=0`, `C=0`. |
| MATH-22 | `ΣSPEAR` | R=[1,2,3], S=[3,2,1] | `r_s=−1` ohne Rangbindungen. |
| MATH-23 | `ΣNORMD` | `x=0`; `q=0.5` | `f(0)=1/√(2π)≈0.39894228`, `Q(0)=0.5`, `Q⁻¹(0.5)=0`. |
| MATH-24 | `ΣCHISQD` | `ν=2`, `x=2` | `f(2)=e⁻¹/2≈0.18393972`, `P(2)=1−e⁻¹≈0.63212056`. |

Alle 24 MATH-Prüfungen sind **VORSCHLÄGE**, nicht im Repository ausgeführte Tests. Insbesondere sind leicht exakte Datensätze bei vollrangigen Modellen nicht gleichbedeutend mit robusten Singulär-/Rundungs- und historischen Verhaltenstests.

### 7.1 Verbindliche Testarten für die spätere Nachbildung

1. **Catalog/dispatch:** jeder Name exakt einmal; `CAT`- bzw. XROM-Mapping nach Referenz.
2. **Pure numerics:** bekannte Werte aus unabhängigen, frei nachrechenbaren Quellen.
3. **Input correction:** Originaldaten aufnehmen → Ergebnis → einzelne Aufnahme zurücknehmen → korrigiert neu hinzufügen; `C` darf die Gruppenphase nicht unzulässig ändern.
4. **Historical output trace:** `XEQ`, `A`, `C`, `E`, jede `R/S`-Fortsetzung; **nach jedem Schritt** Displaytext, X/Y/Z/T, LAST X, Register, Flags, Programmzeiger und Fehler protokollieren, soweit beobachtbar.
5. **Register/memory limit:** exakt `SIZE−1` und `SIZE` sowie Kollision mit vorhandener `ΣREG`-Konfiguration.
6. **Numerical stress:** große/kleine Zahlen, fast identische Beobachtungen, Subtraktionsauslöschung, Nullvarianz, Gewichtsextreme, Singularität und Überlauf.
7. **State restore:** Wiederherstellung nach Unterbrechung mitten in einer Datengruppe, beim Ergebnis-`R/S` und nach einem Fehler.
8. **Cross-model:** identisches freigegebenes Verhalten auf 41C/41CV/41CX soweit historische Quellen es verlangen; Unterschiede explizit ausweisen.
9. **No regression:** Änderungen am Stat Pac dürfen Classic-M1/M2, ALG und HP-48-Profile nicht unbemerkt beeinflussen.
10. **Rights/security:** keine fremden ROM-/Handbuch-Assets im Repository, keine Ausführung fremder Binärdaten außerhalb kontrollierter virtueller Speichergrenzen.

**Historisches Golden-Trace-Schema (Vorlage; noch keine Werte):**

~~~yaml
case_id: HIST-ST-XX-001
entry_point: "Σ..."
source_manual: "HP-ST-EN"
source_print_page: null
source_scan_page: null
reference: "physical-41C | physical-41CV | emulator+licensed-ROM"
reference_rom_revision: null
test_platform: null
sequence: []  # e.g. XEQ, ENTER, A, C, E, R/S
expected_display: []
expected_x_y_z_t: []
expected_register_deltas: []
expected_flags: []
expected_errors: []
numeric_tolerance: null  # original display precision first; document any deviation
rights_of_fixture: "independently recorded; no ROM bytes included"
checked_on: null
implementation_commit: null
status: planned
~~~

## 8. Offene historische Abgleicharbeiten (Pflicht vor Konformitätszusage)

| Priorität | Prüfauftrag | Grund |
| --- | --- | --- |
| P1 | **Alle 24 Original-Aufrufe im 80-seitigen Handbuch seitenweise erfassen:** Formeln, Schritte, Beispiele und Ergebnislabels. | QRC allein reicht nicht für vollständige Ablaufsemantik. |
| P1 | Sechs Ausgaben von `ΣMMTUG`/`ΣMMTGD` und insbesondere `GM2`-Definition überprüfen. | Die deutsche Bezeichnung *Exzess* und englische *kurtosis* können gegensätzliche −3-Konventionen nahelegen. |
| P1 | Ergebnisreihenfolge und Anzeigeetiketten für `ΣBSTAT`, ANOVA/ANCOVA, alle Regressions- und Tabellenprogramme transkribierend **eigenständig protokollieren**. | Jede abweichende `R/S`-Phase ist historisch beobachtbar. |
| P1 | `ΣTSTAT`-Phasen (Stichprobe X/Y, Eingabe `d`, Freiheitsgrade) verifizieren. | Gleich aussehende moderne Tests können unterschiedliche Ergebnisse liefern. |
| P1 | Spezialtasten `A/C/E/R/S`, Shift+`A`, Prompttexte, Stacklift, Fehler und Wiederinitialisierung testen. | K2-Verhalten ist mehr als ein mathematisches Ergebnis. |
| P1 | Originales Registermapping mit `SIZE`/`ΣREG`, gemeinsamen Speicherbereichen und Flagnutzung bestimmen. | Historische Programme verändern einen gemeinsamen HP-41-Zustand. |
| P1 | Echtes Modul als XROM/CAT-Liste gegen Aufrufnamen abgleichen; interne Labels getrennt dokumentieren. | Unqualifizierte Aussagen über zusätzliche ROM-Markierungen vermeiden. |
| P2 | Genauigkeit, Rundung, Overflow und deterministische Abbruchkriterien je Routine messen. | Moderne binary64-/SVD-Lösungen können abweichende Werte zeigen. |
| P2 | `ΣNORMD`-Endpunkte und `ΣCHISQD`-Freiheitsgradgrenzen historisch nachmessen. | Nicht alle mathematisch definierten Eingaben sind historisch unterstützt. |
| P2 | Varianten/Revisionsstände der Stat-Pac-Module und 41C/41CV/41CX prüfen. | Kompatibilitätsclaims müssen ein konkretes Profil nennen. |
| P2 | Unabhängige, urheberrechtlich zulässige Golden-Fixtures ergänzen und versionieren. | Reproduzierbare, lizenzsichere Tests ermöglichen. |

**Nachweiskette:** `Aufruf-ID → HP-Handbuchseite → Original-Tastensequenz → unabhängiger Referenztrace → SASD-Unit-/Integrationstest → Commit/Release → gemessene Abdeckung`.

## 9. Geplante Implementierungsreihenfolge (ohne V1-Blockade)

Die folgende Reihenfolge ist eine **fachliche Empfehlung**, keine Termin- oder Funktionszusage. Sie berücksichtigt die bindende Roadmap [M0–M5](../../ROADMAP.md):

| Phase | Arbeit | Voraussetzung | Freigabe |
| --- | --- | --- | --- |
| **R0 – Dokumentation** | Vollständige QRC-Labelmatrix, Quellenregister, offener Originalabgleich (dieses Dokument) | keine | Dokument / Review |
| **R1 – mathematische Bibliothek** | Ungewichtete/gewichtete Basisstatistik, Momente, Pearson, einfache OLS, Verteilungsfunktionen | numerische Designentscheidung | unabhängige Mathematiktests |
| **R2 – erweiterte Statistik** | Regressionen, Polynome, ANOVA, ANCOVA, t-/Chi-Quadrat-Tests, Spearman | R1 | Randfall- und Fachtests |
| **R3 – 41-Modulschnittstelle** | Modul-Dispatch und Modellzustand, Register-/Stackadapter, `A/C/E/R/S`-Phasen, `SIZE` | verifizierter Series-41-FOCAL-/Zustandsvertrag | Tastensequenztests |
| **R4 – historische Fidelity** | Anzeigeprotokolle, Korrekturen, Originalbeispiele, ROM-/Gerätevergleich je Revision | R3 und rechtmäßige Referenz | evidenzbasierte Einzelabnahmen |
| **R5 – Freigabe** | Kompatibilitätsmatrix mit ausgewiesenen Grenzen und regressionssicheren Tests | R4 | nachvollziehbare K1/K2-Aussagen pro Funktion |

**Kein** R0–R5-Schritt darf die erste hochwertige, offlinefähige und werbefreie iPhone-RPN-V1.0 unnötig verzögern. Diese Dokumentation ist bewusst jetzt möglich, die Implementierung wird in der vorhandenen Projekt-Roadmap priorisiert.

## 10. Abnahmekriterien des fertigen Stat-Pac-Profils

- [ ] Sämtliche **24** öffentlichen Aufrufnamen geprüft, ausführbar und je historischer Modell-/ROM-Revision kategorisiert.
- [ ] Alle **14** Programmeinheiten in ihren **Daten-, Korrektur-, Ergebnis- und Neuinitialisierungsphasen** gegen Originaltraces nachgewiesen.
- [ ] `SIZE`, Stack, Register, Programmausführung, Flags und historische Anzeigeformate belegt.
- [ ] Jedes Original-Handbuchbeispiel unabhängig nachgerechnet und als rechtssicherer Testfall erfasst; Abweichungen dokumentiert.
- [ ] Statistikvarianten (Stichprobe/Population, Exzess/Kurtosis, pooled/Welch, obere/untere Wahrscheinlichkeiten) explizit entschieden.
- [ ] Sonder-/Fehlerfälle in Referenztests erfasst, nicht nur mathematisch plausible Resultate.
- [ ] Tests auf mindestens einer definierten historischen Referenzkonfiguration oder nachweislich passender Emulator-ROM-Kombination nachvollziehbar.
- [ ] Bestätigte Abdeckung als **unterstützt / teilweise / nicht unterstützt / ungetestet** veröffentlicht; kein unbelegtes „100 % kompatibel“.
- [ ] Rechtliche Trennung: keine mitgelieferten fremden ROMs, kein unveränderter Abdruck des fremden Handbuchs.
- [ ] Keine Regression der Classic-V1-iPhone-App oder des getrennten HP-48-Funktionsmodells.

## 11. Dokumentationspflege

**Eine Zeile in dieser Datei ist keine implementierte Funktion.** Bei späteren Änderungen Datum, Historienreferenz, Test-IDs und Status je Aufruf aktualisieren. Tatsächlich implementierte Fähigkeiten dürfen erst nach bestandenen Tests in README/Release-Notes oder in der Kompatibilitätsmatrix als verfügbar erscheinen.

**Weiterführende Repository-Dokumente:**
- [HP-41C – Grundfunktionen](HP-41C-FUNKTIONSKATALOG.md)
- [HP-41C – Vollständigkeitsprüfung](HP-41C-VOLLSTAENDIGKEITSPRUEFUNG.md)
- [Architektur der Series 41](../en/HISTORICAL-41.md)
- [Kompatibilitäts- und Evidenzmodell](../en/COMPATIBILITY.md)
- [Gesamt-Roadmap](../../ROADMAP.md)
- [AGENTS.md – Entwicklungsregeln](../../AGENTS.md)

---

**Bearbeitungsvermerk 2026-11-23:** Öffentliches Funktionsinventar und QRC-Tastenmuster gegen die historischen englischen/deutschen Original-Kurzanleitungen geprüft; 80-seitige Handbücher lokalisiert, aber noch **nicht** vollständig seitenweise in verifizierte Golden-Trace-Spezifikationen überführt. Alle Implementierungs- und Teststatus bleiben **GEPLANT**.