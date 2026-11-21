# SASD Development Standard – Übernahme und Compliance-Prüfstand

**Dokument-ID:** SASD-SCI-COMPLIANCE-001  
**Datum:** 2026-11-21  
**Status:** **Pilot Alignment – Assessment in Progress**, nicht als „SASD-konform“ abgenommen  
**SASD-Bezugsfassung:** [SASD Development Standard, Commit `f12e2c038205892107440b4a58bfd41f21214036`](https://github.com/Robin-Goerlach/SASD-Development-Standard/tree/f12e2c038205892107440b4a58bfd41f21214036); normative Baseline: Approved 0.9.0, **Standard 1.0 weiterhin Spezifikationskandidat, nicht veröffentlicht**  
**Scientific-Basis vor dieser Übernahme:** `3f12d6899f05044fb2ba35b1389798d30a29aa6e`  
**Bewertungsverantwortung:** Scientific-Projektverantwortung – formelles Review/Freigabe steht noch aus  
**Nächster Review:** vor M1-Freigabe; erneut vor M2/App-Store-Release  
**Fachliche Quellen:** [Lastenheft](LASTENHEFT.md), [Pflichtenheft](PFLICHTENHEFT.md), [Architektur](ARCHITEKTUR.md), [Roadmap](../ROADMAP.md)

> Diese Dokumentation übernimmt **den Prozess- und Qualitätsrahmen projektbezogen**. Sie bescheinigt weder die vollständige Prüfung aller normativen Anforderungen noch ein bereits erfolgreiches iOS-/Geräte-/Release-Gate. Die neuen Anforderungen sollen eine gute erste Classic-RPN-iPhone-App **unterstützen**, nicht die historische CPU-/RPL-Emulation als V1-Voraussetzung einführen.

## 1. Normativer Status, Quelle und Konfliktregel

- **Referenzfassung festgehalten:** Der oben genannte Git-Commit ist die unveränderliche Bewertungsbasis. Bei neuer Standardfassung ist eine dokumentierte Impact-/Änderungsprüfung erforderlich. Die Standard-README benennt den Status **Version 1.0 Specification Candidate** mit genehmigter normativer Baseline, **nicht** ein endgültig veröffentlichtes 1.0.0-Release.
- **Normative Priorität:** Die [deutschsprachige normative Regelung](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/40-governance/NORMATIVE-LANGUAGE.md) und die [Inhaltsarchitektur](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/00-foundation/CONTENT-ARCHITECTURE.md) unterscheiden **MUSS**, **SOLLTE**, **KANN** und informative Hilfen. Quickstart, Vorlagen, Prompts und Tools schaffen keine zusätzlichen verbindlichen Pflichten.
- **Anwendung nach Kontext:** Qualitätsstufe, Profile, Bedingungen und Risiken bestimmen die einschlägigen Anforderungen. Ein nicht geprüfter Punkt heißt **Not Assessed**, eine vorhandene Lücke **Open**, ein nicht zutreffender Punkt benötigt eine **Begründung**, eine genehmigte Ausnahme ein dokumentiertes Verfahren.
- **Keine falsche Konformität:** Das [SASD-Compliance-Modell](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/40-governance/COMPLIANCE.md) erlaubt „Aligned“ erst mit der tatsächlichen Nachweisabdeckung. **Hier wurde keine vollständige normative Einzelanforderungsmatrix erstellt.**
- **Produktverbindlichkeit:** Die fachlichen Produktentscheidungen stehen weiterhin in [Lastenheft](LASTENHEFT.md) und [Pflichtenheft](PFLICHTENHEFT.md); Prozess- und Qualitätsregeln des Standards ergänzen sie. Strengere Rechte-/Apple-/Plattformbedingungen gelten daneben.
- **Keine Tool-Abhängigkeit:** Die Anwendung des Standards erfordert weder dessen Python-Werkzeuge als Laufzeitdependency noch einen Webserver, neue Frameworks oder Kopien der gesamten Standarddokumentation.

## 2. Vorläufige Projektklassifikation

Die folgende Empfehlung ist ein **Prüfstand, noch keine freigegebene Klassifikation**. Grundlage: [Projektklassifikation](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/30-processes/PROJECT-CLASSIFICATION.md) und [Qualitätsstufen](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/10-core-standard/QUALITY-LEVELS.md).

| Merkmal | Vorläufige Einschätzung und Grund |
| --- | --- |
| Produkt und Lebensdauer | langfristig gepflegter Scientific Calculator; Classic-RPN-iPhone-App als erstes selbstständiges Produkt |
| Projektgröße | **Medium vorgeschlagen**: mehrere geplante Engines/Plattformadapter und technische Daten-/Release-Grenzen; aktuelle C++-V1-Basis allein klein |
| Primäre Qualitätsstufe | **SASD Recommended vorgeschlagen**: öffentliches Repository, längerfristige Pflege, dokumentierte Architektur, risikobasierte Tests |
| Höhere Nachweistiefe | **Production-orientierte Maßnahmen vorgeschlagen** bei Rechenkorrektheit, Zustandssicherung, Sicherheits-/ABI-Grenzen und M2-Release. Abhängige Tests und Wartung müssen entsprechend mitbetrachtet werden |
| Profile | **Core** grundsätzlich. **.NET** nicht für den jetzigen C++20-/Swift-Projektcode; die separate SASD Math Toolkit .NET-Implementierung ändert das nicht. **Desktop** erst neu beurteilen, wenn eine tatsächliche Desktop-App entsteht |
| iOS/C++ | In der geprüften Normbasis **kein eigenes freigegebenes iOS- oder C++-Profil gefunden**; konkrete Swift-/C++-Build-, ABI-, App-Store- und Accessibility-Anforderungen bleiben projektspezifisch |
| Daten und Betrieb | lokale Rechner-/Programmzustände; offline, ohne Accounts, Ads oder Abo; kein öffentlich betriebener Server |
| Risiken | falsche Mathematikergebnisse, Datenverlust, untrusted gespeicherte Dateien und später FOCAL/RPL-/virtuelle Systembefehle: eigene Risiko-/Security-/Testbewertung |
| Rollen | Einzelentwickler darf Entwicklung und Selbstreview organisatorisch bündeln; Reviews, Testbelege und verantwortliche Freigaben müssen nachvollziehbar bleiben |

**Noch zu genehmigen:** Größe, primäre Qualitätsstufe, bereichsweise Hochstufung und tatsächlicher Schutzbedarf. Dass M2 im App Store öffentlich verteilt werden soll, bedeutet nicht automatisch, dass die offline arbeitende App als „öffentlich betriebener Dienst“ klassifiziert werden muss. Dies ist ausdrücklich zu prüfen.

## 3. Erster Lückenabgleich gegen die vorhandenen Scientific-Unterlagen

| SASD-Standard | Scientific-Ausgangspunkt | Status und nächste Maßnahme |
| --- | --- | --- |
| **SASD-CORE-001** Lifecycle | [ROADMAP](../ROADMAP.md) mit M0–M5 und eigenständigen ALG-/Historik-Tracks | **Artefakt vorhanden**; Gates/Reviewnachweise je Phase fortführen |
| **SASD-CORE-002** Requirements | Lastenheft mit 200 IDs, Pflichtenheft-Kapitel 30, [V1-Keymap](de/V1-FUNKTIONS-UND-TASTATURMATRIX.md) | **Artefakt vorhanden**; noch fehlende fachliche P0-Freigabe und reale Testabdeckung |
| **SASD-CORE-003** Architektur | [ARCHITEKTUR.md](ARCHITEKTUR.md) sowie [ADR-Index](adr/README.md) | **Entwurf vorhanden**; ADRs ausdrücklich PROPOSED, nicht ACCEPTED |
| **SASD-CORE-004** Dokumentation | README/Lastenheft/Pflichtenheft/Architektur mit Versionen/Status | **Artefakt vorhanden**; eindeutige Source of Truth beibehalten, keine Doppelpflege |
| **SASD-CORE-005** Repository | Git-`main`, [AGENTS.md](../AGENTS.md), [CONTRIBUTING.md](../CONTRIBUTING.md), [CI](../.github/workflows/core.yml) | **vorhanden**; Build-/Test-/Diff-Review und risikobasiertes Branching nachvollziehbar machen |
| **SASD-CORE-006** Qualitätsstufen | dieses Dokument | **Open:** Klassifikation/Recommended/Elevations ausdrücklich freigeben |
| **SASD-CORE-007** Qualität | Tests und geplante Feature-Gates | Definition of Done, statische Prüfschritte und Reviewbelege je Änderung |
| **SASD-CORE-008** Sicherheit | [SECURITY](../SECURITY.md), [Security/Rights](en/SECURITY-AND-RIGHTS.md), Snapshot-/API-ADRs | kontrollierte Eingaben, Byte-/ROM-Isolation, Dependency-/Lizenz-/Secret-Review |
| **SASD-CORE-009** Testing | [V1-Test-/Releaseplan](de/V1-TEST-UND-FREIGABEPLAN.md), CTest | **Testplan** ist keine Testausführung; Golden-/State-/ABI-/XS-Läufe belegen |
| **SASD-CORE-010** Releases | [Release-Checkliste](en/RELEASE-CHECKLIST.md), Roadmap | **noch keine iPhone-App/Store-Freigabe**; Tags, Commit, Build, Privacy, Screenshots, Gerätebeleg fehlen |
| **SASD-CORE-011** Wartung | CHANGELOG und Security-Kontakt | Update-/Recovery-/Bug-/Apple-SDK-Supportpfad vor M2 dokumentieren |
| **SASD-CORE-012** Wissenserhalt | ADRs, historische Kataloge, AGENTS | Entscheidungen, Testdatenherkunft und bekannte Grenzen dauerhaft bewahren |
| **SASD-CORE-013** KI-Entwicklung | Codex-/Agentenregeln in AGENTS | menschliche Verantwortung, minimaler Schreibscope, nachprüfbare Ergebnisse, keine eigenständige Releasefreigabe |

**Wichtig:** Die Tabelle bewertet die **Existenz und den fachlichen Nutzen** bestehender Artefakte, **nicht** jede einzelne MUSS-Anforderung dieser Standardkapitel als „Satisfied“.

## 4. Konkrete Regelübernahme für Codex und Entwicklung

Quelle: [SASD-CORE-013 KI-gestützte Entwicklung](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/10-core-standard/AI-ASSISTED-DEVELOPMENT.md), [SASD-CORE-005 Repository](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/10-core-standard/REPOSITORY.md), [Solo-Developer-Guide, informativ](https://github.com/Robin-Goerlach/SASD-Development-Standard/blob/f12e2c038205892107440b4a58bfd41f21214036/docs/10-core-standard/SOLO-DEVELOPER-GUIDE.md).

1. **Ein Arbeitspaket, eine prüfbare Änderung:** Scope, LH-/ADR-/Test-IDs, betroffene Module, Erfolgskriterium und Grenzen festhalten. Keine fremde historische Funktion aufgrund eines Handbuchnamens als implementiert deklarieren.
2. **Agentenrechte explizit:** Repository-Schreibaktionen, Seiteneffekte und Berechtigungen müssen passend zum Auftrag freigegeben und prüfbar sein. Codex darf Checks, Rechtekontrollen oder Release-Gates nicht eigenständig abschalten.
3. **Menschliches Review:** KI-Ergebnisse nach Risiko prüfen; keine selbständige Freigabe von Production-Releases, irreversiblen Migrationen oder sicherheitskritischen Änderungen.
4. **Tests im selben Änderungspaket:** CMake/CTest und für ABI/Swift/iPhone zusätzlich echte Integration/Device-Gates. Nicht ausgeführte Tests als nicht ausgeführt kennzeichnen.
5. **Kleine direkte `main`-Änderungen sind möglich:** für einen Einzelentwickler mit erfolgreichem Test/Review und nachvollziehbarem Commit; bei riskanten API-/State-/Security-/Persistenzänderungen bevorzugt Branch oder gleichwertige dokumentierte Selbstprüfung.
6. **Sicherheit:** keine Geheimnisse in Git; neue Abhängigkeiten auf Herkunft/Lizenz/Version/Vulnerabilities prüfen; fremde Programm-/Snapshotdaten validieren; 48er virtuelle Adressen niemals Hostpointer.
7. **Keine neue Release-Abhängigkeit:** vollständige FOCAL-, User-/System-RPL-, Synthetic-/Nut-/Saturn-Emulation, Financial und Desktop-IDE bleiben außerhalb der M2-Releasepflicht.

## 5. Stufenweise Einführung ohne Bürokratieprojekt

| Zeitpunkt | Maßnahme | Erforderlicher Beleg |
| --- | --- | --- |
| **M0 – jetzt** | Referenz-Commit pinnen, Klassifikation vorschlagen, Lücken sichtbar machen | **dieses Dokument, Pilotstatus** |
| **M0 – vor M1-Freigabe** | Qualitätsstufe/Risiko/Reviews entscheiden; V1-INPUT, -NUM-ADRs akzeptieren | datierte Klassifikation/ADRs |
| **M1** | Domainzustand, Zahlentyp, Tests und CMake-Targets nach DoD; Snapshot-ADR bei Persistenz | Run-ID/Commit/Golden-Tests |
| **M2 – Bridge** | C++-/Swift-/ABI-Smoke; iOS-Deployment/XS, Offline-/Accessibility/Recovery-Tests | reales Gerät, Build- und Testprotokoll |
| **M2 – Release** | unabhängige Freigabeentscheidung, Lizenz-/Privacy-/Store-Checks, reproduzierbarer Tag/Artefakt | Release-/Acceptance-Protokoll |
| **M3/M4** | neue Interpreter-/Byte-/ROM-/Import-Trust-Boundaries erneut bewerten | gesondertes Threat Model und Regression |
| **Standardupdate** | neue Bezugsfassung prüfen, Delta zu angewandten Anforderungen dokumentieren | datierte Versions-/Impactentscheidung |

Das Projekt benötigt **keine zusätzliche universelle Prozessplattform**. Vorhandene `TASKS.md`, ADRs, GitHub Issues und CI können die erforderlichen Nachweise aufnehmen.

## 6. Offene Maßnahmen (keine genehmigten Ausnahmen)

| ID | Offener Punkt | Vor welcher Arbeit? | Status |
| --- | --- | --- | --- |
| STD-001 | Klassifikation (Medium), Recommended und risikobasierte zusätzliche Prüfungen fachlich freigeben | M1-Fachfreeze | **Open** |
| STD-002 | normative Einzelanforderungen der gepinnten Fassung nach Qualität/Profil/Anwendbarkeit bewerten; nachvollziehbare Evidenz führen | laufend; Release-relevante Pflicht vor M2 | **Not Assessed / Assessment in Progress** |
| STD-003 | DoD, strukturierte Selbstprüfung und Agentenfreigaben bei riskanten Änderungen dokumentieren | vor entsprechender Änderung | **Open** |
| STD-004 | aktuelle Core-CI-/Test-/Abhängigkeitsnachweise erfassen; statische Qualitätschecks nach Risiko | je Paket | **Open** |
| STD-005 | Stack-, Numerik-, Persistenz- und API-ADRs akzeptieren; echte iPhone-XS-/SDK-Tests durchführen | M1/M2 | **Open** |
| STD-006 | Support-/Wartungs-/Update-/Recovery-/Privacy-/Store-Gate konkretisieren | vor M2 | **Open** |
| STD-007 | bei späteren fremden Programmen/Objekten zusätzliche Sicherheits- und Lizenzprüfung | vor M3/M4 | **Open** |

**Ausnahmen:** Keine genehmigte Ausnahme behauptet. **Not Applicable** bei .NET-/Desktop-Profildetails ist erst nach einer genauen Prüfung der jeweiligen Auslösebedingungen formell zu bestätigen.

## 7. Bewertungsstand

**Gesamtstatus: Pilot Alignment – Assessment in Progress.** Die Erstellung dieses Dokuments ist ein **erster Quell-/Artefaktabgleich**, keine vollständige Compliance-Prüfung. Konkrete `Satisfied`-Aussagen bedürfen Einzelanforderung, Evidenz, geprüftem Quellcommit und Datum; `Aligned` setzt eine vollständig abgeschlossene Bewertung voraus. Der Standard ist zum Referenzzeitpunkt ein **Version-1.0-Kandidat**, nicht ein bereits veröffentlichtes 1.0.0-Release.

| Bereich | Status |
| --- | --- |
| Anforderungs-/Lebenszyklus-Alignment | Assessment in Progress |
| Architektur-/Dokumentations-Alignment | Assessment in Progress |
| Qualitätsstufe und Prozessauswahl | Entscheidung offen |
| Testing/Security/Source-Review | Assessment in Progress |
| iOS-/App-Store-Release und Wartung | Noch nicht durchgeführt |
| AI-/Agenten-Review-Evidenz | bei tatsächlichen Entwicklungsaufträgen nachzuführen |

## 8. Verbindliche nächste Entscheidungen

Vor produktiver Classic-RPN-Entwicklung müssen **SASD Recommended als vorgeschlagene Primärstufe**, die vorgeschlagenen risikobezogenen Zusatzmaßnahmen und die anzuwendenden Profile durch die Projektverantwortung bestätigt oder begründet angepasst werden. Danach die bereits vorbereiteten [V1-ADRs](adr/README.md) freigeben und die [Roadmap](../ROADMAP.md) ohne einen zusätzlichen V1-Emulationsblocker abarbeiten.

**Leitlinie:** Nur so viel Prozess wie für nachvollziehbare, sichere, wartbare Software nötig ist; kein zusätzlicher Dokumentenselbstzweck.
