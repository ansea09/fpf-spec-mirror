---
chunk_kind: "child"
pattern_id: "C.22.PFR"
pattern_title: "Problematic-For Relation"
section_id: "C.22.PFR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.PFR/C.22.PFR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.22.PFR — Problematic-For Relation"
  - "C.22.PFR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 50971
line_end: 50985
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
  - "actual adverse condition"
  - "actual adverse episode"
  - "assessment and evidence separation"
  - "condition-to-predicate input rule"
  - "exact problem-for entity and use"
  - "independent criterion-applicability relation"
---

### C.22.PFR:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Failure | Repair |
|---|---|---|
| Card-created Problem | Creating or accepting a ProblemCard is treated as Problem actuality. | Test actual-condition obtaining, applicability obtaining, and adverse predicate truth; keep the card as an episteme about zero or more occurrences. |
| Duplicated applicability | Predicate, entity, scope, or interval is writable in both applicability and PFR. | Keep those values only in `ProblemCriterionApplicabilityRelation` and derive PFR projections. |
| Applicability conditioned on adversity | Criterion applicability is ended whenever the actual condition becomes non-adverse, so PFR tests the same predicate twice and cannot replay A-B-C with one applicability occurrence. | Let applicability state which criterion governs the entity and scope under the declared window; test adverse-condition satisfaction only in PFR §4.3. |
| Relation-as-coordinate | An arbitrary condition relation is said to be adverse without naming the characteristic point, projection, or link to the problem-for entity. | Use the predicate's exact direct-input or governed-projection rule; reject the nearest plausible projection that does not meet that rule. |
| Assessment-constituted PFR | Evaluation work or an assessment result becomes a universal PFR participant or is treated as starting or ending the world-side episode. | Let evaluation and evidence support a boundary claim; keep PFR participants, actual inception, and actual cessation world-side. |
| Evidence-window splitting | Each measurement or assessment window creates a new Problem occurrence. | Use actual adverse inception and cessation for occurrence identity; keep support windows with the claims they warrant. |
| Unknown-as-recovery or continuity | Missing evidence is treated as proof of recovery or as permission to bridge the gap. | Record `continuity unresolved`; later evidence may revise the boundary assertion but does not create the world-side episode. |
| Open-interval churn | Every observation changes the identity key, or `open` is used for an unsupported evidence gap. | Keep participants plus actual adverse inception as the stable reference; use `open` only for supported current obtaining and add the recovered end to the claimed extent on closure. |
| Method-selected resolution | Finding a repair method is treated as ending the Problem. | Update the solvability claim; end PFR only when the adverse condition or another obtaining condition ceases. |
| Criterion-edition identity | Rewording or republishing a coextensional criterion creates a new Problem. | Recover the by-value predicate; create another applicability occurrence only when a fixed participant changes or when actual applicability ceases and later obtains again. |

