# Modules and historical extension families

**Status:** planned, with individual acceptance criteria. **No historical ROM module is implemented or bundled today.** Extensions belong to their historical model runtime and never enter the mathematical core merely because they have mathematical functions.

## Series 41

| Historical reference | Planned technical scope | Priority |
| --- | --- | --- |
| Time Module / HP 82182A | Model-specific clock/date/alarm registers, commands, virtual time source and deterministic clock tests | After classic core; not V1 |
| Statistics Pac | Statistics commands and 41-style stack/register semantics; shared numerical statistics algorithms where suitable | After classic core; not V1 |
| Advantage Pac | **Functional reference only**: matrices including complex; complex arithmetic; vectors; equation solving; polynomials; integration; differential equations; base conversions; Boolean/bit operations; statistics/curve fitting; elementary financial calculations | Optional later add-on, no ROM copy |

**Advantage Pac rule:** compare each function with already planned Series 48 and common math features before writing code. One tested algorithm may be exposed under different historical command names with independently tested 41-specific stack, register, precision and error effects. Financial workflows (TVM/cashflow/bonds) stay in the separate Financial product.

Compatibility with original historical XROM program binaries **is not implied** by function-level similarity. A true byte/XROM compatibility contract, if later approved, needs a legally sourced program fixture corpus and model-specific decoding.

## Series 48

Potential RAM-card configurations, libraries and object import/export are model-specific. In historical profiles, limits and memory reporting use a documented built-in/extension-card model; in Modern profiles do not impose artificial 128 KiB limits. Compatibility with original third-party binaries requires distinct legal and technical evidence.

## Extension architecture

- Explicit capability / version metadata with model and compatible runtime versions.
- Separate registry for historical command aliases and system/library identifiers.
- Avoid native third-party executable plugin loading in the first iOS app; compiled-in, opt-in feature modules are an appropriate early target.
- No Internet-dependent module installation for basic calculation.
- Tests: activation/deactivation, conflict resolution, error state, persistence, memory profile, cross-model noninterference.
- License/rights audit is mandatory for firmware, ROM, textbook listings and sourced program collections.

## Lifecycle

**Proposed:** identify → document reference function and provenance → classify *shared math* versus *model command* → write contract and tests → implement → measure compatibility. A module being *named* does not mean installed or implemented.
