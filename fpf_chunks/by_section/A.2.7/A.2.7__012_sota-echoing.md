---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
section_id: "A.2.7:10"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__012_sota-echoing.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "A.2.7 — Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
  - "A.2.7:10 — SoTA-Echoing"
line_start: 6116
line_end: 6126
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

### A.2.7:10 - SoTA-Echoing

| Current research or practice line | What changes in this pattern | Practitioner implication |
|---|---|---|
| [gUFO 2026](https://arxiv.org/abs/2603.20948) provides a current foundational-ontology comparator with explicit type typology and reification patterns for relational aspects. | A.2.7 keeps relation obtaining, occurrence individuation, assertion episteme, and representation separate; it does not import gUFO's taxonomy as the FPF constructive ontology. | A relation can be referred to when needed without making every relation a record or every imported class an FPF kind. |
| [OpenFGA role-modeling guidance, updated 2026](https://openfga.dev/docs/best-practices/modeling-roles) documents static role-like relations, user-defined roles, and instance-specific role assignments as different modeling choices. | A.2.7 keeps role-value relations separate from actual `U.RoleAssignment` occurrences and supports a lightweight path before instance-specific assignment complexity is needed. | A stable role relation can be reused while holder assignment remains explicit and instance-specific. |
| [Cedar policy construction](https://docs.cedarpolicy.com/policies/syntax-policy.html) separates principal, action, resource, scope, and additional conditions during authorization evaluation. | A.2.7 treats role structure as one typed premise of a receiving evaluation, not as the acting principal or the decision itself. | The checking system, evaluated assignments, action-facing condition, and outcome remain inspectable. |
| Separation-of-duties practice across safety, clinical work, governance, and authorization depends on exact joint-admission conditions rather than title intuition. | `RoleIncompatibilityPredicateSlot` names holder, work, and temporal conditions, and `RoleBundleRelation` names the allocation rule. | Independence and team-composition claims can be tested in the domain where they matter. |

The software authorization sources are stress cases, not the universal subject. Their useful move is the separation of role definitions, instance assignments, evaluation inputs, and outcomes. A.2.7 generalizes that move to any project in which admitted systems hold roles and perform work.

