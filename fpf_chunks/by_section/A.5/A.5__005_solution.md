---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open-Ended FPF Kernel and Extension Layering"
section_id: "A.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__005_solution.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "A.5 — Open-Ended FPF Kernel and Extension Layering"
  - "A.5:4 — Solution"
line_start: 13605
line_end: 13617
dependencies:
keywords:
  - "FPF architecture"
  - "declarative modularity"
  - "dependency versus specialization"
  - "domain extensions"
  - "extensibility"
  - "kernel boundaries"
---

### A.5:4 - Solution

FPF pattern texts publish law-governed declarations—vocabulary, laws and applicability—that can be reused and specialized.

To keep the Kernel open‑ended, use the following boundary rules:

1. **Kernel minimality (C‑5).** Domain knowledge stays outside the Kernel by default; it enters as extension vocabularies and laws.
2. **Boundary packaging via `U.Signature` (A.6.0).** For reusable declaration bundles admitted as signatures under **A.6.0**, expose actual declaration dependencies in an explicit `SignatureManifest` (`imports`, `provides`).
3. **Dependency vs specialisation are separate relations.** `imports` forms a dependency DAG constrained by **E.5.3**; refinement/extension (`⊑`, `⊑⁺`) is expressed separately (for mechanism declarations, see **A.6.1:4.8**; use **C.29** when a mathematical morphism is claimed) and should not be conflated with `imports`.
4. **Registry references stay references.** Registry identifiers, such as Bridge ids, policy‑ids and edition‑ids in Part F, are cited or pinned where needed, not treated as exported symbols in `provides`.

For example, an extension describes a cooling Method under specified fluid and operating-range assumptions. Keep those assumptions and its heat-transfer law with the extension. If its declaration bundle is admitted as a `U.Signature`, its manifest identifies the scale declaration it imports and the declarations it provides. A changed scale declaration directs attention to the cooling claims that depend on it. A changed fluid assumption instead requires reconsidering uses that rely on that applicability condition; it does not make the assumption a Kernel law. This connects a local revision to its affected uses while preserving unrelated contributions.

