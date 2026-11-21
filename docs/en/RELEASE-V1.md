# iPhone classic RPN V1.0 — scope, exclusions and release evidence

**Normative release priority:** classic, useful, trustworthy scientific RPN calculator first. The planned stand-alone ALG app and all deep historical compatibility do **not** gate this release. The V1.0 product is **not yet implemented or published**.

**Design evidence under review:** [V1 function/key candidate matrix](../de/V1-FUNKTIONS-UND-TASTATURMATRIX.md), [ADR index](../adr/README.md), [test/release plan](../de/V1-TEST-UND-FREIGABEPLAN.md). These are proposals, not approved key/stack/numeric/iOS contracts. The actual M2 release criteria are unchanged.

## Release behavior

- Native iPhone interface, usable on the iPhone XS target with validated Xcode deployment version, readable screen, responsive keypad, accurate tactile interaction and accessibility.
- First-screen portrait layout consists of calculator display and complete **approved** key inventory; optional desktop panes are not visible. Shift/Alpha/soft-menu handling must match the approved specification, not generated artwork.
- Classic four-level-oriented RPN interaction, ENTER/stack lift/drop and registers with approved exact model, common scientific functions, angle modes and defined errors.
- Versioned persistent state with atomic restore and tested corrupted-file handling; nothing lost on background/restart/upgrade.
- Entire calculation, help minimum and state restoration available in airplane mode, with no ads, subscription, forced registration or permanent server. Free price is a preference, subject to separate release decision.
- Subtle top-left clickable `SASD` label leading to a verified official SASD URL (not yet entered in source/spec).
- Version-specific, legally reviewed supported-features and compatibility matrix; real device screenshots for App Store rather than artwork mockups.

## Not a V1.0 gate

Historic 41 FOCAL/User RPL, 41 synthetic programming/Byte Grabber, System RPL, Saturn/Nut machines, hardware/OS emulation, ROM collections, complete legacy memory profiles, expansion cards, Advantage Pac, full desktop editor, advanced lessons, Financial, ALG app or an ALG/RPN switch in the classic app.

## Mandatory decision freezes before feature work

| ID | Decision | Owner/action |
| --- | --- | --- |
| V1-OD01 | Exact primary/shift/Alpha key inventory and display modes | Historical key reference + independent SASD layout review |
| V1-OD02 | Four-level behavior, LAST X, ENTER, digit entry, clear/undo | State-transition table and golden tests |
| V1-OD03 | Numeric type, precision, rounding, underflow/overflow, error precedence | Approved numeric contract and tests |
| V1-OD04 | Commands, angle modes and minimum common scientific set | Feature matrix with test mapping |
| V1-OD05 | Snapshot format, schema migrations, recovery | Documented persistence contract |
| V1-OD06 | iOS minimum, iPhone XS build/device setup, bundle identity | Physical-device/toolchain verification |
| V1-OD07 | Official SASD URL, legal assets and privacy/App Store packaging | Release compliance review |

These are *implementation design decisions*, not an invitation to debate full historic emulation again.

## Evidence checklist

- [ ] Approved V1 key/command inventory and numerics.
- [ ] Unit/property/error/persistence/ABI/UI tests green; documented test run IDs.
- [ ] Physical iPhone XS and other supported device QA; VoiceOver and touch areas.
- [ ] State recovery after termination/upgrade verified.
- [ ] Offline with no ads/telemetry requirement or unapproved network services.
- [ ] Accurate product listing with actual build screenshots and trademark/assets audit.
- [ ] No known severe calculation, crash, security or data-loss defects.
- [ ] Signed release record: Git commit, app version, platforms/devices, reviewer, date and limitations.

See [release checklist](RELEASE-CHECKLIST.md), [requirements matrix](REQUIREMENTS-MATRIX.md), [roadmap](../../ROADMAP.md). The current generic C++ engine is not equivalent to a completed V1.
