# End-to-end quality matrix

**Current implemented evidence:** generic vector RPN arithmetic with finite double operations and a small CTest suite. No app, historical compatibility, numeric-completeness or historical hardware tests are claimed.

## Test families and ownership

| Prefix | Scope | Contract |
| --- | --- | --- |
| CORE | Shared math; results, numeric context, deterministic failure semantics | Basic and advanced algorithm unit tests |
| ALG-LEX/PAR/AST | Tokenization, associativity, parentheses, functions, malformed expressions | Grammar and source-location goldens |
| ALG-EVAL | Type checks, variable resolution, angle, resources and error rollback | Model-context evaluator tests |
| RPN | ENTER, X/Y/Z/T, LAST X, lift/drop, roll, registers, key state | Full before/after state snapshots |
| 41-FOCAL | Historical programs, flags and instructions | Reference program/byte stream suite |
| 41-SYN | Raw 56-bit registers, synthetic bytes, pointers, key assignments | Source-backed A/B test sets; C optional |
| 48-USER | Historical RPL objects, data stack/return stack, user programs | Object/VM reference suite |
| 48-SYS | System objects, profile-specific SYSEVAL/LIBEVAL, virtual memory | Primitive/system-state reference suite |
| MEM | Modern and Strict/Hybrid profiles, limits, card expansion, memory reporting | Cross-profile resource tests |
| CROSS | Algebraic vs RPN result equivalence under matching numerical contexts | **Mathematical** results, not necessarily stack state |
| SAFE | Corrupt state, virtual address exploits, unbounded input/nesting | No host escape or uncontrolled crash |
| UX/IOS | Physical touch, VoiceOver, iPhone XS, offline, lifecycle, release | Device report and signed release evidence |

## Example algebraic conformance data (not yet executed)

```text
3 + 4 * 5                  -> 23
(3 + 4) * 5                -> 35
2 + 3^2                    -> 11
20 / 4 * 2                 -> 10
2^3^2                      -> 512
-(3 + 4)                   -> -7
(3 + 4 * 5^2) / 2          -> 51.5
-2^2                       -> -4
(-2)^2                     -> 4
2^-3                       -> 0.125
```

Division by zero, incomplete expressions, missing parentheses, overflow/underflow, NaN propagation policy, precision limits, max depth, user-defined functions and signed literals require negative/boundary tests. Historical error behavior can differ; use the correct reference profile.

## Release and CI discipline

Portable C++: Linux, Windows, macOS build/CTest on push and PR. iOS build and physical iPhone XS checks must be conducted separately and documented; desktop CI cannot prove App Store readiness. Record commits, test IDs, platform/toolchain and results. For every shared math/API change, run all affected app/41/48/ALG suites; never pass an unimplemented subsystem by omitting its mandatory tests once it is in scope.
