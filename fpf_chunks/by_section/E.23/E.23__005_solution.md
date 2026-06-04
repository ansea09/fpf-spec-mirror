---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__005_solution.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:4 — Solution"
line_start: 68702
line_end: 68877
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.24"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:4 - Solution

Run a `QualityImprovementLoopMethod` only after naming the exact `ObjectVersionUnderImprovement` and the `ObjectUnderImprovementEvaluationRef` that supplies values and stop meanings.

`QualityImprovementLoopMethod := <ObjectUnderImprovementRef, ObjectUnderImprovementEvaluationRef, ImprovementAim, DeclaredFloor?, TradeoffProtectionSet, QualityReadQuestionFrameRef, MethodFamilySelection, OperationFamilySelectionSet?, QualityReviewFindingRows?, ChangedObjectVersionRef?, ObjectUnderImprovementEvaluationReRead, CostAndRiskAccount, StopNarrowContinueSwitchHoldDecision>`

`ObjectUnderImprovementRef` is a local field for the exact object kind and exact version under the object-under-improvement evaluation. It does not mint a broad new kernel kind.

Admissible object forms include one pattern version, one `DRR` version, episteme publication, architecture description, method description, policy text, benchmark result, declared transduction result, or another exact object kind named by the object-under-improvement evaluation. The object under improvement is not a file bundle, task list, campaign, chat, review packet, source collection, or vague produced thing unless the object-under-improvement evaluation explicitly reads that object kind.

When the object under improvement is a transduction result, the loop also names the producing transduction or `E.18` graph, path, crossing, or flow-valuation context when that context is live; the exact result kind; the object version under improvement; and the object-under-improvement evaluation. The system carrier or rendering of the result is not the object under improvement unless the object-under-improvement evaluation explicitly reads that system carrier or rendering kind.

When the object-under-improvement evaluation also supplies the `Q` side of an NQD or OEE comparison, `E.23` may govern repeated changes to one candidate, object version under improvement, or declared transduction result so that its `Q` position moves relative to a declared comparison set, external candidate set, current non-dominated front, competing candidate set, `SoTA` line, or selected set. `E.23` does not govern novelty, diversity, descriptor or distance definitions, generation, front or archive insertion, candidate-pool policy, selected-set publication, parity, or refresh semantics.

#### E.23:4.1 - Local names and kind settlement

| Local name | Role | Non-use boundary |
|---|---|---|
| `QualityImprovementLoopMethod` | Repeated improvement method for one object under improvement under one object-under-improvement evaluation. | Not a universal work sequence, not project management, not a process script, and not proof of quality by itself. |
| `ObjectUnderImprovementRef` | Exact object kind and exact version under improvement. | Not a source bundle, campaign, chat, task list, review packet, source collection, or generic produced thing unless the object-under-improvement evaluation reads that object kind. |
| `ObjectUnderImprovementEvaluationRef` | Pattern, object-under-improvement evaluation `CharacteristicSpace`, Q-Bundle, rubric, review profile, or local evaluation that supplies values and stop meanings. | Not an opinion, prompt, checklist count, coordinate set, or score sheet invented by `E.23`; construct missing object-under-improvement evaluation `CharacteristicSpace` through `A.19.ECS`. |
| `ImprovementAim` | Declared desired movement under the object-under-improvement evaluation: floor repair, exceptional improvement, trade-off inspection, absorption impact, open-question discovery, or another exact object-under-improvement evaluation aim. | Not permission to optimize visible values while damaging protected qualities. |
| `MethodFamilySelection` | Selected method family for the current object under improvement: general adaptive loop, specialized cycle, or mixed operation-family set. | Not a universal ladder, maturity level, or new kernel kind. |
| `OperationFamilySelectionSet` | Optional operation families selected because they can move the object-under-improvement evaluation enough to justify their cost and risk. | Not mandatory apparatus for every loop. |
| `ObjectUnderImprovementEvaluationReRead` | Re-run or cited result from the object-under-improvement evaluation on the changed object version under improvement. | Not repair self-assessment, reviewer praise, discharge count, or absence of blockers. |
| `CostAndRiskAccount` | Declared cost and risk account used to judge whether the next pass or added operation is worth doing. | Not a scalar quality value and not resource ontology. |
| `StopNarrowContinueSwitchHoldDecision` | The local decision after a re-read: stop, narrow the aim, continue, switch method family, or hold for more exact information. | Not a release gate, work authority, safety acceptance, or evidence claim by itself. |
| `QualityImprovementLoopRecord` | Local record of one loop pass or pass sequence: object version under improvement, object-under-improvement evaluation, applied rows, re-read result, trade-offs, cost and risk account, and stop decision. | Not proof of quality by itself and not a project release, gate, evidence, assurance, safety, compliance, or work-authority record. |
| `QualitySideMovementClaim` | Local claim that the changed object version moved on declared `Q` components under one NQD/OEE comparison. | Not an `N` or `D` claim, not archive or front insertion, not candidate-pool policy, not selected-set publication, not parity, and not refresh. |
| `SourceContributionStratum` | One distinguishable contribution type made by an accepted source or practice line inside a source-bearing improvement: value semantics, operation family, boundary, comparison discipline, failure mode, protected trade-off, or stop discipline. | Not a maturity level, not an architecture layer, not evidence rank, and not permission to cite a source without saying what it contributes. |
| `SourceComposedResultClaim` | The changed object version capability, move, explanation, method result, or other object-under-improvement evaluation-readable result produced by composing accepted source or practice lines. | Not a mathematical function, not a TGA morphism, not a module function, not source volume, and not a novelty claim without object-under-improvement evaluation re-read. |

The words `loop`, `method family`, and `operation family` are local method words. They do not create a sequence that every project must run. They name repeated use of an object-under-improvement evaluation-controlled improvement method.

#### E.23:4.2 - Relationship to E.22, A.19.ECS, and object-under-improvement evaluations

`E.23` is one loop method, not a separate cycle for each object kind. Different applications are object-under-improvement-specific loop instances: they differ by `ObjectUnderImprovementRef`, object-under-improvement evaluation, active coordinates, protected trade-offs, stop meanings, and neighbour exits. A product-design instance, safety-case instance, pattern-version instance, `DRR` instance, NQD candidate instance, architecture-description instance, or corpus-adequacy instance uses the same method only after the declared object kind and object-under-improvement evaluation are named. `E.23` does not turn those differences into holon levels, maturity ladders, or a decision-composition algebra.

The parameter pair is simple: name the object version under improvement, then name the evaluation that supplies the values for that object. Examples:

- a physical product, engineering design, policy text, method description, safety-case argument, or other domain object under improvement uses a declared object-under-improvement evaluation `CharacteristicSpace`, Q-Bundle, rubric, review profile, or assurance-adjacent evaluation pattern that supplies those values;
- an FPF pattern version uses `E.21`;
- a `DRR` version uses `E.9.DA`;
- an FPF-corpus or whole-FPF Pillar-adequacy object under improvement uses `E.2.DA`;
- a durable naming object under improvement uses `F.18`;
- an engineering quality-family object under improvement may use `C.25` as the Q-Bundle endpoint;
- an NQD/OEE object under improvement uses the declared `Q` side or the governing OEE/NQD neighbour.

If no adequate object-under-improvement evaluation exists for the object under improvement, `A.19.ECS` is opened before `E.23`. `A.19.ECS` constructs or repairs the object-under-improvement evaluation `CharacteristicSpace`: object kind, declared use, contrast cases, coordinate set, scales, value meanings, evidence and missingness rules, protected trade-offs, status meanings, and stop or reopen condition. `E.23` starts only after that evaluation is recoverable enough to re-read a changed object version.

For NQD/OEE use, the object-under-improvement evaluation can be the declared `Q` side of `C.18` or a governing OEE/NQD neighbour. `E.23` then asks whether object changes produce expected `Q` movement relative to the current comparison set, external candidate set, current non-dominated front, competing candidate set, accepted `SoTA` line, or selected set named by that object-under-improvement evaluation. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` still govern candidate characteristics, novelty and diversity treatment, descriptor and distance definitions, archive and front semantics, pool policy, selected-set publication, parity, and refresh.

`E.23` does not define the coordinates, floors, values, dominance rules, or measuring instruments. If no object-under-improvement evaluation is declared, the loop cannot start as a quality-improvement loop. First repair the question through `E.22`, repair overloaded quality wording through `C.16.Q`, construct or repair the object-under-improvement evaluation `CharacteristicSpace` through `A.19.ECS`, or select an existing exact object-under-improvement evaluation.

#### E.23:4.3 - Work order for using this pattern

For one quality-improvement loop:

1. Declare the object version under improvement and object-under-improvement evaluation; if no adequate object-under-improvement evaluation exists, use `A.19.ECS` before opening this loop.
2. Declare the improvement aim, floor, protected trade-offs, and first stop condition.
3. Frame the first quality review through `E.22`.
4. Run the object-under-improvement evaluation and produce row-atomic findings when work is returned.
5. Apply repairs or variants to the object under improvement, or hand proposal generation and selection to an exact neighbour, without silently damaging protected trade-offs.
6. Record row discharge as changed-object evidence, not as the quality value.
7. Re-read the changed object version through the object-under-improvement evaluation rather than accepting repair self-assessment. When `Q`-side NQD comparison is live, read the changed object version against the declared comparison set or front named in the loop record.
8. Record what got worse, including reader cost, authoring cost, maintainer cost, neighbour-pattern cost, source-loss risk, corpus-ecology cost, supervision cost, or rework cost when those can change admissible use.
9. Decide `stop`, `narrow`, `continue`, `switchMethodFamily`, or `holdForExactInformation`.
10. Leave one `QualityImprovementLoopRecord` that lets a later reader recover the object version under improvement, object-under-improvement evaluation, applied rows, re-read result, changed trade-offs, cost and risk account, and stop decision without reconstructing chat memory.

If the next pass has no live findings, feasible non-dominated improvement, required trade-off inspection, or unresolved open question under the declared object-under-improvement evaluation, stop or narrow. Do not continue merely because more attempts are possible.

An all-`5` or all-exceptional claim requires an explicit object-under-improvement evaluation coordinate-value table over the changed object version. It cannot be inferred from a floor-pass capsule, clean discharge table, external-review absorption pass, landing, popularity, adoption, or absence of blockers.

An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result is a local stop condition, not a permanent maturity end. It closes this loop only under the named object version under improvement, object-under-improvement evaluation, declared `Q` components, externally declared comparison set or current front, protected trade-offs, and cost boundary. Development can reopen when a new use, comparison set, front, archive, `Q` component, source, `SoTA` line, affordability boundary, or higher-payoff proposal changes the object-under-improvement evaluation. Do not encode the stop as a maturity level or as proof that further improvement is impossible.

When the object-under-improvement evaluation uses an ordinal scale, the declared floor is the local viable-for-use threshold under the named use claim; it is not always the same ordinal value. The object-under-improvement evaluation supplies the floor rules for that evaluation. A highest value means exceptional expression for the declared use and can serve as current-front reach or front improvement for this loop only when the object-under-improvement evaluation names the comparison basis: accepted `SoTA`, competing candidates, prior front members, current practice, or another explicit declared use frontier. It is not an upper bound on future development and not self-assigned praise.

For source-bearing improvement work, accepted `SoTA` is treated as the working external front: it shows what currently works for the improvement question at the time of the read. `SoTA` is assigned from outside the loop by the object-under-improvement evaluation, by an accepted use of a cited source plus a source adoption/adaptation/rejection decision, or by a declared comparison set. `E.23` can govern a loop that reaches that front, holds the object under improvement near that front as sources change, or tests a front-improving proposal, but it does not assign `SoTA` to itself or to the object under improvement.

Source-bearing improvement is compositional. PDSA or PDCA, POOGI, OODA, Ralph-like loops, SkillOpt-like fixed-performer optimization, MCDA, Goodhart, and NQD/OEE lines are not a citation shelf. Each line contributes one operation family, boundary, value semantic, stop discipline, or comparison discipline. A conforming loop keeps those contribution strata distinguishable enough that an object-under-improvement evaluation read can recover which contribution caused which useful movement and which neighbouring pattern still governs each boundary.

The entry vocabulary may say all `5`s, exceptional, `SoTA`, Pareto front, NQD `Q` movement, proposal portfolio, or shortlist. `E.23` accepts that vocabulary only after `E.22` or the object-under-improvement evaluation has named the governing pattern. In this pattern the shared operational question is simple: which object version under improvement is being changed, which externally declared comparison or value space reads the change, what movement is expected, what trade-off must not worsen, and what local stop or neighbour exit follows?

#### E.23:4.4 - Method-family selection

The generalization is not another named loop. It is a typed improvement method over one declared object under improvement, one exact version, and one declared object-under-improvement evaluation. Improvement is multi-characteristic optimization by changing the object under improvement and accepting only non-dominated gains or explicitly justified trade-offs under the object-under-improvement evaluation.

| Method family | Characteristic-space fit | Boundary |
|---|---|---|
| `PDSAorPDCAFamily` | Learning quality, measurement-backed comparison, stable baseline, standardize-or-repeat action. | Use when the object-under-improvement evaluation has declared measuring instruments or comparable read coordinates; do not reduce improvement to completing four labels. |
| `POOGIFamily` | Throughput, constraint selection for work, system throughput relation, inertia after a constraint shifts. | Use when the quality problem is actually throughput-shaped or constraint-shaped; do not force TOC constraint language onto every object under improvement. |
| `OODAFamily` | Orientation, feedback, decision under uncertainty, changing external situation. | Use when orientation quality and feedback materially change the object read; do not count speed or action cadence as quality. |
| `RalphLikeGeneralAdaptiveFamily` | Broadly capable agent repeatedly works from specification, failure feedback, memory, and verification. | Use only under `C.19.1` cost and risk discipline, supervision boundary where needed, object-under-improvement evaluation re-read, and stop or switch conditions. |
| `FixedPerformerObjectVersionUnderImprovementOptimizationFamily` | Performer, harness, or execution environment stays fixed while a mutable object version under improvement is improved through bounded edits and object-under-improvement evaluation re-read. | Use when the loop changes the object under improvement rather than the performer. If the live work changes candidate generation, archive or front semantics, live pool policy, selected-set publication, parity, or refresh, hand off to `C.18`, `C.19`, `G.5`, `G.9`, or `G.11`. |
| `NQDQualitySideImprovementFamily` | The object-under-improvement evaluation supplies the `Q` side for a declared NQD/OEE comparison, and loop changes seek non-dominated `Q` movement for one candidate, object version under improvement, or declared transduction result. | Use only with declared `Q` components, external comparison basis, comparison set or current front, protected trade-offs, and neighbour exits. A front-improving proposal must name the externally assigned front and the declared result or capability it is expected to improve. `E.23` does not govern novelty, diversity, descriptors, distances, archive or front insertion, pool policy, selected-set publication, parity, or refresh. |
| `SoTAReachAndMaintainFamily` | Several accepted source or practice lines must be composed so the object under improvement reaches or maintains an externally assigned `SoTA` front rather than citing those lines separately. | Use only when each source line has an assigned contribution, contribution strata are distinguishable, the `SourceComposedResultClaim` is named, the object-under-improvement evaluation can read the claimed movement, and protected trade-offs are checked. |
| `SpecializedObjectFamilyCycle` | A narrower method family optimized for one declared characteristic space such as throughput and constraint, variation and defect, learning and stabilization, or orientation quality. | Use when the object-under-improvement evaluation declares that space and the specialization is BLP-compatible; durable adaptation claims are assigned to `C.22.1`. |

Specialized cycles and general adaptive loops are alternatives under the same object-under-improvement evaluation discipline. A specialized cycle is not automatically better because it is familiar. A general adaptive loop is not automatically better because it is scalable or automated.

#### E.23:4.5 - Operation-family activation rule

An operation family is selected for a concrete loop only when the loop record names all of the following:

1. the object-under-improvement evaluation coordinate, quality value, or stop meaning expected to improve;
2. the failure mode the operation addresses;
3. the cost or risk reason for adding the operation;
4. the protected trade-offs it must not damage;
5. the stop or removal condition if the operation does not move the object-under-improvement evaluation.

If those fields are absent, the operation family stays unselected for that loop. It may remain a rationale or example, but it must not become required apparatus.

| Operation family | Use when | Boundary |
|---|---|---|
| `SpecificationArticulation` | The object under improvement is not clear enough for repeated attempts. | `E.22` frames the improvement-oriented quality read; `E.9` and the exact pattern for the object under improvement name the decision or specification content when live. |
| `TaskDecomposition` | A large object under improvement would otherwise produce blind retries. | Use only when the object-under-improvement evaluation can preserve protected trade-offs across the split. |
| `ContextRefreshWithCarryForwardEvidence` | A fresh context is useful but previous pass evidence must not be lost. | Carried-forward evidence is material for the next pass, not a quality value by itself. |
| `FailureContextRetry` | A failed attempt contains useful error, tool, reviewer, or object-version-under-improvement feedback. | Retrying is inadmissible when the failure shows wrong object under improvement, wrong evaluation, or missing authority. |
| `VerificationAgainstSpecification` | Passing local checks could diverge from the intended result. | `E.22` and the object-under-improvement evaluation decide whether the result meets the declared aim. |
| `MemoryOrDistillation` | Previous failures or local lessons would otherwise be rediscovered repeatedly. | Durable specialization claims go to `C.22.1`; selected-set publication or parity claims go to `G.5` or `G.9` when live. |
| `ExternalCriticOrMetacognitiveCoRegulation` | Fixation, underexploration, or high-cost mistakes are live risks. | Opens only when added supervision cost is justified by `C.19.1` cost and risk comparison and the object-under-improvement evaluation can use the feedback. |
| `ImprovementProposalPortfolioUse` | One `E.22` read returns several candidate improvement proposals, and the loop must decide how to apply, split, reject, or hand off them. | `E.23` can govern object-version-under-improvement changes and re-reads; NQD generation, front or archive handling, selected-set publication, parity, and refresh stay with `C.18`, `C.19`, `G.5`, `G.9`, and `G.11`. |
| `SearchBreadthVariantsOrTreeSearch` | Several candidate changes may matter and one linear retry path is too narrow. | Option generation and pool policy stay outside `E.23`; `C.11`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` govern choice, generation, exploration policy, selected-set publication, parity, and refresh when live. |
| `BoundedObjectChangeBudget` | Too many object edits can hide which change moved the object-under-improvement evaluation. | State the permitted edit scope, protected trade-offs, and re-read boundary before applying changes. |
| `HeldOutObjectUnderImprovementEvaluationRead` | The loop could overfit to the same visible read. | Use a held-out or more demanding object-under-improvement evaluation read only when the object-under-improvement evaluation defines that demanding relation; do not invent a second score. |
| `RejectedChangeMemory` | Rejected proposals would otherwise be retried. | Record rejection reason as loop memory; do not treat it as archive, selected-set publication, or source evidence. |
| `OptimizerMemorySeparation` | Local optimizer notes or prompt memories could leak into the changed object version or quality value. | Keep optimizer memory, loop record, changed object version, and object-under-improvement evaluation result distinct. |
| `SourceLineContributionAssignment` | Several accepted `SoTA` or practice lines are being composed into one improvement. | State the contribution of each line as operation family, boundary, comparison discipline, failure mode, protected trade-off, or value semantics; keep contribution strata distinct enough that source names cannot stand in for the source-composed result claim. |
| `AgentToolInterfaceHardening` | Tool-using agent action, observation, and verification need reliability. | `C.24` governs call planning, budgets, stop or replan conditions, and checkpoint returns. |
| `TaskFamilyAdaptationSignature` | A loop claims acquisition of reusable specialization for a task family. | `C.22.1` records threshold target, time-to-threshold, budget-to-threshold, prior exposure, transfer, retention, downside, and corridor-entry fields. |

#### E.23:4.6 - BLP and accepted-work cost

`C.19.1` governs the preference for general, scale-amenable methods when safety and legality are comparable. `E.23` does not replace that preference.

A Ralph-like loop is accepted here only as a current external example of a general adaptive agentic method shape: one broadly capable agent repeatedly works from a specification, receives feedback from the changed object version under improvement, declared transduction result, or tool feedback channel, and starts subsequent attempts with refreshed context or carried state. `E.23` does not import the Ralph name, the infinite-loop idiom, or coding-tool scope as method law.

The local cost and risk prompt is:

```text
AcceptedWorkCost ~= token_or_compute_cost + tool_cost + adaptation_attempt_cost + human_supervision_cost + rework_cost - avoided_loss_value
```

This expression is not a hidden scalar quality score. If avoided loss is large, an expensive loop can be right. If the object under improvement is simple, a cheaper model, human edit, small direct repair, specialized cycle, or one-shot review can be better. If the loop keeps burning attempts without object-under-improvement evaluation movement, BLP does not protect it.

Harness improvement is usually the preferred first improvement move when it can reduce blind trial-and-error: better prompts, better object-under-improvement evaluation frames, better row shapes, better test cases, better exact source references, better local tooling, better memory or distillation, better verification, and better stop conditions. This follows `C.19.1` when the improved harness makes the general method more scale-amenable rather than adding a narrow patch that must be re-tuned for every object under improvement.

#### E.23:4.7 - Re-read, trade-offs, and stopping

Row-atomic absorption changes the object under improvement. It is not coordinate improvement until the object-under-improvement evaluation re-reads the changed object version.

The re-read names:

1. object version under improvement before and after the change;
2. object-under-improvement evaluation;
3. active coordinates, statuses, or declared values affected;
4. findings applied, already satisfied, rejected, or assigned outside the object-under-improvement evaluation;
5. expected and observed quality movement;
6. protected trade-offs that worsened or stayed intact;
7. remaining blockers, feasible non-dominated improvements, or bounded non-use;
8. stop, narrow, continue, switch, or hold decision.

Use `continue` only when another pass has a recoverable expected object-under-improvement evaluation movement. Use `switchMethodFamily` when the current method family is not moving the object under improvement, has become too costly, or no longer fits the characteristic space. Use `holdForExactInformation` when the object under improvement, evaluation, authority, evidence, or source condition is too under-specified for the next pass to be meaningful.

A loop record is sufficient when it lets the next reader tell what changed, what the object-under-improvement evaluation read after the change, what became worse, what remains bounded non-use, and why the chosen stop, narrow, continue, switch, or hold decision follows. A record that lists applied findings without the object-under-improvement evaluation re-read is row-discharge evidence, not quality-improvement closure.

#### E.23:4.8 - Non-use boundaries

A quality-improvement-loop result is not project evidence, assurance, gate passage, release approval, safety acceptance, compliance evidence, or work authority unless the exact neighbouring FPF pattern is opened for that claim.

Repeated agentic attempts are not BLP-compatible merely because they are automated. They need declared object under improvement, object-under-improvement evaluation, protected trade-offs, bounded cost and risk account, and stop or switch conditions.

External review, landing, monolith placement, praise, popularity, adoption, or absence of blockers does not raise quality values by itself. Such signals may point to content evidence only after the object-under-improvement evaluation says how they matter.

`E.23` must not force full-loop apparatus on cheap local edits. A clean floor read may close through `E.22` plus the object-under-improvement evaluation without opening this method.

