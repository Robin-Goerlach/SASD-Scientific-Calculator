# Architecture and boundaries

> **Canonical detailed architecture (German):** [SASD Scientific Calculator – Gesamtarchitektur](../ARCHITEKTUR.md). This English document is an earlier focused summary; the canonical design and current M0–M5 plan are in the comprehensive architecture and [ROADMAP.md](../../ROADMAP.md). Proposed interfaces/ADRs do not imply implemented code.

## Principle: platform strategy C, priority A

Implement a **small headless calculator first**, build the reliable iPhone product, then add depth and platforms. The current working code is **one generic C++20 arithmetic stack**, not a complete scientific engine, not a historic interpreter, and not a native iOS app.

```text
iOS native UI (planned SwiftUI)        Desktop UI (planned)
             |                                   |
      versioned C ABI (proposed)      platform adapter (later)
             |                                   |
             +---------- command façade --------+
                                |
                    SASD classic RPN core (M1)
                stack / registers / modes / errors
                      numeric / state / commands
                                |
            shared utilities and optional math adapters
                                |
                    no UI or network dependency

Later and separate:             Later and separate:
  Series 41 semantics             Series 48 semantics
  FOCAL/programs/modules          User RPL/objects/programs
          |                               |
          +--- compatibility test suites -+
                     K2→K3→K4
```

## Current implementation
- `include/sasd/scientific/rpn_engine.hpp` declares a deliberately small reusable API.
- `src/rpn_engine.cpp` implements finite binary64 arithmetic, basic stack manipulation and error codes; failed operations preserve the stack.
- `apps/cli/main.cpp` is a development driver only. It is not the final interaction model.
- `tests/rpn_engine_test.cpp` covers initial smoke and error invariants.
- CMake builds on systems with C++20; GitHub Actions checks common desktop OSes.

## Planned M1 domain model
- Document number types, decimal input, arithmetic/angle modes, internal precision and error conditions before expanding function coverage.
- Specify stack arity, ENTER behavior, registers, exchange/roll operations, state transitions, and strict error invariants.
- Keep command input/response (potentially event-based) independent of frontend controls.
- Make state snapshots explicit, versioned, validated and atomic; define recovery on corrupted files and schema changes.
- Maintain deterministic examples independent of frontends; locale stays a presentation concern.
- Future precision libraries should be evaluated as a decision, not a silent patch to `double`.

## Ownership

| Component | Owns | Must not own |
| --- | --- | --- |
| `scientific-core` | Stack semantics, calculations, registers, error states | SwiftUI/Win32, storage paths, HTTP, ads |
| Persistence adapter | Versioned durable snapshots, recovery | Calculation rules |
| iOS frontend | Touch layout, rendering, accessibility, lifecycle | Independent arithmetic semantics |
| Desktop frontend | Calculator canvas, optional editor/inspectors | Alternative numeric rules |
| Series 41/48 modules | Their own program languages, object/register models | Reinterpreting generic V1 silently |
| Math adapter | Stable reusable numerical algorithms | App lifecycle or incompatible C# runtime |

## ABI and portability
The initial native C++ API is **not** an ABI promise. Before iOS work, introduce a separate and versioned C-compatible façade with documented ownership, non-throwing error transport, valid UTF-8 boundaries and explicit snapshot operation. Do not expose STL containers across Swift/FFI boundaries. Check C++ library deployment options with the actual Xcode/iPhone XS toolchain.

## Existing SASD mathematics
[SASD Math Toolkit](https://github.com/Robin-Goerlach/SASD-Math-Toolkit) is a useful *candidate* for algorithms and shared tests. As of repository planning, its initial public implementation emphasizes C#; a usable supported native C++ library **must be confirmed** before depending on it. M1 basic arithmetic must not wait for this. Avoid duplicating advanced math only where a proven C++ library interface exists.

## Prohibited coupling
- Scientific ↔ Financial release or runtime dependencies.
- Series 41 ↔ Series 48 same-interpreter assumption.
- Native app ↔ permanent web server or cloud account.
- Historical profile ↔ global 128-KB memory cap.
- App Store V1 ↔ Nut/Saturn instructions, ROMs, System RPL, full historical formats.

## Proposed future layout (not implemented)
```text
apps/ios/                      Native frontend, later
apps/desktop/                  Optional desktop workspace, later
core/commands/                 Versioned command API, later
core/persistence/              State versioning, later
calculators/series41/          Independent historical semantics, M3+
calculators/series48/          Independent historical semantics, M3+
platform/ios/                  ABI adapter, later
learning/                      Offline handbook and exercises, later
tests/compatibility/           Legal fixtures and evidence, M3+
```

Directories are added **only when implemented**; empty scaffolding should not be mistaken for supported features.

## Multi-app and historical-system addendum (2026-11-21)

The earlier diagram describes the **current V1-first critical path**, not the full future Scientific app family. The separate ALG scientific app and optional ALG input in historic calculator profiles use a **single neutral parser** but have their own app state and integration adapters. See [multi-app architecture](MULTI-APP-ARCHITECTURE.md) and [ALG grammar](ALGEBRAIC-INPUT.md).

**Series 41** needs a later 56-bit raw register/byte-oriented programme store (ordinary FOCAL, then synthetic commands/programs); **Series 48** needs separately versioned historical RPL object/nibble representation, ROM/RAM virtual addresses, User RPL followed by selected System RPL. These are not compatible memory maps and must not be unified. See [41](HISTORICAL-41.md), [48](HISTORICAL-48.md) and [extensions](MODULES.md).

A family-specific operation may use shared mathematics, but historic rounding, under/overflow, stack lift, object conversion and error state must remain family-owned. Modern ALG results must enter historical calculator state through a deliberate, tested transfer operation. Shared libraries must not import historical family internals or SwiftUI.

The main classic RPN release remains M1→M2. Full hardware/software simulation is not a prerequisite. The existing vector-stack code is explicitly **not** reclassified as a finished historical four-level engine.
