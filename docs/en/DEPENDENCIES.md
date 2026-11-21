# Dependency boundaries

## Already required
- **CMake ≥3.20**, **C++20** compiler and C++ standard library.
- Local CTest; no third-party runtime library needed for the initial arithmetic engine.
- GitHub Actions standard hosted runner toolchains for desktop CI.

## Proposed, not yet integrated
- SwiftUI and the Apple toolchain for an iPhone frontend.
- An explicit C ABI bridge (ownership, errors, UTF-8, versions) for native interoperation.
- Stable **C++** interfaces from SASD Math Toolkit for advanced operations when they exist and pass readiness tests.
- Family-specific historical interpreters and test fixtures in later milestones.
- Desktop UI toolkit only after iPhone prioritization is maintained.

**Do not** pull in a .NET runtime on iPhone solely because the related mathematics repository currently has a C# implementation. A math-library dependency must be versioned, buildable on every target that uses it, licensed compatibly, and have compatibility tests. Keep Financial Calculator releases wholly decoupled.
