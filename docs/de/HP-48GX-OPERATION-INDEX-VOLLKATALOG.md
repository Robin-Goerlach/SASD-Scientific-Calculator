# HP 48GX – Original-Operation-Index G-2 bis G-58 (vollständiger Zeilenkatalog)

**Prüfstand:** 21.11.2026 · **Modell:** HP 48GX serienmäßig, ohne nachgerüstete Karten  
**Originalquelle:** [Hewlett-Packard, *HP 48G Series User's Guide*, 8. Ausgabe (1994), Appendix G](https://www.hp.com/ctg/Manual/c00442262.pdf) · Original-PDF SHA-256 `77b25f276277e90fbbd7ca1676d7440f69a844169fec6951382255df26e0782a`.  
**Maschinenlesbare Einzelbelege:** [Indexinventar mit Klassifikation und OCR-Abgleich](../reference/hp48gx-operation-index-crosschecked-pages.json).  
**Technischer ROM-Katalog:** [HP-48GX-FUNKTIONSKATALOG.md](HP-48GX-FUNKTIONSKATALOG.md).  
**Status:** **57/57 Tabellenseiten anhand des auslesbaren Originalindex gegengeprüft; nicht visuell auf jeder Scan-Seite abgenommen.** Dies ist ein vollständiger **zeilenweiser Datenbestand der verfügbaren Original-Textindexdarstellung**. Er ersetzt **nicht** die unabhängige AUR-Kontrolle, ROM-Revisionsprüfung und Formel-/Einheitentabellenabnahme.

## Einordnung

- **696 gedruckte Originalindexzeilen** aus G-2 bis G-58, **661 verschiedene angezeigte Namen/Labels**. Mehrfachnennungen mit unterschiedlichem Kontext bleiben erhalten.
- **517 Zeilen mit wenigstens einer Klasse C/F/A** (einschließlich Mischform C/O), **179 rein nichtprogrammierbare O-Zeilen**. Mehrere Zeilen verwenden dieselben Namen; diese Zahlen sind **nicht** die Zahl unabhängiger programmierbarer Kommandos.
- **26 unterschiedliche, im Originalindex programmierbar klassifizierte Drucknamen fehlen wörtlich im 517-Namen-ROM-Index**. Überwiegend Schrift-/Aliasvarianten oder reservierte Variablennamen. Die Zuordnung ist **ein Prüfvorschlag**, keine unbesehene Erzeugung von XLIB-IDs.
- **143 unterschiedliche reine UI-Labels ohne identischen ROM-Namen**. Diese sind **kein** Teil des 517er-ROM-Namensinventars und müssen für eine komplette App-/Menü-Spezifikation berücksichtigt werden.
- **G-1** definiert die Klassen `O` (Bedienoperation), `C` (programmierbarer Befehl), `F` (algebraisch verwendbare Funktion), `A` (analytische Funktion) und enthält keine normale Namens-Tabelle.

**Quellen-/OCR-Vorbehalte:** Die Sonderzeichen G-57 wurden im separaten OCR-Durchlauf gar nicht korrekt erkannt; dort ist die Original-Textindexdarstellung die Grundlage. Die Zeichen `FO^` (Original-Textindex G-17) und `TAHN` (G-48, in der verifizierenden PDF-OCR als `TANH`) haben erkennbare Textindexfehler. Beim ersten Eintrag bleibt die exakte Druckschreibweise noch durch Sichtprüfung zu klären; `TANH` wurde anhand der OCR und AUR als kanonischer Name behandelt. Auch `Σ` vs. `S`, Sonderzeichen, Steuerpfeile und trennende Minuszeichen brauchen einen Scan-/AUR-Abgleich.

## Vollständige Zeilentabelle des Operation Index

| Originalseite | Aufschrift/Name | HP-Typ | ROM-Zuordnung / Einordnung | OCR exakt erkannt |
| --- | --- | --- | --- | --- |
| G-2 | `←A` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-2 | `↪A←` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-2 | `A→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-2 | `↪A→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-2 | `ABS` | `F` | ROM-Index, gleicher Name | ja |
| G-2 | `ACK` | `C` | ROM-Index, gleicher Name | ja |
| G-2 | `ACKALL` | `C` | ROM-Index, gleicher Name | ja |
| G-2 | `ACOS` | `A` | ROM-Index, gleicher Name | ja |
| G-2 | `ACOSH` | `A` | ROM-Index, gleicher Name | ja |
| G-2 | `ADD` | `C` | ROM-Index, gleicher Name | ja |
| G-2 | `AF` | `O` | zusätzliche Bedienfunktion | ja |
| G-2 | `ALOG` | `A` | ROM-Index, gleicher Name | ja |
| G-2 | `AMORT` | `O` | ROM-Index, gleicher Name | ja |
| G-3 | `AMORT` | `C` | ROM-Index, gleicher Name | ja |
| G-3 | `AMRT` | `O` | zusätzliche Bedienfunktion | ja |
| G-3 | `AND` | `C/F` | ROM-Index, gleicher Name | ja |
| G-3 | `ANIMATE` | `C` | ROM-Index, gleicher Name | ja |
| G-3 | `APPLY` | `F` | ROM-Index, gleicher Name | ja |
| G-3 | `ARC` | `C` | ROM-Index, gleicher Name | ja |
| G-3 | `ARCHIVE` | `C` | ROM-Index, gleicher Name | ja |
| G-3 | `AREA` | `O` | zusätzliche Bedienfunktion | ja |
| G-3 | `ARG` | `F` | ROM-Index, gleicher Name | ja |
| G-3 | `ARRY→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-4 | `→ARRY` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-4 | `ASIN` | `A` | ROM-Index, gleicher Name | ja |
| G-4 | `ASINH` | `A` | ROM-Index, gleicher Name | ja |
| G-4 | `ASN` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `ASR` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `ATAN` | `A` | ROM-Index, gleicher Name | ja |
| G-4 | `ATANH` | `A` | ROM-Index, gleicher Name | ja |
| G-4 | `ATICK` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `ATTACH` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `AUTO` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `AXES` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `BAR` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `BARPLOT` | `C` | ROM-Index, gleicher Name | ja |
| G-4 | `BAUD` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `BEEP` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `BEG` | `O` | zusätzliche Bedienfunktion | ja |
| G-5 | `BESTFIT` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `BIN` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `BINS` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `BLANK` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `BOX` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `BOX` | `O` | ROM-Index, gleicher Name | ja |
| G-5 | `BOXZ` | `O` | zusätzliche Bedienfunktion | ja |
| G-5 | `BUF LEN` | `C` | `BUFLEN` – Schreibvariante | nein / abweichend |
| G-5 | `BYTES` | `C` | ROM-Index, gleicher Name | ja |
| G-5 | `B→PV` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-6 | `B→R` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-6 | `CALC` | `O` | zusätzliche Bedienfunktion | ja |
| G-6 | `CANCL` | `O` | zusätzliche Bedienfunktion | ja |
| G-6 | `CASE / ↩CASE / ↪CASE` | `C/O/O` | `CASE` – Sammelzeile: C/O/O | nein / abweichend |
| G-6 | `CEIL` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-6 | `CENTR` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-6 | `CF` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-6 | `%CH` | `F` | ROM-Index, gleicher Name | ja |
| G-6 | `✓CHK` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-6 | `CHOOS` | `O` | zusätzliche Bedienfunktion | ja |
| G-7 | `CHOOSE` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CHR` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CIRCL` | `O` | zusätzliche Bedienfunktion | ja |
| G-7 | `CKSM` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CLEAR` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CLK` | `O` | zusätzliche Bedienfunktion | ja |
| G-7 | `CLKADJ` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CLLCD` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CLOSEIO` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CLS` | `C` | `CLΣ` – OCR/Schriftzeichen: Σ | nein / abweichend |
| G-7 | `CLUSR` | `C` | `CLVAR` – Historisches Alias (AUR 3-52) | ja |
| G-7 | `CLVAR` | `C` | ROM-Index, gleicher Name | ja |
| G-7 | `CNCT` | `O` | zusätzliche Bedienfunktion | ja |
| G-7 | `CNRM` | `C` | ROM-Index, gleicher Name | ja |
| G-8 | `CNTR` | `O` | zusätzliche Bedienfunktion | ja |
| G-8 | `→COL` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-8 | `+COL` | `O` | zusätzliche Bedienfunktion | ja |
| G-8 | `COL+` | `C` | ROM-Index, gleicher Name | ja |
| G-8 | `−COL` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-8 | `COL−` | `C` | `COL-` – Unicode Minuszeichen | nein / abweichend |
| G-8 | `COL→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-8 | `COLΣ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-8 | `COLCT` | `C` | ROM-Index, gleicher Name | ja |
| G-8 | `COLCT` | `O` | ROM-Index, gleicher Name | ja |
| G-8 | `COLCT` | `O` | ROM-Index, gleicher Name | ja |
| G-8 | `COMB` | `F` | ROM-Index, gleicher Name | ja |
| G-9 | `CON` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `COND` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `CONIC` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `CONJ` | `F` | ROM-Index, gleicher Name | ja |
| G-9 | `CONLIB` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `CONST` | `F` | ROM-Index, gleicher Name | ja |
| G-9 | `CONT` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `CONVERT` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `COPY` | `O` | zusätzliche Bedienfunktion | ja |
| G-9 | `CORR` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `COS` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-9 | `COSH` | `A` | ROM-Index, gleicher Name | ja |
| G-9 | `COV` | `C` | ROM-Index, gleicher Name | ja |
| G-9 | `CR` | `C` | ROM-Index, gleicher Name | ja |
| G-10 | `CRDIR` | `C` | ROM-Index, gleicher Name | ja |
| G-10 | `CROSS` | `C` | ROM-Index, gleicher Name | ja |
| G-10 | `CST` | `C` | Reservierter Variablenname | ja |
| G-10 | `CSWP` | `C` | ROM-Index, gleicher Name | ja |
| G-10 | `CYLIN` | `C` | ROM-Index, gleicher Name | ja |
| G-10 | `C→PX` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-10 | `C→R` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-10 | `←D` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-10 | `↪←D` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-10 | `D→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-10 | `↪D→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-10 | `DARCY` | `F` | ROM-Index, gleicher Name | ja |
| G-10 | `ΣDAT` | `C` | Reservierter Variablenname | nein / abweichend |
| G-11 | `DATE` | `C` | ROM-Index, gleicher Name | ja |
| G-11 | `DATE+` | `C` | ROM-Index, gleicher Name | ja |
| G-11 | `→DATE` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-11 | `DBUG` | `O` | zusätzliche Bedienfunktion | ja |
| G-11 | `DDAYS` | `C` | ROM-Index, gleicher Name | ja |
| G-11 | `DEC` | `C` | ROM-Index, gleicher Name | ja |
| G-11 | `DECR` | `C` | ROM-Index, gleicher Name | ja |
| G-11 | `DEFINE` | `C` | ROM-Index, gleicher Name | ja |
| G-11 | `→DEF` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-11 | `DEG` | `C` | ROM-Index, gleicher Name | ja |
| G-11 | `DEL` | `O` | zusätzliche Bedienfunktion | ja |
| G-11 | `→DEL` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-11 | `↪→DEL` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-12 | `DEL→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-12 | `DEL→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-12 | `DELALARM` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-12 | `DELAY` | `C` | ROM-Index, gleicher Name | ja |
| G-12 | `DELKEYS` | `C` | ROM-Index, gleicher Name | ja |
| G-12 | `DEPND` | `C` | ROM-Index, gleicher Name | ja |
| G-12 | `DEPTH` | `C` | ROM-Index, gleicher Name | ja |
| G-12 | `DET` | `C` | ROM-Index, gleicher Name | ja |
| G-12 | `DETACH` | `C` | ROM-Index, gleicher Name | ja |
| G-12 | `→DIAG` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-12 | `DIAG→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-12 | `DIFFEQ` | `C` | ROM-Index, gleicher Name | ja |
| G-12 | `DIV` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-12 | `DISP` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DNEG` | `O` | zusätzliche Bedienfunktion | ja |
| G-13 | `DO` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `↩ DO` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-13 | `DOERR` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DOLIST` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DOSUBS` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DOT` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DOT+` | `O` | zusätzliche Bedienfunktion | ja |
| G-13 | `DOT−` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-13 | `DRAW` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DRAW` | `O` | ROM-Index, gleicher Name | ja |
| G-13 | `DRAX` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DROP` | `C` | ROM-Index, gleicher Name | ja |
| G-13 | `DROPN` | `C` | ROM-Index, gleicher Name | ja |
| G-14 | `DRPN` | `O` | zusätzliche Bedienfunktion | ja |
| G-14 | `DROP2` | `C` | ROM-Index, gleicher Name | ja |
| G-14 | `DTAG` | `C` | ROM-Index, gleicher Name | ja |
| G-14 | `DUP` | `C` | ROM-Index, gleicher Name | ja |
| G-14 | `DUPN` | `C` | ROM-Index, gleicher Name | ja |
| G-14 | `DUPN` | `O` | ROM-Index, gleicher Name | ja |
| G-14 | `DUP2` | `C` | ROM-Index, gleicher Name | ja |
| G-14 | `D→R` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-14 | `e` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-14 | `ECHO` | `O` | zusätzliche Bedienfunktion | ja |
| G-14 | `EDIT` | `O` | zusätzliche Bedienfunktion | ja |
| G-14 | `EDIT` | `O` | zusätzliche Bedienfunktion | ja |
| G-14 | `EDIT` | `O` | zusätzliche Bedienfunktion | ja |
| G-15 | `EEX` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-15 | `EGV` | `C` | ROM-Index, gleicher Name | ja |
| G-15 | `EGVL` | `C` | ROM-Index, gleicher Name | ja |
| G-15 | `ELSE` | `C` | ROM-Index, gleicher Name | ja |
| G-15 | `END` | `C` | ROM-Index, gleicher Name | ja |
| G-15 | `ENDSUB` | `C` | ROM-Index, gleicher Name | ja |
| G-15 | `ENG` | `C` | ROM-Index, gleicher Name | ja |
| G-15 | `EQ` | `C` | Reservierter Variablenname | ja |
| G-15 | `EQ→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-15 | `EQNLIB` | `C` | ROM-Index, gleicher Name | ja |
| G-15 | `ERASE` | `C` | ROM-Index, gleicher Name | ja |
| G-16 | `ERASE` | `O` | ROM-Index, gleicher Name | ja |
| G-16 | `ERRM` | `C` | ROM-Index, gleicher Name | ja |
| G-16 | `ERRN` | `C` | ROM-Index, gleicher Name | ja |
| G-16 | `ERR0` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-16 | `EVAL` | `C` | ROM-Index, gleicher Name | ja |
| G-16 | `EXIT` | `O` | zusätzliche Bedienfunktion | ja |
| G-16 | `EXP` | `A` | ROM-Index, gleicher Name | ja |
| G-16 | `EXPAN` | `C` | ROM-Index, gleicher Name | ja |
| G-16 | `EXPND` | `O` | zusätzliche Bedienfunktion | ja |
| G-16 | `EXPFIT` | `C` | ROM-Index, gleicher Name | ja |
| G-16 | `EXPM` | `A` | ROM-Index, gleicher Name | ja |
| G-16 | `EXPR` | `O` | zusätzliche Bedienfunktion | ja |
| G-16 | `EXTR` | `O` | zusätzliche Bedienfunktion | ja |
| G-16 | `EYEPT` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `E^` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-17 | `E()` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-17 | `FO^` | `F` | `F0λ` – OCR/Schriftzeichen: 0/λ | nein / abweichend |
| G-17 | `FACT` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `FANNING` | `F` | ROM-Index, gleicher Name | ja |
| G-17 | `FC?` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `FC?C` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `FFT` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `FINDALARM` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `FINISH` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `FIX` | `C` | ROM-Index, gleicher Name | ja |
| G-17 | `FLOOR` | `F` | ROM-Index, gleicher Name | ja |
| G-17 | `FM,` | `O` | zusätzliche Bedienfunktion | ja |
| G-18 | `FOR` | `C` | ROM-Index, gleicher Name | ja |
| G-18 | `↩ FOR` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-18 | `↪ FOR` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-18 | `FP` | `F` | ROM-Index, gleicher Name | ja |
| G-18 | `FREE1` | `C` | ROM-Index, gleicher Name | ja |
| G-18 | `FREEZE` | `C` | ROM-Index, gleicher Name | ja |
| G-18 | `FS?` | `C` | ROM-Index, gleicher Name | ja |
| G-18 | `FS?C` | `C` | ROM-Index, gleicher Name | ja |
| G-18 | `FUNCTION` | `C` | ROM-Index, gleicher Name | ja |
| G-18 | `FV` | `C` | TVM-Systemvariable | ja |
| G-18 | `F(X)` | `O` | zusätzliche Bedienfunktion | ja |
| G-18 | `F′` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-18 | `GET` | `C` | ROM-Index, gleicher Name | ja |
| G-19 | `GETI` | `C` | ROM-Index, gleicher Name | ja |
| G-19 | `GOR` | `C` | ROM-Index, gleicher Name | ja |
| G-19 | `GO↓` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-19 | `GO→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-19 | `GRAD` | `C` | ROM-Index, gleicher Name | ja |
| G-19 | `GRAPH` | `C` | `PICTURE` – Historischer Kompatibilitätsalias | ja |
| G-19 | `GRIDMAP` | `C` | ROM-Index, gleicher Name | ja |
| G-19 | `→GROB` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-19 | `GXOR` | `C` | ROM-Index, gleicher Name | ja |
| G-19 | `*H` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-19 | `HALT` | `C` | ROM-Index, gleicher Name | ja |
| G-19 | `HEAD` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `HEX` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `HISTOGRAM` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `HISTPLOT` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `HMS+` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `HMS−` | `C` | `HMS-` – Unicode Minuszeichen | nein / abweichend |
| G-20 | `HMS→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-20 | `→HMS` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-20 | `HOME` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `HZIN` | `O` | zusätzliche Bedienfunktion | ja |
| G-20 | `HZOUT` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-20 | `i` | `F` | ROM-Index, gleicher Name | ja |
| G-20 | `IDN` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `IF` | `C` | ROM-Index, gleicher Name | ja |
| G-20 | `↩ IF` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-20 | `↪ IF` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-21 | `IFERR` | `C` | ROM-Index, gleicher Name | ja |
| G-21 | `↩ IFERR` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-21 | `↪ IFERR` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-21 | `IFFT` | `C` | ROM-Index, gleicher Name | ja |
| G-21 | `IFT` | `C` | ROM-Index, gleicher Name | ja |
| G-21 | `IFTE` | `F` | ROM-Index, gleicher Name | ja |
| G-21 | `IM` | `F` | ROM-Index, gleicher Name | ja |
| G-21 | `INCR` | `C` | ROM-Index, gleicher Name | ja |
| G-21 | `INDEP` | `C` | ROM-Index, gleicher Name | ja |
| G-21 | `INFO` | `O` | zusätzliche Bedienfunktion | ja |
| G-22 | `INFO` | `O` | zusätzliche Bedienfunktion | ja |
| G-22 | `INFO?` | `O` | zusätzliche Bedienfunktion | ja |
| G-22 | `INFORM` | `C` | ROM-Index, gleicher Name | ja |
| G-22 | `INIT+` | `O` | zusätzliche Bedienfunktion | ja |
| G-22 | `INPUT` | `C` | ROM-Index, gleicher Name | ja |
| G-22 | `INS` | `O` | zusätzliche Bedienfunktion | ja |
| G-22 | `INV` | `A` | ROM-Index, gleicher Name | ja |
| G-22 | `IOPAR` | `C` | Reservierter Variablenname | ja |
| G-22 | `IP` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-22 | `ISECT` | `O` | zusätzliche Bedienfunktion | ja |
| G-22 | `ISOL` | `C` | ROM-Index, gleicher Name | ja |
| G-22 | `KEEP` | `O` | zusätzliche Bedienfunktion | ja |
| G-23 | `KERRM` | `C` | ROM-Index, gleicher Name | ja |
| G-23 | `KEY` | `C` | ROM-Index, gleicher Name | ja |
| G-23 | `KGET` | `C` | ROM-Index, gleicher Name | ja |
| G-23 | `KILL` | `C` | ROM-Index, gleicher Name | ja |
| G-23 | `LABEL` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-23 | `LABEL` | `O` | ROM-Index, gleicher Name | nein / abweichend |
| G-23 | `LAST` | `C` | `LASTARG` – Historisches Alias | ja |
| G-23 | `LASTARG` | `C` | ROM-Index, gleicher Name | ja |
| G-23 | `LCD→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-23 | `→LCD` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-23 | `LEVEL` | `O` | zusätzliche Bedienfunktion | ja |
| G-23 | `LIBEVAL` | `C` | ROM-Index, gleicher Name | ja |
| G-23 | `LIBS` | `C` | ROM-Index, gleicher Name | ja |
| G-23 | `LINE` | `C` | ROM-Index, gleicher Name | ja |
| G-24 | `LINE` | `O` | ROM-Index, gleicher Name | ja |
| G-24 | `ΣLINE` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `LINFIT` | `C` | ROM-Index, gleicher Name | ja |
| G-24 | `LININ` | `F` | ROM-Index, gleicher Name | ja |
| G-24 | `LIST→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `→LIST` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `→LIST` | `O` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `ΣLIST` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `ΠLIST` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `ΔLIST` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `LN` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-24 | `LNP1` | `A` | ROM-Index, gleicher Name | ja |
| G-24 | `LOG` | `A` | ROM-Index, gleicher Name | ja |
| G-25 | `LOGFIT` | `C` | ROM-Index, gleicher Name | ja |
| G-25 | `LQ` | `C` | ROM-Index, gleicher Name | ja |
| G-25 | `LR` | `C` | ROM-Index, gleicher Name | ja |
| G-25 | `LSQ` | `C` | ROM-Index, gleicher Name | ja |
| G-25 | `LU` | `C` | ROM-Index, gleicher Name | ja |
| G-25 | `L*` | `O` | zusätzliche Bedienfunktion | ja |
| G-25 | `L()` | `O` | zusätzliche Bedienfunktion | ja |
| G-25 | `←M` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-25 | `↪←M` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-25 | `M→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-25 | `↪M→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-25 | `MANT` | `F` | ROM-Index, gleicher Name | ja |
| G-26 | `MARK` | `O` | zusätzliche Bedienfunktion | ja |
| G-26 | `MATCH` | `O` | zusätzliche Bedienfunktion | ja |
| G-26 | `↑MATCH` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-26 | `↓MATCH` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-26 | `MAX` | `F` | ROM-Index, gleicher Name | ja |
| G-26 | `MAXR` | `F` | ROM-Index, gleicher Name | ja |
| G-26 | `MAXΣ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-26 | `MCALC` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-26 | `MEAN` | `C` | ROM-Index, gleicher Name | ja |
| G-26 | `MEM` | `C` | ROM-Index, gleicher Name | ja |
| G-26 | `MENU` | `C` | ROM-Index, gleicher Name | ja |
| G-27 | `MENU` | `O` | ROM-Index, gleicher Name | ja |
| G-27 | `MERGE1` | `C` | ROM-Index, gleicher Name | ja |
| G-27 | `MIN` | `F` | ROM-Index, gleicher Name | ja |
| G-27 | `MINEHUNT` | `C` | ROM-Index, gleicher Name | ja |
| G-27 | `MINIT` | `C` | ROM-Index, gleicher Name | ja |
| G-27 | `MINR` | `F` | ROM-Index, gleicher Name | ja |
| G-27 | `MINΣ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-27 | `MITM` | `C` | ROM-Index, gleicher Name | ja |
| G-27 | `ML` | `O` | zusätzliche Bedienfunktion | ja |
| G-27 | `MOD` | `F` | ROM-Index, gleicher Name | ja |
| G-27 | `MOVE` | `O` | zusätzliche Bedienfunktion | ja |
| G-27 | `MSGBOX` | `C` | ROM-Index, gleicher Name | ja |
| G-28 | `MROOT` | `C` | ROM-Index, gleicher Name | ja |
| G-28 | `MSOLVR` | `C` | ROM-Index, gleicher Name | ja |
| G-28 | `MUSER` | `C` | ROM-Index, gleicher Name | ja |
| G-28 | `NDIST` | `C` | ROM-Index, gleicher Name | ja |
| G-28 | `NΣ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-28 | `NEG` | `A` | ROM-Index, gleicher Name | ja |
| G-28 | `NEW` | `O` | zusätzliche Bedienfunktion | ja |
| G-28 | `NEW` | `O` | zusätzliche Bedienfunktion | ja |
| G-28 | `NEWOB` | `C` | ROM-Index, gleicher Name | ja |
| G-28 | `NEXT` | `C` | ROM-Index, gleicher Name | ja |
| G-28 | `NEXT` | `O` | ROM-Index, gleicher Name | ja |
| G-29 | `NOT` | `C/F` | ROM-Index, gleicher Name | ja |
| G-29 | `NOVAL` | `C` | ROM-Index, gleicher Name | ja |
| G-29 | `NSUB` | `C` | ROM-Index, gleicher Name | ja |
| G-29 | `NUM` | `C` | ROM-Index, gleicher Name | ja |
| G-29 | `NUMX` | `C` | ROM-Index, gleicher Name | ja |
| G-29 | `NUMY` | `C` | ROM-Index, gleicher Name | ja |
| G-29 | `→NUM` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-29 | `NXEQ` | `O` | zusätzliche Bedienfunktion | ja |
| G-29 | `OBJ→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-29 | `OCT` | `C` | ROM-Index, gleicher Name | ja |
| G-29 | `OFF` | `C` | ROM-Index, gleicher Name | ja |
| G-30 | `OK` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-30 | `OLDPRT` | `C` | ROM-Index, gleicher Name | ja |
| G-30 | `OPENIO` | `C` | ROM-Index, gleicher Name | ja |
| G-30 | `OPTS` | `O` | zusätzliche Bedienfunktion | ja |
| G-30 | `OR` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-30 | `ORDER` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-30 | `OVER` | `C` | ROM-Index, gleicher Name | ja |
| G-30 | `ΣPAR` | `C` | Reservierter Variablenname | nein / abweichend |
| G-30 | `PARAMETRIC` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-30 | `PARITY` | `C` | ROM-Index, gleicher Name | ja |
| G-30 | `PARSURFACE` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-30 | `PATH` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PCOEF` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PCONTOUR` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PCOV` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PDIM` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PERM` | `F` | ROM-Index, gleicher Name | ja |
| G-31 | `PEVAL` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PGDIR` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PICK` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PICK` | `O` | ROM-Index, gleicher Name | ja |
| G-31 | `PICT` | `C` | ROM-Index, gleicher Name | ja |
| G-31 | `PICT→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-31 | `PICTURE` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PINIT` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PIXOFF` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PIXON` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PIX?` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PKT` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PMAX` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PMIN` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PMT` | `C` | TVM-Systemvariable | ja |
| G-32 | `POLAR` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `POS` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PRED` | `O` | zusätzliche Bedienfunktion | ja |
| G-32 | `PREDV` | `C` | ROM-Index, gleicher Name | ja |
| G-32 | `PREDX` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PREDY` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PRINT` | `O` | zusätzliche Bedienfunktion | ja |
| G-33 | `PRLCD` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PROMPT` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PROOT` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PRST` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PRSTC` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PRTPAR` | `C` | Reservierter Variablenname | ja |
| G-33 | `PRVAR` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PR1` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PSDEV` | `C` | ROM-Index, gleicher Name | ja |
| G-33 | `PURGE` | `C` | ROM-Index, gleicher Name | ja |
| G-34 | `PURG` | `C/O` | `PURGE` – Menübezeichnung; selbstständige Wirkung prüfen | ja |
| G-34 | `PUT` | `C` | ROM-Index, gleicher Name | ja |
| G-34 | `PUTI` | `C` | ROM-Index, gleicher Name | ja |
| G-34 | `PV` | `C` | TVM-Systemvariable | nein / abweichend |
| G-34 | `PVAR` | `C` | ROM-Index, gleicher Name | ja |
| G-34 | `PVARS` | `C` | ROM-Index, gleicher Name | ja |
| G-34 | `PVIEW` | `C` | ROM-Index, gleicher Name | ja |
| G-34 | `PWRFIT` | `C` | ROM-Index, gleicher Name | ja |
| G-34 | `PYR` | `C` | TVM-Systemvariable | ja |
| G-34 | `PX→C` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-34 | `→Q` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-34 | `QR` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-35 | `QUAD` | `C` | ROM-Index, gleicher Name | ja |
| G-35 | `QUOTE` | `F` | ROM-Index, gleicher Name | ja |
| G-35 | `→Qπ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-35 | `RAD` | `C` | ROM-Index, gleicher Name | ja |
| G-35 | `RAND` | `C` | ROM-Index, gleicher Name | ja |
| G-35 | `RANK` | `C` | ROM-Index, gleicher Name | ja |
| G-35 | `RANM` | `C` | ROM-Index, gleicher Name | ja |
| G-35 | `RATIO` | `F` | ROM-Index, gleicher Name | ja |
| G-35 | `RCEQ` | `C` | ROM-Index, gleicher Name | ja |
| G-35 | `RCI` | `C` | ROM-Index, gleicher Name | ja |
| G-35 | `RCIJ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-35 | `RCL` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RCL` | `O` | ROM-Index, gleicher Name | ja |
| G-36 | `RCLALARM` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RCLF` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RCLKEYS` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RCLMENU` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RCLΣ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-36 | `RCWS` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RDM` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RDZ` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RE` | `F` | ROM-Index, gleicher Name | ja |
| G-36 | `RECN` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RECT` | `C` | ROM-Index, gleicher Name | ja |
| G-36 | `RECV` | `C` | ROM-Index, gleicher Name | ja |
| G-37 | `RECV` | `O` | ROM-Index, gleicher Name | ja |
| G-37 | `REPEAT` | `C` | ROM-Index, gleicher Name | ja |
| G-37 | `REPL` | `C` | ROM-Index, gleicher Name | ja |
| G-37 | `REPL` | `O` | ROM-Index, gleicher Name | ja |
| G-37 | `REPL` | `O` | ROM-Index, gleicher Name | ja |
| G-37 | `RES` | `C` | ROM-Index, gleicher Name | ja |
| G-37 | `RESET` | `O` | zusätzliche Bedienfunktion | ja |
| G-37 | `RESET` | `O` | zusätzliche Bedienfunktion | ja |
| G-37 | `RESTORE` | `C` | ROM-Index, gleicher Name | ja |
| G-37 | `REVLIST` | `C` | ROM-Index, gleicher Name | ja |
| G-38 | `RKF` | `C` | ROM-Index, gleicher Name | ja |
| G-38 | `RKFERR` | `C` | ROM-Index, gleicher Name | ja |
| G-38 | `RKFSTEP` | `C` | ROM-Index, gleicher Name | ja |
| G-38 | `RL` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-38 | `RLB` | `C` | ROM-Index, gleicher Name | ja |
| G-38 | `RND` | `F` | ROM-Index, gleicher Name | ja |
| G-38 | `RNRM` | `C` | ROM-Index, gleicher Name | ja |
| G-38 | `ROLL` | `C` | ROM-Index, gleicher Name | ja |
| G-38 | `ROLL` | `O` | ROM-Index, gleicher Name | ja |
| G-39 | `ROLLD` | `C` | ROM-Index, gleicher Name | ja |
| G-39 | `ROLLD` | `O` | ROM-Index, gleicher Name | ja |
| G-39 | `ROOT` | `C` | ROM-Index, gleicher Name | ja |
| G-39 | `ROOT` | `O` | ROM-Index, gleicher Name | ja |
| G-39 | `ROT` | `C` | ROM-Index, gleicher Name | ja |
| G-39 | `ROW+` | `C` | ROM-Index, gleicher Name | ja |
| G-39 | `+ROW` | `O` | zusätzliche Bedienfunktion | ja |
| G-39 | `ROW−` | `C` | `ROW-` – Unicode Minuszeichen | nein / abweichend |
| G-39 | `−ROW` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-39 | `→ROW` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-39 | `ROW→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-39 | `RR` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `RRB` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `RREF` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `RRK` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `RRKSTEP` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `RSBERR` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `RSD` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `RSWP` | `C` | ROM-Index, gleicher Name | ja |
| G-40 | `R→B` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-41 | `R→C` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-41 | `R→D` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-41 | `SAME` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SBRK` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SCALE` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SCATRPLOT` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SCATTER` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SCHUR` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SCI` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-41 | `SCLS` | `C` | `SCLΣ` – OCR/Schriftzeichen: Σ (AUR 3-299) | nein / abweichend |
| G-41 | `SCONJ` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SDEV` | `C` | ROM-Index, gleicher Name | ja |
| G-41 | `SEND` | `C` | ROM-Index, gleicher Name | ja |
| G-42 | `SEND` | `O` | ROM-Index, gleicher Name | ja |
| G-42 | `SEQ` | `C` | ROM-Index, gleicher Name | ja |
| G-42 | `SERVER` | `C` | ROM-Index, gleicher Name | ja |
| G-42 | `SF` | `C` | ROM-Index, gleicher Name | ja |
| G-42 | `SHADE` | `O` | zusätzliche Bedienfunktion | ja |
| G-42 | `SHOW` | `C` | ROM-Index, gleicher Name | ja |
| G-42 | `SIDENS` | `F` | ROM-Index, gleicher Name | ja |
| G-42 | `SIGN` | `F` | ROM-Index, gleicher Name | ja |
| G-42 | `SIMU` | `O` | zusätzliche Bedienfunktion | ja |
| G-42 | `SIN` | `A` | ROM-Index, gleicher Name | ja |
| G-42 | `SINH` | `A` | ROM-Index, gleicher Name | ja |
| G-42 | `SINV` | `C` | ROM-Index, gleicher Name | ja |
| G-43 | `SIZE` | `C` | ROM-Index, gleicher Name | ja |
| G-43 | `SIZE` | `O` | ROM-Index, gleicher Name | ja |
| G-43 | `←SKIP` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-43 | `SKIP→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-43 | `SL` | `C` | ROM-Index, gleicher Name | ja |
| G-43 | `SLB` | `C` | ROM-Index, gleicher Name | ja |
| G-43 | `SLOPE` | `O` | zusätzliche Bedienfunktion | ja |
| G-43 | `SLOPEFIELD` | `C` | ROM-Index, gleicher Name | ja |
| G-43 | `SNEG` | `C` | ROM-Index, gleicher Name | ja |
| G-43 | `SNRM` | `C` | ROM-Index, gleicher Name | ja |
| G-43 | `SOLVE` | `O` | zusätzliche Bedienfunktion | ja |
| G-43 | `SOLVEQN` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `SORT` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `SPHERE` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `SQ` | `A` | ROM-Index, gleicher Name | ja |
| G-44 | `SR` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `SRAD` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `SRB` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `SRECV` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `SST` | `O` | zusätzliche Bedienfunktion | ja |
| G-44 | `SST↓` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-44 | `START` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `↩ START` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-44 | `↪ START` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-44 | `STD` | `C` | ROM-Index, gleicher Name | ja |
| G-44 | `STEP` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `STEP` | `O` | ROM-Index, gleicher Name | ja |
| G-45 | `STEQ` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `STIME` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `↑STK` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-45 | `→STK` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-45 | `→STK` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-45 | `STO` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `STOALARM` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `STOF` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `STOKEYS` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `STO+` | `C` | ROM-Index, gleicher Name | ja |
| G-45 | `STO−` | `C` | `STO-` – Unicode Minuszeichen | nein / abweichend |
| G-46 | `STO*` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-46 | `STO/` | `C` | ROM-Index, gleicher Name | ja |
| G-46 | `STOΣ` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-46 | `STR→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-46 | `→STR` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-46 | `STREAM` | `C` | ROM-Index, gleicher Name | ja |
| G-46 | `STS` | `O` | zusätzliche Bedienfunktion | ja |
| G-46 | `STWS` | `C` | ROM-Index, gleicher Name | ja |
| G-46 | `SUB` | `C` | ROM-Index, gleicher Name | ja |
| G-46 | `SUB` | `O` | ROM-Index, gleicher Name | ja |
| G-46 | `SUB` | `O` | ROM-Index, gleicher Name | ja |
| G-47 | `SVD` | `C` | ROM-Index, gleicher Name | ja |
| G-47 | `SVL` | `C` | ROM-Index, gleicher Name | ja |
| G-47 | `SWAP` | `C` | ROM-Index, gleicher Name | ja |
| G-47 | `SYM` | `O` | zusätzliche Bedienfunktion | ja |
| G-47 | `SYSEVAL` | `C` | ROM-Index, gleicher Name | ja |
| G-47 | `←T` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-47 | `↪←T` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-47 | `T→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-47 | `↪T→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-47 | `%T` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-47 | `→TAG` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-47 | `TAN` | `A` | ROM-Index, gleicher Name | ja |
| G-47 | `TAIL` | `C` | ROM-Index, gleicher Name | ja |
| G-48 | `TANH` | `A` | ROM-Index, gleicher Name | ja |
| G-48 | `TANL` | `O` | zusätzliche Bedienfunktion | ja |
| G-48 | `TAYLR` | `C` | ROM-Index, gleicher Name | ja |
| G-48 | `TDELTA` | `F` | ROM-Index, gleicher Name | ja |
| G-48 | `TEACH` | `C` | ROM-Index, gleicher Name | ja |
| G-48 | `TEXT` | `C` | ROM-Index, gleicher Name | ja |
| G-48 | `THEN` | `C` | ROM-Index, gleicher Name | ja |
| G-48 | `TICKS` | `C` | ROM-Index, gleicher Name | ja |
| G-48 | `TIME` | `C` | ROM-Index, gleicher Name | ja |
| G-48 | `→TIME` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-48 | `TINC` | `F` | ROM-Index, gleicher Name | ja |
| G-49 | `TLINE` | `C` | ROM-Index, gleicher Name | ja |
| G-49 | `TLINE` | `O` | ROM-Index, gleicher Name | ja |
| G-49 | `TMENU` | `C` | ROM-Index, gleicher Name | ja |
| G-49 | `TOT` | `C` | ROM-Index, gleicher Name | ja |
| G-49 | `TRACE` | `C` | ROM-Index, gleicher Name | ja |
| G-49 | `TRACE` | `O` | ROM-Index, gleicher Name | ja |
| G-49 | `TRANSIO` | `C` | ROM-Index, gleicher Name | ja |
| G-49 | `TRG*` | `O` | zusätzliche Bedienfunktion | ja |
| G-49 | `→TRG` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-49 | `TRN` | `C` | ROM-Index, gleicher Name | ja |
| G-49 | `TRNC` | `F` | ROM-Index, gleicher Name | ja |
| G-49 | `TRUTH` | `C` | ROM-Index, gleicher Name | ja |
| G-49 | `TSTR` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `TVARS` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `TVM` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `TVMBEG` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `TVMEND` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `TVMROOT` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `TYPE` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `TYPES` | `O` | zusätzliche Bedienfunktion | ja |
| G-50 | `UBASE` | `F` | ROM-Index, gleicher Name | ja |
| G-50 | `UFACT` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `→UNIT` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-50 | `UNTIL` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `UPDIR` | `C` | ROM-Index, gleicher Name | ja |
| G-50 | `UTPC` | `C` | ROM-Index, gleicher Name | ja |
| G-51 | `UTPF` | `C` | ROM-Index, gleicher Name | ja |
| G-51 | `UTPN` | `C` | ROM-Index, gleicher Name | ja |
| G-51 | `UTPT` | `C` | ROM-Index, gleicher Name | ja |
| G-51 | `UVAL` | `F` | ROM-Index, gleicher Name | ja |
| G-51 | `VAR` | `C` | ROM-Index, gleicher Name | ja |
| G-51 | `VARS` | `C` | ROM-Index, gleicher Name | ja |
| G-51 | `VEC` | `O` | zusätzliche Bedienfunktion | ja |
| G-51 | `VIEW` | `O` | zusätzliche Bedienfunktion | ja |
| G-51 | `↪ VIEW` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-51 | `VIEW` | `O` | zusätzliche Bedienfunktion | ja |
| G-51 | `VPAR` | `C` | Reservierter Variablenname | ja |
| G-52 | `VTYPE` | `C` | ROM-Index, gleicher Name | ja |
| G-52 | `VZIN` | `O` | zusätzliche Bedienfunktion | ja |
| G-52 | `VZOUT` | `O` | zusätzliche Bedienfunktion | ja |
| G-52 | `→V2` | `O` | ROM-Index, gleicher Name | nein / abweichend |
| G-52 | `→V3` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-52 | `V→` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-52 | `*W` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-52 | `WAIT` | `C` | ROM-Index, gleicher Name | ja |
| G-52 | `WHILE` | `C` | ROM-Index, gleicher Name | ja |
| G-52 | `↩ WHILE` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-52 | `WID→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-52 | `←WID` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-52 | `WIREFRAME` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-53 | `WSLOG` | `C` | ROM-Index, gleicher Name | ja |
| G-53 | `ΣX` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-53 | `ΣX^2` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-53 | `XCOL` | `C` | ROM-Index, gleicher Name | ja |
| G-53 | `XMIT` | `C` | ROM-Index, gleicher Name | ja |
| G-53 | `XOR` | `F` | ROM-Index, gleicher Name | ja |
| G-53 | `XPON` | `F` | ROM-Index, gleicher Name | ja |
| G-53 | `XRECV` | `C` | ROM-Index, gleicher Name | ja |
| G-53 | `XRNG` | `C` | ROM-Index, gleicher Name | ja |
| G-53 | `XROOT` | `A` | ROM-Index, gleicher Name | ja |
| G-53 | `XSEND` | `C` | ROM-Index, gleicher Name | ja |
| G-53 | `XVOL` | `C` | ROM-Index, gleicher Name | ja |
| G-54 | `XXRNG` | `C` | ROM-Index, gleicher Name | ja |
| G-54 | `ΣX*Y` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-54 | `(X,Y)` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-54 | `X,Y→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-54 | `ΣY` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-54 | `ΣY^2` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-54 | `YCOL` | `C` | ROM-Index, gleicher Name | ja |
| G-54 | `YRNG` | `C` | ROM-Index, gleicher Name | ja |
| G-54 | `YSLICE` | `C` | ROM-Index, gleicher Name | ja |
| G-54 | `YVOL` | `C` | ROM-Index, gleicher Name | ja |
| G-55 | `YYRNG` | `C` | ROM-Index, gleicher Name | ja |
| G-55 | `ZAUTO` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZDECI` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZDFLT` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZFACT` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZFACTOR` | `F` | ROM-Index, gleicher Name | ja |
| G-55 | `ZIN` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZINTG` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZLAST` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZOOM` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZOUT` | `O` | zusätzliche Bedienfunktion | ja |
| G-55 | `ZSQR` | `O` | zusätzliche Bedienfunktion | ja |
| G-56 | `ZTRIG` | `O` | zusätzliche Bedienfunktion | ja |
| G-56 | `ZVOL` | `C` | ROM-Index, gleicher Name | ja |
| G-56 | `+` | `A` | ROM-Index, gleicher Name | ja |
| G-56 | `+/−` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-56 | `+1−1` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-56 | `−` | `A` | `-` – Schreibvariante | nein / abweichend |
| G-56 | `−()` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-56 | `*` | `A` | ROM-Index, gleicher Name | ja |
| G-56 | `*1` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-56 | `/` | `A` | ROM-Index, gleicher Name | ja |
| G-56 | `/1` | `O` | zusätzliche Bedienfunktion | ja |
| G-56 | `^` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-56 | `^1` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-57 | `<` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `≤` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `>` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `≥` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `=` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `==` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `≠` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `!` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `∫` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `∂` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `%` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `π` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-57 | `Σ` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-58 | `Σ+` | `C` | ROM-Index, gleicher Name | nein / abweichend |
| G-58 | `Σ−` | `C` | `Σ-` – Unicode Minuszeichen | nein / abweichend |
| G-58 | `√` | `A` | ROM-Index, gleicher Name | nein / abweichend |
| G-58 | `\|` | `F` | ROM-Index, gleicher Name | nein / abweichend |
| G-58 | `1/()` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-58 | `(())` | `O` | zusätzliche Bedienfunktion | ja |
| G-58 | `(←` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-58 | `↪ (←` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-58 | `→()` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-58 | `→)` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-58 | `↪ →)` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-58 | `←→` | `O` | zusätzliche Bedienfunktion | nein / abweichend |
| G-58 | `→` | `C` | ROM-Index, gleicher Name | nein / abweichend |

## Zusätzliche, wörtlich nicht im ROM-Index auftretende programmierbare Originalbezeichnungen

**Wichtig:** Anders als die 517 ROM-Namen ist diese Liste eine **Differenz**, nicht notwendigerweise eine Liste zusätzlicher reiner Maschinenbefehle. `CLUSR` / `LAST` und `GRAPH` sind klassische Aliase/Kompatibilitätszugänge. Reservierte Variablen sind getrennte Datenobjekte.

| Name aus HP-Index | Vorgeschlagene kanonische Zuordnung | Begründung / Prüfung |
| --- | --- | --- |
| `−` | `-` | Schreibvariante |
| `BUF LEN` | `BUFLEN` | Schreibvariante |
| `CASE / ↩CASE / ↪CASE` | `CASE` | Sammelzeile: C/O/O |
| `CLS` | `CLΣ` | OCR/Schriftzeichen: Σ |
| `CLUSR` | `CLVAR` | Historisches Alias (AUR 3-52) |
| `COL−` | `COL-` | Unicode Minuszeichen |
| `CST` | kein zusätzlicher ROM-Name | Reservierter Variablenname |
| `EQ` | kein zusätzlicher ROM-Name | Reservierter Variablenname |
| `FO^` | `F0λ` | OCR/Schriftzeichen: 0/λ |
| `FV` | kein zusätzlicher ROM-Name | TVM-Systemvariable |
| `GRAPH` | `PICTURE` | Historischer Kompatibilitätsalias |
| `HMS−` | `HMS-` | Unicode Minuszeichen |
| `IOPAR` | kein zusätzlicher ROM-Name | Reservierter Variablenname |
| `LAST` | `LASTARG` | Historisches Alias |
| `PMT` | kein zusätzlicher ROM-Name | TVM-Systemvariable |
| `PRTPAR` | kein zusätzlicher ROM-Name | Reservierter Variablenname |
| `PURG` | `PURGE` | Menübezeichnung; selbstständige Wirkung prüfen |
| `PV` | kein zusätzlicher ROM-Name | TVM-Systemvariable |
| `PYR` | kein zusätzlicher ROM-Name | TVM-Systemvariable |
| `ROW−` | `ROW-` | Unicode Minuszeichen |
| `SCLS` | `SCLΣ` | OCR/Schriftzeichen: Σ (AUR 3-299) |
| `STO−` | `STO-` | Unicode Minuszeichen |
| `VPAR` | kein zusätzlicher ROM-Name | Reservierter Variablenname |
| `Σ−` | `Σ-` | Unicode Minuszeichen |
| `ΣDAT` | kein zusätzlicher ROM-Name | Reservierter Variablenname |
| `ΣPAR` | kein zusätzlicher ROM-Name | Reservierter Variablenname |

## Durchgeführte und noch erforderliche Kontrollen

- [x] G-1 als Klassifikationslegende erfasst; G-2 bis G-58 sämtlich als unterschiedliche Tabellen-Seiten übernommen.
- [x] Alle `696` erfassten Tabellenzeilen besitzen Druckseitenangabe, HP-Klasse, Namen und Kontextprüfung gegen ROM (direkter Namensvergleich/ausgewiesener Alias).
- [x] Exaktes Erkennen durch den **separaten** Scan-OCR-Durchlauf pro Zeile separat markiert; **keine** erfundenen OCR-Hits für G-57.
- [ ] Jede Zeile optisch am Scan gegenprüfen; hoch- und tiefgestellte Zeichen, Pfeile, Minuszeichen und Σ gesondert bestätigen.
- [ ] Jede User-RPL-Befehlsreferenz aus der *Advanced User's Reference* unabhängig mit Stack- und Fehlersemantik abgleichen.
- [ ] Unterschiede der G/GX-ROM-Revisionen und Anzeige-/Tastenkontexte per Gerät/Emulator prüfen.
- [ ] Alle 315 eingebauten Gleichungen, 396 Variablenbeziehungen, Einheiten-/Konstantentabellen gesondert prüfen.

**Abnahmeentscheidung:** Diese Dateifassung ist **kein Nachweis einer vollständigen historischen Funktionssemantik**, sondern der abschließende **Index-Zeilenabgleich im vorliegenden auslesbaren Originalformat**. Die globalen Abnahmekriterien bleiben im [Vollständigkeitsaudit](HP-48GX-VOLLSTAENDIGKEITSAUDIT.md) offen.
