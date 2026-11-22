# HP 48GX – Semantische Nachprüfung 01: RSD, CLUSR/CLVAR und LAST/LASTARG

**Prüfstand:** 22.11.2026 · **Gerät:** HP 48GX (historische HP-48G-Serie).  
**Status:** Originalhandbuch-/zeitgenössische Sekundärbelege ausgewertet; vollständige AUR-Stackdiagramm-Sichtprüfung und echter Hardwaretest stehen **aus**. Dieser Bericht ist ein *separater, wiederaufnehmbarer Prüfabschnitt*, keine historische Gesamtfreigabe.

## 1. RSD: Vorzeichen der Restgröße

**Direkt aus der HP-Dokumentation:** Der *HP 48G Series User's Guide*, Edition 8, gedruckte Seite **G-40**, bezeichnet `RSD` als Operation, die aus drei Arrays den Ausdruck `z − y·x` berechnet. Dieses historische Dokument ist als OCR-HTML-Einzelseite abrufbar:
https://www.manualsdir.com/manuals/631929/hp-48g-graphing-calculator-48gx-graphing-calculator.html?page=520

**Anderer Kontext desselben Handbuchs:** Der Text zur Güte einer Lösung von `A·X=B` (gedruckte Seite **14-17**) diskutiert die Restgröße `A·X−B`. Das ist mathematisch das **negative** der in G-40 angegebenen Restgröße, wenn man `y=A`, `x=X` und `z=B` einsetzt.

**Folgerung:** Die frühere Kurzbeschreibung im Hauptkatalog `RSD = A·X−B` ist für das **konkrete ROM-Kommando** nicht verlässlich und wird durch den expliziten G-40-Index `z−y·x` ersetzt. Unabhängige AUR-Einzelreferenz, Reihenfolge der drei Stack-Operanden, Array-Typen, Fehler und numerische Konformität bleiben zu verifizieren. **Nicht** aus der späteren 48gII-Referenz ableiten.

**Geplanter Konformitätstest:** Ein asymmetrisches, nichttriviales Beispiel mit `A=[2]`, `X=[3]`, `B=[7]` ergibt je Formel `B−A·X=[1]` bzw. `A·X−B=[−1]`. Erst die dokumentierte Stackbelegung (und danach ein Originalgerät/legitimer Emulator) klärt die Ausführung; keine freihändige Parameterreihenfolge unterstellen.

## 2. CLUSR versus CLVAR

**HP-AUR-Einträge:** Die Original-*Advanced User's Reference*, 4. Ausgabe, Kapitel 3, behandelt die Drucknamen **`CLUSR` (3-52)** und **`CLVAR` (3-53)** getrennt im Inhaltsverzeichnis. Daraus allein folgt keine unterschiedliche Funktion.

**Zeitgenössische Erklärung:** Eine technische HP-28-zu-HP-48-Übersicht führt `CLUSR` als beibehaltene ältere Schreibweise auf, die in Programmen zu `CLVAR` übersetzt werde:
https://groups.google.com/g/comp.sys.handhelds/c/W8SISptcdpY

**Unabhängiger Nachweis:** Der *HP 48G/GX Pocket Guide*, Command Index S. 43, bezeichnet `CLUSR` ausdrücklich als identisch mit `CLVAR`: https://literature.hpcalc.org/community/hp48g-pg-en.pdf . Damit ist die **dokumentierte Namensalias-Zuordnung** unabhängig bestätigt; ein separater Mathematikbefehl wird nicht daraus. Die alte Vermutung zwingend anderer Löschsemantik ist nicht begründet. **Noch offen:** Wortlaut/Stackdiagramm beider AUR-Einträge am Scan, Status unter G/GX-ROM-Revisionen, Verzeichnisse/Fehler.

## 3. LAST versus LASTARG

**AUR-TOC:** `LAST` (3-162) steht eigenständig im historischen Verzeichnis; `LASTARG` erscheint in der ROM-Namentabelle.

Die oben genannte zeitgenössische HP-28/48-Übersicht erläutert, `LAST` sei in `LASTARG` umbenannt worden. Allerdings enthält der alte Text auch die Schreibweise `LASTARGS`, sodass **nicht ohne Gegenprüfung** das genaue Speicher-/Übersetzungsverhalten feststeht.

**Unabhängiger Nachweis:** Der *HP 48G/GX Pocket Guide*, Command Index, führt den gemeinsamen Eintrag `LASTARG or LAST`. Dies stützt die dokumentierte Namensalias-Zuordnung. **Aber** Flagabhängigkeit, Argumentrückgabe, Programmauswertung und ROM-Einstiegspunkte bleiben am AUR/Hardware zu prüfen. Kein eigenständiger RPN-Rechenbefehl allein aus einem Inhaltsverzeichnis-Eintrag.

**Nachtrag aus dem unabhängigen Pocket-Guide-Abgleich:** Die Quellenangabe ist ein Namens-/Kurzfunktionsbeleg, kein vollständiges Verhaltenszertifikat. Der 50-Namen-Abgleich ist unter [AUR A01](HP-48GX-AUR-TEILPRUEFUNG-A01.md) checkpointiert.

## 4. Provenienz- und Qualitätsgrenzen

- **Primärbezug:** Hewlett-Packard, *HP 48G Series User's Guide*, Edition 8, 1994, G-40 und 14-17; *HP 48G Series Advanced User's Reference*, Edition 4, 1994, TOC 3-52, 3-53, 3-162. Quellenmetadaten im [Prüfbericht](HP-48GX-QUELLENABGLEICH-PRUEFBERICHT.md).
- **Direkt betrachtetes Material dieser Teilprüfung:** Textübertragung des Original-Operation-Index und zeitgenössischer technischer Erläuterungstext. Das vollständige Bild des Original-AUR-Stackdiagramms wurde **nicht** eingesehen; darum **keine Freigabe der exakten RPL-Operandenreihenfolge**.
- **Bewusst getrennt:** Das historische Gerät, spätere 48gII-Modelle, andere Emulator-Implementierungen, aktuelle SASD-Codebasis.
- **Auditstatus:** `RSD: COMMAND_DESCRIPTION_CORRECTED_STACK_TEST_PENDING`; `CLUSR: COMPATIBILITY_ALIAS_EVIDENCE_SEMANTICS_PENDING`; `LAST: COMPATIBILITY_ALIAS_EVIDENCE_SEMANTICS_PENDING`.

**Nächster atomarer Semantikblock:** Original-AUR-Seiten 3-52, 3-53, 3-162 und RSD-Referenzseite einzeln als Seitenbild prüfen, die vollständigen Stackdiagramme übertragen und mindestens je einen nachprüfbaren Testfall dokumentieren.
