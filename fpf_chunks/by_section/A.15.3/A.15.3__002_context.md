---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:1"
section_title: "Context"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__002_context.md"
commit_sha: "44dd88188a07646ef23aca32627a3f670525853f"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:1 — Context"
line_start: 22798
line_end: 22810
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

### A.15.3:1 - Context

`A.15.2` can already say that work is planned. Some plans also need to freeze a more specific relation: "for this planned work, this slot-bearing description will use these planned fillers in these SlotKinds under this bounded context and time rule."

That extra relation is not the target description, not the mechanism, not a publication view, and not the later performed work. It is a plan item inside work planning. `SlotFillingsPlanItem` gives that relation a stable place.

Typical situations:

- a CHR or CG-frame plan chooses comparator specs, normalization methods, indicator policies, or guard refs before work;
- a mechanism-suite plan chooses which suite description, method-description edition, or policy ref will be used later;
- a QD or archive plan fixes descriptor and distance-definition editions before selection work;
- a refresh or parity plan cites planned refs so later performed work can record variance rather than silently changing the plan.

