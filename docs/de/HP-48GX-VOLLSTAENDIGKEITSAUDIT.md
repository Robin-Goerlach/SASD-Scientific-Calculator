# HP 48GX – Vollständigkeitsprüfung des historischen Funktionskatalogs

**Stand:** 2026-11-21 · **Auditstatus:** **OFFEN – keine behauptete Gesamtvollständigkeit**  
**Zielkatalog:** [HP-48GX-FUNKTIONSKATALOG.md](HP-48GX-FUNKTIONSKATALOG.md)  
**Ziel:** Eine reproduzierbare, quellengestützte Aussage zur Abdeckung des **serienmäßigen HP 48GX** ermöglichen – **ohne** ihn mit dem HP 48SX, dem späteren HP 48gII, Anwenderkarten oder internen undokumentierten Saturn-Routinen zu verwechseln.

> **Wichtig:** Das Ziel ist ein nachweisbarer Katalog, kein vorgebliches „100 %“ allein aufgrund der Länge. Eine nichtprogrammierbare Bildschirmaktion ist ebenfalls eine Bedienfunktion. Die 517 ROM-Namen zählen dagegen auch Konstanten und RPL-Strukturtoken. Diese Zahlen haben verschiedene Bezugsräume und dürfen nicht addiert werden.

## 1. Verbindliche Definition des Untersuchungsumfangs

| Teilumfang | Gehört zum Basis-Historikkatalog? | Abschlusskriterium |
| --- | --- | --- |
| Programmierbare User-RPL-Befehle und Operatoren | **Ja** | Jede AUR-Einzelreferenz und jeder ROM-Name eindeutig erfasst/abgeglichen |
| Nichtprogrammierbare Bedienoperationen | **Ja** | Jede Operation aus *User's Guide*, Appendix G, erfasst/abgeglichen |
| Alle 49 Tasten und tatsächlich zugänglichen Shift-/Alpha-/User-Ebenen | **Ja** | Jede belegte Kombination und ihr kontextabhängiger Effekt nachgewiesen |
| Eingebaute Menüs, Untermenüs und dynamische Softkeys | **Ja** | Navigationsgraph und alle ausgelösten Operationen gegenüber Appendix G geprüft |
| 12 Applications, Editor- und Dialogfunktionen | **Ja** | Interaktive Bedienpfade und Resultate dokumentiert |
| Alle eingebauten Plottypen samt Zoom-, Trace-, Analyse- und Editoraktionen | **Ja** | Dialog-/Menüwege und unterschiedliche Funktionssemantik geprüft |
| Eingebaute Einheiten | **Ja** | Jede Definition mit Bezeichnung, Dimension, Faktor und nötigem Offset separat verifiziert |
| Eingebaute Gleichungsbibliothek und Konstanten | **Ja** | Jedes Thema, jeder Problemtitel, jede einzelne Formel und jeder Konstantenwert nachgewiesen; rechtlich nur eigenständige Beschreibungen/Metadaten veröffentlichen |
| Speicher, Verzeichnisse, Systemflags, Objekttypen, Alarme, IR/Seriell | **Ja** | Appendix-/Handbuchabschnitte + relevante Zustandswirkungen abgearbeitet |
| Physische GX-Kartenslots und Portoperationen | **Ja** | Basishardware, Kartenfähigkeit und reale GX-Semantik getrennt dokumentiert |
| Zusätzliche Programme/Bibliotheken von eingesteckten Fremdkarten | **Nein, separat** | Als optionale Erweiterung mit Hersteller/Modul/Version und eigener Prüfliste |
| HP 48gII, 49/50g und HP-48SX-exklusive Neuerungen | **Nein** | Fehlzuordnungen herausfiltern |
| Undokumentiertes System RPL, Saturn-Instruktionssatz | **Separater K3/K4-Forschungsumfang** | **Keine** unhaltbare absolute Vollständigkeitsbehauptung zum internen System |

**Varianten:** Ein Abschluss gilt immer für eine namentlich bezeichnete Hardware-/ROM-Konfiguration (mindestens „48GX Basisgerät, keine Zusatzkarten“). Revisionsabweichungen werden als eigene Deltas erfasst. Ein umfassender Gerätefamilienanspruch ohne geprüfte Revisionen ist unzulässig.

## 2. Quellennachweis: vier **unabhängige Inventare**

| Inventar | Quelle (identifizierbar) | Welche Einträge werden gesammelt? | Gegenwärtiger Auditstatus |
| --- | --- | --- | --- |
| **G – Operationen** | HP, *HP 48G Series User's Guide*, 8. Ausgabe, **Appendix G: Operation Index, G-1–G-58**, [Original](https://www.hp.com/ctg/Manual/c00442262.pdf) | Alle **Operationen**, auch *nicht programmierbare*, Tastenwege, Typ und Handbuchseite | **OFFEN**: noch kein vollständiger zeilenweiser Abgleich mit dem bisherigen Katalog |
| **A – Programmierbefehle** | HP, *HP 48G Series Advanced User's Reference*, 4. Ausgabe, **Kapitel 3: Command Reference**, [Original](https://literature.hpcalc.org/community/hp48g-aur-en.pdf) | Alle Befehle; Argument-/Ergebnis-Stack, Typen, Modi, Flags, Fehler und Sonderfälle | **OFFEN**: die 517 ROM-Kurzbeschreibungen sind kein AUR-Einzelnachweis |
| **P – unabhängiger Befehlsindex** | James Donnelly, *The HP 48G/GX Pocket Guide*, **Command Index, S. 41 ff.**, [PDF](https://literature.hpcalc.org/community/hp48g-pg-en.pdf) | Programmierbare Befehle und knappe Stacknotation; **keine** UI-only-Operationen | **OFFEN**: vollständiger Zwei-Richtungen-Abgleich |
| **R – ROM-Namen** | saturnus, aus dem HP-48GX-ROM abgeleitete [48gx.json](https://github.com/ractive/saturnus/blob/main/crates/saturnus-cli/data/commands/48gx.json) | Befehlsnamen, XLIB-Nummer und ROM-Menüzuordnung | **Teilprüfung durchgeführt:** 517 eindeutige Namen/517 Tabellenzeilen; **nicht** gleichbedeutend mit Gesamtvollständigkeit |
| **K – physische Tastatur** | Eigenes HP-48GX-Foto + Original-Handbuchabschnitt zur Tastatur | 49 Tasten; Normal, Links-/Rechts-Shift, Alpha, User, kontextabhängige Wirkung | **Teilprüfung:** 49 physische Positionen aufgelistet; nicht jede Kombination und jeder Kontext nachgetestet |
| **M – Menü-/Application-Graph** | *User's Guide* Kapitel zu Menüs, Apps, Editoren, Appendix C sowie Appendix G | Alle Softkey-Seiten, Aktionen, modale Zustände und dynamischen Menüs | **OFFEN:** bisher Menüübersichten, keine vollständige Erreichbarkeitsmatrix |
| **D – eingebaute Daten** | *User's Guide* und *Advanced User's Reference* (Tabellen für Gleichungen, Units, Flags, Variablen, Konstanten) | Jede Formel, Einheitendefinition, Konstantenwert und jedes reservierte Objekt | **OFFEN:** 15 Gleichungsthemen/102 Titel und 16 Einheiten-Menügruppen, aber keine vollständigen Datentabellen |

**Nicht als GX-Primärquelle verwenden:** die hochgeladene Datei `HP 48GX grafikfähiger Taschenrechner.pdf` trägt tatsächlich den Titel **`hp 48gII grafikfähiger Taschenrechner`**, Ausgabe **2004**. Sie gehört zu einem anderen Modell. Das hochgeladene `HP 48g-qsg-de.pdf` ist die echte deutsche *HP 48G Kurzanleitung*, 3. Ausgabe 1994, eignet sich aber erklärtermaßen **nicht als vollständiger Befehlsindex**.

### 2.1 Verfahrensregel für PDF-Quellen

Originaldatei, Edition, Artikelnummer, Seitenzählweise (PDF-Seite **und** gedruckte Seite) und SHA-256 des verwendeten PDFs festhalten. Scans, extrahierten Text und Tabellen optisch gegen die tatsächliche Seite prüfen. Jede automatische OCR-/Textgewinnung kann Pfeilzeichen, Indizes, griechische Zeichen, hochgestellte Ziffern, Leerzeichen und `0/O` verfälschen. Die PDFs, ROMs oder fremde Buchseiten **nicht** in das öffentliche SASD-Repository kopieren; nur eigene Extrakte/Metadaten, Quellennachweise und lizenzgeprüfte Testfälle.

## 3. Eindeutige Identitäten statt Namenszählung

Jede Funktion/Aktion erhält eine stabile ID und einen **Typ**:

- `GX-CMD-xxxx`: programmierbarer RPL-Befehl (mit genauer ROM-/AUR-Zuordnung).
- `GX-UI-xxxx`: nichtprogrammierbare Menü-/Tastatur-/Editoroperation.
- `GX-KEY-rr-cc-mode`: tatsächlicher Tastenweg in einem gegebenen Tastaturzustand.
- `GX-MENU-xxxx`: Menü/Untermenü/Softkey-Aktion mit Kontext.
- `GX-EQL-xxxx`: einzelne Formel-/Konstantendatendefinition.
- `GX-UNIT-xxxx`: einzelne Einheitendefinition.
- `GX-FLAG-xxxx`, `GX-OBJ-xxxx`, `GX-SYSVAR-xxxx`: Zustände/Objekte.
- `GX-PORT-xxxx`: physische Portfähigkeit/Speicheroperation.

**Nicht anhand desselben sichtbaren Namens zusammenfassen:** `TRACE` als Matrixspur vs. Grafik-`TRACE` als UI; `NEXT` als RPL-Schleifenwort vs. nichtprogrammierbarer Debug-Bedienpunkt; `RULES` als ROM-Name vs. EquationWriter-Kontext; `ROOT` im User-RPL vs. grafische Nullstellensuche. **Aliase** dürfen zu einer zugrundeliegenden Funktion zeigen, aber jeder getrennte Bedienweg muss referenziert sein.

### 3.1 Minimales Einzelfeldschema

| Feld | Zweck |
| --- | --- |
| `id`, `canonical_name`, `display_label`, `aliases` | stabile Identität und Mehrdeutigkeiten |
| `kind`, `category`, `subsystem`, `menu_path` | UI / programmierbar / Datentabelle / Systemkontext |
| `model`, `rom_revision`, `hardware_profile` | keine irrtümliche Modellübertragung |
| `source_id`, `printed_page`, `pdf_page`, `reference_symbol` | unabhängig überprüfbare Fundstelle pro Aussage |
| `argument_types`, `stack_before`, `stack_after` | HP-48-typkonforme RPL-Wirkung |
| `modes_flags`, `errors`, `side_effects` | tatsächliches Verhalten über Rechenwert hinaus |
| `documentation_status` | `unreviewed` / `documented` / `cross_checked` / `hardware_checked` / `conflict` / `excluded` |
| `sasD_implementation_status` | **getrennt**: `implemented` / `tested` / `planned` / `optional` / `explicitly_excluded` |
| `tests`, `tested_platform`, `fixture_origin` | reproduzierbare Konformitätskontrolle |
| `reviewer`, `reviewed_on`, `notes` | wer hat was anhand welcher Ausgabe geprüft |

## 4. Abgleichverfahren – immer **in beide Richtungen**

1. **Appendix-G-Index G** vollständig in ein tabellarisches Inventar übertragen – einschließlich *alle* nichtprogrammierbaren Operationen. Zeilen und Seiten visuell prüfen.
2. **AUR-Inventar A** aus dem gesamten Command-Reference-Teil unabhängig aufbauen; nicht einfach die 517 ROM-Namen wiederverwenden. Name, Klassifikation, Stackdiagramm, argumentabhängige Fälle, Flags und Verweise pro Befehlsreferenz aufnehmen.
3. **Pocket-Guide-Inventar P** unabhängig erfassen. Fehlende Einträge gegenüber A und R sind nicht automatisch Fehler des Pocket Guide; aber jede Abweichung erhält einen Prüfvermerk.
4. **ROM-Inventar R** aus der versioniert festgehaltenen JSON-Quelle reproduzieren und danach eine Kommandokennungsprüfung vornehmen.
5. **Tasten-/Menüinventare K/M** als Zustandsgraph statt als flache Liste prüfen: physische Taste → Shift-/Alpha-/User-State → Menüseite/Editor → Wirkung. Jede Kante besitzt einen Quellbeleg, Dialogtest oder explizites `unreviewed`.
6. **Dateninventar D** gesondert für jede Gleichung, jeden Problemtitel, jede Einheit und jede Konstante erstellen. Nur die 15 Bereiche und 102 Namen zu zählen ist kein Formelnachweis.
7. **Bilateral diffen:** `G - Katalog`, `Katalog - G`, `A - Katalog`, `Katalog - A`, `P - R`, `R - P`, `M - G`, `D - Katalog`. Jedes Delta muss `added`, `alias`, `alternate_context`, `model_specific`, `not_programmable`, `not_in_source` oder `unresolved` erhalten.
8. **Unabhängige Stichproben am echten 48GX oder einem rechtmäßig betriebenen Emulator** für repräsentative Typ-/Stack-/Modus-/Fehlerfälle. Das beweist das *Verhalten* ausgewählter Fälle, nicht ohne weiteres die Katalogvollständigkeit.
9. **Dokumentation und CI:** automatisierte Kontrolle auf doppelte IDs, Quellenverweise, fehlende Tabelleneinträge, unaufgelöste Deltas, Tasten-/Menüabdeckung und unbewiesene Statuswechsel; Reports unter Versionskontrolle.

## 5. Harte Abschlussregeln (Gate)

Die Kennzeichnung **„vollständig für den definierten HP-48GX-Basisumfang“** ist **nur dann** zulässig, wenn:

- [ ] Der Operation Index, Appendix G (G-1–G-58), **zeilenweise vollständig** erfasst und gegen den Katalog geprüft ist.
- [ ] **Jeder** AUR-Command-Reference-Eintrag erfasst und mit einer Katalog-ID verbunden ist.
- [ ] Der Pocket-Guide-Command-Index vollständig differenziert und alle Abweichungen begründet sind.
- [ ] Sämtliche 517 derzeit bekannten ROM-Namen erfasst bleiben; ROM-Revisionen/Abweichungen sind explizit identifiziert.
- [ ] Alle 49 physischen Tasten sind in ihren dokumentierten Shift-/Alpha-/User-Kontexten überprüft.
- [ ] Menüs, Editor- und Dialogaktionen sowie 12 Anwendungen und 15 Plottypen sind durch Quell- oder Gerätetests inventarisiert.
- [ ] Die komplette Menge der **einzelnen** Gleichungen und Konstanten der eingebauten Equation Library ist im eigenen Dateninventar verzeichnet.
- [ ] Die vollständigen **einzelnen** Einheiten mit Dimensions-/Skalen- und Temperatur-Offsets sind verzeichnet und überprüft.
- [ ] Systemflags, reservierte Variablen, Objekttypen und GX-Ports haben eigenständige, geprüfte Inventare.
- [ ] Es gibt **null ungeklärte Differenzen**, **null unklassifizierte Einträge**, **null unprüfbare Katalogzeilen** und **null vermischte 48gII-Funktionen**.
- [ ] Alle Quellennachweise sind mit **Edition, Fundseite und geprüftem Status** nachvollziehbar.
- [ ] Der automatische Inventar-/Diff-Check läuft fehlerfrei. Er prüft **Katalogkonsistenz**, nicht die laufende Rechnerimplementierung.

Ein menschlicher Abgleich (Handbuch/Display) bleibt **zusätzlich** erforderlich. „Null ungeklärte Deltas“ darf nie dadurch erreicht werden, dass Einträge ohne Begründung als `excluded` markiert werden.

## 6. Aktueller Befund: keine Freigabe

| Prüfdimension | Aktueller Befund am 21.11.2026 | Ergebnis |
| --- | --- | --- |
| ROM-Namensindex (eine ROM-basierte Quelle) | 517 eindeutige Namen im `HP-48GX-FUNKTIONSKATALOG.md` | **nur diese Liste strukturell vollständig** |
| Tastatur | 49 Positionen aufgelistet, Kontext-/Shift-Verhalten nicht überall unabhängig geprüft | **teilweise** |
| Betrieb und Apps | 12 Anwendungsumgebungen und Menügruppen beschrieben | **teilweise** |
| Plottypen | 15 Klassen aufgelistet, grafische UI-Aktionen noch nicht durchgängig verifiziert | **teilweise** |
| Equation Library | 15 Gruppen / 102 Titel inventarisiert; nicht jede der 300+ Gleichungen einzeln geprüft | **offen** |
| Einheiten | 16 Menügruppen, 148 notierte Indexpositionen teils mehrfach/kontextabhängig; historische 147 Einheiten nicht zeilenweise und mit Faktoren nachgewiesen | **offen** |
| Appendix G | Verweis vorhanden, aber kein geprüfter bilateraler Einzeleintragsabgleich | **offen** |
| AUR-Kommandoreferenz | Als Quelle genannt; Stack-/Flag-/Fehlersemantik nicht pro Zeile nachgewiesen | **offen** |
| Modellfilter | Separater 2004er HP 48gII erkannt; systematischer Ausschlussvergleich noch offen | **offen** |

**Daraus folgt:** Das aktuelle Dokument ist eine umfangreiche **Arbeitsreferenz**, aber noch kein abgenommener vollständiger historischer Katalog. Die richtige Kennzeichnung im Zielkatalog lautet bis zur Gate-Erfüllung **„Vollständigkeit ungeprüft – Inventar in Audit“**. Nichtprogrammierbare Handlungen und doppelt belegte Labels müssen gesondert identifiziert werden. Keine V1-/M2-Releaseblockade: Die historische Konformitätsprüfung wird gemäß `AGENTS.md` und `LASTENHEFT.md` als langfristiger separater Nachweis geführt.

## 7. Empfohlene verbindliche Reihenfolge

1. **Zuerst Appendix G, G-1–G-58, abschreiben/prüfen und mit bestehenden 517 Einträgen abgleichen.** Das liefert am schnellsten belastbare Fehlbestände und UI-only-Operationen.
2. Danach **AUR Kapitel 3** vollständig mit Stackdiagrammen, Objektklassen, Flags und Fehlerfällen je Eintrag kontrollieren.
3. Erst danach Tastatur-/Menügraph, App-Dialoge und Datenkataloge vollständig abarbeiten.
4. Zuletzt Handgeräte-/Emulatortests und Null-Differenzen-Freigabe. Bei Zweifeln **offen** lassen statt schöngerechnet „fertig“ zu melden.

**Dokumentationsregel für künftige Änderungen:** Jede behauptete neue, fehlende oder geänderte Funktion braucht einen Beleg und eine Audit-ID. Nach jedem Eintrag/Quellupdate die Differenzübersicht aktualisieren. Kein Produkt-README soll aus dem bloßen Vorhandensein dieses Inventars eine tatsächlich implementierte historische Kompatibilität ableiten.

## 8. Durchgeführter Prüfstand vom 21.11.2026 (tatsächliche Evidenz)

- **Reproduzierbares ROM-Basisset:** 517 Namen aus einer spezifischen `saturnus`-ROM-Indexdatei; 517 alphabetische Tabellenzeilen im Hauptkatalog und 517 XLIB-Referenzen in der [Befehlsabgleich-Matrix](HP-48GX-BEFEHLSABGLEICH-MATRIX.md). Die dazugehörigen Kennungen stimmen beim strukturellen Vergleich überein.
- **Ergänzende Indizien:** Sekundärindex `manuals.json` liefert AUR-Fundstellenhinweise für 464, User's-Guide-Hinweise für 204, beide Hinweise für 197, mindestens einen für 471 und **keinen** für 46 der ROM-Namen. Diese Zahl ist eine Eigenschaft des **unvollständigen Sekundärindex**. Insbesondere zahlreiche der 46 Befehle sind sehr wohl direkt im Original-Operation-Index nachweisbar; sie sind **nicht** 46 fehlende oder falsche Befehle.
- **Original-Operation-Index:** Erste Einzelvergleiche mit **Appendix G, G-1–G-58**, enthalten 41 ausgewählte Fälle aus G-2–G-16 und **102 weitere ausgewählte interaktive Fälle aus G-17–G-58** in der Befehlsabgleich-Matrix. **143 geprüfte Tabellenzeilen** sind *nicht* gleichbedeutend mit vollständiger Abschrift aller G-Seiten; manche gleiche Namen sind absichtlich für verschiedene Kontexte doppelt enthalten.
- **Erkannte zusätzliche Namen/Quellenkontexte:** `GRAPH` als älterer, dokumentierter Grafikbefehl (siehe AUR und Guide), `LAST` als zu prüfender Alias, `CST`, `ΣDAT`, `IOPAR`, `PPAR`, `VPAR`, `PRTPAR`, `FV`, `PMT`, `PV`, `PYR` als Originalindex-Zugriffe/reservierte Namen, `SCLS` als separat zu prüfender Statistikzugang. Keine davon wird ungeprüft als neue XLIB-ID ausgegeben.
- **Fachlich korrigierte Katalogstellen:** u.a. `COLΣ` (Statistikspalten **auswählen**, nicht aufsummieren), `TRACE` (Matrixspur vs. Grafikverfolgung), `PGDIR` (Verzeichnis löschen statt dorthin wechseln), `PINIT` (RAM-Ports initialisieren), Richtung der Matrix-Umwandlungen.
- **Maschinenlesbarer Konsistenzschutz:** [`scripts/check_hp48gx_inventory.py`](../../scripts/check_hp48gx_inventory.py) kontrolliert ROM-Namenssatz, XLIB-Kennungen und Anzahl der 49 Tastaturpositionen über beide Markdown-Dokumente. [GitHub Actions `hp48gx-inventory-audit.yml`](../../.github/workflows/hp48gx-inventory-audit.yml) startet den Check bei relevanten Änderungen. Dieser Check weist **nicht** die Vollständigkeit der historischen Funktionalität nach; er meldet das ausdrücklich.
- **Nicht geprüft / Abnahme offen:** lückenlose Erfassung jeder einzelnen Operation der 58 gedruckten G-Seiten, vollständige Einzelabnahme jeder AUR-Stackvariante, unabhängiger Pocket-Guide-Vergleich sämtlicher Befehle, vollständige historische Werte aller 300+ Gleichungen und 147 Einheiten, ROM-Revisionsvarianten und Tests an Originalhardware.

**Abnahmeentscheidung weiterhin: KEIN GO.** Ein fehlerfreier Konsistenzcheck ist eine notwendige technische Schranke, ersetzt aber keine historische Vollständigkeitsprüfung.

## 9. Quellenwiderspruch bei der Zahl der eingebauten Maßeinheiten

Im **selben** offiziellen HP-48G-Series-User's-Guide (Edition 8, 1994) stehen unterschiedliche Bestandsangaben:

- **Kapitel 10, Einleitung / „Unit Objects“:** Katalog mit **147 Einheiten**.
- **Kapitel 10, Seite 10-1:** **neun Basiseinheiten** und **141 abgeleitete Einheiten**, also bei schlichter Addition **150**; das Handbuch erklärt dort nicht, warum beide Gesamtzahlen auseinanderfallen.

Dies ist ein **nachgewiesener interner Quellenwiderspruch**, nicht eine von SASD zu entscheidende Produktfunktion. Die frühere Aussage „147 einzelne Definitionen sind vollständig nachgewiesen“ ist deshalb **nicht zulässig**. Erst ein tatsächlicher Abgleich sämtlicher Einträge des `UNITS`-Katalogs samt Synonymen, Präfixvarianten und Menügruppen kann den konsistenten Modellbestand festlegen. Auch ein aus einer Quelle abgeleitetes arithmetisches Ergebnis `9 + 141 = 150` rechtfertigt noch keine 150 eindeutigen Implementierungen.

**Quellennachweis:** [HP 48G Series User's Guide, Kapitel 10 („Unit Objects“), gedruckte Seiten 10-1 bis 10-2](https://www.hp.com/ctg/Manual/c00442262.pdf). **Status:** `OPEN_SOURCE_CONFLICT`.

## 10. Kontrollsumme der Equation Library (Anhang F)

Das offizielle Handbuch belegt in **Anhang F, F-1 bis F-3** genau **315 Gleichungen und 396 Variablen in 15 Fachgebieten**. Die 15 sachgebietsweisen Summen sind im [Hauptkatalog](HP-48GX-FUNKTIONSKATALOG.md) dokumentiert und addieren sich zu diesen Zahlen. Das ist eine **abgeschlossene Kontrollsummenprüfung**, aber **keine** Validierung jeder einzelnen Formel oder Variablenbeziehung. Die 102 bisher zusammengetragenen Problemüberschriften brauchen ihren separaten 1:1-Abgleich.

**Status:** `SUMMARY_VERIFIED`; Einzelgleichungen `UNVERIFIED`.
