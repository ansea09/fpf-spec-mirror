---
chunk_kind: "child"
pattern_id: "C.17"
pattern_title: "Characterising Generative Novelty and Value"
section_id: "C.17:9"
section_title: "Worked cases"
source_path: "FPF-Spec.md"
output_path: "by_section/C.17/C.17__011_worked-cases.md"
commit_sha: "d325a051ac7b2bb37cd870f90b4ed8b2d0426e58"
heading_path:
  - "C.17 — Characterising Generative Novelty and Value"
  - "C.17:9 — Worked cases"
line_start: 63457
line_end: 63496
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.3.1"
  - "A.3.2"
  - "B.3"
  - "B.4"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "E.10.LRN"
  - "F.18"
  - "F.6"
  - "F.9"
  - "G.11"
  - "G.5"
keywords:
  - "ConstraintFit"
  - "Novelty"
  - "Use-Value"
  - "bounded quantitative result"
  - "evidence"
  - "incomparability"
  - "named comparison basis"
  - "qualitative-first evaluation"
  - "uncertainty"
---

### C.17:9 - Worked cases

#### C.17:9.1 - Pump design: stop early or open the measurement branch

Identify `P-22` as the exact design episteme. Compared with the admitted five-year pump-design set, its inspected split-clamp arrangement is a supported difference. Assembly evidence supports shorter assembly than the current shop design P-11, and the candidate must not require new tooling. The cited comparison uses the same assembly task and conditions. State what was inspected and the limit of that support. A second shop asking the same question can use the supported conclusion when its assembly conditions and comparison basis match.

To use Novelty value `0.42`, cite `P22-NoveltyResult-4`, an already constituted C.16 measurement-result episteme. Its chain identifies P-22 as the measurement subject, the Novelty Characteristic and Scale, exact similarity Method, the calibrated `[0,1]` CAD-graph similarity result used by the declared Novelty construction, encoder and model edition, uncertainty, dated measurement Work, actual bindings, time, and evidence. The Method compares `P22-CADGraph-7`, produced from and representing P-22 under `CADGraphProjection-2`, with graphs produced by the same projection for every corpus design; the result states that this projection omits surface finish and manufacturing tolerances. If the current action measures novelty, constitute that chain first. To resolve the tooling requirement, compare the proposed operations with the available tooling and record what that comparison establishes. It remains open while only the requirement is known.

A `CreativityEvaluationResult` can now report the supported difference and the assembly comparison with P-11. To establish eligibility, check each applicable must-condition. To place P-22 on a non-dominated front, use the declared comparison over eligible rivals (§7). The two results about P-22 alone leave its front membership open.

If an audit later asserts that an overall assessment occurred, identify the evaluator System, its exact assignment, `PumpCreativityAssessment-17` Work, and `PumpCreativityAssessmentMethod-2`; state that the Work enacts the Method. The MethodDescription explains the Method, the result states claims, and coordinate-measurement Work stays separate. Do not add an A.6.1 operation application merely because those values are recorded. If the audit separately asserts an exact operation application or binding, satisfy the current A.6.1 application account and cite that application.

#### C.17:9.2 - Software and algorithmic design

**Software design.** In this worked example, `ETL-Parallel-12` is compared with 40 admitted internal pipeline designs through `ASTGraphSimilarity-3`, whose declared Novelty construction uses calibrated `[0,1]` similarities. The Method compares AST-graph representations produced by the same declared parser and projection for the evaluated design and every corpus design; the result states that runtime configuration and deployment topology are not preserved by that projection. Its Novelty result is `0.36`.

A fixed-workload benchmark reports an 18% lower p95 latency than the serial baseline, but the segregation-of-duties test fails. The benchmark run, corpus edition, nearest-neighbour report, and policy test are the evidence.

The result therefore supports a latency gain but leaves the design ineligible for the stated use; if the candidate is revised for that use, repair the isolation boundary and repeat the affected tests before claiming that the revised design meets this constraint.

**Algorithmic search Work.** `SpikeSet-7` contains nine dated attempts in three declared approach classes over six hours. Tagged Work records support `DiversityOfSearch = 3 classes`; the first runnable output appeared after 2 h 10 m. The held-out viability test was never run, so `Time-to-First-Viable` is not established. Run the test when the receiving work needs the viability result. The supported search-diversity reading remains available; time-to-first-runnable cannot substitute for time-to-first-viable.

#### C.17:9.3 - Health analytics

For `Cardio-Readmit-H4`, the held-out AUROC is `0.79` against a `0.75` baseline under the frozen test set, clearing the declared uplift threshold of `0.03`. The model card, held-out plot, and evaluation Work support that local Use-Value result. No receiving-use pilot has yet been performed at Hospital B, so Transferability there remains unsupported. Use the local result for the applicable pool or choice question, but leave the target-hospital claim open until pilot evidence exists. Use an F.9 Bridge only if the two hospitals' reference schemes require one.

#### C.17:9.4 - Product reframing

`OnboardingFrame-v1` treats onboarding as one completion task; `OnboardingFrame-v2` separates job setup from obtaining the first result. The declared ReframeDelta rule returns `BoundaryShift`, supported by the frame diff and a simpler causal map. Suppose a four-week A/B trial assigns users at random to the existing one-task procedure or to a revised procedure with separate job setup and first-result activities. The revised group’s median time-to-value was 22% lower on the same outcome definition, clearing the 20% objective for this trial. The frame comparison establishes what changed in the model. The trial evaluates the procedures the groups used. Exploratory Work used 9 of the 12 allowed staff-days, so the realized risk-budget ratio is `0.75` with no overrun. The frame diff, A/B report, WorkPlan, and Work records support the result. This evidence can inform the later choice; it does not make the choice.

#### C.17:9.5 - Scientific and policy proposals

**Scientific proposal.** `ScalingRelation-S4` has Novelty `0.61` from the declared calibrated `[0,1]` similarity construction relative to the admitted literature corpus. The Novelty Method compares one text embedding that describes the proposal with embeddings produced by the same encoder for every corpus paper; the result names that projection and states that notation and experimental detail may be lost.

Its Surprise is `4.1 bits per token` under `PriorModel-2`, using the same versioned tokenizer and abstract-text sample unit for the proposal and model basis; the per-token normalization handles text length but does not support a claim about equations or full papers.

The corpus, neighbour report, model calibration and derivation evidence support those bounded coordinates. Independent replication is missing; any later empirical-use claim that requires it remains unsupported. Report the available coordinates now and obtain the required replication before making that dependent reliance claim.

**Policy proposal.** In a municipal permit-triage pilot, `Policy-P8` reduces median processing time by 12% against the prior-procedure baseline and passes the declared legal-form test. Subgroup error evidence required by the equity must-criterion is missing, so ConstraintFit and eligibility are not established. Keep the proposal out of an approval-facing comparison until the subgroup test is complete; the time result remains usable for its narrower operational question.

