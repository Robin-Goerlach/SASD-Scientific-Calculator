# Contributing

The repository is currently an early engineering foundation. Improvements to reproducible builds, numerical tests, portability, accessibility and documentation are welcome. Focus on **M1/M2**; compatibility archaeology and optional desktop work must not displace the first usable iPhone app.

## Proposed workflow
1. Read `AGENTS.md`, `ROADMAP.md` and `docs/en/DECISIONS.md`.
2. For behavioral changes, describe the operation's input, stack arity, numeric behavior and error semantics *before* writing tests/code.
3. Add tests and run CMake/CTest locally; document unavailable platform tests honestly.
4. Keep changes small with English technical docs and update the German overview for visible feature status changes.
5. Distinguish **planned**, **implemented**, and **verified**; do not claim historical compatibility from visual resemblance.
6. Document the license/provenance for outside test data; do not include proprietary firmware/manuals/program collections.
7. Prefer direct `main` commits for safe, verified solo-maintainer work; use a branch/PR when review or risk isolation helps.

The repository's existing **MIT** license remains authoritative. Source contributions should be intended for distribution under that license unless the maintainer explicitly agrees otherwise.

Do not create release tags, upload real-device screenshots, or state that an App Store review passed without independent confirmation.
