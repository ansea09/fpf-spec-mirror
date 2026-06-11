---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12a"
section_title: "P2W Planned-Baseline Use Relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__014_p2w-planned-baseline-use-relation.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12a — P2W Planned-Baseline Use Relation"
line_start: 21155
line_end: 21160
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

### A.15.3:12a - P2W Planned-Baseline Use Relation

When `E.18.1` reaches a planned-baseline question, `SlotFillingsPlanItem` records the planned mapping from a slot-bearing description and `SlotKind`s to planned fillers. It may include evidence-reference hooks, edition pins, assumptions, dependencies, and freshness requests needed before work is enacted.

If the same phrase also carries launch-value, run-time actual, evidence, gate, or result meaning, the carry-through record names that separate relation before the PlanItem is used downstream.

