---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__011_rationale.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:10 — Rationale"
line_start: 22712
line_end: 22719
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

### A.15.3:10 - Rationale

The pattern exists because planned slot fillings are neither generic plan text nor performed work. They are relation-bearing plan items: one target description supplies SlotKinds, the plan chooses fillers, and later work records what happened.

A.6.5 prevents a common type explosion. `slot_kind`, `planned_filler`, and RefKind fields are not new U-kinds. They are positions and fillers inside one relation-bearing PlanItem. E.17 prevents a second row source by keeping views and cards as projections. A.15.1 prevents plan backfilling by keeping performed-work actuals and variance outside the plan.

This split is especially useful in P2W and Part G work because many downstream records need the same planned baseline without copying suite semantics, mechanism definitions, gate decisions, evidence claims, or publication views into the plan.

