# Pflichtenheft – SASD Scientific Calculator

**Dokument-ID:** SASD-SCI-PH-001  
**Fassung:** 1.0 – technischer Umsetzungsvorschlag auf Basis des Lastenhefts vom 21.11.2026  
**Stand:** 21.11.2026  
**Quelle:** [Lastenheft `SASD-SCI-LH-001`](LASTENHEFT.md)  
**Repository:** https://github.com/Robin-Goerlach/SASD-Scientific-Calculator  
**Status:** **Technische Soll-Konzeption, nicht als implementiert oder als Detailentwurf vollständig freigegeben zu verstehen.**

> **Verbindliche Priorität:** Zuerst ein zuverlässiger klassischer wissenschaftlicher UPN/RPN-Rechner für das iPhone (M1/M2), offline und werbefrei. Vollständige historische Programme, System-RPL, synthetische Programmierung, CPU-/OS-Emulation und die eigenständige ALG-App sind keine V1.0-Blocker.
>
> **Leseregel:** Aussagen mit **„verbindlich“** beziehen sich auf bereits im Lastenheft beschlossene Ziele oder Architekturgrenzen. Aussagen mit **„Lösungsvorschlag“** bestimmen einen konkreten technischen Weg, der vor Umsetzung per ADR/Review freizugeben ist. Offene Anforderungen bleiben ausdrücklich **OFFEN**. Dieses Pflichtenheft darf sie nicht eigenmächtig entscheiden.

---

## 1. Aufgabe, Grundlage und Abnahmegegenstand

### 1.1 Zweck und Verhältnis zum Lastenheft

Das [Lastenheft](LASTENHEFT.md) beschreibt, **welche Leistung** das SASD-Produkt erbringen muss. Dieses Pflichtenheft beschreibt, **wie** die festgelegten Anforderungen nachvollziehbar, testbar und in einer wartbaren C++20-/App-Architektur realisiert werden sollen. Es dient als Grundlage für Architektur-Decision-Records (ADR), technische Arbeitspakete, Tests, Codex-Aufträge und nachvollziehbare Releases. Es ersetzt **weder** die Lastenheft-Freigabe **noch** spätere Detail-ADRs oder vollständig recherchierte historische Befehlssemantik.

Die **200 Kennungen des Lastenhefts** (einschließlich 20 offener Entscheidungen) sind im vollständigen Rückverfolgbarkeitsverzeichnis in **Kapitel 30** aufgeführt. Jede Quellenanforderung wird einem technischen Lösungsteil und einer Prüfgruppe zugeordnet. Die Bezeichnung „V1-MUSS“ im Lastenheft bleibt unverändert und darf nicht in „optional“ umgedeutet werden. Die in der ersten Version tatsächlich verpflichtenden *Einzelfunktionen* ergeben sich nach Freigabe der V1-Tasten-/Funktionsmatrix.

### 1.2 Fachlicher und technischer Geltungsbereich

- **Scientific (Repository dieses Dokuments):** Classic RPN für iPhone **zuerst**, später eigenständige ALG-Scientific-App und Advanced-RPL-App bzw. optionale zusätzliche ALG-Eingabe in historischen Rechnerprofilen.
- **Getrennter Financial Calculator:** anderes Repository, anderes fachliches Domänenmodell, eigenständige Roadmap/App-Store-Veröffentlichung; nur passend versionierte, quelloffene Komponenten gemeinsam verwenden. Keine Financial-Implementierung oder -Repository-Anlage mit diesem Auftrag.
- **Historische Familien:** 41C/CV (ggf. später CX), 48GX. Sie besitzen absichtlich **verschiedene Programmsprachen, Stackregeln, Speicherbilder und Fehlerkonventionen**.
- **Plattformen:** V1 native iPhone-App mit XS-Kompatibilitätsziel; danach iPad, macOS, Windows, Linux; Android bei späterem gesonderten Beschluss.
- **Quellen der vollständigen historischen Funktionsinventare:** [HP-41C](de/HP-41C-FUNKTIONSKATALOG.md) und [HP 48GX](de/HP-48GX-FUNKTIONSKATALOG.md). Deren historische Einträge begründen **keine automatische SASD-Implementierung**. Funktionen aus Fremd-ROMs werden getrennt erfasst.

### 1.3 Bezeichnungen für Ausbaustatus

| Bezeichnung | Technischer Sinn | Freigabewirkung |
| --- | --- | --- |
| **V1** | Freigegebener und durch Tests belegter Classic-RPN-iPhone-Grundumfang | Blockiert nur die erste klassische App |
| **Architekturvertrag** | Modulgrenze/Datentyp-/Sicherheitsinvariante, die jetzt einzuhalten ist | Nicht gleichbedeutend mit der Umsetzung aller späteren Features |
| **Langfristig verbindlich** | Vereinbarte Produktfähigkeit nach V1 (insbesondere Synthetic B und System RPL im definierten Umfang) | Erhält einen eigenen Meilenstein und eigene Abnahme |
| **Geplant** | Technisch vorgesehen, konkrete Funktions-/Releasefreigabe ausstehend | Nicht als aktuell unterstützt darstellen |
| **Optional** | Byte Grabber C, vollständige Nut-/Saturn-/OS-Emulation usw. | Wird erst nach gesonderter Entscheidung implementiert |
| **Offen** | Präzision, Tastatur, historische Detailsemantik usw. | Muss vor Codearbeit im betroffenen Teil festgelegt werden |

**Kompatibilitätsstufen K1–K4** beschreiben historische Nähe; **M0–M5** Entwicklungsmeilensteine. Die weiter unten beschriebenen technischen Schnittstellen sind **empfohlene Entwürfe**, solange kein ADR diese fixiert.

### 1.4 Vorhandener IST-Stand

Zum geprüften Ausgangsstand existieren: `include/sasd/scientific/rpn_engine.hpp`, `src/rpn_engine.cpp`, `apps/cli/main.cpp`, `tests/rpn_engine_test.cpp`, CMake/CTest und GitHub Actions. Der vorhandene `RpnEngine` besitzt einen **dynamischen Vektor-Stack mit `double`** und Push/Duplicate/Swap/Drop/Clear sowie `+−×÷`. Bei Fehlern bleiben seine Werte unverändert; nichtendliche Eingabewerte werden abgewiesen. **Das ist keine fertige historische Vier-Ebenen-/LAST-X-Zustandsmaschine, keine wissenschaftlich vollständige App und keine iOS-Implementierung.**

Der Weg vom experimentellen Stack zum freizugebenden Classic-Rechner soll **über eine neue fachlich spezifizierte Zustandsmaschine**, nicht über stillschweigendes Uminterpretieren der bisherigen API, erfolgen. Historische Rechnerkerne, ALG-Parser und native Views werden erst dann als vorhanden dokumentiert, wenn tatsächlich Code und Tests dafür vorliegen.

---

## 2. Architekturleitlinien und verbindliche Modulgrenzen

### 2.1 Grundaufbau: kommandogetriebene, headless Domänenschicht

**Lösungsvorschlag** für den schrittweisen Aufbau:

```text
SASD Scientific Calculator / Monorepo
  Apps
    Classic RPN iPhone (V1-Pfad)    ALG Scientific (später)    Advanced RPL (später)
           |                               |                         |
       Plattform-Adapter und Input-Controller / UI-State / Accessibility
           |                               |                         |
       Native C-ABI oder Desktop-Adapter; versionierte Commands/Responses
           |                               |                         |
    +-- Classic-RPN-Zustandsmaschine --+  Moderner ALG-Context   48GX-RPL-Context
    |                                  |          |                  |
    |   (41er-Historik später separat) |        ALG-AST          RPL-Objekte/VM
    +--------- Modelladapter ----------+----------+------------------+
                                     |
                          Gemeinsame Mathematik/Numerik
                                     |
                 Diagnostics / Value contracts / Serialization utilities
```

**Vorgeschriebene Abhängigkeitsrichtung:** App → Anwendungs-/Eingabeadapter → jeweiliger Rechnerkontext → gemeinsame mathematische Dienste. Ein Mathematical Core darf **nicht** von SwiftUI, Windows-APIs, historischen 41er-Registerbytes, 48er-RPL-Objektprologen oder einem Financial-Rechenkern abhängen. Umgekehrt darf ein historischer Interpreter gemeinsame reine Algorithmen verwenden, ohne historische Stack-/Fehlerwirkungen dorthin zu verlagern.

### 2.2 Modulverantwortung und Schnittstellen

| Logisches Modul | Eingabe/Ausgabe | Alleinige Verantwortung | Nicht erlaubt |
| --- | --- | --- | --- |
| **`core/commands`** | normierte Command-ID + Eingabedaten → Response/Diagnose/State-Summary | Eingang für UI/CLI, Orchestrierung, Typ-/Profilprüfung | mathematische Berechnungen in UI-Handlern |
| **`calculators/classic-rpn`** | Key/Command → Stack-/Register-/Mode-State | Tasten-, Stack-/Lift-/LAST-X-/Registersemantik | 48GX-Objekte oder ALG-Parser als Ersatz |
| **`calculators/algebraic`** | Formular/Ausdruck → AST/Evaluation/Ans/History | selbstständiger ALG-Rechnerzustand | Abhängigkeit auf 41er/48er-Interpreter |
| **`libs/expression`** | normierter Quelltext → Lexer-Tokens/AST/Diagnose | Syntax, Vorrang, Position und Fehler | implizite Ausführung von FOCAL/System RPL |
| **`calculators/series41`** | historische Commands/Programme → virt. 41er-Zustand | 56-Bit-Rohregister, FOCAL, später Synthetic | reale Hostadressen |
| **`calculators/series48`** | RPL-Objekte/Programme → virt. 48er-Zustand | User/System RPL, Objekte, Saturn-speicherbezogen | 41er-Registermodell übernehmen |
| **`libs/math`, `libs/numeric`** | Werte, Context, Funktion → numerisches Ergebnis/Diagnose | unabhängige Verfahren | historische Stackwirkung oder GUI |
| **`libs/function-catalog`** | Function-ID + Capabilities → Signatur/Help-ID | reine Funktionseinordnung/Verfügbarkeit | Freischalten unerlaubter historischer Opcodes |
| **`platform/native-bridge`** | C-ABI-Anfrage → stabile Antwort; opaque handles | Ownership, Encoding, Error Boundary | C++-Exceptions/STL in Swift abgeben |
| **`persistence`** | validierter Domänen-Snapshot → atomar gespeicherte Version | Speicher-/Lade-/Migrationstechnik | unkontrollierte Status-/Rechenveränderung |
| **`learning`** | freigegebene Commands/Help-Metadaten → Erklärung/Übung | Offlinehilfe, spätere Lernkurse | zweiter Rechenkern |
| **`tests`** | definierte Eingaben/Referenzen → Ergebnisse, Zustände, Belege | V1-/Cross-App-/historische Regression | Tests auf Basis unrechtmäßig kopierter ROMs |

**Physische Zielverzeichnisse sind Vorschläge**, nicht sofort anzulegende leere Gerüste. CMake-Targets werden erst mit ihrer Implementierung ergänzt. Bestehende öffentliche Header bleiben bis zu einer geprüften Migration erhalten.

### 2.3 Verbotene Kopplungen und architektonische Invarianten

**PH-ARCH-01 (verbindlich):** Keine gegenseitige Laufzeit-/Releaseabhängigkeit Scientific ↔ Financial.  
**PH-ARCH-02 (verbindlich):** Keine gemeinsame 41-/48-Historikzustandsmaschine; nur geeignete, vertraglich definierte Basisalgorithmen teilen.  
**PH-ARCH-03 (verbindlich):** Moderne ALG-Benutzereingabe und historisches gespeichertes Programm sind unterschiedliche Syntax-/Ausführungspfade.  
**PH-ARCH-04 (verbindlich):** Gemeinsame mathematische Verfahren sind UI-neutral; Stack-, Genauigkeits-, Fehler- und Speicherprofile bleiben explizit.  
**PH-ARCH-05 (verbindlich):** Historische virtuelle Adresse wird nie als nativer Hostpointer interpretiert.  
**PH-ARCH-06 (verbindlich):** Ein weiterführendes Feature wird nicht deshalb V1-Pflicht, weil die Architektur es später zulässt.  
**PH-ARCH-07 (verbindlich):** Jede nach außen zugesagte App ist ohne installierte andere App baubar, startbar und im freigegebenen Umfang nutzbar.

---

## 3. C++20-/Build-/Projektstruktur und Entwicklungsprozess

### 3.1 Zielverzeichnisstruktur (nicht IST-Bestand)

```text
SASD-Scientific-Calculator/
├── apps/
│   ├── cli/                          # bestehender Entwicklungsclient
│   ├── classic-rpn/ios/              # V1
│   ├── algebraic/ios/                # eigenständiger ALG-Track
│   ├── advanced-rpl/ios/             # später
│   └── desktop/                      # optional gemeinsame Plattformansichten
├── calculators/
│   ├── classic-rpn/                  # V1-Zustandsmaschine, noch zu bauen
│   ├── algebraic/                    # eigener moderner Rechnerkontext, später
│   ├── series41/                     # FOCAL/56bit/Synthetic, später
│   └── series48/                     # RPL/System RPL/Saturn, später
├── libs/
│   ├── math/                         # reine Algorithmen
│   ├── numeric/                      # Rechenwerte/Context/Präzision
│   ├── expression/                   # ein moderner algebraischer Parser
│   ├── function-catalog/
│   └── diagnostics/
├── platform/
│   ├── native-bridge/                # versioniertes C ABI
│   ├── profiles/
│   └── persistence/
├── learning/
├── tests/
│   ├── core/
│   ├── classic-rpn/
│   ├── algebraic/
│   ├── historical/
│   │   ├── series41/
│   │   └── series48/
│   ├── persistence/
│   ├── integration/
│   └── ui/
├── docs/                             # Lasten-/Pflichtenheft, ADR, Kataloge
├── tools/
├── .github/workflows/
├── CMakeLists.txt
├── AGENTS.md
├── ROADMAP.md
└── TASKS.md
```

Die vorhandene `sasd_scientific_core`-Bibliothek bleibt beim Übergang als experimentelles Basismodul erhalten. **Zielbild**, keine behauptete aktuell vorhandene Dateistruktur.

### 3.2 Build und Versionierung

- Basis: **C++20, CMake/CTest**, kleine eindeutig benannte Bibliotheks-Targets, öffentliche Include-Pfade, Tests ohne GUI. CI auf Linux, Windows und macOS; für iOS zusätzlich Xcode-Build und Geräteprüfungen.
- Vorschlag für künftige Targets: `sasd_math`, `sasd_numeric`, `sasd_classic_rpn`, `sasd_expression`, `sasd_series41`, `sasd_series48`, `sasd_native_bridge` und je Testgruppe getrennte Targets. **Keine sofortige Verpflichtung, all diese Targets anzulegen.**
- Versionierte Schnittstellen; bei ABI-Brüchen oder Persistenz-Schemawechseln Migration/Feature-Gates prüfen.
- Allgemeine Math-Algorithmen dürfen nicht vom aktuellen C#/.NET-SASD-Math-Toolkit abhängig gemacht werden. Dessen C++-Eignung ist erst zu belegen.
- GitHub ist die maßgebliche Quelle. Parallele Codex-Aufgaben erhalten eigene Eigentumsbereiche und bei Bedarf Git-Worktrees/Branches; gemeinsame API-Änderungen koordinieren. Einzelentwickler darf `main` nach erfolgreicher Prüfung direkt aktualisieren.
- Reproduzierbare Artefakte sollen Commit, Compiler/SDK, Plattform, Build-Konfiguration, abhängige Paketversionen, Prüfergebnis und Releasezuordnung erfassen.

### 3.3 Review-/Dokumentationsregeln

Vor Implementierung einer öffentlichen Funktion muss der Auftrag mindestens **Anforderungs-ID, Ziel-App/Modell, Eingaben/Datentypen, Zustandswirkung, Ergebnis, Fehler, Tests, Dokumentation und Abhängigkeiten** enthalten. Kommentare erläutern Invarianten, Modellunterschiede und Sicherheitsgrenzen, nicht nur Syntax. Bei gemeinsamen Änderungen werden alle tatsächlich vorhandenen abhängigen Tests ausgeführt; noch nicht existierende Suites dürfen nicht als erfolgreich bezeichnet werden.

---

## 4. M0: verbindlich vorzubereitende Fachverträge

M0 hat als technische Ergebnisse **nicht** bereits die historische Emulation, sondern für M1/M2 erforderliche Entscheidungen und Prüfungen. Ohne diese müssen Entwickler bewusst stoppen, anstatt historisches Verhalten zu erfinden.

| Kennung | Vor M1/M2 freizugebender Vertrag | Inhalt | Beleg |
| --- | --- | --- | --- |
| **ADR-V1-INPUT** | Tastatur und RPN-Eingabe | vollständige V1-Tasten-/Shift-/ALPHA-Matrix, Eingabepuffer, ENTER, Lift/Drop/LAST-X, Clear/Undo | State-Transition-Tabelle + repräsentative Key-Sequenzen |
| **ADR-V1-NUM** | Zahlen- und Fehlersemantik | Repräsentation/Präzision, Eingabe-/Anzeige-/Rundungsregeln, Winkelmodi, Über-/Unterlauf, definierte Ausnahmen | unabhängige numerische Vektoren und tolerierte Abweichungen |
| **ADR-V1-STATE** | persistenter Zustand | Felder und Versionen, Speicher-/Load-Semantik, Schemawechsel, Defekt-/Recovery-Fälle | Roundtrip- und Crash-/Lifecycle-Tests |
| **ADR-V1-API** | Command/Response + Bridge | Fehler- und Lifetime-Transport, UTF-8, Thread-Affinität, UI-Zustandsbesitz | CLI-/C-ABI-Test, Swift-Integration |
| **ADR-V1-IOS** | iOS-Ziel und Release | iPhone-XS-Mindestversion, Xcode, physische Testgeräte, App-ID, Privacy und SASD-URL | Toolchain-Protokoll und Gerätetests |
| **ADR-V1-FEATURES** | Freigegebener wissenschaftlicher Basisumfang | welche Tasten/Mathematikfunktionen, Speicherregister, Winkel-/Anzeigemodi, Hilfe | Abnahmeliste pro Command und Kontext |

**Wichtig:** Die zuvor diskutierte **Pratt-Parserentscheidung** gehört zum ALG-Track und darf **M1/M2 nicht blockieren**. Details von 56-Bit-Registerordnung, Saturn-Objekten, ROM-Adressbelegung, synthetischer Befehlsliste und Strict Historical sind **architektonische Erweiterungspunkte**, keine zwingenden M0-Implementierungsobjekte.

---

## 5. Command-Modell und steuerbare Rechner-Sitzung

### 5.1 Fachliche API-Eigenschaften

**Lösungsvorschlag:** Jede UI-/CLI-Eingabe wird als eine **typisierte fachliche Aktion** interpretiert, beispielsweise Ziffer, Dezimaltrennzeichen, Exponent, ENTER, Arithmetik, Registeraktion, Moduswechsel, Stackoperation, Clear. Aktueller Befehl und gültiger Rechnerzustand bestimmen die Folgeaktion. Rohes `double`-Push durch jeden Key-Tap würde Eingabe-/Lift-/Fehlerkonventionen unzureichend abbilden.

```text
Input source (touch, keyboard, CLI, automation)
   -> normalized action / command ID
   -> session.execute(action)
        validate capability + entry state + operand types
        calculate proposed transition under numeric context
        apply model-specific stack/register side effects
        commit one consistent calculator state or return diagnostic
   -> immutable read-only view of display/stack/status
   -> frontend renders; renderer never calculates
```

### 5.2 Sitzung, Commands, Resultate

| Abstraktion | Vorgesehene Inhalte | Invarianten |
| --- | --- | --- |
| `CalculatorSession` | Modell-/Profilkennung; aktive Engine; aktueller Zustand; Versions-/Featureinformationen | andere Sessions beeinflussen sich nicht |
| `CalculatorAction` | stabile Command-ID + normierte Parameter, ggf. Eingabezeichen oder Register-ID | nicht unbekannten historischen Opcode ausführen |
| `CalculatorResult` | Erfolg/Fehlercode, optionale Werte-/State-Version, Änderungssummary | kein unkontrolliertes Exception-Leck |
| `CalculatorViewState` | Anzeigezeilen, X/Y/Z/T, Anzeige-/Shift-/Angle-Flags, Fehlermeldungsschlüssel | ausschließlich aus gültigem Zustand abgeleitet |
| `NumericContext` | Präzision, Rundung, Winkelmodus, Darstellungsregeln, Sonderwertepolitik | nicht durch UI-Formatierung heimlich geändert |
| `CompatibilityProfile` | Modell, Historikstatus, Ressourcen und später ROM-/Modul-Capabilities | ausdrücklich auswählbar/validierbar |
| `Snapshot` | Schemakennung, Modell/Profile, Daten mit Prüfintegrität | persistenter Zustand rekonstruierbar |

Die Bezeichner sind **Schnittstellenvorschläge**, keine vorgegebene Klassenstruktur. Fehler sollen als **stabile Codes** mit separaten lokalen DE/EN-Texten transportiert werden.

### 5.3 Konsistente Zustandsübergänge

- Für die moderne Classic-/ALG-Basis gelten vor einer anderen ausdrücklich freigegebenen historischen Regel die Prinzipien **Validieren → Vorschau/temporäres Resultat → vollständiger Commit**.
- Bei Division durch null, ungültiger Zahl, Stackunterlauf, zu großem Ergebnis oder gescheiterter Typkonvertierung bleiben die nicht ausdrücklich zur Fehlerbehandlung bestimmten Nutzdaten unversehrt.
- **Modellspezifische Ausnahme:** Historische Programme können dokumentierte, abweichende Effekte besitzen; sie werden im jeweiligen Interpreter verifiziert, nicht durch allgemeine Atomicity-Regeln überschrieben.
- Anzeige darf für Formatierung runden; dies verändert nicht ohne explizite Operation den gespeicherten Rechenwert.
- Jede Aktion ist mit Vorher-/Nachher-Snapshot und Freigabe-Testvektor prüfbar.

---

## 6. Classic RPN: vierstufiger Stack, Eingabe und Register

### 6.1 Zielzustand

Für den ersten klassischen Rechner wird ein **Vier-Ebenen-orientierter Stack X/Y/Z/T** mit Eingabepuffer, `LAST X`, Lift-/Drop- und `ENTER`-Zuständen gefordert. **Der genaue historische Ableitungsgrad ist vor M1 einzufrieren.** Insbesondere sind Tastaturmodus und interne Rechenregeln nicht aus einer Bildvorlage zu erraten.

**Lösungsvorschlag:** Ein expliziter, testbarer Zustand umfasst folgende logisch getrennte Felder (konkrete Typen ADR-V1-NUM/-STATE):

- `stack.X/Y/Z/T` (numerische Werte und Status), `last_x`;
- `entry` (Ziffernfolge, Exponentteil, Vorzeichen, aktive Editierposition/Validierungszustand);
- `stack_lift_mode` / `enter_pending` als fachlich dokumentierte Zustandsmerkmale;
- `register_bank` mit freigegebenen Registern und validierten Adressen;
- `angle_mode`, `display_format`, Fehler-/Statuscode;
- optional Shift-/Alpha-Modus in **Input Controller oder Session**, je nach finalem Vertrag;
- `schema_version`, `calculator_profile_id` und `numeric_context_id` für Persistenz.

### 6.2 Operationen und abzuschließende Details

| Operation | Verpflichtender Testgegenstand | Noch zu spezifizieren |
| --- | --- | --- |
| Ziffer/Dezimalpunkt/Exponent | Zeichenweise Eingabestates, Darstellung, Vorzeichen, Zahlenübernahme | Exponent-Syntax, Dezimaltrennung, fehlerhafte Nachkommastellen |
| `ENTER` | Vorher-/Nachherzustände aller vier Stackebenen und Lift-Flag | genauen Duplikations- und Übergangseffekt festlegen |
| `+ − × ÷` | `Y op X`, T-/Z-/Y-Verhalten, LAST X und Fehlerzustand | vierstufiges Drop-/T-Replikationsverhalten |
| Unäre Funktionen | nur X oder weitere Registers-/Stackregeln verändern | LAST X, Lift-/Anzeigeeffekt |
| `SWAP`/Roll/Drop | vollständige Stackreihenfolge | welche Aktionen freigegeben werden |
| `STO`/`RCL`/Registerarithmetik | Adresse, Typ, Effekt auf Stack und Zielregister | Zahl/Anzahl verfügbarer Register |
| Clear/Undo/Error-Reset | unterschiedliches Löschen von Eingabe, X, Stack, Fehler, Register | Taste, Menü, Undo-Historie und Speicherwirkungen |
| Winkel-/Anzeigeformat | mathematische Kontexte vs rein optische Darstellung | DEG/RAD/ggf. GRAD, FIX/SCI/ENG |
| `LAST X` | speichert freigegebenen vorherigen Operanden/Wert | welche Befehle LAST X aktualisieren |

**Nicht zulässig:** einfach die bestehende `std::vector<double>`-Engine auf vier Elemente begrenzen und das als vollständige historische Semantik ausgeben. Die bisherige Engine kann als mathematischer Referenzprototyp weiter genutzt oder kontrolliert migriert werden, sobald Tests und Vertrag vorliegen.

### 6.3 Beispielhafte fachliche Golden Tests

- `3 ENTER 4 ENTER 5 × +` → X = 23, **alle weiteren Stackebenen nach freigegebener Tabelle**.
- `10 ENTER 4 −` → X = 6; `10 ENTER 4 ÷` → X = 2,5, bei zuvor definierten Numerik-/Stackregeln.
- Falsche Reihenfolge `4 ENTER 10 −` → X = −6.
- Operation mit nicht ausreichend gültigen Operanden: normierter Fehler und definierter Zustand.
- Fehlerhafte Registrierung / ungültige Registeradresse: kein unkontrollierter Zugriff.
- Bei Fehlern Stack-/Register-/LAST-X-/Entry-Snapshots vollständig vergleichen.
- Mehrfaches ENTER, direktes Nachrechnen, vorherige Fehlerrücksetzung, Moduswechsel und App-Restart gesondert testen.

Die **Abnahmewerte für alle Register** werden erst aus ADR-V1-INPUT abgeleitet; hier absichtlich keine nicht belegte historische T-/Z-Füllregel als bereits beschlossen vorgegeben.

---

## 7. Gemeinsame Mathematik und numerische Genauigkeit

### 7.1 Funktionsaufrufschicht

**Lösungsvorschlag:** mathematische Dienste nehmen **validierte Werte und einen NumericContext** an und liefern Wert/Fehlercode. Historische bzw. App-spezifische Adapter sorgen für Argumentübernahme, historische Beschränkungen, Stack-Effekte und Ausgabe. Pure Algorithmen dürfen die globalen Register einer Session nicht direkt verändern.

Vorgesehene Bibliotheksfamilien: Grundarithmetik, Potenzen/Wurzeln, trigonometrische/exponentielle/logarithmische Funktionen, Konstanten, komplexe Zahlen, Vektor-/Matrixarithmetik, Statistik/Regression, Gleichungslöser/Polynome, Integration, Differentialgleichungen, Zahlensysteme/Bitoperationen, Einheiten und optional grundlegende Finanzmathematik. **Nur freigegebene V1-Kernfunktionen müssen für M2 implementiert sein.**

### 7.2 Numerikvertrag (ADR-V1-NUM)

Die konkrete Wahl zwischen binary64, dezimalbasierter Arithmetik, höherer Präzision oder mehreren Backends wird **nicht** in diesem Pflichtenheft endgültig getroffen. Bevor neue Fachfunktionen freigegeben werden, sind zu spezifizieren:

1. Interner Zahlentyp und erlaubte Wertebereiche; Umgang mit `NaN`, ±`Inf`, `-0` und Über-/Unterlauf.
2. Präzision für elementare und transzendente Operationen; Rundungsmodus und definierte Testtoleranz.
3. Eingabesyntax, Exponentendarstellung, Rundung beim numerischen Einlesen.
4. Anzeigeformat `FIX/SCI/ENG` oder äquivalente freigegebene Modi; Zahl der sichtbaren Stellen.
5. Winkeleinheiten DEG/RAD und ggf. GRAD, trigonometrische Eingaben/Resultate.
6. Verhalten an Definitionsgrenzen, Zweig-/Vorzeichenkonventionen bei Wurzeln/komplexen Funktionen.
7. Unterschiedliche historische Profile: 41er-Bit-/BCD-Register und 48er-RPL-Zahlen sind **nicht** bloße Formatierungsansichten einer `double`-Zahl.
8. Plattformübergreifender Reproduzierbarkeitsanspruch: gleiches Profil/gleiche Testeingabe muss innerhalb der freigegebenen Toleranz übereinstimmen.

### 7.3 Mathematik- und Funktionsmetadaten

Ein **einheitlicher fachlicher Function Catalog** enthält für jede reale Implementierung eine stabile Function-ID, Kategorie, Signatur/Argumentzahl, geeignete Typen, Angle-/Precision-Abhängigkeiten, Fehlercodes, Capability-Merkmale, Hilfe-ID und Testreferenzen. Historische Befehlsaliasse und 48er-Systemprimitive werden **separat** registriert: ein gemeinsamer SIN-Algorithmus macht nicht automatisch einen historischen Opcode verfügbar.

### 7.4 Pflicht zur Testbarkeit

Grundfunktionen werden unabhängig vom Stack geprüft; ihre Modelladapter zusätzlich mit Stack-/Objektzustandstests. Bei Algorithmen, für die mehr als eine Präzisions-/Konvergenzstrategie fachlich notwendig ist, dürfen dokumentierte spezialisierte Implementierungen bestehen; die pauschale Behauptung „ein Algorithmus für jede historische Semantik“ ist untersagt.

---

## 8. Fehlerkatalog, Diagnose und Fehler-Sicherheitsverhalten

**Lösungsvorschlag:** stabile **maschinenlesbare Diagnosecodes** mit getrennten lokalisierten Texten, optionalem Quelltextoffset, Kontextdetails und Klassifizierung. Der Fehlerkatalog umfasst mindestens:

| Kategorie | Beispiel | Erwartete Verarbeitung |
| --- | --- | --- |
| `INPUT` | unzulässige Ziffer/Exponent-Syntax | kein ungültiger numerischer Commit |
| `STACK` | zu wenige Operanden | definierter Fehler; Nutzdaten bleiben gültig |
| `REGISTER` | ungültige Speicheradresse | keine unzulässige Registermutation |
| `DIV_ZERO` | Division durch null | expliziter Fehler nach numerischem Profil |
| `DOMAIN` | Wurzel/Log außerhalb des reellen Bereichs | kontrollierter Typ-/Definitionsfehler |
| `OVERFLOW / UNDERFLOW` | nicht darstellbares Ergebnis | definiertes numerisches Verhalten, kein unbemerkter `NaN`-Leak |
| `TYPE / ARITY` | falscher Objekttyp / Argumentanzahl | nachvollziehbare Fehlermeldung |
| `PARSE / NAME` | ALG-Klammer oder unbekannte Variable | genaue Position / Diagnose |
| `RESOURCE` | zu tiefer Ausdruck, zu großes Objekt/Datei | begrenzter Verbrauch, reproduzierbarer Fehler |
| `COMPAT / UNSUPPORTED` | unbekannter historischer Opcode/Systemcall | kontrollierter virtueller Fehler |
| `PERSIST / VERSION` | beschädigter oder alter Snapshot | Wiederherstellungs- bzw. Migrationspfad |

**Regel:** historische Fehlermeldung/Zustandswirkung kann von der freundlicheren modernen UI-Meldung abweichen. Die Fehlerkategorie ist gemeinsam nutzbar, die semantische Reaktion nicht zwangsläufig.

---

## 9. ALG: Lexer, Pratt-Parser, AST und eigenständiger Rechnerkontext

### 9.1 Trennung der Verantwortlichkeiten

Die **ALG-App ist nicht** Teil des Classic-RPN-V1-Freigabepfads. Sie erhält eine eigene Session mit Ausdruckseditor, `Ans`, Angle Mode, eigenen Variablen, letzter Berechnung/History und separater Versionierung. Ein optional späterer ALG-Eingabemodus in einer 41er-/48er-App verwendet **denselben modernen Parser**, führt jedoch das Ergebnis **nur** über einen dokumentierten Übernahmeadapter in deren Zustand ein.

### 9.2 Parserentwurf (Empfehlung, ADR vor Implementierung)

```text
Unicode/UI-Eingabe → kanonische Token-Normalisierung → Lexer mit Quellpositionsdaten
  → Pratt-Parser für Priorität/Assoziativität
  → Recursive-Descent-Teilregeln für Namen, Gruppierung und Funktionsaufrufe
  → typisierter AST (keine sofortige Auswertung)
  → Name/Typ/Arity/Capability-Prüfung
  → Evaluator unter NumericContext
  → pure Ergebnisvorbereitung
  → explizite Commit-Operation oder Diagnose
```

**Begründung:** Ein Pratt-Parser ist für wachsende Infix-/Präfix-/Postfix-Operatoren kompakter und zentraler erweiterbar; reine Recursive Descent ist für kleine feste Grammatiken einfacher zu lesen, erzeugt jedoch viele Ebenen bei wachsendem Funktionsumfang. Beide sind testbar. Die kombinierte Lösung wird **empfohlen**, erst per ADR verbindlich.

### 9.3 Syntax-Testvektoren

| Eingabe (kanonisch) | Erwartung / Parserregel |
| --- | --- |
| `3 + 4 * 5` | 23, Multiplikation vor Addition |
| `(3 + 4) * 5` | 35 |
| `2 + 3^2` | 11 |
| `20 / 4 * 2` | 10, linksassoziatives Mal/Geteilt |
| `2^3^2` | 512, rechtsassoziative Potenz |
| `-(3 + 4)` | −7 |
| `(3 + 4 * 5^2) / 2` | 51,5 |
| `-2^2` | −4 **gemäß vorgeschlagener moderner Grammatik** |
| `(-2)^2` | 4 |
| `2^-3` | 0,125 |
| `3--4` | 7, unäres Minus |
| `2 + 3 * (4 + 5)` | 29 |

Für einen historischen 48er-algebraischen **Objektausdruck** wird diese moderne Grammatik **nicht automatisch** als historische Semantik ausgegeben.

### 9.4 Ausbau und Risiken

- **Erste ALG-Stufe:** reelle Zahlen, `+ - * / ^`, unäre Vorzeichen, Klammern, vollständiger Input und Quellpositionsfehler.
- **Danach:** Konstanten, Variablen, lesende Registeradapter, Funktionsaufrufe/Typ- und Arityprüfung.
- **Später:** Trigonometrie, komplexe Werte, Matrizen, Vektoren, Statistik, benutzerdefinierte Funktionen, ggf. symbolische Objekte.
- **Offen:** Dezimalkomma/Listentrenner, implizite Multiplikation (etwa `2(3+4)`), Prozentsemantik, Postfixoperatoren, Variablenzuweisung, komplexe Domains, symbolische Unbekannte und Seiteneffekte.
- **Robustheit:** Token-/AST-/Nesting-/Längenlimits; Terminationstests; keine unkontrollierte Rekursion. Beim reinen Ausdrucksevaluieren verändert ein Fehler keinen Rechnerzustand. Uhrzeit/Zufall/Zuweisung benötigen vor Freigabe eine gesonderte Seiteneffektstrategie.

### 9.5 Expliziter Übergang zur historischen Maschine

Ein ALG-Ausdruck darf den historischen Programmspeicher nicht ändern. Für die 41er-Variante müssen Stack Lift, X, LAST X, Register-/Zahlenkonvertierung spezifiziert werden; für die 48er-Variante ist zu unterscheiden zwischen **numerischem Wert**, **algebraischem RPL-Objekt** und **symbolischer Weiterverarbeitung**. Das Umschalten der interaktiven Eingabeart darf gespeicherte FOCAL-/RPL-Programme nicht neu parsen oder umschreiben.

---

## 10. 41er-Familie: historischer Register-/Programmkern

### 10.1 Entkoppelte historische Zustandsbasis

Der 41er-Kern ist ein eigener historischer Ausführungskontext für HP-41C/CV und später optionale Varianten. Er darf nicht durch die moderne ALG-Session und nicht durch 48GX-RPL ersetzt werden. Vor vollständigem historisch genauen Betrieb werden folgende **darstellbare** Zustandskomponenten benötigt:

- Vier-Ebenen-Stack X/Y/Z/T und LAST X, ALPHA, Flags und programmrelevante Register nach historischem Referenzprofil.
- Historische **56-Bit-Rohregister** (sieben Byte) einschließlich ungewöhnlicher/unnormalisierter Bitmuster; Zahleninterpretation ist separater Adapter.
- Byteorientierter Programmspeicher und Programmzeiger; abgeleitetes Listing/Decoder-Cache wird bei Byteänderung ungültig.
- Modell-/Erweiterungsprofil (41C/41CV, eventuell CX; Speicher-/Funktionsmodule), Tastenzuweisungen und Statusverwaltung.
- Kontrollierter virtueller Adress-/Registerraum; kein Zugriff auf reale C++-Adressen.

**Nicht für V1 nötig:** diese historische Byte-/Registerverwaltung vollständig zu implementieren. **Schon früh nötig:** Keine öffentliche Classic-RPN-API so fixieren, dass später nur `double`-Stack und keine historische Ausführung anschließbar wäre.

### 10.2 Reguläre Programme M3

FOCAL-/Tastenprogramme erfordern historisch dokumentierte Befehlsdekodierung, Programmkontrolle, Register-/Flag-/Stackeffekte, Programmanzeige und Verwaltung. Programmimport/-export erhalten eigenständige Formatadapter. Eine **Programmdaten-Datei** ist kein vollständiger **Snapshot**; Programme aus externen Quellen werden als untrusted data geprüft.

### 10.3 Synthetische Programmierung M4

Die kanonische Anforderung `SASD-CALC-COMPAT-041-SYN` bleibt langfristig verbindlich:

| Stufe | Umsetzungspfad | Abnahme |
| --- | --- | --- |
| **A** | einzelne belegte synthetische Bytecodes über den gleichen historischen Programmausführungskern | korrekte Dekodierung, Ausführung, Status-/Stack-/Registerzustände |
| **B – verbindliches langfristiges Minimum** | ausgewählte historische synthetische Programme, Rohbytes, Status- und Programmzeiger, spezielle Tastenzuweisungen und Speicherzustände | Byte-/Snapshot-Roundtrips, Referenzprogramme und differenzierte Kompatibilitätsmatrix |
| **C – optional** | Byte-Hüpfer/Byte Grabber, besondere Speicher-/Firmware-Nebeneffekte | eigene Wirtschaftlichkeits-/Technikentscheidung und Referenztests |

Es wird **kein zweiter kompletter Interpreter nur für synthetische Befehle** angelegt; normale und synthetische Kommandos greifen auf einen konsistenten virtuellen 41er-Zustand zurück. Eine synthetische B-Kompatibilitätszusage ist auf **benannte belegte Programme** beschränkt; sie verlangt nicht pauschal vollständige Nut-CPU-Emulation.

### 10.4 Nachweise

Register-Rohroundtrips aller 56 Bit, erhaltene Programmbytes, normale vs synthetische Befehlsdekodierung, Status-/Zeigeränderungen, Tastenzuweisungen, Switch der Eingabearten ohne Programmkorruption, Test mit unzulässigen virtuellen Adressen und referenzierte historisch verifizierbare Programmläufe.

---

## 11. 48GX-Familie: RPL-Objekte, User RPL und System RPL

### 11.1 Objektbasierte, historisch unabhängige Ausführung

Das 48GX-orientierte Modell besitzt **keinen Vier-Ebenen-41er-Stack**. Es verarbeitet historische RPL-Objekte und -Programme, dynamischen Objektstack, Rücksprung-/Return-Stack und Ausführungsframes. Der vollständige Grundmodell-Funktionskatalog wird in [HP 48GX](de/HP-48GX-FUNKTIONSKATALOG.md) unabhängig geführt; er nennt 517 eindeutige Einträge in einem dokumentierten ROM-Namensindex, **nicht** „517 bereits implementierte SASD-Funktionen“ oder alle System-RPL-Primitiven.

**Lösungsvorschlag:** logische RPL-Objektansichten zusammen mit einem verlustfreien historischen Nibble-/Prolog-Datenvertrag für unterstützte Typen. Unbekannte Rohfelder importierter unterstützter Objekte dürfen durch bloßes Lesen nicht verloren gehen; Schreiboperationen verlangen explizite Codec-/Konvertierungsregeln.

### 11.2 Historische Runtime-Aufgaben

- Logische und historische Objekttypen: Zahlen (reell/komplex), Zeichenketten, Listen, Vektoren/Matrizen, Namen/Variablen, Verzeichnisse, algebraische Objekte, Programmobjekte, später Einheiten/Plots/Bibliotheken.
- Object Stack / Return Stack / Programmkontext und Fehlerzustände.
- User RPL: Kontrollstrukturen, lokale Variablen, Programme, Objekt-/Stackoperationen, definierte Befehlsauflösung.
- Speicher: modellbasierter virtueller Saturn-adressierter Raum, ROM-/RAM-/Kartenprofile, Objektreferenzen und Speicherverwaltung.
- Separater Adapter zu gemeinsamen mathematischen Diensten, nicht als Ersatz für historische Objektkonvertierung.

### 11.3 System RPL langfristig verbindlich

Die Anforderung `SASD-CALC-COMPAT-048-SYSRPL` fordert nach User-RPL-Grundlagen einen **ausgewählten und dokumentierten Umfang** historischer System-RPL-Programme und -Primitive. User RPL und System RPL teilen passende Laufzeitmechanismen, bleiben jedoch bei Rechten, Objekt-/Fehlersystem und internen Voraussetzungen getrennt.

**Vorgesehene virtuelle Aufrufauflösung:**

```text
System-RPL command/object
  → SYSEVAL (historical virtual address) oder LIBEVAL (library identifier)
  → ROM-/Bibliotheksprofil
  → erlaubter, explizit registrierter virtueller Systemaufruf
  → geprüftes RPL-Objekt-/Stack-/Speicherergebnis oder definierter Fehler
```

**Keinesfalls:** historische Adresse als Hostpointer casten oder beliebige native Funktionen/Dateien/Shell-Kommandos durch untrusted RPL-Programme öffnen. Nicht unterstützte ROM-Profile und primitive IDs erhalten kontrollierte Fehler und klaren Kompatibilitätsstatus.

### 11.4 Saturn-Maschinensprache optional

`SASD-CALC-COMPAT-048-SATURN` und eine mögliche Nut-CPU-Forschungsrichtung sind **OPTIONAL M5**. Eine spätere CPU-VM kann über die abstrakte historische Speicher-/Aufrufschicht integriert werden; sie ist **nicht Voraussetzung** für die iPhone-V1 oder die erste User-/System-RPL-Ausbaustufe. Ob spezielle Programme doch tiefe Emulation benötigen, muss anhand realer Referenzfälle entschieden werden.

### 11.5 Historischer Speicher und Grundkonfiguration

Der HP 48GX besitzt als historisches Grundmodell **128 KiB internes RAM**, gegebenenfalls erweiterbar durch Karten; die tatsächliche nutzbare Kapazität wird nicht mit einer pauschalen freien-Nutzer-RAM-Zahl verwechselt. Moderne App-Profile nutzen **keine künstliche 128-KiB-Grenze**. Streng historische Profile sollen später reservierte Bereiche, Karten, Objekt-/Programmverwaltung, sichtbare freie Kapazität und Fehler abhängig von konkretem ROM-/Kartenstand modellieren.

---

## 12. Erweiterungen, Module und Advantage-Pac-Abgleich

### 12.1 Modulschnittstelle (späterer Vertrag)

Ein historischer oder funktionaler Moduladapter beschreibt mindestens: `module_id`, Zielmodell, Version, kompatible historische Profile, öffentliche Fähigkeiten, interne Befehlssignaturen, Register-/Stack-/State-Effekte, persistente Felder, Lizenz-/Quellenangaben, Testgruppe und eventuelle Namenskonflikte. Frühere iOS-Versionen sollen **keine** zur Laufzeit aus Fremdquellen geladenen ausführbaren Plug-ins erfordern; wenn nötig statisch einkompilierte und separat aktivierbare Funktionen.

### 12.2 Historische Gruppen und Doppelimplementierungsschutz

| Referenz | Geplante Umsetzung | Nicht zugesagt |
| --- | --- | --- |
| **Time Module** | modellgerechte Datums-/Zeit-/Alarmbefehle, definierbare Test-Uhr und Zustandsregeln | V1-Pflicht, exakte ROM-Reproduktion |
| **Statistics Pac** | historisch orientierte 41er-Kommando-/Registeradapter auf gemeinsam getestete Statistikverfahren | eigenständiger zweiter Statistikalgorithmus |
| **Advantage Pac** | **optionaler** Adapter für komplexe Zahlen/Matrizen, Vektoren, Polynome, Solver, Integration, Differentialgleichungen, BIN/OCT/DEC/HEX, Boolesche/Bitoperationen, Statistik, finanzmathematische Basisoperationen | Original-ROM, automatisch vollständiges XROM-Binärformat |
| **48GX RAM cards/libraries** | später modell-/ROM-profilabhängige Speicher- und Bibliotheksfähigkeiten | globale 128-KiB-App-Limitierung |

**Doppelimplementierung vermeiden:** Für jede Advantage-Pac-Funktion wird zuerst geprüft, ob der mathematische Algorithmus bereits in den gemeinsamen Bibliotheken oder der 48GX-orientierten Entwicklung vorhanden ist. Der 41er-Adapter ergänzt ausschließlich die historisch notwendige Stack-/Register-/Fehler-/Namenssemantik. Finanzielle Fachworkflows (TVM, IRR/NPV, Anleihen) gehören vorrangig dem separaten Financial Calculator.

---

## 13. Kompatibilitätsprofile, Ressourcen und Modellkonfiguration

### 13.1 Konfigurationsachsen

```text
App / CalculatorFamily
 + InteractiveInputMode (RPN, ALG – falls unterstützt)
 + ExecutionProfile (Modern, HistoricalCoreModernInput, StrictHistorical)
 + ModelROMVersion
 + NumericContext
 + ModuleAndMemoryConfiguration
```

**Kein automatisches kartesisches Produkt:** Nicht jede Kombination ist schon realisiert; das UI bietet nur belegte Kombinationen an. Ein Wechsel in Strict Historical kann moderne ALG-Eingabe im selben Profil einschränken, während ein Hybridprofil moderne Eingabe mit historischem Programmablauf erlaubt.

### 13.2 Speicherregeln

- **Modern:** Ressourcen entsprechen dem realen Gerät und implementierten Sicherheitslimits; keine künstliche historische 41-/48er-Begrenzung.
- **Hybrid:** moderne Eingabeverarbeitung außerhalb des historischen Speichers; Ergebnisübernahme wird auf historisch erlaubte Typen, Größe und Zustandsoperation geprüft.
- **Strict Historical:** später konkrete Register-/RAM-/ROM-/Karten-/Programmpartition, Anzeige freier Kapazität, historische Meldungen und fehlerhafte Zugriffsszenarien anhand eines benannten Referenzmodells.
- Profil-ID und ROM-/Modulkonfiguration gehören bei historischen Zuständen in Snapshot-, Test- und Kompatibilitätsmetadaten.
- Ein echter Hostspeicherzeiger wird nie als historischer virtueller Register-/Saturn-Zeiger exportiert.

### 13.3 Umstellung und Migration

**Lösungsvorschlag:** Bei Wechsel in ein engeres Profil zunächst *Capability- und Ressourcenprüfung*; falls Daten nicht repräsentierbar sind, **nicht** stillschweigend abschneiden oder überschreiben. Der Benutzer erhält Diagnose/Option zum Abbrechen oder expliziten Export. Die genauen UX- und Stackwirkungen müssen beim Profil-ADR beschlossen werden.

---

## 14. Persistenz, Zustand und Datenmigration

### 14.1 Dauerhaft zu sichernde Daten

**V1-Pflicht:** zugesagte Stack-/Registerwerte, LAST X, Eingabepuffer bzw. definierten Wiederaufnahmezustand, Winkel-/Anzeige-/Fehlermodus, aktives Rechnerprofil, zustandsrelevante UI-Optionen. **Später:** FOCAL-Programmbytes, RPL-Objekte, Verzeichnisse, virtuelle ROM-/RAM-/Karten-/Modulzustände, User-Settings und historische Zeiger.

### 14.2 Lösungsvorschlag Snapshot-Protokoll

| Bestandteil | Technische Verantwortung |
| --- | --- |
| Formatkennung, Schema-Version | Unterscheidung neuer/alter oder fremder Dateien |
| Calculator-ID und Profile-ID | keine RPL-Daten als 41er-Register auslegen |
| NumericPolicy-ID | genaue Rückrechnung unabhängig vom Anzeigeformat |
| State Payload | freigegebene Register/Stack/Entry/Modes |
| Längen-/Integritätsangaben | Erkennen von Truncation/Beschädigung |
| Migrationsinformationen | kontrolliertes Einlesen kompatibler Altversionen |
| expliziter Transaktionspunkt | nur vollständige geprüfte Zustände als aktuell verwenden |

**Empfehlung, noch kein konkretes Dateiformat beschlossen:** versioniertes Schema mit validierter Serialisierung; temporäre Datei schreiben, Vollständigkeit prüfen, dann atomar ersetzen (unter den Garantien des Betriebssystems). Währenddessen bleibt eine gültige letzte Version erhalten. Keine ungeprüfte Deserialisierung untrusted Rohspeicherbilder. Für speicherintensive historische Modelle muss Chunking/Größenlimit und sichere Wiederherstellung spezifiziert werden.

### 14.3 Fehler- und Lebenszyklustests

- App-Zwischenzustand und wiederholtes Background/Foreground;
- App-Prozess beendet; danach Neustart;
- Speichern unter hoher Eingabeaktivität, gleichzeitige Persistenzaktionen verhindern;
- beschädigte, verkürzte oder zu neue Snapshot-Version;
- Migration aus real vorhandenen älteren Schemata;
- Zahlenformat und Stack-/Register-/Moduswerte nach Restore identisch;
- keine falsche „Wiederherstellung erfolgreich“-Meldung bei Fehler.

Wichtig: **V1 muss stabilen Rechnerzustand wiederherstellen**, vollständiger Export historischer Programmbibliotheken ist erst M3/M4.

---

## 15. Native iOS-App, Eingabekontroller und Darstellung

### 15.1 Vorgesehene Technologie

**Lösungsvorschlag:** SwiftUI-Oberfläche mit **schmaler versionierter C-ABI** zur C++20-Domäne, ohne STL-Objekte/Exceptions über die Grenze. Vor Implementierung sind Ownership, Memory-Lifetime, Thread-/Main-Actor-Grenzen, UTF-8, Unicode-Tastenlabels, Fehlermeldungen, Bildschirmupdate und iOS-Toolchain auf dem **iPhone XS** zu prüfen. Es wird **kein** bereits existierender iOS-Build behauptet.

### 15.2 Hochformat als erstes UI

- Rechner **füllt die nutzbare Hochformatfläche**. Kein Editor, Desktoppane, Werbebanner, Account oder permanentes Web-Frontend auf dem Startbildschirm.
- Display zeigt freigegebene RPN-Ebenen, Eingabe, relevante Winkel-/Shift-/Statusmodi und klare Fehler.
- Jede freigegebene Funktion ist über Haupt-/Shift-/Alpha-Layer, kontextuelles Menü und ggf. sechs Softmenüpositionen sinnvoll erreichbar. **Genaues Keyboard-Mapping wird aus einem geprüften Tasteninventar abgeleitet**, nicht aus generierter Illustration.
- Dezenter klickbarer **SASD**-Schriftzug **links oben** führt auf die **noch zu bestätigende offizielle SASD-Adresse**; im Flugmodus darf dieser Link die eigentlichen Rechenfunktionen nicht beeinträchtigen.
- Tap-/Long-Press-/Eingabetastenfeedback, ergonomische Ziele, Dynamic Type, Safe Areas, Hochformat und VoiceOver auf dem kleinsten freigegebenen Gerät testen.
- Anzeige und Tasten dürfen sich bei Fehlerzuständen nicht überlagern. Kein Rendern in einer Art, die eine nicht erreichbare Funktion verspricht.

### 15.3 UX-Architektur und Key Inventory

Jeder sichtbare Key erhält eine stabile Key-ID, Primäraktion, Shift-/Alpha-/Softmenu-Aktion, zugelassenen Modus, Label-/Help-ID und Test-ID. Der Input Controller interpretiert UI-Events als `CalculatorAction`, enthält aber keine mathematische Funktion. Die geprüften Befehle sind aus dem **freigegebenen V1-Funktionskatalog**, nicht aus den Originalmodellen ungeprüft übernommen.

Die im Repository sichtbaren SVG-Dateien in `docs/images/` sind **Design-Neuzeichnungen** der diskutierten iPhone-/Desktop-Konzepte, **keine realen App-Screenshots** und keine belastbare historische Tastenvorlage. Die Original-PNGs gehören nicht automatisch zur GitHub-Dateibasis.

### 15.4 Weitere Plattformen (nicht V1)

- **iPad:** angepasste Größe und Multitasking, gemeinsamer Kern.
- **macOS/Windows/Linux:** eigenständige Frontends, vollständige Tastatureingabe, Standardrechner plus optionalen Resizable-Editor, Programmbibliothek, Stack-/Register-/Variableninspektor und später Debugger.
- **Android:** langfristiger Kandidat, keine V1-Pflicht.
- Künftige native Darstellung greift **auf dieselbe fachliche Command-Schnittstelle** zu; plattformabhängige Abkürzungen erzeugen keine eigene Rechenlogik.

---

## 16. Bedienhilfe, Dokumentation und interaktives Lernen

### 16.1 Erste Hilfe-Ausbaustufe

**M2-Pflicht:** kompakte, lokal mitgelieferte Hilfe in Deutsch/Englisch bzw. der konkret freigegebenen Sprachmatrix: Stack/ENTER, Register, Winkelmodus, wichtigsten Funktionen und Fehlerzustände. Kein Internetzwang zur Erklärung einer Taste.

### 16.2 Vollständiger Ausbau (später)

- Funktionsverzeichnis aus tatsächlich registrierten Funktion-/Befehlsmetadaten; Katalogeinträge sind durch Feature-Status gekennzeichnet.
- Offline-Suche nach Name/Kategorie, Kontext-Hilfe per Key, Beispiele für RPN und ALG, Fehlerdiagnose und Stackvisualisierung.
- Interaktive Übungen („gleiches Resultat, anderer Eingabeweg“) mit echter Rechen-/Ausführungs-Engine.
- Schritt-für-Schritt-Modus mit echter Evaluator-/Stack-Trace statt zweiter, möglicherweise abweichender Mathematikimplementierung.
- Spätere Programmierkurse zu FOCAL/User RPL/Synthetic/System RPL nur dann, wenn die gezeigten Funktionen implementiert und getestet sind.
- Inhalte sind eigenständig formuliert; keine ungeprüfte Textübernahme aus historischen Handbüchern.

---

## 17. Scientific / Financial: Wiederverwendung ohne Produktkopplung

**Bindende Entscheidung STR-002:** Das Scientific-Repository bleibt eigenständig; das spätere `SASD-Financial-Calculator`-Repository ist getrennt und wird hier **nicht** angelegt. Financial besitzt eigenes Finanzmodell, RPN-/ALG-UX, App-ID, Tests, Versionierung und Releases. Historische Financial-Rechnernachbildung (z. B. HP-12C, 17BII, 19BII, 30b) bleibt im Financial-Projekt optional.

### 17.1 Shared-Bausteine nach tatsächlichem Bedarf

| Baustein | Projektübergreifend nutzbar? | Einschränkung |
| --- | --- | --- |
| reelle/komplexe Mathematik, Solver, Statistik | grundsätzlich ja | Finanz-Konventionen (TVM, nominal/effektiv, Cashflowzeichen) bleiben Financial |
| numerische Genauigkeitsdienste/Dezimalarithmetik | Kandidat | historisch modellabhängige Rundungen und Objektformate getrennt |
| ALG Lexer/AST/Pratt-Parser | Kandidat | getrennte Variablen-/Funktionsumgebungen und Business-Funktionen |
| generischer Stack-Container | Kandidat | ersetzt nicht die 41er-/48er-Stackregeln |
| Diagnose-/Format-/Testmodule | Kandidat | App-/Modellkonfiguration separat |
| Historical FOCAL/Synthetic/RPL | **nein** | Scientific-spezifische historische Programmlaufzeit |
| Financial TVM/NPV/IRR/Bonds/Abschreibung | **Financial** | kann gemeinsame Numerik verwenden, darf Scientific-V1 nicht belasten |

### 17.2 Paket- und Kopierstrategie

1. Zuerst eine **kleine getestete Bibliothek** für einen real benötigten Scientific-Fall entwickeln.
2. Wenn Financial tatsächlich diese Funktion benötigt: konkreten API-Vertrag und Lizenz prüfen.
3. Bevorzugt **immutable, versionierte Bibliothek** mit gepinntem Release, sofern API stabil und gemeinsame Wartung wirtschaftlich ist.
4. Alternativ **quellcodekopierte Version mit Herkunft, Commit, Lizenz, Änderungen und Wartungsweg**.
5. Keine zwingende gemeinsame Runtime, Netzwerkschnittstelle, Datenbank oder synchronized release.
6. Kein voreiliges großes „Universal Calculator Framework“.

---

## 18. Sicherheit, Datenschutz und Rechte

### 18.1 Bedrohungen

Vertrauensgrenzen sind: Nutzer-/App-Tasten, importierter Ausdruck, externe Programm-/State-Datei, RPL-/FOCAL-/synthetischer Programmcode, historische virtuelle Adressen, Netzwerklink zum SASD-Webauftritt und eingebundene Drittbibliothek.

| Risiko | Kontrollmaßnahme | Nachweis |
| --- | --- | --- |
| ungültiger Stack/Register-/Object-Zugriff | geprüfte Indizes/Typen, keine rohen Hostpointer | Negativtests/Fuzzing |
| System RPL/`SYSEVAL`/`LIBEVAL` | ausschließlich allowlist-basierter **virtueller** Resolver | unzulässige Zieladresse liefert definierten Fehler |
| Synthetic Byte Grabber | nur virtueller Register-/Programmraum, optional | Host-Isolationstest |
| sehr tiefe/teure ALG-Ausdrücke | Token-/Tiefe-/Ausführungs-/Speicherlimits | Limit-/Terminationstests |
| korrupte Snapshot- oder Programmdaten | Länge/Schema/Integrität prüfen, atomarer Restore | Mutations-/Truncationtests |
| unkontrollierte Plugin-Ausführung | früh keine frei geladenen nativen fremden iOS-Binaries | Bundle-/Codeaudit |
| ungefragte Netz-/Telemetrie/Ads | Offline-first, keine Account-/Werbe-SDKs | Airplane Mode und Paketprüfung |
| Rechtsverletzung über ROM/Manual/Screenshot | Clean-room, Lizenz-/Quellen-/Bildnachweis | Provenienz-/Release-Audit |

Historische Authentizität ist **keine** Erlaubnis, hostseitig unsicher zu sein. Für Rechte/Marken gelten bereits dokumentierte MIT-Repository-Lizenz, keine kopierten Herstellerlogos/ROM-Dateien, keine „offizielle HP-App“-Behauptung, und historische Modellnamen nur als sachlicher Kompatibilitätsbezug. Store-Grafiken müssen reale, getestete App-Bilder sein, wenn als echte Screenshots ausgegeben.

---

## 19. Testarchitektur und Freigabebeweise

### 19.1 Testpyramide

```text
End-to-End auf echten iPhones / später Desktop-Apps
    Native Bridge + Persistenz + UI-Aktionen
        Modellkonforme RPN- und historische VM-Zustandstests
            ALG Lexer/AST/Evaluator (separater späterer Track)
                Gemeinsame Mathematik-/Numeriktests
                    Fehler-/Ressourcen-/Sicherheits-/Format-Unit-Tests
```

### 19.2 Benannte Suites

| Testgruppe | Minimum und Abnahmebedingung |
| --- | --- |
| `CORE` | feste Werte, Referenznumerik, Domains, Fehler und Toleranzen |
| `RPN` | alle freigegebenen Haupt-/Shift-/Registercommands mit vollständigen Stack-/LastX-/Entry-Snapshots |
| `ALG-LEX/PAR/AST/EVAL` | Priorität, Assoziativität, Klammern, unäre Zeichen, Namen, Typen, Fehlerpositionen, Limits |
| `CROSS` | gleicher mathematischer Ausdruck über ALG und RPN bei identischem NumericContext → gleiches **Resultat**, nicht zwangsläufig identischer Stackzustand |
| `STATE` | Schema-/Roundtrip-/Migration-/Beschädigungs-/Abbruchtests |
| `41-FOCAL` | Kontrollfluss, Register, Bytes, Flags, Zustands-/Programmreferenz |
| `41-SYN-A/B` | 56-Bit-Bits, synthetische Befehle, Programme, Pointer, Tastenzuweisung |
| `41-SYN-C` | **optional**, Byte-Hüpfer/Firmware-Sonderfälle |
| `48-USER` | Objekte, Stack/Return Stack, lokale Variablen, Programme, Fehler |
| `48-SYS` | Systemprimitive, `SYSEVAL/LIBEVAL`, ROM-Profile, virtuelle Adressen |
| `MEM/EXT` | Modern/Hybrid/Strict-Profil, RAM-Karten, Module, Ressourcen-/Capability-Konflikte |
| `SEC` | korrupte Bytes/Objekte, hostile Inputs, Interpreter-/ABI-Isolation |
| `IOS-UX` | iPhone XS, Tastatur, VoiceOver, dynamische Schrift, Hochformat, Offline, Lifecycle, echte App-Bilder |

### 19.3 Goldens, Quellen und Testdaten

Jeder historische Testfall soll benanntes Modell/ROM-/Modulprofil, Inputprogramm oder Command-Sequenz, **erwarteten vollständigen relevanten Zustand**, Referenzquelle, Lizenzstatus, numerische Toleranz und Wiederholbarkeit dokumentieren. Ein Emulator kann als Vergleich dienen, ersetzt nicht unabhängige historische Dokumentation/Beobachtung. Proprietäre Original-ROMs oder urheberrechtlich geschützte Programme sind nicht automatisch Testfixtures.

### 19.4 CI und Belege

- Jede PR/Änderung am portablen Kern: CMake-/CTest-Läufe Linux/Windows/macOS (soweit vorhanden und CI definiert).
- Für iOS gesonderte Xcode-/Bridge-/Gerätesuites; erfolgreicher Desktop-CI-Lauf beweist **nicht** iPhone-XS- oder App-Store-Fähigkeit.
- Für jede reale Releaseversion: Git-Commit/Tag, Build-Konfiguration, Geräte/SDK, Testlauf-IDs, bekannte Abweichungen, Datenschutz-/Lizenzprüfung und Freigabe.
- Späteres Erweitern historischer Programme darf vorhandene funktionierende V1- und ältere User-RPL-Regressionstests nicht brechen.

---

## 20. Qualität, Leistung und Robustheitsziele

### 20.1 Qualitative Anforderungen

- Bei gewöhnlicher Tastenbedienung soll die Anzeige **subjektiv ohne störende Verzögerung** reagieren; konkrete numerische Antwortzeit-/Startzeit-/Speicherziele werden erst nach Referenzmessungen auf iPhone XS als verbindliche Schwellen freigegeben.
- Keine unsachgemäßen Überlagerungen/Abschneidungen von Display, Softmenü und Tasten; Prüfen gegen kleine Bildschirme/Schriftvergrößerung.
- Numerische Korrektheit gemäß freigegebenem NumericContext und dokumentierter Toleranz; Abweichungen von historischen Modellen sind **nachweisbar**, nicht versteckt.
- Fehlerhafte Eingabe oder Datei darf keine Hostkompromittierung, unkontrolliertes Speicherwachstum oder Datenverlust erzeugen.
- Keine permanente Netz-/Serverabhängigkeit, keine Werbung, kein Abo, keine obligatorische Telemetrie.

### 20.2 Noch nicht freizugebende Messwerte

**Keine erfundenen SLA-Zahlen:** maximale AST-Tiefe, Eingabebytes, durchschnittliche Antwortzeit, Speicherbudget, App-Startzeit, Crash-free Rate, verfügbares Mindest-iOS und konkreter Dezimalgenauigkeitswert sind im Lastenheft **nicht abschließend festgelegt**. Das technische Team erstellt vor dem betreffenden Release eine reproduzierbare Benchmark-/Grenzfallliste und ein ADR mit gemessenen Zielwerten. Unverifizierte Zahlen dürfen nicht zur angeblich bereits beschlossenen Pflicht werden.

---

## 21. Implementierungs- und Veröffentlichungsphasen M0–M5

### 21.1 Die eine maßgebliche Roadmap

| Phase | Technische Umsetzung | Gate und Nachweis |
| --- | --- | --- |
| **M0 – Fundament** | C++20/CMake, CI, Lasten-/Pflichtenheft/ADRs, V1-Key-/Stack-/Numerik-/Zustands-/iOS-Verträge, saubere Modulgrenzen | offene V1-Entscheidungen freigegeben; bestehende Kerntests grün |
| **M1 – Classic RPN Core** | definierte Vier-Ebenen-Zustandsmaschine, ENTER/LAST X, Register, Grundarithmetik, Basiswissenschaft, Fehler, Snapshot-Schema | alle freigegebenen `RPN/CORE/STATE`-Unit-/Golden-Tests grün |
| **M2 – iPhone App Store V1.0** | SwiftUI/native Bridge, vollständige V1-Tastatur, Display, Offlinehilfe, Speichern/Restore, Offline/Werbefreiheit, SASD-Link, reale XS-Tests | vollständiges Release-Gate `IOS-UX`, Legal/Privacy, bekannte Grenzen |
| **M3 – Anwenderprogramme** | 41er-FOCAL, 48er-User-RPL, Programme/Import/Export, referenzierte Regression | versionierte K2-Abdeckungsmatrix und Tests |
| **M4 – systemnahe historische Funktionen** | Synthetic 41 A/B, definierter System-RPL-Teilumfang, virtuelle ROM-/RAM-Funktionen, Module, historische Profile | versionierte K3-Abdeckungsmatrix und Sicherheitsbelege |
| **M5 – Maschinen-/OS-Forschung** | optional Nut-/Saturn-Interpreter, evtl. Betriebssystem-/Hardware-Simulation | **nur bei gesonderter Freigabe**, eigene K4-Studie |

Die früheren Vorschläge M0–M6 sind fachlich in die releaseorientierte M0–M5-Baseline integriert. **M3–M5 sind nicht streng sequenziell**; Teilstudien können parallel erfolgen. Ein historisches Forschungsfeature bekommt jedoch **keine** Freigabe-Blockerrolle für M2.

### 21.2 Parallele, bewusst nicht blockierende Entwicklungslinien

- Eigenständige ALG-App / gemeinsamer Parser nach stabilisiertem Math-Vertrag.
- Erweiterte Wissenschaft: komplexe Zahlen, Matrizen, Solver, Statistik, Einheiten und Plot-/Symbolikforschung.
- 48er-Objekt- und RPL-Fundament kann unabhängig vom Classic-UI-Releaseteam vorbereitet werden.
- Hilfe/Training wird ab M2 minimal und danach umfangreich.
- Weitere Plattformen und optionale Desktop-IDE erhalten eigene Liefer- und Abnahmematrizen.
- Financial wird separat begonnen und veröffentlicht, wenn es den Scientific-Fortschritt nicht beeinträchtigt.

---

## 22. Detaillierte Arbeitspakete und Abhängigkeiten

| Arbeitspaket | Eingang | Umsetzung | Fertig, wenn | Priorität |
| --- | --- | --- | --- | --- |
| **WP-00 Basis / source review** | Repository, Lastenheft, historische Kataloge | Tests, CI, Lizenz, Architektur, API-Review | aktuelle Foundation unverändert validiert | M0/P0 |
| **WP-01 V1 Key/State-ADR** | geprüfte reale Bedienfunktionen | Key-ID-/Shift-/ENTER-/Stacktabellen | alle fachlich offenen V1-Regeln unterschrieben | M0/P0 |
| **WP-02 Numerikvertrag** | Referenzdaten und Zielgerät | Typ, Rundung, Fehler, Context und Benchmarks | definierte Testvektoren vorhanden | M0/P0 |
| **WP-03 Classic state engine** | WP-01/WP-02 | X/Y/Z/T, Entry, LAST X, Registers, Modes | `RPN`-State-Goldens bestanden | M1/P0 |
| **WP-04 Shared basic math** | WP-02 | Basis-/wissenschaftliche Operationsdienste | `CORE`-Tests, keine UI-Abhängigkeit | M1/P0 |
| **WP-05 Persistenz** | WP-03 und State-ADR | versionierte, geprüfte Snapshots/Migration | `STATE`-Tests inklusive Korruption | M1–M2/P0 |
| **WP-06 iOS/native bridge** | WP-03/04, Xcode-Vertrag | SwiftUI, C ABI, Layout, Fehler/Accessibility | echte iPhone-XS-Integrationstests | M2/P0 |
| **WP-07 Release + help** | WP-03–06 | Offline-Hilfe, SASD-Link, Legal, Store Assets | alle M2-Gates belegbar | M2/P0 |
| **WP-08 ALG-App** | Shared math API + ALG ADR | Lexer/AST/Parser/Context/Editor | `ALG`/`CROSS`-Tests, separat baubar | Parallel, nicht V1 |
| **WP-09 Series41 FOCAL** | historischer Rohregister-/Bytevertrag | normale Programmlaufzeit/Datei-/Snapshot-Adapter | `41-FOCAL`-Golden | M3 |
| **WP-10 Series48 User RPL** | Objektnibble-/Speichervertrag | RPL-Objekte, VM, Daten-/Return-Stack | `48-USER`-Golden | M3 |
| **WP-11 Synthetic A/B** | WP-09 + Belege | ausgewählte synthetische Bytes/Programme | `41-SYN-A/B`-Golden, B-Mindestumfang dokumentiert | M4, langfristig |
| **WP-12 System RPL** | WP-10 + ROM-Profil | virtuelle Systemprimitive/`SYSEVAL/LIBEVAL` | `48-SYS`-Golden, Scope dokumentiert | M4, langfristig |
| **WP-13 Module + Profile** | historische Familien-/Math-Verträge | Time/Statistics/Advantage-Adapter, Karten/Profile | `MEM/EXT`-Tests; ohne ROM-Kopie | M4+ |
| **WP-14 Training/desktop** | freigegebene Commands | DE/EN-Hilfe, Übungen, Desktop-Inspektoren | reale Core-Kommandos, UI-Test | post-M2 |
| **WP-15 Nut/Saturn research** | nachgewiesene K3-Lücken | Kosten-/Machbarkeit/Prototyp | eigene optionale ADR-Entscheidung | M5 optional |
| **WP-16 Financial reuse** | zweiter Verbraucher, License/API | gepinnte Paketversion oder dokumentierter Source-Copy | unabhängige Produkt-Builds/Releases | separat |

**Keine Arbeitspakete WP-08 bis WP-16 sind pauschale Voraussetzungen für den erfolgreichen Abschluss von WP-07.**

---

## 23. Release- und Änderungsverwaltung

### 23.1 Definition of Done je Arbeitspaket

Ein „fertiges“ Feature benötigt, entsprechend seinem geltenden Scope: implementierte Funktion, konsistenten API-/Zustandsvertrag, positive/negative/Grenztests, Entwickler-/Benutzerdokumentation, aktualisierte Requirements-/Funktionsmatrix, Versions-/Modellprofil, korrekte Fehlerbehandlung, CI-Nachweis, Rechteprüfung und ggf. reale Gerätetests. Für historische Features gehört ein unabhängiger Kompatibilitätsbeleg dazu.

### 23.2 Unabhängige Versionierung

- **Scientific Classic iOS V1:** eigene Releaseidentität, minimale geprüfte Funktionalität.
- **Scientific ALG und Advanced RPL:** eigene Build-/Versions-/Store-IDs bei tatsächlicher Veröffentlichung; gemeinsames Monorepo heißt **nicht** synchronisierte Freigabe.
- **Financial:** eigenständiges GitHub-Repository, eigener technischer/professioneller Kern und Release.
- Gemeinsame Pakete werden pro Verbraucher gepinnt, changelog-/kompatibilitätsgeprüft und dürfen keine fremde Releaseentscheidung blockieren.

### 23.3 Kompatibilitätsnachweise

Jeder veröffentlichte Kompatibilitätsgrad nennt: **K1–K4-Ziel**, *welche* Funktion/Programme unterstützt sind, *welcher* Modell-/ROM-/Modulstand, *welche* Syntax-/Ergebnis-/Zustands- und ggf. Maschinenebene geprüft wurde sowie bekannte Abweichungen. Eine historische Funktionskatalogliste allein ist **keine implementierte Abdeckung**.

### 23.4 Änderung dieses Dokuments

Dieses Pflichtenheft ist eine **abgeleitete technische Planung**. Eine Änderung der produktstrategischen MUSS-Pflichten, M2-Gates oder langfristig zugesagten Synthetic-B-/System-RPL-Ziele erfordert einen **neuen datierten Produktentscheid** und Anpassung des Lastenhefts, nicht lediglich eine Änderung des Pflichtenhefts. Technische Vorschläge dürfen über ADRs nach Test-/Aufwandsbewertung konkretisiert werden.

---

## 24. Entscheidungsregister: Was vor Implementierung **offen** bleibt

Die 20 expliziten `LH-OD-001` bis `LH-OD-020` aus dem Lastenheft werden **vollständig in Kapitel 30** mitgeführt; hier die Zuordnung zu technischen ADRs und Gates. Dies sind **keine stillschweigend angenommenen Werte**.

| Entscheidung | Technisches Ergebnis | Fällig | Status |
| --- | --- | --- | --- |
| `LH-OD-001` | vollständige Tasten-/Shift-/ALPHA-/Anzeige-/Command-Matrix | vor M1 | offen |
| `LH-OD-002` | RPN-ENTER, LAST X, Lift/Drop/Roll, Entry, Reset, Undo als State-Tabelle | vor M1 | offen |
| `LH-OD-003` | Zahlentyp, Präzision, Rundung, Winkel/Format, Grenzfallregeln | vor M1 | offen |
| `LH-OD-004` | Schema/Snapshot, Schreibtransaktion, Recovery/Backups | vor M1/M2 | offen |
| `LH-OD-005` | iOS-Minimum, Xcode, XS-Testgerät, Bundle-ID, Signing | vor M2 | offen |
| `LH-OD-006` | offizieller SASD-Link, Marken-/Store-/Bildrechte | vor M2 | offen |
| `LH-OD-007` | DE/EN-Hilfeumfang, Preisentscheidung bei werbe-/abofreiem V1 | vor M2 | offen |
| `LH-OD-008` | Pratt-/Grammatik-ADR, Locale, Prozent, Seiteneffekte | vor ALG | offen |
| `LH-OD-009` | getrennte App-IDs, Version-/Store-Strategie, Kombi-App | vor deren Release | offen |
| `LH-OD-010` | 41er-FOCAL-/Register-/Byteformat/legale Programme | vor M3 | offen |
| `LH-OD-011` | 48er-RPL-/Objekt-/Nibble-/Verzeichnis-/Austauschformat | vor M3 | offen |
| `LH-OD-012` | ausgewählte Synthetic A/B-Testprogramme, C-Nutzen | vor M4 | offen |
| `LH-OD-013` | ROM-Profil, erste System-RPL-Primitiven, `SYSEVAL/LIBEVAL` | vor M4 | offen |
| `LH-OD-014` | Strict-Historical-RAM/ROM/Karten/Fehler/Bericht | bei Profilbau | offen |
| `LH-OD-015` | Modul-Features, Ausnahmen und XROM-Rechte | vor Modul | offen |
| `LH-OD-016` | Paket vs. Codekopie mit Lizenz/Provenienz | bei Financial-Reuse | offen |
| `LH-OD-017` | separates Financial-Projekt/TVM-/Finanzkonventionen | Financial-Start | offen |
| `LH-OD-018` | Nut-/Saturn-/OS-Emulation Nutzen/Kosten/Umfang | M5 optional | offen |
| `LH-OD-019` | Desktop/iPad/Android/Training-Ausbau | jeweiliger Ausbau | offen |
| `LH-OD-020` | geprüfte HP-48GX-Katalogvollständigkeit jenseits ROM-Namensindex | katalog-/referenzbezogen | offen |

**Ausdrücklich keine offene Grundsatzfrage:** M2 benötigt **keine** vollständige historische Gesamtemulation. Der klassische RPN-Rechner wird nicht von ALG verdrängt. Scientific und Financial werden nicht verschmolzen.

---

## 25. Detail-Abnahmeszenarien für die erste iPhone-Version

Die folgende Liste beschreibt **technisch testbare Szenarien**, keine Behauptung bereits vorhandener Tests. Endgültige exakte Stack-/Anzeige-„Expected“-Werte werden aus den vorher freigegebenen ADRs abgeleitet.

| Test-ID | Benutzer-/Systemaktion | Beobachtung und Abnahme |
| --- | --- | --- |
| **AC-V1-001** | Erste Installation / Kaltstart offline | Rechner sofort nutzbar, kein Login/Netzaufruf, definierter Anfangszustand |
| **AC-V1-002** | `3 ENTER 4 ENTER 5 × +` | X zeigt 23; X/Y/Z/T, LAST X und Flags entsprechen genehmigtem RPN-Vertrag |
| **AC-V1-003** | `10 ENTER 4 −` und `10 ENTER 4 ÷` | 6 und 2,5; vollständiger Stacknachweis, richtige Operandenreihenfolge |
| **AC-V1-004** | Trigonometrie in DEG und RAD | Resultate innerhalb freigegebener Toleranz; Modusanzeige korrekt |
| **AC-V1-005** | Wurzel/Potenz/Logarithmus und ungültiger Definitionsbereich | richtiges Ergebnis oder definierter Fehler, ohne beschädigten Zustand |
| **AC-V1-006** | Register `STO`, `RCL` und freigegebene Registerarithmetik | richtiger Inhalt, Stack-/LAST-X-Effekte gemäß Matrix |
| **AC-V1-007** | mehrfach ENTER, Swap/Roll, Clear/Undo und Fehler-Rücksetzung | reproduzierbare vollständige Übergangssnapshots |
| **AC-V1-008** | Rechner benutzen, App in Hintergrund, beenden, neu starten | relevanter Zustand identisch / definierte Wiederaufnahme |
| **AC-V1-009** | Korrupter, alter oder zu neuer Snapshot | App bleibt bedienbar, Fehlerrückmeldung und Daten-Recovery wie spezifiziert |
| **AC-V1-010** | Anzeige FIX/SCI/ENG oder freigegebene Formatvarianten | zugrundeliegender numerischer Wert verändert sich nicht |
| **AC-V1-011** | iPhone XS im Hochformat, Shift-/ALPHA-/Softmenüs | alle V1-Funktionen erreichbar, keine überdeckten Tasten/Labels |
| **AC-V1-012** | VoiceOver, dynamische Schrift, Safe Areas | verständliche Labels, verlässliche Bedienbarkeit |
| **AC-V1-013** | Flugmodus, App-Nutzung, Zugriff auf SASD-Link | Berechnungen/Hilfe offline; Weblink ist optionaler externer Aufruf |
| **AC-V1-014** | App-Paket/Netzwerkverhalten prüfen | keine Werbung/SDK, kein Abo-/Loginzwang, keine notwendige Cloud |
| **AC-V1-015** | Store-Paket bauen, App-Listing prüfen | Signatur, iPhone-XS-Gerätebeleg, Datenschutz, Bildrechte, echte Screenshots |
| **AC-V1-016** | Regression/CI/Linux-Win-mac + iOS-Test | Tests/Builds protokolliert; keine kritischen offenen M1/M2-Fehler |
| **AC-V1-017** | Release-Dokumentation anzeigen | umgesetzte Funktionen und **nicht** unterstützte historische Programme/Profile korrekt gekennzeichnet |

Ein fehlender FOCAL-, Synthetic-, System-RPL- oder Saturn-Test ist **kein V1-Fehler**, sofern dieser Teil nicht zum genehmigten V1-Umfang gehört. Ein defektes `ENTER` oder eine fehlerhafte reelle Division dagegen **blockiert** die erste App.

---

## 26. Nachweise für spätere ALG-, FOCAL-, RPL- und Erweiterungsfreigaben

| Test-ID / Ziel | Technischer Nachweis | Releaseabhängigkeit |
| --- | --- | --- |
| **AC-ALG-001** | Lexer-/AST-Test sämtlicher [Präzedenzfälle](en/ALGEBRAIC-INPUT.md) einschließlich rechtsassoziativem `^` und unärem Minus | Nur ALG-App/ALG-Eingabemodus |
| **AC-ALG-002** | Pure Auswertung, Variable/Function Lookup, Arity/Type/Error-Position, Depth/Timeout-Schutz | ALG |
| **AC-ALG-003** | ALG-Ergebnisimport unter 41-/48-Profil ohne Programmbyte-/RPL-Korruption | Hybrid-ALG-Freigabe |
| **AC-41-001** | historisch belegte 41er-Stack-/Register-/Programmoperationen | K2/M3 |
| **AC-41-002** | alle 56 Rohregisterbits, Byteprogramm-Export/Import und Zeigeränderungen | Synthetic K3/M4 |
| **AC-41-003** | ausgewählte synthetische Programme A/B gegen Referenz, Host-Isolation | K3/M4 |
| **AC-41-004** | Byte-Hüpfer/Byte Grabber C gegen Referenz | nur optional |
| **AC-48-001** | logische und historisch dargestellte RPL-Objekte, Daten-/Return-Stack und User-Programme | K2/M3 |
| **AC-48-002** | Systemprimitive, `SYSEVAL`, `LIBEVAL`, ROM-/Bibliotheksprofile, ungültige Adressen | K3/M4 |
| **AC-EXT-001** | Time/Statistics/Advantage-Adapter gegen 41er-Stack-/Register- und gemeinsame Mathematiktests | Erweiterungsrelease |
| **AC-MEM-001** | Modern-/Hybrid-/Strict-Historical-Ressourcen, 48GX-128-KiB-Grundprofil und Karten | eigener Historikrelease |
| **AC-MACHINE-001** | Maschineninstruktions-/Hardware-/OS-Konformität mit legalen Quellen | erst bei M5-Entscheidung |
| **AC-EDU-001** | Hilfe/Übungen rechnen nachweislich mit derselben Domain-Engine | Trainingsrelease |
| **AC-FIN-001** | Scientific-Bibliothek versioniert/kopiert dokumentiert; Financial allein baubar und releasbar | nur Financial-Projekt |

---

## 27. V1-Lieferobjekte und Release-Dokumente

| Artefakt | Realisierungsziel | Voraussetzung |
| --- | --- | --- |
| Rechenkernbibliothek | sauber versionierte C++20-API, Classic-RPN-Zustandsmaschine, Mathematik | M1 |
| Konsolentesttreiber | Referenz-/Entwicklungs-CLI, reproduzierbare Kommandoausführung | M1 |
| Native iOS-App | vollständiges freigegebenes Tastenfeld, Anzeige, Store-Paket | M2 |
| C-ABI-Adapter | dokumentierte nicht-werfende Schnittstelle, Lifecycle/Ownership | M2 |
| Persistenzkomponente | versionierte, überprüfte lokale Zustands-/Recovery-Strategie | M2 |
| Offlinehilfe | kurze Bedien-/Fehlerhilfe für reale freigegebene Befehle | M2 |
| Funktions-/Kompatibilitätsmatrix | „implementiert / getestet / teilweise / fehlt“ pro Version | M2 |
| Build-/Testprotokoll | Commit/Toolchain/Testdaten/Geräte/Testergebnis | M2 |
| Rechtliche Produktunterlagen | MIT-/Drittanbieter-Nachweise, App Store, Datenschutz, echte Screenshots | M2 |
| Spätere Programmdokumente | 41er-/48er-Dateiformate, Virtual Memory, A/B-Systemprimitiven | M3/M4 |
| Future RPL/ALG/Financial Releases | eigene getrennte Freigabebelege, keine gemeinsame Abnahmesperre | bei Bedarf |

Das Pflichtenheft ist **kein** Implementierungsauftrag. Es beschreibt die zukünftige Lieferpflicht und ermöglicht, daraus gezielte Arbeitspakete zu erstellen.

---

## 28. Konsistenzprüfung: Beschlüsse und mögliche Fehlinterpretationen

| Frühere Diskussion / mögliche Fehldeutung | Maßgebliche Auflösung |
| --- | --- |
| „ALG auch auf historischen Rechnern“ vs. „eine eigenständige ALG-App“ | **Beides architektonisch vorgesehen**: eine neutrale ALG-Engine, aber eine separate ALG-App und mögliche spätere Übergabeadapter; RPN-V1 bleibt zuerst. |
| „eine mathematische Funktion einmal“ vs. „historische Zahlen sind verschieden“ | möglichst gemeinsame **Algorithmen**, ausdrücklich getrennte Modellrepräsentation/Fehler-/Stack-/Präzisionsregeln. |
| „zwei historische Rechnerkerne parallel“ vs. „V1 muss nur ein ausgereiftes Modell haben“ | 41/48-Grenzen schon jetzt beachten; für M2 ist **nur der freigegebene klassische RPN-Rechner** notwendig. |
| „Synthetic B langfristig verbindlich“ vs. „K3 vorerst kein V1-Blocker“ | langfristiges B-Ziel bleibt, aber wird **nicht** als M2-Gate behandelt; C ist optional. |
| „System RPL verbindlich“ vs. „Saturn optional“ | **ausgewählter dokumentierter System-RPL-Umfang** langfristig; keine pauschale ROM-Vollständigkeit, CPU-Emulation optional. |
| „historisches HP-48-RAM 128 KiB“ vs. „moderne Geräte dürfen mehr“ | **opt-in historisches Profil**; Modern kennt keine künstliche 128-KiB-Grenze. |
| „Advantage Pac bietet Mathematik/Finanzen“ vs. „Financial separat“ | historisch inspirierte Scientific-Funktionsadapter möglich, vollständige Finanz-Workflows bleiben Financial. |
| „erste ALG-App könnte früher fertig sein“ vs. „Scientific V1 soll klassisch RPN sein“ | ALG darf parallel vorankommen, hat aber **keinen Vorrang** vor klassischem RPN-V1. |
| „ein Monorepo“ vs. „unabhängige Apps/Financial“ | Scientific-Monorepo mit unabhängigen Scientific-Targets; Financial **separates** Repository und Release. |
| „auf dem Screenshot sieht man Taste X“ vs. „historischer Funktionskatalog“ | Grafik ist Entwurf; verbindlich nur freigegebenes Tasteninventar und unabhängiger historischer Quellenbeleg. |
| „vorhandene RPN-Engine“ vs. „historisch korrekter Vier-Ebenen-Stack“ | ursprünglicher dynamischer `double`-Testkern wird nicht als historisch kompatibel ausgegeben. |

---

## 29. Anhänge: technische Referenzdokumente

### 29.1 Quellen und Projektplanung

- [Lastenheft (verbindliche fachliche Quelle)](LASTENHEFT.md)
- [HP-41C-Funktionskatalog](de/HP-41C-FUNKTIONSKATALOG.md)
- [HP-48GX-Funktionskatalog](de/HP-48GX-FUNKTIONSKATALOG.md)
- [Konsolidierte Anforderungen](de/ANFORDERUNGEN.md)
- [Requirements Matrix / V1 IDs](en/REQUIREMENTS-MATRIX.md)
- [Release-V1-Anforderungen](en/RELEASE-V1.md) / [Checkliste](en/RELEASE-CHECKLIST.md)
- [Architektur](en/ARCHITECTURE.md) / [Mehrrechner-Architektur](en/MULTI-APP-ARCHITECTURE.md)
- [ALG-Planung](en/ALGEBRAIC-INPUT.md)
- [Historische 41er-Planung](en/HISTORICAL-41.md) / [historische 48er-Planung](en/HISTORICAL-48.md)
- [Module](en/MODULES.md), [gemeinsame Bibliotheken](en/SHARED-COMPONENTS.md), [Lernen](en/LEARNING.md)
- [Historische Forschungs-/Rechtsquellen](en/REFERENCE-SOURCES.md), [Sicherheit/Rechte](en/SECURITY-AND-RIGHTS.md)
- [Testmatrix](en/TEST-MATRIX.md), [Entscheidungsfragen](en/DECISION-QUESTIONS.md)
- [ROADMAP](../ROADMAP.md), [TASKS](../TASKS.md), [AGENTS](../AGENTS.md)
- [Designillustrationen und Bildherkunft](images/README.md)

### 29.2 Quellencharakter und Rechte

Historische Dokumentation und Emulatoren sind **Referenzmaterial**, aber keine Lizenz zur Weiterverteilung von ROM-Abbildern, Firmware, Handbüchern, Programmeinträgen oder Fremdbildern. Für jeden Testkorpus gilt eigenständige Herkunfts-/Rechteprüfung. Die über 130 Standardoperationen/Bedienfunktionen des 41C und die 517 dokumentierten Namenseinträge des 48GX-ROM-Index sind **Katalogaspekte**, keine automatischen Product-Backlog- oder V1-Funktionszählungen.

### 29.3 Stand und Änderungsvorbehalt

**Stand dieses Pflichtenhefts:** technische Konzeption mit weitreichender Traceability; **kein** Hinweis darauf, dass die vorgeschlagenen Module/Interfaces/ADRs schon implementiert wurden. Falls Anforderung, Implementierung und historisches Referenzverhalten voneinander abweichen, muss die Abweichung **sichtbar** gemacht und begründet entschieden werden.

---

## 30. Vollständige Rückverfolgbarkeitsmatrix Lastenheft → technische Umsetzung → Prüfung

Diese Matrix übernimmt **jede** eindeutige Anforderungs-ID und ihren **originalen Status / Entscheidungszeitpunkt** aus [`docs/LASTENHEFT.md`](LASTENHEFT.md). Die Kurzbeschreibung kommt aus der dortigen Anforderungstabelle. Ihre Zuordnung zu diesem Pflichtenheft ist ein **technischer Lösungsvorschlag**, soweit nicht bereits bindende Architekturgrenzen übernommen sind. **Kein Eintrag bedeutet automatisch „implementiert“**.

- **LH-ID** = Quellanforderung; nicht ersetzen oder umnummerieren.
- **Originalstatus** = aus dem Lastenheft übernommen.
- **PH-Abschnitt** = hier spezifizierter Realisierungsbaustein.
- **Testnachweis** = geplante Testfamilie bzw. Entscheidungs-/Reviewnachweis; noch keine grüne Suite.

| Lastenheft-ID | Originalstatus / Zeitpunkt | Original-Anforderung (sinngemäß aus Tabelle) | PH-Teil | Geplanter Nachweis |
| --- | --- | --- | --- | --- |
| `LH-PROD-001` | V1-MUSS | Erste öffentliche Scientific-App ist ein **vollwertig nutzbarer klassischer RPN-Wissenschaftsrechner** für das iPhone, keine unfertige technische Demo. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-002` | V1-MUSS | Rechnen, Wiederherstellen des Zustands und notwendige Bedienhilfe funktionieren **vollständig offline**; keine dauerhafte Internetverbindung, kein Konto und kein Server. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-003` | V1-MUSS | **Keine Werbung und kein Abonnement**; keine Werbe-SDKs als Bestandteil des ersten Releases. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-004` | GEPLANT | Möglichst kostenlose Verfügbarkeit; endgültige Preisentscheidung nach wirtschaftlicher Prüfung. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-005` | V1-MUSS | Dezentes, barrierefrei anklickbares **SASD**-Kennzeichen **oben links** als Link zur offiziell bestätigten SASD-Webseite; kein sonstiger Werbebereich. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-006` | ARCH-MUSS | Historisch orientierte Bedienphilosophie bleibt erhalten; spätere moderne Funktionen verdrängen die klassische RPN-Bedienung nicht. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-007` | ARCH-MUSS | Produkte und App-Store-Angaben müssen ihren **tatsächlich verfügbaren** Funktionsumfang und ihre Grenzen ehrlich nennen. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-008` | ARCH-MUSS | Unabhängige SASD-Produktidentität; keine Darstellung als offizielles oder verbundenes historisches Herstellerprodukt. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PROD-009` | V1-MUSS | Die App soll als hochwertiger, responsiver und optisch ruhiger alltäglicher Rechner funktionieren; Benutzerfreundlichkeit und Fehlerfreiheit haben Vorrang vor historischer Gehäusenachbildung. | `2/17/23` | `PRODUCT/STORE` |
| `LH-PORT-001` | ARCH-MUSS | Scientific und Financial besitzen getrennte Repositories, Produktidentitäten, App-Store-Auftritte, Releasezyklen und Freigabekriterien. | `17/23` | `BUILD/RELEASE` |
| `LH-PORT-002` | ARCH-MUSS | Ein unvollständiges Financial-Feature darf Scientific nicht blockieren und umgekehrt. | `17/23` | `BUILD/RELEASE` |
| `LH-PORT-003` | ARCH-MUSS | Classic RPN, ALG und Advanced RPL dürfen keine zwingende Laufzeitabhängigkeit von einer anderen Scientific-App haben. | `17/23` | `BUILD/RELEASE` |
| `LH-PORT-004` | ARCH-MUSS | Gemeinsam nutzbare Mathematik ist erwünscht; die jeweilige Bedienung, Historik, Datenhaltung und Programmsemantik bleiben eigenständig. | `17/23` | `BUILD/RELEASE` |
| `LH-PORT-005` | ARCH-MUSS | Classic RPN erhält bei Ressourcen- und Releasekonflikten **Vorrang** gegenüber parallelen ALG-, RPL-, Financial-, Desktop- und Forschungsarbeiten. | `17/23` | `BUILD/RELEASE` |
| `LH-PORT-006` | GEPLANT | Eine ALG-App kann zeitlich parallel entwickelt werden, muss nicht bis zur historischen Gesamtkompatibilität warten und kann separat erscheinen. | `17/23` | `BUILD/RELEASE` |
| `LH-PORT-007` | OFFEN | Ob Classic RPN, ALG und Advanced RPL als drei separate App-Store-Listings oder teilweise gemeinsam vertrieben werden, wird bei der jeweiligen Veröffentlichung entschieden; technische Entkopplung ist trotzdem nötig. | `17/23` | `BUILD/RELEASE` |
| `LH-RPN-001` | V1-MUSS | Klassische RPN-Tastenfolgen mit `ENTER`, Zifferneingabe und binären Operationen funktionieren nach einem freigegebenen Zustandsmodell. | `5–6` | `RPN` |
| `LH-RPN-002` | V1-MUSS | Die für V1 freigegebenen Stackregister X/Y/Z/T werden angezeigt und in definierter Reihenfolge aktualisiert. | `5–6` | `RPN` |
| `LH-RPN-003` | V1-MUSS | Stack Lift, Drop, Duplizieren, Vertauschen, Rollen und andere freigegebene Stackfunktionen haben reproduzierbare Wirkung. | `5–6` | `RPN` |
| `LH-RPN-004` | V1-MUSS | `LAST X` und weitere für V1 freigegebene Speicher-/Stackkonventionen werden als Zustandsübergänge dokumentiert und geprüft. | `5–6` | `RPN` |
| `LH-RPN-005` | V1-MUSS | Addition, Subtraktion, Multiplikation und Division berücksichtigen die Operandensemantik und klar definierte Fehlerzustände. | `5–6` | `RPN` |
| `LH-RPN-006` | V1-MUSS | Speicherregister erlauben Ablegen, Abrufen und festgelegte Rechenoperationen mit Registerinhalten. | `5–6` | `RPN` |
| `LH-RPN-007` | V1-MUSS | Benutzer können Eingaben löschen bzw. korrigieren; Umfang und Wirkung von Clear, Undo und Fehlerrücksetzung werden vor der Freigabe festgelegt. | `5–6` | `RPN` |
| `LH-RPN-008` | V1-MUSS | Ein Fehler darf den bestehenden Rechnerzustand nicht unerwartet beschädigen; definierte zulässige historische Abweichungen werden für spätere Profile dokumentiert. | `5–6` | `RPN` |
| `LH-RPN-009` | ARCH-MUSS | Die RPN-Stackverwaltung ist fachlich von Tastendarstellung und Betriebssystem getrennt. | `5–6` | `RPN` |
| `LH-RPN-010` | ARCH-MUSS | Eine allgemeine technische Stack-Datenstruktur ersetzt nicht die historische 41er- oder 48er-Ausführungssemantik. | `5–6` | `RPN` |
| `LH-RPN-011` | GEPLANT | Historische ALPHA-/Tastenzuweisungen, Flags und programmierbezogene Befehle werden modell- und katalogbezogen später ergänzt. | `5–6` | `RPN` |
| `LH-ALG-001` | ARCH-MUSS | Genau ein gemeinsam nutzbarer, oberflächenunabhängiger moderner algebraischer Ausdrucksparser wird vorgesehen. | `9` | `ALG/CROSS` |
| `LH-ALG-002` | GEPLANT | Vollständige Ausdrücke, Klammern, Operatorprioritäten, korrekte Assoziativität, Potenzen, unäre Operatoren und Wurzeln werden verarbeitet. | `9` | `ALG/CROSS` |
| `LH-ALG-003` | GEPLANT | Konstanten, Variablen, Registerbezüge und Funktionsaufrufe mit validierten Argumenten sind vorgesehen. | `9` | `ALG/CROSS` |
| `LH-ALG-004` | GEPLANT | Der Parser unterstützt schrittweise Trigonometrie, Logarithmen, komplexe Werte, Vektoren, Matrizen, Statistik und benutzerdefinierte Funktionen, soweit der jeweilige Rechenkontext dies anbietet. | `9` | `ALG/CROSS` |
| `LH-ALG-005` | ARCH-MUSS | Lexikalische, syntaktische, Typ-, Bereichs-, Genauigkeits- und Auswertungsfehler sind voneinander unterscheidbar und nutzerverständlich erklärbar. | `9` | `ALG/CROSS` |
| `LH-ALG-006` | ARCH-MUSS | Parsing und mathematische Auswertung werden getrennt; die grafische Eingabekomponente enthält keine eigene Mathematikimplementierung. | `9` | `ALG/CROSS` |
| `LH-ALG-007` | ARCH-MUSS | Programmcode historischer Rechner wird nicht über den modernen ALG-Parser interpretiert oder übersetzt. | `9` | `ALG/CROSS` |
| `LH-ALG-008` | ARCH-MUSS | Das Ergebnis eines modernen Ausdrucks wird nur über einen kontrollierten, modellgerechten Zustandsübergang an historische Stack-/Registermodelle übergeben. | `9` | `ALG/CROSS` |
| `LH-ALG-009` | GEPLANT | Die ALG-App bietet eine gut editierbare vollständige Ausdruckseingabe mit `=` und sinnvollen Korrektur-/Verlaufsmöglichkeiten. | `9` | `ALG/CROSS` |
| `LH-ALG-010` | OFFEN | Lokale Dezimal-/Listentrennzeichen, `%`, implizite Multiplikation, symbolische Ausdrücke und Zuweisungssyntax werden bei ALG-Entwicklung definiert. | `9` | `ALG/CROSS` |
| `LH-ALG-011` | ARCH-MUSS | Ausdrücke dürfen durch übergroße Eingaben, Verschachtelung oder rekursive Auflösung keine unkontrollierten Ressourcen verbrauchen. | `9` | `ALG/CROSS` |
| `LH-MATH-001` | V1-MUSS | Grundrechenarten, übliche Potenzen/Wurzeln, Logarithmen, Exponential- und trigonometrische Funktionen sind im **vorher freigegebenen V1-Umfang** nutzbar. | `7` | `CORE/NUM` |
| `LH-MATH-002` | V1-MUSS | Winkelmodi und numerisches Ein-/Ausgabeformat werden für freigegebene Operationen nachvollziehbar behandelt. | `7` | `CORE/NUM` |
| `LH-MATH-003` | ARCH-MUSS | Fachlich gleiche mathematische Algorithmen sollen möglichst **einmal** entwickelt, geprüft und wiederverwendet werden. | `7` | `CORE/NUM` |
| `LH-MATH-004` | ARCH-MUSS | Unterschiede in Zahlentyp, historischer Genauigkeit, Rundung, Stack- und Fehlereffekt werden **nicht** durch eine falsche globale Universalregel verdeckt. | `7` | `CORE/NUM` |
| `LH-MATH-005` | ARCH-MUSS | Zahlenwert, historische interne Repräsentation, Anzeigeformat und Eingabeformat bleiben logisch unterscheidbar. | `7` | `CORE/NUM` |
| `LH-MATH-006` | GEPLANT | Komplexe Zahlen, Vektoren, reelle/komplexe Matrizen und Matrixoperationen werden schrittweise ergänzt. | `7` | `CORE/NUM` |
| `LH-MATH-007` | GEPLANT | Numerische Solver, Polynom-/Nullstellenverfahren, Integration und Differentialgleichungslösungen werden schrittweise ergänzt. | `7` | `CORE/NUM` |
| `LH-MATH-008` | GEPLANT | Statistik, Regression, Zahlensysteme, Bitoperationen und Einheiten werden über geeignete gemeinsame Bibliotheken bereitgestellt. | `7` | `CORE/NUM` |
| `LH-MATH-009` | ARCH-MUSS | Funktionen werden mit Argumentzahl, Typen, Winkel-/Präzisionskontext, Verfügbarkeit, Diagnose und Hilfe verknüpfbar dokumentiert. | `7` | `CORE/NUM` |
| `LH-MATH-010` | OFFEN | Numerischer Basistyp (u. a. `double`, Dezimal-/Mehrpräzisionsarithmetik), Toleranzen und historische Konformitätsgrade werden vor der betreffenden Implementierung spezifiziert. | `7` | `CORE/NUM` |
| `LH-MATH-011` | ARCH-MUSS | Eine vorhandene C#/.NET-Lösung ist keine automatische C++/iOS-Laufzeitabhängigkeit; SASD Math Toolkit wird nur bei tatsächlich passender, versionierter Schnittstelle wiederverwendet. | `7` | `CORE/NUM` |
| `LH-41-001` | ARCH-MUSS | Der 41er-Kern ist von 48er-RPL und moderner ALG-Laufzeit funktional und in seinem historischen Zustand unabhängig. | `10` | `41-FOCAL` |
| `LH-41-002` | LANGFRISTIG-MUSS | Historisch relevante Bedien-, Register-, Stack-, ALPHA-, Flag- und Fehlereffekte werden im jeweils freigegebenen 41er-Kompatibilitätsprofil reproduziert. | `10` | `41-FOCAL` |
| `LH-41-003` | LANGFRISTIG-MUSS | Normale historische Tastenprogramme/FOCAL-Befehle werden anhand separater Modellreferenztests ausführbar. | `10` | `41-FOCAL` |
| `LH-41-004` | ARCH-MUSS | Historische Register können im späteren Kompatibilitätskern **verlustfrei 56 Bit / sieben Byte** abbilden; ein reines `double` genügt für beliebige Rohzustände nicht. | `10` | `41-FOCAL` |
| `LH-41-005` | ARCH-MUSS | Die spätere historische Programmspeicherung muss originale Bytefolgen erhalten können; eine lesbare disassemblierte Befehlsansicht darf nicht die einzige Wahrheit sein. | `10` | `41-FOCAL` |
| `LH-41-006` | LANGFRISTIG-MUSS | Historisch relevante Programmzeiger, Tastenzuweisungen, Verwaltungsregister und Speicheraufteilungen werden für unterstützte Programme modelliert. | `10` | `41-FOCAL` |
| `LH-41-007` | GEPLANT | Angemessene getrennte Modellprofile für HP-41C/CV, optional CX und Speicher-/Funktionsmodule. | `10` | `41-FOCAL` |
| `LH-41-008` | ARCH-MUSS | Normale und synthetische Befehle sollen bei späterer Umsetzung denselben konsistenten **virtuellen** historischen Rechnerzustand verwenden und keine konkurrierenden Gesamtinterpreter benötigen. | `10` | `41-FOCAL` |
| `LH-41S-001` | ARCH-MUSS | Synthetische Bytecodes und historische Zustandsänderungen sind im künftigen 41er-Programmmodell darstellbar. | `10` | `41-SYN-A/B` |
| `LH-41S-002` | LANGFRISTIG-MUSS | Historische Programmbytes unterstützter Austauschformate können verlustfrei geladen, gespeichert und auf Übereinstimmung geprüft werden. | `10` | `41-SYN-A/B` |
| `LH-41S-003` | LANGFRISTIG-MUSS | Unterstützte synthetische Befehle und Programme bestehen Byte-, Register-, Zeiger-, Tastenzuweisungs- und Fehler-Referenztests. | `10` | `41-SYN-A/B` |
| `LH-41S-004` | ARCH-MUSS | Synthetische Operationen greifen ausschließlich auf virtuell geprüfte Register/Speicherbereiche zu und können den Host nicht kompromittieren. | `10` | `41-SYN-A/B` |
| `LH-41S-005` | ARCH-MUSS | Moderne ALG-Eingabe und normaler RPN-Betrieb bleiben von synthetischen Programmbytes unabhängig. | `10` | `41-SYN-A/B` |
| `LH-41S-006` | OPTIONAL | Byte-Hüpfer Stufe C und vollständigere historische Firmware-Effekte werden nur nach separater Machbarkeits-/Kostenentscheidung realisiert. | `10` | `41-SYN-A/B` |
| `LH-48-001` | ARCH-MUSS | Eine unabhängige 48er-RPL-/Objektlaufzeit ist vorgesehen, nicht ein umbenannter Vier-Ebenen-Stack. | `11` | `48-USER` |
| `LH-48-002` | LANGFRISTIG-MUSS | Historische User-RPL-Programme werden im dokumentierten Funktions- und Modellumfang ausführbar. | `11` | `48-USER` |
| `LH-48-003` | LANGFRISTIG-MUSS | Für unterstützte Objekte werden Typ-, Objekt-, Stack-/Return-Stack- und Ausführungseffekte modellkonform verarbeitet. | `11` | `48-USER` |
| `LH-48-004` | ARCH-MUSS | Das spätere Objektmodell ermöglicht eine für unterstützte historische Fälle **verlustfreie Nibble-/Objekt-/Prolog-Repräsentation** neben modernen logischen Objekten. | `11` | `48-USER` |
| `LH-48-005` | ARCH-MUSS | Historische Saturn-Adressen und Speicherreferenzen werden als **virtuelle** Modelladressen verstanden, niemals als Hostpointer. | `11` | `48-USER` |
| `LH-48-006` | GEPLANT | Varianten der RAM-/ROM-Konfiguration und spätere ROM-Kompatibilitätsprofile werden versionierbar dokumentiert. | `11` | `48-USER` |
| `LH-48-007` | LANGFRISTIG-MUSS | Das Verhalten der jeweils freigegebenen User-RPL-Programme ist mit unabhängigen Objekttyp-/Zustands-/Fehler-Referenztests nachweisbar. | `11` | `48-USER` |
| `LH-48S-001` | ARCH-MUSS | System-RPL-Primitive, interne Objekte und systemnahe Ausführungszustände sind getrennt von normalen mathematischen Funktionen behandelbar. | `11` | `48-SYS` |
| `LH-48S-002` | LANGFRISTIG-MUSS | Ausgewählte dokumentierte System-RPL-Befehle und historische Programme werden mit definierten Seiteneffekten ausgeführt. | `11` | `48-SYS` |
| `LH-48S-003` | LANGFRISTIG-MUSS | `SYSEVAL` (historisch adressbezogen) und `LIBEVAL` (Bibliothekskennung/Aufruf) sind **im freigegebenen Umfang** über kontrollierte virtuelle Zuordnungen unterstützbar. | `11` | `48-SYS` |
| `LH-48S-004` | ARCH-MUSS | ROM-Profile, historische Systemadressen und Bibliothekskennungen werden getrennt von Hostfunktion/-adresse verwaltet. | `11` | `48-SYS` |
| `LH-48S-005` | LANGFRISTIG-MUSS | Unterstützte Systemobjekte, Daten-/Return-Stack-Zustände, Speicher- und Programmfehler bestehen reproduzierbare Modelltests. | `11` | `48-SYS` |
| `LH-48S-006` | ARCH-MUSS | Fehlerhafte System-RPL-Programme dürfen keine realen Hostspeicher-/Dateisystemzugriffe erzwingen. | `11` | `48-SYS` |
| `LH-48S-007` | LANGFRISTIG-MUSS | User-RPL-Regressionen müssen auch nach Ergänzung von System-RPL-Primitiven bestehen. | `11` | `48-SYS` |
| `LH-48S-008` | OFFEN | Welche historische ROM-Version und welche konkreten Systemprimitive zuerst unterstützt werden, wird vor M4 anhand Referenzprogrammen entschieden. | `11` | `48-SYS` |
| `LH-MOD-001` | ARCH-MUSS | Erweiterungen werden pro Rechnermodell, Version, Fähigkeiten, Zustandswirkung und Lizenz/Provenienz erfasst. | `12` | `MOD/EXT` |
| `LH-MOD-002` | GEPLANT | Time- und Statistics-Modulfunktionen werden mit eigenem historischen Befehlskontext und gemeinsamen mathematischen Diensten modelliert. | `12` | `MOD/EXT` |
| `LH-MOD-003` | OPTIONAL | Advantage-Pac-inspirierte Bedien- und Funktionsadapter können später angeboten werden. | `12` | `MOD/EXT` |
| `LH-MOD-004` | ARCH-MUSS | Vor Modulimplementation ist die Überschneidung mit bestehenden 48er-/Core-Funktionen zu prüfen; Doppelentwicklung nur begründet. | `12` | `MOD/EXT` |
| `LH-MOD-005` | ARCH-MUSS | Die Dokumentation trennt funktionale Ähnlichkeit, historische Befehlssemantik, Binär-/XROM-Kompatibilität und tatsächliche Modullaufzeit. | `12` | `MOD/EXT` |
| `LH-MOD-006` | V1-MUSS | Fehlende Module verhindern den ersten klassischen iPhone-Release nicht. | `12` | `MOD/EXT` |
| `LH-MOD-007` | GEPLANT | 48er-Bibliotheken, RAM-Karten, Systemfunktionen und Dateiformate werden nach Referenzprofil und rechtlichem Status separat freigegeben. | `12` | `MOD/EXT` |
| `LH-MEM-001` | ARCH-MUSS | Moderne Rechnerprofile dürfen nicht künstlich auf historisches Basis-RAM begrenzt werden. | `13` | `MEM` |
| `LH-MEM-002` | ARCH-MUSS | Historische Speicherprofile sind **pro Modell und Erweiterungszustand** definierbar, nicht als ein globales Byte-Limit. | `13` | `MEM` |
| `LH-MEM-003` | GEPLANT | Strict Historical kann historische Speicherpartitionen, Allokation, Freispeicherabfrage und Speicherfehler entsprechend einer Referenzkonfiguration nachbilden. | `13` | `MEM` |
| `LH-MEM-004` | GEPLANT | Historical Core + Modern Input trennt Komforteingabe vom historisch begrenzten Ergebnis-/Programmzustand. | `13` | `MEM` |
| `LH-MEM-005` | ARCH-MUSS | Virtueller Rechneradressraum, tatsächlicher Hostspeicher und angezeigte historische Speichernutzung bleiben unterscheidbar. | `13` | `MEM` |
| `LH-MEM-006` | ARCH-MUSS | Historische Speicherkonfiguration/ROM-Profil werden bei relevanten Snapshots/Tests zusammen mit dem Zustand identifizierbar. | `13` | `MEM` |
| `LH-MEM-007` | OPTIONAL | Didaktische Speicher-/Registerinspektoren und visualisierte historische Belegung werden später geprüft. | `13` | `MEM` |
| `LH-MEM-008` | GEPLANT | Unzulässige historische Zugriffe führen zu kontrolliertem virtuellen Fehlerverhalten, niemals zu Hostzugriffen. | `13` | `MEM` |
| `LH-UI-001` | V1-MUSS | iPhone-Hochformat nutzt die verfügbare Fläche für einen vollständigen, gut lesbaren und bedienbaren Rechner. | `15` | `IOS-UX` |
| `LH-UI-002` | V1-MUSS | V1-Tasten einschließlich freigegebener Zweit-/ALPHA-Funktionen sind tatsächlich zugänglich; kein Verlust durch Bildvorlagen. | `15` | `IOS-UX` |
| `LH-UI-003` | V1-MUSS | Schriftgrößen, Touchziele, Safe Areas, Erreichbarkeit und VoiceOver/Accessibility werden am iPhone XS überprüft. | `15` | `IOS-UX` |
| `LH-UI-004` | V1-MUSS | Verlässliche Anzeige von Stack-/Ergebnis-/Statuswerten, Winkel-/Moduszuständen und verständlichen Fehlern. | `15` | `IOS-UX` |
| `LH-UI-005` | V1-MUSS | Dezenter SASD-Link oben links, ohne störende Überlagerung von Display oder Tasten. | `15` | `IOS-UX` |
| `LH-UI-006` | ARCH-MUSS | Alle UI-Ereignisse delegieren Berechnung/State-Mutationen an testbare Kern- oder Anwendungsoperationen; keine eigene Mathematik in Button-Callbacks. | `15` | `IOS-UX` |
| `LH-UI-007` | GEPLANT | Desktopoberflächen erlauben vollständige Tastatureingabe algebraischer Ausdrücke und RPN-Steuerung. | `15` | `IOS-UX` |
| `LH-UI-008` | OPTIONAL | Editoren, Variablen-/Stackinspektoren, Debugger und Programm-/Bibliotheksansichten am Desktop. | `15` | `IOS-UX` |
| `LH-UI-009` | GEPLANT | iPad/macOS/Windows/Linux erhalten später angemessene native oder portable Frontends; Android ist ein langfristiger Kandidat. | `15` | `IOS-UX` |
| `LH-UI-010` | ARCH-MUSS | Illustrationen und eigentliche App-Screenshots werden klar unterschieden; die historische Tastaturinventur basiert auf überprüften Quellen, nicht auf generierten Bildern. | `15` | `IOS-UX` |
| `LH-UI-011` | OFFEN | Genaue Display-/Tastenbelegung, Abmessungen, Querformat, endgültige Farben/Skins und Apple-Mindestversion werden vor UI-Abnahme fixiert. | `15` | `IOS-UX` |
| `LH-DATA-001` | V1-MUSS | Rechnerzustand wird nach Suspendierung, Neustart und üblichen App-Lebenszyklusereignissen zuverlässig gespeichert/wiederhergestellt. | `14` | `STATE` |
| `LH-DATA-002` | V1-MUSS | Das Zustandsformat ist versioniert; beschädigte/inkompatible Daten werden kontrolliert erkannt und behandelt. | `14` | `STATE` |
| `LH-DATA-003` | ARCH-MUSS | Fehler beim Einlesen oder Rechnen verursachen keine unkontrollierte partielle Zustandsbeschädigung; gültige vorherige Zustände bleiben wiederherstellbar. | `14` | `STATE` |
| `LH-DATA-004` | ARCH-MUSS | Persistenzformat und Speicherung unterscheiden fachlichen Zustand von iOS-/Desktop-Pfaden, Dialogen und Dateisystemzugriff. | `14` | `STATE` |
| `LH-DATA-005` | LANGFRISTIG-MUSS | Für freigegebene historische Programme wird ein dokumentierter Import/Export angeboten, soweit unterstützte Dateiformate und rechtliche Grundlagen vorliegen. | `14` | `STATE` |
| `LH-DATA-006` | LANGFRISTIG-MUSS | In unterstützten Byte-/Nibble-Formaten versprochene Roundtrips erhalten historische Daten verlustfrei. | `14` | `STATE` |
| `LH-DATA-007` | GEPLANT | Programmverwaltung, Bibliotheken, Name/Version, Speicherzustände und Register-/Programmexport werden auf späteren Oberflächen zugänglich. | `14` | `STATE` |
| `LH-DATA-008` | ARCH-MUSS | Gespeicherte Zustände enthalten ausreichende Versions-/Modell-/Profilinformationen für reproduzierbare Tests und spätere Migration. | `14` | `STATE` |
| `LH-DATA-009` | OFFEN | Konkretes Datenschema, Autosave-Auslöser, atomare Schreibstrategie, Export-/Backupformate und Kollisionsregeln werden vor der jeweiligen Umsetzung spezifiziert. | `14` | `STATE` |
| `LH-HELP-001` | V1-MUSS | Verständlicher kurzer **offline verfügbarer** Einstieg in die klassische RPN-Bedienung und Erklärung der freigegebenen Fehler/Funktionen. | `16` | `HELP/EDU` |
| `LH-HELP-002` | GEPLANT | Kontextbezogene Tasten-/Funktionshilfe und vollständiges durchsuchbares DE/EN-Handbuch. | `16` | `HELP/EDU` |
| `LH-HELP-003` | GEPLANT | Vergleichende Lernbeispiele für ALG und RPN, Klammern/Prioritäten und relevante Stackaktionen. | `16` | `HELP/EDU` |
| `LH-HELP-004` | GEPLANT | Interaktive Übungen und Schritt-für-Schritt-Ansichten über echte Kernoperationen. | `16` | `HELP/EDU` |
| `LH-HELP-005` | OPTIONAL | Ausführliche historische Programmierkurse (FOCAL, Synthetic, User/System RPL), AST-/Debugger-/Speichervisualisierung. | `16` | `HELP/EDU` |
| `LH-HELP-006` | ARCH-MUSS | Hilfe und Tests beziehen sich auf dieselben tatsächlich unterstützten Funktions-/Kommandometadaten und weisen fehlende Funktionen aus. | `16` | `HELP/EDU` |
| `LH-ARCH-001` | ARCH-MUSS | Wissenschaftlicher Kern unabhängig von Benutzeroberflächen und Betriebssystemen; bevorzugte Basis **C++20** mit **CMake** und automatisierten Tests. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-002` | ARCH-MUSS | Separate fachliche Ausführungsmodelle für Classic RPN/41, ALG und RPL/48; nur geeignetes gemeinsames Verhalten wiederverwenden. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-003` | ARCH-MUSS | Gemeinsame mathematische Algorithmen dürfen keine versteckten HP-41-/HP-48- oder GUI-Abhängigkeiten voraussetzen. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-004` | ARCH-MUSS | Beabsichtigte Erweiterungen dürfen bereits freigegebene Stack-, Programm- oder Fehlerspezifikationen nicht stillschweigend verändern. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-005` | ARCH-MUSS | Neue Funktionen verfügen über definierte Typ-, Fehler-, Zustands- und Testverträge; begründete historische Unterschiede bleiben zulässig. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-006` | ARCH-MUSS | Getrennte Scientific-App-Targets sind unabhängig baubar und releasbar, auch wenn sie sich Quellbibliotheken teilen. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-007` | ARCH-MUSS | Keine zwingende Laufzeitkopplung von Scientific und Financial, keine gemeinsam vorausgesetzte Internet-/Serverinstanz. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-008` | GEPLANT | Versionierte Bibliotheken/Pakete werden **erst bei echtem zweitem Verbraucher** gegenüber Kopie und Herkunftsnachweis geprüft; kein frühzeitiges unnötiges Framework. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-009` | ARCH-MUSS | Wird Code zwischen Projekten kopiert, werden Quelle, Commit/Version, Lizenz, Änderungen und Wartungsverantwortung dokumentiert. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-010` | GEPLANT | Native iOS-Oberfläche mit **SwiftUI** und wohldefinierter möglichst versionierter C-ABI-Brücke zu C++; konkrete Lifetime-/Fehlerregeln vor Implementierung festlegen. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-011` | ARCH-MUSS | Keine nativen C++-STL-Datentypen unkontrolliert über eine öffentliche C-/Swift-ABI-Grenze geben. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-012` | ARCH-MUSS | Historischer 41er-Bytecode, 48er-RPL und moderne ALG-ASTs bleiben unabhängige Programm-/Syntaxrepräsentationen. | `2–3/17` | `ARCH/BUILD` |
| `LH-ARCH-013` | ARCH-MUSS | Die Ablage im Monorepo und die spätere Weitergabe von Bibliotheken dürfen keine künstlichen wechselseitigen Abhängigkeiten erzeugen. | `2–3/17` | `ARCH/BUILD` |
| `LH-NF-001` | V1-MUSS | Für alle freigegebenen Funktionen existieren nachvollziehbare automatisierte positive, negative und Grenzfalltests. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-002` | V1-MUSS | Rechen-, Anzeige- und Speicherfehler dürfen zu keinem bekannten kritischen Absturz, Verlust gültiger Zustände oder unbemerktem Falschergebnis führen. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-003` | V1-MUSS | Wiederaufnahme nach Unterbrechung und Neuinstallation/Upgrade entsprechend freigegebener Datensicherungsregeln wird praktisch getestet. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-004` | V1-MUSS | Bedienbarkeit, Lesbarkeit, Touch, Zugänglichkeit und Offline-Betrieb werden auf echten unterstützten Geräten – besonders iPhone XS – überprüft. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-005` | ARCH-MUSS | Änderungen an gemeinsamer Mathematik oder öffentlichen Schnittstellen lösen Tests aller betroffenen Calculator-Engines aus. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-006` | ARCH-MUSS | Fehler und Diagnosen sind strukturiert; falsche Typen, Stackunterlauf, Division durch null, mathematische Definitionsfehler, Überläufe und Ressourcenprobleme bleiben unterscheidbar. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-007` | ARCH-MUSS | Importierte Programme, beschädigte Snapshots und historische Speicherzugriffe gelten als nicht vertrauenswürdige Eingabe und werden sicher begrenzt. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-008` | ARCH-MUSS | Keine Ausführung beliebiger Host-Shell-Kommandos, Hostpointer oder unkontrollierter nativer Plug-ins durch historische Programme. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-009` | ARCH-MUSS | Fachlogik ist unter Windows, Linux und macOS in einer CI-Build-/Testmatrix prüfbar; iOS-Freigabe verlangt zusätzliche Apple-Tests. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-010` | ARCH-MUSS | Numerische Genauigkeit, Anzeige-/Eingabetransformation, Rundungsregeln und Vergleichstoleranzen sind kontext- und versionierbar dokumentiert. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-011` | ARCH-MUSS | Keine abgeleiteten Kompatibilitätsversprechen ohne Modell-/ROM-Profil, Referenzfall und konkrete Testergebnisse. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-012` | ARCH-MUSS | Nutzerdaten werden lokal verarbeitet; keine erforderliche Registrierung, Cloud-Synchronisation oder Telemetrie für die erste App. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-013` | ARCH-MUSS | Bei App-Store- und Lizenz-/Datenschutzerklärungen muss tatsächliches Verhalten dem angegebenen entsprechen. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-014` | GEPLANT | Systematischer Regressionstest für Zustandsformate, ältere Programme, zusätzliche Module und zukünftige App-Varianten. | `18–20` | `SEC/CI/NUM` |
| `LH-NF-015` | ARCH-MUSS | Tests sind soweit möglich deterministisch, reproduzierbar und automatisiert; Referenzdaten und Herkunft werden dokumentiert. | `18–20` | `SEC/CI/NUM` |
| `LH-LEGAL-001` | ARCH-MUSS | Unabhängige, eigenständig geschriebene SASD-Implementierung; keine ungeprüfte Übernahme von HP-ROMs, Firmware, historischen Betriebssystemabbildern oder Quellcode. | `18/23` | `LEGAL/STORE` |
| `LH-LEGAL-002` | ARCH-MUSS | Geschützte historische Handbücher, kommerzielle Programmsammlungen, Bilder und Originalressourcen werden nicht ohne Nutzungsrechte mitgeliefert. | `18/23` | `LEGAL/STORE` |
| `LH-LEGAL-003` | ARCH-MUSS | Historische Modellbezeichnungen dienen in technischen Kompatibilitätsdokumenten der sachlichen Identifikation; App-Branding verwendet SASD ohne irreführende Herstellerzuordnung. | `18/23` | `LEGAL/STORE` |
| `LH-LEGAL-004` | ARCH-MUSS | Für Referenzprogramme und Testdaten werden Quelle, Lizenz/Nutzungsrecht, Modell/Version, Beobachtung und Datum erfasst. | `18/23` | `LEGAL/STORE` |
| `LH-LEGAL-005` | ARCH-MUSS | Im Repository vorhandene **MIT-Lizenz** und Urheberhinweise werden nicht stillschweigend geändert; Fremdbibliotheken werden vor Aufnahme separat geprüft. | `18/23` | `LEGAL/STORE` |
| `LH-LEGAL-006` | V1-MUSS | Die App-Store-Veröffentlichung besitzt rechtsgeprüfte App-Grafik, Screenshots eines **echten laufenden Builds**, korrekte Datenschutzangaben und erforderliche Rechte. | `18/23` | `LEGAL/STORE` |
| `LH-LEGAL-007` | OFFEN | Umfang konkreter historischer Kompatibilitätsaussagen und Marken-/Designrechtsprüfung vor Veröffentlichung festlegen. | `18/23` | `LEGAL/STORE` |
| `LH-COMP-001` | ARCH-MUSS | K1–K4 werden in der Dokumentation konsequent von M0–M5 getrennt. | `10–13/23` | `COMP/K1-K4` |
| `LH-COMP-002` | ARCH-MUSS | Jede veröffentlichte Kompatibilitätsangabe verweist auf modell- und versionsbezogene Nachweise. | `10–13/23` | `COMP/K1-K4` |
| `LH-COMP-003` | LANGFRISTIG-MUSS | FOCAL und User RPL erhalten eigenständige K2-Testkataloge. | `10–13/23` | `COMP/K1-K4` |
| `LH-COMP-004` | LANGFRISTIG-MUSS | Synthetische 41er-Programme Stufe B und ausgewähltes System RPL erhalten eigenständige K3-Testkataloge. | `10–13/23` | `COMP/K1-K4` |
| `LH-COMP-005` | OPTIONAL | CPU-/Firmware-/OS-Nachbildung und Maschinenprogrammtests werden erst bei ausdrücklicher M5-Entscheidung verpflichtend. | `10–13/23` | `COMP/K1-K4` |
| `LH-REL-001` | V1-MUSS | Die verbindlich freigegebene V1-Tasten-/Funktionsmatrix ist vollständig implementiert und für jede Funktion getestet. | `21/25` | `AC-V1/STORE` |
| `LH-REL-002` | V1-MUSS | Stack-, Register-, Eingabe-, Zahlentyp-/Rundungs- und Fehlerverhalten bestehen dokumentierte Referenztests. | `21/25` | `AC-V1/STORE` |
| `LH-REL-003` | V1-MUSS | Wiederherstellung nach Suspend/Neustart/Upgrade und Behandlung beschädigter Daten sind praktisch geprüft. | `21/25` | `AC-V1/STORE` |
| `LH-REL-004` | V1-MUSS | Reale unterstützte iPhones, insbesondere das XS-Ziel, haben Touch-/Lesbarkeits-/Accessibility-/Offline-/Stabilitätstests bestanden. | `21/25` | `AC-V1/STORE` |
| `LH-REL-005` | V1-MUSS | Alle relevanten C++- und iOS-Tests, Release-/Lizenz-/Datenschutz-/App-Store-Prüfungen sind mit Commit, Version und Testergebnis dokumentiert. | `21/25` | `AC-V1/STORE` |
| `LH-REL-006` | V1-MUSS | Keine bekannten schwerwiegenden Rechen-, Absturz-, Sicherheits- oder Datenverlustfehler verbleiben. | `21/25` | `AC-V1/STORE` |
| `LH-REL-007` | V1-MUSS | SASD-Kennzeichnung, Bildrechte und echte Store-Screenshots sind geprüft. | `21/25` | `AC-V1/STORE` |
| `LH-REL-008` | V1-MUSS | Release Notes geben **tatsächliche** Funktions-/Kompatibilitätsabdeckung und bekannte Grenzen an. | `21/25` | `AC-V1/STORE` |
| `LH-REL-009` | ARCH-MUSS | Kein späterer historischer Funktionswunsch wird ohne neue ausdrückliche Entscheidung zum M2-Releaseblocker. | `21/25` | `AC-V1/STORE` |
| `LH-TEST-001` | ARCH-MUSS | Jede neu freigegebene fachliche Operation wird durch reproduzierbare Kern-/Zustands-/Fehlertests abgesichert. | `19/26` | `TEST/CI` |
| `LH-TEST-002` | ARCH-MUSS | Historische Tests nennen rechtlich zulässige Referenz, Modellprofil und erwartete **Zustandsänderung**, nicht bloß Ergebniszahl. | `19/26` | `TEST/CI` |
| `LH-TEST-003` | ARCH-MUSS | Anpassungen an gemeinsamen Bibliotheken prüfen die betroffenen RPN-, ALG- und RPL-Konsumenten. | `19/26` | `TEST/CI` |
| `LH-TEST-004` | ARCH-MUSS | CI auf Linux, Windows und macOS ist nötig, beweist jedoch weder iPhone-Gerätequalität noch App-Store-Freigabe. | `19/26` | `TEST/CI` |
| `LH-TEST-005` | GEPLANT | Erweiterte automatisierte Parser-Grenzwert-, Speicher-/Snapshot-, Import-/Export- und historische Programmregressionen. | `19/26` | `TEST/CI` |
| `LH-TEST-006` | OPTIONAL | K4-Maschinenausführungstests erst bei freigegebener M5-Forschung. | `19/26` | `TEST/CI` |
| `LH-PROC-001` | ARCH-MUSS | Aufgaben mit eindeutiger Modulzuständigkeit, Abhängigkeiten und überprüfbaren Abnahmekriterien dokumentieren. | `3/23` | `REVIEW/CI` |
| `LH-PROC-002` | ARCH-MUSS | Neue Funktionen mit Tests und angemessener Entwickler-/Benutzerdokumentation liefern. | `3/23` | `REVIEW/CI` |
| `LH-PROC-003` | ARCH-MUSS | Änderungen am Funktionsumfang in README, Lasten-/Folgespezifikationen, Roadmap und Release-Matrix nachvollziehen. | `3/23` | `REVIEW/CI` |
| `LH-PROC-004` | ARCH-MUSS | CI-Fehler aus eigenen Änderungen beheben und nur tatsächlich beobachtete erfolgreiche Prüfungen melden. | `3/23` | `REVIEW/CI` |
| `LH-PROC-005` | ARCH-MUSS | Keine unkoordinierten Änderungen an gemeinsam genutzten APIs durch parallele Codex-Aufträge. | `3/23` | `REVIEW/CI` |
| `LH-PROC-006` | ARCH-MUSS | Keine unautorisierte Lizenz-/Marken-/ROM-Verwendung oder Neudefinition freigegebener historischer Semantik. | `3/23` | `REVIEW/CI` |
| `LH-OD-001` | Vor M1 | Exakte V1-Haupt-/Shift-/ALPHA-Tasten-, Display- und Kommandoliste, unabhängig vom Konzeptbild | `24` | `ADR/DECISION` |
| `LH-OD-002` | Vor M1 | Vier-Ebenen-Stackregeln: `ENTER`, Lift, Drop, Roll, LAST X, Eingabepuffer, Clear, Undo, Fehlerrücksetzung | `24` | `ADR/DECISION` |
| `LH-OD-003` | Vor M1 | Zahlentyp, Genauigkeit, Rundung, Winkeleinheiten, Über-/Unterlauf und Referenztoleranzen | `24` | `ADR/DECISION` |
| `LH-OD-004` | Vor M1/M2 | Zustandsschema, atomare Sicherung, Migration, beschädigte Dateien und Backup-/Exportverhalten | `24` | `ADR/DECISION` |
| `LH-OD-005` | Vor M2 | Unterstützte iOS-Minimalversion, Xcode-Toolchain, reale iPhone-XS-Tests, Bundle-ID und App-Signierung | `24` | `ADR/DECISION` |
| `LH-OD-006` | Vor M2 | Offizielle SASD-Webadresse für Logo-Link, App-Store-Branding und Bild-/Lizenzprüfung | `24` | `ADR/DECISION` |
| `LH-OD-007` | Vor M2 | Konkreter Offline-Hilfe-Mindestumfang, Preismodell innerhalb der Vorgabe „ohne Werbung/Abo“ | `24` | `ADR/DECISION` |
| `LH-OD-008` | Vor ALG-Implementierung | Endgültige Parser-Grammatik, Pratt/Recursive-Descent-ADR, Dezimal-/Argumenttrenner, implizite Operatoren und Seiteneffekte | `24` | `ADR/DECISION` |
| `LH-OD-009` | Vor eigenständigen ALG-/RPL-Releases | App-Namen, Bundle-IDs, Versionierungs-/Releasekonzept und mögliche kombinierte Modus-App | `24` | `ADR/DECISION` |
| `LH-OD-010` | Vor M3 | 41er-FOCAL-Kompatibilitätsumfang, Rohregister/Programmspeicherordnung und legale Referenzprogrammformate | `24` | `ADR/DECISION` |
| `LH-OD-011` | Vor M3 | 48er-User-RPL-Objekt-/Nibbleformat, Referenzprofil, Verzeichnisse, Persistenz- und Austauschformate | `24` | `ADR/DECISION` |
| `LH-OD-012` | Vor M4 | Synthetische 41er-Befehls-/Programmbeispiele für Stufe A/B; konkreter optionaler Byte-Hüpfer-C-Nutzen | `24` | `ADR/DECISION` |
| `LH-OD-013` | Vor M4 | Erstes 48er-ROM-Profil, konkrete System-RPL-Primitive, `SYSEVAL`/`LIBEVAL`-Abdeckung | `24` | `ADR/DECISION` |
| `LH-OD-014` | Vor historischer Speichersimulation | Strict-Historical-Detailumfang, 128-KiB-/Kartenkonfigurationen, Speicheranzeige, Fehlersemantik | `24` | `ADR/DECISION` |
| `LH-OD-015` | Vor Modulrealisierung | Time-/Statistics-/Advantage-Inventare, fachliche Überschneidungen, XROM- und Lizenzumfang | `24` | `ADR/DECISION` |
| `LH-OD-016` | Bei zweitem Bibliotheksnutzer | Gemeinsam versioniertes Paket versus dokumentierte Quellcodekopie; C++-Schnittstelle und Lizenz | `24` | `ADR/DECISION` |
| `LH-OD-017` | Bei Financial-Start | Financial-Repository anlegen, TVM-/Finanzkonventionen und eigene Release-Gates spezifizieren | `24` | `ADR/DECISION` |
| `LH-OD-018` | Vor M5 | Nut-/Saturn-Maschinenemulation und Betriebssystemforschung wirtschaftlich/technisch gesondert freigeben | `24` | `ADR/DECISION` |
| `LH-OD-019` | Bei späterem UX-Ausbau | Freigabe von Desktopeditor, iPad-/Android-/Windows-/Linux-/macOS-Versionen und eigenständiger Trainings-App | `24` | `ADR/DECISION` |
| `LH-OD-020` | Bei historischen Funktionskatalogen | Vollständigkeit des HP-48GX-Katalogs, gesonderte Module, jeweilige Quellen- und Rechtslage unabhängig prüfen | `24` | `ADR/DECISION` |

### 30.1 Matrixprüfung und Abschlussregeln

**Vollständigkeitskriterium dieses Dokuments:** Die ID-Liste wurde aus dem aktuell im Repository vorhandenen Lastenheft abgeleitet; alle **200 eindeutigen** Datensätze sind genau einmal aufgeführt. Die 20 Datensätze `LH-OD-001` bis `LH-OD-020` bleiben **offene Entscheidungen**. Die Quell-ID-Reihenfolge und der Quellstatus werden nicht durch technische Vorschläge ersetzt.

**Achtung:** Für die technische Abnahme reicht eine Kapitel-/Testfamilienzuordnung noch nicht aus. Sobald eine konkrete Arbeit beginnt, wird für jede betreffende Zeile zusätzlich ein **realer Test-ID/Dateipfad**, ein **Commit/Run**, eine **Implementierungsstatuskennung**, ein **App-/Profilbezug** und ggf. ein **historischer Quellenbeleg** eingetragen (in einem separaten maschinenlesbaren Nachweis, Testkatalog oder Release-Matrix). Wer hierzu lediglich „geplant“ schreibt, hat die Anforderung **noch nicht erfüllt**.

### 30.2 Definition der technischen Übergabe

Die **M0-Übergabe** besteht aus Dokumenten/ADRs, die V1-Schnittstellen festlegen. Die **M1-Übergabe** besteht aus implementierter, testbarer Classic-RPN-Domänenlogik. Die **M2-Übergabe** besteht aus der tatsächlich installierbaren, auf dem iPhone XS validierten werbefreien/offline Classic-App samt Hilfe, Persistenz und Nachweisunterlagen. Alle über M2 hinausgehenden historischen/App-/Financial-Ziele werden in gesonderte Umsetzungspakete mit eigenen Freigaben überführt.

**Leitsatz:** Eine fachlich belegte, technisch saubere und zuverlässig nutzbare erste Scientific-App hat Vorrang vor einer historisch vollständigen, aber noch nicht alltagstauglichen Gesamtemulation.
