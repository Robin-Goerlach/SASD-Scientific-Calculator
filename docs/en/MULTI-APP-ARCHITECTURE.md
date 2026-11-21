# Scientific multi-app architecture — binding boundaries

**Status:** Agreed product architecture; most applications/engines are *not implemented*. The early `sasd_scientific_core` is a generic vector-stack arithmetic development slice, not a certified four-level machine.

## Four independent axes

1. **Product**: Scientific in this repository; Financial in a different future repository and App Store listing.
2. **App**: classic RPN (first release priority), stand-alone ALG app (planned), advanced RPL app (planned), and optionally a combined app (not a V1 gate).
3. **Calculator model**: modern algebraic context, 41-style historical state machine, 48-style historical object/RPL machine.
4. **Interactive input / compatibility profile**: RPN/ALG input independently from Modern, Historical Core + Modern Input, and Strict Historical *where the model supports the combination*. Strict Historical may restrict modern entry while still allowing a separate hybrid profile.

A user-selected input mode is **not** a program-execution mode. Existing programs run through their own historical VM unchanged by a UI preference. A stand-alone ALG app requires no historical 41/48 core to compute.

## Target dependency direction

```text
apps/algebraic, apps/classic-rpn, apps/advanced-rpl (planned)
  -> app-level view models / input controllers (planned)
     -> neutral facade / command and state contracts
        -> modern ALG runtime | 41-family VM | 48-family RPL runtime
           -> model-owned numerical and state adapters
              -> portable shared math / diagnostics / storage codecs
```

Never invert this dependency. User interface tap handlers delegate to testable application commands; no calculation code in SwiftUI button callbacks. The 41 and 48 runtimes must not import each other. A common mathematical algorithm is not a common historical opcode or data object.

## Planned module ownership (create directories only when code exists)

| Module boundary | Owns | Must not own |
| --- | --- | --- |
| `libs/math` or `SASD Mathematical Core` | portable algorithms, tested contracts | stack lift, RPL prologues, SwiftUI |
| `libs/expression` | lexing, parsing, AST, diagnostics | implicit historical program conversion |
| `libs/function-catalog` | mathematical metadata, arity, types and documentation keys | permissions to execute arbitrary system internals |
| `calculators/algebraic` | result/Ans/history/variables/angle mode for modern ALG app | HP-41 registers or System RPL |
| `calculators/series41` | four-level stack, LAST X, registers, future FOCAL/synthetic state | HP-48 RPL interpreter |
| `calculators/series48` | RPL objects, stacks, directories, User/System RPL, virtual Saturn memory | HP-41 byte program state |
| `platform/native-bridge` | versioned non-throwing C ABI, opaque handles, lifetime and errors | native UI or numeric policy |
| `apps/*` | platform layout, input affordances, accessibility and lifecycle | alternate math evaluator |
| `learning/*` | localized help and exercises from real command metadata | separate training-only calculator |
| `tests/*` | mathematical, state, cross-input and historical conformance | copyrighted unknown-origin fixtures |

## Shared algorithms do not imply shared numbers

- Keep numerical **algorithm** separate from model-specific **representation, precision, rounding, exceptional cases and state effects**.
- Historic 41 registers are 56-bit entities. Historic 48 RPL objects use their own prologues/nibble-oriented representation. Neither reduces to `double` merely because the V1 prototype uses binary64.
- Explicit adapters convert between common mathematical values and historical values. A conversion can fail, report loss or be unavailable.
- Importing an ALG result into a historical stack is a separately specified *state transition*; it is not arbitrary program execution.
- Mathematical functions and historical command aliases have **distinct registration**: same SIN algorithm may have different angle/error/stack rules.

## Applications and release independence

Each planned Scientific app has its own front-end target, bundle identifier, version and App Store release gate; exact identities remain open. CMake shared targets are allowed within the Scientific monorepo; runtime inter-app dependencies are not. Full native SwiftUI/C ABI contracts are still to be designed and tested on iPhone XS. Financial must also compile/test/release independently from a separate repository.

## Parallellism / Codex ownership

A task owns one area (shared math, expression, 41, 48, app/bridge, tests/docs). Public API changes require a documented compatibility impact review and cross-consumer test runs. Prefer short independent worktrees for risky parallel activity; main may be used directly after a coherent verified change by the solo maintainer. CI on Linux/Windows/macOS covers the portable core, **not** iPhone device acceptance.

## Current source reality

Existing executable paths remain `src/rpn_engine.cpp`, `include/sasd/scientific/rpn_engine.hpp`, `apps/cli` and `tests/rpn_engine_test.cpp`. This document does **not** assert that the above planned directories, historical machines or native apps exist.
