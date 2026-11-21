# Decisions not to pre-empt — architecture register supplement

**Do not reopen whether full vintage emulation must block V1.0: it does not.** This register lists the *real* dependencies a developer must settle, and which questions are deliberately deferred.

**V1 decision drafts now exist:** [candidate key/function matrix](../de/V1-FUNKTIONS-UND-TASTATURMATRIX.md), [four ADRs](../adr/README.md) and [V1 test/release plan](../de/V1-TEST-UND-FREIGABEPLAN.md). They are **PROPOSED (not ACCEPTED)**; missing signatures, exact key positions, numeric precision and real iPhone XS evidence remain open.

## Must decide before building the corresponding early component

| Key | Scope | Required output |
| --- | --- | --- |
| DQ-01 | Classic RPN V1 | Key/shift/alpha inventory, stack lift and ENTER/LAST-X state transition tables |
| DQ-02 | Numeric V1 | Precision/rounding/overflow, trig degrees/radians and error taxonomy |
| DQ-03 | Persistence V1 | Versioned snapshots, corrupted state recovery, storage and migration |
| DQ-04 | iPhone V1 | iPhone XS deployment target, device-testing method, native bridge, SASD official URL |
| DQ-05 | Stand-alone ALG | Pratt binding powers, minus/power syntax, decimal separator and symbol/side-effect rules |
| DQ-06 | Public Mathematical Core | Type/number contracts and supported C++ package reuse |
| DQ-07 | Independent app releases | Bundle IDs, version tags, build target naming and App Store product positioning |

## Deliberately deferred until corresponding historical milestone

| Key | Deferred item | Earliest phase |
| --- | --- | --- |
| DH-01 | 41 FOCAL completeness, 56-bit raw register ordering, bytecode layout and import formats | M3, architectural seam earlier |
| DH-02 | Synthetic command A/B compatibility corpus, Byte Grabber C scope | M4 / optional C |
| DH-03 | 48 RPL object/nibble codecs and ROM-compatible memory mapping | M3, seam earlier |
| DH-04 | First ROM profile, SYSEVAL/LIBEVAL supported identifiers and system primitives | M4 |
| DH-05 | Strict Historical memory reporting, storage allocation and card matrix | M3/M4 |
| DH-06 | Nut/Saturn CPU emulation, native historical OS and machine programs | M5 optional |
| DH-07 | Advantage-Pac-era complete historical XROM compatibility vs function-inspired add-on | Post-M2 |
| DH-08 | Financial package extraction and Financial repository creation | When second consumer starts |

Any decision change requires date, rationale, affected requirements, tests, release impact and explicit stakeholder sign-off; don't turn a planned capability into a fake implemented one.
