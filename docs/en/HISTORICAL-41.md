# Series 41 historical compatibility — implementation plan

**Canonical requirement:** `SASD-CALC-COMPAT-041-SYN`. **Status:** planned; architecture preparation required. **Long-term synthetic minimum:** stage **B**; **C** optional. No part of this document claims historical compatibility of the present generic RPN prototype. M1/M2 classic RPN shipping must not wait for stage B.

## Separate from both the 48 family and modern algebraic input

The future 41-family domain owns the four-level X/Y/Z/T stack, LAST X, stack lift/drop, program entry, register organisation, flags, key assignments, normal FOCAL program control and, later, synthetic execution. A common math function may be reused, but the vintage state transitions are owned by this model.

### Historical state design: required early boundaries

- A 41-family historical register has **56 bits / seven bytes**. Retain all raw bits for unusual/synthetic values; a `double` cannot substitute for raw register state.
- Define byte/nibble ordering and addressing from independent historical references **before implementation**. Seven-byte register storage is a representational option, not a normative C++ layout requirement.
- Historical programs need **lossless byte sequences** as primary stored data; disassembly/listings are derived views, invalidated by byte changes.
- Model status registers, programme pointers, register/program partition, key assignments and memory move side effects as virtual state where supported.
- Model variants (41C/41CV and potential later CX) and extension memory separately. Do not impose a universal flat byte-cap across models.
- All historical memory operations use checked virtual addresses. The host pointer/file system is never accessible by an old program or a Byte Grabber.

### Staged delivery with acceptance

| Stage | Commitment | Acceptance |
| --- | --- | --- |
| Preparation | Architecture/P0 | Roundtrip 56-bit arbitrary patterns; state/bytecode interfaces specified; legal fixture policy |
| Ordinary programs (M3) | Long-term program goal | FOCAL control flow and registers against recorded golden states |
| Synthetic A (M4) | Required developmental stage | Selected documented synthetic bytes decode, execute and preserve expected state |
| Synthetic B (M4+) | **Committed long-term minimum** | Selected historical synthetic programs, status/pointer/key assignments, lossless programme byte exchange and repeatable tests |
| Synthetic C | **Optional** | Byte Grabber/Byte-Hüpfer, more intrusive memory/firmware effects and special pointer behavior when reference evidence supports implementation |

Stage B does **not** automatically imply full microcode/Nut CPU emulation. Stage C may reveal cases requiring deeper firmware/hardware emulation; document deviations rather than claim success.

### Recommended module boundary

```text
calculators/series41/
  core: registers / stack / flags / entry
  memory: register image / program bytes / virtual address layout
  program: FOCAL decode / instructions / control flow
  synthetic: extra decode / stateful operations / key assignments
  modules: time / statistics / advantage-compatible adapters
  io: snapshot and historical import-export adapters
```

Only add physical directories as implementations become real. Do **not** make a second full interpreter for synthetic code: regular and synthetic paths use one consistent virtual 41 state and an extensible byte-command executor.

### Reference regression categories

- Raw 56-bit register pattern import/export and unknown-data preservation.
- Historical program byte roundtrip, decoding of known/unknown commands and state snapshots.
- ENTER/LAST X/stack lift with program calls, flags and error recovery.
- Pointer and status transitions, synthetic assignments and library/module interactions.
- Invalid virtual-memory accesses fail without corrupting host memory; snapshot remains restorable.
- Original binary programme compatibility claims only after independently obtained legal fixtures and reference observations.

### Source bibliography (reference only)

William C. Wickes, *Synthetische Programmierung auf dem HP-41C/CV* (German translation Heinz Dalkowski):
https://www.mh-aerotools.de/hp/heldermann/Synthetische%20Programmierung%20auf%20dem%20HP-41C-CV.pdf

Karl-Heinz Gosmann, *Anwenderhandbuch HP-41C/CV* (1983):
https://literature.hpcalc.org/community/hp41-anwenderhandbuch.pdf

These texts support research and independently written tests; their wording, ROMs and proprietary program code are **not** to be copied into the repository without rights.
