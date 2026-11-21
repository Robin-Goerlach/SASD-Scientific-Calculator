# V1.0 – wissenschaftlicher Funktionsumfang, Tasten- und Bedienmatrix

**Dokument-ID:** SASD-SCI-V1-KEYMAP-001  
**Stand:** 2026-11-21  
**Status:** **Vollständiger Vorschlag für die fachliche V1-Entscheidung; keine freigegebene endgültige Tastaturbelegung**  
**Geltungsbereich:** erste native iPhone-Anwendung **Classic RPN** (M1/M2), nicht der gesamte historische HP-41C/HP-48GX-Kommandoumfang  
**Quellen:** [Lastenheft](../LASTENHEFT.md), [Pflichtenheft](../PFLICHTENHEFT.md), [Architektur](../ARCHITEKTUR.md), [Roadmap](../../ROADMAP.md), [HP-41C-Katalog](HP-41C-FUNKTIONSKATALOG.md), [HP-48GX-Katalog](HP-48GX-FUNKTIONSKATALOG.md)  
**Technische Übergänge:** [ADR-V1-INPUT](../adr/ADR-V1-INPUT.md), [ADR-V1-NUM](../adr/ADR-V1-NUM.md), [Test- und Freigabeplan](V1-TEST-UND-FREIGABEPLAN.md)

> **Wichtig:** Die historische Befehlsvollständigkeit und die Freigabe der ersten App sind verschiedene Aufgaben. V1 muss die **hier nach Entscheidung zugesagten** wissenschaftlichen und klassischen Bedienfunktionen vollständig beherrschen; sie muss **nicht sämtliche HP-41C-/HP-48GX-Kommandos** ausführen. Die SVG-Abbildungen in `docs/images/` sind **Gestaltungskonzepte**, keine geprüfte HP-Tastenbelegung. Ein Tastenname/Command-Eintrag bedeutet **nicht**, dass er bereits implementiert wurde.

## 1. Begriffe, Status und Entscheidungsgrenzen

- **V1-Kandidat/P0:** für die erste alltagstaugliche Classic-RPN-App vorgeschlagene Kernfunktion. Erst nach einer **expliziten fachlichen V1-Freigabe** verbindlicher Command-/Layoutumfang.
- **V1-Prüffall:** eine zustands- und numerikbezogene Testanforderung, die beim späteren Freeze ein konkretes Golden erhält.
- **P1:** sinnvoller nächster Classic-Ausbau; nur Bestandteil der ersten Version, falls **ausdrücklich** in die freigegebene V1-Matrix übernommen.
- **Später:** FOCAL, historische Speicher-/Statusbefehle, Softmenüs, RPL, ALG-App, Module, System RPL etc.
- **TBD:** noch nicht beschlossen (Tastenposition, Shift-/ALPHA-Aufdruck, Registerzahl, Rundung, numerisches Format); darf nicht durch Bildinterpretation aufgefüllt werden.
- **Hardwaretasten vs. virtuelle Key-IDs:** SASD kann eine eigenständige ergonomische iPhone-Anordnung verwenden. Die zu prüfende **historische Funktionssemantik** ist getrennt von einer originalgetreuen **Gehäuse-/Tastaturkopie**.

**Grundsatzentscheidung bereits getroffen:** Classic **UPN/RPN ohne erzwungene `=`-Taste**, nutzbar offline, werbefrei/ohne Abo, erste Veröffentlichung ohne komplette historische Programmausführung.

## 2. Nutzbare V1-Sicht: 5 Funktionsflächen

1. **Display:** X als Eingabe-/Ergebnisregister; nach freigegebener UX-Matrix zusätzlich Y/Z/T (oder eindeutig erreichbare Stackansicht), Status DEG/RAD, Shift/ALPHA, Fehleranzeige.
2. **Ziffern- und Editierfeld:** Ziffern, Dezimaltrennzeichen, Vorzeichen, Exponenteneingabe, Korrektur und Löschen.
3. **Stack-/Registerfeld:** `ENTER`, `X↔Y`, `R↓`, `LAST X`, `STO`/`RCL` und deren freigegebene Registeradressierung.
4. **Arithmetik-/Wissenschaftsfeld:** Grundrechenarten, Potenz/Wurzel, Log/Exponential, trigonometrische Funktionen, Konstanten.
5. **Modi/weitere Befehle:** DEG/RAD, Zahlenformat, zusätzliche Shift-Ebene; sechs Softmenüpositionen **nur wenn** das freigegebene Bedienmodell sie benötigt.

**Kein implizites Menüsystem:** Sechs Softkeys sind *keine* zwingende historische 41C-Eigenschaft; sie sind eine mögliche spätere 48-/Menü-UX oder ein modernes SASD-Mittel. V1-Softkeys werden nur gebaut, wenn freigegebene Funktionen sonst nicht konsistent erreichbar sind.

## 3. Kanonische Key-IDs und Command-IDs (V1-Kandidaten)

Die Key-ID bezeichnet die **Bedienabsicht**; die Command-ID die fachliche Wirkung. Sie ist nicht identisch mit einem historischen Bytecode. Alle hier notierten IDs sind **vorgeschlagene stabile Namen**, noch keine veröffentlichte Programmierschnittstelle. Die Spalte „Ebene/Position“ ist **bewusst nicht als historische Originaltastenzuweisung ausgegeben**.

### 3.1 Eingabe und klassische Stackoperationen

| Key-ID / sichtbare Funktion | Vorgeschlagene Command-ID | Kandidat | Parameter / Wirkung | Shift-/ALPHA-/Position | Primärtest |
| --- | --- | --- | --- | --- | --- |
| `K-0` bis `K-9` / Ziffern 0–9 | `INPUT_DIGIT` | P0 | eine Ziffer in den aktiven X-Eingabepuffer; Stack-Lift nur nach Zustandstabelle | Ziffernfeld; historischer Aufdruck TBD | V1-KEY-001 |
| `K-DOT` / Dezimalzeichen | `INPUT_DECIMAL` | P0 | höchstens eine Mantissenmarkierung pro Zahl; Anzeige locale-gerecht | Ziffernfeld; Locale-Vorschlag TBD | V1-KEY-002 |
| `K-CHS` / ± | `CHANGE_SIGN` | P0 | Zeichenwechsel im Eingabepuffer oder Wert-/Stackoperation nach ADR | Position TBD | V1-KEY-003 |
| `K-EEX` / EEX | `INPUT_EXPONENT` | P0 | öffnet/bearbeitet Exponentenfeld; getrennte Vorzeichen-/Grenzprüfung | Position TBD | V1-KEY-004 |
| `K-ENTER` / ENTER↑ | `ENTER` | **P0** | duplizieren/liften und nachfolgendes Ziffern-Lift kontrollieren | große, gut erreichbare Taste; exakter Platz TBD | V1-KEY-005 |
| `K-SWAP` / X↔Y | `SWAP_XY` | P0 | X und Y vertauschen, alle anderen Register gemäß ADR | Haupt- oder Shift-Ebene TBD | V1-KEY-006 |
| `K-RDOWN` / R↓ | `ROLL_DOWN` | P0 | Rotation der vier Ebenen; `R↑` gesondert | Haupt-/Shift-Ebene TBD | V1-KEY-007 |
| `K-LASTX` / LAST X | `RECALL_LAST_X` | P0 | historisch orientierte Wiederherstellung des gesicherten X | Ebene TBD; Historikabweichungen offenlegen | V1-KEY-008 |
| `K-CLX` / CLX | `CLEAR_X` | P0 | X/Eingabe löschen, Register/Stack- und Lift-Effekte nach ADR | Ebene TBD | V1-KEY-009 |
| `K-DEL` / ← | `BACKSPACE_ENTRY` | P0 | korrigiert **eine laufende Eingabe**; außerhalb Entry vorher spezifizieren | Ebene TBD | V1-KEY-010 |
| `K-RESET` / Clear/Reset | `CLEAR_STACK` oder `RESET_SESSION` | P0 als **erreichbare** Funktion | Schutz vor versehentlichem Datenverlust; Reset/CLX unterscheiden | Schutzmenü/Langdruck TBD | V1-KEY-011 |
| `K-STO` / STO | `STORE_REGISTER` | P0 | schreibt in gültiges V1-Register, unveränderte Zielwerte bei Fehler | Adresswahl TBD | V1-KEY-012 |
| `K-RCL` / RCL | `RECALL_REGISTER` | P0 | holt V1-Register nach dokumentierter Stack-Lift-Regel | Adresswahl TBD | V1-KEY-013 |
| `K-SHIFT` / Shift | `SET_SHIFT_LAYER` | P0, **wenn** zweite Ebene benutzt | reine Eingabekontrolleraktion, keine Mathematik | Farbe, Label, Rücksetzung TBD | V1-KEY-014 |

**Registeranzahl/-adressierung:** Vorschlag **`00`–`09` für die erste UI-Ausbaustufe**. Das ist **keine** historische 41C-/CV-Speicherbehauptung; vor ADR-Freeze werden Anzahl, Registerarithmetik, indirekte Adressierung und Endbenutzer-Namenskonzept getrennt entschieden.

### 3.2 Grundrechenarten, Potenzen und mathematische Konstanten

| Key-ID / Label | Command-ID | Kandidat | Numerik/Stackwirkung | Ebene TBD / Test |
| --- | --- | --- | --- | --- |
| `K-ADD` / + | `ADD` | P0 | `Y + X`, binärer Drop, `LAST X` nach ADR | V1-MATH-001 |
| `K-SUB` / − | `SUBTRACT` | P0 | `Y − X` | V1-MATH-002 |
| `K-MUL` / × | `MULTIPLY` | P0 | `Y × X` | V1-MATH-003 |
| `K-DIV` / ÷ | `DIVIDE` | P0 | `Y ÷ X`, Fehler bei null | V1-MATH-004 |
| `K-SQRT` / √x | `SQRT` | P0 | unäre reelle Wurzel mit Domain-Prüfung | V1-MATH-005 |
| `K-SQUARE` / x² | `SQUARE` | P0 | unäres Quadrat; Overflow-Prüfung | V1-MATH-006 |
| `K-RECIP` / 1/x | `RECIPROCAL` | P0 | unärer Kehrwert; X=0 prüfen | V1-MATH-007 |
| `K-POW` / yˣ | `POWER_YX` | P0 | Potenz mit definierten reellen Domain-Regeln | V1-MATH-008 |
| `K-PI` / π | `PUSH_PI` | P0 | definierter π-Wert, kein Host-spezifischer Display-String | V1-MATH-009 |
| `K-PERCENT` / % | `PERCENT` | P1 | **nicht** ohne Business-/ALG-Konvention festlegen | Entscheidung offen |
| `K-ABS` / ABS | `ABSOLUTE` | P1 | unär, sinnvoll für wissenschaftlichen Ausbau | V1-EXT-001 |
| `K-FACT` / n! | `FACTORIAL` | P1 | Eingabebereich/Gamma-Erweiterung getrennt | V1-EXT-002 |
| `K-MOD` / MOD | `MODULO` | P1 | Vorzeichen-/Integerkonvention und Nullteiler | V1-EXT-003 |

### 3.3 Trigonometrie, Exponential- und Logarithmusfunktionen

| Key-ID / Label | Command-ID | Kandidat | Zahlen-/Winkelkontext | Test |
| --- | --- | --- | --- | --- |
| `K-SIN` / SIN | `SIN` | P0 | DEG/RAD über NumericContext | V1-MATH-010 |
| `K-COS` / COS | `COS` | P0 | DEG/RAD | V1-MATH-011 |
| `K-TAN` / TAN | `TAN` | P0 | Singularitäten nach Numeric-ADR | V1-MATH-012 |
| `K-ASIN` / SIN⁻¹ | `ASIN` | P0 | Wertebereich [-1,1], Resultat DEG/RAD | V1-MATH-013 |
| `K-ACOS` / COS⁻¹ | `ACOS` | P0 | Wertebereich [-1,1] | V1-MATH-014 |
| `K-ATAN` / TAN⁻¹ | `ATAN` | P0 | Ergebnis im aktiven Winkelmaß | V1-MATH-015 |
| `K-LN` / LN | `LN` | P0 | X>0 | V1-MATH-016 |
| `K-LOG` / LOG | `LOG10` | P0 | X>0 | V1-MATH-017 |
| `K-EXP` / eˣ | `EXP` | P0 | Overflow/Underflow definiert | V1-MATH-018 |
| `K-10X` / 10ˣ | `POW10` | P0 | Overflow/Underflow | V1-MATH-019 |
| `K-EXPM1` / eˣ−1 | `EXPM1` | P1 | Genauigkeit für kleine X | V1-EXT-004 |
| `K-LOG1P` / ln(1+x) | `LOG1P` | P1 | Genauigkeit für kleine X, X>-1 | V1-EXT-005 |

**Hinweis:** Das historische HP-41C-SIGN-Verhalten ist nicht identisch mit dem gewöhnlichen mathematischen Signum (siehe [41er-Katalog](HP-41C-FUNKTIONSKATALOG.md)). Eine generische `SIGN`-Funktion wird deshalb **nicht** unüberlegt in den P0-Kern aufgenommen.

### 3.4 Modi, Anzeige, Bedienhilfe und Status

| Aktion | vorgeschlagener Command | Kandidat | Abnahmepunkt |
| --- | --- | --- | --- |
| DEG aktivieren | `SET_ANGLE_DEG` | P0 | unveränderte Wertdaten; anderer Trigonometriekontext |
| RAD aktivieren | `SET_ANGLE_RAD` | P0 | gegen DEG-Testvektoren |
| GRAD aktivieren | `SET_ANGLE_GRAD` | P1 | historische Varianten später |
| Anzeige auf FIX n | `SET_FORMAT_FIXED` | P0 **im freigegebenen n-Bereich** | Rundung nur der Ansicht |
| Anzeige auf SCI n | `SET_FORMAT_SCI` | P0 | exponentielle Form, ohne Wertänderung |
| Anzeige auf ENG n | `SET_FORMAT_ENG` | P1 | Exponenten in Dreierschritten |
| Fehlerhilfe / Tastenerklärung | `OPEN_CONTEXT_HELP` (UI) | P0 | lokal/offline, kein serverseitiger Hilfezwang |
| SASD-Logo oben links | `OPEN_SASD_WEBSITE` (UI) | P0 | nur nach Nutzer-Tap und mit bestätigter URL |
| ALPHA-Modus / freies Programmieren | `SET_ALPHA_MODE` | später | **nicht** allein wegen historischer Beschriftung P0 |
| Tastenbelegung für FOCAL | historischer KeyAssign | M3/M4 | keine V1-Pflicht |
| Sechs Softmenüs | `OPEN_SOFT_MENU` | nach freigegebener UX-Matrix | kein ungeprüftes HP-48-Feature im Classic-Layout |
| ALG-Taste / `=`-Editor | kein Classic-P0 | eigenständiger ALG-Track | historischer Interpreter bleibt getrennt |

## 4. Historischer Funktionsumfang – absichtlich **nicht** in der V1-Tabelle dupliziert

| Bereich | Separates Verzeichnis / Status |
| --- | --- |
| Historischer HP-41C-Grundumfang | [vollständiger Forschungs-Katalog](HP-41C-FUNKTIONSKATALOG.md); die darin genannten Befehle sind **nicht** alle V1-Funktionen |
| HP-41CV/CX-spezifische Varianten | getrennt zu kennzeichnen, **keine** pauschale 41C-Pflicht |
| HP 48GX-Grundumfang, ROM-Index und nicht-verbale Menü-/Equation-Library-Operationen | [48GX-Katalog](HP-48GX-FUNKTIONSKATALOG.md) und [Abgleichmatrix](HP-48GX-BEFEHLSABGLEICH-MATRIX.md); Vollständigkeitsprüfung **offen** |
| 41er FOCAL und synthetische Programmierung A/B | M3/M4 langfristig; Byte Grabber C optional |
| 48er User RPL und ausgewählte System-RPL-Programme | M3/M4; Saturn-K4 optional |
| Time/Statistics/Advantage-Pac-inspirierte Funktionen | später, ohne Original-ROM und ohne zweiten Math-Algorithmus |
| Matrizen, Complex, Statistik, Solver, Integration, Differentialgleichungen, Bitlogik | später nach eigenem wissenschaftlichem Funktionsfreeze; nicht heimlich P0 |
| Financial-TVM/NPV/IRR/Anleihen | **eigenständiges Financial-Produkt**; keine V1-Pflicht |

## 5. Physische Tastaturbelegung und Shift-Layout: **noch nicht freigegeben**

Eine *Funktionsmatrix* ist noch **keine** fotografisch festgelegte Taste-zu-Taste-Abbildung. Für die reale iPhone-UI ist eine folgende **zusätzliche, zu füllende Entscheidungstabelle** erforderlich:

| UI-Slot | Key-ID / Primärlabel | Shift-Aktion | ALPHA-Aktion | Menü-/Profilkontext | Golden-Test | Status |
| --- | --- | --- | --- | --- | --- | --- |
| Display / vier Stackebenen | N/A | N/A | N/A | RPN/Mode | UI-DISPLAY-* | Layout TBD |
| Enter-Funktionszone | `K-ENTER` | TBD | TBD | Classic RPN | V1-KEY-005 | Slot TBD |
| Ziffern 0…9 | `K-0`…`K-9` | TBD | TBD | Editing/Normal | V1-KEY-001 | Slot TBD |
| Operatorzone `+−×÷` | `K-ADD`…`K-DIV` | TBD | TBD | RPN | V1-MATH-001…004 | Slot TBD |
| Wissenschafts-/Shift-Zone | Befehle aus 3.2/3.3 | TBD | TBD | freigegebene Funktionsmatrix | V1-MATH-* | Slot TBD |
| Register-/Moduszone | `K-STO`/`K-RCL`/DEG/RAD | TBD | TBD | Programmlaufzeit **nicht** V1 | V1-KEY-012… | Slot TBD |

**Vor Implementierung abzunehmen:** tatsächliche Tastenpositionen auf dem iPhone XS, aktive Shift-/ALPHA-Ebenen, Softmenübedarf, Tap-Flächen/Safe Areas, Beschriftungen, Zugänglichkeit und nachweislich erreichbare P0-Befehle. Ein V1-Key darf **nicht** unsichtbar unter einem Panel verschwinden.

## 6. Bedienfluss und Sichtbarkeitsregeln

- **Rechner-Zustandsmaschine:** [ADR-V1-INPUT](../adr/ADR-V1-INPUT.md). Ein Key-Tap ist nicht einfach `push(double)`.
- **Tastenverfügbarkeit:** Die View bezieht tatsächliche Command-/Capability-Liste aus der Session; die Anzeige darf historische, nicht implementierte Befehle **nicht** als aktiv ausweisen.
- **Fehler:** ungültige Eingabe, Domain, Division durch null, Overflow, Registeradresse und Persistenz müssen über stabile Fehlercodes/Offline-Texte nachvollziehbar sein.
- **Reset:** `CLX`, Backspace, vollständige Stacklöschung, Registerlöschung und Restore sind **verschiedene Aktionen**; gefährliche Rücksetzung vor unbeabsichtigtem Tap schützen.
- **Physische Eingabehilfen:** optional Tastatur-/Hardware-Keyboard-Mapping über dieselben Key-IDs; keine parallele Rechenlogik.
- **Deutsch/Englisch:** Anzeigenamen und Help-Texte getrennt von stabilen Command-IDs; locale-spezifisches Dezimalzeichen und `EEX`-Bearbeitung via Numeric-ADR.
- **Design:** Display/Stack/Tasten im Hochformat; Branding klein oben links; keine permanente Desktop-IDE, kein `=`-Zwang, keine Werbung.

## 7. Testfälle, die **jede** P0-Zusage benötigen

| Gruppe | Beispiel | Erwartung |
| --- | --- | --- |
| V1-KEY | `3 ENTER 4 ENTER 5 × +` | X = 23 und alle Stack-/Lift-/LAST-X-Zustände nach freigegebener ADR |
| V1-MATH | `10 ENTER 4 −`; `10 ENTER 4 ÷` | X = 6 und 2,5 |
| V1-MATH | `30 SIN` (DEG); `π 6 ÷ SIN` (RAD) | ca. 0,5 innerhalb numerischer Toleranz |
| V1-MATH | `0 LN`, `-1 SQRT`, `0 1/x` | kontrollierte Domain-/Divisionfehler, kein Stackschaden |
| V1-KEY | `STO 00`, `RCL 00` | nach Freigabe definierte Stack-/Register-/LAST-X-Effekte |
| V1-KEY | CLX, DEL, RESET getrennt | niemals unerwartet andere Register löschen |
| V1-MODE | FIX/SCI/DEG/RAD ändern | Anzeige/AngleContext korrekt, interner Wert unverändert |
| V1-UX | jede sichtbare Taste auch in Shift | erreichbar/VoiceOver/ohne Überlagerung auf XS |
| V1-STATE | Suspend/Terminate/Restore | Zustand gemäß [Snapshot-ADR](../adr/ADR-V1-STATE.md) wiederhergestellt |
| V1-OFFLINE | Flugmodus, erster Start | vollständige P0-Mathematik und Hilfe ohne Internet |

Vollständige Gate-Zuordnung und Freigabevorlage: [V1-Test- und Freigabeplan](V1-TEST-UND-FREIGABEPLAN.md).

## 8. Liste der noch zu treffenden **fachlichen** Entscheidungen

| Decision-ID | Abhängigkeit | Minimaler Beschluss |
| --- | --- | --- |
| `KEY-DEC-01` | `LH-OD-001` | endgültige V1-P0-/P1-Auswahl und Umfang der wissenschaftlichen Tastatur |
| `KEY-DEC-02` | `LH-OD-001` | physische iPhone-X-Slots, Layout/Shift-/ALPHA-/Softmenü und Beschriftung |
| `KEY-DEC-03` | `LH-OD-002` | `ENTER`/LAST X/CLX/Backspace/Stack-Roll-/Register- und Lift-Semantik |
| `KEY-DEC-04` | `LH-OD-003` | NumericContext, DEG/RAD, Display-/Fehlerkonvention |
| `KEY-DEC-05` | `LH-OD-005` | Mindest-iOS/XS-Testhardware, UI-Accessibility |
| `KEY-DEC-06` | `LH-OD-006/007` | offizielle SASD-Web-URL, Offlinehilfe, Store-Preismodell |

**Abnahmeregel:** Nach Zustimmung werden **genau** P0 und ausdrücklich übernommene P1-Funktionen in einer versionierten V1-Freeze-Liste gekennzeichnet; erst diese ist für Umsetzung/Tests verbindlich. Die historischen Komplettkataloge bleiben davon unabhängig.
