---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - System Role Assignment"
section_id: "A.2.1:12"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__014_sota-echoing.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "A.2.1 — U.RoleAssignment - System Role Assignment"
  - "A.2.1:12 — SoTA-Echoing"
line_start: 3291
line_end: 3298
dependencies:
  - "A.1.1"
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.2"
  - "A.2.5"
  - "A.2.7"
  - "A.3.1"
  - "A.3.2"
  - "A.6.5"
  - "A.6.9"
  - "A.6.REL"
  - "C.2.1"
  - "F.6"
  - "F.9"
  - "U.Role"
keywords:
  - "AssignmentInterval"
  - "assignment occurrence"
  - "effective ReferenceScheme"
  - "holder System"
  - "performedUnderAssignment"
  - "role value"
  - "role-taxonomy episteme"
---

### A.2.1:12 - SoTA-Echoing

| Practice line | Source and status | FPF mutation | Practical consequence |
| --- | --- | --- | --- |
| Current foundational ontology distinguishes role-like classification, relation aspects, and explicit relation occurrences. | Almeida, Guizzardi, Sales, and Fonseca, [gUFO](https://arxiv.org/abs/2603.20948), 2026 preprint; used as a current comparator rather than an imported hierarchy. | Keep role value, assignment relation occurrence, participant SlotKinds, and performed work distinct; apply FPF's own holder and occurrence-identity rules. | The same system can hold several roles and enter repeated assignments without new system kinds. |
| DDD makes model interpretation local to an actual model-use organization. | Eric Evans, [Domain-Driven Design Reference](https://www.domainlanguage.com/wp-content/uploads/2016/05/DDD_Reference_2015-03.pdf), 2015 mature reference; Evans, [Context Mapping with an AI-based Component](https://www.domainlanguage.com/articles/context-mapping-an-ai-based-component/), 2026 current worked practice. | Let a receiving assertion or work use designate a selected `BoundedModelUseStructure` only when that organization changes the receiving interpretation; taxonomy and scheme remain the generic assignment participants. | Physical and organizational assignments need no fabricated `U.BoundedContext`, while a real DDD use can retain its selected structure without changing generic relation identity. |
| FPF relation-occurrence discipline separates predicate obtaining, assertion, explicit individuation, identifier assignment, and reference use. | Current `A.6.REL` line. | Materialize a role-assignment occurrence only when another claim needs its identity; use temporal extent to distinguish repeated episodes. | A staffing sentence stays readable, while a work-attribution claim can reference the exact shift assignment. |

