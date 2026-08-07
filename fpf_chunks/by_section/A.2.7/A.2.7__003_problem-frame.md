---
chunk_kind: "child"
pattern_id: "A.2.7"
pattern_title: "Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
section_id: "A.2.7:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.7/A.2.7__003_problem-frame.md"
commit_sha: "2729cfe5a3e4a86da8632aabcb859488c06a2d51"
heading_path:
  - "A.2.7 — Role Relation Structure - Substitution, Incompatibility, Qualification, and Joint Admission"
  - "A.2.7:1 — Problem Frame"
line_start: 5728
line_end: 5737
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

A system applying a maintenance admission method may admit a current assignment to `SeniorHydraulicsTechnicianRole` where the method description names `HydraulicsTechnicianRole`. A system applying a safety method may reject overlapping author and approver assignments. A clinical method description may state a joint admission condition over surgeon, anesthetist, and scrub roles. These uses all concern relations among role values, but they do not concern the same relation.

The values are interpreted through a named role-taxonomy episteme and an effective `U.ReferenceScheme`. The direct relation predicate may obtain under that interpretation even before FPF publishes an assertion about it. A taxonomy statement can correctly or incorrectly assert the relation; the statement is not the occurrence by form. A specialized social ontology may make an accepted appointment, policy decision, or installation act constitutive, but only when its direct pattern says so.

Plainly, the role-taxonomy episteme is the claim-bearing description in which the role vocabulary and its relation claims can be inspected. The effective reference scheme is the by-value interpretation convention under which the current use resolves those role names and relation terms. `RoleRelationStructure` is the selected organization among the interpreted role values; a table or diagram may describe that organization but does not become it.

The relation structure is also not the actual assignment configuration. Only an admitted `U.System` can hold `U.RoleAssignment`. Systems act and perform work. Role values, taxonomy epistemes, relation occurrences, and selected structures do not.

