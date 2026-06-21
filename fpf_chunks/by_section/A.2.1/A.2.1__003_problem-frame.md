---
chunk_kind: "child"
pattern_id: "A.2.1"
pattern_title: "U.RoleAssignment - Contextual Work-Role Assignment"
section_id: "A.2.1:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.1/A.2.1__003_problem-frame.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.2.1 — U.RoleAssignment - Contextual Work-Role Assignment"
  - "A.2.1:1 — Problem Frame"
line_start: 2308
line_end: 2315
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

Work-facing roles are useful only after they are connected to concrete holders in a bounded context. "Reviewer", "operator", "deployer", "inspector", "authorizer", and "coordinator" are not enough by themselves. The project needs to know which holder bears the role, in which context, for which window or current claim, and under which neighboring role-state, capability, method, plan, and work relations.

The assignment relation must be narrow. It should not absorb capability, method, work, evidence, status, or publication use. A standard used as a requirement source can constrain work, but it does not hold a work-facing role. A report can be used as evidence, but it does not perform the review that produced it. A method description can require `ReviewerRole`, but the method description is not the reviewer.

A.2.1 therefore defines `U.RoleAssignment` as a typed relation value using `A.6.5` SlotSpec discipline. The relation is work-facing: its holder is a `U.System` or acting holon admitted as system-like performer by the governing work or method pattern. Epistemes stay in evidence-use, status-use, source-use, publication-use, requirement-use, definition-use, explanation-use, assurance-use, gate-use, or decision-use relations.

