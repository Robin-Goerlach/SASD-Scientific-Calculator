# ADR-V1-INPUT – klassische UPN-Eingabe, Stack und Tasten-Zustandsmaschine

**ADR-ID:** ADR-V1-INPUT  
**Datum:** 2026-11-21  
**Status:** **PROPOSED / NICHT FREIGEGEBEN**  
**Entscheidungsreife:** Umsetzungsvorschlag mit konkreter Übergangstabelle; vor Änderungen am Classic-RPN-State **fachlich freigeben**  
**Meilenstein:** M0-Gate für Classic-M1  
**Bezug:** `LH-RPN-001…011`, `LH-OD-001/002`, `WP-01/03` und [V1-Tastaturmatrix](../de/V1-FUNKTIONS-UND-TASTATURMATRIX.md)

## 1. Entscheidungskontext

Der vorhandene C++20-Prototyp `RpnEngine` verwaltet einen **dynamischen `std::vector<double>`-Stack** und einfache Push-/Dup-/Swap-/Drop-/Arithmetikfunktionen. Er ist **kein** historisch korrekter Vier-Ebenen-Rechner. Die erste Scientific-iPhone-App soll dagegen eine klassische RPN-Bedienung besitzen, in der die Sequenz `3 ENTER 4 ENTER 5 × +` das Ergebnis 23 liefert und alle Stack-, Eingabe- und `LAST X`-Nebenwirkungen vorhersagbar sind.

Die HP-41C-Handbücher beschreiben insbesondere den vierstufigen automatischen Stack und das separate LAST-X-Register. Als **historische Referenz**, nicht als kopierte Implementierung: https://archived.hpcalc.org/greendyk/hp41c-manual/39.html und https://literature.hpcalc.org/community/hp41-anwenderhandbuch.pdf. Die V1-App ist **historisch orientiert**, ohne vollständige HP-41C-K1-Kompatibilität zu behaupten.

**Offen bleibt**, welche historischen Sonderfälle zwingend zum V1-Scope gehören. Die nachstehenden Regeln sind ein **begründeter Vorschlag**, keine bereits beschlossenen historischen Tatsachen.

## 2. Erwogene Varianten

| Alternative | Nutzen | Gegenargument | Bewertung |
| --- | --- | --- | --- |
| A. Bestehender dynamischer Prototyp mit 4er-Größenlimit | kleinster Codeänderungsaufwand | `ENTER`/Lift/LAST X/Replace-Entry/T-Replikation und Historik nicht als State spezifiziert | **nicht als V1-Classic-Modell wählen** |
| B. Eigene V1-Classic-Zustandsmaschine mit expliziten X/Y/Z/T | klare Bedien- und Testsemantik, überschaubare iPhone-V1-Umsetzung | braucht neue Tests und Migrationspfad | **empfohlen** |
| C. Vollständige HP-41/Nut-CPU-Emulation vor V1 | potenziell hohe Historiktreue | enorme Kosten, ROM-/Rechtefragen, V1-Verzögerung | **nicht V1** |

**Empfehlung:** B. Die 41er-FOCAL-/Synthetic-Laufzeit nutzt später ein eigenes historisches Register-/Byte-Modell; konkrete 41er-Historikzustände werden nicht als `double`-Only-Vertrag in B festgeschrieben.

## 3. Architektur und Datenvertrag

```text
Touch / physical keyboard / CLI
   → KeyId + Modifier/Layer + optional payload
   → InputController (Shift / Help / Navigation)
   → CalculatorAction
   → ClassicSession.transition(action)
       → validate syntax, register, numeric domain
       → build candidate state + obtain math result
       → apply documented stack/lastX/entry/mode effects
       → commit one new generation OR error transition
   → immutable CalculatorViewState
```

**Vorgeschlagene logische Felder:**

- `stack = {X, Y, Z, T}` (immer **vier existierende numerische Register**, kein Vektor mit variabler Tiefe);
- `last_x` als separater Wert;
- `entry = {active, mantissa_sign, digits, decimal_seen, exponent_mode, exponent_sign, exponent_digits}`;
- `lift_state = {enabled, disabled_for_next_numeric_entry}`;
- `registers` als geprüfte, versionierte V1-Registerbank; **00–09 ist nur Vorschlag**;
- `angle_mode`, `display_mode`, `numeric_policy` und `diagnostic`;
- fachliche `state_generation`; Shift-/ALPHA-UI-Layer als separater, eindeutig gehaltener Controllerzustand oder bewusst mit serialisiert (ADR-V1-STATE).

Ein **vierstufiger, mit null initialisierter Stack ist nicht „unterfüllt“**, sobald eine Session existiert. Eine binäre Addition mit 0 in X/Y ist nicht allein deshalb „Stackunterlauf“, weil zuvor nur eine Zahl eingetippt wurde. Das bisherige `Error::stack_underflow` stammt aus der **anderen dynamischen Prototypsemantik**. Bei der V1-State-Engine wird das Verhalten durch den tatsächlichen numerischen Inhalt, Entry-Status und dokumentierte Operatorregel bestimmt, nicht durch `std::vector::size()`.

## 4. Kandidaten für die historische Vier-Ebenen-Transformation

Die folgende Tabelle verwendet die **Notation [T,Z,Y,X]**, nicht `[X,Y,Z,T]`. `E` steht für aktive Zahleneingabe, `L` für den Lift-Zustand.

| Aktion / Vorzustand | Vorschlag: Nachzustand [T,Z,Y,X] | LAST X | Entry/Lift | Prüfschwerpunkt |
| --- | --- | --- | --- | --- |
| Session-Erststart | `[0,0,0,0]` | `0` | `E=inactive, L=enabled` | Nullinitialisierung ist ein V1-Vorschlag |
| `ENTER` aus `[40,30,20,10]` | `[30,20,10,10]` | unverändert | `E=inactive, L=disabled` | Y erhält altes X; T erhält altes Z |
| Neue vollständige Zahl `7` **nach ENTER** | `[30,20,10,7]` | unverändert | `E=active, L=disabled` während Editieren | X wird überschrieben, Stack bleibt |
| Neue Zahl `7` bei **enabled Lift**, vorher `[40,30,20,10]` | `[30,20,10,7]` | unverändert | ein Lift zu Beginn der Zahl; `E=active` | keine weitere Lift bei jeder Folgeziffer |
| `+` aus `[40,30,20,10]` | `[40,40,30,30]` | `10` | `E=inactive, L=enabled` | Y+X=30; altes T wird repliziert |
| `−` aus `[40,30,20,10]` | `[40,40,30,10]` | `10` | `E=inactive, L=enabled` | Y−X=10; gleiche Drop-Wirkung |
| `×` aus `[40,30,20,10]` | `[40,40,30,200]` | `10` | `E=inactive, L=enabled` | Y×X=200 |
| `÷` aus `[40,30,20,10]` | `[40,40,30,2]` | `10` | `E=inactive, L=enabled` | Y÷X=2 |
| `X↔Y` aus `[40,30,20,10]` | `[40,30,10,20]` | vorläufig unverändert | **Lift/Entry-Effekt ADR gesondert** | T/Z bleiben |
| `R↓` aus `[40,30,20,10]` | `[10,40,30,20]` | vorläufig unverändert | **Lift/Entry-Effekt ADR gesondert** | X→T, Y→X, Z→Y, T→Z |
| `R↑` aus `[40,30,20,10]` | `[30,20,10,40]` | vorläufig unverändert | **Lift/Entry-Effekt ADR gesondert** | inverse Rotation; P1, falls V1 nicht freigegeben |
| `CLX` | X wird 0; T/Z/Y zunächst unverändert | **prüfen** | **historische Lift-Regel prüfen** | nicht mit vollständigem Reset vermischen |
| `BACKSPACE` während aktiver Zahl | Eingabepuffer verkürzt; eventuell X neu aus Text abgeleitet | unverändert | Entry bleibt aktiv, solange gültig | kein Y/Z/T-Verlust |
| `RESET` bestätigt | `[0,0,0,0]` | 0 | E inaktiv, L initial | Registerlöschung/Modi **separat entscheiden** |
| Ungültiger Operator | **kein Commit an Stack/Registern** | unverändert | Diagnose/Fehlerstatus gemäß Fehlervertrag | Test gegen korrupte Zustandsteile |

**Nicht aus dieser Tabelle als historisch beweisen:** Lift-Status nach allen unären Tasten, `LAST X`-Recall-Effekt, `STO/RCL`-Lift, `CLX`, ALPHA/USER-Modus und die Tastenbelegung. Diese Effekte werden in einem **separaten überprüften Semantik-Golden** freigegeben; bis dahin gelten die jeweiligen Zeilen nur als vorgeschlagene Teiltransformation.

## 5. Modus `Entry`: konkrete Kandidaten-Zustände

```text
Idle/Result
  ├─ digit/decimal → EditingMantissa  [first char triggers one stack lift iff L=enabled]
  ├─ EEX → EditingExponent           [if permitted by numeric grammar]
  ├─ ENTER → Result                  [stack copy; next entry replaces X]
  └─ operation → Result or Diagnostic

EditingMantissa
  ├─ digit/decimal/CHS → EditingMantissa
  ├─ EEX → EditingExponent
  ├─ DEL → EditingMantissa or Idle (documented)
  ├─ ENTER → Result
  └─ operation → Result or Diagnostic

EditingExponent
  ├─ digit/CHS → EditingExponent
  ├─ DEL → prior editing state or exponent edit
  ├─ operation → Result if numeric token valid; else Diagnostic
  └─ ENTER → Result if numeric token valid
```

- **Ziffernfolge ist Text**, nicht wiederholt gerundete Addition im Kern. `1.2345E−10` muss als **ein** gültiges Token verarbeitet werden können.
- `CHS` während Entry ändert das **richtige** Vorzeichenfeld (Mantisse oder Exponent). Nach Commit ist `CHS` eine numerische Operation mit gesondertem `LAST X`-/Lift-Vertrag.
- Das erste Zeichen einer neuen Zahl führt **höchstens einen** Lift aus. Nach `ENTER` ersetzt die neue Zahl X ohne zusätzlichen Lift.
- `DEL` ist von `CLX` getrennt. Fehlender exponentieller Ziffernteil darf nicht zu `0` oder `NaN` werden.
- Bei Fehler müssen InputController und Domain-State kontrolliert in einen wiederherstellbaren Zustand wechseln.
- **Zustandsereignisse werden serialisiert**; zwei gleichzeitige UI-Taps dürfen keine konkurrierenden Registeränderungen erzeugen.

## 6. LAST X, unäre Funktionen und Speicherregister – noch zu prüfende Sonderfälle

| Befehl | zu prüfende Domänenwirkung | Freigabe-Test |
| --- | --- | --- |
| `SQRT`, `SIN`, `LN`, `1/X` | wie wird altes X in LAST X gesichert? Lift nach Ergebnis? | definierte [T,Z,Y,X,LastX,L,E]-Goldens |
| `RECALL_LAST_X` | wie wird der alte LAST-X-Wert in X/Stack übertragen? | `LAST X` mehrfach / nach binärer Operation |
| `STO nn` / `RCL nn` | Liftstatus, X-Inhalt, Registeradresse, Fehler, Registerarithmetik | STO/RCL und `nn`-Grenzen |
| `CLX` / `DEL` | Wirkbereich, Liftstatus, Entry-Reset und LAST X | verwechselte Tasten, Fehlerreset |
| `R↓` / `X↔Y` | Stackwerte plus nachfolgende Zahleneingabe | komplette Folgeaktion, nicht isolierter Stack |
| `ENTER ENTER` | wiederholte Lift- und Replace-Entry-Status | mehrere ENTER hintereinander |
| `ANGLE/FORMAT` | keine versehentliche Änderung von Zahlen oder Stack | Moduswechsel mitten im Entry |
| `EEX` | leeres Exponentenfeld, Wechsel CHS/DEL, Dezimalpunkt im Exponenten abweisen | Eingabegrenzfälle |

**Historischer Umfang:** Grundlegende Stackbewegungen werden gegen die 41er-Handbücher geprüft; SASD-spezifische Korrekturtasten (z. B. `DEL` und ein geschützter `RESET`) können **bewusst modern** sein und müssen nicht „HP-41C-identisch“ genannt werden.

## 7. Fehler und Transaktionsmodell

Vorgeschlagen: bei Bereichs-/Syntax-/Divisions-/Overflowfehlern **keine partielle Stack-/Register-/LAST-X-Mutation**. Fehler darf eine strukturierte Diagnose und ggf. eine *separat dokumentierte* Entry-Fehleransicht auslösen. Historische Programme können **später** andere belegte Side Effects haben – deren Laufzeit benutzt **nicht** heimlich die moderne V1-Fehlerregel.

**Fehlerkatalog:** `INVALID_ENTRY`, `DIV_ZERO`, `DOMAIN`, `OVERFLOW`, `INVALID_REGISTER`, `UNSUPPORTED_COMMAND`, `PERSISTENCE_ERROR`. `STACK_UNDERFLOW` ist für den historischen Vier-Ebenen-Stack **nicht automatisch** korrekt: anders als der heutige dynamische Prototyp sind die vier Ebenen immer vorhanden.

## 8. Implementierungsschritte und Testbasis

1. **Fachfreeze:** Funktions-/Keymap-Matrix freigeben; Zustandsfelder und Semantik aller P0-Kommandos vervollständigen.
2. **Golden-Tabellen:** Für jeden P0-Command mindestens zwei Vorzustände (mit/ohne aktiven Entry), ein Fehlerfall wenn relevant, vollständiger Nachzustand (X/Y/Z/T, LAST X, L, E, Modus, Register).
3. **Neue Domänenklasse:** RPN-Session + reine Transitionen, ohne SwiftUI oder Controller-Lifecycle.
4. **Legacy behalten:** bestehende `RpnEngine`-Unit-Tests müssen weiter bestehen; Migration über einen definierten Wrapper oder eigenen neuen Target.
5. **Cross-UI:** CLI und iPhone führen dieselben Actions aus, gleiche Domainstate-Generation und Ergebnisse.
6. **Persistenz:** unterbrochene Editierung nach Neustart nach [ADR-V1-STATE](ADR-V1-STATE.md) wiederaufnehmen/abbrechen, niemals implizit umdeuten.
7. **K1-Aussage nur für geprüfte Kommandos**; der Vier-Ebenen-State allein beweist keine vollständige HP-41C-Kompatibilität.

### Abnahmematrix (noch nicht ausgeführt)

| Test-ID | Anfang [T,Z,Y,X] | Eingabe | Erwartetes Ende / Entscheidungsbedarf |
| --- | --- | --- | --- |
| RPN-STATE-001 | [40,30,20,10] | ENTER | [30,20,10,10], L=disabled |
| RPN-STATE-002 | nach RPN-STATE-001 | Zahl 7 | [30,20,10,7] |
| RPN-STATE-003 | [40,30,20,10] | + | [40,40,30,30], LASTX=10 |
| RPN-STATE-004 | [40,30,20,10] | − | [40,40,30,10], LASTX=10 |
| RPN-STATE-005 | [40,30,20,10] | R↓ | [10,40,30,20] (Lift-Effekt separat) |
| RPN-STATE-006 | [40,30,20,10] | X↔Y | [40,30,10,20] (Lift-Effekt separat) |
| RPN-STATE-007 | Standard-Nullstate | `3 ENTER 4 ENTER 5 × +` | X=23; weitere Ebenen erst nach genehmigtem Zustandsvertrag fest |
| RPN-STATE-008 | definierter Endzustand | Fehlerhafte Division | keine beschädigten Zahlen/Registers |
| RPN-STATE-009 | `[0,0,0,0]` | `1 ENTER 2` | **kein `stack_underflow` aus bloßer Vier-Ebenen-Invariante** |
| RPN-STATE-010 | 1.234567… im Entry | DEL, EEX, CHS | numerische/Anzeige-Token nach Numeric-ADR |

## 9. Konsequenzen für die Zukunft

Die saubere Domänentrennung lässt spätere **historische 56-Bit-Register** und **FOCAL/Synthetic-Programme** mit eigenem Speichermodell zu, statt Modern Classic zur angeblichen HP-41-VM zu erklären. Die 48GX-RPL-Welt benötigt einen **dynamischen Objektstack** und ist **kein Subtyp dieser Vier-Ebenen-Zustandsmaschine**. Ein moderner ALG-Parser ist ein **anderes Modul**, das erst über einen kontrollierten Ergebnisübergabeadapter in Classic oder historische Modelle eingreift.

## 10. Noch zu beschließende Punkte

- [ ] genaue RPN-Stacksemantik aller P0-Befehle inklusive LASTX/Lift nach Unary, CLX, RCL, R↓;
- [ ] Registerzahl, indirekte Adressen und Registerarithmetik;
- [ ] Input-/Fehlerkorrektur (Backspace vs. CLX, Alarm-/Anzeigezustand);
- [ ] NumericPolicy inkl. Parsing, Über-/Unterlauf, Runden und `CHS` bei Exponent;
- [ ] exakte UI-Keys, Shift-/ALPHA-Ebenen und Statusanzeige;
- [ ] golden fixtures aus zulässigen historischen Referenzaufzeichnungen;
- [ ] das Eintreten einer endgültigen **ACCEPTED**-Entscheidung wird mit Datum, begründeter gewählter Regel, Abweichungen und Tests im [Entscheidungsregister](../en/DECISIONS.md) dokumentiert.

**NICHT** als offen wieder aufrollen: Erstveröffentlichung Classic RPN iPhone, danach historische Programme; keine fremden ROM-Binaries, keine ALG-Ersetzung von FOCAL, Financial separat.
