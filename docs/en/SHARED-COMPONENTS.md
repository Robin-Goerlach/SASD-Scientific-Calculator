# Reuse between Scientific and Financial — engineering policy

**Product split STR-002 (2026-11-20):** Scientific here; a separate `SASD-Financial-Calculator` repository is proposed but not created by this document. The Scientific classic iPhone release has priority. No Financial feature or dependency can block a Scientific release or vice versa.

## Reuse decision table

| Component | Share? | Boundary |
| --- | --- | --- |
| Portable numeric types and precision services | Strong candidate | Separate model-specific rounding/representations |
| Basic math, complex, matrix, roots and solver algorithms | Strong candidate | Financial's TVM conventions remain Financial-owned |
| Pratt ALG lexer/AST/parser | Strong candidate | App-specific grammar affordances and symbol catalogs |
| Statistics and curve fitting | Strong candidate | Distinct UI and model-specific accumulator semantics |
| Generically typed data stack container | Potential | **Not** the vintage 41 four-level stack state machine or 48 RPL object stack |
| Diagnostic codes, serialization helpers, test utilities | Strong candidate | Per-app schema and policies stay separate |
| FOCAL, synthetic 41 commands | No | Scientific Series 41 only |
| User/System RPL and Saturn virtual memory | No | Scientific Series 48 only |
| TVM, annuities, amortization schedules, cashflows, IRR/NPV, bonds | Financial domain | May consume generic numeric solvers; not moved to Scientific core |
| UI keyboard/layout | Limited | Independent product UX and release certification |

## No premature framework

1. Build and test a narrowly scoped, UI-neutral C++20 algorithm in the Scientific monorepo *when Scientific needs it*.
2. When a second actual consumer exists, compare source-copy with provenance versus versioned library/external package.
3. Prefer a separately tagged, immutable library only once the API is stable enough for both consumers. Pin dependency revisions and compile/test independently.
4. Source copy is allowed for release independence: record origin repo/commit, license text, changes and upstream security maintenance owner. Do not silently fork.
5. A shared repository does not imply shared runtime installation, account, network, release train, app ID or mandatory synchronized upgrades.
6. The existing SASD Math Toolkit can be evaluated for **actual C++-usable** APIs, not assumed interchangeable with a .NET-only implementation.

**Decision still open:** package transport (CMake package, FetchContent pinned tag, vcpkg, vendor copy), precise shared numeric types and licensing plan for a new extracted package. Keep MIT for this existing repository unless explicitly redecided; third-party rights remain separate.
