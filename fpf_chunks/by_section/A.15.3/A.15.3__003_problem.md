---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__003_problem.md"
commit_sha: "cf12b97913ff82ca8a45ba77d3658ad11e0fdeb6"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:2 — Problem"
line_start: 21487
line_end: 21497
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
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

### A.15.3:2 - Problem

Without an explicit `SlotFillingsPlanItem`, six failures recur:

1. **Plan and performed-work blur.** Planned fillers get treated as launch values or run-time actuals.
2. **Slot drift.** A SlotKind's meaning changes because the target description edition changed, but the plan still reads as if it meant the old description.
3. **Implicit latest.** Source text says "use latest" or "current best" without a time selector or pinned edition.
4. **View becomes authority.** A card, dashboard, or generated view becomes the de facto place where planned rows live.
5. **Mechanism prose hides planning.** Suite or mechanism text quietly carries chosen fillers even though those choices vary by plan instance.
6. **Variance disappears.** After work happens, the plan is edited to match the performed work, erasing the gap that audit or improvement needs.

