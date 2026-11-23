---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "CharacteristicSpace Construction: Define What Counts as Better"
section_id: "A.19.ECS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__005_solution.md"
commit_sha: "6226816d8005a4c8ee3af338bb3752f6732449a9"
heading_path:
  - "A.19.ECS — CharacteristicSpace Construction: Define What Counts as Better"
  - "A.19.ECS:4 — Solution"
line_start: 36670
line_end: 36779
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

Construct an evaluation specification that declares an A.19 `CharacteristicSpace` and its use. The space contains the characteristic slots, Scale bindings and value meanings. The evaluation separately supplies the object kind, use scope, contrast cases, evidence and missingness rules, result content, calibration, protected trade-offs, statuses and stop or reopen conditions; these consumer rules do not become fields of the space.

`EvaluationCharacteristicSpaceSpec := <EvaluatedObjectKindRef, ObjectVersionUnderImprovementRef?, DeclaredUseScope, WorkingReaderScope, QualificationWindow, DiscriminatingCaseSet, ObjectKindFitRule, CharacteristicSlotSet, ScaleBindingSet, PolarityAndPreferredMovement, FloorAndExceptionalMeaningSet, EvaluationEvidenceBasisRule, EvidenceAndMissingnessRule, ResultRowShape, AdjacentValueRationaleRule, CalibrationPointSet, CoordinateSpecificEvidencePayloadRule?, ProtectedTradeoffSet, DominanceOrComparisonRule?, StatusValueSet, StopOrReopenCondition, NeighborPatternExitSet, E22QuestionFrameUse?, E23StartCondition>`

#### A.19.ECS:4.1 - Local names and kind settlement

| Local name | Use | Non-use boundary |
|---|---|---|
| `EvaluationCharacteristicSpaceSpec` | Local specification for constructing one evaluation `CharacteristicSpace`. | Declaring an evaluation alone establishes neither a value for the evaluated object nor permission to act. |
| `EvaluatedObjectKindRef` | Kind of object being evaluated. | — |
| `DeclaredUseScope` | Use for which the evaluated object is being judged or improved. | Not all possible uses. |
| `DiscriminatingCaseSet` | Cases whose evaluations should differ for the declared use, with the scope and grounds for any outcome that cannot occur there. | Tests the choice of coordinates and the kind boundary. |
| `ObjectKindFitRule` | Determines whether the object belongs to the evaluated kind. For an admitted object the floor and its supporting facts determine the property verdict. | Kind fit can be established while a property value remains unknown. |
| `CharacteristicSlotSet` | The grouped slots, each binding one characteristic to one scale. | Not an arbitrary checklist and not hidden aggregation. |
| `ScaleBindingSet` | The chosen scale and value meaning for each characteristic slot. | — |
| `PolarityAndPreferredMovement` | Direction of preferred movement for each coordinate, or a statement that the coordinate has no simple preferred direction. | Not permission to optimize one coordinate while damaging protected trade-offs. |
| `FloorAndExceptionalMeaningSet` | Viable-for-use and exceptional-for-use value meanings for declared coordinates. | An exceptional value does not establish that future improvement is impossible. |
| `EvaluationEvidenceBasisRule` | The checked evidence loci required for the result: object version, corpus/projection loci when corpus-facing, source-currentness loci when currentness is valued, comparator loci when parity is valued, worked-case loci when case coverage is valued, and any missing or unchecked basis that limits the conclusion. | An unchecked premise leaves its dependent value unestablished; it supplies neither a low property value nor a positive evaluation. Do not infer values from reputation, review state, or absence of visible defects. |
| `EvidenceAndMissingnessRule` | What justifies a value and how missing, censored, unknown, object-kind-fit, or boundary-return cases are handled. | Claiming a property value still requires the evidence specified by the rule. |
| `ResultRowShape` | Required result content: coordinate, value and a short rationale, with evidence loci or payload when needed. | A paragraph or table is sufficient when it carries that content; a value list without its basis is insufficient. |
| `AdjacentValueRationaleRule` | For a discrete ordered Scale, explain why adjacent alternatives misstate the evidence; at the top value, state what would lower or reopen it. For a continuous Scale, justify the value or interval at the applicable resolution and uncertainty. | Do not invent adjacent values for a dense Scale or order for nominal categories. |
| `CalibrationPointSet` | Reusable cases and reference values for common disagreements, including 3/4/5 or equivalent adjacent values when the Scale has them. | Calibration uses the declared Scale and supplies no second score system. |
| `CoordinateSpecificEvidencePayloadRule` | Extra payload that a coordinate needs when a category label can fake discharge: comparator plus selected ingredient plus current locus, source plus adopted payload plus currentness window, projection locus plus retrieval cue, or another payload named by value. | Not the evaluated object's method, and not live evaluated-object text unless the evaluated object itself is an evaluation result or projection carrier. |
| `ProtectedTradeoffSet` | Qualities or neighbour claims that must be checked when visible coordinates improve. | Not a hidden veto without a declared evaluation pattern or value meaning. |
| `PrecisionRepairKindRule` | Rule for checking pre-repair and post-repair evaluated object kind, characteristic kind, relation or claim kind, ontic slot, relation position, use relation, admissible use, and scope when coordinate or evaluation wording is repaired; cite another pattern's definition or constraint when it governs that meaning; name a ClaimGraph only when its identity or edition changes the use. | Not permission to change object kind or slot, relation position, use relation, or claim kind by cleaner wording. |
| `StatusValueSet` | Local admissible-use result values for the evaluation. | Not release state, gate status, or evaluator praise. |
| `E23StartCondition` | Minimum condition for using this evaluation inside `E.23`. | — |

These names are local to this pattern.

#### A.19.ECS:4.2 - Construction moves

Use these moves when constructing or repairing an evaluation. They are not a mandatory work sequence; each move is a required content question whose answer must be recoverable before the evaluation is used for improvement.

1. **Name the evaluated object kind and use.** Say what object kind is being evaluated and for which declared use. When designing criteria for someone else’s decision, recover that decision and the terms governing it from the initiating sources (E.22:4.0). An established use or a prescribed test supplies its own starting extent. If the evaluated object kind is not recoverable, stop before choosing coordinates.
2. **Build the discriminating cases.** Show how the evaluation distinguishes a passing object, a below-floor object and an input outside the admitted kind when those cases are possible. If membership or the operating conditions entail one outcome for the whole admitted domain, show why. Identify an empty domain separately. An excluded input calls for evaluation selection or, when already submitted, the declared kind-fit result.
3. **Choose candidate characteristics.** Draw candidates from the object kind's failure modes, first-principles structure, user or operator harms, domain tradition, current `SoTA`, existing evaluations, and FPF neighbouring patterns named by value.
4. **Bind each slot.** For each candidate, state the characteristic, chosen scale, value set, admissible domain, missingness semantics, and whether the value is a measurement claim or a content evaluation. Keep the property value, object-kind fit, and missing observation distinct. An observed absence of required support can justify a low value; an unperformed check cannot establish that absence. A local diagnostic code such as `0` may represent missing basis only when declared as a code, without the arithmetic or comparison rights of a measured zero. Preserve supported values while leaving dependent conclusions open.
5. **Remove false coordinates.** Drop coordinates that do not change admissible action, do not discriminate the evaluated object, duplicate another coordinate without a different repair action, or belong to another evaluation.
6. **Split compound coordinates.** If a coordinate mixes two repair actions, two object kinds, or two incompatible scales, split it or assign one part to the neighboring pattern that governs that claim.
7. **State preferred movement and trade-offs.** For each declared coordinate, state the preferred direction or explain why no simple direction exists. Name the protected trade-offs that must be checked when the coordinate improves.
8. **Define result form, evidence basis, and calibration.** State the required result content, evidence basis, Scale-appropriate rationale rule, calibration cases for common disagreements, and any coordinate-specific payload needed for high or floor-reaching values.
9. **Define floor, exceptional, status, and stop.** State the viable-for-use floor, exceptional-for-use meaning, status values, and local stop or reopen condition.
10. **Recover dependent claims and their rules.** When a coordinate depends on a separate evidence, assurance, gate, Work, decision, publication, naming, measurement, quality-bundle, OEE/NQD or mathematical-lens claim, identify its subject, relation and the rule that defines or constrains it. An ordinary pattern citation can locate that content. Identify a ClaimGraph only when its identity or edition affects the use; the citation itself establishes no subject fact.
11. **Start `E.23` with a usable evaluation basis.** A repeated improvement loop can start only when the evaluated object version, evidence basis, result form, and evaluation are recoverable for re-evaluation.

#### A.19.ECS:4.3 - Evaluation specification minimum

A.19.ECS does not prescribe a publication or record form. It states which evaluation characteristic-space elements must be recoverable before an evaluation characteristic space is reusable for judgement or improvement. The selected publication or record form may be an FPF pattern, local engineering standard, rubric, table, review form, model card section, protocol note, or project rule, but that form is not governed here.

The evaluation characteristic-space specification must make these items recoverable by value:

| Specification item | Required content |
|---|---|
| `Evaluation problem frame` | Evaluated object kind, declared use, first useful move, existing-evaluation boundary, and what goes wrong if no evaluation exists. |
| `Non-use boundary` | Boundaries that distinguish this evaluation from other questions or claims relevant to its declared use. |
| `Local names and kind settlement` | Any local names used, their meanings, and the boundaries needed to interpret or apply them. |
| `Evaluation expression` | How the required evaluation content is made recoverable in the chosen form. |
| `Object-kind fit rule` | Grounds for admitting an object or treating its dependent coordinates as inapplicable. For an admitted object, specify how the evaluator distinguishes a supported pass, a supported failure and insufficient grounds. |
| `Evaluation evidence basis` | Loci named by value that must be checked or named when a value depends on object version, corpus projection, source currentness, mature comparator, worked case, retrieval, or other external evidence. |
| `Result-row shape` | Coordinate, value and short rationale, plus the evidence locus or payload required for that value. These are content requirements, independent of table or prose layout. |
| `Coordinate set` | Coordinate heads, evaluated-object properties and use conditions, scale/value meanings, evidence loci, and protected trade-offs. |
| `Calibration and payload rules` | Scale-appropriate calibration cases and required coordinate-specific payloads; use adjacent 3/4/5 cases only where the Scale has those values. |
| `Status and stop condition` | Admissible-use statuses, local stop meanings, and reopen conditions. |
| `Worked slices` | Attainable cases that exercise the decisive distinctions, including the treatment of an outside-kind input when possible. Identify the grounds for any outcome excluded throughout the declared domain. |
| `Common anti-patterns` | The false interpretations or values the evaluation must block. |
| `Neighbouring-pattern claim assignment` | Neighbouring FPF patterns named by value and the claims being made that each pattern defines or constrains. |

This minimum is a content requirement, not a file-format requirement. For an FPF pattern publication form, `E.8` still governs the authoring form. `A.19.ECS` only states what the evaluation must make recoverable so that `E.22` can frame an improvement-oriented quality evaluation and `E.23` can run a repeated improvement loop.

When construction or repair changes coordinate wording or evaluation wording, compare the pre-repair and post-repair evaluated object kind, characteristic kind, relation or claim kind, ontic slot, relation position, use relation, admissible use, and scope. Cite another pattern's definition or constraint when it governs the repaired meaning. Identify its ClaimGraph only when identity or edition matters to the repaired use.

A cleaner phrase that changes those items, treats a coordinate position as an object kind, or loses the value's slot, relation position, use relation, or claim kind is a changed evaluation decision, not a wording repair.

#### A.19.ECS:4.4 - Discriminating-case test

Check which of the following outcomes can occur for this use and whether the evaluation can distinguish those that require different action. If the domain definition rules one out, verify the implication and apply the floor to the remaining possibilities. If the domain is empty, there is no instance on which the evaluation shows success or failure. If attainability is unresolved, state what is known about the evaluation.

1. **Passing evaluated object.** The object belongs to the evaluated kind and the applicable evidence establishes that it meets all required floors for this use. An admitted object can still have an unresolved verdict if the required grounds are missing.
2. **Below-floor evaluated object.** The object is of the evaluated object kind or a declared comparable family, but fails one or more floors.
3. **Outside-declared-object-kind boundary case.** Before the evaluation is opened, the object should return to evaluation selection or construction rather than be treated as the evaluated object kind. If the evaluation has already been invoked for that object, the result identifies the object-kind-fit defect or repair status and marks the affected coordinates inapplicable under the declared rule. It does not assign weak property values to an object outside their domain.

Example: for a nuclear-plant adequacy evaluation, a nuclear plant can vary along safety, output, maintenance, regulatory, thermal, waste-handling, grid, and resilience coordinates.

A coal plant may be a power-generation alternative only when the declared use compares power-generation options across plant kinds.

A chair or FPF pattern is outside the nuclear-plant evaluated-object kind: before opening the evaluation it returns to a suitable evaluation; after a forced invocation, the result records the kind mismatch and explains why the plant-specific coordinates do not apply to the chair.
#### A.19.ECS:4.5 - Scale-set improvement

Improve an evaluation when its use misses a consequential defect, rejects an admissible object, recommends a harmful repair, fails on a new use, or demands more work than its decision value justifies. First distinguish a defect in the evaluation from a failure to perform it, unavailable inputs, or reliance beyond its scope. A better-written specification and more agreement among evaluators do not by themselves establish better decisions.

Use the following comparison to decide whether to adopt a change:

1. **Identify what would improve for the recipient.** State which decision, action or cost of obtaining the result could change. An evaluation can yield the right decision at unnecessary cost. Keep the present evaluation as the basis of comparison and propose a change that addresses the identified problem.
2. **Establish the relevant differences independently.** Derive from the use which outcomes, costs and protected qualities matter and which variations can occur. Exercise attainable disagreements when they can change the adoption decision. A subject rule can establish the comparison across its domain. For example, removing a duplicate calculation preserves verdicts if the retained calculation entails the same result for every admitted input. If the second calculation was independently obtained to expose an error, account for the checking function it served.
3. **Apply both evaluations to the same material.** Keep object versions, task conditions and available evidence comparable. Inspect missed defects, false objections, the proposed action, damage from that action and the work needed to obtain and use the answer. Investigate disagreement through the conflicting grounds and conditions; neither majority agreement, stricter verdicts nor a larger finding count establishes practical improvement.
4. **Justify adoption for the intended use.** A change fitted to known cases needs independent grounds covering the claim made for it. These may include new observations under the intended conditions or a subject argument establishing the result across the required domain. State what the evidence covers and any prior exposure or help in an empirical trial. An individual new case can settle its own decision. A wider adoption claim needs grounds for that reach.
5. **Choose at attainable cost.** Use `C.11.DUA` to compare the useful decision change with preparation, data collection, independent judgement, interpretation, repair, repeated evaluation, maintenance, transition and displaced useful work. Keep uncertain and non-commensurable costs visible. Adopt for the supported use, retain on a bounded trial, revise, reject, or keep the existing adequate evaluation.
6. **Preserve scoped results.** Name the changed evaluation and whether earlier results remain comparable, need an explicit bridge, or cannot support the new use. Re-evaluate only conclusions that depend on the changed rule or conditions. A new evaluation does not erase an earlier result within its supported scope.

This comparison checks the evaluation's practical contribution. Use `E.21` separately when the specification is an FPF pattern whose quality is in question; `E.9.DA` for the decision record selecting it; `E.2.DA` for FPF-level Pillar adequacy; `F.18` for naming; and `C.16`, `A.17`, `A.18`, or `A.19` for measurement, scale or characteristic-space admissibility. Their results answer those questions and can supply premises here. Use `E.23` when repeated improvement of the evaluation is needed.

An independent subject basis and a bounded adoption comparison can settle the choice without creating an endless sequence of numeric meta-evaluations. If a decisive premise remains unknown, retain the corresponding limit or trial disposition; another score does not supply that premise.

**Worked comparison.** A team proposes replacing a review criterion that counts source links with one that checks whether a required claim is supported. A known defective text has many links but omits the dependent claim; a difficult admissible text uses one sufficient source and a different valid explanation. The new criterion detects the omission and preserves the admissible explanation. A proposed repair that copies every source paragraph would make ordinary use harder, so the comparison also checks the repaired text.

These are development results on known cases. Adoption still needs an independently grounded new case and an affordable way to obtain the supporting judgement. If the new criterion merely produces more objections or requires whole-corpus reading for every local use, revise it or retain the adequate earlier procedure in its supported scope.

