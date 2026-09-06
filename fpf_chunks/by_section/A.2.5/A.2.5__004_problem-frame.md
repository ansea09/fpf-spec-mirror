---
chunk_kind: "child"
pattern_id: "A.2.5"
pattern_title: "SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
section_id: "A.2.5:1"
section_title: "Problem Frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.5/A.2.5__004_problem-frame.md"
commit_sha: "9208be543f1ede0f53eb24604bf97fd2f121dd24"
heading_path:
  - "A.2.5 — SystemRoleAssignmentStateRelation - Assignment-State Recognition and Work Admission"
  - "A.2.5:1 — Problem Frame"
line_start: 4990
line_end: 4999
dependencies:
  - "A.15"
  - "A.15.1"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.2.7"
  - "A.21"
  - "A.6.5"
  - "A.6.REL"
  - "C.3"
keywords:
  - "Work admission"
  - "assignment-state predicate"
  - "assignment-state relation"
  - "evidence boundary"
  - "state condition"
  - "time window"
---

### A.2.5:1 - Problem Frame

An occurrence of a declared `U.SystemRoleAssignment` species assigns an admitted System to one local system-role kind and supplies any other values required by that species. It does not establish that the assignment satisfies a condition needed by a Method or Work claim in the evaluated interval.

`Robot-7` can remain under `InspectionShiftAssignment-17` throughout an eight-hour shift while calibration expires at noon. The assignment continues. The `InspectionReady` state occurrence ends when its predicate ceases to hold. Recalibration can start another occurrence under the same assignment without creating another assignment.

The same distinction appears in social and computational Work. An on-call person can remain assigned while conflicted or fatigued. A service can remain assigned to `ApproverSystemRole` while one predicate concerns fulfilment approval and another concerns payment authorization. A tool-using agent can expose a capability while a concrete action remains inadmissible for the current task and inputs.

The engineering problem is therefore to identify the exact assignment, predicate, and interval; distinguish affirmative or negative assertion polarity from reliance posture; recognize an occurrence only while the direct predicate is true; and connect an assertion to evidence only when a consequence-bearing use needs that support.

