---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction: Define What Counts as Better"
section_id: "A.19.ECS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__005_solution.md"
commit_sha: "8685aeda98d24b7a7533364cb0df680eccfbfd4c"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction: Define What Counts as Better"
  - "A.19.ECS:4 — Solution"
line_start: 32599
line_end: 32698
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

### A.19.ECS:4 - Solution

Construct an evaluation `CharacteristicSpace` by declaring the evaluated object kind, use scope, contrast cases, characteristic slots, scale bindings, value meanings, evidence-basis and missingness rules, result-row shape, calibration points, coordinate-specific evidence payloads, protected trade-offs, status meanings, and stop or reopen conditions.

`EvaluationCharacteristicSpaceSpec := <EvaluatedObjectKindRef, ObjectVersionUnderImprovementRef?, DeclaredUseScope, WorkingReaderScope, QualificationWindow, DiscriminatingCaseSet, ObjectKindFitRule, CharacteristicSlotSet, ScaleBindingSet, PolarityAndPreferredMovement, FloorAndExceptionalMeaningSet, EvaluationEvidenceBasisRule, EvidenceAndMissingnessRule, ResultRowShape, AdjacentValueRationaleRule, CalibrationPointSet, CoordinateSpecificEvidencePayloadRule?, ProtectedTradeoffSet, DominanceOrComparisonRule?, StatusValueSet, StopOrReopenCondition, NeighborPatternExitSet, E22QuestionFrameUse?, E23StartCondition>`

#### A.19.ECS:4.1 - Local names and kind settlement

| Local name | Use | Non-use boundary |
|---|---|---|
| `EvaluationCharacteristicSpaceSpec` | Local specification for constructing one evaluation `CharacteristicSpace`. | Not a score sheet, review packet, work plan, gate, evidence record, or project approval. |
| `EvaluatedObjectKindRef` | Exact kind of object the evaluation evaluates. | Not a vague artifact, file bundle, campaign, chat, or source collection. |
| `DeclaredUseScope` | Use for which the evaluated object is being judged or improved. | Not all possible uses. |
| `DiscriminatingCaseSet` | Positive, below-floor, and outside-declared-object-kind boundary cases used to test whether the characteristic space distinguishes the evaluated object kind and use. | Not a substitute for the coordinate set. |
| `ObjectKindFitRule` | Rule for admissible evaluated object, below-floor evaluated object, and outside-declared-object-kind boundary case. | Not permission to omit declared coordinates after an evaluation has been invoked. |
| `CharacteristicSlotSet` | The grouped slots, each binding one characteristic to one scale. | Not an arbitrary checklist and not hidden aggregation. |
| `ScaleBindingSet` | The chosen scale and value meaning for each characteristic slot. | Not a metric dashboard unless a distance or measurement claim is explicitly declared by the neighbour. |
| `PolarityAndPreferredMovement` | Direction of preferred movement for each coordinate, or a statement that the coordinate has no simple preferred direction. | Not permission to optimize one coordinate while damaging protected trade-offs. |
| `FloorAndExceptionalMeaningSet` | Viable-for-use and exceptional-for-use value meanings for declared coordinates. | Not a maturity ladder and not proof that future improvement is impossible. |
| `EvaluationEvidenceBasisRule` | The checked evidence loci required for the result: object version, corpus/projection loci when corpus-facing, source-currentness loci when currentness is valued, comparator loci when parity is valued, worked-case loci when case coverage is valued, and any missing or unchecked basis that limits the conclusion. | An unchecked premise leaves its dependent value unestablished; it supplies neither a low property value nor a positive evaluation. Do not infer values from reputation, review state, or absence of visible defects. |
| `EvidenceAndMissingnessRule` | What justifies a value and how missing, censored, unknown, object-kind-fit, or boundary-return cases are handled. | Not project evidence, assurance, or gate proof by itself. |
| `ResultRowShape` | Required result row fields for the evaluation, including coordinate, value, and a short rationale; some evaluations may add evidence-locus or payload fields. | Not a free-form review paragraph and not a two-column coordinate/value table. |
| `AdjacentValueRationaleRule` | Rule that each result rationale says why the lower adjacent value would understate the evidence and why the higher adjacent value would overstate it, or for the top value what would lower or reopen the claim. | Not verbosity for its own sake. |
| `CalibrationPointSet` | Reusable 3/4/5 or equivalent adjacent-value calibration points for common evaluator disagreements. | Not a second score system and not a shortcut around the declared scale. |
| `CoordinateSpecificEvidencePayloadRule` | Extra payload that a coordinate needs when a category label can fake discharge: comparator plus selected ingredient plus current locus, source plus adopted payload plus currentness window, projection locus plus retrieval cue, or another payload named by value. | Not administrative burden, not the evaluated object's method, and not live evaluated-object text unless the evaluated object itself is an evaluation result or projection carrier. |
| `ProtectedTradeoffSet` | Qualities or neighbour claims that must be checked when visible coordinates improve. | Not a hidden veto without a declared evaluation pattern or value meaning. |
| `PrecisionRepairKindRule` | Rule for checking pre-repair and post-repair evaluated object kind, characteristic kind, relation or claim kind, current ontic slot, relation position, use relation, admissible use, and scope when coordinate or evaluation wording is repaired; when another pattern description contains the defining or constraining content, cite its `subjectPatternLocator` and exact ClaimGraph. | Not a lexical substitution table and not permission to change object kind or slot, relation position, use relation, or claim kind by cleaner wording. |
| `StatusValueSet` | Local admissible-use result values for the evaluation. | Not release state, gate status, or evaluator praise. |
| `E23StartCondition` | Minimum condition for using this evaluation inside `E.23`. | Not the improvement loop itself. |

These names are local to this pattern. They do not mint kernel `U.*` kinds, measurement templates, gate states, evidence kinds, or release states.

#### A.19.ECS:4.2 - Construction moves

Use these moves when constructing or repairing an evaluation. They are not a mandatory work sequence; each move is a required content question whose answer must be recoverable before the evaluation is used for improvement.

1. **Name the evaluated object kind and use.** Say what object kind is being evaluated and for which declared use. If the evaluated object kind is not recoverable, stop before choosing coordinates.
2. **Build the discriminating cases.** Include at least one evaluated object that should pass, one object of the same general family that should fail the floor, and one different object kind that should return to evaluation selection before opening or receive an explicit object-kind-fit defect/value if this evaluation has already been invoked.
3. **Choose candidate characteristics.** Draw candidates from the object kind's real failure modes, first-principles structure, user or operator harms, domain tradition, current `SoTA`, existing evaluations, and FPF neighbouring patterns named by value.
4. **Bind each slot.** For each candidate, state the characteristic, chosen scale, value set, admissible domain, missingness semantics, and whether the value is a measurement claim or an ordinal content evaluation. Keep the property value, object-kind fit, and missing observation distinct. An observed absence of required support can justify a low value; an unperformed check cannot establish that absence. A local diagnostic code such as `0` may represent missing basis only when explicitly declared as a code, without the arithmetic or comparison rights of a measured zero. Preserve already supported values while leaving dependent conclusions open.
5. **Remove false coordinates.** Drop coordinates that do not change admissible action, do not discriminate the evaluated object, duplicate another coordinate without a different repair action, or belong to another exact evaluation.
6. **Split compound coordinates.** If a coordinate mixes two repair actions, two object kinds, or two incompatible scales, split it or assign one part to the neighboring pattern governing the claim that governs it.
7. **State preferred movement and trade-offs.** For each declared coordinate, state the preferred direction or explain why no simple direction exists. Name the protected trade-offs that must be checked when the coordinate improves.
8. **Define result form, evidence basis, and calibration.** State the required result row shape, evidence basis, adjacent-value rationale rule, calibration points for common disagreements, and any coordinate-specific payload needed for high or floor-reaching values.
9. **Define floor, exceptional, status, and stop.** State the viable-for-use floor, exceptional-for-use meaning, status values, and local stop or reopen condition.
10. **Record subject assertions and their rule loci.** When the coordinate depends on evidence, assurance, gate, work, decision, publication, naming, quality-bundle, measurement, OEE/NQD, or mathematical-lens content, name the exact subject, relation function, defining or constraining ClaimGraph, and subject assertion. A `subjectPatternLocator` may help find that ClaimGraph but asserts no governance relation; do not rewrite the dependency as routing or package-placement prose.
11. **Start `E.23` only after evaluation values exist.** A repeated improvement loop can start only when the evaluated object version, evidence basis, result form, and evaluation are recoverable enough for re-evaluation.

#### A.19.ECS:4.3 - Evaluation specification minimum

A.19.ECS does not prescribe a publication or record form. It states which evaluation characteristic-space elements must be recoverable before an evaluation characteristic space is reusable for judgement or improvement. The selected publication or record form may be an FPF pattern, local engineering standard, rubric, table, review form, model card section, protocol note, or project rule, but that form is not governed here. The evaluation characteristic-space specification must make these items recoverable by value:

| Specification item | Required content |
|---|---|
| `Evaluation problem frame` | Evaluated object kind, declared use, first useful move, existing-evaluation boundary, and what goes wrong if no evaluation exists. |
| `Non-use boundary` | Boundaries to single-characteristic, measurement, Q-Bundle, naming, evidence, assurance, gate, work, decision, publication, and loop-method patterns. |
| `Local names and kind settlement` | Local field names, use named by values, and non-use boundaries. |
| `Evaluation record shape` | The local record or bundle shape used by the evaluation. |
| `Object-kind fit rule` | Admissible evaluated object, below-floor evaluated object, and outside-declared-object-kind boundary handling before and after invocation. |
| `Evaluation evidence basis` | Loci named by value that must be checked or named when a value depends on object version, corpus projection, source currentness, mature comparator, worked case, retrieval, or other external evidence. |
| `Result-row shape` | Required result row fields, at minimum coordinate, value, and short rationale; any required evidence-locus or coordinate-specific payload fields are declared here. |
| `Coordinate set` | Coordinate heads, properties of the evaluated object, evaluated-object properties and use conditions, scale/value meanings, evidence loci, and protected trade-offs. |
| `Calibration and payload rules` | Adjacent-value calibration points and coordinate-specific payloads that prevent impressionistic `3`/`4`/`5` assignment or category-list discharge. |
| `Status and stop condition` | Admissible-use statuses, local stop meanings, and reopen conditions. |
| `Worked slices` | At least one passing evaluated object, one below-floor evaluated object, and one outside-declared-object-kind boundary case. |
| `Common anti-patterns` | The false interpretations or values the evaluation must block. |
| `Neighbouring-pattern claim assignment` | Neighbouring FPF patterns named by value and the claims being made that each pattern defines or constrains. |

This minimum is a content requirement, not a file-format requirement. For an FPF pattern publication form, `E.8` still governs the authoring form. `A.19.ECS` only states what the evaluation must make recoverable so that `E.22` can frame an improvement-oriented quality evaluation and `E.23` can run a repeated improvement loop.

When construction or repair changes coordinate wording or evaluation wording, the evaluation characteristic-space specification records `PrecisionRepairKindRule` or an equivalent result-row requirement. The check compares the pre-repair and post-repair evaluated object kind, characteristic kind, relation or claim kind, current ontic slot, relation position, use relation, admissible use, and scope; when another pattern description contains the relevant definition or constraint, it cites that exact ClaimGraph and may add a non-semantic subject-pattern locator. A cleaner phrase that changes those items, treats a coordinate position as an object kind, or loses the value's slot, relation position, use relation, or claim kind is a changed evaluation decision, not a wording repair.

#### A.19.ECS:4.4 - Discriminating-case test

An evaluation is not ready if it cannot distinguish these three outcomes:

1. **Admissible evaluated object.** The object is of the evaluated object kind and can meet or exceed the floor under the declared use.
2. **Below-floor evaluated object.** The object is of the evaluated object kind or a declared comparable family, but fails one or more floors.
3. **Outside-declared-object-kind boundary case.** Before the evaluation is opened, the object should return to evaluation selection or construction rather than be treated as the evaluated object kind. If the evaluation has already been invoked for that object, the result is an explicit object-kind-fit defect/value or repair status, not omitted coordinates.

Example: for a nuclear-plant adequacy evaluation, a nuclear plant can vary along safety, output, maintenance, regulatory, thermal, waste-handling, grid, and resilience coordinates. A coal plant may be a power-generation alternative only when the declared use explicitly compares power-generation options across plant kinds. A chair or FPF pattern is outside the nuclear-plant evaluated-object kind: before opening the evaluation it returns to a suitable evaluation; after a forced invocation, the record shows an object-kind-fit defect/value rather than pretending the chair has weak nuclear-plant quality or silently skipping coordinates.
#### A.19.ECS:4.5 - Scale-set improvement

Improve an evaluation when its use misses a consequential defect, rejects an admissible object, recommends a harmful repair, fails on a new use, or demands more work than its decision value justifies. First distinguish a defect in the evaluation from a failure to perform it, unavailable inputs, or reliance beyond its scope. A better-written specification and more agreement among evaluators do not by themselves establish better decisions.

Use the following comparison to decide whether to adopt a change:

1. **Name the lost practical result.** State which decision or next action the current evaluation gets wrong or cannot support, for which object and use. Preserve the current evaluation as the comparison basis and propose the smallest change that addresses that loss.
2. **Establish contrasting cases independently of the proposed evaluation.** Use subject requirements, observed work results, or other applicable grounds to identify a consequential defect and a difficult but admissible case. Include a case in which an apparently helpful repair would damage a protected quality. The proposed evaluation's own verdict cannot establish these cases' correctness.
3. **Apply both evaluations to the same material.** Keep object versions, task conditions and available evidence comparable. Inspect missed defects, false objections, the proposed action, damage from that action and the work needed to obtain and use the answer. Investigate disagreement through the conflicting grounds and conditions; neither majority agreement, stricter verdicts nor a larger finding count establishes practical improvement.
4. **Test adoption beyond the cases used for tuning.** When the change was fitted to known cases, use a new case with an independent basis for the adoption decision. Keep its relevant answer out of tuning and disclose prior exposure or assistance. Replaying a known case remains useful development evidence; if no independent case is available, limit the conclusion to a trial in the examined scope.
5. **Choose at attainable cost.** Use `C.11.DUA` to compare the useful decision change with preparation, data collection, independent judgement, interpretation, repair, repeated evaluation, maintenance, transition and displaced useful work. Keep uncertain and non-commensurable costs visible. Adopt for the supported use, retain on a bounded trial, revise, reject, or keep the existing adequate evaluation.
6. **Preserve scoped results.** Name the changed evaluation and whether earlier results remain comparable, need an explicit bridge, or cannot support the new use. Re-evaluate only conclusions that depend on the changed rule or conditions. A new evaluation does not erase an earlier result within its supported scope.

This comparison checks the evaluation's practical contribution. Use `E.21` separately when the specification is an FPF pattern whose quality is in question; `E.9.DA` for the decision record selecting it; `E.2.DA` for FPF-level Pillar adequacy; `F.18` for naming; and `C.16`, `A.17`, `A.18`, or `A.19` for measurement, scale or characteristic-space admissibility. Their results answer those questions and can supply premises here. Use `E.23` when repeated improvement of the evaluation is needed.

An independent subject basis and a bounded adoption comparison can settle the current choice without creating an endless sequence of numeric meta-evaluations. If a decisive premise remains unknown, retain the corresponding limit or trial disposition; another score does not supply that premise.

**Worked comparison.** A team proposes replacing a review criterion that counts source links with one that checks whether a required claim is actually supported. A known defective text has many links but omits the dependent claim; a difficult admissible text uses one sufficient source and a different valid explanation. The new criterion detects the omission and preserves the admissible explanation. A proposed repair that copies every source paragraph would make ordinary use harder, so the comparison also checks the repaired text. These are development results on known cases. Adoption still needs an independently grounded new case and an affordable way to obtain the supporting judgement. If the new criterion merely produces more objections or requires whole-corpus reading for every local use, revise it or retain the adequate earlier procedure in its supported scope.

