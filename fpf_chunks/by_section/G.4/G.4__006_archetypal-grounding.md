---
chunk_kind: "child"
pattern_id: "G.4"
pattern_title: "CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
section_id: "G.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/G.4/G.4__006_archetypal-grounding.md"
commit_sha: "e400eab3757d60a8d05196046bed002dff1839e0"
heading_path:
  - "G.4 — CAL Authoring for a CG-Frame: Operators, Acceptance Clauses, Evidence Wiring"
  - "G.4:5 — Archetypal Grounding"
line_start: 102465
line_end: 102499
dependencies:
  - "A.10"
  - "A.13"
  - "A.15.1"
  - "A.18"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.2.1"
  - "C.23"
  - "E.17"
  - "E.18"
  - "E.8"
  - "F.17"
  - "F.6"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.2"
  - "G.3"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.8"
  - "G.9"
  - "G.Core"
  - "U.ClaimScope"
keywords:
  - "CAL Pack@CG-Frame"
  - "Context charter"
  - "acceptance clause"
  - "legal flow"
  - "pass \\"
  - "typed operator card"
---

### G.4:5 - Archetypal Grounding

**Tell.** A CG‑Frame must choose and justify a set of candidate methods (possibly a selected set or archive) under explicit legality, evidence, and scope constraints. CHR provides the typed measurement basis; CAL declares auditable predicates and flows that separately grounded runtime work may apply.

**Show 1 (bounded CAL pack skeleton).**
Use: R&D selected-set choice. The pack names the exact CG frame and EntityOfConcern, candidate-set `ClaimScope`, ReferencePlane, and evaluation window. CHR defines `SafetyClass(ord↑)`, `CostUSD_2026(ratio↓)`, `Readiness(nominal)`.

* `CAL.Operator: DominatesPareto`
  Signature over CHR types, precondition references CHR guard macros.
* `CAL.AcceptanceClause: AC_SafetyGate`
  Reusable typed predicate for `SafetyClass` (and its levels), citing `SafetyResultArgument-D1`, the A.6.1 argument declaration that admits a C.16 measurement-result episteme for that Characteristic. Thresholds are valid for the stated `ClaimScope` and evaluation window; unknown handling uses tri-state pins. The clause names no current measurement-result episteme.
* `CAL.Flow: Flow_ParetoPortfolio`
  Produces a selected-set result kind; gates by `AC_SafetyGate` and `AC_Budget`.
* `CAL.EvidenceProfile: EP_SafetyEvidence`
  Declares anchor ids and freshness policy pins required for `SCR`.

When this CAL pack supplies selector gates, it publishes `TaskMapRef=<SafetySelectionMap, E3>`. That map cites `CALCharterRef=<SafetyCALCharter, E2>`, C.22 `TaskSignatureRef=SafetyPortfolioTaskSignature-E4`, the exact task, and edition-bearing refs `AC_SafetyGate-E2`, `Flow_ParetoPortfolio-E1`, `DominatesPareto-E3`, and `EP_SafetyEvidence-E4`; it contains no threshold values. Downstream G.5 consumes the exact TaskSignatureRef and this TaskMapRef together, verifies that the map cites the same signature, and resolves the charter and declarations through their refs. If the charter or a cited clause changes, G.4 publishes another TaskMap edition; selectors that still cite `<SafetySelectionMap, E3>` continue to replay the old boundary.

**Show 2 (explicit cross-sense or ReferencePlane import).**
A `SafetyClass` result uses an expression with a different F.17 source-local meaning or comes from another ReferencePlane. CAL may author a clause using it only after the exact F.17 cells and obtaining F.9 relation are cited when meanings differ, and the applicable plane or edition crossing records are cited when those values differ. The clause keeps its declared `ClaimScope` and window; the import does not silently widen either.

**Show 3 (one performed acceptance evaluation).**

Before the candidate action is admitted as Work, A.13 recovers `SafetyEvaluatorSystem-17 : U.System` for exact action `SafetyAcceptanceEvaluationAction-17`. Its admitted `SafetyEvaluatorBoundary-17` contains the evaluation controller, its active decision state, and the input/output channels through which it applies the clause; it excludes the CAL declarations, measurement-result episteme, candidate, assignment, and containing team System. The action's scope is `SafetyAcceptanceClaimScope-17`, its working situation is `SafetyGateEvaluationSituation-17`, and its window is `2026-07-30T09:00:00Z` through `2026-07-30T09:20:00Z`. It is directed by `SafetyAcceptanceDecisionNorm-17`: apply the current clause to admissible current inputs, return `unknown` rather than force a threshold verdict when uncertainty crosses the boundary, and reject an input whose declared result shape is incompatible. The relevant conditions are clause edition, result-shape admissibility, measurement currentness, and uncertainty relative to the threshold.

The local kind `SafetyAcceptanceEvaluatorSystemRole` is declared under A.2. Its membership criterion requires the stable work-facing contribution of safety-acceptance evaluation and goal-directed, condition-sensitive regulation under `SafetyAcceptanceDecisionNorm-17`: the holder must bind admissible inputs, choose the clause-defined verdict, and abstain or return `unknown` when the declared conditions require it. `SafetyEvaluatorDecisionTrace-17` shows `SafetyEvaluatorSystem-17` rejecting an incompatible result shape and returning `unknown` when the admissible uncertainty interval crosses the threshold; the system-boundary and runtime records show that those actions occurred within `SafetyEvaluatorBoundary-17`. A.10 evidence-use claims support the criterion facts, and the case independently classifies `SafetyEvaluatorSystem-17` under `SafetyAcceptanceEvaluatorSystemRole`. Neither the candidate Work nor the assignment supplies that classification. No Grade, autonomy result, characteristic profile, or stronger assurance claim is consumed here.

The same A.13 core uses `SafetyAcceptanceEvaluationAssignment`, a directly declared `U.SystemRoleAssignment` species under A.2.1. The species defines holder, assigned-kind, and evaluation-candidate participant meanings; its predicate appoints the holder to evaluate that candidate under the applicable clause for the stated scope, situation, and window. `SafetyAcceptanceEvaluationAssignment-17` obtains with `SafetyEvaluatorSystem-17` as holder, `SafetyAcceptanceEvaluatorSystemRole` as assigned-kind value, and `C-17` as evaluation candidate. Its maximal uninterrupted predicate-true interval covers the full stated window.

Only after that A.13 core is established does A.15.1 independently admit `EvalWork-2026-07-30-17 : U.Work` from its exact performance history, enacted `SafetyAcceptanceMethod`, temporal extent, and obtaining containing-System relation to independently admitted `SafetyEvaluationTeamSystem-17`. The actual A.6.1 application `SafetyAcceptanceApplication-17` separately binds candidate `C-17` and current C.16 measurement-result episteme `SafetyMeasureResult-E17` to `SafetyResultArgument-D1` while using unchanged reusable clause `AC_SafetyGate`. Neither the assignment nor an F.6 conclusion is an A.15.1 admission premise.

Because this worked case explicitly says that the Work was performed under an assignment, F.6 afterward establishes `performedUnderAssignment(EvalWork-2026-07-30-17, SafetyAcceptanceEvaluationAssignment-17)` through the same obtaining A.13 assignment. The direct case fact links that exact pair, holder equality holds, and the assignment interval covers the Work. A different overlapping assignment held by the same performer would not establish this attribution.

`SafetyMeasureResult-E17` states the measured safety characteristic, scale, attributed value, uncertainty, model, calibration, and measurement Work; it is neither the raw detector output nor the acceptance verdict. The clause application obtains `unknown` because the uncertainty interval crosses the threshold. A later `SafetyMeasureResult-E18` can bind through separately identified `SafetyAcceptanceApplication-18` while `AC_SafetyGate` remains unchanged. A C.16 result for `CostUSD_2026`, a result with an incompatible declared shape, or raw detector output fails `SafetyResultArgument-D1` before the predicate runs; it does not cause a new reusable clause edition. A separate C.2.1 episteme asserts that exact verdict and cites its provenance under A.10 and, when the EvidenceGraph extension is present, G.6; G.11 supplies currentness. A later C.11 result may record `defer`, and its claim uses the verdict episteme through an exact premise or decision-use relation. Any decision-making Work remains separate. The clause card, proof-ledger row, evidence edge, and decision record do not retroactively establish the measurement Work or the evaluation occurrence.

