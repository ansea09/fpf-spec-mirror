---
chunk_kind: "child"
pattern_id: "A.1.1"
pattern_title: "U.BoundedContext: The Semantic Frame"
section_id: "A.1.1:12"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.1.1/A.1.1__013_relations.md"
commit_sha: "3d19010169827708d0bca36d0551af8323908640"
heading_path:
  - "A.1.1 — U.BoundedContext: The Semantic Frame"
  - "A.1.1:12 — Relations"
line_start: 1503
line_end: 1514
dependencies:
  - "A.1"
  - "A.2.1"
  - "D.3"
  - "D.CTX"
  - "E.10.D1"
  - "F.0.1"
  - "U.Boundary"
  - "U.BoundedContext"
  - "U.Holon"
keywords:
  - "DDD"
  - "context"
  - "domain"
  - "glossary"
  - "invariants"
  - "local meaning"
  - "semantic boundary"
---

### A.1.1:12 - Relations

*   **Constitutes:** The foundational "semantic space" for patterns like `A.2 Role Taxonomy` and `A.13 The Agential Role`.
*   **Builds on:** `A.1 Holonic Foundation`, as a `U.BoundedContext` is itself a `U.Holon`.
*   **Constrained by:** `E.10.D1 D.CTX`, which fixes the lexical discipline for “Context”, forbids context hierarchies, and makes Domain family informative.
*   **Interacts with:**
    *   `Norm-CAL`: A context's `Invariants` are typically expressed as `U.ConstraintRule`s.
    *   `Lang-CHR`: A context's `Glossary` is a collection of `U.Lexeme`s.
    *   `Decsn-CAL`: Decisions and objectives are often scoped to a specific context.
    *   `F.9 Alignment & Bridge`: the canonical FPF pattern for cross-context relations and loss policies.
*   **Enables:** The resolution of conflicts as modeled in `D.3 Holonic Conflict Topology`, by showing that many conflicts are context-dependent.

