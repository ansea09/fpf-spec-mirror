---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__002_problem-frame.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:1 — Problem frame"
line_start: 65438
line_end: 65518
dependencies:
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.19.CPM"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.25"
  - "C.32"
  - "C.32.ACS"
  - "C.32.HCS"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.13"
  - "E.22"
  - "E.23"
  - "G.5"
keywords:
  - "architecture-characteristic eval program"
  - "comparison input"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:1 - Problem frame

Use this pattern when an architecture team already has project architecture-characteristic rows and must evaluate the current architecture, compare candidate architectures, monitor evolution, or prepare a selection input.

Primary working reader: an architect or evaluator preparing readings over declared architecture-characteristic criteria without turning those readings into the criteria or the decision.

Typical entry phrases:

```text
"We have criteria rows; which eval reading shows how candidate A and candidate B compare under the same parity frame?"
"The monitor is useful, but is this a reading, a test failure, or a decision input?"
"Two methods, roles, system variants, or AI workflows need fair comparison against the same architecture characteristics."
```

**First-minute use slice.** A product-family team has ACS rows for substitutability, evidence reuse, and latency, plus safety as a monitored guardrail. Two candidate architectures look plausible. The practitioner writes one ACE program record with the same claim scope, selected context slices, reference scheme and plane, evaluation window, parity frame, and input projections for both candidates. `EvalService-7`, the admitted System holding `EvaluatorAssignment-3`, separately performs dated `CandidateEvalWork-42` over both candidates under that assignment; its exact Method enactment or operation application is separately governed. `CandidateLatencyReading-42` and `CandidateEvidenceScopeFinding-42` are separately governed typed results, and any observed protected-safety loss remains explicit rather than being absorbed into one score. Those results can become inputs for `A.19.CPM` comparison or the next C.32 synthesis pass; neither the program record, Work, nor a result defines the criterion or decides the architecture.

The primary governed object is one architecture-characteristic eval-program record over declared criteria rows, Q-Bundle slots, candidates, bearers, or selected structures under a parity frame. It is a C.32.ACE-local record form, not a new `U.*` kind and not, by its `program` label, a `U.Method`, `U.MethodDescription`, `U.WorkPlan`, dated `U.Work`, or evaluation result. Measurement validity, comparison policy, selection results, G.5 publications, and architecture decisions remain with their receiving patterns.

Ordinary working move: choose the declared criteria rows, bind the exact claim scope, relevant context slices, reference scheme and plane, evaluation window, and input projections, and hold one parity frame for all variants. When evaluation actually occurs, identify the admitted System and role assignment performing the dated Work plus any exact Method enactment or operation application, then return the separately governed typed results as feedback for comparison or the next synthesis pass.

The first useful output is an `ArchitectureCharacteristicEvalProgram@Project`. This C.32.ACE-local working record states how one bounded architecture evaluation is to be framed over declared criteria. When a reusable way of evaluating is current, identify that separate `U.Method` under A.3.1; when a claim-bearing episteme describes that exact Method, test the same episteme for `U.MethodDescription` under A.3.2. A planned evaluation belongs to A.15.2, an actual dated evaluation to A.15.1, and each result to its direct measurement, comparison, evaluation, or assertion owner. The record reads characteristics through rows, slots, candidates, or structures; it is not any of those neighboring objects:

For a first pass, fill the exact claim scope and selected context slices, reference scheme and plane, evaluation window and input projections, evaluated rows or Q-Bundle slots, evaluated candidates or structures, parity frame, eval purpose, intended eval operation, result form, receiving use, and refresh or retire condition. Add project-use refs only for a claimed project-local program; add Method, MethodDescription, actual evaluation Work, operation-application, and typed-result refs only when those separate objects are current.

```text
ArchitectureCharacteristicEvalProgram@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureEvalProgramProjectUseRelationRef?: U.RelationRef governed by the exact eval-program-use or work-use pattern
  claimScopeRef: U.EntityRef referencing one U.ClaimScope
  selectedContextSliceRefs:
  effectiveReferenceScheme:
  referencePlane?:
  evaluationWindow:
  inputProjectionRefs:
  evaluatedCriteriaSetRef:
  evaluatedCriteriaRowRefs:
  evaluatedQBundleSlotRefs?:
  evaluatedCandidateRefs?:
  evaluatedBearerOrSelectedStructureRefs:
  evalPurpose: characterizeCurrentArchitecture | compareCandidates | monitorEvolution | prepareSelection | triggerNextSynthesis
  evalQuestion:
  parityFrameRef:
  evalScope: singleCriterion | coupledCriteria | qBundleSlice | variantPortfolio | holisticUseSlice
  evalOperation: measurement | simulation | benchmark | scenarioWalkthrough | test | monitor | expertReview | evidenceAudit
  triggerMode: onePass | batchComparison | continual | onChange | manualOnDemand
  resultForm: reading | band | rank | dominanceRelation | tradeoffFront | qualitativeState | evidenceFinding
  runContext: designTime | laboratory | pipeline | production | workReview | decisionPrep
  measurementOrObservationMethodRefs:
  methodDescriptionRefs?:
  evaluationWorkOccurrenceRefs?: U.EntityRef constrained to U.Work
  evaluationOperationApplicationRefs?: direct-owner relation or A.6.1 application references
  evaluationResultRefs?: typed result references governed by the selected direct owner
  uncertaintyAndMissingDataPolicy:
  proxyRisk:
  protectedCounterCharacteristicRefs:
  comparisonPolicyRef?:
  receivingUseRef:
  refreshOrRetireCondition:
```

Here `@Project` is a compatibility and retrieval cue only. It supplies no project entity, composite-work identity, context, authority, viewpoint, or parthood. A program local to one actual project names both the exact composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining direct program-use relation in `architectureEvalProgramProjectUseRelationRef`; either field alone is insufficient. `evalOperation` states the intended operation family in the program record, not an actual run or application. Each value in `evaluationWorkOccurrenceRefs` denotes a separate dated `U.Work`; its admitted performer System, exact `U.RoleAssignment`, F.6 attribution, any enacted Method or actual direct-owner/A.6.1 application binding, and each typed result remain under their direct owners. A program, Method, MethodDescription, Work occurrence, operation application, and result never substitute for one another.

What goes wrong if C.32.ACE is missed: a project has architecture-characteristic rows but treats a test, monitor, dashboard, or source-side "fitness function" as the criterion or as the decision. The team may then reject useful losing variants as errors, optimize one indicator, or choose a candidate without fair comparison.

What C.32.ACE buys in practice: eval work is framed as typed evaluation over declared architecture criteria. A losing candidate can still add knowledge about the solution space, while an actual error remains a failure against an expectation that causes unplanned rework.

Adoption test: after using C.32.ACE, the record shows which variants were read under the same parity frame, what result form was produced, and which receiving pattern may use that reading as feedback.

Not this pattern when the characteristic rows do not exist yet. Also not this pattern when the current work is measurement validity, composite-quality modeling, explicit comparison, set-returning selection, local choice, publication of a selected set, evidence, assurance, or project architecture decision.

Common exits by claim kind:

- `C.32.HCS` and `C.32.ACS` before characteristic rows exist.
- `C.16` for measurement validity, readings, units, uncertainty, or comparability claims.
- `C.25` for Q-Bundles and composite quality families.
- `E.13` when an eval result or dashboard starts replacing the declared architecture concern.
- `C.32` for candidate synthesis, `C.32.MLAO` for residual input, and `E.23` for repeated improvement feedback.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for publication of a selected set.
- `A.10` and `B.3` when evidence or assurance claims are being made.
- `C.32.PAD` for project decision.

