---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__015_rationale.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:10 — Rationale"
line_start: 5203
line_end: 5206
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.5"
keywords:
  - "bundles (⊗)"
  - "incompatibility (⊥)"
  - "requiredRoles substitution"
  - "role algebra"
  - "separation of duties (SoD)"
  - "specialization (≤)"
---

### A.2.7:10 - Rationale

A.2.7 keeps role relation structure as a selected relation structure rather than a new U-kind because the durable object is still `U.Role` and its contextual use through assignments, states, methods, and work claims. This preserves ordinary role naming while preventing algebraic notation or organizational labels from becoming a second ontology.

