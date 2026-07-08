---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__003_problem-frame.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:1 — Problem frame"
line_start: 5061
line_end: 5086
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

### A.2.7:1 - Problem frame

**Use this when** a method, work-admission rule, staffing rule, safety case, governance rule, or role description needs a declared context-local relation among role values, role expressions, or role-bundle expressions.

**What goes wrong if missed.** Role labels act as type hierarchy, org chart, permission, capability, method family, staffing plan, or cross-context equivalence; mathematical notation then starts replacing the role relation structure in life.

**What this buys.** Role-admission substitution, incompatibility, role factors, and role bundles become inspectable local relations while role assignment, capability, method, work, evidence, source, status, and publication claims stay with their governing patterns.

Work governed by role values and role assignments often needs three small claims:

1. One role value can satisfy a role-admission condition stated with another role value in the same context when a role-admission substitution relation is declared.
2. Two roles are incompatible for the same holder during overlapping windows.
3. A recurring conjunction of roles can be named as a role bundle expression.

Role decomposition is not a fourth primitive and not evidence of role holonhood. It prompts recovery of one of the declared relations above, a role-state refinement under `A.2.5`, a separate role value under `A.2`, a capability, responsibility, permission, commitment, or obligation relation under its direct owner, or a coupled method/work decomposition under `A.15`.

Without a local role relation structure, teams usually encode those claims in the wrong objects:

- a role assignment says "senior inspector" and silently satisfies "inspector" without declared relation;
- a separation-of-duties rule is written as a deontic slogan rather than an incompatibility relation over assignments;
- a role bundle becomes a new holder, capability, work product, or method;
- a cross-context label match is treated as role equivalence;
- method role-admission wording smuggles capability or work claims into role names.

A.2.7 keeps the role relation structure small and local. It says how role values, role descriptions, and role expressions relate; it does not say who holds them, whether holders are able, whether work happened, or whether an episteme proves something. Algebraic, graph, factor, embedding, distributed, neural, or other mathematical descriptions are optional lenses over that structure.

