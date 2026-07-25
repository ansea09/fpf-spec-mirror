---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__012_conformance-checklist.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:7 — Conformance Checklist"
line_start: 5309
line_end: 5324
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

### A.2.7:7 - Conformance Checklist

| Check | Question |
|---|---|
| `CC-A2.7-01` | Is the bounded context named? |
| `CC-A2.7-02` | Are the related values `U.Role` values governed by A.2? |
| `CC-A2.7-03` | Is each `<=` claim framed as same-context role-admission substitution rather than kind hierarchy or generic specialization? |
| `CC-A2.7-04` | Is incompatibility checked over role assignments, holders, and overlapping windows rather than over labels alone? |
| `CC-A2.7-05` | Is a bundle expression kept separate from holder, capability, method, and performed work? |
| `CC-A2.7-06` | Has any role decomposition claim been recovered as role-admission substitution, factor or qualification, bundle, separate role value, role-state refinement, capability-fit condition, responsibility, permission, commitment, or obligation relation, method/work decomposition, or ordinary prose rather than role `partOf`? |
| `CC-A2.7-07` | Do capability-fit conditions use A.2.2? |
| `CC-A2.7-08` | Do assignment and state checks use A.2.1 and A.2.5? |
| `CC-A2.7-09` | Do method claims use A.3 patterns and work claims use A.15 patterns? |
| `CC-A2.7-10` | Do cross-context equivalence and translation claims use F-family patterns? |
| `CC-A2.7-11` | Does any evidence, source, approval, status, assurance, publication, description, or strict-distinction claim use `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, or `A.7` rather than expressed as role relation structure or a lens over it? |

