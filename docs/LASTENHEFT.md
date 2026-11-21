# Lastenheft – SASD Scientific Calculator

**Dokumentkennung:** SASD-SCI-LH-001  
**Version:** 1.0 (konsolidierter fachlicher Planungsstand)  
**Datum:** 21.11.2026  
**Status:** Verbindliche und geplante Anforderungen aus dem Projektgespräch; **keine Produktfreigabe und kein Nachweis der Implementierung**  
**Geltungsbereich:** SASD Scientific Calculator und seine vorgesehenen wissenschaftlichen App-Varianten  
**Repository:** https://github.com/Robin-Goerlach/SASD-Scientific-Calculator  
**Sprache:** Deutsch; weitere technische Spezifikationen können auf Englisch geführt werden.

> **Maßgeblicher Leitsatz:** Erst ein hervorragender, klassischer wissenschaftlicher UPN/RPN-Taschenrechner im App Store – anschließend schrittweise mehr historische Kompatibilität und zusätzliche Funktionen.
>
> **Dieses Lastenheft beschreibt aus Auftraggeber- und Produktsicht das WAS und WARUM.** Technische Ausführungsdetails, konkrete C++-Typen, Dateien, Tastencodes und die vollständigen Befehlsinventare gehören in Architektur, Pflichtenheft, Testfälle bzw. separate Funktionskataloge. Übernommene Architekturentscheidungen werden hier als Randbedingungen festgehalten, ohne einen bereits implementierten Funktionsumfang vorzutäuschen.

---

## 1. Dokumentzweck, Verbindlichkeit und Abgrenzung

### 1.1 Zweck

Dieses Lastenheft bündelt die im Projekt besprochenen Anforderungen an einen modernen, qualitativ hochwertigen, wissenschaftlichen Taschenrechner mit klassischer UPN/RPN-Bedienung, einer separat vorgesehenen ALG-Variante und langfristiger historischer Kompatibilität mit den Rechnerfamilien HP-41C/CV und HP 48GX. Die Anforderungen sollen bei Entwicklung, Planung, Priorisierung, Umsetzung durch Codex und späterer Produktabnahme als nachvollziehbare Grundlage dienen.

Das Dokument ist **keine vollständige wortgetreue Gesprächsabschrift**. Es ist eine gegliederte fachliche Konsolidierung: Wiederholungen werden zusammengeführt, spätere verbindliche Entscheidungen gehen älteren Priorisierungsvorschlägen vor, offene Punkte bleiben offen. Insbesondere sind frühere, umfangreichere Vorab-Emulationspläne durch den jüngeren **RPN-V1.0-first-Beschluss** in ihrer zeitlichen Einordnung geändert, nicht automatisch inhaltlich gestrichen.

### 1.2 Statussprache

| Kennzeichen | Bedeutung | Verbindlichkeit |
| --- | --- | --- |
| **V1-MUSS** | Nachweisbare Anforderung für die erste klassische iPhone-App V1.0, bezogen auf den noch freizugebenden genauen Funktionsumfang | Blockiert V1-Freigabe, sofern nicht ausdrücklich neu entschieden |
| **ARCH-MUSS** | Architekturgrenze, Sicherheits- oder Entkopplungsregel, die früh einzuhalten ist | Muss bei betroffenen Entwicklungen beachtet werden, ohne alle Folgefunktionen sofort umzusetzen |
| **LANGFRISTIG-MUSS** | Verbindliches langfristiges Ziel mit später konkretisiertem Umfang und eigener Abnahme | **Kein** V1-Freigabeblocker |
| **GEPLANT** | Beabsichtigte Funktion bzw. empfohlene Realisierung; genauer Zeit- und Leistungsumfang noch nicht fixiert | Wird mit eigenem Meilenstein/Scope freigegeben |
| **OPTIONAL** | Bewusst nicht verpflichtende Erweiterung oder Forschungsrichtung | Erst nach gesondertem Beschluss |
| **OFFEN** | Fachliche oder technische Detailentscheidung wurde noch nicht getroffen | Darf nicht als feststehende Zusage dargestellt werden |
| **IST** | Gegenwärtig im Repository nachweisbar vorhanden | Ohne dokumentierten Test keine Aussage über historische Genauigkeit |

Priorität und Status sind getrennt: Eine LANGFRISTIG-MUSS-Funktion kann heute vollständig ungeplant für einen konkreten Release sein, ohne ihr langfristiges Ziel zu verlieren. Die **Kompatibilitätsstufen K1–K4** sind außerdem nicht mit den **Meilensteinen M0–M5** gleichzusetzen.

### 1.3 Verweis auf vollständige historische Funktionslisten

Die historischen Einzelbefehle, Tastenkombinationen, Menüs, Programmanweisungen und Betriebsfunktionen sind **nicht** Bestandteil der Tabellen dieses Lastenhefts. Sie erhalten eigenständige, versionierte Funktionskataloge:

- **HP-41C (Grundmodell, ohne beliebige Zusatz-ROMs):** [`docs/de/HP-41C-FUNKTIONSKATALOG.md`](de/HP-41C-FUNKTIONSKATALOG.md) – vorhanden; Referenzbestand, **keine** SASD-Implementierungsbehauptung.
- **HP 48GX:** [Funktionskatalog `docs/de/HP-48GX-FUNKTIONSKATALOG.md`](de/HP-48GX-FUNKTIONSKATALOG.md) – inzwischen vorhanden; dokumentiert unter anderem 517 unterschiedliche ROM-Befehlsnameneinträge. Dies bedeutet **nicht** vollständige Erfassung aller System-RPL-Interna oder bereits implementierte SASD-Funktionen.
- **HP-41-Erweiterungsmodule** (Time Module, Statistics Pac, Advantage Pac usw.) sowie HP-48-Bibliotheken/Karten sind **gesondert** zu erfassen; ihre Befehle gehören nicht ungeprüft zum Grundmodell.
- Die Kataloge brauchen mindestens: historischen Namen, Tastenzugriff bzw. Menü, Argumente/Objekttypen, Wirkung auf Stack/Register/Zustand, Betriebsmodi, Modell-/ROM-/Modulabhängigkeit, Referenzquelle, Priorität und tatsächlich vorhandene SASD-Tests.

**Katalogvollständigkeit** und **implementierte Funktionsabdeckung** sind unabhängig voneinander zu messen. Dieses Lastenheft verlangt die spätere Zuordnung von jeder zugesagten Funktion zu Implementierung, Test und Release; es ersetzt keine Recherche eines konkreten historischen Befehls.

### 1.4 Unterlagen und Entscheidungshierarchie

Für die operative Planung gelten ergänzend: [README](../README.md), [ROADMAP](../ROADMAP.md), [TASKS](../TASKS.md), [Entscheidungsregister](en/DECISIONS.md), [Anforderungsmatrix](en/REQUIREMENTS-MATRIX.md), [V1-Freigabe](en/RELEASE-V1.md), [Architektur](en/MULTI-APP-ARCHITECTURE.md), [Kompatibilität](en/COMPATIBILITY.md) und [Codex-Regeln](../AGENTS.md). Bei einem Widerspruch werden **eine neuere ausdrücklich verbindliche Produktentscheidung** und deren begründete Auswirkungen dokumentiert; ältere Verpflichtungen werden nicht stillschweigend beseitigt.

---

## 2. Motivation, Zielgruppen und Produktcharakter

### 2.1 Hauptmotivation

Primär wird ein **hochwertiger, klassischer, wissenschaftlicher Taschenrechner auf dem iPhone** gewünscht. Die UPN/RPN-Eingabe, ein klar sichtbarer Stack, eine angenehme haptisch gedachte Tastenbedienung und die Zuverlässigkeit bei alltäglichen Berechnungen sind wichtiger als eine schon zur ersten Veröffentlichung vollständige historische Maschine.

Es ist **kein Massenmarktzwang** vorgesehen. Das Produkt darf ein Nischenangebot für Menschen sein, die klassische wissenschaftliche Rechner bevorzugen. Zugleich soll die Qualität der Softwareentwicklung und Dokumentation als unaufdringliche Referenz für **SASD** dienen.

### 2.2 Zielgruppen

| Gruppe | Erwarteter Nutzen |
| --- | --- |
| Liebhaber klassischer wissenschaftlicher UPN-Rechner | Vertraute Eingabe ohne erzwungene `=`-Taste; angenehme Nutzung eines modernen Telefons |
| Technisch und mathematisch arbeitende Nutzer | Zuverlässige Mathematik, klare Zahlen-/Fehlerdarstellung, Register und später erweiterte Numerik |
| Lernende | Verständliche, schrittweise Erklärung von UPN/RPN und algebraischer Eingabe sowie praktischer Vergleich |
| Historische Programmnutzer | Langfristig Ausführung und Austausch geeigneter FOCAL- und RPL-Programme |
| Anwender mit ALG-Präferenz | Eigenständige Scientific-App mit `=`, Klammern, Prioritäten und wissenschaftlichen Funktionen |
| Entwickler/Administratoren | Spätere Desktop-Oberfläche mit Editor, Stack-/Registeranalyse, Bibliothek und Debugging |

### 2.3 Produktprinzipien

| ID | Status | Forderung |
| --- | --- | --- |
| LH-PROD-001 | V1-MUSS | Erste öffentliche Scientific-App ist ein **vollwertig nutzbarer klassischer RPN-Wissenschaftsrechner** für das iPhone, keine unfertige technische Demo. |
| LH-PROD-002 | V1-MUSS | Rechnen, Wiederherstellen des Zustands und notwendige Bedienhilfe funktionieren **vollständig offline**; keine dauerhafte Internetverbindung, kein Konto und kein Server. |
| LH-PROD-003 | V1-MUSS | **Keine Werbung und kein Abonnement**; keine Werbe-SDKs als Bestandteil des ersten Releases. |
| LH-PROD-004 | GEPLANT | Möglichst kostenlose Verfügbarkeit; endgültige Preisentscheidung nach wirtschaftlicher Prüfung. |
| LH-PROD-005 | V1-MUSS | Dezentes, barrierefrei anklickbares **SASD**-Kennzeichen **oben links** als Link zur offiziell bestätigten SASD-Webseite; kein sonstiger Werbebereich. |
| LH-PROD-006 | ARCH-MUSS | Historisch orientierte Bedienphilosophie bleibt erhalten; spätere moderne Funktionen verdrängen die klassische RPN-Bedienung nicht. |
| LH-PROD-007 | ARCH-MUSS | Produkte und App-Store-Angaben müssen ihren **tatsächlich verfügbaren** Funktionsumfang und ihre Grenzen ehrlich nennen. |
| LH-PROD-008 | ARCH-MUSS | Unabhängige SASD-Produktidentität; keine Darstellung als offizielles oder verbundenes historisches Herstellerprodukt. |
| LH-PROD-009 | V1-MUSS | Die App soll als hochwertiger, responsiver und optisch ruhiger alltäglicher Rechner funktionieren; Benutzerfreundlichkeit und Fehlerfreiheit haben Vorrang vor historischer Gehäusenachbildung. |

---

## 3. Produktfamilien, Anwendungen und Veröffentlichungen

### 3.1 Scientific versus Financial

**SASD Scientific Calculator** bleibt das priorisierte Projekt mit bereits bestehendem Repository. **SASD Financial Calculator** ist eine zweite, eigenständig vermarktete und veröffentlichbare Produktlinie mit **separat vorgesehenem** Repository `SASD-Financial-Calculator`. Dieses Lastenheft beauftragt **nicht** dessen Anlage.

Scientific gehört die wissenschaftliche Mathematik und die langfristige historische Kompatibilität mit den hier definierten 41er-/48er-Zielen. Financial soll als eigenes Fachprodukt unter anderem TVM (N, I/Y, PV, PMT, FV), Zinseszins, Annuitäten, Tilgungspläne, Cashflows, NPV, IRR, Anleihen, Renditeberechnungen und Abschreibungen abdecken. Historische Vorbilder HP-12C, HP-17BII, HP-19BII und HP-30b sind **Referenzen**, keine unmittelbare Pflicht zur originalgetreuen Emulation.

Einzelne finanzmathematische Basisfunktionen dürfen in Scientific vorkommen, beispielsweise über historische Erweiterungen. Eine solche Überschneidung begründet **keinen** gemeinsamen Finanz-Workflow oder eine Zusammenlegung beider Apps.

### 3.2 Scientific-App-Varianten

| Variante | Charakter | Status |
| --- | --- | --- |
| **Classic RPN** | Klassischer wissenschaftlicher UPN-Rechner mit ENTER, Stack, Registern und später historisch orientierten 41er-Funktionen | **Erster V1-Pfad** |
| **Algebraic Scientific / ALG** | **Eigenständige** wissenschaftliche App mit `=`, Ausdruckseditor, Klammern, Variablen und Operatorprioritäten | **Architektonisch verbindlich**, separat zu priorisierender Release |
| **Advanced RPL** | Eigenständige komplexere UPN/RPL-Welt mit RPL-Objekten, User RPL und später System RPL | **Langfristig geplant** |
| **Kombinierte Eingabevariante** | Spätere App oder Profil, das ALG und RPN für interaktive Eingaben umschalten kann | **OPTIONAL** als eigenständiges Produkt; Eingabeadapter weiterhin vorgesehen |

Alle geplanten wissenschaftlichen Anwendungen werden **in einem Scientific-Monorepo** entwickelt, können aber **getrennt gebaut, getestet, versioniert und veröffentlicht** werden. Endgültige App-Namen, Bundle-IDs, Preisgestaltung und Freigabereihenfolge jenseits der ersten RPN-App sind offen.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-PORT-001 | ARCH-MUSS | Scientific und Financial besitzen getrennte Repositories, Produktidentitäten, App-Store-Auftritte, Releasezyklen und Freigabekriterien. |
| LH-PORT-002 | ARCH-MUSS | Ein unvollständiges Financial-Feature darf Scientific nicht blockieren und umgekehrt. |
| LH-PORT-003 | ARCH-MUSS | Classic RPN, ALG und Advanced RPL dürfen keine zwingende Laufzeitabhängigkeit von einer anderen Scientific-App haben. |
| LH-PORT-004 | ARCH-MUSS | Gemeinsam nutzbare Mathematik ist erwünscht; die jeweilige Bedienung, Historik, Datenhaltung und Programmsemantik bleiben eigenständig. |
| LH-PORT-005 | ARCH-MUSS | Classic RPN erhält bei Ressourcen- und Releasekonflikten **Vorrang** gegenüber parallelen ALG-, RPL-, Financial-, Desktop- und Forschungsarbeiten. |
| LH-PORT-006 | GEPLANT | Eine ALG-App kann zeitlich parallel entwickelt werden, muss nicht bis zur historischen Gesamtkompatibilität warten und kann separat erscheinen. |
| LH-PORT-007 | OFFEN | Ob Classic RPN, ALG und Advanced RPL als drei separate App-Store-Listings oder teilweise gemeinsam vertrieben werden, wird bei der jeweiligen Veröffentlichung entschieden; technische Entkopplung ist trotzdem nötig. |

---

## 4. Funktionaler Kern: klassische UPN/RPN-Bedienung

### 4.1 Erwartete Bedienphilosophie

Die klassische Eingabe verwendet einen Stack statt automatisch geparster Infix-Ausdrücke. Als bewusst einfaches Vergleichsbeispiel gilt:

- RPN: `3 ENTER 4 ENTER 5 × +` → **23**.
- ALG: `3 + 4 × 5` → **23**.

Bei RPN wird **keine** nachträgliche Operatorpriorität über die eingegebene Tastenfolge gelegt. Für binäre Operatoren gilt die dokumentierte Operandenreihenfolge, etwa `Y − X` und `Y ÷ X`. Exakte Wirkungen von ENTER, Stack Lift, Drop, LAST X und Eingabezuständen müssen vor der fachlichen Abnahme spezifiziert werden.

Für V1.0 ist ein **historisch orientierter Vier-Ebenen-Stack (X/Y/Z/T)** vorgesehen. Das bestehende anfängliche, dynamische C++-Stackexperiment ist nicht automatisch ein getreues Modell. Die genaue Wahl der V1-Regeln muss vor Implementierung ausdrücklich festgelegt und getestet werden.

### 4.2 Anforderungen

| ID | Status | Forderung / prüfbares Ergebnis |
| --- | --- | --- |
| LH-RPN-001 | V1-MUSS | Klassische RPN-Tastenfolgen mit `ENTER`, Zifferneingabe und binären Operationen funktionieren nach einem freigegebenen Zustandsmodell. |
| LH-RPN-002 | V1-MUSS | Die für V1 freigegebenen Stackregister X/Y/Z/T werden angezeigt und in definierter Reihenfolge aktualisiert. |
| LH-RPN-003 | V1-MUSS | Stack Lift, Drop, Duplizieren, Vertauschen, Rollen und andere freigegebene Stackfunktionen haben reproduzierbare Wirkung. |
| LH-RPN-004 | V1-MUSS | `LAST X` und weitere für V1 freigegebene Speicher-/Stackkonventionen werden als Zustandsübergänge dokumentiert und geprüft. |
| LH-RPN-005 | V1-MUSS | Addition, Subtraktion, Multiplikation und Division berücksichtigen die Operandensemantik und klar definierte Fehlerzustände. |
| LH-RPN-006 | V1-MUSS | Speicherregister erlauben Ablegen, Abrufen und festgelegte Rechenoperationen mit Registerinhalten. |
| LH-RPN-007 | V1-MUSS | Benutzer können Eingaben löschen bzw. korrigieren; Umfang und Wirkung von Clear, Undo und Fehlerrücksetzung werden vor der Freigabe festgelegt. |
| LH-RPN-008 | V1-MUSS | Ein Fehler darf den bestehenden Rechnerzustand nicht unerwartet beschädigen; definierte zulässige historische Abweichungen werden für spätere Profile dokumentiert. |
| LH-RPN-009 | ARCH-MUSS | Die RPN-Stackverwaltung ist fachlich von Tastendarstellung und Betriebssystem getrennt. |
| LH-RPN-010 | ARCH-MUSS | Eine allgemeine technische Stack-Datenstruktur ersetzt nicht die historische 41er- oder 48er-Ausführungssemantik. |
| LH-RPN-011 | GEPLANT | Historische ALPHA-/Tastenzuweisungen, Flags und programmierbezogene Befehle werden modell- und katalogbezogen später ergänzt. |

---

## 5. Algebraischer wissenschaftlicher Rechner und optionale ALG-Eingabe

### 5.1 Eigenständigkeit

Die ALG-App ist **eine eigene Scientific-Anwendung**, kein Abbild der RPN-Oberfläche mit hinzugefügter `=`-Taste. Sie benötigt einen eigenen Rechnerkontext, etwa für `Ans`, Variablen, gespeicherte Werte, Angle Mode, Verlauf und Fehlermeldungen. Sie soll denselben mathematischen Funktionsunterbau verwenden wie der klassische Rechner.

Eine moderne **ALG-Eingabe innerhalb historisch orientierter Rechnerprofile** bleibt ebenfalls vorgesehen, darf jedoch die Ausführungslogik historischer FOCAL-, User-RPL- oder System-RPL-Programme **niemals stillschweigend ändern**. Eingabemodus, Rechnerfamilie und Kompatibilitätsprofil sind verschiedene Konfigurationsdimensionen.

### 5.2 Algebraische Syntax und Beispiele

| Testeingabe | Erwartetes Ergebnis | Regel |
| --- | ---: | --- |
| `3 + 4 × 5` | 23 | Punkt vor Strich |
| `(3 + 4) × 5` | 35 | Klammern |
| `2 + 3²` | 11 | Potenzen vor Addition |
| `20 ÷ 4 × 2` | 10 | Linksassoziative Division/Multiplikation |
| `2^3^2` | 512 | Rechtsassoziative Potenzierung |
| `-(3 + 4)` | −7 | Unäres Vorzeichen |
| `(3 + 4 × 5²) ÷ 2` | 51,5 | Verschachtelte Auswertung |
| `2 + 3 × (4 + 5)` | 29 | Zusammenwirken von Prioritäten |

**Zu spezifizierende Konvention:** Für die moderne ALG-Syntax wird `-2^2 = -(2^2) = -4` und `(-2)^2 = 4` empfohlen. Die endgültige normierte Grammatik einschließlich Dezimalkomma, impliziter Multiplikation und unären Vorzeichen ist eine **offene Detailentscheidung**, nicht etwas, das aus dem HP-48-Rechnerverhalten ungeprüft abgeleitet wird.

### 5.3 Anforderungen

| ID | Status | Forderung |
| --- | --- | --- |
| LH-ALG-001 | ARCH-MUSS | Genau ein gemeinsam nutzbarer, oberflächenunabhängiger moderner algebraischer Ausdrucksparser wird vorgesehen. |
| LH-ALG-002 | GEPLANT | Vollständige Ausdrücke, Klammern, Operatorprioritäten, korrekte Assoziativität, Potenzen, unäre Operatoren und Wurzeln werden verarbeitet. |
| LH-ALG-003 | GEPLANT | Konstanten, Variablen, Registerbezüge und Funktionsaufrufe mit validierten Argumenten sind vorgesehen. |
| LH-ALG-004 | GEPLANT | Der Parser unterstützt schrittweise Trigonometrie, Logarithmen, komplexe Werte, Vektoren, Matrizen, Statistik und benutzerdefinierte Funktionen, soweit der jeweilige Rechenkontext dies anbietet. |
| LH-ALG-005 | ARCH-MUSS | Lexikalische, syntaktische, Typ-, Bereichs-, Genauigkeits- und Auswertungsfehler sind voneinander unterscheidbar und nutzerverständlich erklärbar. |
| LH-ALG-006 | ARCH-MUSS | Parsing und mathematische Auswertung werden getrennt; die grafische Eingabekomponente enthält keine eigene Mathematikimplementierung. |
| LH-ALG-007 | ARCH-MUSS | Programmcode historischer Rechner wird nicht über den modernen ALG-Parser interpretiert oder übersetzt. |
| LH-ALG-008 | ARCH-MUSS | Das Ergebnis eines modernen Ausdrucks wird nur über einen kontrollierten, modellgerechten Zustandsübergang an historische Stack-/Registermodelle übergeben. |
| LH-ALG-009 | GEPLANT | Die ALG-App bietet eine gut editierbare vollständige Ausdruckseingabe mit `=` und sinnvollen Korrektur-/Verlaufsmöglichkeiten. |
| LH-ALG-010 | OFFEN | Lokale Dezimal-/Listentrennzeichen, `%`, implizite Multiplikation, symbolische Ausdrücke und Zuweisungssyntax werden bei ALG-Entwicklung definiert. |
| LH-ALG-011 | ARCH-MUSS | Ausdrücke dürfen durch übergroße Eingaben, Verschachtelung oder rekursive Auflösung keine unkontrollierten Ressourcen verbrauchen. |

### 5.4 Parserstrategie (nicht Teil der fachlichen Abnahme)

Als **begründete technische Empfehlung** wurde ein **Pratt-Parser** für Operatorprioritäten, kombiniert mit rekursivem Abstieg für Klammern, Funktionsargumente und strukturierte Formen, gegenüber einer langen reinen Recursive-Descent-Prioritätsleiter bevorzugt. Vorteile: zentrale Binding-Power-Regeln, Erweiterbarkeit und isolierte Tests; Risiken: leicht missverständliche Assoziativitäts-/Minus-Regeln. Die verbindliche Entscheidung ist **erst bei Erstellung des Parser-ADRs** zu treffen.

---

## 6. Gemeinsame mathematische und numerische Leistungsfähigkeit

### 6.1 Fachlicher Funktionsrahmen

Scientific soll nach Entwicklungsstand folgende Gruppen unterstützen können:

- **Grundmathematik:** Arithmetik, Vorzeichen, Brüche nach Festlegung, Potenzen/Wurzeln, reelle Zahlen, Konstanten, Fakultät und weitere wissenschaftliche Basisoperationen.
- **Trigonometrie:** sin/cos/tan und Umkehrfunktionen, erforderliche Winkelmodi, klare Darstellungs-/Rundungsregeln.
- **Exponential-/Logarithmusfunktionen:** `e^x`, `10^x`, `ln`, `log` usw. gemäß freigegebenem Funktionskatalog.
- **Erweiterte Datentypen:** komplexe Zahlen, Vektoren, Matrizen und komplexe Matrizen.
- **Numerik:** Nullstellen, Polynome, Gleichungen/Gleichungssysteme, numerische Integration, Differentialgleichungen, gegebenenfalls weitere Verfahren.
- **Statistik:** Summen/Accumulatoren, Kennzahlen, Regression/Kurvenanpassung und zugehörige Datenmodelle.
- **Zahlensysteme und Logik:** binär, oktal, dezimal, hexadezimal, Ganzzahl- und Bitoperationen, boolesche Operationen.
- **Einheiten und Konvertierungen:** mathematisch/fachlich geeignete Umrechnungen.
- **Grafik und symbolische Verfahren:** spätere, gesondert priorisierte Scientific-Erweiterungen.
- **Finanzmathematische Basisoperationen:** nur soweit wissenschaftlich oder aus einem historischen Modul sinnvoll; vollständige Geschäftsabläufe gehören Financial.

Die historische Funktionszuordnung und die konkrete Vollständigkeit je Modell werden aus den **separaten HP-Funktionskatalogen** abgeleitet. Ein Funktionsname im Lastenheft ist keine automatische V1-Zusage und kein Nachweis einer historisch identischen Implementierung.

### 6.2 Anforderungen

| ID | Status | Forderung |
| --- | --- | --- |
| LH-MATH-001 | V1-MUSS | Grundrechenarten, übliche Potenzen/Wurzeln, Logarithmen, Exponential- und trigonometrische Funktionen sind im **vorher freigegebenen V1-Umfang** nutzbar. |
| LH-MATH-002 | V1-MUSS | Winkelmodi und numerisches Ein-/Ausgabeformat werden für freigegebene Operationen nachvollziehbar behandelt. |
| LH-MATH-003 | ARCH-MUSS | Fachlich gleiche mathematische Algorithmen sollen möglichst **einmal** entwickelt, geprüft und wiederverwendet werden. |
| LH-MATH-004 | ARCH-MUSS | Unterschiede in Zahlentyp, historischer Genauigkeit, Rundung, Stack- und Fehlereffekt werden **nicht** durch eine falsche globale Universalregel verdeckt. |
| LH-MATH-005 | ARCH-MUSS | Zahlenwert, historische interne Repräsentation, Anzeigeformat und Eingabeformat bleiben logisch unterscheidbar. |
| LH-MATH-006 | GEPLANT | Komplexe Zahlen, Vektoren, reelle/komplexe Matrizen und Matrixoperationen werden schrittweise ergänzt. |
| LH-MATH-007 | GEPLANT | Numerische Solver, Polynom-/Nullstellenverfahren, Integration und Differentialgleichungslösungen werden schrittweise ergänzt. |
| LH-MATH-008 | GEPLANT | Statistik, Regression, Zahlensysteme, Bitoperationen und Einheiten werden über geeignete gemeinsame Bibliotheken bereitgestellt. |
| LH-MATH-009 | ARCH-MUSS | Funktionen werden mit Argumentzahl, Typen, Winkel-/Präzisionskontext, Verfügbarkeit, Diagnose und Hilfe verknüpfbar dokumentiert. |
| LH-MATH-010 | OFFEN | Numerischer Basistyp (u. a. `double`, Dezimal-/Mehrpräzisionsarithmetik), Toleranzen und historische Konformitätsgrade werden vor der betreffenden Implementierung spezifiziert. |
| LH-MATH-011 | ARCH-MUSS | Eine vorhandene C#/.NET-Lösung ist keine automatische C++/iOS-Laufzeitabhängigkeit; SASD Math Toolkit wird nur bei tatsächlich passender, versionierter Schnittstelle wiederverwendet. |

---

## 7. Historisches 41-kompatibles Rechnermodell

### 7.1 Fachliche Zielsetzung

Das langfristige 41-orientierte Rechnermodell soll klassische Bedienung, Register, ALPHA, Flags, Anzeigezustände, normale Tastenprogrammierung und **FOCAL**-Programme mit möglichst modellkonformer Semantik unterstützen. Die Differenz zwischen HP-41C, HP-41CV und ggf. später HP-41CX sowie eingesteckten Modulen muss ausdrückliche Konfiguration bleiben.

Die vollständigen ab Werk vorhandenen **HP-41C-Befehle und Bedienmöglichkeiten** sind **separat** unter [HP-41C-Funktionskatalog](de/HP-41C-FUNKTIONSKATALOG.md) beschrieben. Sie werden hier nicht dupliziert.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-41-001 | ARCH-MUSS | Der 41er-Kern ist von 48er-RPL und moderner ALG-Laufzeit funktional und in seinem historischen Zustand unabhängig. |
| LH-41-002 | LANGFRISTIG-MUSS | Historisch relevante Bedien-, Register-, Stack-, ALPHA-, Flag- und Fehlereffekte werden im jeweils freigegebenen 41er-Kompatibilitätsprofil reproduziert. |
| LH-41-003 | LANGFRISTIG-MUSS | Normale historische Tastenprogramme/FOCAL-Befehle werden anhand separater Modellreferenztests ausführbar. |
| LH-41-004 | ARCH-MUSS | Historische Register können im späteren Kompatibilitätskern **verlustfrei 56 Bit / sieben Byte** abbilden; ein reines `double` genügt für beliebige Rohzustände nicht. |
| LH-41-005 | ARCH-MUSS | Die spätere historische Programmspeicherung muss originale Bytefolgen erhalten können; eine lesbare disassemblierte Befehlsansicht darf nicht die einzige Wahrheit sein. |
| LH-41-006 | LANGFRISTIG-MUSS | Historisch relevante Programmzeiger, Tastenzuweisungen, Verwaltungsregister und Speicheraufteilungen werden für unterstützte Programme modelliert. |
| LH-41-007 | GEPLANT | Angemessene getrennte Modellprofile für HP-41C/CV, optional CX und Speicher-/Funktionsmodule. |
| LH-41-008 | ARCH-MUSS | Normale und synthetische Befehle sollen bei späterer Umsetzung denselben konsistenten **virtuellen** historischen Rechnerzustand verwenden und keine konkurrierenden Gesamtinterpreter benötigen. |

### 7.2 Synthetische Programmierung – `SASD-CALC-COMPAT-041-SYN`

Die synthetische HP-41-Programmierung ist keine zusätzliche mathematische Operatorfamilie, sondern eine eigenständige **historische Programmkompatibilitätsanforderung**. Ihre drei technischen Zielstufen sind:

| Stufe | Status | Inhalt und Abgrenzung |
| --- | --- | --- |
| **A – synthetische Befehle** | LANGFRISTIG-MUSS als Vorstufe | Ausgewählte historische Bytes/Befehle erkennen, dekodieren, ausführen und referenztesten |
| **B – synthetische Programme** | **LANGFRISTIG-MUSS, verbindliches Mindestziel** | Ausgewählte historische synthetische Programme mit benötigten Rohregister-, Status-, Zeiger-, Programmbyte- und Tastenzuweisungseffekten ausführen; reproduzierbare Zustände/Austauschformate |
| **C – erweiterte Speichertricks** | **OPTIONAL** | Byte-Hüpfer/Byte Grabber, ungewöhnliche Programmspeicher- und Firmwareeffekte, besonders tiefe historische Nebenwirkungen |

Die Definition **B ist ein langfristiges Mindestziel, nicht die Behauptung vollständiger Kompatibilität aller denkbaren 1980er-Programme**. A/B/C sind auch **nicht** die Kompatibilitätsstufen K1–K4 oder Roadmap-Meilensteine.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-41S-001 | ARCH-MUSS | Synthetische Bytecodes und historische Zustandsänderungen sind im künftigen 41er-Programmmodell darstellbar. |
| LH-41S-002 | LANGFRISTIG-MUSS | Historische Programmbytes unterstützter Austauschformate können verlustfrei geladen, gespeichert und auf Übereinstimmung geprüft werden. |
| LH-41S-003 | LANGFRISTIG-MUSS | Unterstützte synthetische Befehle und Programme bestehen Byte-, Register-, Zeiger-, Tastenzuweisungs- und Fehler-Referenztests. |
| LH-41S-004 | ARCH-MUSS | Synthetische Operationen greifen ausschließlich auf virtuell geprüfte Register/Speicherbereiche zu und können den Host nicht kompromittieren. |
| LH-41S-005 | ARCH-MUSS | Moderne ALG-Eingabe und normaler RPN-Betrieb bleiben von synthetischen Programmbytes unabhängig. |
| LH-41S-006 | OPTIONAL | Byte-Hüpfer Stufe C und vollständigere historische Firmware-Effekte werden nur nach separater Machbarkeits-/Kostenentscheidung realisiert. |

Historische Referenzwerke werden in [Quellen und Provenienz](en/REFERENCE-SOURCES.md) und [41er-Architektur](en/HISTORICAL-41.md) benannt; historische Programmtexte werden nur bei nachweislich zulässiger Übernahme in das Projekt aufgenommen.

---

## 8. Historisches 48GX-kompatibles Rechnermodell

### 8.1 User RPL, Objekte und wissenschaftliche Funktionen

Das 48GX-orientierte Modell ist **keine bloße Erweiterung des vierstufigen RPN-Stacks**. Es besitzt eine objektorientierte RPL-Umgebung, eigene Daten-/Return-Stacks, Programmobjekte, historische Speicherdarstellungen und benutzerbezogene Verzeichnisse.

Langfristig sind unter anderem logische und historische Objekttypen, Namen/Variablen, Verzeichnisse, Listen, algebraische Objekte, komplexe Zahlen, Vektoren, Matrizen, Kontrollstrukturen, Programme, Fehler und aufrufbare Mathematik zu berücksichtigen. **User RPL hat innerhalb dieser Rechnerfamilie vor System RPL funktionalen Vorrang.**

Ein [eigener HP-48GX-Funktionskatalog](de/HP-48GX-FUNKTIONSKATALOG.md) liegt vor und grenzt die erfassten ROM-Befehlsnameneinträge von weiteren System-RPL-Interna und Erweiterungen ab. Eine Funktionsliste darf nicht ungeprüft aus der 41er-Welt übernommen werden.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-48-001 | ARCH-MUSS | Eine unabhängige 48er-RPL-/Objektlaufzeit ist vorgesehen, nicht ein umbenannter Vier-Ebenen-Stack. |
| LH-48-002 | LANGFRISTIG-MUSS | Historische User-RPL-Programme werden im dokumentierten Funktions- und Modellumfang ausführbar. |
| LH-48-003 | LANGFRISTIG-MUSS | Für unterstützte Objekte werden Typ-, Objekt-, Stack-/Return-Stack- und Ausführungseffekte modellkonform verarbeitet. |
| LH-48-004 | ARCH-MUSS | Das spätere Objektmodell ermöglicht eine für unterstützte historische Fälle **verlustfreie Nibble-/Objekt-/Prolog-Repräsentation** neben modernen logischen Objekten. |
| LH-48-005 | ARCH-MUSS | Historische Saturn-Adressen und Speicherreferenzen werden als **virtuelle** Modelladressen verstanden, niemals als Hostpointer. |
| LH-48-006 | GEPLANT | Varianten der RAM-/ROM-Konfiguration und spätere ROM-Kompatibilitätsprofile werden versionierbar dokumentiert. |
| LH-48-007 | LANGFRISTIG-MUSS | Das Verhalten der jeweils freigegebenen User-RPL-Programme ist mit unabhängigen Objekttyp-/Zustands-/Fehler-Referenztests nachweisbar. |

### 8.2 System RPL – `SASD-CALC-COMPAT-048-SYSRPL`

**LANGFRISTIG-MUSS** ist die **kompatible Ausführung eines definierten, dokumentierten, referenzgeprüften Umfangs historischer System-RPL-Programme**. **Nicht** verpflichtend ist die vollständige Rekonstruktion aller ROM-internen Routinen. Das Ziel wird nach den regulären User-RPL-Grundlagen angegangen und ist kein V1.0-Blocker.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-48S-001 | ARCH-MUSS | System-RPL-Primitive, interne Objekte und systemnahe Ausführungszustände sind getrennt von normalen mathematischen Funktionen behandelbar. |
| LH-48S-002 | LANGFRISTIG-MUSS | Ausgewählte dokumentierte System-RPL-Befehle und historische Programme werden mit definierten Seiteneffekten ausgeführt. |
| LH-48S-003 | LANGFRISTIG-MUSS | `SYSEVAL` (historisch adressbezogen) und `LIBEVAL` (Bibliothekskennung/Aufruf) sind **im freigegebenen Umfang** über kontrollierte virtuelle Zuordnungen unterstützbar. |
| LH-48S-004 | ARCH-MUSS | ROM-Profile, historische Systemadressen und Bibliothekskennungen werden getrennt von Hostfunktion/-adresse verwaltet. |
| LH-48S-005 | LANGFRISTIG-MUSS | Unterstützte Systemobjekte, Daten-/Return-Stack-Zustände, Speicher- und Programmfehler bestehen reproduzierbare Modelltests. |
| LH-48S-006 | ARCH-MUSS | Fehlerhafte System-RPL-Programme dürfen keine realen Hostspeicher-/Dateisystemzugriffe erzwingen. |
| LH-48S-007 | LANGFRISTIG-MUSS | User-RPL-Regressionen müssen auch nach Ergänzung von System-RPL-Primitiven bestehen. |
| LH-48S-008 | OFFEN | Welche historische ROM-Version und welche konkreten Systemprimitive zuerst unterstützt werden, wird vor M4 anhand Referenzprogrammen entschieden. |

### 8.3 Saturn-Maschinensprache – `SASD-CALC-COMPAT-048-SATURN`

Die spätere Nachbildung historischer **Saturn-Instruktionen**, CPU-Zustände und gegebenenfalls Maschinenprogrammschnittstellen bleibt **OPTIONAL**. Sie darf nicht vorzeitig zur Bedingung für User RPL, den zugesagten System-RPL-Teilumfang oder die iPhone-V1 werden. Ob einzelne systemnahe Referenzprogramme tiefere CPU-/Firmware-Nachbildung erfordern, ist vor konkreter Freigabe empirisch zu klären.

---

## 9. Historische Erweiterungsmodule und Funktionsüberschneidungen

### 9.1 41er-Module

| Modul / Referenz | Status | Erwarteter Gegenstand |
| --- | --- | --- |
| **HP 82182A Time Module** | GEPLANT, nicht V1 | Zeit-, Datum-, Uhr-/Alarm-Befehle und Zustände; Modellzeit für reproduzierbare Tests |
| **Statistics Pac** | GEPLANT, nicht V1 | Statistik- und Regressionsfunktionen mit 41er-Registern/Stackkonventionen |
| **Advantage Pac** | OPTIONAL als funktionsorientiertes Add-on | Historische Befehlsnamen/Bedienung über weitgehend gemeinsame mathematische Algorithmen |
| Speichermodule / spätere CX-Varianten | GEPLANT/OPTIONAL je Modell | Erweiterung der Ressourcen und des unterstützten Funktionssatzes |

### 9.2 Vorteilspaket als Funktionsreferenz, nicht als zu kopierendes ROM

Vor der Implementierung sind insbesondere folgende Gruppen auf **bereits durch 48GX-Entwicklung oder gemeinsame Mathematik abgedeckte Funktionen** zu prüfen: reelle und komplexe Matrizen, komplexe Arithmetik, Vektoren, numerische Gleichungslösung, Polynome/Nullstellen, Integration, Differentialgleichungen, BIN/OCT/DEC/HEX, Boolesche/Bitoperationen, Statistik/Kurvenanpassung und finanzmathematische Grundfunktionen.

Ein optionales Advantage-inspiriertes Modul liefert möglichst **41-spezifische Befehlsadapter, Stack-/Registereffekte und Hilfetexte**, **keinen zweiten Matrix-/Solver-/Trigonometriekern**. Ein funktionsähnliches Add-on garantiert **keine** Ausführung historischer XROM-Binaries. Eine originalgetreue ROM-Nachbildung ist hiermit **nicht beschlossen**.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-MOD-001 | ARCH-MUSS | Erweiterungen werden pro Rechnermodell, Version, Fähigkeiten, Zustandswirkung und Lizenz/Provenienz erfasst. |
| LH-MOD-002 | GEPLANT | Time- und Statistics-Modulfunktionen werden mit eigenem historischen Befehlskontext und gemeinsamen mathematischen Diensten modelliert. |
| LH-MOD-003 | OPTIONAL | Advantage-Pac-inspirierte Bedien- und Funktionsadapter können später angeboten werden. |
| LH-MOD-004 | ARCH-MUSS | Vor Modulimplementation ist die Überschneidung mit bestehenden 48er-/Core-Funktionen zu prüfen; Doppelentwicklung nur begründet. |
| LH-MOD-005 | ARCH-MUSS | Die Dokumentation trennt funktionale Ähnlichkeit, historische Befehlssemantik, Binär-/XROM-Kompatibilität und tatsächliche Modullaufzeit. |
| LH-MOD-006 | V1-MUSS | Fehlende Module verhindern den ersten klassischen iPhone-Release nicht. |
| LH-MOD-007 | GEPLANT | 48er-Bibliotheken, RAM-Karten, Systemfunktionen und Dateiformate werden nach Referenzprofil und rechtlichem Status separat freigegeben. |

---

## 10. Historische Kompatibilitätsprofile und Speichergrenzen

### 10.1 Drei Konfigurationsdimensionen

Nicht vermischen:

1. **Rechner-/Programmmodell:** Modern ALG, klassischer RPN/41, fortgeschrittener RPL/48.
2. **Interaktive Eingabeart:** RPN/UPN oder ALG, **soweit in der jeweiligen App tatsächlich verfügbar**.
3. **Kompatibilitäts-/Ressourcenprofil:** Modern, Historical Core + Modern Input, Strict Historical.

**Modern** nutzt geräteübliche Ressourcen ohne künstliche historische Grenzen. **Historical Core + Modern Input** erlaubt modernen Komfort bei historisch definierter Ausführung. **Strict Historical** soll später möglichst genaue historische Befehls-, Speicher-, Fehler- und Ressourcenregeln für ein konkret benanntes Modell bereitstellen. Nicht jede beliebige Kombination muss bei jedem App-Release verfügbar sein; Verfügbarkeit ist auszuweisen.

### 10.2 Historische RAM-Modelle

Beim **HP 48GX** sind die historische **128-KiB-RAM-Grundausstattung**, mögliche Erweiterungskarten, reservierte Bereiche, Speicherbelegung, freie-Speicher-Anzeigen und speicherbezogene Fehler von einer allgemeinen 128-KiB-Begrenzung der modernen iPhone-App zu unterscheiden. Für den **HP-41C/CV** gelten die eigenen historischen Register-/Speicher-/Modulregeln und keine pauschal aus dem 48GX übernommene Grenze.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-MEM-001 | ARCH-MUSS | Moderne Rechnerprofile dürfen nicht künstlich auf historisches Basis-RAM begrenzt werden. |
| LH-MEM-002 | ARCH-MUSS | Historische Speicherprofile sind **pro Modell und Erweiterungszustand** definierbar, nicht als ein globales Byte-Limit. |
| LH-MEM-003 | GEPLANT | Strict Historical kann historische Speicherpartitionen, Allokation, Freispeicherabfrage und Speicherfehler entsprechend einer Referenzkonfiguration nachbilden. |
| LH-MEM-004 | GEPLANT | Historical Core + Modern Input trennt Komforteingabe vom historisch begrenzten Ergebnis-/Programmzustand. |
| LH-MEM-005 | ARCH-MUSS | Virtueller Rechneradressraum, tatsächlicher Hostspeicher und angezeigte historische Speichernutzung bleiben unterscheidbar. |
| LH-MEM-006 | ARCH-MUSS | Historische Speicherkonfiguration/ROM-Profil werden bei relevanten Snapshots/Tests zusammen mit dem Zustand identifizierbar. |
| LH-MEM-007 | OPTIONAL | Didaktische Speicher-/Registerinspektoren und visualisierte historische Belegung werden später geprüft. |
| LH-MEM-008 | GEPLANT | Unzulässige historische Zugriffe führen zu kontrolliertem virtuellen Fehlerverhalten, niemals zu Hostzugriffen. |

---

## 11. Bedienoberflächen, Geräte und Darstellung

### 11.1 iPhone zuerst

Das erste Hauptgerät ist das **iPhone**, ausdrücklich einschließlich eines **iPhone-XS-Zielgeräts**, soweit ein geeignetes Apple-Toolchain-/iOS-Deployment-Ziel praktisch verifiziert werden kann. Die App soll im **Hochformat den Rechner selbst** zeigen: Display, Stack-/Statusanzeige, sinnvoll vollständiges Tastenfeld, erforderliche Shift-/ALPHA-Ebenen und gegebenenfalls sechs kontextbezogene Soft-Menütasten. Kein permanenter Editor, keine seitliche Programmierumgebung, kein Konto-/Webbereich und kein Werbebanner.

Die bisher diskutierten Entwürfe sind **Gestaltungsreferenzen**, nicht verbindliche Tasten- oder historische Gehäusezeichnungen: [iPhone-Konzept](images/ios-calculator-concept.svg), [Desktop-Konzept](images/desktop-workspace-concept.svg), [Icon-Konzept](images/science-icon-concept.svg). Diese SVG-Dateien sind Neuzeichnungen, **keine pixelidentischen Original-PNGs und keine echten Screenshots einer lauffähigen App**. Originaldateinamen aus dem Projekt: `SASD RPN Calculator on iPhone.png` und `SASD RPN Calculator SC-48 Interface.png`; Details in [Bildherkunft](images/README.md).

### 11.2 Spätere Desktop-Umgebung

Windows, Linux und macOS sollen später eigenständige Oberflächen ermöglichen. Ein **Desktop-Arbeitsplatz** darf neben dem Rechner einen Programmeditor, Stack-/Register-/Variableninspektor, Programmbibliothek, Bibliotheks-/Dateiverwaltung, Debugger und Diagnosen darstellen. Diese Werkzeuge sind **nicht** verpflichtend für den iPhone-Betrieb. Tastatur/Maus und Touch müssen auf die gleichen fachlichen Kernkommandos führen. Für **iPad** sind größere Layouts möglich; **Android** bleibt eine spätere Plattformoption.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-UI-001 | V1-MUSS | iPhone-Hochformat nutzt die verfügbare Fläche für einen vollständigen, gut lesbaren und bedienbaren Rechner. |
| LH-UI-002 | V1-MUSS | V1-Tasten einschließlich freigegebener Zweit-/ALPHA-Funktionen sind tatsächlich zugänglich; kein Verlust durch Bildvorlagen. |
| LH-UI-003 | V1-MUSS | Schriftgrößen, Touchziele, Safe Areas, Erreichbarkeit und VoiceOver/Accessibility werden am iPhone XS überprüft. |
| LH-UI-004 | V1-MUSS | Verlässliche Anzeige von Stack-/Ergebnis-/Statuswerten, Winkel-/Moduszuständen und verständlichen Fehlern. |
| LH-UI-005 | V1-MUSS | Dezenter SASD-Link oben links, ohne störende Überlagerung von Display oder Tasten. |
| LH-UI-006 | ARCH-MUSS | Alle UI-Ereignisse delegieren Berechnung/State-Mutationen an testbare Kern- oder Anwendungsoperationen; keine eigene Mathematik in Button-Callbacks. |
| LH-UI-007 | GEPLANT | Desktopoberflächen erlauben vollständige Tastatureingabe algebraischer Ausdrücke und RPN-Steuerung. |
| LH-UI-008 | OPTIONAL | Editoren, Variablen-/Stackinspektoren, Debugger und Programm-/Bibliotheksansichten am Desktop. |
| LH-UI-009 | GEPLANT | iPad/macOS/Windows/Linux erhalten später angemessene native oder portable Frontends; Android ist ein langfristiger Kandidat. |
| LH-UI-010 | ARCH-MUSS | Illustrationen und eigentliche App-Screenshots werden klar unterschieden; die historische Tastaturinventur basiert auf überprüften Quellen, nicht auf generierten Bildern. |
| LH-UI-011 | OFFEN | Genaue Display-/Tastenbelegung, Abmessungen, Querformat, endgültige Farben/Skins und Apple-Mindestversion werden vor UI-Abnahme fixiert. |

---

## 12. Rechnerzustand, Programmverwaltung und Datenaustausch

Rechnerzustand bedeutet mehr als den sichtbaren X-Wert: Dazu zählen soweit freigegeben Stack einschließlich Lift-Zustand/LAST X, Register, Modus, Eingabepuffer, Fehlerstatus, variables Profil und gegebenenfalls Programme, Objekte und historische Ressourcen.

Bei der späteren Programmkompatibilität sind **Programmdatei**, **historisches Byte-/Nibble-Abbild**, **Bibliothek/ROM-Modul** und **vollständiger Rechner-Snapshot** unterschiedliche Artefakte, die nicht gegenseitig verwechselt werden dürfen.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-DATA-001 | V1-MUSS | Rechnerzustand wird nach Suspendierung, Neustart und üblichen App-Lebenszyklusereignissen zuverlässig gespeichert/wiederhergestellt. |
| LH-DATA-002 | V1-MUSS | Das Zustandsformat ist versioniert; beschädigte/inkompatible Daten werden kontrolliert erkannt und behandelt. |
| LH-DATA-003 | ARCH-MUSS | Fehler beim Einlesen oder Rechnen verursachen keine unkontrollierte partielle Zustandsbeschädigung; gültige vorherige Zustände bleiben wiederherstellbar. |
| LH-DATA-004 | ARCH-MUSS | Persistenzformat und Speicherung unterscheiden fachlichen Zustand von iOS-/Desktop-Pfaden, Dialogen und Dateisystemzugriff. |
| LH-DATA-005 | LANGFRISTIG-MUSS | Für freigegebene historische Programme wird ein dokumentierter Import/Export angeboten, soweit unterstützte Dateiformate und rechtliche Grundlagen vorliegen. |
| LH-DATA-006 | LANGFRISTIG-MUSS | In unterstützten Byte-/Nibble-Formaten versprochene Roundtrips erhalten historische Daten verlustfrei. |
| LH-DATA-007 | GEPLANT | Programmverwaltung, Bibliotheken, Name/Version, Speicherzustände und Register-/Programmexport werden auf späteren Oberflächen zugänglich. |
| LH-DATA-008 | ARCH-MUSS | Gespeicherte Zustände enthalten ausreichende Versions-/Modell-/Profilinformationen für reproduzierbare Tests und spätere Migration. |
| LH-DATA-009 | OFFEN | Konkretes Datenschema, Autosave-Auslöser, atomare Schreibstrategie, Export-/Backupformate und Kollisionsregeln werden vor der jeweiligen Umsetzung spezifiziert. |

---

## 13. Online-Hilfe, Offline-Handbuch und Trainingsprogramm

Obwohl historisch von einer **Online-Hilfe** gesprochen wurde, darf die App **für grundlegende Hilfe keinen Internetzugang voraussetzen**. Die Hilfe ist innerhalb der App erreichbar und soll mindestens Deutsch und Englisch unterstützen.

Drei Ebenen:

1. **Kontextbezogene Hilfe:** Was tut eine Taste/Funktion, welche Argumente werden erwartet, was bedeutet der aktuelle Fehler oder Modus? Für freigegebene V1-Funktionen ein kurzer Offline-Grundumfang.
2. **Vollständige durchsuchbare Referenz:** UPN-Grundlagen, ALG-Syntax, Stack, Register, Programme, historische Profile, unabhängige Erläuterungen und aktuelle Abdeckungsstände.
3. **Didaktisches Lernen:** Gegenüberstellung derselben Rechnung als RPN/ALG, Stackvisualisierung, Operatorpriorität, typische Bedienfehler, interaktive Übungen und später Debugging-/AST-Auswertungsschritte.

Ein **separater zweiter didaktischer Rechenkern** ist unerwünscht: Übungsaufgaben sollen durch dieselben mathematischen und zustandsführenden Komponenten laufen. Die Lernansichten können später Erklärungsspuren der echten Ausführung verwenden.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-HELP-001 | V1-MUSS | Verständlicher kurzer **offline verfügbarer** Einstieg in die klassische RPN-Bedienung und Erklärung der freigegebenen Fehler/Funktionen. |
| LH-HELP-002 | GEPLANT | Kontextbezogene Tasten-/Funktionshilfe und vollständiges durchsuchbares DE/EN-Handbuch. |
| LH-HELP-003 | GEPLANT | Vergleichende Lernbeispiele für ALG und RPN, Klammern/Prioritäten und relevante Stackaktionen. |
| LH-HELP-004 | GEPLANT | Interaktive Übungen und Schritt-für-Schritt-Ansichten über echte Kernoperationen. |
| LH-HELP-005 | OPTIONAL | Ausführliche historische Programmierkurse (FOCAL, Synthetic, User/System RPL), AST-/Debugger-/Speichervisualisierung. |
| LH-HELP-006 | ARCH-MUSS | Hilfe und Tests beziehen sich auf dieselben tatsächlich unterstützten Funktions-/Kommandometadaten und weisen fehlende Funktionen aus. |

---

## 14. Gemeinsame Komponenten und Wiederverwendungsstrategie

### 14.1 Ein mathematischer Unterbau, getrennte Laufzeiten

Das logische Zielbild **SASD Mathematical Core** umfasst gemeinsame Algorithmen für Grundmathematik, Numerik, Matrizen, Statistik, komplexe Zahlen, Einheiten, Zahlensysteme und nach Bedarf gemeinsame Typen/Formatdienste. Eine einzige fachliche Funktion darf mehrere Aufrufwege besitzen – beispielsweise ALG `sin(x)` und RPN `SIN` –, jedoch nicht automatisch identische historische Stack-/Rundungseffekte.

Gemeinsam nutzbar sind außerdem Parser, Diagnosekatalog, Testwerkzeuge, definierte Daten-/Formatdienste und Build-Templates. **Nicht gemeinsam zu vereinheitlichen** sind historische 41er-Rohregister und FOCAL, 48er-RPL-Objekte/Systemaufrufe, produktspezifische Finanzmodelle, App-UI und ihre Freigaben.

### 14.2 Entwicklungs- und Repository-Randbedingungen

| ID | Status | Forderung |
| --- | --- | --- |
| LH-ARCH-001 | ARCH-MUSS | Wissenschaftlicher Kern unabhängig von Benutzeroberflächen und Betriebssystemen; bevorzugte Basis **C++20** mit **CMake** und automatisierten Tests. |
| LH-ARCH-002 | ARCH-MUSS | Separate fachliche Ausführungsmodelle für Classic RPN/41, ALG und RPL/48; nur geeignetes gemeinsames Verhalten wiederverwenden. |
| LH-ARCH-003 | ARCH-MUSS | Gemeinsame mathematische Algorithmen dürfen keine versteckten HP-41-/HP-48- oder GUI-Abhängigkeiten voraussetzen. |
| LH-ARCH-004 | ARCH-MUSS | Beabsichtigte Erweiterungen dürfen bereits freigegebene Stack-, Programm- oder Fehlerspezifikationen nicht stillschweigend verändern. |
| LH-ARCH-005 | ARCH-MUSS | Neue Funktionen verfügen über definierte Typ-, Fehler-, Zustands- und Testverträge; begründete historische Unterschiede bleiben zulässig. |
| LH-ARCH-006 | ARCH-MUSS | Getrennte Scientific-App-Targets sind unabhängig baubar und releasbar, auch wenn sie sich Quellbibliotheken teilen. |
| LH-ARCH-007 | ARCH-MUSS | Keine zwingende Laufzeitkopplung von Scientific und Financial, keine gemeinsam vorausgesetzte Internet-/Serverinstanz. |
| LH-ARCH-008 | GEPLANT | Versionierte Bibliotheken/Pakete werden **erst bei echtem zweitem Verbraucher** gegenüber Kopie und Herkunftsnachweis geprüft; kein frühzeitiges unnötiges Framework. |
| LH-ARCH-009 | ARCH-MUSS | Wird Code zwischen Projekten kopiert, werden Quelle, Commit/Version, Lizenz, Änderungen und Wartungsverantwortung dokumentiert. |
| LH-ARCH-010 | GEPLANT | Native iOS-Oberfläche mit **SwiftUI** und wohldefinierter möglichst versionierter C-ABI-Brücke zu C++; konkrete Lifetime-/Fehlerregeln vor Implementierung festlegen. |
| LH-ARCH-011 | ARCH-MUSS | Keine nativen C++-STL-Datentypen unkontrolliert über eine öffentliche C-/Swift-ABI-Grenze geben. |
| LH-ARCH-012 | ARCH-MUSS | Historischer 41er-Bytecode, 48er-RPL und moderne ALG-ASTs bleiben unabhängige Programm-/Syntaxrepräsentationen. |
| LH-ARCH-013 | ARCH-MUSS | Die Ablage im Monorepo und die spätere Weitergabe von Bibliotheken dürfen keine künstlichen wechselseitigen Abhängigkeiten erzeugen. |

**Geplante, nicht zwingend heute anzulegende Struktur:** `apps/` (ALG, Classic RPN, Advanced RPL, CLI und native Plattformfrontends), `calculators/` (ALG-Kontext, 41er-, 48er-Ausführung), `libs/` (Mathematik, numerische Typen, ALG-Ausdrücke, Funktionskatalog), `platform/` (API/Bridge/Profile), `learning/`, `tests/`, `docs/`, `tools/`, `.github/`. Ein Verzeichnisname ist **kein** Implementierungsnachweis.

---

## 15. Nichtfunktionale Qualität, Stabilität, Portabilität und Datenschutz

| ID | Status | Forderung / Nachweis |
| --- | --- | --- |
| LH-NF-001 | V1-MUSS | Für alle freigegebenen Funktionen existieren nachvollziehbare automatisierte positive, negative und Grenzfalltests. |
| LH-NF-002 | V1-MUSS | Rechen-, Anzeige- und Speicherfehler dürfen zu keinem bekannten kritischen Absturz, Verlust gültiger Zustände oder unbemerktem Falschergebnis führen. |
| LH-NF-003 | V1-MUSS | Wiederaufnahme nach Unterbrechung und Neuinstallation/Upgrade entsprechend freigegebener Datensicherungsregeln wird praktisch getestet. |
| LH-NF-004 | V1-MUSS | Bedienbarkeit, Lesbarkeit, Touch, Zugänglichkeit und Offline-Betrieb werden auf echten unterstützten Geräten – besonders iPhone XS – überprüft. |
| LH-NF-005 | ARCH-MUSS | Änderungen an gemeinsamer Mathematik oder öffentlichen Schnittstellen lösen Tests aller betroffenen Calculator-Engines aus. |
| LH-NF-006 | ARCH-MUSS | Fehler und Diagnosen sind strukturiert; falsche Typen, Stackunterlauf, Division durch null, mathematische Definitionsfehler, Überläufe und Ressourcenprobleme bleiben unterscheidbar. |
| LH-NF-007 | ARCH-MUSS | Importierte Programme, beschädigte Snapshots und historische Speicherzugriffe gelten als nicht vertrauenswürdige Eingabe und werden sicher begrenzt. |
| LH-NF-008 | ARCH-MUSS | Keine Ausführung beliebiger Host-Shell-Kommandos, Hostpointer oder unkontrollierter nativer Plug-ins durch historische Programme. |
| LH-NF-009 | ARCH-MUSS | Fachlogik ist unter Windows, Linux und macOS in einer CI-Build-/Testmatrix prüfbar; iOS-Freigabe verlangt zusätzliche Apple-Tests. |
| LH-NF-010 | ARCH-MUSS | Numerische Genauigkeit, Anzeige-/Eingabetransformation, Rundungsregeln und Vergleichstoleranzen sind kontext- und versionierbar dokumentiert. |
| LH-NF-011 | ARCH-MUSS | Keine abgeleiteten Kompatibilitätsversprechen ohne Modell-/ROM-Profil, Referenzfall und konkrete Testergebnisse. |
| LH-NF-012 | ARCH-MUSS | Nutzerdaten werden lokal verarbeitet; keine erforderliche Registrierung, Cloud-Synchronisation oder Telemetrie für die erste App. |
| LH-NF-013 | ARCH-MUSS | Bei App-Store- und Lizenz-/Datenschutzerklärungen muss tatsächliches Verhalten dem angegebenen entsprechen. |
| LH-NF-014 | GEPLANT | Systematischer Regressionstest für Zustandsformate, ältere Programme, zusätzliche Module und zukünftige App-Varianten. |
| LH-NF-015 | ARCH-MUSS | Tests sind soweit möglich deterministisch, reproduzierbar und automatisiert; Referenzdaten und Herkunft werden dokumentiert. |

**Bereits nachweisbarer IST-Stand (Repositoryprüfstand 21.11.2026):** kleiner generischer C++20-RPN-Stack mit Push/Dup/Swap/Drop/Clear und `+−×÷`, Entwickler-CLI und CTest-Suite; keine iOS-App, keine fertigen wissenschaftlichen Funktionen/Registrier-/Persistenzsuite und kein nachgewiesener historischer Emulator. Ein früherer GitHub-Actions-Build der vorhandenen C++-Basis war erfolgreich; daraus folgt **keine** historische K1-Konformität oder App-Store-Freigabe.

---

## 16. Rechtliche Randbedingungen, Quellen und Marken

| ID | Status | Forderung |
| --- | --- | --- |
| LH-LEGAL-001 | ARCH-MUSS | Unabhängige, eigenständig geschriebene SASD-Implementierung; keine ungeprüfte Übernahme von HP-ROMs, Firmware, historischen Betriebssystemabbildern oder Quellcode. |
| LH-LEGAL-002 | ARCH-MUSS | Geschützte historische Handbücher, kommerzielle Programmsammlungen, Bilder und Originalressourcen werden nicht ohne Nutzungsrechte mitgeliefert. |
| LH-LEGAL-003 | ARCH-MUSS | Historische Modellbezeichnungen dienen in technischen Kompatibilitätsdokumenten der sachlichen Identifikation; App-Branding verwendet SASD ohne irreführende Herstellerzuordnung. |
| LH-LEGAL-004 | ARCH-MUSS | Für Referenzprogramme und Testdaten werden Quelle, Lizenz/Nutzungsrecht, Modell/Version, Beobachtung und Datum erfasst. |
| LH-LEGAL-005 | ARCH-MUSS | Im Repository vorhandene **MIT-Lizenz** und Urheberhinweise werden nicht stillschweigend geändert; Fremdbibliotheken werden vor Aufnahme separat geprüft. |
| LH-LEGAL-006 | V1-MUSS | Die App-Store-Veröffentlichung besitzt rechtsgeprüfte App-Grafik, Screenshots eines **echten laufenden Builds**, korrekte Datenschutzangaben und erforderliche Rechte. |
| LH-LEGAL-007 | OFFEN | Umfang konkreter historischer Kompatibilitätsaussagen und Marken-/Designrechtsprüfung vor Veröffentlichung festlegen. |

**Referenzliteratur:** Historische Werke zu synthetischer HP-41-Programmierung (Wickes, Gosmann), zu System RPL (Donnelly, Kalinowski), offizielle Modellhandbücher und geeignete unabhängige Emulatoren sind Forschungs- und Testquellen. Ausführliche Links: [Quellenverzeichnis](en/REFERENCE-SOURCES.md). Sie sind **keine** automatische Erlaubnis zur Weitergabe historischer Materialien.

---

## 17. Historische Kompatibilitätsstufen und Nachweisgrad

### 17.1 Vier Zielstufen K1–K4

| Stufe | Ziel | Typischer Entwicklungspfad |
| --- | --- | --- |
| **K1 – klassische Funktionskompatibilität** | Historisch orientierte Tasten, Stack, Register, Mathematik, Fehler, definierte Zahlensemantik | M1/M2 in **einem begrenzten belegten Ausschnitt** |
| **K2 – historische Anwenderprogramme** | FOCAL-/Tastenprogramme und User RPL mit jeweiliger Programmlaufzeit | M3 |
| **K3 – systemnahe Kompatibilität** | Synthetic HP-41, System RPL, interne Schnittstellen, entsprechende Module | M4 |
| **K4 – Maschinenkompatibilität** | Nut-/Saturn-CPU-Instruktionen, Hardware- und ggf. Betriebssystemumgebung | M5, OPTIONAL |

Eine App kann K1 **teilweise** nachweisen, ohne K1 vollständig oder K2 überhaupt zu erfüllen. Ebenso kann eine einzelne System-RPL-Funktion unterstützt sein, ohne ein vollständiges System-RPL-ROM nachzubilden.

### 17.2 Belege für eine konkrete Produktversion

Für jedes Kompatibilitätsversprechen sind mindestens anzugeben: SASD-Version/Commit, Rechnerfamilie/Modell, ROM-/Modul-/Speicherprofil, Befehl/Programm, erwartetes Ergebnis **und relevanter Zustand**, Referenzprovenienz, Test/Beobachtung, Status (*unterstützt, teilweise, nicht unterstützt, ungetestet*), bekannte Abweichungen und Datum. Zusätzlich kann innerhalb einer Stufe unterschieden werden: **syntaktisch erkannt**, **funktional ausgeführt**, **verhaltensgetreu**, **system-/speichergetreu**, **maschineninstruktionsgetreu**.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-COMP-001 | ARCH-MUSS | K1–K4 werden in der Dokumentation konsequent von M0–M5 getrennt. |
| LH-COMP-002 | ARCH-MUSS | Jede veröffentlichte Kompatibilitätsangabe verweist auf modell- und versionsbezogene Nachweise. |
| LH-COMP-003 | LANGFRISTIG-MUSS | FOCAL und User RPL erhalten eigenständige K2-Testkataloge. |
| LH-COMP-004 | LANGFRISTIG-MUSS | Synthetische 41er-Programme Stufe B und ausgewähltes System RPL erhalten eigenständige K3-Testkataloge. |
| LH-COMP-005 | OPTIONAL | CPU-/Firmware-/OS-Nachbildung und Maschinenprogrammtests werden erst bei ausdrücklicher M5-Entscheidung verpflichtend. |

---

## 18. Roadmap und Freigabestrategie

### 18.1 Maßgebliche Meilensteine

Die früher diskutierte technische **M0–M6**-Aufteilung ist durch eine **einheitliche releaseorientierte M0–M5-Roadmap** konsolidiert. Darin bleiben ALG, wissenschaftlicher Ausbau, Module, Training und zusätzliche Plattformen als **parallele Entwicklungslinien** erhalten, aber sie dürfen den kritischen Pfad zur klassischen V1 nicht verdrängen.

| Meilenstein | Zweck und Ergebnis | Verbindlichkeit |
| --- | --- | --- |
| **M0 – Projektfundament** | Produkt-/Funktionsabgrenzung, Architektur, Key-/State-/Numerikverträge, C++20/CMake, Tests, CI, Lizenz/Quellen, iOS-Machbarkeit | Voraussetzung für gezielten M1-Aufbau |
| **M1 – klassischer Rechnerkern** | Verlässliche RPN-/Stack-/Register-/Basiswissenschaftsoperationen, Zustands-/Fehlerverträge und automatisierte Tests | **V1-Pflichtgrundlage** |
| **M2 – iPhone-App / App Store V1.0** | Vollständige freigegebene Tastatur, hochwertige Bedienung, Persistenz, Offline, SASD-Marke, iPhone XS/Apple-Gerätetests, Legal/Store-Gates | **Erstes Produktziel** |
| **M3 – historische Anwenderprogramme** | 41er-FOCAL und 48er-User-RPL, Programme, Import/Export und Referenzprüfungen; inkrementelle App-Updates | LANGFRISTIG-MUSS im zugesagten Umfang |
| **M4 – erweiterte historische Kompatibilität** | Synthetic 41 A/B, ausgewähltes System RPL, Module, historische Profile und Systemfunktionen | Langfristige Teilziele, **kein V1-Blocker** |
| **M5 – CPU-/OS-Forschung** | Nut-/Saturn-CPU, Maschinenprogramme, historische Hardwareschnittstellen und optionale OS-Fragen | **OPTIONAL, eigenständiger Forschungspfad** |

M3/M4/M5 müssen nicht vollständig strikt nacheinander abgearbeitet werden. Referenzanalysen und isolierte Grundlagen können parallel erfolgen; **es entsteht kein zweites widersprüchliches Meilensteinsystem**.

### 18.2 Was V1.0 ausdrücklich nicht voraussetzt

- Vollständige HP-41-FOCAL-Programmierung oder 48GX-User-RPL-Programmierung.
- Synthetische HP-41-Programme und Byte-Hüpfer.
- System RPL oder ROM-interne Systemroutinen.
- Originale ROMs/Firmware/OS und Nut-/Saturn-Maschinenemulation.
- Vollständige historische RAM-/ROM-/Registerabbilder, Speicher- oder Zusatzkarten.
- Time-, Statistics- und Advantage-Pac-Module.
- Eigenständige ALG-App oder in Classic RPN integrierter ALG-Modus.
- Fertige Desktop-IDE, Android/iPad-Parität und ausführliche interaktive Lernkurse.
- Komplette HP-41C-/48GX-Kommandofunktionsabdeckung.

Die Abwesenheit dieser Funktionen **muss in der V1-Dokumentation klar angegeben werden**, ist aber alleine **kein Grund, eine ansonsten reife V1 zurückzuhalten**.

### 18.3 Freigabegates

| ID | Status | Abnahmekriterium für M1/M2 |
| --- | --- | --- |
| LH-REL-001 | V1-MUSS | Die verbindlich freigegebene V1-Tasten-/Funktionsmatrix ist vollständig implementiert und für jede Funktion getestet. |
| LH-REL-002 | V1-MUSS | Stack-, Register-, Eingabe-, Zahlentyp-/Rundungs- und Fehlerverhalten bestehen dokumentierte Referenztests. |
| LH-REL-003 | V1-MUSS | Wiederherstellung nach Suspend/Neustart/Upgrade und Behandlung beschädigter Daten sind praktisch geprüft. |
| LH-REL-004 | V1-MUSS | Reale unterstützte iPhones, insbesondere das XS-Ziel, haben Touch-/Lesbarkeits-/Accessibility-/Offline-/Stabilitätstests bestanden. |
| LH-REL-005 | V1-MUSS | Alle relevanten C++- und iOS-Tests, Release-/Lizenz-/Datenschutz-/App-Store-Prüfungen sind mit Commit, Version und Testergebnis dokumentiert. |
| LH-REL-006 | V1-MUSS | Keine bekannten schwerwiegenden Rechen-, Absturz-, Sicherheits- oder Datenverlustfehler verbleiben. |
| LH-REL-007 | V1-MUSS | SASD-Kennzeichnung, Bildrechte und echte Store-Screenshots sind geprüft. |
| LH-REL-008 | V1-MUSS | Release Notes geben **tatsächliche** Funktions-/Kompatibilitätsabdeckung und bekannte Grenzen an. |
| LH-REL-009 | ARCH-MUSS | Kein späterer historischer Funktionswunsch wird ohne neue ausdrückliche Entscheidung zum M2-Releaseblocker. |

---

## 19. Test-, Referenz- und Nachweismatrix

### 19.1 Fachliche Testgruppen

| Testfamilie | Beispiele und Ziel |
| --- | --- |
| **RPN / Stack** | `3 ENTER 4 ENTER 5 × + → 23`, `Y−X`, ENTER/LAST X, Lift/Drop/Roll/Swap, Registerzustand |
| **Basisnumerik** | Division durch null, Definitionsbereich von Log/Wurzel, Über-/Unterlauf, Winkelmodi, Fehlerrollback |
| **ALG / Parser** | `3+4×5=23`, `(3+4)×5=35`, `2^3^2=512`, falsche Klammern, unäre Zeichen, Tokenpositionen |
| **Cross-Input** | Mathematisches Ergebnis bei gleicher Zahl-/Winkelumgebung vergleichen; historische Zustandsunterschiede bleiben erlaubt |
| **Persistenz** | Speichern/Wiederherstellen, unvollständige Dateien, Schemawechsel, Unterbrechungen |
| **41 FOCAL** | Historische Befehle und Programmabläufe mit Register-/Flag-/Stackgoldens |
| **41 Synthetic** | 56-Bit-Roundtrip, Bytefolgen, Dekodierung, Status-/Zeiger-/Tastenzuweisungseffekte; C optional |
| **48 User RPL** | Objekte, Daten-/Return-Stack, Variablen, Programme, Fehler, Import/Export |
| **48 System RPL** | Systemobjekte, `SYSEVAL`/`LIBEVAL`, ROM-Profile, virtuelle Adressen und kontrollierte Fehler |
| **Modul / Speicherprofil** | Modellkonfiguration, freier Speicher, Karten, Zeit/Statistik, Capability-Konflikte |
| **Sicherheit** | Ungültige Bytes, große Ausdrücke, korrupte Daten, feindliche virtuelle Zugriffe; keine Hostkompromittierung |
| **UI / Gerät** | Touch, Safe Area, VoiceOver, Hochformat, Offline, Speicherung, echte App-Store-Screenshots |

### 19.2 Nachweisanforderungen

| ID | Status | Forderung |
| --- | --- | --- |
| LH-TEST-001 | ARCH-MUSS | Jede neu freigegebene fachliche Operation wird durch reproduzierbare Kern-/Zustands-/Fehlertests abgesichert. |
| LH-TEST-002 | ARCH-MUSS | Historische Tests nennen rechtlich zulässige Referenz, Modellprofil und erwartete **Zustandsänderung**, nicht bloß Ergebniszahl. |
| LH-TEST-003 | ARCH-MUSS | Anpassungen an gemeinsamen Bibliotheken prüfen die betroffenen RPN-, ALG- und RPL-Konsumenten. |
| LH-TEST-004 | ARCH-MUSS | CI auf Linux, Windows und macOS ist nötig, beweist jedoch weder iPhone-Gerätequalität noch App-Store-Freigabe. |
| LH-TEST-005 | GEPLANT | Erweiterte automatisierte Parser-Grenzwert-, Speicher-/Snapshot-, Import-/Export- und historische Programmregressionen. |
| LH-TEST-006 | OPTIONAL | K4-Maschinenausführungstests erst bei freigegebener M5-Forschung. |

Für bekannte Beispielaufgaben können die Testdaten aus diesem Lastenheft übernommen werden. Sie sind **noch keine** empirisch validierten HP-41C-/48GX-Referenzbeobachtungen. Historisch begründete numerische Unterschiede sind explizit zu protokollieren.

---

## 20. Organisation der Entwicklung und Codex-Regeln

- Das **GitHub-Repository** ist die zentrale Quelle für Produktdokumente, Quellcode, CMake-Targets und CI. Änderungen an `main` sind für die Einzelentwicklerpraxis zulässig, wenn sie kohärent, prüfbar und nicht destruktiv sind; riskante parallele Änderungen können getrennte Branches/Worktrees verwenden.
- Die Architektur unterstützt getrennte Aufgabenbereiche für mathematischen Kern, ALG-Parser, klassischen RPN-Zustand, 41er/48er-Kompatibilität, Plattform-/App-Anbindungen, Tests und Dokumentation.
- Bei neuen Funktionen **erst prüfen**, ob ein geeignetes gemeinsames mathematisches Verfahren schon vorhanden ist. Fachlogik in Testtreiberschichten und UI-Eventhandlern ist zu vermeiden.
- Öffentliche APIs benötigen benannte Verantwortlichkeit, dokumentierte Verträge, Fehlersemantik und verständliche Kommentare zu historischen Besonderheiten, Invarianten und Sicherheitsgrenzen.
- Jede Änderung an shared interfaces benötigt Folgenabschätzung, Regressionstests und aktualisierte Anforderungen/Kompatibilitätsdokumentation.
- Codex darf **nicht** aus einem künftig geplanten, optionalen oder bloß im Screenshot gezeigten Feature einen Implementierungs-/Releaseanspruch ableiten.
- Releases, CI-Status, Kompatibilitätsquoten und echte iPhone-Prüfungen dürfen **nicht erfunden** werden.
- Die primäre Entwicklungspriorität ist: **Korrektheit/Stabilität der klassischen iPhone-V1 vor Vollständigkeit historischer Spezialfälle**.

| ID | Status | Forderung |
| --- | --- | --- |
| LH-PROC-001 | ARCH-MUSS | Aufgaben mit eindeutiger Modulzuständigkeit, Abhängigkeiten und überprüfbaren Abnahmekriterien dokumentieren. |
| LH-PROC-002 | ARCH-MUSS | Neue Funktionen mit Tests und angemessener Entwickler-/Benutzerdokumentation liefern. |
| LH-PROC-003 | ARCH-MUSS | Änderungen am Funktionsumfang in README, Lasten-/Folgespezifikationen, Roadmap und Release-Matrix nachvollziehen. |
| LH-PROC-004 | ARCH-MUSS | CI-Fehler aus eigenen Änderungen beheben und nur tatsächlich beobachtete erfolgreiche Prüfungen melden. |
| LH-PROC-005 | ARCH-MUSS | Keine unkoordinierten Änderungen an gemeinsam genutzten APIs durch parallele Codex-Aufträge. |
| LH-PROC-006 | ARCH-MUSS | Keine unautorisierte Lizenz-/Marken-/ROM-Verwendung oder Neudefinition freigegebener historischer Semantik. |

---

## 21. Risiken, Zielkonflikte und Abhilfen

| Risiko / möglicher Widerspruch | Bewertung | Fachlich verbindliche Behandlung |
| --- | --- | --- |
| **ALG-App** versus RPN-V1.0-Priorität | Hoch | Beide architektonisch berücksichtigen; **RPN-iPhone-V1 hat Ressourcen- und Freigabevorrang** |
| Gemeinsame Mathematik versus abweichende historische Genauigkeit | Hoch | Gemeinsame Algorithmen, ausdrücklich getrennte numerische/profileigene Semantik |
| Historische 41-Register nur als `double` | Hoch | Spätere 56-Bit-Rohrepräsentation verlustfrei ermöglichen |
| Historische 48er-Objekte nur als moderne C++-Werte | Hoch | Verlustfreien historischen Objekt-/Nibble-Kontrakt vor System-RPL-Umsetzung vorsehen |
| Full Historical als V1-Blocker | Kritisch für Termin/Fokus | Ausdrücklich untersagt; späte Profile und Systemfunktionen separat freigeben |
| Original-ROMs/Handbücher aus fremden Quellen | Rechtlich hoch | Clean-room-/Rechteprüfung; keine unautorisierte Verteilung |
| Modellunspezifische virtuelle Speicher- und Stackregeln | Hoch | Eigene 41er- und 48er-Semantik/Referenztests |
| Zu frühes riesiges Shared Framework | Hoch | Kleine getestete Module, auslagern erst bei realem Bedarf |
| Desktop-IDE verdrängt Mobilrechner | Mittel–hoch | Desktop-Ansichten optional, iPhone-Hochformat Rechner-only |
| Screenshots/Moc​kups mit falscher Tastenzuordnung | Mittel–hoch | Bilder sind Inspiration, **nicht** Prüforakel; eigene verifizierte Tastenmatrix |
| Gleichzeitige Scientific-/Financial-Releases | Mittel | Getrennte Repositories, Build-/Release-Pipelines und Abhängigkeiten |
| Optionaler CPU-/OS-Emulator verschlingt Kernentwicklung | Sehr hoch | M5 als eigenständiges optionales Forschungsprojekt |
| App-Store/Apple-Toolchain unterstützt Zielgerät nicht wie angenommen | Hoch | iPhone-XS-/iOS-Mindestversion rechtzeitig prüfen und dokumentieren |
| Fehlende oder rechtlich unklare historische Testprogramme | Hoch | Referenzprovenienz, Freigaben, unabhängige eigene Testfälle |
| Behauptete Funktionsvollständigkeit ohne Tests | Hoch | Funktionskatalog, Implementierungsstatus und tatsächliche Abnahme separat ausweisen |

---

## 22. Ausdrücklich offene Entscheidungen

Diese Fragen werden **nicht** durch das Lastenheft stillschweigend beantwortet. Die ersten sieben Punkte sind **vor Implementierung/Abnahme des betreffenden M1-/M2-Bausteins** zu klären; die übrigen erst bei ihrem Meilenstein.

| ID | Zeitpunkt | Entscheidung / erwartetes Ergebnis |
| --- | --- | --- |
| LH-OD-001 | Vor M1 | Exakte V1-Haupt-/Shift-/ALPHA-Tasten-, Display- und Kommandoliste, unabhängig vom Konzeptbild |
| LH-OD-002 | Vor M1 | Vier-Ebenen-Stackregeln: `ENTER`, Lift, Drop, Roll, LAST X, Eingabepuffer, Clear, Undo, Fehlerrücksetzung |
| LH-OD-003 | Vor M1 | Zahlentyp, Genauigkeit, Rundung, Winkeleinheiten, Über-/Unterlauf und Referenztoleranzen |
| LH-OD-004 | Vor M1/M2 | Zustandsschema, atomare Sicherung, Migration, beschädigte Dateien und Backup-/Exportverhalten |
| LH-OD-005 | Vor M2 | Unterstützte iOS-Minimalversion, Xcode-Toolchain, reale iPhone-XS-Tests, Bundle-ID und App-Signierung |
| LH-OD-006 | Vor M2 | Offizielle SASD-Webadresse für Logo-Link, App-Store-Branding und Bild-/Lizenzprüfung |
| LH-OD-007 | Vor M2 | Konkreter Offline-Hilfe-Mindestumfang, Preismodell innerhalb der Vorgabe „ohne Werbung/Abo“ |
| LH-OD-008 | Vor ALG-Implementierung | Endgültige Parser-Grammatik, Pratt/Recursive-Descent-ADR, Dezimal-/Argumenttrenner, implizite Operatoren und Seiteneffekte |
| LH-OD-009 | Vor eigenständigen ALG-/RPL-Releases | App-Namen, Bundle-IDs, Versionierungs-/Releasekonzept und mögliche kombinierte Modus-App |
| LH-OD-010 | Vor M3 | 41er-FOCAL-Kompatibilitätsumfang, Rohregister/Programmspeicherordnung und legale Referenzprogrammformate |
| LH-OD-011 | Vor M3 | 48er-User-RPL-Objekt-/Nibbleformat, Referenzprofil, Verzeichnisse, Persistenz- und Austauschformate |
| LH-OD-012 | Vor M4 | Synthetische 41er-Befehls-/Programmbeispiele für Stufe A/B; konkreter optionaler Byte-Hüpfer-C-Nutzen |
| LH-OD-013 | Vor M4 | Erstes 48er-ROM-Profil, konkrete System-RPL-Primitive, `SYSEVAL`/`LIBEVAL`-Abdeckung |
| LH-OD-014 | Vor historischer Speichersimulation | Strict-Historical-Detailumfang, 128-KiB-/Kartenkonfigurationen, Speicheranzeige, Fehlersemantik |
| LH-OD-015 | Vor Modulrealisierung | Time-/Statistics-/Advantage-Inventare, fachliche Überschneidungen, XROM- und Lizenzumfang |
| LH-OD-016 | Bei zweitem Bibliotheksnutzer | Gemeinsam versioniertes Paket versus dokumentierte Quellcodekopie; C++-Schnittstelle und Lizenz |
| LH-OD-017 | Bei Financial-Start | Financial-Repository anlegen, TVM-/Finanzkonventionen und eigene Release-Gates spezifizieren |
| LH-OD-018 | Vor M5 | Nut-/Saturn-Maschinenemulation und Betriebssystemforschung wirtschaftlich/technisch gesondert freigeben |
| LH-OD-019 | Bei späterem UX-Ausbau | Freigabe von Desktopeditor, iPad-/Android-/Windows-/Linux-/macOS-Versionen und eigenständiger Trainings-App |
| LH-OD-020 | Bei historischen Funktionskatalogen | Vollständigkeit des HP-48GX-Katalogs, gesonderte Module, jeweilige Quellen- und Rechtslage unabhängig prüfen |

**Explizit nicht offen:** Ob wir die erste App bis zur vollständigen historischen CPU-/ROM-/Programmkompatibilität zurückhalten – **nein**. Ob Scientific und Financial ein Produkt werden – **nein**. Ob UPN/RPN durch ALG ersetzt wird – **nein**.

---

## 23. Fachliche Abnahme und Änderungen des Lastenhefts

### 23.1 Abnahmeverfahren

1. **Anforderungen freigeben:** V1-MUSS-Matrix einschließlich Funktions-/Tasteninventar und numerischen Regeln mit Version einfrieren.
2. **Implementierung nachweisen:** Ausgeführte Unit-, Zustands-, Integration-, Persistenz- und Mobiltests mit Build- und Plattformdaten.
3. **Benutzbarkeit prüfen:** Realistische Alltagsszenarien auf unterstützten iPhones durchspielen; Anzeige, Tastatur, Fehler, Wiederherstellung und Offline-Nutzung prüfen.
4. **Kompatibilitätsumfang offenlegen:** Nur belegte Funktionen/Modelle/Programme freigeben; Unbekanntes als offen, ungetestet oder nicht unterstützt kennzeichnen.
5. **Rechte und App Store prüfen:** Urheberrecht/Lizenzen/Marke, Datenschutz, echte Screenshots, Signierung, Release Notes und App-Store-Anforderungen dokumentieren.
6. **Erst dann veröffentlichen:** Keine vollständige historische Gesamtemulation als zusätzlicher pauschaler Gate.

### 23.2 Änderungen und Versionspflege

Jede Änderung an verbindlichen Produktprioritäten (RPN first, offline/werbefrei/ohne Abo, Produkttrennung), historischen Langfristzielen (Synthetic B, System RPL) oder Release-Gates erfordert einen **datierten neuen Beschluss**, Auswirkungen auf andere Dokumente und eine aktualisierte Traceability-Matrix. Empfehlungen und offene Entscheidungen dürfen bei späterer Ausarbeitung konkretisiert werden, ohne rückwirkend als ursprünglich entschieden ausgegeben zu werden.

### 23.3 Dokumentation als Nachweis

Zum jeweiligen Release gehören Funktions- und Kompatibilitätsmatrix, Versions-/Geräteangaben, bekannte Fehler/Abweichungen, ausgeführte Tests, Quellennachweise sowie Releaseentscheidung. Dokumentation des Lastenhefts ist **kein Ersatz für Tests**.

---

## 24. Anhänge und Querverweise

### A. Projektinterne Unterlagen

- [Konsolidierte Anforderungen (DE)](de/ANFORDERUNGEN.md)
- [HP-41C-Funktionskatalog (DE)](de/HP-41C-FUNKTIONSKATALOG.md)
- [HP-48GX-Funktionskatalog (DE)](de/HP-48GX-FUNKTIONSKATALOG.md) – recherchierter ROM-/Bedienkatalog, **kein** SASD-Implementierungsnachweis
- [Produktanforderungen (EN)](en/PRODUCT.md)
- [Historische 41er-Planung](en/HISTORICAL-41.md) und [48er-Planung](en/HISTORICAL-48.md)
- [Algebraische Eingabe](en/ALGEBRAIC-INPUT.md)
- [Mehrrechner-Architektur](en/MULTI-APP-ARCHITECTURE.md)
- [Wiederverwendbare Komponenten](en/SHARED-COMPONENTS.md)
- [Module und Advantage Pac](en/MODULES.md)
- [Speicher-/Kompatibilitätsstufen](en/COMPATIBILITY.md)
- [Hilfe und Training](en/LEARNING.md)
- [V1-Releaseumfang](en/RELEASE-V1.md) und [Release-Checkliste](en/RELEASE-CHECKLIST.md)
- [Testmatrix](en/TEST-MATRIX.md)
- [Historische Quellen](en/REFERENCE-SOURCES.md)
- [Entscheidungsregister](en/DECISIONS.md) und [offene Entscheidungen](en/DECISION-QUESTIONS.md)
- [Roadmap](../ROADMAP.md), [Aufgabenplan](../TASKS.md), [Codex-/Entwicklungsregeln](../AGENTS.md)
- [SASD-Bildquellen/Entwürfe](images/README.md)

### B. Vollständige Webadressen der wichtigsten Projektquellen

- Scientific GitHub: https://github.com/Robin-Goerlach/SASD-Scientific-Calculator
- SASD Math Toolkit (zu prüfende Wiederverwendung): https://github.com/Robin-Goerlach/SASD-Math-Toolkit
- HP-41C synthetische Programmierung, Wickes: https://www.mh-aerotools.de/hp/heldermann/Synthetische%20Programmierung%20auf%20dem%20HP-41C-CV.pdf
- HP-41C/CV Anwenderhandbuch, Gosmann: https://literature.hpcalc.org/community/hp41-anwenderhandbuch.pdf
- HP-48 System RPL, Donnelly: https://literature.hpcalc.org/items/1474
- HP-48 System RPL, Kalinowski: https://literature.hpcalc.org/items/1695
- HP-48 System RPL, weitere Ausgabe: https://literature.hpcalc.org/items/1696
- V41 (Referenzemulator): https://hp.giesselink.com/v41.htm
- Emu41 (Referenzemulator): https://jeffcalc.hp41.eu/emu41/index.html

Die Links dienen der Quellenidentifikation und sind **keine** Zusage, dass sämtliche URL-Inhalte am Datum dieses Lastenhefts erneut wissenschaftlich oder rechtlich geprüft wurden.

### C. Zusammenfassung des verbindlichen Vertrags

> **SASD Scientific Calculator ist zuerst ein hervorragender, klassischer wissenschaftlicher UPN/RPN-Rechner für das iPhone: zuverlässig, offline, werbefrei, ohne Abonnement, möglichst kostenlos, mit dezenter SASD-Kennzeichnung.**
>
> Seine gemeinsame mathematische Grundlage darf zugleich eigenständige ALG- und erweiterte RPL-Anwendungen sowie langfristig geeignete Finanzbibliotheken ermöglichen. Historische 41er- und 48er-Programmsemantiken bleiben getrennt; FOCAL/User RPL, synthetische 41er-Programme bis Stufe B und ein abgegrenzter System-RPL-Umfang bleiben langfristige Ziele. Byte-Hüpfer-Stufe C, Nut-/Saturn-CPU- und OS-Nachentwicklung sind optional.
>
> **Keines dieser historischen Spezialgebiete blockiert die erste hochwertige iPhone-App V1.0.**
