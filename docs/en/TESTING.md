# Test strategy, provenance, and acceptance

## Executed foundation

`cmake` and `ctest` run a first small test executable for the current generic engine. It checks stack order, +/−/×/÷, stack underflow, duplicate, drop, swap, clear, NaN rejection, division by zero and overflow **with no state mutation on failed arithmetic**. This is initial native regression coverage, **not** device, persistence, or compatibility testing.

## Layered evidence plan
1. **Unit/contract:** operand order, input parsing, numeric boundary values, invalid arguments, nonfinite results, mode/register invariants.
2. **Property/metamorphic:** data preservation on failure, stack depth and valid transformations; property testing only after semantics are fixed.
3. **Persistence:** schema versions, atomic writes, corruption, power interruption, app suspension/relaunch, legacy migration and no user-data loss.
4. **Bridge/ABI:** lifecycle, memory ownership, UTF-8 boundary, errors, ABI version negotiation, platform calls from non-UI threads.
5. **Frontend:** touch hit boxes, accessibility labels, VoiceOver, iPhone XS safe areas, orientation, actual device regression.
6. **Offline/privacy:** airplane-mode functional tests, no subscriptions/ad components, no server dependence.
7. **Compatibility:** legal independent fixture origin, golden results per Series 41/48 model, program regression, explicit K1–K4 claim rows.
8. **Release gates:** App Store policy, privacy statements, source/asset rights, store screenshots from real approved build.

## CI
GitHub Actions workflow builds and runs CTest on Linux, Windows and macOS. CI status is **not considered confirmed until GitHub reports a green run**. iOS device tests need a separate Apple-device acceptance stage; macOS compilation alone is insufficient.

## Test data and dependencies
- Never commit copyrighted third-party firmware/manuals or proprietary program images.
- Preserve fixture source, author/license and reference readings.
- Do not rely on a single public online calculator result to infer historical fidelity.
- Version the expected output of goldens and document numerical tolerances.
- Record compiler, platform, source commit, app version and test date for every release.

## Suggested commands
```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug -DSASD_SCIENTIFIC_BUILD_TESTS=ON
cmake --build build --config Debug
ctest --test-dir build -C Debug --output-on-failure
```

No mocking of App Store approval, iPhone device checks or compatibility percentages. Report gaps plainly.

## Consolidated regression inventory and current CI evidence

The [detailed future test matrix](TEST-MATRIX.md) separates core arithmetic, ALG lexer/Pratt/AST and evaluator, classic stack state, historic 41 bytes/FOCAL/synthetic, 48 User/System RPL, memory profiles, safe virtual address space, cross-input *result* comparisons and iPhone UX. Each historical fixture needs provenance and distribution rights. No unimplemented suite is represented as passing.

**Verified initial GitHub Actions status:** [run 44899248003](https://github.com/Robin-Goerlach/SASD-Scientific-Calculator/actions/runs/44899248003) finished successfully on the existing native C++ Linux/Windows/macOS build matrix at commit `9f266421` on 2026-11-21. This verifies **only** the current generic RPN core and its small CTest suite, not a four-level historical model, iOS or App Store.
