---
chunk_kind: "child"
pattern_id: "A.5"
pattern_title: "Open-Ended FPF Kernel and Extension Layering"
section_id: "A.5:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.5/A.5__005_solution.md"
commit_sha: "55ef163f91d42b48785bd297b50322e072d0a950"
heading_path:
  - "A.5 — Open-Ended FPF Kernel and Extension Layering"
  - "A.5:4 — Solution"
line_start: 14220
line_end: 14232
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
2. **Boundary packaging via `U.Signature` (A.6.0).** For reusable declaration bundles admitted as signatures under **A.6.0**, expose declaration dependencies in a `SignatureManifest` (`imports`, `provides`).
3. **Distinguish dependency from declaration comparison.** `imports` forms a dependency DAG constrained by **E.5.3**. Compare declarations under the predicate for the claimed relation. For mechanism declarations, **A.6.1:4.8** distinguishes refinement, conservative extension and equivalence by their preservation tests. Use **C.29** when a mathematical morphism is claimed.
4. **Registry references stay references.** Registry identifiers, such as Bridge ids, policy‑ids and edition‑ids in Part F, are cited or pinned where needed, not treated as exported symbols in `provides`.

For example, an extension describes a cooling Method under specified fluid and operating-range assumptions. Keep those assumptions and its heat-transfer law with the extension. If its declaration bundle is admitted as a `U.Signature`, its manifest identifies the scale declaration it imports and the declarations it provides. A changed scale declaration directs attention to the cooling claims that depend on it. A changed fluid assumption instead requires reconsidering uses that rely on that applicability condition; it does not make the assumption a Kernel law. This connects a local revision to its affected uses while preserving unrelated contributions.

