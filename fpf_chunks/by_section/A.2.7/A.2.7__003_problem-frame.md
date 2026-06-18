---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__003_problem-frame.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:1 — Problem Frame"
line_start: 4843
line_end: 4860
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

### A.2.7:1 - Problem Frame

Work governed by role values and role assignments often needs three small claims:

1. One role value can satisfy another role requirement in the same context when a role-requirement substitution relation is declared.
2. Two roles are incompatible for the same holder during overlapping windows.
3. A recurring conjunction of roles can be named as a role bundle expression.

Without a local role relation structure, teams usually encode those claims in the wrong objects:

- a role assignment says "senior inspector" and silently satisfies "inspector" without declared relation;
- a separation-of-duties rule is written as a deontic slogan rather than an incompatibility relation over assignments;
- a role bundle becomes a new holder, capability, work product, or method;
- a cross-context label match is treated as role equivalence;
- method requirements smuggle capability or work claims into role names.

A.2.7 keeps the role relation structure small and local. It says how role values, role descriptions, and role expressions relate; it does not say who holds them, whether holders are able, whether work happened, or whether an episteme proves something. Algebraic, graph, factor, embedding, distributed, neural, or other mathematical descriptions are optional lenses over that structure.

