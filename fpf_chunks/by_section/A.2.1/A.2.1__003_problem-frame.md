---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__003_problem-frame.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:1 — Problem Frame"
line_start: 2337
line_end: 2344
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

### A.2.1:1 - Problem Frame

Work-facing roles are useful only after they are connected to concrete holders in a bounded context. "Reviewer", "operator", "deployer", "inspector", "authorizer", "coordinator", "drive motor", and "cooling circulator" are not enough by themselves. The project needs to know which holder bears the role, in which context, for which window or current claim, and under which neighboring role-state, capability, method, plan, transformation, functioning, and work relations.

The assignment relation must be narrow. It should not absorb capability, method, work, evidence, status, or publication use. A standard used as a requirement source can constrain work, but it does not hold an enactment-facing role. A report can be used as evidence, but it does not perform the review that produced it. A method description can state `ReviewerRole` as a role-admission condition, but the method description is not the reviewer.

A.2.1 therefore defines `U.RoleAssignment` as a typed relation value using `A.6.5` SlotSpec discipline. The relation is enactment-facing: its holder is an admitted `U.System` selected as system-like performer by the governing method, work, transformation, or functioning pattern. "Performer" includes physical and operational performance by machines, components, organisms, services, teams, and people; it does not imply consciousness, intention, legal accountability, or ethical responsibility unless a neighboring pattern makes that stronger claim current. Epistemes stay in evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, gate-use, or decision-use relations.

