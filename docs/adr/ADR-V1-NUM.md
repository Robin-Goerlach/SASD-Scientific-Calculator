# ADR-V1-NUM – Zahlentypen, Genauigkeit, Anzeigen und numerische Fehler

**ADR-ID:** ADR-V1-NUM  
**Datum:** 2026-11-21  
**Status:** **PROPOSED / NICHT FREIGEGEBEN**  
**Fällig:** vor dem Ausbau des wissenschaftlichen Classic-RPN-Kerns (M1)  
**Anforderungen:** `LH-MATH-001…011`, `LH-NF-001/006/010`, `LH-OD-003`, `WP-02/04`  
**Quellen:** [Lastenheft](../LASTENHEFT.md), [Pflichtenheft](../PFLICHTENHEFT.md), [Gesamtarchitektur](../ARCHITEKTUR.md), [V1-Funktionen](../de/V1-FUNKTIONS-UND-TASTATURMATRIX.md), [Input-ADR](ADR-V1-INPUT.md)

> **Entscheidung ist noch offen:** Die im Prototyp eingesetzten `double`-Werte sind kein historisch exakter HP-41C-Zahlentyp. Dieses Dokument empfiehlt einen **bewusst austauschbaren V1-NumericPolicy-Ansatz** und eine prüfbare Kandidatenkonfiguration; es beschließt weder eine bitidentische BCD-/Saturn-Emulation noch eine vom Benutzer nicht genehmigte numerische Präzision.

## 1. Problem und zwingende Eigenschaften

Der Calculator muss Grundoperationen, Wurzeln, Potenzen, Logarithmen, trigonometrische Funktionen, Register und Stackverhalten **zuverlässig** ausführen. Der Zahlentyp beeinflusst Eingabe, Rundung, Overflow, gespeicherte Register, Ergebnisse, Testtoleranzen und späteren Programmaustausch.

**Vier unterschiedliche Ebenen werden nicht verschmolzen:**

1. **Kanonischer Eingabetext** (Mantisse/Exponent, Dezimalpunkt, Vorzeichen; noch vor Konversion).
2. **Numerischer Rechenwert** (`NumericValue`, intern mit ausdrücklich deklarierter Policy).
3. **Anzeigeformat** (z. B. FIX/SCI/ENG, Stellenzahl, Locale, Exponentenform).
4. **Historische Rohrepräsentation** (41er sieben Byte, 48er RPL-Objekt/Nibbles), **erst in späteren Modulen**.

Ein Rechenwert als intern gerundeter Anzeige-String ist unzulässig. Eine moderne Zahl wird später **kontrolliert** in historische Register/Objekte konvertiert; bei Wertverlust oder nicht darstellbarer Zahl muss eine dokumentierte Entscheidung/Diagnose erfolgen.

## 2. Alternativen und Entwurfsentscheidung

| Variante | Vorteile | Risiken | Verwendung |
| --- | --- | --- | --- |
| A: IEEE-754 **binary64** (`double`) | C++20 verfügbar, performant, auf allen Zielplattformen praktikabel | nicht dezimal-/HP-41-BCD-exakt; Binärartefakte; Plattform-/Libm-Unterschiede | **empfohlener kleiner V1-Backend-Kandidat** |
| B: Dezimale Fest-/Fließkommaarithmetik | dezimale Reproduzierbarkeit und gezielte Rundung | weitere Bibliothek/Code, Operationen wie `sin`/`ln` komplexer; nicht automatisch historisch kompatibel | späterer oder alternativer NumericPolicy-Backend |
| C: Arbitrary Precision / MPFR-ähnlicher Backend | hohe Genauigkeit | Port-/Lizenz-/Performance-/Paketaufwand, iOS-Testbedarf | nach realem wissenschaftlichem Anwendungsfall |
| D: direkt 41er-BCD-/48er-RPL-Zahlentypen überall | historische Daten näher am Original | falsche Kopplung aller Apps, komplex, V1 verzögert | **nur in eigenständigen historischen Ausführungskontexten** |

**Empfehlung, noch nicht akzeptiert:** V1 arbeitet zunächst mit `binary64` für die freigegebene reelle Wissenschaftsmathematik, aber jede Session enthält eine explizite `NumericPolicyId`. Der Math-Core ist **nicht** auf die Annahme „alle künftigen Werte sind immer double“ zu fixieren. Kein großer generischer Value-Framework-Bau vor dem ersten iPhone.

## 3. Vorgeschlagener V1-NumericPolicy-Vertrag

| Feld | Kandidatenfestlegung | Abnahmekriterium |
| --- | --- | --- |
| `value_representation` | `REAL_BINARY64_V1` | identischer Backend-Identifier in Snapshot und Testlauf |
| `binary_precision` | IEEE-754 binary64, sofern `std::numeric_limits<double>::is_iec559` und Plattformprobe passen | Build-/Runtime-Prüfung der Zielplattform |
| `accepted_inputs` | endliche Dezimalzahlen, optional Exponent `E±nn`; keine textuellen `NaN`/`Inf`-Nutzereingaben | Parser gegen ungültige Zeichen/Exponentgrenzen |
| `internal_specials` | keine nichtendlichen Resultate im *freigegebenen* V1-RPN-Registerzustand | `std::isfinite` vor Commit prüfen |
| `display_default` | **Vorschlag:** 10 signifikante Stellen in Normalansicht, unabhängig vom internen `double` | Display-Roundtrip und Referenzanzeige |
| `display_modes` | FIX n und SCI n als P0-Kandidaten, ENG n P1 | Anzeige ändert den gespeicherten `double`-Wert nicht |
| `rounding` | **Vorschlag:** konsistente, getestete Formatierung zur nächstliegenden darstellbaren Dezimalanzeige | 0.5-Tie-/Grenzfälle dokumentieren |
| `angle` | DEG und RAD zwingende Kandidaten, GRAD P1 | sin/cos/tan/asin/acos/atan entsprechend Kontext |
| `zero_sign` | **Vorschlag:** `−0` als numerischer Wert erhalten, standardmäßig als `0` darstellen; bei Sonderfällen klar definieren | ±0, `1/x` und Anzeige getrennt prüfen |
| `underflow` | kontrollierte Policy, **nicht** still auf positive 0 „normalisieren“ | Subnormal/0-Grenzen und Ergebnisstatus |
| `overflow` | Fehlercode und keine ungültige State-Mutation | `max_double * 2` |
| `domain` | reelle Domains, keine automatische komplexe Erweiterung ohne Capability | `sqrt(-1)`, `ln(0)`, `asin(2)` |
| `strict_history` | **keine** implizite 41er-/48er-Bitgenauigkeitszusage | späterer unabhängiger HistoricalNumericAdapter |

**Was noch ausdrücklich zu entscheiden ist:** Anzahl der Display-Stellen, Runden am Halbwert, maximaler Eingabe-Exponent, Subnormal-/Underflow-Regeln, zulässige numerische Präzisionsklasse, `tan` nahe Polstellen, Zweigkonventionen für negative Basen und `−0`.

## 4. Numerische API und fachliche Trennung

```text
ClassicSession/X,Y/Z,T + NumericPolicy
    → validated operands + MathFunctionId
    → ScientificMath::evaluate(operands, NumericContext)
       • arity/type/domain
       • calculate (no calculator-state mutation)
       • finite/range/policy checks
    → MathResult(value | TypedNumericError)
    → Classic model-specific stack/LAST-X/entry transition
    → committed state and display projection
```

**Gewollte Eigenschaften:**

- Reine mathematische Funktion kennt weder `LAST X` noch Displayformat/Shift/Store.
- Registrierung einer mathematischen `SIN`-Funktion impliziert **nicht**, dass der historische HP-41C-Opcode oder RPL-Primitive schon freigegeben ist.
- Fehlermeldungen sind **typenstabil** und getrennt von DE/EN-Texten.
- Typkonvertierung und Interoperabilität mit `std::complex`, Vektor-/Matrixbibliotheken oder Dezimalbackend sind explizite, versionierte Adapter.
- Keine C++-Exception, nativer `long double`-ABI-Typ oder `std::string` ungeprüft über die späteren Swift/C-ABI-Grenzen exportieren.
- Bessere historische Rundungs- oder Zahlentypimplementierungen werden an Modelladapter angeschlossen statt globale Mathematik umzudefinieren.

## 5. Domain-Regeln für die V1-Wissenschaftsfunktionen

| Funktion | Reeller V1-Domain-Vorschlag | Besonderheit |
| --- | --- | --- |
| `+ − × ÷` | endliche Operanden, endliches Resultat; Division `X=0` Fehler | Operandenfolge **Y op X** vom Classic-Model |
| `sqrt(X)` | `X ≥ 0` | `sqrt(-0)` und Output-Format definieren |
| `1/X` | `X ≠ 0` | signed zero, Overflow und Subnormals testen |
| `x²` | endlicher Wert und darstellbares Ergebnis | kein ungeprüfter Infinity-Commit |
| `Y^X` | reell definierter Bereich: negative Basis nur zulässiger ganzzahliger Exponent, `0^0` nach ADR | `std::pow`-Randfälle nicht blind übernehmen |
| `ln(X)`, `log10(X)` | `X > 0` | `ln(1) = 0` |
| `exp(X)`, `10^X` | endlicher Input, Policy für Über-/Unterlauf | nicht still nach Infinity akzeptieren |
| `sin`, `cos`, `tan` | endliche X-Werte, Winkelkontext | Polstellen und Genauigkeit bei großen Argumenten |
| `asin`, `acos` | `X ∈ [-1,1]` | Ergebnis in aktivem Winkelmaß |
| `atan` | reelle X | Ergebnis in aktivem Winkelmaß |
| `π` | interne Policy-Konstante, dokumentierte Dezimalanzeige | nicht aus UI-String als Zahl importieren |

**Nicht in V1 automatisch:** komplexe Werte, Matrix-/Einheitenrechnung, CAS, Solver, historische HP-41C-`SIGN`-Spezialsemantik, ALG-Auswertung oder finanzmathematische `%`-Regel.

## 6. Winkelmodi und Formatregeln

### 6.1 DEG versus RAD

- *Empfohlene Policy:* DEG-Koordinaten werden vor `sin/cos/tan` mit `π/180` in Radian umgerechnet, inverse Funktionen vor Anzeige/Stackcommit analog nach Grad konvertiert.
- **Nicht** durch Runden von Eingabewerten am Display konvertieren.
- Gegenfälle: `sin_DEG(30) ≈ 0,5`, `cos_DEG(60) ≈ 0,5`, `sin_RAD(π/6) ≈ 0,5`, `asin_DEG(0,5) ≈ 30`, `asin_RAD(0,5) ≈ π/6`.
- Für großes |X| ist die trigon. Argumentreduktion und Fehlergrenze (auch durch libm) zu prüfen. Historische Rundungs-/Pol-Konventionen sind **kein** automatisch erfülltes V1-Ziel.

### 6.2 FIX/SCI/ENG

- `FIX n`: n Nachkommastellen in der Anzeige; **interner Wert bleibt identisch**.
- `SCI n`: n Nachkommastellen oder signifikante Stellen **vor Freigabe festlegen**. Das ist eine wichtige Mehrdeutigkeit, nicht zu verbergen.
- `ENG n`: Exponent Vielfaches von 3; als P1-Kandidat.
- Zwischen Anzeigemodi wird **nicht numerisch neu ausgewertet**.
- Locale-Komma/Dezimalpunkt: intern ein kanonisches Speicher-/Eingabeformat, Darstellung kann lokalisiert sein; Ambiguität mit ALG-Argumentlisten erst in ALG-ADR.

## 7. Golden-Referenzen und Toleranzen

### 7.1 Exakte Beispiele

| Test-ID | Eingaben | Erwartung / Prüfmethode |
| --- | --- | --- |
| NUM-EXACT-001 | 10−4 | intern exakt als binary64 darstellbar: 6 |
| NUM-EXACT-002 | 10÷4 | intern exakt: 2,5 |
| NUM-EXACT-003 | 2^3 | intern exakt: 8 |
| NUM-EXACT-004 | sqrt(81) | 9, sofern gültiges Domain |
| NUM-EXACT-005 | ln(1) | ideal 0; wegen libm ggf. gegen freigegebene Toleranz |
| NUM-ERR-001 | 1÷0 | `DIV_ZERO`, keine teilweise State-Änderung |
| NUM-ERR-002 | sqrt(-1) | `DOMAIN`, keine automatische komplexe Zahl |
| NUM-ERR-003 | ln(0) | `DOMAIN` |
| NUM-ERR-004 | asin(2) | `DOMAIN` |
| NUM-ERR-005 | max(binary64) × 2 | `OVERFLOW` ohne Infinity im Register |
| NUM-DISP-001 | Wert 1/3, dann FIX/SCI umschalten | gespeicherter Wert bleibt bitgleich |
| NUM-ANGLE-001 | sin(30) DEG | nahe 0,5 (Toleranz nach ADR) |
| NUM-ANGLE-002 | sin(π/6) RAD | nahe 0,5 (Toleranz nach ADR) |
| NUM-ANGLE-003 | atan(1) DEG/RAD | nahe 45 bzw. π/4 |
| NUM-SER-001 | endlicher binary64-Wert → Snapshot-Text → Wert | bitgenauer Roundtrip, einschließlich ±0 falls Policy |
| NUM-ROUND-001 | Werte genau an Anzeigegrenzen | feste, dokumentierte Tie-/Rundungsregel |

**Warnung:** `1/3` ist binär nicht exakt. Eine „12-stellig exakt“-Behauptung kann ohne freigegebenes Zahlensystem und korrekte Toleranz nicht Bestandteil der Abnahme sein.

### 7.2 Vergleichsstrategie

- Exakte arithmetische Werte, wenn im gewählten Backend exakt darstellbar, dürfen exakt verglichen werden.
- Transzendente Funktionen: **vor Freigabe definierte** Kombination aus absoluten und relativen Toleranzen, ggf. ULP-Schwellen bei geeigneter Referenz. `0`-Nähe getrennt behandeln.
- Testvektoren für mindestens zwei unterschiedliche Compiler/Libm-Implementierungen prüfen, aber **keine** unbewiesene bitgleiche transzendente Ausgabe verlangen.
- Langlauf-/Stress-/Random-Property-Tests sollten generierte Fälle und dokumentierten Seed speichern.

## 8. Persistenz- und ABI-Konsequenzen

- Der gespeicherte **NumericPolicyId** gehört in den Snapshot. „Modern binary64“ wird nicht in „HP-41C-kompatibles BCD“ umbenannt.
- **Vorschlag für binär64-Roundtrip:** numerische Strings mit `std::numeric_limits<double>::max_digits10` bzw. äquivalenter garantierter Darstellung; alternativ dokumentierte bitgenaue Kodierung. Der tatsächliche Parser/Formatierer muss per Roundtrip getestet werden.
- Die Bridge überträgt **keinen frei übersetzten Anzeige-String als einziges mathematisches Ergebnis**; Wert-/Zahlrepräsentation und anzuzeigender Text sind getrennt.
- Bei späterer Umstellung auf Dezimal-/Mehrpräzisionsarithmetik müssen alte Snapshots migriert oder als eigener numerischer Typ lesbar bleiben; keine stillschweigende Neuberechnung alter Registerwerte.
- Historische rohe 56-Bit-Register und RPL-Nibbleobjekte erhalten **eigene Codecs**; ihre verlustfreie Repräsentation wird durch den modernen binary64-V1-Vorschlag **nicht** ersetzt.

## 9. Entscheidungen zur Freigabe

- [ ] **Backend:** binary64 als V1-Policy akzeptiert oder begründete alternative Wahl?
- [ ] **Präzision:** verbindliche Stellen-/Rundungs-/Domain-/Underflow- und `−0`-Regeln?
- [ ] **Display:** FIX/SCI-Stellen, Vorzeichen/Exponent, Locale?
- [ ] **Winkel:** DEG/RAD, ggf. GRAD; Konvertierungs-/Toleranzprofil?
- [ ] **Sonderfälle:** `0^0`, negative Basis, `tan`-Polstellen, Overflow, Subnormal?
- [ ] **Persistenz:** bitgenauer Roundtrip und Policy-ID für Updates?
- [ ] **Testbelege:** Grenzvektoren unter Linux/Windows/macOS und später Apple-SDK/iPhone?
- [ ] **Freigabe:** datierter Beschluss im [Entscheidungsregister](../en/DECISIONS.md), erst dann Status **ACCEPTED**.

**Leitregel:** V1 muss im **zugesagten modernen Classic-Umfang korrekt** rechnen, ohne dass die gesamte historische 41er-/48er-Zahlendarstellung schon fertig ist.
