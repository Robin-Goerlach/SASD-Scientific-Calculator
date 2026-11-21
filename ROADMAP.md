# Roadmap — SASD Scientific Calculator

**Baseline:** 2026-11-21. These milestones supersede the older, feature-first seven-phase proposal. Order is based on **usable first iPhone release**, not the order in which vintage machines were originally built.

**Strategy C with strict priority A:** the portable architecture and future calculator family remain in view, but work that does not improve a shippable *classic scientific calculator* must not delay M1/M2.

## Status vocabulary

- **DONE** means implemented, verified, and linked to evidence.
- **IN PROGRESS** means some work has begun; no release guarantee.
- **PLANNED** means specified but unimplemented.
- **OPTIONAL** means not a delivery obligation.
- **BLOCKED** must include a concrete dependency and owner/action.

| Phase | Status | Scope and release gate |
| --- | --- | --- |
| **M0 — Foundation** | **IN PROGRESS** | Repository hygiene; confirmed MIT license; bilingual entry docs; specs; C++20/CMake core; reproducible native CI; basic tests; design sketches clearly marked. Gate: local + CI build/tests passing and decisions traceable. |
| **M1 — Classic scientific core** | **IN PROGRESS (minimal arithmetic only)** | Real calculator-grade stack and register operations, numeric inputs, common scientific functions, angle modes, predictable error semantics, persistence interfaces, command API and tests. Gate: acceptance matrix plus state/error tests. |
| **M2 — iPhone V1.0** | **PLANNED** | Native iPhone UI with full practical key coverage; stable suspend/relaunch restoration; iPhone XS validation; offline/ad-free/no subscription; accessibility; SASD branding/link; QA, privacy/store requirements. Gate: release checklist passed on real devices. |
| **M3 — Historical user programs** | **PLANNED** | Separated Series 41/48 models, User RPL/FOCAL programming with legally sourced fixtures, import/export where possible. Gate: K2 compatibility matrix with reproducible samples. |
| **M4 — Advanced historical compatibility** | **PLANNED** | System-near language/semantics and obscure behavior: system RPL, synthetic execution paths, extension modules. Gate: K3 evidence; failures published. |
| **M5 — Hardware/OS research** | **OPTIONAL** | Nut-/Saturn-class CPU instruction or OS emulation as separate, legally safe research modules. Gate: separate decision and licensing/data-source review. **Never blocks M2.** |

## M0 acceptance
- [x] Repo exists and already has a MIT license (retain author copyright and notice).
- [x] Product priorities and K1–K4 separated in repository documentation.
- [x] First portable C++20 target and minimal unit tests prepared and locally validated.
- [x] Desktop/iPhone/science-art **SVG redrawings** stored as mockups (not releases).
- [x] GitHub Actions native core CI observed successful on Linux, Windows, macOS — [run 44899248003](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/actions/runs/44899248003) (2026-11-21); this is **not** iOS or historical compatibility validation.
- [ ] Approve exact iOS minimum deployment target after device/SDK research.
- [ ] Review final key inventory against authoritative specifications and owned reference device.

## M1 acceptance
- [ ] Numeric formats, precision/error policy, stack model, registers and modes approved.
- [ ] Binary/unary/common scientific operations with domain and non-finite policy tested.
- [ ] Repeatable command-oriented core API with no UI dependency.
- [ ] Versioned persistent-state format with corruption detection and migration tests.
- [ ] Independent reference test cases + golden examples.
- [ ] Deterministic build/test matrix, memory safety and regression checks.
- [ ] Document exact implemented K1 subset; do **not** label full K1 complete.

## M2 acceptance
- [ ] iPhone portrait screen displays calculator only, no always-visible desktop editor.
- [ ] Complete **agreed V1** keyboard map; readability and touch targets validated on iPhone XS.
- [ ] Stable recovery after suspension, termination and upgrade.
- [ ] Common scientific functions, error explanations, physical device tests.
- [ ] Works in airplane mode; no ads, tracking dependency or subscription paywall.
- [ ] Small top-left SASD brand link; privacy and third-party rights review.
- [ ] App Store archival/release checklist signed off.
- [ ] Release notes accurately enumerate shipped features and compatibility limitations.

## Non-blocking parallel tracks and historical dependencies

**Classic RPN M1→M2 is the critical release path.** The independently publishable **ALG scientific app** has its own modern calculator state, planned shared Pratt parser and scientific function catalog; it may proceed concurrently after shared contracts stabilize, but cannot delay the first classic iPhone V1. The **Advanced RPL app** is a distinct later consumer. A combined ALG/RPN user interface is optional. The external **Financial Calculator** has separate repository, domain and release train.

The historical compatibility milestones are intentionally *delivery order*, not a reduction in long-term commitments:

- **41-family:** virtual 56-bit register and byte-program architecture seam from the outset; regular FOCAL in M3; selected synthetic **A**, program-level **B** as a long-term commitment in M4; Byte Grabber **C optional**.
- **48-family:** historical object/nibble and Saturn virtual address seam; User RPL before selected System RPL; a documented subset of System RPL remains a **long-term commitment** in M4; Saturn machine-language interpretation optional M5.
- **Modules:** Time/Statistics and Advantage-Pac-inspired command adapters after priority-A work; no original ROM replication and no duplicate math algorithms.
- **Memory:** modern host resources by default; opt-in historical modes and 128 KiB built-in 48GX plus extensions accounted for later, not a flat host RAM cap.
- **Education:** minimal offline help with M2; bilingual manual, interactive comparison and step-by-step traces after core readiness.

See [requirements](docs/en/REQUIREMENTS-MATRIX.md), [41-family](docs/en/HISTORICAL-41.md), [48-family](docs/en/HISTORICAL-48.md), [ALgebraic](docs/en/ALGEBRAIC-INPUT.md) and [decisions](docs/en/DECISION-QUESTIONS.md).


## Prioritization rules
1. Fix correctness, crash, lost state, and key usability regressions ahead of new features.
2. iPhone M2 quality beats optional desktop tooling, Android, iPad extras and historical depth.
3. Financial functionality, Advantage-Pac-style additions and their licensing are separate.
4. No vendor ROM, copyrighted manual, proprietary program or borrowed imagery in source.
5. Never silently promote a plan to **DONE**; show failing and passing evidence.

See [TASKS.md](TASKS.md), [PRODUCT](docs/en/PRODUCT.md) and [RELEASE-CHECKLIST](docs/en/RELEASE-CHECKLIST.md).
