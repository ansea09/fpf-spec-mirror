---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__014_consequences.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:9 — Consequences"
line_start: 5556
line_end: 5570
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

- Method role-admission checks can use declared role substitutions without encoding taxonomy in every method-description source.
- Separation-of-duties and independence claims become inspectable relations over assignments and windows.
- Frequent role conjunctions can be named without creating fake holders or capabilities.
- Role relation structure remains small enough to use in ordinary project work.

**Costs.**

- Contexts need to declare their role relations instead of relying on job-title intuition.
- Some role-like source labels need F-family cross-context repair before role relation structure can be reused.
- Capability-fit conditions and method role-admission conditions need separate claims when role labels used to hide them.

