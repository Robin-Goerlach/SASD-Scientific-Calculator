# HP 48GX – AUR-Teilprüfung A11 (Positionen 501–517)

**Prüfstand:** 22.11.2026 · **Gerät:** serienmäßiger HP 48GX, ohne Fremdkarten.  
**Bereich:** Letzte **17** Positionen des AUR-Kapitel-3-Befehlsindex, `>` bis `→`, einschließlich Kontrollsymbole, Mathematik- und Statistikoperatoren.  
**Prüfstufe:** **A01–A11-Textinventar nach diesen 17 Positionen lückenlos erfasst, aber NICHT historisch abgenommen.** Quellen-TOC/ROM-Vergleich und unabhängiger Pocket-Guide-Textabgleich. **Keine** Originalbild-/Glyphensichtfreigabe, keine umfassende Stack-/Typ-/Flag-/Fehler-/Hardwareprüfung.

## 1. Nachgewiesene Quellen

1. Hewlett-Packard, *HP 48G Series Advanced User's Reference*, 4. Auflage (1994), `Contents-16`, Positionen 501–517, unveränderte Texttranskription [hp48gx-aur-command-index.json](../reference/hp48gx-aur-command-index.json). Original https://literature.hpcalc.org/community/hp48g-aur-en.pdf .
2. [hp48gx-rom-index-baseline.json](../reference/hp48gx-rom-index-baseline.json), stock HP 48GX: zu allen **17 Quellpositionen** existiert rein *mechanisch* ein normierter ROM-Namenseintrag mit XLIB. Das bedeutet **nicht**, dass jeder normierte Name fachlich zum Quellsymbol passt: **Position 515 ist ausdrücklich widersprüchlich**.
3. Chris Coffin und Thomas Dick, *The HP 48G/GX Pocket Guide* (Grapevine Publications, 1996), unabhängiger **Command Index, gedruckte S. 76** (Webansicht: https://www.manualslib.com/manual/3743173/Hp-48g.html?page=78 ; durchsuchbarer Text: https://literature.hpcalc.org/community/hp48g-pg-en.pdf). Die nachfolgenden Stackdiagramme beginnen auf **gedruckter S. 77**. Der textuelle PDF-Index gibt beispielsweise `==` statt `≡`, `d` statt `∂` und eine schwer unterscheidbare Glyphe für den Einheitenanhang wieder. Auch dieser Text ist **keine bildliche Originalscanprüfung**.
4. Für die unabhängige Kurzsemantik zusätzlich: James Donnelly, *HP 48 Pocket Book*, https://literature.hpcalc.org/community/hp48g-pb.pdf . Dieses Werk führt symbolische Gleichungsbildung `=`, logischen Vergleich `==`, Addieren/Entfernen aus `ΣDAT` und lokale Bindung `→` separat auf. Die Original-Glyphenverwechslung von AUR #515 wird durch dieses sekundäre Werk nicht abschließend aufgelöst.

**Bildprüf-Grenze:** Die Bildseitenansicht des 34-MB-Pocket-Guide-Original-PDF konnte wegen Größenbegrenzung des Webzugriffs nicht geöffnet werden. Gedruckte AUR-Glyphen in der eingefrorenen JSON-Textbasis bleiben ebenfalls `SOURCE_TOC_TEXT_NOT_SCAN_VISUALLY_APPROVED`. Kein Eintrag in diesem Bericht darf als visuell bestätigte Abschrift ausgegeben werden.

## 2. Vollständige A11-Positionsliste

| AUR # | AUR-Quelltextname | AUR-TOC-Seite | ROM-Normalisierung / XLIB | Pocket-Druckseite | Pocket-OCR-Text bzw. kontextueller Kandidat | Prüfstatus | Deutsche Arbeitsbeschreibung |
| ---: | --- | --- | --- | ---: | --- | --- | --- |
| 501 | `>` | Contents-16 | `>` / `2:236` | 76 | `>` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Prüft für zwei vergleichbare Argumente, ob das erste größer als das zweite ist; Rückgabewert 0 oder 1. |
| 502 | `≥` | Contents-16 | `≥` / `2:238` | 76 | `= (OCR verliest ≥)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Prüft für zwei vergleichbare Argumente, ob das erste größer oder gleich dem zweiten ist; Rückgabewert 0 oder 1. |
| 503 | `=` | Contents-16 | `=` / `2:59` | 76 | `=` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Bildet aus zwei Objekten eine symbolische Gleichung; ist kein boolescher Gleichheitstest. |
| 504 | `≡` | Contents-16 | `==` / `2:233` | 76 | `==` | ROM-Name `==`; AUR-Glyphe visuell offen | Prüft die logische Gleichheit zweier Argumente und liefert 0 oder 1. Quelltextglyphe ≡, ROM-Name ==. |
| 505 | `≠` | Contents-16 | `≠` / `2:234` | 76 | `# (OCR verliest ≠)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Prüft auf Ungleichheit; Ergebnis als historischer Wahrheitswert 0 oder 1. |
| 506 | `!` | Contents-16 | `!` / `2:99` | 76 | `\| (OCR verliest !)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Berechnet die Fakultät oder für passende andere Eingaben die Gammafunktion Γ(x+1). |
| 507 | `∫` | Contents-16 | `∫` / `2:252, 2:253` | 76 | `I (OCR verliest ∫)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Integriert einen Ausdruck nach einer Variablen zwischen zwei Grenzen; numerische oder symbolische Ausgabe abhängig von Flags und Eingaben. |
| 508 | `∂` | Contents-16 | `∂` / `2:247, 2:248` | 76 | `& oder d (OCR verliest ∂)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Bildet die symbolische Ableitung eines Ausdrucks nach einer benannten Variablen. |
| 509 | `%` | Contents-16 | `%` / `2:124` | 76 | `%` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Liefert x Prozent von y; Ergebnis x·y/100, kein Prozentänderungsbefehl. |
| 510 | `π` | Contents-16 | `π` / `2:63` | 76 | `T (OCR verliest π)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Liefert die Kreiszahl π symbolisch oder numerisch abhängig vom Auswertungsmodus. |
| 511 | `Σ` | Contents-16 | `Σ` / `2:254` | 76 | `Z (OCR verliest Σ)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Bildet eine Folge-Summe anhand von Indexvariable, Start, Ende und Summanden-Ausdruck. |
| 512 | `Σ+` | Contents-16 | `Σ+` / `2:286` | 76 | `2+ (OCR verliest Σ+)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Fügt einen oder mehrere statistische Datenpunkte in ΣDAT hinzu. |
| 513 | `Σ−` | Contents-16 | `Σ-` / `2:287` | 76 | `2= (OCR verliest Σ−)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Entfernt den zuletzt mit Σ+ erfassten Datenpunkt aus ΣDAT; Verhaltensdetails bei Mehrspaltendaten offen. |
| 514 | `√` | Contents-16 | `√` / `2:79` | 76 | `I (OCR verliest √)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Berechnet die Quadratwurzel eines Arguments; Reell-/Komplex-/Symbol-Fälle später separat prüfen. |
| 515 | `¯` | Contents-16 | `NEG` / `2:60` | — | `- / Einheitenanhang (kein NEG-Nachweis)` | QUELLENKONFLIKT – KEINE unabhängige Namensbestätigung | Ungeklärte Textindexglyphe: eingefrorene Baseline interpretiert ¯ als NEG (Vorzeichenwechsel), während der unabhängige Pocket Guide hier das Anfügen einer Einheit an einen Zahlenwert beschreibt. Nicht freigegeben. |
| 516 | `\|` | Contents-16 | `|` / `2:255, 2:256` | 76 | `\| (Substitution)` | Mehrdeutige Pocket-Glyphe; SUBST nach Kontext | Algebraische Ersetzung von Namen bzw. Teilausdrücken durch zugeordnete Werte in einem symbolischen Ausdruck; Pocket-Guide-Text führt daneben einen ähnlich dargestellten Einheitenanhang. |
| 517 | `→` | Contents-16 | `→` / `1792:4, 1792:16` | 76 | `#* (OCR verliest →)` | Pocket-Text kontextuell zugeordnet, Originalglyphe offen | Bindet Stackobjekte an nachfolgend benannte lokale Variablen in einer User-RPL-Struktur. |

### Bilanz

- **17/17 AUR-Quellindexpositionen** einzeln beschrieben, nummeriert und auf Quellindex `Contents-16` zurückgeführt.
- **17/17 technische ROM-Normalisierungstreffer** (einschließlich der **fragwürdigen** Zuordnung `¯`→`NEG`). **16/17** sind nach unabhängiger Pocket-Guide-Semantik auf Namens-/Funktionsfamilienebene plausibel; **#515 bleibt ungeklärt**.
- **16/17** unabhängige Pocket-Guide-*Command Index*-Textzuordnungen als Prüfbeleg gezählt. **#515 keine bestätigte Zuordnung**: Die unabhängige Seite beschreibt an derselben Alphabetposition einen **Einheitenanhang**, nicht `NEG` als Vorzeichenwechsel. Die Pocket-Seitenzelle bleibt daher absichtlich leer/nichtnumerisch.
- **0** visuelle Originalseitenabnahmen; **0** vollständige historische AUR-Stack-/Geräteabnahmen. Die Liste sämtlicher A01–A11-Indexpositionen ist textuell dokumentiert, die **historische Vollständigkeit jedoch noch NICHT zertifiziert**.

## 3. Kritische fachliche Unterschiede und Fehlerquellen

### A11-503 `=` und A11-504 `≡` (ROM `==`)

- Die Quelle unterscheidet symbolische **Gleichungsbildung** `=` (ROM `2:59`) von logischer **Objektgleichheit** `==` (ROM `2:233`), die einen Wahrheitswert liefert.
- Die AUR-TOC-Texttranskription `≡` ist nicht identisch mit der ROM-Schreibweise `==`. Solange die originale AUR-Druckglyphe nicht visuell abgenommen wurde, **keine** automatische Alias- oder identische Parserfunktion `=`/`==`/`≡` freigeben.
- Der unabhängige Pocket-Guide-Text trennt beide Funktionen im Command Index ausdrücklich; ein numerischer Wahrheitswert darf nicht an die Stelle eines Gleichungsobjekts treten.

### A11-506 `!`, A11-507 `∫`, A11-508 `∂`

- `!` erlaubt Fakultät und entsprechend unterstützte Gammafunktion; keine Behauptung, dass die gesamte komplexe Gammafunktion ohne Spezialfälle bereits implementiert sei.
- `∫`: untere Grenze, obere Grenze, Integrand, Variable. Ergebnis numerisch oder symbolisch je nach Status (u.a. Flag -3); exakte Stackreihenfolge und Fehlerfälle in V prüfen.
- `∂`: symbolischer Ausdruck und Variable; keine Gleichsetzung mit numerischem Differenzenquotienten.

### A11-509 `%`, A11-511 `Σ`, A11-512/513 `Σ+`/`Σ−`

- `%` bedeutet **x Prozent von y** (x·y/100), **nicht** die prozentuale Veränderung `%CH`.
- `Σ` ist eine **symbolische Summation** über eine Indexvariable; `Σ+` und `Σ−` ändern hingegen **statistische Daten in `ΣDAT`**.
- `Σ−` entfernt den zuletzt eingefügten Datenpunkt; die Wortwahl `Σ−` als bloße arithmetische Subtraktion wäre falsch.

### **A11-515 `¯` – offener Quellenwiderspruch, nicht als NEG freigeben**

- Einfrierdaten `hp48gx-aur-command-index.json`: `printed_name=¯`, `rom_normalized_candidate=NEG`, `in_rom_baseline=true`, mit Locator zur **NEG-**AUR-Referenz und ROM `2:60`.
- Der AUR-Index hat aber bereits **#242 `NEG`** als eigenständigen Originalnamen. Bei #515 steht das Zeichen in der Gruppe der **nichtalphabetischen Operatoren**, unmittelbar nach `√` und vor `|`.
- Der Pocket Guide beschreibt an exakt dieser Stelle die Operation **„Einheit an Realwert anhängen“**. Das ist funktional **nicht** gleich `NEG`. Auch die Web-OCR gibt die Glyphe nicht zuverlässig wieder.
- **Konsequenz:** Den vorhandenen normalisierten ROM-Index nicht blind löschen oder umschreiben; `¯` aber **nicht als historischen Alias zu NEG behaupten**. Quelloriginal `Contents-16` und AUR-Detailseite sowie das Pocket-Guide-Originalbild auf gedruckter S. 76 visuell prüfen. **Bis dahin keine Implementierungsfreigabe und kein zusätzlicher Befehl.**

### A11-516 `|` – zwei Pocket-Texteinträge, nur einer im ROM gleichnamig

- Die unabhängige Pocket-Liste enthält **zwei benachbarte Zeilen** mit verwischten, sehr ähnlichen Zeichen: einen **Einheitenanhang** (mutmaßlicher Bezug zu #515) und das Ersetzen von Variablen im algebraischen Ausdruck.
- Die ROM-Namenszuordnung `|` → `2:255`, `2:256` ist für die **symbolische Substitution** plausibel. Dies ist **nicht** mit der getrennten Einheiteneingabe gleichzusetzen. Erst Bildprüfung entscheidet die tatsächlich gedruckten zwei Symbole.

### A11-517 `→` und Mehrfach-XLIB

- `→` bindet benannte **lokale** Variablen; zwei ROM-XLIB-Kennungen (`1792:4`, `1792:16`) bedeuten unterschiedliche Ausführungskontexte, **keine zwei unabhängigen AUR-TOC-Namen**. Der RPL-Pfeil ist kein allgemeiner mathematischer Folgepfeil.
- Weitere mehrere XLIBs: `∫` (`2:252/253`), `∂` (`2:247/248`) und `|` (`2:255/256`). Anzahl der XLIB-Aufrufe ist nicht Anzahl der AUR-Indexpositionen.

## 4. Abnahme- und Restarbeiten

- [x] **Alle 517 AUR-Quellindexpositionen** in A01–A11 positionstreu als Textinventar dokumentiert.
- [x] Alle **17 A11-Zeilen** auf ROM-Namensstand überprüft; offensichtlicher Sachkonflikt bei #515 nicht verschwiegen.
- [x] **16/17** unabhängige Pocket-Guide-Command-Index-Textentsprechungen, der problematische Fall als offenes Delta.
- [x] Kontrollwort-/Operatorsemantik in Gleichungsbildung, Gleichheit, Prozentrechnung, Differential-/Integralrechnung, Statistik-Σ-Befehlen und lokalen Bindungen sauber getrennt.
- [ ] Original-AUR-Quellseiten (TOC) und Pocket-Guide-Seite 76 **bildlich** überprüfen; A11-515 `¯`, `|`, `≡` und `∂` nach Sichtprüfung ggf. **quellgestützt** korrigieren, keine stille Änderung des eingefrorenen Quellindex.
- [ ] Vollständige AUR-Stackdiagramme, Objekttypen, Systemflags, Fehlerbedingungen und reale HP48GX-Ausführung dokumentieren.
- [ ] Nach der Namensinventur die weiteren **O-/E-/U-/M-/F-Katalogtranchen** des [Prüfplans](HP-48GX-PRUEFTRANCHEN-PLAN.md) aufnehmen; historische Vollständigkeit bleibt `HISTORICAL_COMPLETENESS_NOT_CERTIFIED`.

**A11-Status:** `AUR_TOC_POCKET_TEXT_COMPARISON_DONE_WITH_OPEN_DISCREPANCY`. **Nächster Schritt:** erster **O-Originalscan-/Glyphen-Prüfblock** nach dem maschinenlesbaren Checkpoint; auf keinen Fall die A11-515-Differenz als erledigt ausgeben. Die historische Emulation ist kein Release-Blocker für die erste ausgereifte iPhone-RPN-Rechner-V1.
