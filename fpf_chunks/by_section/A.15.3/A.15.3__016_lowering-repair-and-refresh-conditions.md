---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12c"
section_title: "Lowering, repair, and refresh conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__016_lowering-repair-and-refresh-conditions.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12c — Lowering, repair, and refresh conditions"
line_start: 23598
line_end: 23605
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

### A.15.3:12c - Lowering, repair, and refresh conditions

Lower a `SlotFillingsPlanItem` claim when the item cannot name exactly one target slot-bearing description, concrete SlotKinds from that description, EntityOfConcern, bounded context, time selector or time rule, authoritative planned-filling rows, concrete RefKinds for ByRef fillers, or required edition pins. The lowered result is a plan cue, missing-source-relation note, relation governed by another FPF pattern, or blocked kind-definition gap.

Repair the PlanItem when a source-currentness change alters the target description edition, exposed SlotKind set, planned filler, concrete RefKind, edition pin, context, time rule, evidence-reference pin, guard-preparation ref, crossing-policy ref, or expected gate relation. If performed `U.Work` already cited the PlanItem as a baseline, preserve the cited baseline and record variance or crossing witness in the work-governed relation.

Refresh before the PlanItem is used for performed-work preparation, work-entry readiness, launch-guard preparation, cross-context comparison, suite or kit reuse, Part G universalization, publication-view projection, evidence-reference use, or P2W carry-through. Stop the refresh at the smallest changed relation: the PlanItem, target slot-bearing description, concrete RefKind, cited source edition, readiness relation, performed-work variance record, or related gate, evidence, bridge, or publication relation.

