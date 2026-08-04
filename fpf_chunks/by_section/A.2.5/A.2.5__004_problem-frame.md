---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "RoleStateRelation - Windowed Role-State Recognition and Work Admission"
section_id: "A.2.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__004_problem-frame.md"
commit_sha: "8b727cba9e893a467b82aab9da84fb7d6d945480"
heading_path:
  - "A.2.5 — RoleStateRelation - Windowed Role-State Recognition and Work Admission"
  - "A.2.5:1 — Problem Frame"
line_start: 4451
line_end: 4460
dependencies:
  - "A.15"
  - "A.2.1"
keywords:
  - "RSG"
  - "enactability"
  - "role state"
  - "role-state evolution"
  - "state machine"
---

### A.2.5:1 - Problem Frame

`U.RoleAssignment` establishes that one admitted system holds one role under a named role-taxonomy episteme and effective reference scheme for an assignment episode. That does not settle whether the assignment currently satisfies the condition needed by a particular method or work claim.

The distinction is easy to see in physical work. `Robot-7` can remain assigned `InspectorRole` through an eight-hour shift while calibration expires at noon. The assignment occurrence continues. The `InspectionReady` role-state occurrence ends when its predicate ceases to hold. A later recalibration can start another role-state occurrence without creating another assignment.

The same distinction appears in social and computational work. An on-call person can be assigned while conflicted or fatigued. A service can hold `ApproverRole` while the relations selected in one model-use structure give the role a fulfilment-approval interpretation and the relations selected in another give it a payment-approval interpretation. A tool-using agent can expose a capability while a concrete action is not admitted for the current task and input values.

The engineering problem is therefore to state the exact assignment, predicate, and interval; state affirmative or negative assertion polarity and the separately governed reliance posture; recognize an obtaining occurrence only when the direct predicate is true; and connect the assertion to the evidence needed by the consequence-bearing use. A universal list of state labels solves none of those tasks.

