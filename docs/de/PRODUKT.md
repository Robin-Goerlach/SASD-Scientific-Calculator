# Produktanforderungen (Deutsch) — Stand 21.11.2026

## Ziel

Zuerst entsteht ein **wirklich nutzbarer klassischer wissenschaftlicher UPN/RPN-Rechner auf dem iPhone**, einschließlich iPhone-XS-Zielgerät. Der Rechner soll **offline, werbefrei, ohne Abo und möglichst kostenlos** sein. Die erste App-Store-Version wartet **nicht** auf vollständige Nachbildung historischer Rechner.

## Verbindlich

- **Scientific** und **Financial** bleiben eigene Produkte, Repositories und Releasezyklen. Financial blockiert Scientific nicht.
- **Strategie C, Priorität A:** wiederverwendbare Architektur langfristig; zuerst ein gut getesteter klassischer Rechner.
- Im iPhone-Hochformat ist ausschließlich der **Rechner** sichtbar: Display, Tasten, Funktions- und Shift-/Alpha-Ebenen; keine Desktop-Seitenleisten.
- Eine dezente **anklickbare SASD-Kennzeichnung links oben**; kein fremdes Herstellerlogo.
- Aktueller Gerätespeicher wird genutzt. Historische Speichergrenzen werden später höchstens für gezielte Kompatibilitätsprofile verwendet.
- Version 1.0 benötigt einen belastbaren Stack, Register, gebräuchliche wissenschaftliche Funktionen, vorhersehbare Fehlermeldungen, verlässliche Zustandswiederherstellung, gute Tastenbedienung und nachgewiesene Tests auf Zielgeräten.

## Bewusst später

- **M3:** historische Anwenderprogramme mit getrennten Familien-Semantiken (Series 41 / 48).
- **M4:** systemnahe Programme und interne Funktionen.
- **M5:** optionale CPU-/OS-Forschung.
- Desktop-IDE, große Lernplattform, Android, iPad-Erweiterungen und Finanzmodule sind **keine** V1-Blocker.

## Technischer Ansatz

Portabler **C++20-Rechenkern** mit CMake/CTest; für iOS ist **SwiftUI** mit schmaler C-Schnittstelle vorgeschlagen. Plattform-/UI-Code wird vom Kern getrennt. Ein gemeinsames Math Toolkit darf nur über passende, stabile und tatsächlich verfügbare Schnittstellen integriert werden.

## Noch zu entscheiden

Exakte Tasten-/Funktionsliste für V1, numerisches Modell, Stack-/ENTER-Semantik, minimale iOS-Version auf dem iPhone XS, Persistenzformat, Barrierefreiheit und konkrete App-Store-Prüfbedingungen. Die generierten Konzeptbilder sind **kein** normativer Beleg.

Ausführlich: [englische Produktspezifikation](../en/PRODUCT.md), [Roadmap](../../ROADMAP.md), [Tests](../en/TESTING.md).
