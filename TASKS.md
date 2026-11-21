# Work packages — prioritized, verifiable

**Architectural source and dependencies:** [German system architecture](docs/ARCHITEKTUR.md) and the canonical [ROADMAP.md](ROADMAP.md). Use its WP-00…WP-16 and ADR gate mapping when opening work items; do not mark planned historic engines as implemented.

Maintain this as a lightweight, task-oriented overview. GitHub Issues may track implementation detail. **Order is deliberate**: the calculator's first usable iPhone release wins over compatibility research. Each issue/PR must link its scope, tests, dependencies and completion evidence.

| ID | Priority | Milestone | Work package | Dependencies | Acceptance evidence | State |
| --- | --- | --- | --- | --- | --- | --- |
| F-01 | P0 | M0 | Bootstrap docs, MIT license preserved, native C++20 build/test, CI | none | CMake/CTest smoke; CI runs | **partial** |
| F-02 | P0 | M0 | Approve V1 key inventory from original-device reference, validate design and legal differentiation | reference spec/photo | key-by-key test mapping | planned |
| C-01 | P0 | M1 | Establish precise stack semantics, modes, registers and error taxonomy | F-01 | approved behavioral specification + fixtures | planned |
| C-02 | P0 | M1 | Core scientific functions and numeric edge policies | C-01 | unit/golden tests | planned |
| C-03 | P0 | M1 | Versioned serialized state, crash-safe restore, migration | C-01 | restart/corruption/upgrade tests | planned |
| C-04 | P0 | M1 | Stable versioned C ABI boundary and native test driver | C-01 | lifecycle/ABI tests | planned |
| I-01 | P0 | M2 | SwiftUI iPhone calculator view, iPhone XS layout | F-02,C-04 | device snapshots + interaction tests | planned |
| I-02 | P0 | M2 | iOS lifecycle, state, accessibility, offline verification | C-03,I-01 | physical-device QA | planned |
| I-03 | P0 | M2 | App Store checklists, SASD link, privacy, licensing | I-02 | signed release checklist | planned |
| H-01 | P2 | M3 | Separate Series 41 and Series 48 behavioral profiles | M2 | family-specific acceptance tests | planned |
| H-02 | P2 | M3 | Historical user programming (FOCAL/User RPL) | H-01 | K2 matrix and fixture provenance | planned |
| H-03 | P3 | M4 | Advanced internal/system programming | H-02 | K3 matrix; published limits | planned |
| H-04 | P4 | M5 | Optional instruction/OS emulation research | explicit decision | K4 matrix, rights review | optional |
| D-01 | P2 | post-M2 | Optional desktop stack/editor/library workspace | C-04 | distinct native UI tests | planned |
| L-01 | P2 | post-M2 | Bundled searchable manual and guided RPN tutorials | implemented functions | offline tutorial tests | planned |
| P-01 | separate | other repo | Financial calculator and optional modules | own requirements | **never a blocker** | out of scope |

**Task completion rule:** code merged on `main` with regression tests + documentation updated; CI green. A generated image or planned API does not count as implementation. Small incremental commits to `main` are acceptable for this solo-maintained repository if the gates are respected.

## New documentation-backed work tracks (not yet implemented)

| ID | Priority | Target | Deliverable | Dependency / mandatory evidence | State |
| --- | --- | --- | --- | --- | --- |
| ARC-01 | P0 | M0 | Confirm public math/numeric contracts and calculator-neutral input API | Independent build, numerical decision record, shared tests | specified; open |
| RPN-01 | P0 | M1 | Four-level stack/ENTER/LAST-X/flags/register state machine | Exact state transition table and golden tests; do not repurpose generic vector stack silently | planned |
| RPN-02 | P0 | M1 | Approved scientific key set, angle and precision behavior | Unit/domain/error tests and independent key inventory | planned |
| APP-01 | P0 | M2 | Native iPhone XS app and versioned bridge | physical iPhone testing, lifecycle persistence, offline, release compliance | planned |
| ALG-01 | P2 | parallel | Stand-alone ALG scientific app context, Pratt lexer/AST and evaluator | `docs/en/ALGEBRAIC-INPUT.md` golden cases, separate release gate | planned |
| HIST41-01 | P2 | M0 seam / M3 | Raw 56-bit/byte program architecture and regular FOCAL | independently sourced byte/state fixtures | planned |
| HIST41-02 | P3 | M4 | Synthetic commands A, programs B long-term; Byte Grabber C optional | separately gated A/B/C compatibility suites | planned |
| HIST48-01 | P2 | M0 seam / M3 | Historical RPL object representation and User RPL | object roundtrips; legal User RPL fixtures | planned |
| HIST48-02 | P3 | M4 | Documented subset of System RPL, virtual SYSEVAL/LIBEVAL | ROM profile, virtual address, system stack and safety tests | planned |
| MOD-01 | P3 | M4+ | Time/Statistics and optional Advantage-style function adapters | no duplicate math; module state/rights/behavior tests | planned |
| EDU-01 | P2 | M2/post-M2 | Minimal offline help then interactive RPN/ALG lessons | real command metadata and bilingual reference tests | planned |
| REUSE-01 | P2 | when Financial starts | Evaluate real shared-package consumers vs provenance-tracked code copy | independent release/build, license and version evidence | deferred |
| RSRCH-01 | P4 | M5 | Optional Nut/Saturn emulator feasibility | separate decision, rights analysis, test fixtures | optional |

Do not start P3/P4 projects to make the V1 backlog appear complete. **P0 defects and release gates always win**. Refer to [full requirements](docs/en/REQUIREMENTS-MATRIX.md), [architecture](docs/en/MULTI-APP-ARCHITECTURE.md) and [V1 scope](docs/en/RELEASE-V1.md).


## Active GitHub issue entry points

- [#1 — V1 keyboard/command inventory](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/1) — F-02 (M0/P0).
- [#2 — iPhone XS / Xcode deployment verification](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/2) — M0/P0.
- [#3 — RPN semantics and error contract](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/3) — C-01 (M1/P0).
- [#4 — Scientific functions and test fixtures](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/4) — C-02 (M1/P0).
- [#5 — Versioned persistent state](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/5) — C-03 (M1/P0).
- [#6 — Versioned C ABI and native iPhone UI](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/6) — C-04/I-01 (M1→M2/P0).
- [#7 — App Store / physical-device acceptance](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/7) — I-03 (M2/P0).
- [#8 — Verify actual CI runs and regression coverage](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/issues/8) — F-01 follow-up (M0/P1).
