---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__003_problem.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:2 — Problem"
line_start: 30191
line_end: 30208
dependencies:
  - "A.17-A.19"
  - "C.16"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8.ECSPF"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### A.19.ECS:2 - Problem

FPF already has named patterns for single characteristics, scales, coordinate values, Q-Bundles, and repeated improvement. The gap is the construction of a useful grouped scale set for an evaluated object kind.

Recurring failures:

1. **Scale set from air.** An evaluation lists coordinates because they are familiar, not because they discriminate the evaluated object kind or use.
2. **Wrong-kind comparison.** Objects outside the declared kind are scored as if they were weak objects under improvement, or are silently skipped, instead of being returned to evaluation selection before opening or handled by an explicit object-kind-fit defect/value after opening.
3. **One-score collapse.** Several independent characteristics are averaged into one score, hiding object-kind-fit defects and trade-offs.
4. **Unstated polarity.** Readers cannot tell which direction is preferred or when a value has no preferred direction.
5. **No floor or exceptional meaning.** Values are recorded, but nobody can say what is viable, exceptional, or still inadmissible for the declared use.
6. **No evidence or missingness rule.** A coordinate value is asserted without saying what observation, content locus, test, example, source, or judgment can justify it, or what absence means.
7. **No protected trade-off.** The evaluation encourages improvement on visible coordinates while damaging safety, usability, affordability, source preservation, entry cost, neighbour fit, or another value that should constrain the change.
8. **No stop or reopen condition.** Improvement continues forever or stops after a convenient checklist closure, not because the evaluation says the evaluated object has reached the declared aim.
9. **Specification underdeclaration.** A new evaluation is mentioned in prose, table, rule, or local rubric, but its declared specification does not make evaluated object kind, coordinate set, value meanings, status meanings, relations, and non-use boundaries recoverable.
10. **Result-form underdeclaration.** The evaluation has coordinates, but the returned result can be a prose impression, a two-column value table, or a checklist count without evidence basis, adjacent-value rationale, calibration discipline, or coordinate-specific payload.
11. **Evidence-basis leakage.** Evidence needed to justify the evaluation result, corpus projection, currentness, retrieval, or parity is written as if it were the evaluated object's own method or user action.

