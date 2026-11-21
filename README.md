# SASD Scientific Calculator

[English](README.md) · [Deutsch](README.de.md) · **[Full requirements / Lastenheft (DE)](docs/LASTENHEFT.md)** · **[Technical specification / Pflichtenheft (DE)](docs/PFLICHTENHEFT.md)** · [Roadmap](ROADMAP.md) · **[Gesamtarchitektur (DE)](docs/ARCHITEKTUR.md)** · [Architecture summary (EN)](docs/en/ARCHITECTURE.md) · [Compatibility](docs/en/COMPATIBILITY.md)

<p align="center"><img src="docs/images/science-icon-concept.svg" alt="Scientific calculator icon concept: sine and cosine" width="136"></p>

**A classic, stack-based scientific calculator for modern devices.**

> **Status — early engineering foundation, not a released app.** The portable C++ development core currently implements a small, tested arithmetic RPN slice. There is **no iPhone application, historical program interpreter, desktop IDE, or downloadable product release yet**. The pictures below are generated **design concepts**, not application screenshots. The feature descriptions distinguish confirmed direction from future work.

## The product we are building

The first user-facing deliverable is a **polished, reliable, offline, ad-free and subscription-free iPhone scientific RPN calculator**, including an older iPhone XS target. A free app is preferred if sustainable. A full vintage emulator is **not** required for version 1.0.

Our guiding decision is **platform strategy C, executed with priority A**: build reusable foundations and preserve long-term compatibility ambitions, but allocate initial engineering and release attention to the stand-alone classic calculator. A separate financial calculator is **not** part of this product or its release gate.

### iPhone concept — the calculator fills the screen

<p align="center"><img src="docs/images/ios-calculator-concept.svg" alt="Generated SASD iPhone calculator concept, not a running app" width="340"></p>

Portrait mode should display **only the calculator** — its screen, full keypad, six contextual menu keys where appropriate, Shift/Alpha layers, and a subtle clickable **SASD** mark at top left. No desktop editor, advertisement, permanent toolbar, account, or web service. Correct key mapping and readability take precedence over visual imitation. The concept image is **not** an authoritative keyboard specification.

### Desktop concept — optional development workspace

![Generated concept of a desktop calculator with editor, stack, and library](docs/images/desktop-workspace-concept.svg)

Desktop applications may add an optional editor, stack and variable inspector, program libraries, and debugging tools beside the calculator. These tools must consume the same portable semantics; they must never be mandatory for iPhone operation. The image is a **mockup only**.

## What is real today

| Capability | Status |
| --- | --- |
| Product requirements, prioritization, compatibility tiers, and architecture documents | **Documented** |
| Portable C++20 core: push, duplicate, swap, drop, clear, +, −, ×, ÷ | **Initial working slice** |
| Headless developer CLI and CTest regression checks | **Initial working slice** |
| Scientific functions, registers, modes, and persistent state | **Planned, not implemented** |
| Native iPhone/iPad UI and App Store delivery | **Planned, not implemented** |
| Full vintage user-program compatibility, OS/CPU emulation | **Later milestones; not version-1 blockers** |
| Financial-calculator application | **Separate product/repository; not delivered here** |

Development core operations use host-managed memory, a modern unbounded vector stack, and binary64 arithmetic. They **do not** claim exact historical numeric or stack behavior. The published MIT license applies to this repository; the concept images are included as project artwork, not evidence of production readiness.

## Three scientific experiences — one mathematical foundation

The long-term Scientific monorepo supports **three independently releasable app tracks**, not three copies of the same math engine:

| Experience | Role | Delivery priority |
| --- | --- | --- |
| **Classic RPN** | First, excellent offline iPhone calculator; historically oriented stack/keys | **M1–M2 / V1.0 first** |
| **Algebraic (ALG)** | Separate scientific app with `=`, parentheses, precedence and scientific functions; may later serve as a secondary input mode | **Planned parallel track; not a V1.0 blocker** |
| **Advanced RPL** | Separate object-based historical calculator with User RPL and later system-level compatibility | **Longer-term track** |

All three can share a **SASD Mathematical Core** and metadata; historical execution semantics remain separate. The modern ALG parser is **not** a replacement for historic stored-program interpreters. A fourth combined input-mode app is a future possibility, not a release requirement. The Financial Calculator is a **separate product and repository**.

### The latest visual concepts, not app screenshots

The **iPhone portrait** and **desktop workspace** previews shown above are the repository's *current scalable SVG redrawings* of the last design concepts. They are intentionally not claimed to be pixel-identical copies of the original high-resolution PNG artwork. The latest source concept filenames are `SASD RPN Calculator on iPhone.png` and `SASD RPN Calculator SC-48 Interface.png`. Those original PNGs were retained in the project handoff/library but are **not committed in this repository**. See [image provenance](docs/images/README.md). Neither drawing proves the final key mapping or a running app.

### Requirements and engineering specifications

- [Consolidated acceptance and traceability matrix](docs/en/REQUIREMENTS-MATRIX.md) — V1 vs architecture vs long-term vs optional.
- [Multi-app architecture and dependencies](docs/en/MULTI-APP-ARCHITECTURE.md) and [shared-component policy](docs/en/SHARED-COMPONENTS.md).
- [Algebraic expression language](docs/en/ALGEBRAIC-INPUT.md) — Pratt parser recommendation, precedence and test vectors.
- [Historical Series 41](docs/en/HISTORICAL-41.md) — FOCAL, 56-bit registers, synthetic programming A/B, optional Byte Grabber C.
- [Historical Series 48](docs/en/HISTORICAL-48.md) — User RPL, long-term System RPL, optional Saturn.
- [Historical extensions](docs/en/MODULES.md), [help/training](docs/en/LEARNING.md) and [research references](docs/en/REFERENCE-SOURCES.md).
- [V1.0 release acceptance](docs/en/RELEASE-V1.md), [detailed test matrix](docs/en/TEST-MATRIX.md) and [deliberately deferred decisions](docs/en/DECISION-QUESTIONS.md).


## Concrete V1 design drafts (pending approval)

The [V1 function/key matrix](docs/de/V1-FUNKTIONS-UND-TASTATURMATRIX.md), [RPN/stack ADR](docs/adr/ADR-V1-INPUT.md), [numeric ADR](docs/adr/ADR-V1-NUM.md), [snapshot ADR](docs/adr/ADR-V1-STATE.md), [C++/Swift and iPhone XS ADR](docs/adr/ADR-V1-API.md), and [test/release plan](docs/de/V1-TEST-UND-FREIGABEPLAN.md) are now available in Markdown. **They are drafts, not ratified semantics or implemented features.** The [ADR index](docs/adr/README.md) tracks the required decision gates.

## First release — intentionally narrow

Version 1.0 acceptance is driven by: fundamental and commonly used scientific functions; dependable stack and register operations; explicit error behavior; state restoration after app suspension/restart; reliable and accessible touch interaction; offline use; no advertisements or recurring subscription; tested on supported devices, including the iPhone XS target; and a discreet SASD link. The exact supported iOS versions and App Store entitlements must be verified during implementation. A version number alone is not evidence of release readiness.

Integrated offline documentation and RPN training are important goals, but a large tutorial platform must not delay a functioning calculator.

## Later compatibility, clearly separated

Two **independent historical calculator-family implementations** are envisaged, provisionally called **Series 48** and **Series 41**. Their program languages, register/stack behavior, errors, modules, and internal representations are different; a shared UI or arithmetic library must not blur these boundaries. Historical memory-size restrictions are optional compatibility-test behavior, **not** a limit on host-device RAM.

| Level | Meaning | Planned delivery |
| --- | --- | --- |
| **K1** | Classic function compatibility: key operations, stack, registers, arithmetic semantics | M1–M2, focused version-1 subset |
| **K2** | Historical user programs (e.g. User RPL / FOCAL) | M3 |
| **K3** | System-near programming and undocumented/internal behavior | M4 |
| **K4** | CPU/instruction/hardware compatibility | M5, optional research |

Compatibility is **measured and documented per release**, not asserted based on visual similarity. A feature-level K1 subset is not blanket K1 or complete historical compatibility.

## Technology and architecture

- **Core:** modern, independently written C++20, CMake and automated headless tests; no proprietary firmware or binaries.
- **Native iOS:** proposed SwiftUI frontend with a narrow, versioned C-compatible bridge to the C++ core. Target hardware testing is mandatory.
- **Desktop / other OSes:** Windows, Linux, macOS, iPadOS, Android are future frontend targets. The CLI is a **development tool**, not a shipped replacement app.
- **Reuse:** investigate stable, versioned mathematical components from [SASD Math Toolkit](https://github.com/Robin-Goerlach/SASD-Math-Toolkit) when corresponding **C++** APIs are actually available; do not block the calculator on a different-language implementation or duplicate advanced algorithms without reason.
- **Extension principle:** iOS app lifecycle, key rendering, file access and UI code stay outside calculator semantics.
- **No external service dependency:** calculation and local storage must function without the network.

See [Architecture](docs/en/ARCHITECTURE.md), [Product requirements](docs/en/PRODUCT.md), [Roadmap](ROADMAP.md), [Testing](docs/en/TESTING.md) and [Decision log](docs/en/DECISIONS.md).

## Build the initial developer core

Requirements: C++20 compiler and CMake 3.20 or later. This builds a **minimal non-historical core**, not an iPhone app:

```sh
cmake -S . -B build -DCMAKE_BUILD_TYPE=Debug
cmake --build build --config Debug
ctest --test-dir build -C Debug --output-on-failure
./build/sasd-scientific-cli  # on Windows, run the .exe under build/Debug
```

Example input in the CLI: `push 3`, `push 4`, `+`, `stack`, `quit`. Binary operators consume `y` (next-to-top) and `x` (top). Failed operations leave the stack unchanged. The CLI intentionally has no program loader, persistence, keyboard emulator, or system-RPL interpreter.

## Repository navigation

| File | Purpose |
| --- | --- |
| [README.de.md](README.de.md) | German overview |
| [ROADMAP.md](ROADMAP.md) / [TASKS.md](TASKS.md) | Prioritized release gates and executable backlog |
| [AGENTS.md](AGENTS.md) | Guardrails for Codex and contributors |
| [docs/en/PRODUCT.md](docs/en/PRODUCT.md) | Product requirements, scope, non-goals |
| [docs/en/ARCHITECTURE.md](docs/en/ARCHITECTURE.md) | Boundaries, portability, interfaces, dependency policy |
| [docs/en/COMPATIBILITY.md](docs/en/COMPATIBILITY.md) | K1–K4 and evidence rules |
| [docs/en/KEYBOARD-UX.md](docs/en/KEYBOARD-UX.md) | Mobile/desktop interaction and key mapping plan |
| [docs/en/TESTING.md](docs/en/TESTING.md) | Test strategy and quality gates |
| [docs/en/RELEASE-CHECKLIST.md](docs/en/RELEASE-CHECKLIST.md) | iOS release acceptance |
| [docs/en/DECISIONS.md](docs/en/DECISIONS.md) | Decision register and unresolved questions |
| [CONTRIBUTING.md](CONTRIBUTING.md) / [SECURITY.md](SECURITY.md) | Contribution and responsible reporting |

## Independent product and legal boundaries

**SASD Scientific Calculator** is independently developed and branded. Product screens and README branding do not use another manufacturer's name or logo. A technically accurate third-party compatibility statement may eventually be provided **separately**, after testing and legal review; compatibility is not affiliation. Do not add proprietary ROMs, firmware, manuals, or unlicensed program collections.

**License:** [MIT](LICENSE), as already selected in this GitHub repository. Historical names, images, or other third-party assets are not automatically licensed by that file.

---

**Engineering principle:** ship a trustworthy classic calculator before claiming a complete historical machine.
