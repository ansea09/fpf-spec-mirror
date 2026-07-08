---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__005_forces.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:3 — Forces"
line_start: 2357
line_end: 2367
dependencies:
  - "A.15"
  - "A.2"
  - "A.2.1"
keywords:
  - "RCS/RSG"
  - "RoleEnactmentFact"
  - "Standard"
  - "context"
  - "holder"
  - "performedBy"
  - "role"
---

### A.2.1:3 - Forces

| Force | Tension |
| --- | --- |
| Local meaning vs corpus reuse | Role assignments must be local to one bounded context, while the pattern must remain reusable across engineering, organizations, software, AI agents, laboratories, and governance work. |
| Traceability vs relation overreach | Work attribution needs a concrete assignment relation, but the assignment must not swallow method, capability, evidence, status, or publication semantics. |
| Open-world use vs heavy forms | Some assignment claims need only holder, role, and context; other claims need window, state assertion, assignment source, capability, or method details. Missing optional-in-use slots must not force dummy values. |
| Role state vs work occurrence | A role assignment can be current while the holder is not in an enactable role state; work occurrence is still a separate dated occurrence. |
| Ordinary notation vs ontology | `Holder#Role:Context@Window` is memorable, but it is notation for a typed assignment relation, not the relation's ontology. |
| Episteme use vs work performance | Epistemes can be used as evidence, standard, requirement, definition, explanation, status bearer, publication, or assurance input; they do not perform work by holding enactment-facing roles. |

