---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12b"
section_title: "Planned-Baseline To Performed-Work Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__015_planned-baseline-to-performed-work-boundary.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12b — Planned-Baseline To Performed-Work Boundary"
line_start: 21161
line_end: 21166
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.TGA"
  - "U.WorkPlan"
keywords:
  - "P2W seam"
  - "WorkPlanning"
  - "edition pins"
  - "guard pins"
  - "planned baseline"
  - "planned filler"
  - "slot-bearing description"
  - "variance trail"
  - "Γ_time selector"
---

### A.15.3:12b - Planned-Baseline To Performed-Work Boundary

A performed `U.Work` occurrence may cite a `SlotFillingsPlanItem` as the planned baseline for slot fillers. The performed-work record states variance, substitution, and launch-value finalization under the current gate relation and work-governing patterns.

This preserves the P2W split: WorkPlanning places the baseline, while performed work records what happened.

