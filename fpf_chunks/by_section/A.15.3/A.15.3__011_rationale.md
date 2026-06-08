---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__011_rationale.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:10 — Rationale"
line_start: 21046
line_end: 21055
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

### A.15.3:10 - Rationale

This pattern exists to give WorkPlanning an explicit, citeable place to commit to “which planned values or references will fill which slots” without collapsing into run-time state.

Keeping the baseline bound to exactly one slot-bearing description makes SlotKind semantics checkable and prevents accidental cross-slot-bearing-description drift.

Treating indices as derived projections preserves the canonical row source while still enabling human-friendly navigation or tooling acceleration.

Finally, by disallowing run-time witnesses (launch values, observed values, concrete `Γ_time`) the pattern enforces the planning and enactment split and keeps audit variance attributable to an explicit baseline rather than to shifting defaults.

