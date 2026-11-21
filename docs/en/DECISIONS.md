# Decision register — evidence-based project baseline

Decisions are ordered by priority. Dates refer to the 2026-11-19 to 2026-11-21 project discussions; they are **not release dates**.

| ID | Status | Decision | Consequence |
| --- | --- | --- | --- |
| D-001 | **Decided 2026-11-21** | **Strategy C with strict priority A:** reusable platform long-term; classic scientific iPhone product first. | M1/M2 trump extra families/tools. |
| D-002 | **Decided 2026-11-21** | M0 foundation, M1 classic tested core, M2 App Store V1, M3 historical programs, M4 extended compatibility, M5 optional CPU/OS research. | Old generic roadmap replaced. |
| D-003 | **Decided 2026-11-21** | K1 classic functions, K2 user programs, K3 system-near, K4 machine execution are **not** the same as milestones. | Release claims need level/feature evidence. |
| D-004 | **Decided 2026-11-20** | Scientific and Financial are distinct products/repos/releases; Financial never blocks Scientific. | Shared code only stable/versioned. |
| D-005 | **Decided 2026-11-20** | iPhone portrait view shows only calculator; desktop may offer editor, inspector, library. | Separate user experiences, same semantics. |
| D-006 | **Decided 2026-11-20** | Independent SASD name/brand; drop foreign branding from public primary READMEs. | Historical compatibility notes separate and factual. |
| D-007 | **Decided 2026-11-20** | Modern host memory by default; legacy bounds only optional profiles. | No universal historical RAM labels. |
| D-008 | **Confirmed from repository 2026-11-21** | Existing repository is **MIT** licensed. | Preserve the actual copyright/licensing file. |
| D-009 | **Architecture direction** | Portable C++20/CMake headless core, native iOS UI with proposed SwiftUI + versioned C ABI. | API design required before UI integration. |
| D-010 | **Architecture direction** | Two historical calculator families eventually use separate semantics/program engines. | Do not force a shared interpreter. |
| D-011 | **Architecture direction** | Reuse a compatible versioned Math Toolkit where available, do not block M2 on other runtimes. | Native basic operations stay self-contained initially. |
| D-012 | **Decided** | Concepts are non-executable images; key labels/layout require review against true device. | No feature/fidelity claims from graphics. |

## Dated strategic decision addendum (retains previous entries)

| ID | Status | Decision | Consequence |
| --- | --- | --- | --- |
| D-013 | **Decided 2026-11-20** | A separate stand-alone **ALG Scientific app** joins classic RPN and advanced RPL within Scientific; one shared math basis, no duplicate ALG parser. | ALG can progress separately but must not delay classic V1. |
| D-014 | **Decided 2026-11-20** | Modern ALG input is distinct from historic program execution; Modern / Historical Core + Modern Input / Strict Historical profiles are distinct from model and interactive input choice. | Historical program semantics unchanged by UI preference. |
| D-015 | **Long-term commitment 2026-11-20** | `SASD-CALC-COMPAT-041-SYN`: raw 56-bit register/byte architecture; synthetic programme stage B long-term; Byte Grabber stage C optional. | Architecture seam now, execution later, no V1 block. |
| D-016 | **Long-term commitment 2026-11-20** | `SASD-CALC-COMPAT-048-SYSRPL`: after User RPL, implement a documented reference-tested subset of System RPL; `SASD-CALC-COMPAT-048-SATURN` optional. | Virtual ROM/system resolver, no host pointers; no V1 block. |
| D-017 | **Decided 2026-11-20** | Time and Statistics modules and Advantage-Pac-inspired features may extend Scientific only after shared-function analysis. | No second math engine, no implicit proprietary ROM/XROM replication. |
| D-018 | **Decided 2026-11-21** | V1.0 accepts a reliable classic iPhone RPN calculator **without** complete FOCAL/User RPL/System RPL/synthetic programmes, Strict Historical or CPU/OS emulation. | M1→M2 critical path; preserve longer-term commitments. |
| D-019 | **Confirmed 2026-11-21** | Native C++ core workflow green on Linux, Windows and macOS for commit `9f266421`. | [CI evidence](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/actions/runs/44899248003); not iOS evidence. |
| D-020 | **Asset provenance 2026-11-21** | Public README uses SVG concept redrawings of the latest iPhone/desktop visual ideas; source PNGs are not in Git. | No pixel-identical or app-screenshot claim. |

The above records *extend*, not erase, D-001–D-012. Their detailed acceptance/source status is in [requirements](REQUIREMENTS-MATRIX.md) and [deferred decisions](DECISION-QUESTIONS.md).


## Explicitly open decisions
- O-001: exact V1 keyboard/function matrix, mode model, numerical precision, ENTER/input semantics.
- O-002: formal iOS minimum version and tested Xcode/iPhone XS build environment.
- O-003: snapshot/restore schema, persistence privacy and import/export.
- O-004: first native UI implementation detail and FFI ownership contract.
- O-005: later dual-family profile boundaries and legal fixture sources.
- O-006: future online manual, interactive lessons and source licensing for historical reference materials.

## Process for changes

A changed decision must give a dated reason, effect on M1/M2, compatibility consequences and tests. Do **not** rewrite history or silently turn speculative options into requirements. The core priority (D-001) may change only with an explicit product decision.
