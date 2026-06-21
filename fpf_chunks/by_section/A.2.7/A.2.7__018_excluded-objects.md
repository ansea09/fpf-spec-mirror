---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:12"
section_title: "Excluded Objects"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__018_excluded-objects.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:12 — Excluded Objects"
line_start: 5264
line_end: 5276
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

### A.2.7:12 - Excluded Objects

Do not use `RoleRelationStructure@BoundedContext` or a role-algebra lens as the current object for:

- holder taxonomy, system kind hierarchy, or org chart hierarchy;
- capability model, skill model, performance threshold, or operating envelope;
- method family, algorithm family, or work procedure;
- work plan, work occurrence, approval act, or audit record;
- evidence graph, source record, standard, report, dashboard, publication, or model card;
- cross-context translation, public naming, or bridge claim.

Those values may cite or justify a role relation. They do not become role relation structure by adjacency.

