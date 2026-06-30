---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12a"
section_title: "P2W planned-baseline use relation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__014_p2w-planned-baseline-use-relation.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12a — P2W planned-baseline use relation"
line_start: 22735
line_end: 22742
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.20"
  - "A.21"
  - "A.6.5"
  - "A.6.7"
  - "B.3"
  - "C.27.TA"
  - "E.10.D1"
  - "E.10.D2"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.19"
  - "E.20"
  - "E.24"
  - "G.11"
  - "G.6"
  - "U.RelationSlotDiscipline"
  - "U.Work"
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

### A.15.3:12a - P2W planned-baseline use relation

When `E.18.1` reaches a planned-baseline question, `SlotFillingsPlanItem` records the planned relation between one slot-bearing description's SlotKinds and the fillers intended for a future work-planning or work-entry-readiness use.

When `A.15.5` checks full-kit condition, it may cite `SlotFillingsPlanItem` for planned fillers, target description edition, required refs, and time selector. That citation does not make the planned baseline a readiness verdict; `A.15.5` states the readiness relation and any missing-input or degraded-use condition.

If the same source phrase also carries launch-value, performed-work, evidence, gate, result, measurement, publication-use, source-restoration, or refresh meaning, name that separate current relation before using the PlanItem downstream.

