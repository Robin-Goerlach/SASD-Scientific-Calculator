# Compatibility model and evidence rules

**Do not equate product release milestones M0–M5 with compatibility levels K1–K4.** A finished M2 iPhone app may implement only a documented portion of K1. Levels describe **observable compatibility claims**; milestones describe delivery phases.

| Level | Definition | Intended milestone | Initial status |
| --- | --- | --- | --- |
| **K1** | Classic function behavior: keys, stack/registers, arithmetic semantics, errors and familiar workflows | M1–M2 | **Subset underway; not verified as a historical match** |
| **K2** | Historical user programs, including separately specified FOCAL and User RPL source semantics | M3 | **Not implemented** |
| **K3** | System-near programming, internals, synthetic paths and System RPL | M4 | **Not implemented** |
| **K4** | CPU instructions, memory-mapped hardware and machine/OS-dependent execution | M5 optional | **Not implemented** |

## Independence of families

The historic **Series 41** and **Series 48** targets require **separate** specification and execution models. Even when a user action appears similar, register depths, objects, numeric representations, error and program semantics may differ. No generic stack implementation should be called a faithful family emulator without independent evidence. Optional time/statistics/other modules must be versioned, licensed and tested separately.

## Measurable claims

Future release compatibility documentation should list:
1. Published SASD version/commit and operating system.
2. Affected model and mode/profile; compatibility level (K1–K4).
3. Named behavior/command/program and expectation.
4. Fixture origin and redistribution rights (and citations if public).
5. Automated test reference plus physical/reference-device observations where possible.
6. **Supported / partial / unsupported / untested**, known limitations and regressions.
7. Date of last verification.

Suggested CSV schema: `release,model,level,feature,source,fixture,test,status,limits,last_verified`. **A checked box is not evidence** without a running test or verified observation.

## Technical exclusions / risk

- No proprietary ROM, firmware, copyrighted operating-system image, unlicensed manual or sourced commercial program included.
- CPU-specific behavior can make behavior-level compatibility impossible; classify rather than hide it.
- Historical memory limits are **opt-in per profile**, not the host application's resource budget.
- Exact legacy numeric fidelity and file formats must be tested before claiming compatibility.
- Personal reference-device photographs inform key inventory, but generated mockups cannot establish the true key map.
- Main product branding uses SASD only. Third-party names may be used only factually in future tested compatibility notes after rights review.

## Initial working-core classification
As of bootstrap, **no historical compatibility level is certified**. The demonstrated generic stack operations are a starting point toward an eventual **subset of K1**, not an emulated historical machine.

## Commitment versus delivery detail

The planning decision to ship classic V1 before historical programs **does not cancel** the later committed stage-B synthetic 41 program goal or bounded System RPL compatibility. Their normative planning IDs are `SASD-CALC-COMPAT-041-SYN` and `SASD-CALC-COMPAT-048-SYSRPL`; Saturn remains optional. The optional Byte Grabber stage C is **not** mandatory. See [41 details](HISTORICAL-41.md), [48 details](HISTORICAL-48.md) and the [requirements matrix](REQUIREMENTS-MATRIX.md).

The documented K1–K4 *target level* is independent of a feature's evidence grade: syntax recognized, function executed, behavioral match, historical system-state match, and machine-instruction emulation. For every programme/command report the exact tested scope and ROM/model profile; do not infer historic fidelity from mathematical output alone. The interactive modern ALG app has no automatic historical compatibility grade.
