---
chunk_kind: "child"
pattern_id: "A.15.2"
pattern_title: "U.WorkPlan"
section_id: "A.15.2:7e"
section_title: "Relations"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.2/A.15.2__013_relations.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "A.15.2 — U.WorkPlan"
  - "A.15.2:7e — Relations"
line_start: 22503
line_end: 22508
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.3"
  - "A.15.4"
  - "A.15.5"
  - "A.2.1"
  - "A.20"
  - "A.21"
  - "B.3"
  - "C.32.P2S"
  - "E.17"
  - "U.Method"
  - "U.MethodDescription"
  - "U.RoleAssignment"
  - "U.Work"
keywords:
  - "forecast"
  - "intent"
  - "plan"
  - "schedule"
---

### A.15.2:7e - Relations

* **Builds on:** `A.15` Role-Method-Work Alignment, `A.15.1` `U.Work`, `A.2.1` `U.RoleAssignment`, `U.Method`, and `U.MethodDescription`.
* **Coordinates with:** `A.15.3` for `SlotFillingsPlanItem` values, `A.15.4` for work-relevant appearance-based reliance repair, `A.15.5` for work-entry readiness and full-kit preparation, `A.10` for evidence-provenance relations, `B.3` for assurance, `A.20` and `A.21` for gates and constraint decisions, `C.32.P2S` for architecturing-flow refs to intended work that realizes selected structures, and `E.17` for publication-use questions.
* **Used by:** P2W carry-through when principle-to-work reasoning reaches WorkPlanning, and P2S carry-through when architecture-selected structures require intended work records. Both uses keep plan, work-entry readiness, performed work, evidence, gate, and result-measurement relations separate.

