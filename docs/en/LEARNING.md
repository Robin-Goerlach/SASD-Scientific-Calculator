# Offline help, reference and interactive education

**Intent:** a calculator that is usable immediately and can teach unfamiliar stack notation. Documentation must describe actual supported commands, not planned historical functions.

## Three content layers

1. **Contextual help** — per active key, state, errors, angle modes and ENTER/stack behavior; usable offline with short DE/EN explanations. **Small V1 minimum** after the key map is frozen.
2. **Searchable manual** — bilingual scientific command reference, RPN primer, independent ALG syntax, examples, registers/stack and explicitly marked historical differences. Offline-first; optional online source updates, never a calculator dependency.
3. **Interactive lessons** — entry and stack visualization; compare `3 ENTER 4 ENTER 5 × +` with `3 + 4 × 5`, precedence, error diagnosis, simple scientific missions; later programmer/RPL/module learning tracks.

## Architecture contract

Keep a single command/function metadata source for supported calculator variants, input arguments, types, error and numeric context, help identifiers and references. Do not hard-code a second mathematical engine for teaching. Lessons execute through the same application commands as the ordinary UI. Optional stepwise traces are produced from the real evaluator/stack transitions, sanitized for display.

## Milestone rules

- M2: brief offline starter help and accessible error explanations **as approved by the V1 scope**.
- After M2: richer DE/EN manual, indexed search, exercises and progress saving.
- Later: optional AST evaluation trace, debugger, synthetic 41 and RPL programming courses where corresponding engines actually exist.

Avoid copyrighted reproductions of historical manuals. Publish original explanations and examples with proper provenance for historical comparisons. Exercises must remain fun and practical without disguising a speculative feature as implemented.
