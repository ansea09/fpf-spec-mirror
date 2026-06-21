---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:15a"
section_title: "P2W Performed-Work Use Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__020_p2w-performed-work-use-relation.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:15a — P2W Performed-Work Use Relation"
line_start: 21734
line_end: 21739
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "actuals"
  - "event"
  - "execution"
  - "log"
  - "occurrence"
  - "run"
---

### A.15.1:15a - P2W Performed-Work Use Relation

When `E.18.1` reaches performed work, `U.Work` states the dated occurrence: performer, method-description source, parameters, resources, time window, pre-state, post-state, outputs, outcome, and audit trace.

A `U.Work` occurrence may cite a `U.WorkPlan` or `SlotFillingsPlanItem` as planned baseline. The performed-work record states launch values, performed values, substitutions, variance, telemetry, and result-related records; comparator, transport, `PrincipleFrame`, evidence, assurance, and gate claims are separate current relations when the carry-through record names them.

