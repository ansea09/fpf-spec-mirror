---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__015_rationale.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:10 — Rationale"
line_start: 5346
line_end: 5349
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

