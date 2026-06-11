---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:12c"
section_title: "Lowering, Repair, and Refresh Conditions"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__016_lowering-repair-and-refresh-conditions.md"
commit_sha: "3f9a2dd65b0df9cf6bed602fb1f189162060954f"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:12c — Lowering, Repair, and Refresh Conditions"
line_start: 21090
line_end: 21097
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

### A.15.3:12c - Lowering, Repair, and Refresh Conditions

Lower a `SlotFillingsPlanItem` claim when the item cannot name exactly one Description-scoped slot-bearing description, concrete `SlotKind`s from that description, `described_entity_ref`, `bounded_context_ref`, time selector or time rule, authoritative planned-filling rows, concrete RefKinds for ByRef fillers, or required edition pins. Do not repair the missing detail by widening the planned-baseline claim; lower it to a plan cue, source-gap note, relation governed by another FPF pattern, or blocked kind-definition gap.

Repair the PlanItem when a source-currentness change alters the slot-bearing description edition, SlotKind interface, planned filler, concrete RefKind, edition pin, context anchor, time rule, evidence pin, guard pin, crossing-policy reference, or expected gate relation. If a performed `U.Work` occurrence already cited the PlanItem as a baseline, preserve the cited baseline and record variance or crossing witnesses in the work-governed relation rather than rewriting the cited baseline to match what happened.

Refresh before the PlanItem is used for work enactment, launch guard preparation, cross-context comparison, suite or kit reuse, Part G universalization, publication-view projection, evidence-reference use, or P2W carry-through. Stop the refresh at the smallest changed object: the plan item, its target slot-bearing description, a concrete RefKind, the cited source edition, the performed-work variance record, or the related gate, evidence, bridge, or publication relation.

