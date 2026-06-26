---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__005_solution.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:4 — Solution"
line_start: 77976
line_end: 78071
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.19.1"
  - "C.22.1"
  - "C.24"
  - "C.32.P2S"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.9.DA"
  - "F.19"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:4 - Solution

`E.23` is the general method for repeated improvement of an object version under an object-under-improvement evaluation named by value. It changes the object, re-evaluates the changed version using that evaluation's required evidence basis and result-row shape, checks trade-offs and cost, and decides whether to stop, continue, switch method family, open a new frame, or hold for exact information.

#### E.23:4.1 - Local names and kind settlement

| Local name | Kind and function |
|---|---|
| `QualityImprovementLoopMethod` | Repeated improvement method for one object version under one evaluation. |
| `ObjectUnderImprovementRef` | Exact object kind and version being changed. |
| `ObjectUnderImprovementEvaluationRef` | Exact evaluation pattern, characteristic space, Q-Bundle, rubric, or review profile that supplies values. |
| `LoopEvaluationEvidenceBasis` | Evidence loci checked or named for the current loop evaluation result, including missing loci that lower values. |
| `LoopEvaluationResultForm` | Result-row shape required by the object-under-improvement evaluation for the current pass. |
| `ImprovementAim` | Desired movement: floor repair, optional exceptional improvement, trade-off inspection, absorption impact, open-question discovery, source-front reach, or another exact aim. It names desired quality movement, not a value that the repair must prove. |
| `MethodFamilySelection` | Selected method family for the current object and evaluation. |
| `OperationFamilySelectionSet` | Optional operation families selected because they can move the evaluation enough to justify cost. |
| `ObjectUnderImprovementReEvaluation` | Re-run or cited result of the evaluation on the changed object version. |
| `CostAndRiskAccount` | Cost and risk account used to judge another pass or operation. |
| `StopContinueSwitchFrameHoldDecision` | Local loop decision after re-evaluation. |
| `QualityImprovementLoopRecord` | Record of object versions, applied rows, re-evaluation, trade-offs, cost/risk, and loop decision. |
| `QualitySideMovementClaim` | Local claim that a changed object moved on declared `Q` components under NQD/OEE comparison. |
| `SourceComposedResultClaim` | Result produced by composing accepted source or practice lines and readable by the evaluation. |
| `KindRestorationCheck` | Required precision-repair check that records pre-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope, proposed post-repair kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope, and whether each live field is not triggered, ordinary prose, preserved, split, intentionally changed by accepted decision, or blocking. |

These names belong to loop method. They do not create quality values, project evidence, release state, selected-set publication, parity, refresh, or proof of quality.

#### E.23:4.2 - Loop method

For one quality-improvement loop:

1. Declare `ObjectUnderImprovementRef`, object version, and `ObjectUnderImprovementEvaluationRef`.
2. Declare `ImprovementAim`, declared floor or desired substantive quality movement, protected trade-offs, cost and risk account, and local stop condition. Do not declare `5`, all-`5`, or `5-defensible` as the work target; name the content property to improve instead.
3. Use `E.22` to frame the first quality evaluation when the purpose is not already explicit.
4. Run the object-under-improvement evaluation in its required result form. For one FPF pattern version, this is an `E.21` result with every required coordinate, every `ShortRationale`, the `PrecisionRestorationProfile`, evidence basis, coordinate-specific payloads, and status. A loop record, profile pass, blocker summary, two-column table, or "no blockers" note is not a substitute.
5. Record row-atomic findings or proposal rows when work is returned. A step is closed only after its finding or proposal row is written; do not rely on memory or a later grouped summary.
6. Apply repairs or variants to the object. Repair below-floor findings first. When exceptional improvement is requested, search coordinate-by-coordinate for substantive content moves: better positive action guidance, a missing worked slice, case/countercase coverage, source-currentness carry-through, mature-content discharge, relation cleanup, deletion of displaced apparatus, split of overloaded content, or relocation of quality/process proof. Repairs must not add guards, boundary catalogues, relation menus, or quality proof solely to make a higher value defensible. A no-change closure is admissible only when the row gives loci and explains why no non-dominated content improvement is available under the protected trade-offs. When generation, selection, publication, parity, refresh, decision, planning, work, evidence, or assurance claims leave quality improvement, keep the pattern that governs that claim, relation, or boundary in the loop record or `Relations`. Do not let loop-method prose replace the object's positive content. For precision-restoration defects, use the selected restoration or governing pattern named by the evaluation: `E.10`, `E.10.ARCH`, `F.18`, `F.19`, or an object-specific pattern. Also record a bounded complete `KindRestorationCheck` before closing the finding: the repair must say what kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope were present before the edit and what kind, relation, current ontic slot, relation position, use relation, or claim kind, admissible use, and scope the changed text now carries when those items are live. No-op closure is admissible only as `not triggered`, `ordinary prose`, or `already satisfied` with loci; otherwise unchanged text remains a live finding. When another pattern governs the kind under repair, relation, claim, or position, cite that pattern; `E.23` records the repair and reruns the evaluation, it does not duplicate the restoration algorithm.
7. Re-evaluate the changed object version through the object-under-improvement evaluation, using that evaluation's required coordinate set, evidence basis, result-row shape, short rationales, mandatory attention-discharge rows, and coordinate-specific payloads.
8. Record what improved, what stayed floor-only, what was unchanged by value with loci, what became worse, and which rows moved outside the evaluation.
9. Decide `stop`, `continue`, `switchMethodFamily`, `openNewFrame`, or `holdForExactInformation`.
10. Leave a `QualityImprovementLoopRecord` sufficient for the next reader to replay the object versions, evidence basis, evaluation result, trade-offs, cost/risk, and loop decision.

#### E.23:4.3 - Stop, continue, and reopen

Stop when the current object version meets the declared floor or improvement aim and no feasible non-dominated proposal remains worth its cost under the current use, comparison set, source state, and protected trade-offs. If the remaining proposal mainly makes a value easier to argue while adding apparatus or worsening use, affordability, locality, source preservation, or ecology, reject that proposal; continue searching for a substantive content move if the improvement aim is still open, and stop only with a by-value no-proposal disposition.

Continue only when the next pass has an expected evaluation movement and acceptable cost/risk. Switch method when the current method family is not moving the object, is too costly, or no longer fits the evaluation. Hold when object, evaluation, authority, evidence, source condition, or comparison set is too under-specified.

An all-`5`, all-exceptional, current-front-reaching, or current-front-improving result closes this loop locally. It does not say that future development is impossible. A new use, `Q` component, source line, `SoTA` front, comparison set, affordability boundary, or higher-payoff proposal can open a later loop.

#### E.23:4.4 - Method-family selection

| Method family | Use when |
|---|---|
| `PDSAorPDCAFamily` | Learning quality, baseline comparison, measuring instruments, or standardize/repeat action matter for the improvement loop. |
| `POOGIFamily` | The evaluation problem is throughput-shaped or constraint-shaped. |
| `OODAFamily` | Orientation quality and feedback under changing conditions affect the evaluation. |
| `RalphLikeGeneralAdaptiveFamily` | A broadly capable agent can improve the object through repeated specification, feedback, memory, and verification under `C.19.1` cost/risk discipline. |
| `FixedPerformerObjectVersionUnderImprovementOptimizationFamily` | The performer or harness stays fixed while the object version is edited and re-evaluated. |
| `NQDQualitySideImprovementFamily` | The evaluation supplies the `Q` side for a declared NQD/OEE comparison and loop changes seek non-dominated `Q` movement. |
| `SoTAReachAndMaintainFamily` | Several accepted source or practice lines must be composed to reach or maintain an externally assigned front. |
| `SpecializedObjectFamilyCycle` | A specialized method family fits a declared characteristic space and is BLP-compatible. |

The selected family is justified by characteristic-space fit, expected evaluation movement, cost/risk, and protected trade-offs. Familiarity, automation, or current popularity is not enough.

#### E.23:4.5 - Operation-family selection

An operation family is selected only when the loop record names:

1. expected movement under the object-under-improvement evaluation;
2. failure mode addressed;
3. cost or risk reason;
4. protected trade-offs;
5. stop or removal condition.

Typical operation families are specification articulation, task decomposition, context refresh with carry-forward evidence, failure-context retry, verification against specification, memory or distillation, external critic or co-regulation, proposal portfolio use, search breadth or variants, bounded object-change budget, held-out evaluation, rejected-change memory, optimizer-memory separation, source-line contribution assignment, agent-tool-interface hardening, and task-family adaptation signature. They remain selectable only for the loop that justifies them.

#### E.23:4.6 - Cost and BLP discipline

`C.19.1` governs the preference for broad, scale-amenable methods when safety, legality, and practical fitness are comparable. `E.23` uses that preference but still evaluates end-to-end accepted-work cost:

```text
AcceptedWorkCost ~= token_or_compute_cost + tool_cost + adaptation_attempt_cost + human_supervision_cost + rework_cost - avoided_loss_value
```

This is not a hidden quality score. It is a prompt for cost/risk reasoning. If avoided loss is large, an expensive loop can be right. If the object is simple, a human edit, small direct repair, lower-cost model, specialized cycle, or one-shot evaluation can be better.

Harness improvement is usually the first high-leverage move when it reduces blind retry: better frames, row shapes, test cases, source references, local tools, memory, verification, and stop conditions.

#### E.23:4.7 - Source-bearing and OEE/NQD improvement

Accepted `SoTA` is the working external front only when assigned by the object-under-improvement evaluation, accepted source-use decision, or declared comparison set. `E.23` can govern a loop that reaches, maintains, or improves relative to that front; it does not self-assign `SoTA`.

When several source lines are used, the loop records each line's contribution: value semantics, operation family, boundary, comparison discipline, failure mode, protected trade-off, or stop discipline. The changed object version then states the `SourceComposedResultClaim` and is re-evaluated.

For NQD/OEE, `E.23` can change one object version or candidate to improve declared `Q` movement. `C.17`, `C.18`, `C.19`, `G.5`, `G.9`, and `G.11` keep authority over novelty, diversity, descriptors, distances, archive/front insertion, pool policy, selected-set publication, parity, and refresh.

