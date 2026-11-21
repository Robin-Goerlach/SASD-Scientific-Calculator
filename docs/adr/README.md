# V1-Architekturentscheidungen (ADR-Register)

**Stand:** 21.11.2026  
**Status:** Die folgenden ADRs wurden als **ausführliche, aber noch nicht akzeptierte Entwürfe** erstellt. Es ist **kein** numerischer Typ, keine Tastaturposition und keine historische Stacksemantik automatisch zur unumstößlichen Projektentscheidung geworden.

## 1. Dokumente und Fälligkeiten

| ADR | Gegenstand | Nächster Schritt | Verbindliche Ausgangsanforderung |
| --- | --- | --- | --- |
| [ADR-V1-INPUT](ADR-V1-INPUT.md) | Vier-Ebenen-Stack, ENTER, Lift, LAST X, Register, Entry und Key-Events | Testgoldens und historische Abweichungen freigeben | `LH-OD-001/002` |
| [ADR-V1-NUM](ADR-V1-NUM.md) | NumericPolicy, binary64-Kandidat, Anzeige, Grad/Rad, Domain, Rundung | Zahlentyp und Toleranzen freigeben | `LH-OD-003` |
| [ADR-V1-STATE](ADR-V1-STATE.md) | Snapshot, Format, Recovery, Migration und lokales Offline-Speichern | Codec/atomare Speicherung und Geräte-Tests festlegen | `LH-OD-004` |
| [ADR-V1-API](ADR-V1-API.md) | C++20/C ABI/SwiftUI Ownership/Threading und iPhone-XS-Deployment | realen iOS-Toolchain-/Bridge-Spike durchführen und ABI finalisieren | `LH-OD-005/006/007` |

**Weitere notwendige V1-Spezifikationen** (bewusst nicht als ein vorgeblich angenommener ADR dargestellt):

- [V1-Funktions-/Tastaturmatrix](../de/V1-FUNKTIONS-UND-TASTATURMATRIX.md) – P0-Kandidaten und noch freizugebende physische/Shift-Tastenbelegung.
- [V1-Test- und Freigabeplan](../de/V1-TEST-UND-FREIGABEPLAN.md) – mindestens `AC-V1-001…017`, Kern-/State-/ABI-/XS- und Store-Gates, derzeit alle nicht als PASS nachgewiesen.

## 2. Verbindlichkeit und Priorität

**Bereits verbindlich:** Klassischer UPN/RPN-iPhone-Rechner zuerst, Offline, werbefrei und ohne Abonnement, eigenständiger Scientific-/Financial-Auftritt, keine historische Komplettemulation als V1-Blocker. Modulgrenzen müssen spätere getrennte 41er-FOCAL/Synthetic- und 48er-RPL-/System-RPL-Laufzeiten zulassen.

**Noch offener technischer Beschluss:** binär64 als Basis-Backend, nummerische Stellen/Toleranz, Tastenposition, jede spezielle Stack-Transition, vollständiges Snapshot-Format, genauer C-ABI-Header, Apple Deployment Target und XS-Geräteergebnis.

**Bewusst später:** ALG-Grammatik-ADR, FOCAL-/56-Bit-Byteordnung, RPL-Prolog/Nibble-Codierung, System-RPL-ROM-Primitive, Strict Historical und Nut-/Saturn-Forschung.

## 3. ADR-Akzeptanzverfahren

1. Problem, Lastenheft-ID, Alternative, Empfehlung und tatsächliche Auswirkung lesen.
2. Für die konkret zu implementierende Komponente erforderliche offenen Werte/Tabellen festlegen.
3. Eigene Referenzfälle/Tests/Spike-Ergebnisse ergänzen und mit numerischem/Modellprofil versionieren.
4. Entscheidung mit Datum, verantwortlicher Freigabe, Gründen, Revisions-/Migrationskonsequenzen und Test-Links im [Entscheidungsregister](../en/DECISIONS.md) festhalten.
5. Erst danach `Status: ACCEPTED` im betreffenden ADR setzen und das Implementierungspaket freigeben.
6. Bei späterem Konflikt eine neue datierte `Superseded-by`-Entscheidung dokumentieren; keine rückwirkende unmarkierte Änderung historischer Beschlüsse.

**Entwicklungsschwerpunkt:** Ein kleines, getestetes Classic-C++20-Core-/iPhone-Prototypinkrement ist wertvoller als ein ungetesteter generischer Historik-Framework-Aufbau.

## 4. Quellen und Hierarchie

[Lastenheft](../LASTENHEFT.md) → [Pflichtenheft](../PFLICHTENHEFT.md) → [Gesamtarchitektur](../ARCHITEKTUR.md) → diese ADR-Entwürfe und [V1-Matrix](../de/V1-FUNKTIONS-UND-TASTATURMATRIX.md) → [ROADMAP](../../ROADMAP.md) und [TASKS](../../TASKS.md) → durch Tests tatsächlich nachgewiesene Produktversion.

Die historischen vollständigen [HP-41C](../de/HP-41C-FUNKTIONSKATALOG.md)- und [HP-48GX](../de/HP-48GX-FUNKTIONSKATALOG.md)-Funktionskataloge sind Forschungs-/Anforderungsreferenzen, **keine** Liste freigeschalteter V1-Commands.
