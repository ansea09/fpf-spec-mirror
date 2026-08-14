---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "Evaluation CharacteristicSpace FPF Pattern Publication Form"
section_id: "E.8.ECSPF:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__005_solution.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "E.8.ECSPF — Evaluation CharacteristicSpace FPF Pattern Publication Form"
  - "E.8.ECSPF:4 — Solution"
line_start: 73116
line_end: 73159
dependencies:
  - "A.19.ECS"
  - "C.25"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.8"
  - "E.9.DA"
  - "F.18"
  - "F.19"
keywords:
---

### E.8.ECSPF:4 - Solution

When an `A.19.ECS` specification is selected for durable FPF publication, author the evaluation as an `E.8` pattern with these additional placement rules:

1. **Keep the evaluation characteristic-space specification separate from the publication form.** The pattern publishes an evaluation `CharacteristicSpace`; it is not itself the evaluated object, the evaluation result, the improvement loop, or the evidence record.
2. **Put recognition before coordinates.** The opening text names evaluated object kind, declared use, first evaluation use, FPF-publication boundary, what goes wrong, and what the pattern buys before any dense table.
3. **Place the `A.19.ECS` specification by value.** The `Solution` carries the record shape, local names, object-kind-fit rule, coordinate set, value meanings, evidence-basis rule, result-row shape, adjacent-value rationale rule, calibration points, coordinate-specific evidence payloads, missingness rule, protected trade-offs, status meanings, and stop or reopen condition.
4. **Use worked slices as the discriminating-case test.** Archetypal Grounding and worked cases include a passing evaluated object, a below-floor evaluated object, and an outside-declared-object-kind boundary case.
5. **Keep checklist rows secondary.** Conformance checks verify that the evaluation is recoverable and usable. They do not become the user's method.
6. **Use applicable pattern content for outside claims.** When `Relations` or a compact non-use boundary makes a claim about, for example, evidence, assurance, work, naming, measurement, or improvement, cite the applicable pattern id and say whether its content defines, constrains, tests, or helps repair that claim. A pattern id is enough for ordinary use. Name a particular assertion, episteme edition, or `ClaimGraph` only when interpretation, migration, conflict, publication, or reuse depends on that identity. Do not call `F.19`, `E.10`, `E.10.ARCH`, `F.18`, or another pattern a Method merely because its guidance is being used. Establish a `U.Method`, a qualifying `U.MethodDescription`, or a particular Method use only after its own admission test passes and the current claim needs that identity. When repairing wording, make sure that the evaluated object kind, relation kind or claim kind, live ontic slot, relation position, use relation, admissible use, and scope remain recoverable before and after the repair. A lexical substitution without this preservation check is not a repair.
7. **Evaluate the publication form with `E.21`.** When the FPF pattern publication form is under quality improvement, `E.21` evaluates the FPF pattern version's quality. The evaluation coordinates inside the pattern continue to judge the evaluated object declared by that evaluation. The `E.21` result, corpus-projection evidence, README/ToC/E.11/I.2 alignment, retrieval or cold-reader evidence, monolith parity, landing evidence, and developer/reviewer/executor correspondence stay in the quality, review, projection, or release carriers unless the publication form's own `EntityOfConcern` and user-facing action are that evaluation/projection work.

The authoring flow and the quality-improvement flow are different flows. This pattern publishes an evaluation for its declared evaluated object kind. A later `E.21` evaluation of this pattern is evidence about the publication form as an FPF pattern, not part of the evaluation that the pattern publishes. That evidence may cause edits to recognition text, coordinates, cases, or boundaries, but it remains outside the pattern unless rewritten as user-facing evaluation guidance.

#### E.8.ECSPF:4.1 - Canonical placement table

| E.8 section | ECS-specific payload |
|---|---|
| `Problem frame` | Evaluated object kind, declared use, first useful evaluation use, FPF-publication boundary, what goes wrong without this evaluation, and what practical move the evaluation enables. |
| `Problem` | Failure modes that the evaluation prevents: wrong-kind scoring, hidden value drift, proxy value, one-score collapse, missingness confusion, or neighbour theft. |
| `Forces` | Tensions among reuse, coordinate count, readability, measurement admissibility, trade-off protection, local stop, and open-ended improvement. |
| `Solution` | `A.19.ECS` record shape, local names, object-kind-fit rule, coordinate set, value meanings, evidence basis, result-row shape, adjacent-value rationale rule, calibration points, coordinate-specific evidence payloads, evidence and missingness rules, protected trade-offs, status meanings, stop and reopen conditions. |
| `Archetypal Grounding` | At least one passing evaluated object, one below-floor evaluated object, and one outside-declared-object-kind boundary case. |
| `Bias-Annotation` | Known skew in source examples, reader family, domain tradition, measurement preference, benchmark preference, or FPF-internal reuse. |
| `Conformance Checklist` | Checks that the specification is recoverable, not that a reviewer likes the evaluated object. |
| `Common Anti-Patterns` | Score-sheet pattern, checklist-as-solution, table-first recognition failure, neighbour theft, one total score, hidden value drift. |
| `Consequences` | What a conforming evaluation use permits, what it does not permit, and which neighbouring pattern defines, constrains, or tests any claim that exceeds the evaluation. |
| `Rationale` | Why this coordinate set and publication-form are selected, including relation to `A.19.ECS` and existing evaluations named by value. |
| `SoTA-Echoing` | Current practice that changes evaluated-object selection, coordinate choice, value meaning, missingness, comparison, or stop discipline. |
| `Relations` | `A.19.ECS`, `E.8`, `E.21`, `E.22`, `E.23`, and exact domain or neighbour patterns. |

#### E.8.ECSPF:4.2 - Local names and kind settlement

| Local name | Function | Non-use boundary |
|---|---|---|
| `EvaluationCharacteristicSpaceFPFPatternPublicationForm` | The authored FPF pattern body that publishes one evaluation `CharacteristicSpace`. | Not the evaluated object being evaluated, evaluation result, improvement loop, evidence record, or release approval. |
| `ECSPayload` | The by-value `A.19.ECS` specification inside the pattern. | Not an arbitrary table or checklist. |
| `RecognitionEvaluationUseLine` | Early line saying what object is evaluated, for which use, and what the first admissible evaluation use does. | Not a slogan or pattern-title paraphrase. |
| `DiscriminatingCaseBank` | Passing, below-floor, and outside-declared-object-kind boundary worked slices. | Not only positive examples. |
| `RelatedPatternRelationBlock` | Declarative statements of outside claims, each with the applicable pattern id and the definition, constraint, test, or repair guidance used here. | Not a general directory of possibly related patterns and not a list of presumed Methods. |
| `EvaluationResultFormBlock` | Published result-form discipline for this evaluation: required row fields, evidence basis, short rationale rule, and any coordinate-specific payload. | Not a review report, project status, or optional appendix. |
| `CalibrationAndPayloadBlock` | Published adjacent-value calibration points and payload rules for values that need comparator, source-currentness, corpus-projection, worked-case, or retrieval evidence. | Not extra bureaucracy and not a second score system. |
| `PatternVersionQualityEvaluation` | Optional `E.21` evaluation over the authored pattern publication form. | Not a replacement for the evaluation for one evaluated object kind and not publication-form method content. |

