---
chunk_kind: "child"
pattern_id: "E.4"
pattern_title: "FPF Ecosystem Family Architecture"
section_id: "E.4:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4/E.4__005_solution.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "E.4 — FPF Ecosystem Family Architecture"
  - "E.4:4 — Solution"
line_start: 48931
line_end: 48940
dependencies:
  - "E.1"
  - "E.5.3"
keywords:
  - "Conceptual Core"
  - "Pedagogical Companion"
  - "Tooling Reference"
  - "canon"
  - "ecosystem families"
  - "linter"
  - "tutorial"
---

### E.4:4 - Solution

The FPF ecosystem is formally stratified into three canonical **FPF ecosystem families**. Each family has a distinct purpose and is governed by different rules, ensuring a clear separation of concerns. The interaction between these families is governed by the **Unidirectional Dependency Principle** (see Guard-Rail E.5.3).

1.  **The Conceptual Core (The Canon):** This family contains the **normative** FPF patterns, kernel definitions, rules, and invariants. It is the canonical FPF pattern set for universal FPF content. It is defined to be tool-agnostic and notation-independent.

2.  **The Tooling Reference:** This family contains executable tools and machine-checkable support publications that implement or verify the normative rules of the Core. This includes reference linters, simulators, and data schemas. This family makes Core rules operational without becoming the Core pattern set.

3.  **The Pedagogical Companion:** This family contains **non-normative, didactic publications** designed to help humans learn and apply FPF. This includes tutorials, worked examples, and playbooks. This family explains the Core and the Tooling Reference without changing Core meaning.

