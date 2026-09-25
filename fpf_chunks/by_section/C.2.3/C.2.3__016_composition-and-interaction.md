---
chunk_kind: "child"
pattern_id: "C.2.3"
pattern_title: "Unified Formality Characteristic F"
section_id: "C.2.3:15"
section_title: "Composition and Interaction"
source_path: "FPF-Spec.md"
output_path: "by_section/C.2.3/C.2.3__016_composition-and-interaction.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "C.2.3 — Unified Formality Characteristic F"
  - "C.2.3:15 — Composition and Interaction"
line_start: 49189
line_end: 49208
dependencies:
  - "A.16"
  - "A.18"
  - "A.19"
  - "B.3"
  - "C.19.2"
  - "C.2"
  - "C.2.2"
  - "C.2.4"
  - "C.2.5"
  - "C.2.6"
  - "C.2.7"
  - "C.2.LS"
  - "F.9"
keywords:
  - "F-scale"
  - "F0-F9"
  - "Formality"
  - "language-state separation"
  - "proof"
  - "rigor"
  - "specification"
---

### C.2.3:15 - Composition and Interaction

#### C.2.3:15.1 - Weakest-essential-support rule

Identify the assessed episteme’s expressed claim or argument and the compositional support relation it actually uses. Its F is bounded by the least-formal essential content or inference within that assessed expression. A machine-checked annex does not make an informal connecting inference machine-checked.

External evidence has a different role. A typed claim supported by an informal observation can remain F4 because its predicates and types are explicit, while its warrant remains weak or unresolved under B.3. If the assessed bearer is instead the whole argument, an essential inference expressed only as controlled prose caps that argument at F3 despite an F7 annex. Name that bearer and inference; do not take a minimum over every external source in an evidence chain.

#### C.2.3:15.2 - Relation to `G`

`F` concerns expression form; `G` concerns applicability or claim scope. Tightening scope may accompany a raise in `F`, but it is a separate change and must remain visible as such.

#### C.2.3:15.3 - Relation to `R`

Higher `F` often makes evidence easier to formulate, test, or prove, but it does not create warrant strength by itself. Empirical freshness, corroboration, and bridge penalties remain `R` concerns.

#### C.2.3:15.4 - Relation to `CL` and Bridges

A bridge may expose loss or mismatch across contexts. Preserve that limitation for the actual receiving use and assess any R effect under its justified model; the loss does not silently lower or raise the attributed F. A receiving rewrite that changes claim content, EntityOfConcern, or the effective reference scheme identifies a new episteme under `C.2.1`; that episteme should be published with its own `F`.

