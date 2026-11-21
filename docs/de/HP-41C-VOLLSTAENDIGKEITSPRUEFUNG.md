# HP-41C – Quellenabgleich, Audit und Vollständigkeitsnachweis

**Prüfstand:** 2026-11-21. **Geltungsbereich:** nackter HP-41C; Erweiterungen separat.  
**Ergebnis:** **Dokumentationsinventar gegen die ausgewählten HP-Originalindizes abgeglichen, aber kein hardware- oder ROM-verifizierter Vollständigkeitsnachweis.** Nicht als bestandenen historischen K1/K2-Test verwenden.

## Verbindliche Referenzquellen

1. HP, *Owner's Handbook and Programming Guide*, HP-41C, **Funktionsindex Druckseiten 267–270**, Vergleichsfunktionen S. 170–171, SIGN S. 85. [Index 267](https://archived.hpcalc.org/greendyk/hp41c-manual/267.html), [268](https://archived.hpcalc.org/greendyk/hp41c-manual/268.html), [269](https://archived.hpcalc.org/greendyk/hp41c-manual/269.html), [270](https://archived.hpcalc.org/greendyk/hp41c-manual/270.html).
2. HP, *HP-41C/41CV Operating Manual*, **Function Index Druckseiten 59–68**. [Original-PDF](https://literature.hpcalc.org/community/hp41c41cv-om-en.pdf).
3. HP, *HP-41C Quick Reference Guide*, **Function Index S. 6–9**, übrige Dokumentation zur indirekten Adressierung, Flags, Tastatur und Programmierung. [Original-PDF](https://literature.hpcalc.org/community/hp41c-qrg-en.pdf).
4. HP, *HP-41C Training Manual*, Unterscheidung „über 130 Standardfunktionen/Operationen“ und **117 Einträge des CATALOG 3**. [Original-PDF](https://literature.hpcalc.org/community/hp41c-training.pdf).
5. HP, *HP 82210A HP 41CV Emulator Application Card Owner's Manual*, **Anhang C, S. 139–140**: vollständig nummerierte XROM-Funktionen für Extended Functions, CX und Time. [Original-PDF](https://literature.hpcalc.org/community/hp82210a-om-en.pdf).
6. Vier vom Projekt bereitgestellte deutschsprachige Quellen: Gosmann *Anwenderhandbuch HP-41C/CV* (1983); Dearing *Tricks, Tips und Routinen ...* (1984); Jarett *Erweiterte Funktionen ...* (1986); HP *HP-41C Standard-Programmsammlung* (1979). **Originaltexte, Listings und Barcodes werden wegen der Rechtevorbehalte nicht übernommen.**

## Unabhängiger CAT-3-Quervergleich: **Gosmann übersieht X>Y?**

Die drei Tabellen auf den gedruckten Seiten **9–11** des bereitgestellten Gosmann-Handbuchs (Datei `hp41-anwenderhandbuch.pdf`, **PDF-Seiten 19–21**) wurden einzeln gelesen und die dort genannten Mnemonics **unabhängig** vom bisherigen SASD-Katalog erfasst: **45 + 60 + 11 = 116 verschiedene Bezeichnungen**. Der ursprüngliche HP-41C-Schulungsband nennt **117 CAT-3-Einträge**. Die Differenz ist konkret identifiziert:

- **Gosmann fehlt `X>Y?`** (auf PDF-Seite 21 in der alphabetischen Schlussgruppe). Die Funktion ist in **HP Owner's Handbook S. 171** und **HP Operating Manual S. 67** nachgewiesen.
- Die vom Original-Funktionsindex abgeleiteten **125** normalisierten Einträge enthalten auch acht zusätzlich erfasste **Eingabe-/Editor-/Betriebstastenhandlungen**: `SHIFT`, `APPEND`, `EEX`, `GTO .`, `GTO ..`, `PRGM`, `USER`, `R/S`. Ohne diese erhalten wir **117** kanonische CAT-3-Befehlsnamen.
- Die Differenz `117 minus 116 = 1` ist exakt **`X>Y?`**. Keine der 116 von Gosmann gelisteten Bezeichnungen liegt außerhalb unserer rekonstruierten 117er Menge.
- Die transkribierten **nur sachlichen Befehlsnamen** (ohne Originaltexte/Programmlistings) liegen pro Seite nachvollziehbar in `docs/reference/hp41c-command-inventory.json` (`gosmann_cat3_transcription`). Der automatisch prüfbare 116/117-Abgleich ist in `tools/audit_hp41c_functions.py` integriert.

**Bewertung:** Es liegt jetzt eine **gegen unabhängige Handbücher und die HP-Zählung abgeglichene 117er-Soll-Liste** vor. Das ist ein starker schriftlicher Vollständigkeitsnachweis. Es ist trotzdem kein unabhängiges Protokoll der **realen** CAT-3-Ausgabe eines bestimmten ROM-Standes; die gerätespezifische Abnahme bleibt offen.

## Gemessene Ergebnisse (gegen vorhandenes Markdown)

| Prüfschritt | Beobachtung | Aussage |
| --- | --- | --- |
| Grundgeräte-Index S. 59–67 manuell als Referenzmenge normalisiert | **124 eindeutig benannte Einträge/Bedienvarianten** | Das ist keine unveränderte CAT-3-Ausgabe und nicht unmittelbar HPs offizielle „130“-Zählung. |
| Zusätzlich getrennt kontrollierte physische RUN/STOP-Taste | **1** | In der Inventur getrennt vom programmierbaren `STOP` berücksichtigt. |
| Abgleich dieser **125 Referenzeinträge** gegen die Befehlstabellen in Abschnitt 2 des Hauptkatalogs | **125 vorhanden; 0 textuelle Fehlstellen** nach expliziter Aliasauflösung | **Nur Präsenzprüfung**: kein Beweis der richtigen Syntax/Semantik und keine ROM-Verifikation. |
| Foto/Faltblatt – normale Tastenpositionen | **39 Positionen** | Einzeln abgehakt; Foto zeigt CX. |
| **Originale ALPHA- und SHIFT+ALPHA-Ebene** | **35 untere Positionen**, beide Ebenen | Gegen das original HP-Dokument (Kurzanleitung PDF-Seite 3) abgeglichen; der Audit prüft jetzt jede Position. |
| XROM 25,01–25,47, HP 82180A | **47/47**, keine nummerische Lücke | Kontrolliert gegen unabhängig publizierte HP-XROM-Tabelle. |
| XROM 25,49–25,62, HP-41CX spezifisch | **14/14**, keine nummerische Lücke | `25,48` ist Kennung, kein 15. Befehl. |
| XROM 26,01–26,29, HP 82182A | **29/29**, keine nummerische Lücke | `26,00` ist Kennung. |
| XROM 26,31–26,35, HP-41CX spezifisch | **5/5**, keine nummerische Lücke | `26,30` ist Kennung. |
| HP-41C Standard-Programmsammlung | **10 Anwenderprogramme** abgegrenzt | Programme ≠ ROM-Standardfunktionen. |
| Dearing | **26 Kapitel** inventarisiert | Dies ist **nicht** die Einzelinventur aller Tipps/Routinen. |
| Gosmann | Anwender-, Programmier- und Anwendungsabschnitte kontrolliert | 26 vollständige Programme werden im Buch genannt; **keine** 26 neuen ROM-Befehle. |

### Grenzen dieser Messung

**Ein „125/125“ ist kein 100-%-Nachweis aller möglichen historischen Fähigkeiten.** Die Zahl entsteht durch Normalisierung von Varianten aus einem gedruckten Index (einschließlich nicht katalogfähiger Bedienaktionen) und einer separat behandelten Taste. Die echte **CAT-3-Ausgabe eines definierten originalen HP-41C-ROM-Standes** wurde hier **nicht** gelesen oder protokolliert. Deren unabhängiger Soll-/Ist-Abgleich mit den **117 CAT-3-Einträgen aus HPs Schulungsunterlagen** ist offen. Eine vollständige Tastenmatrix schließt keine unbekannten SHIFT-ALPHA-Sonderzeichen, Bytecodes oder Moduswechsel aus. Nichts davon ist aktuell als erfolgreich getestet markiert.

## Festgestellte und dokumentierte Quellenkonflikte

| Fall | Widerspruch oder Fehlerrisiko | Konsequenz |
| --- | --- | --- |
| `FACT` | Online-Transkription des ursprünglichen HP-Handbuch-Index S. 268 schreibt „not programmable“; detaillierter Operating-Manual-Index S. 62 nennt **1 Programmbyte**. | Im Hauptkatalog als programmierbar geführt; verbleibender unabhängiger Gerätetest empfohlen. |
| `X<>` | HTML-Index S. 268 weist „not assignable, not executable“ aus; Operating Manual S. 67 führt die **zweibyteige Registeraustauschanweisung**. | `X<> Register` und `X<>Y` unterscheiden; programmierbar ≠ per XEQ ausführbar ≠ USER-belegbar. |
| `SIGN` | Häufig fälschlich als gewöhnliches mathematisches signum angenommen. | Für X=0 ergibt der HP-41C **+1**; ALPHA-Daten geben 0; Beleg Originalhandbuch S. 85. |
| `X<0?` | In manchen digitalisierten alphabetischen Originalverzeichnissen nicht sichtbar. | Im Operating Manual S. 66 und Fließtext des Originalhandbuchs S. 171 nachgewiesen. |
| 130 / 117 / 125 | Je nach Quelle/Zählweise Funktionen, Tastatur-/Bedienoperationen, CAT-3-Inhalte und normierte Indexvarianten. | Zahlen **nicht** gleichsetzen; eine **exakte beobachtete CAT-3-Menge** bleibt erforderlich. |
| `APPEND`, `SIZE`, `ASN`, `GTO .` | Interaktive Eingabe-/Editier- und Betriebsaktionen werden häufig mit ausführbaren Programmbefehlen vermischt. | Metadatenfelder für **Tastatur**, **XEQ**, **USER** und **Programmbytecode** getrennt führen. |
| Modulbefehle ohne Erweiterung | XROM-25/-26-Funktionen können auf einem nackten HP-41C nicht ausgeführt werden. | Jede Erweiterung als eigenständiges Profil; kein falscher Bestandteil von CAT 3. |

## Nachweiskette / Abnahmeregeln

1. **Baseline des HP-41C:** Originalindex samt Tastatur und normalisierten Aliasnamen **als maschinenlesbares Soll** speichern. Es darf keine doppelt vergebene ID und keine fehlende Quellenstelle geben.
2. **Unabhängiges CAT-3-Protokoll:** Auf **echtem HP-41C ohne Module** oder unabhängig geprüftem Modell-/ROM-Referenzgerät den kompletten Katalog aufnehmen. **Ein HP-41CX-Foto ersetzt diesen Schritt nicht.** Katalogeinträge und Reihenfolge mit Soll vergleichen; Unterschiede dokumentieren.
3. **Getrennte Inventare für CAT 2:** Pro Modul und ROM-Revision eine eigene XROM-Referenz mit ID, Befehlsname, Hardwarevoraussetzungen und sekundärem Quellenabgleich. Mehrere Modulrevisionen können voneinander abweichen.
4. **Semantik pro Befehl:** Zulässige Argumentformen; physische Tasteneingabe; XEQ/ASN/Programmierung; Stack-Lift, LAST X, Flags, ALPHA, REGISTER; Fehlerfälle; numerische Grenzen und Präzision; Programmbyte-Länge; Quellenstellen.
5. **Unabhängige Tests:** Charakteristische Referenzfälle auf Gerät oder unabhängig verifiziertem Emulator, reproduzierbare Testfixtures und Testbericht. Auf keinen Fall Gerätetreue aus einem Namen oder einer mathematisch korrekten Host-Berechnung ableiten.
6. **Vier separate Freigaben:** (A) Grundinventar aus Originalindex, (B) tatsächlicher ROM-CAT-3-Dump, (C) belegte Modul- und Geräteprofile, (D) historische Verhaltenskonformität. **A ist dokumentarisch geprüft; B bis D sind offen.**

## Quellenprüfung – zusätzlich abgesicherte ALPHA-Ebene und XROM-Katalog

- **ALPHA:** Die ursprüngliche 39-Tasten-Matrix enthielt nicht die vollständige SHIFT+ALPHA-Belegung. Die [deutsche HP-41C-Kurzanleitung, PDF-Seite 3](https://literature.hpcalc.org/community/hp41c-qrg-de.pdf) zeigt die unteren 35 Positionen einschließlich Kleinbuchstaben, Sonderzeichen und ALPHA-Funktionen. Diese stehen nun in Abschnitt 7.2 und im Datenfeld `alpha_layers` der Referenzdatei; sie werden positionstreu geprüft. Die vier oberen ON/USER/PRGM/ALPHA-Tasten sind gesonderte Bedientasten.
- **XROM:** Die 95 Zusatzfunktionen wurden auch mit einer unabhängigen historischen [XROM.TXT-Tabelle](https://robert-scheibe.de/git/cgit.cgi/hp41c.git/tree/ROMHandler/XROM.TXT?h=main&id=c6c9104a61bb609b040c592ee54ece1ac4b36b0c) kontrolliert. Schreibweisen wie `SREG?`/`ΣREG?` und `X#NN?`/`X≠NN?` sind Aliase, keine neuen Funktionen.
- **Quellenwiderspruch:** Eine sekundäre Modultabelle beschreibt `GETAS` und `SAVEAS` fälschlich als Tastenzuweisung. Das Originalhandbuch des 82180A beschreibt die ASCII-Dateiübertragung mit HP-IL-Massenspeicher; die richtige Beschreibung blieb erhalten.
- **Gosmann-Lücke:** Von Gosmann sind 116 CAT-3-Befehlsnamen abschreibbar; `X>Y?` fehlt gegenüber dem von HP belegten 117er-Satz. Der Grundkatalog enthält den Befehl.
- **Grenze:** Damit sind Dokumentationsquellen gegengeprüft, aber noch **kein** reales, firmwaregenaues CAT-3-Laufzeitprotokoll erstellt.

## Erprobter Prüfer – tatsächlicher GitHub-Actions-Lauf

**GitHub Actions, PR #10, Commit `39cffd74525499678e78143eb77d6b6dff762eeb`: [Run 44937068237](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/actions/runs/44937068237) – erfolgreich abgeschlossen.** Das vollständige Jobprotokoll wurde eingesehen, nicht nur ein Workflow angelegt.

- `python3 -m unittest discover -s tools -p 'test_audit_hp41c_functions.py' -v` → **8 Tests OK**. Davon prüfen **sieben Negativtests**, ob absichtlich gelöschte Befehle, doppelte XROM-Nummern, falsche Kennungen, Tastatur-/ALPHA-Verfälschungen und die Gosmann-Differenz zu einem Fehler führen.
- `python3 tools/audit_hp41c_functions.py --json` → **`"status": "PASS"`**.
- Protokollierte Zahlen: **117 CAT-3-Namen**, **116 Gosmann-Einträge**, **125 normierte Referenz-/Bedienposten**, **39 Tasten**, **35 ALPHA-Positionen**, **47 + 14 + 29 + 5 = 95 XROM-Einträge**.
- Die Fehlerlisten für fehlende oder doppelte Befehle, falsche XROM-Einträge, Tasten und ALPHA-Einträge sind **leer**.

**Geltungsgrenze des grünen CI-Tests:** Textuelle Inventarkonsistenz. **Es wurden weder proprietäre ROM-Bytes ausgewertet noch eine echte HP-41C-CAT-3-Ausgabe gemessen oder historische Programme auf einer validierten ROM-Referenz ausgeführt.** Der Test bestätigt damit **nicht** vollständige numerische oder historische Kompatibilität.

Lokal auszuführen:

```bash
python3 -m unittest discover -s tools -p 'test_audit_hp41c_functions.py' -v
python3 tools/audit_hp41c_functions.py --json
```

## Aktueller Entscheidungsstand

**Status A: quellenbasiertes Index-Inventar geprüft (mit ausdrücklich gekennzeichneter Normalisierung).**  
**Status B: CAT-3-Geräteausgabe nicht unabhängig geprüft.**  
**Status C: vier nummerierte XROM-Teilbereiche gegen HP-Tabelle abgeglichen; nicht sämtliche optionalen Module.**  
**Status D: historische Ausführung, Fehler- und Tastenverhalten nicht getestet.**

Der vorliegende Auditbericht ist **kein** Zertifikat für absolute historische Vollständigkeit. Er dokumentiert die konkret durchgeführten Quellenabgleiche und die verbleibenden Beweislücken. Historische Kompatibilität wird erst in späteren SASD-Milestones getestet; sie blockiert die klassische iPhone-V1.0 nicht.
