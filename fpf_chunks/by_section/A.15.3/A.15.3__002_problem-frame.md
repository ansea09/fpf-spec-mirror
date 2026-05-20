---
chunk_kind: "child"
pattern_id: "A.15.3"
pattern_title: "SlotFillingsPlanItem"
section_id: "A.15.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.3/A.15.3__002_problem-frame.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.15.3 — SlotFillingsPlanItem"
  - "A.15.3:1 — Problem frame"
line_start: 20388
line_end: 20399
dependencies:
  - "A.15.1"
  - "A.15.2"
  - "A.6.5"
  - "A.6.7"
  - "E.10.D1"
  - "E.17"
  - "E.18"
  - "E.19"
  - "E.8"
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

### A.15.3:1 - Problem frame

FPF frequently needs to make **reproducible, reviewable choices** about *what fills which conceptual slot* (spec refs, policy refs, mechanism-instance refs, time selectors, evidence hooks, etc.) **before** any Work is enacted. These choices must be visible as a planned baseline for a concrete P2W slice (CG-frame, path slice, or publication scope), and must remain distinct from run-time “actuals” and gate decisions.

However, absent a universal WorkPlanning plan item for architecture-by-planned-slot-filling, authors tend to hide these choices inside mechanism prose, CG/CN specs, ad-hoc cards, or informal checklists—making Part G patterns difficult to universalize and making Work audit trails ambiguous.

`SlotFillingsPlanItem` addresses this by defining a **WorkPlan PlanItem kind** whose job is to state, in one place and with explicit context, a mapping:

> *(Target slot-bearing description, slot kind) → planned filler (ByValue | ByRef(<concrete RefKind>), with edition pins when needed)*

and to do so in a form that can be cited by Work enactment and by suite/kit spec pins, without collapsing into “execution” or “decision logging”.

