---
chunk_kind: "child"
pattern_id: "E.8.ECSPF"
pattern_title: "FPF Pattern Publication Form for Evaluation Guidance"
section_id: "E.8.ECSPF:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.8.ECSPF/E.8.ECSPF__005_solution.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.8.ECSPF — FPF Pattern Publication Form for Evaluation Guidance"
  - "E.8.ECSPF:4 — Solution"
line_start: 73862
line_end: 73924
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

When an accepted `A.19.ECS` specification is selected for durable FPF publication, use `E.8` to write a pattern that teaches the specified evaluation, with these additional placement rules:

1. **Keep the objects separate.** The accepted specification says what the evaluation requires. The publication form arranges the pattern. The authored content teaches a later practitioner how to evaluate an object. That later evaluation produces a result. Neither the specification nor its `CharacteristicSpace`, the evaluation, the evaluated object, or the result becomes the pattern.
2. **Put recognition before coordinates.** The opening text names evaluated object kind, declared use, working reader, qualification window, first evaluation use, FPF-publication boundary, what goes wrong, and what the pattern buys before any dense table.
3. **Carry the complete accepted specification by value.** Put every required value, and every optional value whose trigger holds, where a practitioner needs it. Do not discharge this move by citing `A.19.ECS`, copying field names, or pointing to an author-only record. The `Solution` and its nearby practitioner-use sections carry the actual selected values from the accepted specification.
4. **Use worked slices as the discriminating-case test.** Archetypal Grounding and worked cases include a passing evaluated object, a below-floor evaluated object, and an outside-declared-object-kind boundary case.
5. **Keep ordinal coordinates separate and protect against proxy improvement.** Do not create an undeclared total, average, or “overall score” from ordinal coordinates. Whenever a visible value improves, ask whether any intended value or protected trade-off became worse. If the published guidance would reward that loss, stop the comparison and reopen the specification. If a bounded use genuinely needs scalarization, name the particular method, its use, the information it loses, and its applicability and stop or return conditions; do not present that scalar as “the evaluation”.
6. **Keep checklist rows secondary.** Conformance checks verify that the evaluation is recoverable and usable. They do not become the user's method.
7. **State the concrete contribution used for each outside claim.** When `Relations` or a grounded local boundary makes a claim about, for example, evidence, assurance, work, naming, measurement, or improvement, cite the applicable `PatternID` and say in ordinary terms what its content contributes here. It may supply an evidence-use boundary, an assurance calculus, a gate decision rule, a measurement test, repair guidance, or something else; these are examples, not a closed vocabulary. The `PatternID` is enough for ordinary use. Name a particular assertion, episteme edition, or `ClaimGraph` only when interpretation, migration, conflict, publication, or reuse depends on that identity. Treat guidance as a `U.Method`, a qualifying `U.MethodDescription`, or a particular Method use only after its own admission test passes and the current claim needs that identity. Use `F.19` for ordinary wording repair. When a repair can change an FPF-governed meaning, confirm that the evaluated object and its kind, relation or claim kind, live ontic slot, relation position, use relation, admissible use, and scope remain recoverable before and after the repair, as applicable to the changed claim.
8. **Evaluate the authored pattern with `E.21`.** When the FPF pattern is under quality improvement, a reviewer uses `E.21` to evaluate that pattern version. A later evaluator uses the guidance published in the pattern to evaluate the declared object kind. The `E.21` result, corpus-projection evidence, README/ToC/E.11/I.2 alignment, retrieval or cold-reader evidence, monolith parity, landing evidence, and developer/reviewer/executor correspondence stay in the quality, review, projection, or release carriers unless the pattern's own `EntityOfConcern` and user-facing action are that evaluation or projection work.

The authoring flow and the quality-improvement flow are different. First an author carries an accepted specification into a pattern. Later a practitioner may use that pattern's guidance to evaluate an object and record a result. `E.22` and `E.23` provide guidance for framing or repeating that work. A reviewer's later `E.21` evaluation of this pattern is evidence about the authored pattern, not part of the object evaluation that the pattern teaches. That evidence may cause edits to recognition text, coordinates, cases, or boundaries, but it remains outside the pattern unless rewritten as user-facing evaluation guidance.

#### E.8.ECSPF:4.1 - Canonical placement table

| E.8 section | Evaluation-specific content |
|---|---|
| `Problem frame` | Evaluated object kind, declared use, working reader, qualification window, first useful evaluation use, FPF-publication boundary, what goes wrong without this evaluation, and what practical move the evaluation enables. |
| `Problem` | Failure modes that the evaluation prevents: wrong-kind scoring, hidden value drift, proxy value, one-score collapse, missingness confusion, or neighbour theft. |
| `Forces` | Tensions among reuse, coordinate count, readability, measurement admissibility, trade-off protection, local stop, and open-ended improvement. |
| `Solution` | Every required accepted-specification value and every triggered optional value: object and use, reader and qualification limits, cases and kind-fit, coordinate and scale bindings, value meanings and preferred movement, evidence and missingness, result form and calibration, coordinate-specific evidence, trade-offs and comparison, statuses, exits, and stop or reopen conditions. |
| `Archetypal Grounding` | At least one passing evaluated object, one below-floor evaluated object, and one outside-declared-object-kind boundary case. |
| `Bias-Annotation` | Known skew in source examples, reader family, domain tradition, measurement preference, benchmark preference, or FPF-internal reuse. |
| `Conformance Checklist` | Checks that the specification is recoverable, not that a reviewer likes the evaluated object. |
| `Common Anti-Patterns` | Score-sheet pattern, checklist-as-solution, table-first recognition failure, neighbour theft, one total score, hidden value drift. |
| `Consequences` | What changes in practice after a conforming evaluation use, its scope, next action, stop or reopen, and the concrete contribution supplied by neighbouring content for any outside claim. Add a denied consequence only when a plausible intended reader has an independent reason to infer it. |
| `Rationale` | Why this coordinate set and publication-form are selected, including relation to `A.19.ECS` and existing evaluations named by value. |
| `SoTA-Echoing` | Current practice that changes evaluated-object selection, coordinate choice, value meaning, missingness, comparison, or stop discipline. |
| `Relations` | `A.19.ECS`, `E.8`, `E.21`, `E.22`, `E.23`, and exact domain or neighbour patterns. |

#### E.8.ECSPF:4.2 - Local names and kind settlement

| Local name | Function | Non-use boundary |
|---|---|---|
| `AcceptedEvaluationCharacteristicSpaceSpec` | The accepted `A.19.ECS` specification selected for publication. | Not the pattern, the later evaluation, or its result. |
| `EvaluationPatternPublicationForm` | The `E.8` arrangement used to publish the guidance as an FPF pattern. | Not the accepted specification or the authored words, tables, and cases. |
| `AuthoredEvaluationPatternContent` | The recognition text, solution, value meanings, cases, result form, and boundaries through which the pattern teaches the evaluation. | Not an occurrence of evaluation work and not its result. |
| `LaterEvaluationUse` | A later practitioner judges an object using the published guidance and records a result. | Establish a particular `MethodDescription`, `Method`, assignment, or dated `Work` only when that identity matters to the receiving claim. |
| `EvaluationResult` | The coordinate rows, evidence, rationales, and status produced by that later evaluation. | Not the pattern and not the accepted specification. |
| `RecognitionEvaluationUseLine` | Early line saying what object is evaluated, for which use, and what the first admissible evaluation use does. | Not a slogan or pattern-title paraphrase. |
| `DiscriminatingCaseBank` | Passing, below-floor, and outside-declared-object-kind boundary worked slices. | Not only positive examples. |
| `RelatedPatternRelationBlock` | Statements of outside claims, each with the applicable pattern id and its concrete contribution in this use. | Not a general directory, a closed relation-verb vocabulary, or a list of presumed Methods. |
| `EvaluationResultFormBlock` | Published result-form discipline for this evaluation: required row fields, evidence basis, short rationale rule, and any coordinate-specific payload. | Not a review report, project status, or optional appendix. |
| `CalibrationAndPayloadBlock` | Published adjacent-value calibration points and payload rules for values that need comparator, source-currentness, corpus-projection, worked-case, or retrieval evidence. | Not extra bureaucracy and not a second score system. |
| `PatternVersionQualityEvaluation` | Optional `E.21` evaluation over the authored pattern publication form. | Not a replacement for the evaluation for one evaluated object kind and not publication-form method content. |

#### E.8.ECSPF:4.3 - By-value carry-through

Carry the accepted specification through the pattern in practitioner order. “By value” means that the reader can find the actual selected value and use it; a field name, an `A.19.ECS` citation, or an author-only attachment is not enough.

| Practitioner need | Accepted values that must be present |
|---|---|
| Recognize whether to enter | `EvaluatedObjectKindRef`, `DeclaredUseScope`, `WorkingReaderScope`, `QualificationWindow`, and `ObjectVersionUnderImprovementRef` when the evaluation is tied to one object version. |
| Test the boundary | `DiscriminatingCaseSet` and `ObjectKindFitRule`, including admissible, below-floor, and outside-kind outcomes. |
| Judge the object | `CharacteristicSlotSet`, `ScaleBindingSet`, `PolarityAndPreferredMovement`, and `FloorAndExceptionalMeaningSet`, with the actual coordinate and value meanings rather than their field labels. |
| Justify and record a result | `EvaluationEvidenceBasisRule`, `EvidenceAndMissingnessRule`, `ResultRowShape`, `AdjacentValueRationaleRule`, `CalibrationPointSet`, and `CoordinateSpecificEvidencePayloadRule` whenever a coordinate triggers such a payload. |
| Protect a useful result from false improvement | `ProtectedTradeoffSet` and `DominanceOrComparisonRule` whenever the accepted specification declares a comparison rule. |
| Continue, stop, or leave this evaluation | `StatusValueSet`, `StopOrReopenCondition`, `NeighborPatternExitSet`, `E22QuestionFrameUse` when selected, and `E23StartCondition`. |

The fields may be expressed in plain language, tables, or worked cases. Keep them close to the practitioner action they qualify. Do not hide required values in conformance rows, source notes, or review evidence.

