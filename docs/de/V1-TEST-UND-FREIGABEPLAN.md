# V1.0 – Teststrategie, Abnahme- und App-Store-Freigabeplan

**Dokument-ID:** SASD-SCI-V1-TEST-001  
**Datum:** 2026-11-21  
**Status:** **PRÜFPLAN ENTWURF; KEIN TESTLAUF ODER RELEASE NACHGEWIESEN**  
**Ziel:** native Classic-RPN-Wissenschaftsrechner-App auf dem iPhone, insbesondere iPhone XS  
**Normative Quellen:** [Lastenheft](../LASTENHEFT.md), [Pflichtenheft](../PFLICHTENHEFT.md), [Architektur](../ARCHITEKTUR.md), [Roadmap](../../ROADMAP.md), [Release-V1](../en/RELEASE-V1.md), [vorhandene Release-Checkliste](../en/RELEASE-CHECKLIST.md)  
**Detailverträge:** [Keymap/Funktionsmatrix](V1-FUNKTIONS-UND-TASTATURMATRIX.md), [Input-ADR](../adr/ADR-V1-INPUT.md), [Numerik-ADR](../adr/ADR-V1-NUM.md), [State-ADR](../adr/ADR-V1-STATE.md), [API-/iOS-ADR](../adr/ADR-V1-API.md)

> **Der geplante Classic-iPhone-Release darf ohne vollständige historische FOCAL-/User-RPL-/System-RPL-/Synthetic-/CPU-Emulation erscheinen.** Er darf **nicht** mit defekten freigegebenen RPN-, Mathe-, Zustandsspeicher-, Sicherheits- oder Bedienfunktionen erscheinen. Ein historischer Funktionskatalog ist keine implementierte oder getestete SASD-Kommandoliste.

## 1. Teststrategie und Verbindlichkeitsgrenze

| Testart | Hauptzweck | Releasepflicht |
| --- | --- | --- |
| **Unit-/Property-Tests C++** | pure Mathematik, numerische Grenzen, RPN-State-Transitions, Fehler | alle freigegebenen P0-Kommandos |
| **Headless Integration** | CLI-/Facade-/Session-/State-/Snapshot-Grenzen | M1/M2 |
| **C-ABI-Tests** | Ownership, Buffergrößen, Encoding, Exceptions, ABI-Version | M2 |
| **Swift-/UI-Tests** | Keymap, Shift-/Modus-Zugriff, Accessibility, Display, offline Hilfe | M2 |
| **iPhone-XS-Gerätetests** | echtes iOS, Touch, Safe Areas, Performance/Start, Persistenz und Netzfreiheit | **vor V1 zwingend** |
| **Build-/CI-Prüfung** | Linux/Windows/macOS C++-Kern, zusätzlich Apple/iOS-Build | M1/M2 |
| **Sicherheit** | untrusted Inputs, übergroße Werte, ungültige Payloads, beschädigte Speicherung | M1/M2 |
| **Rechte/Store** | MIT/Drittlizenzen, Marken, echte Screenshots, Privacy, Signing | M2 |
| **Historische Regression** | K2/K3/K4 / Modelle 41/48 | **erst später; kein V1-Gate** |

**Statusbegriffe:** `TODO` = noch nicht ausgeführt; `PASS` = exakt definierter Test ausgeführt und belegt; `FAIL` = nicht bestanden; `BLOCKED` = konkrete fehlende Entscheidung/Testumgebung; `N/A` = nach freigegebenem Scope begründet nicht zutreffend. Kein Eintrag erhält `PASS` allein wegen Dokumentation.

## 2. Gate M0: erforderliche Entscheidungen

| Gate-ID | Frage | Verbindliche Evidenz | Status |
| --- | --- | --- | --- |
| G0-01 | Sind V1-Commands + UI-Zuordnung freigegeben? | versionierte Keymap, jeder P0-Befehl mit Test-ID | **TODO** |
| G0-02 | Ist der Vier-Ebenen-Stack inkl. LAST X/ENTER/CLX geregelt? | `ADR-V1-INPUT` Status ACCEPTED und vollständige Golden-States | **TODO** |
| G0-03 | Sind Zahlentyp/Präzision/Angle-/Fehlerregeln festgelegt? | `ADR-V1-NUM` ACCEPTED + Referenzvektoren | **TODO** |
| G0-04 | Sind Snapshots/Recovery/Migration spezifiziert? | `ADR-V1-STATE` ACCEPTED + Codec-Testplan | **TODO** |
| G0-05 | Sind native ABI, iOS-Minimum/XS und Toolchain geprüft? | `ADR-V1-API` ACCEPTED + Build-/Device-Spike | **TODO** |
| G0-06 | Sind P0/P1, Hilfe-/Preis-/SASD-URL und Store-Konzepte entschieden? | V1-Freeze und Releaseentscheidungen datiert | **TODO** |
| G0-07 | Existieren Rechts-/Quellen-/Lizenzkonventionen und CI? | MIT, Dokumentation, Repo-Review und beobachtete Basistests | **teilweise vorhanden; neuer Beleg nötig** |

**Wichtig:** Ein offener M4-Bytecode-/System-RPL-ADR blockiert **nicht** G0. Kleine technische Machbarkeitstests sind möglich, bevor alle ADRs angenommen sind; aber deren Ergebnisse ersetzen keine fachspezifische Entscheidung.

## 3. Funktionsabnahme P0: Traceability und Status

Die [Keymap](V1-FUNKTIONS-UND-TASTATURMATRIX.md) definiert vorgeschlagene Key- und Command-IDs. **Erst die fachlich akzeptierte Fassung** wird zur verbindlichen Key-/Feature-Baseline.

| Testgruppe | Prüfgegenstand | Kern-Goldens / Fehler | Zustandsfelder |
| --- | --- | --- | --- |
| `V1-KEY-001…004` | Ziffern, Punkt, CHS, EEX | korrekte Mantisse/Exponent, fehlerhafte Token abweisen | Entry, X, Lift |
| `V1-KEY-005…008` | ENTER, X↔Y, R↓, LAST X | vollständige Vorher-/Nachher-States | T/Z/Y/X, LAST X, Entry, Lift |
| `V1-KEY-009…011` | CLX, Backspace, Reset | klar unterschiedliche Lösch-/Korrekturwirkung | Entry, X/Stack/Register |
| `V1-KEY-012…014` | STO, RCL, Shift-Layer | geprüfte Registeradresse, Key-Layer, Fehlereffekt | X, Register, Lift, Modifier |
| `V1-MATH-001…004` | +, −, ×, ÷ | 10 ENTER 4 −→6; 10 ENTER 4 ÷→2,5; 1/0 Fehler | X/Y/Z/T, LAST X |
| `V1-MATH-005…009` | √x, x², 1/x, yˣ, π | 81 SQRT→9; 2 ENTER 3 yˣ→8 | Stack, NumericContext |
| `V1-MATH-010…015` | SIN/COS/TAN und inverse Funktionen | sin 30 DEG≈0,5; asin 0,5 DEG≈30 | X/Mode/Display |
| `V1-MATH-016…019` | LN/LOG/EXP/10ˣ | ln(1)=0; log(100)=2; exp(0)=1 | X/Mode/Error |
| `V1-MODE` | DEG/RAD, FIX/SCI | UI-Modus/Display ohne Stored-Value-Mutation | Modes, NumericValue |
| `V1-UX` | alle freigegebenen sichtbaren Befehle | erreichbar, beschriftet, offline, kein verdeckter Shift-Key | UI/Capabilities |
| `V1-STATE` | Suspend/Restore, Faults | betroffene State-Felder identisch | Snapshot/Generation |

**Mindestens:** Für jeden freigegebenen Command (1) normaler positiver Fall, (2) relevanter negativer/Grenzfall, (3) vollständige Zustandswirkung, (4) CLI- und UI-Zuordnung. Wo keine negative Domain existiert (z. B. `π`), bewusst `N/A` mit Begründung markieren.

## 4. Kern-/RPN-Golden-Tabellen

Die folgenden Beispiele sind **geplante Tests**, nicht bereits ausgeführte Tests. Vollständige Stackzustände müssen aus dem **akzeptierten** Input-ADR folgen.

| Test-ID | Vorbedingung | Kommando/Sequenz | Ergebnis |
| --- | --- | --- | --- |
| RPN-001 | neue Session | `3 ENTER 4 ENTER 5 × +` | X=23, restlicher Stack gemäß Freeze |
| RPN-002 | neue Session | `10 ENTER 4 −` | X=6 |
| RPN-003 | neue Session | `10 ENTER 4 ÷` | X=2,5 |
| RPN-004 | [T,Z,Y,X]=[40,30,20,10] | ENTER | vorgeschlagen [30,20,10,10]; Lift=disabled |
| RPN-005 | Zustand RPN-004 | Ziffernfolge „7“ | vorgeschlagen [30,20,10,7], kein weiterer Lift |
| RPN-006 | [40,30,20,10] | + | vorgeschlagen [40,40,30,30], LASTX=10 |
| RPN-007 | [40,30,20,10] | R↓ | vorgeschlagen [10,40,30,20], weitere Liftregel offen |
| RPN-008 | [40,30,20,10] | X↔Y | vorgeschlagen [40,30,10,20] |
| RPN-009 | freigegebene Registerbank | STO 00; RCL 00 | exakter Register-/Stack-After-State |
| RPN-010 | aktiver Exponent „1E−“ | Operation/ENTER | definierte Syntaxdiagnose, keine undefinierte Zahl |
| RPN-011 | aktive Eingabe | Backspace/CLX/Reset getrennt | niemals ungeplanter Register-/LAST-X-Verlust |
| RPN-012 | definierter gültiger Stack | Divisionsfehler/Overflow | State-Konsistenz wie ADR |
| RPN-013 | vier Nullregister | binärer Operator | **nicht** automatisch dynamischer Stackunterlauf |
| RPN-014 | nach Moduswechsel | weiterer Entry + Operation | kein fehlerhafter Lift |
| RPN-015 | lange Eingabefolge | begrenzter Eingabepuffer | definierter `RESOURCE_LIMIT` ohne Host-Überlauf |

**Gefährliche Fehlannahme:** Der vorhandene Prototyp meldet bei zu wenig Vektorelementen `stack_underflow`. Das ist **nicht ohne Prüfung** auf die vier permanent vorhandenen X/Y/Z/T-Register übertragbar.

## 5. Mathematische Tests mit Grenzfällen

| Test-ID | Eingabe | Vergleich/Fehler |
| --- | --- | --- |
| NUM-001 | 10−4 | 6 |
| NUM-002 | 10÷4 | 2,5 |
| NUM-003 | 2^3 | 8 |
| NUM-004 | sqrt(81) | 9 |
| NUM-005 | sqrt(-1) im **reellen** Profil | `DOMAIN` |
| NUM-006 | ln(1) | nahe 0 bzw. erwartete exakte Null gemäß Policy |
| NUM-007 | ln(0), log(-1), asin(2) | `DOMAIN` |
| NUM-008 | `1/x` mit X=0, Y/X bei X=0 | `DIV_ZERO` |
| NUM-009 | sin(30) DEG / sin(π/6) RAD | nahe 0,5 innerhalb vorab genehmigter Toleranz |
| NUM-010 | cos(60) DEG / asin(0,5) DEG | ca. 0,5 / ca. 30 |
| NUM-011 | tan(90) DEG | freigegebene Pol-/Toleranz-/Fehlerregel; **nicht** blind `∞` |
| NUM-012 | sehr große Exp/Pow-Werte | `OVERFLOW`; nichtendliche Werte nicht in gültigen State |
| NUM-013 | `min_normal`/Subnormal/Underflow | definierter NumericPolicy-/Statusweg |
| NUM-014 | negative Basis mit ganzzahligem bzw. nichtganzzahligem Exponenten | Domain-/Resultatregeln |
| NUM-015 | −0 und 0 im Display und bei 1/X | nach Numerik-ADR |
| NUM-016 | Wert 1/3; FIX↔SCI | interner Wert **bitgleich**, Anzeige verschieden |
| NUM-017 | Zufalls-/Property-Test mit gespeichertem Seed | reproduzierbar, Referenzdifferenzen dokumentiert |
| NUM-018 | Compiler-/libm-Plattformvergleich | genehmigte absol./relative/ULP-Toleranzen; keine erfundene Bitidentität |

**Vergleichsregel:** mathematisch exakt darstellbare Beispiele gegebenenfalls exakt; `sin`, `exp` und andere transzendente Funktionen nur gegen freigegebene, dokumentierte Toleranz und unabhängige Referenzen vergleichen. Eine reproduzierbar falsche letzte Stelle darf weder versteckt noch als historische HP-41-Bitgenauigkeit ausgegeben werden.

## 6. Persistenz-/Integrations- und ABI-Testgruppen

### 6.1 Snapshots

Die vollständige Liste `STATE-001…015` ist in [ADR-V1-STATE](../adr/ADR-V1-STATE.md) definiert. Releasekritisch: mehrere unterschiedliche Register-/Stackwerte, LAST X, Input-Entry, Angle-/Formatmode, älteres/zu neues Schema, Korruption/Truncation, atomarer Speicherersatz, älteres verspätetes Save, tatsächliche Geräte-Wiederaufnahme.

### 6.2 C++-/Swift-ABI

Die Liste `ABI-001…010` und `IOS-XS-001…005` steht in [ADR-V1-API](../adr/ADR-V1-API.md). Releasekritisch: keine C++-Exception über C ABI, Ownership, UTF-8, kapazitätsgeprüfte Buffers, Error Codes, genauen Sessionzustand pro View-Generation und sichtbare iPhone-UI.

### 6.3 Build und Toolchain

- **CMake/CTest** auf Linux, Windows und macOS für den portablen Kern.
- Für iOS zusätzlich Xcode/SDK-/Deploymenttarget-/arm64-/Signing-Build, Swift-Bridge-/UI-/Gerätetest.
- Der Apple-SDK- und XS-Support wird **auf dem aktuellen Releasewerkzeug** geprüft und dokumentiert; kein „grün“ aus einem früheren simulierten iPhone-Layout.
- Zu jedem `PASS` gehört SHA/Tag, Run-ID, Plattform, Xcode/Compiler und konkreter Testdatensatz.

## 7. Vollständige M2-Abnahmeszenarien AC-V1-001 bis AC-V1-017

Diese Szenarien stammen aus [Pflichtenheft Kap. 25](../PFLICHTENHEFT.md) und dürfen bei Releaseentscheidungen **nicht weggelassen** werden. Die Links zu Untertests werden bei Implementierung konkret eingetragen.

| AC-ID | Endnutzer-/Systemabnahme | Belegarten | Sollstatus |
| --- | --- | --- | --- |
| **AC-V1-001** | Kaltstart **offline**, kein Account-/Login-/Netzzwang, definierter Initialstate | echter XS-Start + Flugmodus | TODO |
| **AC-V1-002** | `3 ENTER 4 ENTER 5 × +` liefert 23 und definierten gesamten Stack | RPN-001 + Stack-Golden + UI | TODO |
| **AC-V1-003** | Subtraktion/Division mit korrekter Y/X-Reihenfolge (6; 2,5) | RPN-002/003 + Fehlerfälle | TODO |
| **AC-V1-004** | SIN/COS/TAN, DEG/RAD und inverse Funktionen | NUM-009/010 + Modi + Gerät | TODO |
| **AC-V1-005** | Potenzen, Wurzeln, Logs, ungültige Domains | NUM-004…008/012/014 | TODO |
| **AC-V1-006** | STO/RCL und freigegebene Registeroperationen | RPN-009 + Persistenz | TODO |
| **AC-V1-007** | ENTER/LAST-X, Roll/Swap, Clear/Undo, Reset-Fehler | RPN-004…015 | TODO |
| **AC-V1-008** | Unterbrechung, Background, Beenden, Relaunch; Zustand bleibt wie zugesagt | STATE-001…004/012, echtes XS | TODO |
| **AC-V1-009** | korrupter/alter/zu neuer Snapshot sicher behandelt | STATE-005…010/015 | TODO |
| **AC-V1-010** | FIX/SCI-Darstellung verändert internen Wert nicht | NUM-016, ViewState | TODO |
| **AC-V1-011** | XS Hochformat, Shift-/ALPHA-/Softmenü falls freigegeben; kein verdeckter Key | vollständige freigegebene Keymap + Screenshots real | TODO |
| **AC-V1-012** | VoiceOver, Dynamic Type, Safe Areas, berührbare Tasten | UI-/Accessibility-Protokoll real | TODO |
| **AC-V1-013** | Flugmodus; Mathematik/Hilfe offline; SASD-Link nur auf Tap | Offline-/Network-Test | TODO |
| **AC-V1-014** | keine Ads, Trackingpflicht, Abo, Konto oder Zwangscloud | Binär-/Privacy-/Paketaudit | TODO |
| **AC-V1-015** | AppStore-Signing/Bundle/Privacy/Lizenzen/echte Screenshots | Release-/Apple-/Rechte-Gate | TODO |
| **AC-V1-016** | C++-CI + iOS-/Geräte-/Fehler-/Stabilitätsprüfung bestanden | Testreport/Run/Commit | TODO |
| **AC-V1-017** | Release Notes nennen genau vorhandene Fähigkeiten und historische Grenzen | veröffentlichungsreife Feature-/K-Matrix | TODO |

**Keine Pseudofreigabe:** `AC-V1-001…017` sind **nicht abgeschlossen**, solange keine App mit realen Tests existiert. Eine leere Tabelle mit `PASS`-Häkchen ist kein Abnahmenachweis.

## 8. Freigaberelevante Sicherheits- und Qualitätsprüfungen

| Bereich | Prüfschritt | Releaseentscheidung |
| --- | --- | --- |
| feindliche/ungültige numerische Eingabe | unterbrochene Exponenten, enorme Ziffernfolgen, NaN/Inf-Strings | kontrollierte Diagnose, keine abgestürzte App |
| Dateikorruption | manipulierte JSON-/Snapshot-Bytes, Längen/Versionen | sichere Recovery, kein Teilcommit |
| ABI | Length-/Null-/Ownership-/Threading- und C++-Exception-Grenzen | kein OOB, kein ungefangenes Exception-Leak |
| Offline | Flugmodus, erster Start, Taschenrechner, Hilfe, Relaunch | keine Rechner-Netzwerkabhängigkeit |
| Datenschutz | konkrete Berechtigungen, SDKs, Netzwerkpfade, App-Store-Privacy-Angaben | wahrheitsgemäß und geprüft |
| Marken/Lizenzen | MIT, Drittanbieter-SBOM soweit nötig, SASD-Logo/URL, HP-Modellnamen nur sachlich | keine unlizenzierte ROM-/Handbuch-/Bildübernahme |
| tatsächliche Screenshots | UI aus installierter realer App, nicht SVG-Konzept | App-Store-Einreichungsassets korrekt |
| Stabilität | mehrere Rechensitzungen, Hintergrund/Neustart, Bedienbarkeit | keine bekannten kritischen Crash-/Datenverlustfehler |
| Performance | gemessene Antwortzeit/Start/Memory auf XS | Schwellen erst nach Messungen als Soll festlegen |

## 9. Fehlerklassen und Release-Entscheidung

**Empfohlene Bug-Schweregrade:**

| Klasse | Typischer Fehler | M2 |
| --- | --- | --- |
| **S0 kritisch** | falsches Ergebnis bei P0-Standardfall, bekannter Datenverlust, schwere Sicherheits-/Crashlücke | **NO-GO** |
| **S1 hoch** | wichtige P0-Funktion nicht erreichbar, Wiederaufnahme beschädigt, iPhone XS nicht startfähig, relevante ADA-/Accessibility-Sperre | **NO-GO** |
| **S2 mittel** | nichtkritische UI-Einschränkung, klar begrenzte dokumentierte Funktionsabweichung | Ausnahme **nur** bei ausdrücklicher Begründung/Freigabe |
| **S3 niedrig** | Kosmetik/Schreibweise ohne Rechen-/Zugänglichkeitsrisiko | dokumentiert akzeptierbar |

**Releasevorschlag:** Alle freigegebenen P0-Tests bestanden; keine S0-/S1-Fehler offen; S2-Abweichungen einzeln bewertet; iPhone-XS-Gerätetest und Apple-/Lizenz-/Privacy-Gates erfüllt. **Ohne tatsächliche Testergebnisse ist der Status NO-GO / NICHT BEREIT**, nicht „grün“.

## 10. Abnahme- und Auditformular (pro Build auszufüllen)

```text
Release-/App-Name:                    TODO
Bundle-ID und Build-Version:         TODO
Git-Tag / Commit-SHA:                TODO
C++ Compiler / CMake / CTest:        TODO
macOS / Xcode / iOS SDK:             TODO
Deployment Target:                   TODO
Reales iPhone XS: OS/Hardware/Test:  TODO
Zusätzliche Testgeräte/Simulatoren:  TODO
NumericPolicy / Keymap-ADR-Version:  TODO
State-Format / ABI-Version:          TODO
CI-Runs (Linux/Windows/macOS):       TODO
iOS Build-/Geräte-/UI-Tests:         TODO
Offene S0/S1-Fehler:                 TODO
Offene S2/S3-Ausnahmen:              TODO
Freigegebener P0-Funktionsumfang:    TODO
Historische K1-Teilabdeckung:        TODO
Datenschutz/Lizenzen/SASD-URL:       TODO
Echte Store-Screenshots:             TODO
Reviewer / Datum / Entscheidung:    TODO
ERGEBNIS:                            NO-GO BIS ZUR VOLLSTÄNDIGEN PRÜFUNG
```

**Durchgeführte Testfälle müssen auf konkrete Log-/CI-/Test-Artefakte verweisen.** Handbücher und HP-41C-/48GX-Funktionskataloge sind Referenz- und Recherchequellen, nicht Beleg für eine ausführbare App.

## 11. Historische Zukunftstests – ausdrücklich **nicht** im V1-Gate

| Track | Testgruppen | Verbindlichkeit |
| --- | --- | --- |
| 41er normale FOCAL-Programme | `41-FOCAL`, Bytes/Flags/Stack/Programmzeiger | langfristig M3 |
| 41er Synthetic A/B | `41-SYN-A/B`, 56-Bit-Rohregister und Byte-/Tastenzuweisungs-Roundtrips | **langfristig verbindliche Stufe B**, M4 |
| 41er Byte Grabber C | `41-SYN-C`, historische Firmware-/Speichertricks | **optional** |
| 48er User RPL | `48-USER`, Objekt-/Daten-/Return-Stack/Programme | langfristig M3 |
| 48er System RPL | `48-SYS`, virtuelle `SYSEVAL`/`LIBEVAL`, dokumentierter ROM-Profil-Teilumfang | **langfristig verbindlich**, M4 |
| Strict Historical und Karten | `MEM/EXT`, 48GX-128-KiB-RAM-/Kartenprofil, 41er-Registeraufteilung | später, kein modernes RAM-Limit |
| Time/Statistics/Advantage | `MOD`, gemeinsame Mathematik mit historischer Befehlswirkung | nach V1 / Advantage optional |
| Nut/Saturn/OS | `K4-MACHINE` | optional M5 |
| ALG Scientific | `ALG-LEX/PAR/AST/EVAL`, eigene App/Release | separater Track, kein V1-Gate |
| Financial | getrennte Fach-/Version-/Release-Tests | anderes Produkt und Repository |

**HP-48GX-Katalogstatus:** Der [Befehlsabgleich](HP-48GX-BEFEHLSABGLEICH-MATRIX.md) ist noch **nicht vollständig unabhängig verifiziert**. Keine aus den 517 ROM-Namen abgeleitete „517 Funktionen implementiert“-Zusage.

## 12. Quellen, Apple-Anforderungen und Verknüpfung

- [Keymap](V1-FUNKTIONS-UND-TASTATURMATRIX.md)
- [RPN Input/Stack](../adr/ADR-V1-INPUT.md)
- [Numerik](../adr/ADR-V1-NUM.md)
- [Snapshot/Recovery](../adr/ADR-V1-STATE.md)
- [C++/Swift ABI und iPhone XS](../adr/ADR-V1-API.md)
- [V1-Freigabeanforderungen EN](../en/RELEASE-V1.md)
- [Prüfcheckliste EN](../en/RELEASE-CHECKLIST.md)
- [Gesamttestmatrix EN](../en/TEST-MATRIX.md)
- Apple Xcode/SDK/Deployment Support: https://developer.apple.com/xcode/system-requirements/
- Apple App Store Connect Upload-Voraussetzungen: https://developer.apple.com/news/upcoming-requirements/
- iPhone XS/OS-Sicherheitsupdates: https://support.apple.com/en-us/100100

**Einsetzbare Abschlussregel:** Erst wenn die fachlichen ADRs genehmigt, der V1-Funktionsfreeze geschlossen, alle P0-Szenarien belegt und die echte iPhone-App geprüft ist, darf die erste App als **V1.0 freigegeben** gelten.
