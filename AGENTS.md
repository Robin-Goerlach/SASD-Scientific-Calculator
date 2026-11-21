# AGENTS.md — operating rules for coding agents and contributors

These instructions apply to the whole repository. Read `README.md`, `ROADMAP.md`, `TASKS.md` and `docs/en/DECISIONS.md` before changing scope or architecture.

## Immutable priorities unless explicitly decided otherwise

1. **First ship a dependable iPhone classic scientific UPN/RPN calculator (M1→M2)**: offline, no ads, no subscriptions, ideally free, tested including iPhone XS.
2. The public iPhone portrait view is **calculator-only**; desktop IDE panels are optional and do not leak into its architecture.
3. Historical program execution (K2), internal/system compatibility (K3) and CPU/OS research (K4) are **not blockers** for M2.
4. Financial calculator is a **separate product, repository, release train**. Never merge its release gates, UI or state with Scientific.
5. Keep separate future 41/48-family semantic implementations; no universal interpreter by assumption.
6. **No trademarked manufacturer's logo/name as SASD branding.** The main READMEs remain neutral; separate, accurate compatibility statements require evidence and review.
7. **Preserve existing MIT `LICENSE` and copyright.** Do not relicense silently.
8. Never copy/publish proprietary firmware, ROMs, operating-system images, manuals, commercial program collections, or third-party photos without explicit permission.

## Architecture and quality policy

- C++20 portable core + CMake; platform-independent logic must not import SwiftUI, Foundation, Win32, UI frameworks or network APIs.
- The initial `RpnEngine` is a generic modern stack, **not** a verified clone of any historic machine. Do not silently retrofit legacy conventions.
- SwiftUI iOS integration via a narrow versioned C ABI is a **proposal**, not an implemented API. Verify Xcode deployment availability before adding targets.
- Prefer incremental, testable changes. Each new command must define arity, stack ordering, error behavior, persistence effect and tests.
- Error paths must not mutate state unless explicitly documented; reject non-finite numeric input rather than silently storing it.
- Avoid duplicated advanced numerical algorithms. Reuse versioned **C++-usable** SASD Math Toolkit components where available and approved. Do **not** force a C# runtime into iOS or block M2 waiting for a dependency.
- No permanent server or network requirement for calculating or for restored state.
- Source files, build configurations and examples need clear comments; explain decisions and invariants, not every trivial statement.
- Update `README.md`, `README.de.md` and release matrices when a status changes. No fictitious functionality, tests, dates or compatibility percentages.
- Preserve minimal supported C++20 toolchain; do not introduce undeclared dependencies.

## Before committing

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --config Debug
ctest --test-dir build -C Debug --output-on-failure
```

If the environment cannot run a required test, describe the gap in the commit/PR. **Do not** claim green iOS/App Store testing from Linux/Windows alone. Prefer verified changes on `main` for the solo-developer workflow; use branches when risky or parallel.

## Documentation statuses

Use **implemented / tested / planned / optional / explicitly excluded**. Compatibility level K1 is not equivalent to the M1 milestone; K2–K4 do not imply release dates. Link every compatibility assertion to tests, fixture provenance, tested platforms and version.

## Out-of-scope without explicit new approval

Emulator CPU/OS, System RPL, synthetic low-level programs, full historical binary compatibility, App Store submission, financial features, forced desktop editor, user accounts, adverts, subscription billing, cloud save and indiscriminate refactors of other SASD repositories.

## Binding multi-app and historic architecture supplement (2026-11-21)

The newly consolidated normative planning documentation is [requirements](docs/en/REQUIREMENTS-MATRIX.md), [multi-app boundaries](docs/en/MULTI-APP-ARCHITECTURE.md), [ALG](docs/en/ALGEBRAIC-INPUT.md), [Series 41](docs/en/HISTORICAL-41.md), [Series 48](docs/en/HISTORICAL-48.md), [shared components](docs/en/SHARED-COMPONENTS.md), and [V1 scope](docs/en/RELEASE-V1.md).

- **One shared mathematical function** where technically meaningful; use model-specific numeric/precision/error/stack adapters. No universal historical interpreter and no duplicate ALG parser. A 41 raw 56-bit register is not a `double`; a 48 RPL object is not a 41 register.
- Independent ALG app is a **planned** Scientific consumer with its own state and `=` input. Keep that path buildable without importing historical family internals when implemented. Its delivery cannot block the classic RPN iPhone V1.
- Preserve future 41 synthetic **B** and documented 48 System-RPL long-term objectives; their implementation is **not authorized merely by this note**, nor required for V1. 41 Byte Grabber stage C and Saturn/Nut execution remain optional.
- Under no circumstances resolve 48 `SYSEVAL` / `LIBEVAL` to host pointers. Byte-level historic execution may only access checked, virtual calculator memory.
- Specify modern expression grammar (power right-associative, `-2^2` parses as `-(2^2)`), source-position errors and resource bounds independently of historical RPL or FOCAL program parsing.
- Historical storage: plan model-specific opt-in profiles, not a global 128-KB cap; profile and module capabilities must appear in snapshots and conformance fixtures.
- Maintain separate catalogs of *mathematical operations* and *historical command effects*. New math must not silently create new vintage opcodes.
- Financial TVM/cashflow/annuity/bond UI, release and data are **not in this repo**; library reuse requires real consumers, pinned versions and license/provenance review.
- Each plan/spec row names status and target. Never say a diagram, archived image, unchecked requirement, manual excerpt or fixture proposal is an implemented feature.
- When a shared API changes, run all existing affected tests and record missing future test suites honestly. Provide code comments for invariants, state ownership, historical divergence, security and serialization decisions.
- README conceptual art is not a true screenshot or authoritative key map. **Do not add proprietary screenshot/ROM/manual assets**. Replace App Store screenshots only with real build captures after rights review.

When working on the initial C++ code, do not casually change `RpnEngine` from its documented generic dynamic stack to a purported exact four-level emulation. Add a separately approved and tested historical state machine when its behavior contract exists.
