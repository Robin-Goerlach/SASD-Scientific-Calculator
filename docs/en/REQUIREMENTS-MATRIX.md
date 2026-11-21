# Requirements baseline and traceability — 2026-11-21

**Normative planning baseline; not an implementation claim.** This document reconciles the November 2026 decisions. **M0–M5 are delivery milestones; K1–K4 are compatibility levels.** A goal may be mandatory in the long term without being a V1.0 release gate. A feature is never "supported" merely because it has a row in this file.

## Priority, status and evidence

- **V1/P0:** Must be demonstrably complete before the *first classic iPhone RPN app* is called V1.0.
- **Architecture/P0:** Establish a boundary now; implementing the feature may be delayed.
- **Long-term committed:** An agreed project objective, with its own acceptance suite and later scope gate; **not** a V1 obligation.
- **Planned:** Intention or recommended delivery; precise schedule/scope remains open.
- **Optional:** No implementation obligation without a new decision.
- **Implemented / tested:** Must be tied to source, tests and run evidence; no historic compatibility is currently certified.

## V1.0 classic scientific calculator — proposed measurable acceptance contract

| ID | Priority | Requirement | Acceptance / evidence | Current state |
| --- | --- | --- | --- | --- |
| V1-F001 | V1/P0 | Historical-style classic RPN input with ENTER and documented input state | Key-sequence/state golden tests | Planned |
| V1-F002 | V1/P0 | Deterministic X/Y/Z/T-oriented stack semantics and stack manipulation per approved profile | Explicit stack-lift/drop, LAST X and error transition tests | Planned |
| V1-F003 | V1/P0 | +, −, ×, ÷ with operand order and domain errors | Automated numerical, state-preservation and boundary tests | Generic arithmetic slice only |
| V1-F004 | V1/P0 | Powers, roots, reciprocal and sign handling in approved key map | Golden/domain/error tests | Planned |
| V1-F005 | V1/P0 | Trigonometric operations, angle modes and inverses per approved key map | Degree/radian/reference tests | Planned |
| V1-F006 | V1/P0 | Logarithms and exponential operations | Representative precision/domain tests | Planned |
| V1-F007 | V1/P0 | Memory registers and recall/store semantics | Register/state tests | Planned |
| V1-F008 | V1/P0 | Defined numeric precision, display rounding and robust errors | Precision specification and regression suite | Decision open |
| V1-F009 | V1/P0 | Versioned state snapshot, restart and upgrade handling | Relaunch/corruption/migration tests | Planned |
| V1-F010 | V1/P0 | Touch-friendly, complete agreed calculator view for iPhone XS | Physical-device visual, interaction and accessibility tests | Planned |
| V1-F011 | V1/P0 | Full calculation without network, ads, accounts or subscription | Airplane-mode/device/package verification | Planned |
| V1-F012 | V1/P0 | Discreet top-left clickable SASD label | UI and accessibility verification; official URL approved | Planned |
| V1-F013 | V1/P0 | Release honestly describes supported functions and historical limits | Version-specific feature matrix and release checklist | Planned |
| V1-F014 | V1/P0 | Minimal bundled help for calculator operation and errors | Offline access to help for all approved V1 keys | Planned |
| V1-N001 | V1/P0 | Portable C++20 domain core and deterministic tests | CMake/CTest on 3 OS; iOS integration separately tested | Foundation implemented |
| V1-N002 | V1/P0 | Frontend contains no independent arithmetic/state semantics | Dependency/architecture review and UI integration tests | Architecture decided |
| V1-N003 | V1/P0 | Native bridge manages lifetimes/errors without STL ABI leakage | C-ABI contract tests | Planned |
| V1-N004 | V1/P0 | No known critical calculation, crash or state-loss defect | Signed-off release test report | Planned |

**Scope freeze before implementation:** approve exact key map, four-level stack operations (including ENTER/LAST X), numerical type and precision, V1 functions, iPhone deployment target and state schema. Generated concept art is never an authoritative key specification.

## Cross-cutting, separately releasable product architecture

| ID | Status | Requirement |
| --- | --- | --- |
| SCI-MULTI-001 | Architecture/P0 | A stand-alone ALG scientific app and independent classic RPN and advanced RPL app targets are allowed inside this Scientific monorepo. |
| SCI-MULTI-002 | Architecture/P0 | A single UI-neutral expression parser can serve ALG app and optional algebraic input on family profiles; no forced sharing of historical interpreters. |
| SCI-MULTI-003 | Architecture/P0 | Share compatible mathematical algorithms and test infrastructure; historic number, error, stack and object semantics remain model-specific. |
| SCI-MULTI-004 | Architecture/P0 | An ALG app has its own modern calculator context; it never needs a 41/48 legacy interpreter at runtime. |
| SCI-MULTI-005 | Architecture/P0 | Scientific apps may have separate build IDs, versions and releases; one app must not block another. |
| SCI-PROD-001 | Decided | Scientific and Financial are different products, GitHub repositories and release trains; **Scientific first, Financial parallel**. |
| SCI-PROD-002 | Decided | Reuse via stable versioned C++-usable components when warranted; copied source is permitted with provenance, license, version and maintenance plan. |
| SCI-PROD-003 | Decided | Financial TVM, annuities, cashflow, NPV/IRR, depreciation and bonds remain Financial-domain requirements, not Scientific V1 gates. |
| SCI-ALG-001 | Committed for ALG track | Parse infix expressions with precedence, parentheses, right-associative exponentiation, unary operators, constants, variables and calls. |
| SCI-ALG-002 | Architecture/P0 | Interactive input mode does not change the execution semantics of stored FOCAL/User/System RPL programs. |
| SCI-MEM-001 | Architecture/P0 | Modern host memory by default; optional historical profiles account for model-specific RAM, registers/cards and visible free-memory behavior. |
| SCI-TRAIN-001 | Planned | Bilingual, offline-first help for RPN and ALG, then comparative exercises and optional evaluation traces. |

## Historical compatibility commitments

| Canonical ID | Goal and scope | Milestone | Release status |
| --- | --- | --- | --- |
| SASD-CALC-COMPAT-041-SYN | Historical 41-family 56-bit register/byte-program-ready design; synthetic command **A**, programs **B** as long-term minimum. Byte Grabber/firmware peculiarities **C optional**. | Prepare M0/M1; deliver in M4 slices | Not implemented; not V1 |
| SASD-CALC-COMPAT-048-SYSRPL | User RPL precedes a documented and reference-tested subset of historical System RPL, internal objects and virtual system calls. | Prepare M0, user programs M3, system M4 | Not implemented; not V1 |
| SASD-CALC-COMPAT-048-SATURN | Potential separate virtual Saturn CPU/instruction execution | M5 research | Optional |
| SCI-COMP-041-FOCAL | Historic normal key-program execution, registers, stack and flags per documented reference profile | M3 | Planned |
| SCI-COMP-048-USERRPL | Historical RPL object stack, program objects and User RPL semantics per documented reference profile | M3 | Planned |
| SCI-ADV-001 | Map Advantage-Pac-era *function groups* to shared mathematics and optional 41-family commands, avoiding reimplementation | M4 / later | Reference analysis; optional add-on |
| SCI-EXT-001 | Time and Statistics modules with model-specific state/commands and rights-reviewed references | M4 / later | Planned |

The earlier F-001…F-030, NF-001…NF-016, SYN-001…SYN-020, SRPL-001…SRPL-020 labels appeared in draft discussion analyses. They are retained as **historical draft cross-references**, not silently renumbered as implemented obligations; this document supplies stable new delivery/traceability IDs. Full low-level historic acceptance requirements are in [Series 41](HISTORICAL-41.md) and [Series 48](HISTORICAL-48.md).

## Exclusions from V1 (not cancellations)

Full FOCAL/User RPL; synthetic programming; System RPL; historical binary programs, ROM and module emulation; Strict Historical completeness; vintage address space; Nut/Saturn CPU; original OS; extensive desktop IDE; financial calculators; large interactive course; ALG app and combined ALG/RPN UI.

## Reference paths

- [V1 scope and release gates](RELEASE-V1.md)
- [Project architecture](ARCHITECTURE.md) and [multi-app contracts](MULTI-APP-ARCHITECTURE.md)
- [RPN keyboard semantics questions](KEYBOARD-UX.md)
- [Compatibility evidence](COMPATIBILITY.md)
- [Roadmap](../../ROADMAP.md) and [backlog](../../TASKS.md)
