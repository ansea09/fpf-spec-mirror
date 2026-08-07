---
chunk_kind: "child"
pattern_id: "A.19.ECS"
pattern_title: "Evaluation CharacteristicSpace Construction"
section_id: "A.19.ECS:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/A.19.ECS/A.19.ECS__005_solution.md"
commit_sha: "1602a8d0a6934a99a79ead914610b070cedd86d2"
heading_path:
  - "A.19.ECS — Evaluation CharacteristicSpace Construction"
  - "A.19.ECS:4 — Solution"
line_start: 28914
line_end: 29009
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

| Local name | Role | Non-use boundary |
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
| `EvaluationEvidenceBasisRule` | The checked evidence loci required for the result: object version, corpus/projection loci when corpus-facing, source-currentness loci when currentness is valued, comparator loci when parity is valued, worked-case loci when case coverage is valued, and missing or unchecked loci when they affect values. | Not a separate "not evaluated" alternative, not permission to infer values from reputation, review state, or absence of visible defects, and not the evaluated object's own method or user action. |
| `EvidenceAndMissingnessRule` | What justifies a value and how missing, censored, unknown, object-kind-fit, or boundary-return cases are handled. | Not project evidence, assurance, or gate proof by itself. |
| `ResultRowShape` | Required result row fields for the evaluation, including coordinate, value, and a short rationale; some evaluations may add evidence-locus or payload fields. | Not a free-form review paragraph and not a two-column coordinate/value table. |
| `AdjacentValueRationaleRule` | Rule that each result rationale says why the lower adjacent value would understate the evidence and why the higher adjacent value would overstate it, or for the top value what would lower or reopen the claim. | Not verbosity for its own sake. |
| `CalibrationPointSet` | Reusable 3/4/5 or equivalent adjacent-value calibration points for common evaluator disagreements. | Not a second score system and not a shortcut around the declared scale. |
| `CoordinateSpecificEvidencePayloadRule` | Extra payload that a coordinate needs when a category label can fake discharge: comparator plus selected ingredient plus current locus, source plus adopted payload plus currentness window, projection locus plus retrieval cue, or another payload named by value. | Not administrative burden, not the evaluated object's method, and not live evaluated-object text unless the evaluated object itself is an evaluation result or projection carrier. |
| `ProtectedTradeoffSet` | Qualities or neighbour claims that must be checked when visible coordinates improve. | Not a hidden veto without a declared evaluation pattern or value meaning. |
| `PrecisionRepairKindRule` | Rule for checking pre-repair and post-repair evaluated object kind, characteristic kind, relation or claim kind, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope when coordinate wording or evaluation wording is repaired, with a governing-pattern reference when another pattern governs the kind under repair, relation, claim, or position. | Not a lexical substitution table and not permission to change object kind or slot, relation position, use relation, or claim kind by cleaner wording. |
| `StatusValueSet` | Local admissible-use result values for the evaluation. | Not release state, gate status, or evaluator praise. |
| `E23StartCondition` | Minimum condition for using this evaluation inside `E.23`. | Not the improvement loop itself. |

These names are local to this pattern. They do not mint kernel `U.*` kinds, measurement templates, gate states, evidence kinds, or release states.

#### A.19.ECS:4.2 - Construction moves

Use these moves when constructing or repairing an evaluation. They are not a mandatory work sequence; each move is a required content question whose answer must be recoverable before the evaluation is used for improvement.

1. **Name the evaluated object kind and use.** Say what object kind is being evaluated and for which declared use. If the evaluated object kind is not recoverable, stop before choosing coordinates.
2. **Build the discriminating cases.** Include at least one evaluated object that should pass, one object of the same general family that should fail the floor, and one different object kind that should return to evaluation selection before opening or receive an explicit object-kind-fit defect/value if this evaluation has already been invoked.
3. **Choose candidate characteristics.** Draw candidates from the object kind's real failure modes, first-principles structure, user or operator harms, domain tradition, current `SoTA`, existing evaluations, and FPF neighbouring patterns named by value.
4. **Bind each slot.** For each candidate, state the characteristic, chosen scale, value set, admissible domain, missingness semantics, and whether the value is a measurement claim or an ordinal content evaluation.
5. **Remove false coordinates.** Drop coordinates that do not change admissible action, do not discriminate the evaluated object, duplicate another coordinate without a different repair action, or belong to another exact evaluation.
6. **Split compound coordinates.** If a coordinate mixes two repair actions, two object kinds, or two incompatible scales, split it or assign one part to the neighboring pattern governing the claim that governs it.
7. **State preferred movement and trade-offs.** For each declared coordinate, state the preferred direction or explain why no simple direction exists. Name the protected trade-offs that must be checked when the coordinate improves.
8. **Define result form, evidence basis, and calibration.** State the required result row shape, evidence basis, adjacent-value rationale rule, calibration points for common disagreements, and any coordinate-specific payload needed for high or floor-reaching values.
9. **Define floor, exceptional, status, and stop.** State the viable-for-use floor, exceptional-for-use meaning, status values, and local stop or reopen condition.
10. **Record governing-pattern relations.** Name the FPF pattern that governs evidence, assurance, gate, work, decision, publication, naming, quality-bundle, measurement, OEE/NQD, or mathematical-lens claims when the coordinate depends on them. This is a declarative relation after the coordinate, value, and evidence content; write it as "claim C is governed by pattern P", not as routing or package-placement prose.
11. **Start `E.23` only after evaluation values exist.** A repeated improvement loop can start only when the evaluated object version, evidence basis, result form, and evaluation are recoverable enough for re-evaluation.

#### A.19.ECS:4.3 - Evaluation specification minimum

A.19.ECS does not prescribe a publication or record form. It states which evaluation characteristic-space elements must be recoverable before an evaluation characteristic space is reusable for judgement or improvement. The selected publication or record form may be an FPF pattern, local engineering standard, rubric, table, review form, model card section, protocol note, or project rule, but that form is not governed here. The evaluation characteristic-space specification must make these items recoverable by value:

| Specification item | Required content |
|---|---|
| `Evaluation problem frame` | Evaluated object kind, declared use, first useful move, existing-evaluation boundary, and what goes wrong if no evaluation exists. |
| `Non-use boundary` | Boundaries to single-characteristic, measurement, Q-Bundle, naming, evidence, assurance, gate, work, decision, publication, and loop-method patterns. |
| `Local names and kind settlement` | Local field names, role named by values, and non-use boundaries. |
| `Evaluation record shape` | The local record or bundle shape used by the evaluation. |
| `Object-kind fit rule` | Admissible evaluated object, below-floor evaluated object, and outside-declared-object-kind boundary handling before and after invocation. |
| `Evaluation evidence basis` | Loci named by value that must be checked or named when a value depends on object version, corpus projection, source currentness, mature comparator, worked case, retrieval, or other external evidence. |
| `Result-row shape` | Required result row fields, at minimum coordinate, value, and short rationale; any required evidence-locus or coordinate-specific payload fields are declared here. |
| `Coordinate set` | Coordinate heads, properties of the evaluated object, evaluated-object properties and use conditions, scale/value meanings, evidence loci, and protected trade-offs. |
| `Calibration and payload rules` | Adjacent-value calibration points and coordinate-specific payloads that prevent impressionistic `3`/`4`/`5` assignment or category-list discharge. |
| `Status and stop condition` | Admissible-use statuses, local stop meanings, and reopen conditions. |
| `Worked slices` | At least one passing evaluated object, one below-floor evaluated object, and one outside-declared-object-kind boundary case. |
| `Common anti-patterns` | The false interpretations or values the evaluation must block. |
| `Neighbouring-pattern claim assignment` | Neighbouring FPF patterns named by value and the claims being made that each pattern governs. |

This minimum is a content requirement, not a file-format requirement. For an FPF pattern publication form, `E.8` still governs the authoring form. `A.19.ECS` only states what the evaluation must make recoverable so that `E.22` can frame an improvement-oriented quality evaluation and `E.23` can run a repeated improvement loop.

When construction or repair changes coordinate wording or evaluation wording, the evaluation characteristic-space specification records `PrecisionRepairKindRule` or an equivalent result-row requirement. The check compares the pre-repair and post-repair evaluated object kind, characteristic kind, relation or claim kind, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope, and names the governing pattern when another pattern governs the kind under repair, relation, claim, or position. A cleaner phrase that changes those items, treats a coordinate position as an object kind, or loses the value's slot, relation position, use relation, or claim kind is a changed evaluation decision, not a wording repair.

#### A.19.ECS:4.4 - Discriminating-case test

An evaluation is not ready if it cannot distinguish these three outcomes:

1. **Admissible evaluated object.** The object is of the evaluated object kind and can meet or exceed the floor under the declared use.
2. **Below-floor evaluated object.** The object is of the evaluated object kind or a declared comparable family, but fails one or more floors.
3. **Outside-declared-object-kind boundary case.** Before the evaluation is opened, the object should return to evaluation selection or construction rather than be treated as the evaluated object kind. If the evaluation has already been invoked for that object, the result is an explicit object-kind-fit defect/value or repair status, not omitted coordinates.

Example: for a nuclear-plant adequacy evaluation, a nuclear plant can vary along safety, output, maintenance, regulatory, thermal, waste-handling, grid, and resilience coordinates. A coal plant may be a power-generation alternative only when the declared use explicitly compares power-generation options across plant kinds. A chair or FPF pattern is outside the nuclear-plant evaluated-object kind: before opening the evaluation it returns to a suitable evaluation; after a forced invocation, the record shows an object-kind-fit defect/value rather than pretending the chair has weak nuclear-plant quality or silently skipping coordinates.
#### A.19.ECS:4.5 - Scale-set improvement

The evaluation characteristic space itself can be improved. In that case, the evaluated object is the current `EvaluationCharacteristicSpaceSpec` version, not the original evaluated object.

Use `E.23` for the repeated improvement method over the scale set when the improvement aim is live. The evaluation for that meta-level improvement may be:

- this pattern's conformance checklist for whether the scale set is constructible and usable;
- `E.21` when the evaluation characteristic-space specification is itself an FPF pattern version;
- `E.9.DA` when the decision record selecting the scale set is the `DRR` decision-adequacy object being evaluated;
- `E.2.DA` when the scale set changes FPF-level Pillar adequacy;
- `F.18` when the live problem is name choice for the scale-set heads;
- `C.16`, `A.17`, `A.18`, or `A.19` when the live problem is measurement admissibility, scale lawfulness, or characteristic-space admissibility.

Do not improve an evaluated object by silently changing its evaluation. If the evaluation changes, the loop record names the changed evaluation version and states whether earlier object-version values remain comparable, need a bridge, or must be retired for the new use.

