# Series 48 historical RPL and system compatibility

**Canonical requirement:** `SASD-CALC-COMPAT-048-SYSRPL`, planned, architecture preparation required; **documented subset of historical System RPL is a long-term commitment**, **not V1**. `SASD-CALC-COMPAT-048-SATURN` remains optional long-term research.

## Program levels and sequencing

| Layer | Goal | Status / scheduling |
| --- | --- | --- |
| User RPL | Object stack, real/complex numbers, algebraic objects, names/directories, programs/control flow, lists, vectors/matrices and documented errors | M3; **highest functional priority inside this family** |
| System RPL | Internal objects, system primitives, virtual stack/return stack operations, memory/object lifecycle and selected documented historical programs | M4; long-term committed in a **bounded reference-tested** scope |
| Saturn machine instructions | Optional interpreter/emulator for historic executable code and hardware-visible state | M5; research only, **not required** for V1 or all System RPL |

System RPL is **not** an extra synonym for ordinary mathematical function calls. User/System RPL may share a runtime where semantics overlap, but internal primitives and validation differ. Never route either stored program through the modern Pratt algebraic input parser.

## Historical objects and memory

- Keep a logical RPL object API **and** a lossless mapping/representation for supported historical objects, prologues, sizes, nibbles and references.
- A Saturn-based virtual address space is **model-specific**; it is not a 41 seven-byte register map and never a native host pointer.
- Distinguish data stack, return stack and executing program context. Store model, ROM compatibility profile, RAM/ROM region mapping and available cards.
- The 48GX built-in **128 KiB RAM** is a base configuration, not a hard application memory cap. Optional cards and actual usable memory accounting are separately modelled. Memory reporting must reflect chosen historical profile when that is implemented.
- If user edits only a logical object, a deliberate serializer owns converting it to historical bytes/nibbles. Unchanged imported objects retain unknown/proprietary fields where a lossless roundtrip is promised.
- A modern C++ value abstraction cannot be the **sole** source of truth for low-level System RPL state, pointers and exotic object encodings.

## Virtual system calls and ROM profiles

- `SYSEVAL`: resolve virtual historical address under a documented model/ROM profile to an explicitly supported virtual operation.
- `LIBEVAL`: resolve supported library command identifiers via a versioned virtual library registry.
- Unsupported symbols, wrong ROM profile and invalid virtual ranges lead to **controlled virtual failures**, never arbitrary host calls.
- Keep historical ROM differences in data-driven profiles and test fixtures, **not** ad hoc absolute pointers into C++ functions.
- Avoid committing proprietary ROM images, copyrighted programmer documentation or unlicensed sample libraries.
- Whether any targeted reference program **requires** Saturn instruction execution is an evidence-based later decision, not an assumption.

## Target ownership

```text
calculators/series48/
  objects: logical types + historical codec + validation
  runtime: stack, return stack, execution frames, error state
  rpl: user program evaluator; system primitives separately gated
  memory: virtual Saturn address space; ROM/RAM/card profiles
  system: address/library call dispatcher and ROM symbol maps
  saturn: future OPTIONAL CPU adapter (not present)
```

### Conformance and safety gates

1. User RPL reference programs and object/stack transitions before System RPL changes.
2. Historical object/nibble roundtrip for explicitly supported types; errors on unsupported types.
3. System RPL primitive result plus expected stack, return stack, object-memory and error-state changes.
4. `SYSEVAL` and `LIBEVAL` known-address/library maps, wrong-ROM maps and unresolved targets.
5. Snapshots with ROM profile identity, deterministic restore and corruption checks.
6. Malicious or malformed object/program cannot read host memory or escape the virtual address space.
7. Re-run User RPL golden programmes whenever a System RPL primitive or shared object codec changes.
8. Publish *syntactic / functional / behavioral / system / machine* evidence separately within compatibility K1–K4.

## Research references (not redistributable implementation)

Jim Donnelly, *An Introduction to HP 48 System RPL and Assembly Language Programming*:
https://literature.hpcalc.org/items/1474

Eduardo Kalinowski, *Programming in System RPL*:
https://literature.hpcalc.org/items/1695

These are historical sources to consult and cite when selecting independently authored tests; do not extract copyrighted text, ROM routines or third-party code into SASD source.
