# Product requirements (English) — baseline 2026-11-21

## Intent and motivation

Create a **usable, excellent modern classic scientific calculator** on iPhone first. Nostalgia and vintage program compatibility are valuable **future differentiators**, not prerequisites to a first reliable product. Target ordinary calculations and users who prefer UPN/RPN's visible stack logic. App should be self-sufficient offline.

### Product constraints (decided)
- **Scientific** is the product here. **Financial** is separate: another repository/product/release, no blocking dependencies.
- iPhone app first. Includes an **iPhone XS validation target**, subject to current Apple toolchain/device compatibility research.
- No ads, no recurring subscription, offline calculation. Prefer free distribution.
- Main screen in portrait is **calculator only**; no desktop developer panels or intrusive banners.
- Discreet, interactive **SASD** branding/link at top left; not a historic manufacturer's marks.
- Host-managed modern memory. Historical 128K labels/limits are neither an iPhone memory specification nor a default restriction.
- **Strategy C with priority A**: build portable reusable infrastructure but devote first release investment to the classic calculator and its tests.

### M2 version-1 capabilities (requirements, not implemented)
- Human-usable scientific calculation: basic arithmetic, fractions of ordinary scientific work, trig/angle modes, powers/roots, logs/exponentials and clear numeric/error policy. The exact function inventory is approved via a key-by-key specification before freeze.
- Intuitive stack input, entry/ENTER, register/memory support, reliable clear/undo where specified, help for errors.
- Core state restored on app suspension, termination, relaunch and compatible upgrade.
- Responsive keypad including appropriately shifted/Alpha behavior, readable LCD-inspired display, accessibility semantics and touch feedback as appropriate.
- Device-specific constraints: iPhone XS layout, performance, older iOS deployment decisions, rotation policy, dynamic scaling.
- Security/privacy: no account or online service required; explain any telemetry if introduced later (default no tracking).
- Automated unit/integration/retention testing, manual device checks, App Store content/privacy/legal audit.
- Minimal bundled offline help may be in scope; interactive programming courses are **later enhancements**, not release blockers.

### Explicit non-goals for v1.0
- Full historical FOCAL/User RPL execution or imported legacy binary programs.
- System RPL / synthetic low-level execution; original firmware, ROMs, CPU instruction emulation.
- Full legacy keyboard **visual** imitation or an exact historical enclosure.
- Side-by-side desktop program IDE on mobile; permanent network service.
- Financial calculator, Advantage-Pac-equivalent modules, bundled commercial program collections.
- Android/desktop parity, despite planned portable design.

### Later goals (not promises)
- Separate Series 41 & Series 48 behavior engines, with independently documented error, object, register, language and module semantics.
- Historic application programs, system-near features and optional hardware/OS emulation as M3–M5.
- Optional desktop workspace, plotting, program libraries, built-in searchable handbook, interactive RPN tutorials and practical exercises.
- Optional iPad, Android, Windows, Linux and macOS frontends.
- Future extensions require licensing/provenance review and must not distort the first calculator's reliability.

### Acceptance language
Each feature is one of **planned, implemented, verified, explicitly unsupported**. Build/compile success is not runtime acceptance. UI render is not numerical correctness. A video/mockup is not a build. Each released version gets its own evidence-based compatibility matrix.

### Pending product decisions
- Exact V1 scientific key/function list and four-stack-vs-unbounded behavior for a new SASD calculator.
- Policy for numeric precision and exceptional values, angle modes, entry semantics, undo.
- iPhone minimum iOS version, real iPhone XS touch target measurement and App Store constraints.
- Exact restore/backup/export rules and privacy policy content.
These are recorded explicitly rather than invented from images.

## Consolidated product-family decisions (2026-11-21)

**Release order:** classical RPN iPhone M1/M2 has priority; an independent ALG Scientific app and an advanced object/RPL app are *separate planned Scientific experiences* with shared mathematical algorithms and independent release gates. ALG as a later **additional input mode** in historical apps remains permitted. The Financial Calculator is a different product/repository, with separate finance-domain workflows and release obligations.

**Long-term historical obligations:** planned 41 FOCAL, 41 synthetic **stage B**, 48 User RPL and documented System RPL subset remain in the requirements. Byte Grabber C, Nut/Saturn machine emulation and full vintage hardware/OS remain **optional**. None block M2. Features are only called compatible following recorded model-specific reference evidence. The 48GX 128-KiB built-in RAM concept belongs to opt-in historical profiles, never to the modern iPhone memory budget.

**Later nonblocking extensions:** Time and Statistics modules; selected Advantage-Pac-inspired *functions* via common numerical algorithms, not historical ROMs; bilingual offline help and interactive RPN/ALG training. The common mathematical core is separately reusable with Financial only after proven stable APIs exist.

For exact status/priorities see [requirements matrix](REQUIREMENTS-MATRIX.md), [V1 contract](RELEASE-V1.md), [APP architecture](MULTI-APP-ARCHITECTURE.md), [historical 41](HISTORICAL-41.md), [historical 48](HISTORICAL-48.md).
