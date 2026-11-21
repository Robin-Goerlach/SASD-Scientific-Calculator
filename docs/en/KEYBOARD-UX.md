# Keyboard, display and interaction specification

## Input references, not unquestioned artwork

A real reference calculator photograph from project discussion shows more keys than the early generated mockups. Before any fidelity or feature-coverage claim, prepare an independently reviewed **key inventory** with: physical key, shifted/Alpha action, context/soft-menu action, label, core command, error behavior and test. The latest iPhone/desktop images in `docs/images/` are **generated concepts only** and contain possible textual and layout inaccuracies.

## iPhone portrait requirements
- Fill available app content with the **calculator itself**: screen + full practical keypad. No permanent editor, desktop panels or intrusive toolbars.
- Provide six soft-menu positions where the chosen mode requires them, plus appropriate Shift and Alpha layers. Avoid dropping or inventing key bindings due to mockup limitations.
- Keep tap areas sufficiently large for the smallest supported iPhone; measure on **iPhone XS** and verify safe areas, font sizes, gesture conflicts, Dynamic Type or alternate accessibility mode.
- Favor reliable entry, response and legible keys over a photorealistic copy of a particular shell.
- Show a discreet **SASD** label in the upper-left of the calculator that is an accessible link; don't sacrifice calculation area or key targets.
- State/result view must remain readable in portrait without a network connection. Provide meaningful access labels for keys and status.

## Desktop
- Default to a complete calculator view.
- Optional resizable panes: editor, stack/registers, libraries and debugging. Pane visibility must not alter core results.
- Keyboard/mouse shortcuts must map to the same canonical commands as mobile touches.
- State is shared in semantics, not necessarily in per-device screen layout.

## Required key coverage matrix (not yet populated)
| Key / context | Primary action | Shift action | Alpha action | Core command | V1 required? | Unit/UI test |
| --- | --- | --- | --- | --- | --- | --- |
| Enter / stack input | **TBD** | **TBD** | **TBD** | **TBD** | likely | pending approval |
| Arithmetic keys | **TBD** | **TBD** | **TBD** | **TBD** | yes | pending |
| Trigonometry | **TBD** | **TBD** | **TBD** | **TBD** | yes | pending |
| Menus / navigation | **TBD** | **TBD** | **TBD** | **TBD** | by mode | pending |

**Important:** we do not invent exact historical labels based on an image model. Final layout awaits key-by-key review and copyright/design review. The V1 design can be an independent SASD arrangement while implementing selected compatible behaviors.
