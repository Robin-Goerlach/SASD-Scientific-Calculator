# Algebraic input — specification and integration

**Status:** Planned, independent Scientific app track and reusable input mode; *no parser implementation yet*. **Not a classic iPhone RPN V1 release blocker.** The same neutral parser may later be reused for modern input in historical-model apps, without executing stored historical programs through it.

## Semantics and testable examples

| Expression | Expected under modern ALG syntax | Rule |
| --- | ---: | --- |
| `3 + 4 * 5` | `23` | multiplication precedence |
| `(3 + 4) * 5` | `35` | grouping |
| `2 + 3^2` | `11` | exponent before addition |
| `20 / 4 * 2` | `10` | left-associative × / ÷ |
| `2^3^2` | `512` | right-associative power |
| `-(3 + 4)` | `-7` | unary negation |
| `(3 + 4 * 5^2) / 2` | `51.5` | nested priorities |
| `-2^2` | `-4` | chosen: power before unary minus |
| `(-2)^2` | `4` | explicit grouping |
| `2^-3` | `0.125` | signed exponent |

The examples above are **proposed normative modern-ALG grammar rules**; historical algebraic objects and EquationWriter-like behavior in the 48 family must be specified independently. Use a canonical operator/token set internally; UI may render `×`, `÷`, superscripts and localized separators. No assumption that visual button labels define exact grammar.

## Parser recommendation and rationale

**Recommended design:** a lexer, a Pratt precedence parser for mathematical expressions, small recursive-descent routines for primary forms (parentheses, calls, argument lists), a typed AST, separate name/type resolution and a model-specific evaluator. This combines Pratt's compact extensible binding-power tables with recursive descent's clarity for structured syntax. A pure precedence-ladder recursive-descent implementation is simple for a tiny grammar but expands with each precedence/associativity level. Both designs are independently testable. Record final binding-power/diagnostic rules in an ADR before code.

### Progressive grammar

1. First: finite real literals, explicit `+ - * / ^`, unary `+/-`, grouping and complete-input checks.
2. Then: constants, variables and read-only model-register bindings, named function calls and argument validation.
3. Then: scientific functions and model-appropriate types (complex, vectors/matrices, angle modes).
4. Later: implicit multiplication, percent conventions, postfix operators, symbolic storage, user-defined functions, evaluation traces.

**Still open:** comma decimal vs argument list; localized digit handling; implicit multiplication; `%`; variable shadowing; assignment and side effects; unknown-symbol symbolic vs error; how much of the 48's historical algebraic object syntax is supported.

## Clear execution boundary

```text
typed interactive formula -> tokenize -> AST -> type/name check
  -> evaluate under explicitly chosen numerical context
  -> explicit and validated result-commit operation

historical stored program -> own 41 FOCAL or 48 RPL runtime
  (never through the modern ALG parser)
```

A pure evaluation failure changes no calculator state. Persisted registers, random generator state, clock access, assignments and other side effects must be deliberately classified before such operations are enabled. No unbounded recursion or unchecked memory growth from malformed expressions.

For classic 41-style stacks, define separately whether importing the ALG result raises stack lift, changes LAST X, drops T or touches registers. For the 48-family, distinguish evaluating to a value vs inserting an algebraic object vs symbolic manipulation. The modern parser must not bypass optional historical memory/resource limits for values committed into a historical context.

## Error categories

Lexical, parse, unknown identifier, wrong arity, wrong type, mathematical domain, divide by zero, overflow/underflow, unsupported capability, memory/resource limit and historical-model error. Return stable diagnostic codes + source locations where relevant; translate to a localized friendly message at UI layer. No raw host exceptions escaping the C ABI.

## Cross-engine tests

- Lexer/AST golden: precedence, associativity, token normalization, malformed/nested expressions.
- Evaluator golden: degree vs radians (e.g. `sin(30) = 0.5` in degrees, within numerical policy), precision and domain errors.
- Cross-input compare **mathematical results only when numeric contexts match**; historical stack/resulting states may intentionally differ.
- Regression: switching input mode must not reinterpret or mutate historical program bytes or RPL objects.
- Fuzz/limit: expression length, nesting, parser termination and failure rollback.
