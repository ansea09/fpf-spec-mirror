---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
section_id: "A.2.7:6"
section_title: "Cross-Context Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__010_cross-context-boundary.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.2.7 — RoleRelationStructure@BoundedContext - Context-Local Role Relations and Representation-Lens Boundary"
  - "A.2.7:6 — Cross-Context Boundary"
line_start: 5184
line_end: 5189
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

### A.2.7:6 - Cross-Context Boundary

Role relation structure is context-local. Matching role labels across contexts are not enough.

`ArticleAssessorRole:JournalContext` and `SafetyAssessorRole:SafetyCaseContext` may share a source label, but a role-requirement substitution or incompatibility relation in one context does not transfer to the other context by label. Cross-context reuse, bridge, translation, public naming, or semantic alignment uses F-family context and naming patterns.

