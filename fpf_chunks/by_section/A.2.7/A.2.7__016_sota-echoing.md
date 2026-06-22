---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:10.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__016_sota-echoing.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:10.1 — SoTA-Echoing"
line_start: 5237
line_end: 5247
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

### A.2.7:10.1 - SoTA-Echoing

| Practice line | What FPF takes | Practical implication |
|---|---|---|
| Role-based access-control and separation-of-duties practice supplies stable relations among roles, users, sessions, and constraints. | A.2.7 keeps the role-relation part but does not turn access-control policy into general role ontology. | Role substitution and incompatibility are declared relations, not labels or permissions. |
| Attribute-based and zero-trust authorization practice separates role-like attributes, current context, policy decision, and resource action. | Role relation structure is one input to a check; capability, state, policy, and work remain separate. | "Has role" does not prove ability, currentness, permission, or performed work. |
| Organizational design and safety practice uses separation of duties and independence constraints beyond IT. | Incompatibility is stated over role assignments and windows in any bounded context. | Safety, audit, laboratory, governance, and operations examples do not become software-only. |
| Current FPF slot-relation and ontic discipline keeps relation positions from becoming kinds. | Role relation structure relates role values; it does not create a new role-slot ontic or reduce role to SlotKind. | A.2.7 can cite A.6.5 and E.24 without duplicating them. |

Source-currentness note: RBAC and separation-of-duties are stable lineage, not the full current frontier. Current practice adds attribute and zero-trust authorization, context and currentness checking, policy-as-code practice, and FPF's newer slot-relation discipline. A.2.7 therefore keeps only the role-relation part and leaves currentness, policy decision, capability, method, work, and evidence to their direct patterns.

