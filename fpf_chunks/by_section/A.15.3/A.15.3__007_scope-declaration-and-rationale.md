---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:6"
section_title: "Scope Declaration and Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__007_scope-declaration-and-rationale.md"
commit_sha: "fe0df9dcb06cfc87c8a6cb2f7cce3ac0d3b64d5e"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:6 — Scope Declaration and Rationale"
line_start: 22262
line_end: 22269
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

### A.15.3:6 - Scope Declaration and Rationale

`SlotFillingsPlanItem` has a deliberate explicitness bias. It asks for target description, context, time, and planned rows because those are the smallest fields that keep planned slot filling separate from performed work and publication views.

The pattern does not try to make every work plan heavy. Ordinary plans stay in A.15.2. A.15.3 opens only when slot-filling choices themselves are the planned baseline that later work, gates, evidence, or publication projections will rely on.

The anti-bias guard is locality: if the current issue is mechanism meaning, evidence sufficiency, gate passage, source restoration, publication use, or performed work, use that governing pattern and bring only the returned planned-baseline relation back here.

