# Architektur — SASD Scientific Calculator

> **Maßgebliches ausführliches Architekturdokument:** [SASD Scientific Calculator – Gesamtarchitektur](../ARCHITEKTUR.md). Diese Datei ist eine knappe frühere Einstiegsskizze; für Module, Datenflüsse, Tests, ADRs und den M0–M5-Plan gelten das zentrale Architekturdokument und die [Roadmap](../../ROADMAP.md). Beide ergänzen das [Pflichtenheft](../PFLICHTENHEFT.md), ohne offene Detailentscheidungen als erledigt auszugeben.

**Priorität:** zuerst der klassische UPN-/RPN-Rechenkern, dann die iPhone-App, **erst danach** historische Anwenderprogramme und systemnahe Emulation. C++20/CMake bildet den portablen Kern; die UI bleibt ein austauschbarer Adapter.

Die derzeit tatsächlich vorhandene Klasse `sasd::scientific::RpnEngine` ist **nur ein generischer erster Stack mit Grundrechenarten**. Sie simuliert keine vollständige historische Rechnerfamilie und besitzt noch keine persistente Zustandsablage. `apps/cli` ist ein Entwicklerwerkzeug.

## Grenzen
- **Kern:** Rechenregeln, Stack/Register (Register noch geplant), Modi (geplant), Fehlermodelle, Kommandos (später).
- **Plattformadapter:** iOS-Dateien, App-Lebenszyklus, native Eingaben, UI-Integration und sichere Wiederherstellung.
- **iPhone-UI:** Anzeige und Tastenbedienung, keine eigene Rechenlogik.
- **Desktop-UI:** optionaler Programmeditor, Stack-/Variablenfenster und Bibliotheken; kein Zwang für iOS.
- **Historische Modelle:** getrennte 41er- und 48er-Semantiken mit eigenen Interpreter-/Objekt-/Registermodellen ab M3.
- **Mathematik:** geeignete stabile C++-Bibliotheken wiederverwenden; keine Pflichtabhängigkeit von .NET auf dem iPhone.

Geplant ist eine **versionierte C-ABI** zwischen C++ und SwiftUI. Noch keine solche Schnittstelle implementiert; Toolchain und iPhone-XS-Unterstützung müssen getestet werden. Keine permanente Webserverpflicht, keine erzwungene Cloudanmeldung, keine pauschalen historischen RAM-Grenzen.

Die umfassenden Verantwortlichkeiten, textuelle Komponentenskizze, offenen Schnittstellenentscheidungen und künftige Ordnerstruktur stehen in [ARCHITECTURE.md](../en/ARCHITECTURE.md).
