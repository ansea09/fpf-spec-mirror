---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__014_consequences.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:9 — Consequences"
line_start: 5228
line_end: 5242
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

### A.2.7:9 - Consequences

**Benefits.**

- Method requirements can accept declared role substitutions without encoding taxonomy in every method step.
- Separation-of-duties and independence claims become inspectable relations over assignments and windows.
- Frequent role conjunctions can be named without creating fake holders or capabilities.
- Role relation structure remains small enough to use in ordinary project work.

**Costs.**

- Contexts need to declare their role relations instead of relying on job-title intuition.
- Some role-like source labels need F-family cross-context repair before role relation structure can be reused.
- Capability and method requirements need separate claims when role labels used to hide them.

