---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:7"
section_title: "Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__009_checklist.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:7 — Checklist"
line_start: 5043
line_end: 5057
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

### A.2.7:7 - Checklist

| Check | Question |
|---|---|
| `CC-A2.7-01` | Is the bounded context named? |
| `CC-A2.7-02` | Are the related values `U.Role` values governed by A.2? |
| `CC-A2.7-03` | Is each `<=` claim framed as same-context role-requirement substitution rather than kind hierarchy or generic specialization? |
| `CC-A2.7-04` | Is incompatibility checked over role assignments, holders, and overlapping windows rather than over labels alone? |
| `CC-A2.7-05` | Is a bundle expression kept separate from holder, capability, method, and performed work? |
| `CC-A2.7-06` | Are capability requirements sent to A.2.2? |
| `CC-A2.7-07` | Are assignment and state checks sent to A.2.1 and A.2.5? |
| `CC-A2.7-08` | Are method claims sent to A.3 patterns and work claims sent to A.15 patterns? |
| `CC-A2.7-09` | Are cross-context equivalence and translation sent to F-family patterns? |
| `CC-A2.7-10` | Is any evidence, source, approval, status, assurance, publication, description, or strict-distinction claim sent to `C.2.1`, `A.10`, `B.3`, `E.17.*`, `E.24.PUB`, or `A.7` rather than expressed as role relation structure or a lens over it? |

