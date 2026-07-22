---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 50576
line_end: 50588
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.19"
  - "A.3.4"
  - "A.6.5"
  - "A.6.REL"
  - "B.3"
  - "C.22"
  - "C.22.2"
  - "E.18.1"
  - "E.23"
  - "G.11"
keywords:
  - "actual condition"
  - "actual problematic-for relation"
  - "applicability predicate"
  - "problem-for entity"
  - "relation occurrence"
---

### C.22.PFR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Card-created Problem | Creating or accepting a ProblemCard is treated as Problem actuality. | Test actual-condition obtaining, applicability obtaining, and adverse predicate truth; keep the card as an episteme about zero or more occurrences. |
| Duplicated applicability | Predicate, entity, scope, or interval is writable in both applicability and PFR. | Keep those values only in `ProblemCriterionApplicabilityRelation` and derive PFR projections. |
| Assessment-constituted PFR | Evaluation work or an assessment result becomes the universal third PFR participant. | Let the direct consumer evaluate and support adverse truth; keep PFR's participant set reduced. |
| Evidence-window splitting | Each measurement or assessment window creates a new Problem occurrence. | Derive one maximal continuous adverse interval and keep support windows with their claims. |
| Unknown-as-recovery | Missing evidence is treated as proof that the condition was non-adverse. | Preserve `unknown`; split PFR only at demonstrated non-adverse behavior or participant change. |
| Open-interval churn | Every later observation replaces `[start, open]` with a new current interval and identifier. | Keep the stable open sentinel until closure; then record the recovered end on the same occurrence. |
| Method-selected resolution | Finding a repair method is treated as ending the Problem. | Update the solvability claim; end PFR only when the adverse condition or another obtaining condition ceases. |
| Criterion-edition identity | Rewording or republishing a coextensional criterion creates a new Problem. | Recover the by-value predicate; create another applicability occurrence only when a fixed participant changes or when actual applicability ceases and later obtains again. |

