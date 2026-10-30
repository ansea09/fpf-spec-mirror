---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "SystemRoleKindRelationStructure - Relations among System-Role Kinds"
section_id: "A.2.7:9"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__011_rationale.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "A.2.7 — SystemRoleKindRelationStructure - Relations among System-Role Kinds"
  - "A.2.7:9 — Rationale"
line_start: 8004
line_end: 8011
dependencies:
  - "A.2"
  - "A.2.1"
  - "A.2.5"
  - "A.22"
  - "A.6.REL"
  - "C.3"
  - "C.3.1"
  - "E.10.ROLE"
keywords:
  - "U.SubkindOf"
  - "incompatibility"
  - "joint assignment requirement"
  - "relations among system-role kinds"
  - "selected structure"
  - "substitution"
---

### A.2.7:9 - Rationale

When a receiving check needs several kind relations together, a dependent `SystemRoleKindRelationStructure` identifies that organization. The actual assignments remain separate inputs to the check.

The families are separate because their laws differ. Substitution is directional. Incompatibility is symmetric under one joint condition. A bundle uses an order-insensitive finite set and an allocation rule. Monotonic qualification belongs to `U.SubkindOf`; non-monotonic restriction stays residual. One generic hierarchy cannot preserve those distinctions.

Relation realism prevents a document model from becoming the ontology. Direct predicates determine obtaining, and identity laws determine whether the same world-side relation occurrence continues; assertions, policies, and diagrams describe those facts. Slot discipline makes context-local participant domains reviewable and keeps the system-role kind, holder, assignment, predicate, slot, and representation position distinct.

