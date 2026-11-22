# HP 48GX – Teilprüfung G-9 bis G-15 (Checkpoint G02)

**Prüfdatum:** 22.11.2026 · **Status:** Quellenindex-Audit abgeschlossen, Originalscan-/Befehlssemantik-Freigabe offen.  
**Historische Quelle:** HP *48G Series User's Guide*, Edition 8 (1994), Appendix G-9–G-15, PDF-S. 489–495. https://www.hp.com/ctg/Manual/c00442262.pdf  
**Datengrundlage:** [HP-Operation-Index](../reference/hp48gx-operation-index-crosschecked-pages.json), [AUR-Befehlsverzeichnis](../reference/hp48gx-aur-command-index.json), [ROM-Index](../reference/hp48gx-rom-index-baseline.json)

**Wichtige Unterscheidung:** Ein exakter OCR-Worttreffer ist **kein Nachweis**, dass die gesamte Zeile/Handbuchtypklasse oder RPL-Stackwirkung richtig erkannt wurde. Visuelle Originalscan-Prüfung bleibt ausstehend.

## 1. Seitenbilanz

| Seite | PDF-Seite | Indexzeilen | Exakte OCR-Token | Ohne OCR-Bestätigung | Scanfreigabe |
| --- | ---: | ---: | ---: | ---: | --- |
| G-9 | 489 | 14 | 13 | 1 | **offen** |
| G-10 | 490 | 13 | 6 | 7 | **offen** |
| G-11 | 491 | 13 | 9 | 4 | **offen** |
| G-12 | 492 | 14 | 8 | 6 | **offen** |
| G-13 | 493 | 14 | 12 | 2 | **offen** |
| G-14 | 494 | 13 | 11 | 2 | **offen** |
| G-15 | 495 | 11 | 9 | 2 | **offen** |

**Gesamt:** 92 gespeicherte Quellzeilen; 68 mit exakter OCR-Token-Präsenz, 24 ohne. G-10 hat besonders viele falsche OCR-Wörter aus dem Fließtext; **23 OCR-Zeilenkandidaten sind nicht 23 tatsächliche Befehlszeilen**, sondern der überlieferte Textindex enthält dort 13.

## 2. Vollständiger Quellen-zu-ROM/AUR-Namensvergleich für diese sieben Seiten

| Quell-ID | Aufschrift | HP-Klasse | Exakter ROM-Name | In AUR-TOC auffindbar | Exakter OCR-Token | Scan visuell |
| --- | --- | --- | --- | --- | --- | --- |
| G-9:01 | `CON` | C | ja | ja | ja | offen |
| G-9:02 | `COND` | C | ja | ja | ja | offen |
| G-9:03 | `CONIC` | C | ja | ja | ja | offen |
| G-9:04 | `CONJ` | F | ja | ja | ja | offen |
| G-9:05 | `CONLIB` | C | ja | ja | ja | offen |
| G-9:06 | `CONST` | F | ja | ja | ja | offen |
| G-9:07 | `CONT` | C | ja | ja | ja | offen |
| G-9:08 | `CONVERT` | C | ja | ja | ja | offen |
| G-9:09 | `COPY` | O | nein | nein | ja | offen |
| G-9:10 | `CORR` | C | ja | ja | ja | offen |
| G-9:11 | `COS` | A | ja | ja | nein | offen |
| G-9:12 | `COSH` | A | ja | ja | ja | offen |
| G-9:13 | `COV` | C | ja | ja | ja | offen |
| G-9:14 | `CR` | C | ja | ja | ja | offen |
| G-10:01 | `CRDIR` | C | ja | ja | ja | offen |
| G-10:02 | `CROSS` | C | ja | ja | ja | offen |
| G-10:03 | `CST` | C | nein | nein | ja | offen |
| G-10:04 | `CSWP` | C | ja | ja | ja | offen |
| G-10:05 | `CYLIN` | C | ja | ja | ja | offen |
| G-10:06 | `C→PX` | C | ja | ja | nein | offen |
| G-10:07 | `C→R` | C | ja | ja | nein | offen |
| G-10:08 | `←D` | O | nein | nein | nein | offen |
| G-10:09 | `↪←D` | O | nein | nein | nein | offen |
| G-10:10 | `D→` | O | nein | nein | nein | offen |
| G-10:11 | `↪D→` | O | nein | nein | nein | offen |
| G-10:12 | `DARCY` | F | ja | ja | ja | offen |
| G-10:13 | `ΣDAT` | C | nein | nein | nein | offen |
| G-11:01 | `DATE` | C | ja | ja | ja | offen |
| G-11:02 | `DATE+` | C | ja | ja | ja | offen |
| G-11:03 | `→DATE` | C | ja | ja | nein | offen |
| G-11:04 | `DBUG` | O | nein | ja | ja | offen |
| G-11:05 | `DDAYS` | C | ja | ja | ja | offen |
| G-11:06 | `DEC` | C | ja | ja | ja | offen |
| G-11:07 | `DECR` | C | ja | ja | ja | offen |
| G-11:08 | `DEFINE` | C | ja | ja | ja | offen |
| G-11:09 | `→DEF` | O | nein | nein | nein | offen |
| G-11:10 | `DEG` | C | ja | ja | ja | offen |
| G-11:11 | `DEL` | O | nein | nein | ja | offen |
| G-11:12 | `→DEL` | O | nein | nein | nein | offen |
| G-11:13 | `↪→DEL` | O | nein | nein | nein | offen |
| G-12:01 | `DEL→` | O | nein | nein | nein | offen |
| G-12:02 | `DEL→` | O | nein | nein | nein | offen |
| G-12:03 | `DELALARM` | C | ja | ja | nein | offen |
| G-12:04 | `DELAY` | C | ja | ja | ja | offen |
| G-12:05 | `DELKEYS` | C | ja | ja | ja | offen |
| G-12:06 | `DEPND` | C | ja | ja | ja | offen |
| G-12:07 | `DEPTH` | C | ja | ja | ja | offen |
| G-12:08 | `DET` | C | ja | ja | ja | offen |
| G-12:09 | `DETACH` | C | ja | ja | ja | offen |
| G-12:10 | `→DIAG` | C | ja | ja | nein | offen |
| G-12:11 | `DIAG→` | C | ja | ja | nein | offen |
| G-12:12 | `DIFFEQ` | C | ja | ja | ja | offen |
| G-12:13 | `DIV` | O | nein | nein | nein | offen |
| G-12:14 | `DISP` | C | ja | ja | ja | offen |
| G-13:01 | `DNEG` | O | nein | nein | ja | offen |
| G-13:02 | `DO` | C | ja | ja | ja | offen |
| G-13:03 | `↩ DO` | O | nein | nein | nein | offen |
| G-13:04 | `DOERR` | C | ja | ja | ja | offen |
| G-13:05 | `DOLIST` | C | ja | ja | ja | offen |
| G-13:06 | `DOSUBS` | C | ja | ja | ja | offen |
| G-13:07 | `DOT` | C | ja | ja | ja | offen |
| G-13:08 | `DOT+` | O | nein | nein | ja | offen |
| G-13:09 | `DOT−` | O | nein | nein | nein | offen |
| G-13:10 | `DRAW` | C | ja | ja | ja | offen |
| G-13:11 | `DRAW` | O | ja | ja | ja | offen |
| G-13:12 | `DRAX` | C | ja | ja | ja | offen |
| G-13:13 | `DROP` | C | ja | ja | ja | offen |
| G-13:14 | `DROPN` | C | ja | ja | ja | offen |
| G-14:01 | `DRPN` | O | nein | nein | ja | offen |
| G-14:02 | `DROP2` | C | ja | ja | ja | offen |
| G-14:03 | `DTAG` | C | ja | ja | ja | offen |
| G-14:04 | `DUP` | C | ja | ja | ja | offen |
| G-14:05 | `DUPN` | C | ja | ja | ja | offen |
| G-14:06 | `DUPN` | O | ja | ja | ja | offen |
| G-14:07 | `DUP2` | C | ja | ja | ja | offen |
| G-14:08 | `D→R` | F | ja | ja | nein | offen |
| G-14:09 | `e` | F | ja | ja | nein | offen |
| G-14:10 | `ECHO` | O | nein | nein | ja | offen |
| G-14:11 | `EDIT` | O | nein | nein | ja | offen |
| G-14:12 | `EDIT` | O | nein | nein | ja | offen |
| G-14:13 | `EDIT` | O | nein | nein | ja | offen |
| G-15:01 | `EEX` | O | nein | nein | nein | offen |
| G-15:02 | `EGV` | C | ja | ja | ja | offen |
| G-15:03 | `EGVL` | C | ja | ja | ja | offen |
| G-15:04 | `ELSE` | C | ja | ja | ja | offen |
| G-15:05 | `END` | C | ja | ja | ja | offen |
| G-15:06 | `ENDSUB` | C | ja | ja | ja | offen |
| G-15:07 | `ENG` | C | ja | ja | ja | offen |
| G-15:08 | `EQ` | C | nein | nein | ja | offen |
| G-15:09 | `EQ→` | C | ja | ja | nein | offen |
| G-15:10 | `EQNLIB` | C | ja | ja | ja | offen |
| G-15:11 | `ERASE` | C | ja | ja | ja | offen |

## 3. Nicht wörtlich im ROM-Index enthaltene programmierbar klassifizierte Namen

| Label | HP-Seite | Befund | Konsequenz |
| --- | --- | --- | --- |
| `CST` | G-10 | Reservierter Menüname bzw. Variablenkontext | Nicht als frei ausführbares neues XLIB erfinden; Kontext und veränderbare Objekte anhand AUR/Guide prüfen |
| `ΣDAT` | G-10 | Statistik-Datenvariable | Als reserviertes Objekt behandeln; Speicher-/Persistenzeffekte getrennt prüfen |
| `EQ` | G-15 | Aktuell gespeicherte Gleichung/Reservat | Kein selbständiger Rechenbefehl allein aufgrund der C-Klassifizierung |

## 4. Besondere Kontext- und OCR-Fallen

- **G-10:** `CST` und `ΣDAT` stehen im Quelltext als C, entsprechen aber reservierten Datenobjekten. Die ursprünglichen OCR-Kandidaten sind durch Layout-Mischungen unzuverlässig.
- **G-11:** `DBUG` ist im AUR-Verzeichnis vorhanden, fehlt aber in der 517er-ROM-Namenliste und ist nicht als gewöhnliche Mathematikfunktion zu behandeln.
- **G-12:** Zweimal `DEL→` in unterschiedlichen Bedienkontexten; die Wiederholung darf nicht als Duplikatdatenfehler entfernt werden.
- **G-14:** Dreimal `EDIT` für unterschiedliche Editierumgebungen; als mehrere Aufrufe eines gleich bezeichneten UI-Kommandos erhalten.
- **G-15:** `EQ` ist eine reservierte Gleichungsvariable, die nicht als eigenständige Mathematikfunktion gezählt werden darf.
- Zeichenähnlichkeiten bei `DEL→`, `→DEL`, `→DIAG`, `DIAG→`, `↩ DO` und `DOT−` verlangen später Originalscan-Sichtkontrolle.

**Audit-Ergebnis G02:** Die 92 vorhandenen Quellzeilen wurden gegen die zwei anderen Namensinventare geprüft und mit dem Originalseitenbereich verknüpft. **Historische Vollständigkeit/Visuelle Scanfreigabe/Stackkonformität weiterhin nicht bescheinigt.** Nächste Teilprüfung G03: G-16–G-22.
