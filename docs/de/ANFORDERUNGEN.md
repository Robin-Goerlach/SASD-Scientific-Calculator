# SASD Scientific Calculator – konsolidierte Anforderungen

**Stand:** 21.11.2026. **Planungsstand, keine Funktionszusage für die vorhandene Software.** Der aktuelle C++20-Kern beherrscht bislang nur einfache generische RPN-Grundoperationen. Eine native iPhone-App gibt es noch nicht.

**Gesamtarchitektur und Meilensteinplanung:** [Architekturdokument](../ARCHITEKTUR.md) und [kanonische Roadmap M0–M5](../../ROADMAP.md).

**Technische Ausarbeitung zum Lastenheft:** [Pflichtenheft – SASD Scientific Calculator](../PFLICHTENHEFT.md). Der aktuelle Codebestand ist nur ein kleiner RPN-Prototyp; die Umsetzungsvorschläge sind ausdrücklich keine Behauptung über bereits fertiggestellte Apps oder historische Kompatibilität.

## Verbindliches erstes Produktziel

Zuerst entsteht ein **hochwertiger klassischer wissenschaftlicher UPN/RPN-Rechner auf dem iPhone**, möglichst auch für das iPhone XS. Er arbeitet offline, ist werbefrei, benötigt kein Abo und soll nach Möglichkeit kostenlos sein. Im Hochformat zeigt er ausschließlich Rechner und vollständige, geprüfte Tastatur; links oben sitzt eine dezente anklickbare SASD-Kennzeichnung.

**M0** Architektur/Tests → **M1** zuverlässiger klassischer Rechenkern → **M2** ausgereifte iPhone-App/App-Store-V1.0. Keine vollständige historische Programmemulation als Releaseblocker. Die konkrete Funktions- und Tastenliste, Vier-Ebenen-Stack-/ENTER-Regeln, Zahlenformat, persistenter Zustand und iOS-Mindestversion müssen vor Implementierung verbindlich spezifiziert werden.

## Drei wissenschaftliche Anwendungsvarianten – ein Monorepo

| App | Zweck | Release-Priorität |
| --- | --- | --- |
| Klassischer UPN/RPN-Rechner | Historisch orientierte Bedienung, 41er-Kern später ausbaubar | **Erstes Ziel** |
| Algebraischer Wissenschaftsrechner | Eigenständige ALG-App mit `=`, Klammern, Operatorpriorität | Architektonisch verbindlich; eigene spätere Veröffentlichung |
| Erweiterter RPL-Rechner | Eigenständiger 48GX-orientierter Objekt-/Programmkern | Eigener langfristiger Entwicklungspfad |

Die eigenständige ALG-App **ersetzt nicht** die zuvor vorgesehene Möglichkeit, algebraische Eingabe später zusätzlich zu historischen Rechnerprofilen anzubieten. Ein gemeinsamer Parser, getrennte Eingabe- und Programmausführung. Bei Konflikten um Entwicklungsressourcen erhält der klassische iPhone-Rechner Vorrang.

## Historische Kompatibilität, nicht mit Meilensteinen verwechseln

| Stufe | Ziel | Planung |
| --- | --- | --- |
| K1 | Historische Tasten-/Stack-/Register-/Zahlensemantik im belegten Umfang | M1/M2-Ausschnitt |
| K2 | FOCAL- und User-RPL-Anwenderprogramme | M3 |
| K3 | Synthetische 41er-Programmierung und System RPL | M4, langfristig vereinbarte Teilziele |
| K4 | Nut-/Saturn-Maschinencode und Hardware | M5, **optional** |

`SASD-CALC-COMPAT-041-SYN`: 56-Bit-Register und Byteprogramm-Vertrag früh vorsehen; synthetische Programme **Stufe B langfristig verbindlich**, Byte-Hüpfer **C optional**. `SASD-CALC-COMPAT-048-SYSRPL`: User RPL zuerst; definierter referenzgeprüfter System-RPL-Umfang langfristig verbindlich. `SASD-CALC-COMPAT-048-SATURN`: optional.

Historische 128-KiB-Grundausstattung des 48GX bedeutet **keine künstliche RAM-Beschränkung** für moderne Geräte. Historische Speicher- und ROM-/Kartenszenarien bleiben opt-in und müssen ihre Grenzen überprüfbar abbilden.

## Gemeinsam statt doppelt

Mathematische Algorithmen, Parser, numerische Hilfen, Statistik, Matrizen, Tests und Diagnose möglichst gemeinsam nutzen. Unterschiede bei RPN-Stack, RPL-Objekten, Rundung, Fehlern, Befehlen und Speicher bleiben in expliziten Modelladaptern. Wissenschaftliche und finanzmathematische Fachanwendungen nicht vermischen.

**SASD Financial Calculator** ist ein eigenständiges zukünftiges Produkt mit eigenem Repository, eigenem App-Store-Release und eigener Finanzdomäne (TVM, Cashflow, NPV/IRR usw.). Scientific zuerst, Financial parallel, wenn der Scientific-Fortschritt nicht leidet. Geeignete gemeinsame Komponenten bei tatsächlichem Bedarf versionieren; keine vorzeitige große Frameworkarchitektur.

## Erweiterungen und Lernen

Time Module, Statistics Pac, Advantage-Pac-inspirierte **funktionale** Ergänzungen, RAM-Karten und Bibliotheken später; keine ungeprüfte historische ROM-Nachbildung. UPN/ALG-Hilfe und erste Offline-Erklärungen früh, vollständiges interaktives Lernprogramm später. Inhalte und Tests dürfen nur als **implementiert** gelten, wenn tatsächlich eine funktionsfähige Umsetzung mit Nachweis existiert.

**Fachlich konsolidiertes Lastenheft:** [SASD Scientific Calculator – Lastenheft](../LASTENHEFT.md). Das Lastenheft beschreibt Anforderungen, Prioritäten, Abnahme und Abgrenzungen; die historischen vollständigen Befehlslisten liegen separat unter [HP-41C](HP-41C-FUNKTIONSKATALOG.md) und [HP 48GX](HP-48GX-FUNKTIONSKATALOG.md).

## Verbindliche Lesewege

- [Detaillierte Anforderungsmatrix (EN)](../en/REQUIREMENTS-MATRIX.md)
- [Produktgrenzen und M0–M5](../../ROADMAP.md)
- [V1-Freigabekriterien (EN)](../en/RELEASE-V1.md)
- [Architektur mehrerer Apps (EN)](../en/MULTI-APP-ARCHITECTURE.md)
- [Algebraische Eingabe (EN)](../en/ALGEBRAIC-INPUT.md)
- [Historisches 41er-Modell (EN)](../en/HISTORICAL-41.md)
- [Historisches 48er-Modell (EN)](../en/HISTORICAL-48.md)
- [Module (EN)](../en/MODULES.md)
- [Lernen und Hilfe (EN)](../en/LEARNING.md)
