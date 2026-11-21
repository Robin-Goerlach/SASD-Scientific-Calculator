# iPhone V1.0 release checklist

**This is a future acceptance gate, not a claim that the app exists.** A single unchecked P0 item blocks the V1 declaration.

**Execution-ready draft test plan:** [V1 test and release plan](../de/V1-TEST-UND-FREIGABEPLAN.md), supported by the [proposed V1 ADRs](../adr/README.md) and [function/key candidate matrix](../de/V1-FUNKTIONS-UND-TASTATURMATRIX.md). **No test is marked PASS simply because these documents exist.**

## Calculator quality (P0)
- [ ] Approved and complete V1 key/function inventory, with Shift/Alpha context verified.
- [ ] Stack, registers, numeric domain, error semantics, angles and modes tested.
- [ ] All calculator functions available offline; reliable cold start and foreground resume.
- [ ] Versioned state saved and restored after suspend/terminate/update, with corruption recovery.
- [ ] Touch, display scaling, accessibility and safe-area checks on **iPhone XS**.
- [ ] High-priority crash/performance regressions resolved, core/bridge/UI tests passing.
- [ ] App starts and calculates without an account, internet, ads or subscriptions.
- [ ] Discreet clickable SASD label top left tested without obstructing keys.

## Platform and legal (P0)
- [ ] Minimum iOS deployment supported by current toolchain and validated on physical target.
- [ ] App metadata, privacy labels and permissions correspond to actual behavior.
- [ ] App Store packaging, signing, screenshots **from a real build** and review-ready archive.
- [ ] License, third-party dependencies, artwork, trademark/design and copyright checks documented.
- [ ] No foreign ROMs, firmware, manuals, unlicensed programs or vendor branding.
- [ ] Build/release reproducibility and independent installation/relaunch validated.
- [ ] Version-tagged release notes enumerate **actual** functionality and known limits.

## Optional/nonblocking after V1
- [ ] Full family-specific historical user-program languages (M3).
- [ ] System-near languages and low-level execution (M4).
- [ ] CPU/OS emulation experiments (M5).
- [ ] Desktop IDE, iPad/Android parity, advanced tutorials and financial features.

**Release decision:** date/commit, tested devices, evidence links, reviewer and outstanding known issues must be recorded when the gate is actually performed.

**Traceability supplement:** consult the [V1.0 scope and open design freezes](RELEASE-V1.md) and [per-requirement matrix](REQUIREMENTS-MATRIX.md). The first release is **Classic RPN**, independent from planned stand-alone ALG and advanced RPL Scientific apps. Neither synthetic 41 stage B nor bounded System RPL is removed from the *long-term* roadmap, but neither may block this release.
