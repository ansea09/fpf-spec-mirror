---
chunk_kind: "child"
pattern_id: "F.14"
pattern_title: "Anti-Explosion Control for Role and Status Name Families"
section_id: "F.14:4"
section_title: "Core idea"
source_path: "FPF-Spec.md"
output_path: "by_section/F.14/F.14__005_core-idea.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "F.14 — Anti-Explosion Control for Role and Status Name Families"
  - "F.14:4 — Core idea"
line_start: 78876
line_end: 78886
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "B.3"
  - "E.10.D2"
  - "E.17"
  - "F.10"
  - "F.17"
  - "F.18"
  - "F.4"
  - "F.5"
  - "F.8"
  - "F.9"
  - "U.Role"
  - "U.RoleAssignment"
keywords:
  - "bundles"
  - "guard-rails"
  - "reuse"
  - "separation-of-duties"
  - "vocabulary growth"
---

### F.14:4 - Core idea

Use the anti-explosion sequence before minting a durable role or status name.

1. **Recover kind first.** Split the candidate family into role values, RoleDescription labels, role-relation expressions, assignments, work, capability, method, status, evidence, source, publication, requirement, policy, bridge, and local-phrase cases.
2. **Reuse existing values.** If a role value, status family, Concept-Set row, local sense, or public term already admits the current use, reuse it and record aliases where needed.
3. **Use role relation structure instead of hybrid roles.** If one role can satisfy another role requirement, two roles conflict, or roles travel together, use A.2.7 role relation structure. Do not mint a fused role unless the bounded context deliberately creates a new `U.Role` with RoleDescription and F.8 and F.18 admission.
4. **Use assignment checks instead of prestige names.** If the issue is who may hold a role, whether a separation holds, or whether work occurred, use A.2.1, F.6, A.15.1, and role state checks.
5. **Use status families and windows instead of status-name sprawl.** If the issue is time stance, evaluation state, grace, confidence, or presentation, use F.10 or the direct status pattern.
6. **Use direct patterns for qualifiers.** Capability, method, work, evidence, source, publication, requirement, policy, and assurance qualifiers stay with their direct patterns. They may inform a name later; they do not become role or status ontology by suffix.

