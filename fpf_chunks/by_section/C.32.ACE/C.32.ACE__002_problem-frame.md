---
chunk_kind: "child"
pattern_id: "C.32.ACE"
pattern_title: "Architecture Characteristic Eval Programs"
section_id: "C.32.ACE:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ACE/C.32.ACE__002_problem-frame.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.32.ACE — Architecture Characteristic Eval Programs"
  - "C.32.ACE:1 — Problem frame"
line_start: 82131
line_end: 82212
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
  - "architecture fitness-function source wording"
  - "architecture-characteristic eval program"
  - "comparison input"
  - "current-architecture evaluation"
  - "eval result"
  - "measurement boundary"
  - "missing-data policy"
  - "monitoring"
  - "parity frame"
  - "proxy risk"
---

### C.32.ACE:1 - Problem frame

Use this pattern when an architecture team has a criterion for an architecture characteristic, either in a project criteria set or in a declared C.25 Q-Bundle slot, and must evaluate the current architecture, compare candidate architectures, monitor evolution, or prepare a selection input.

Primary working reader: an architect or evaluator preparing readings over declared architecture-characteristic criteria without turning those readings into the criteria or the decision.

Typical entry phrases:

```text
"We have criteria rows; which eval reading shows how candidate A and candidate B compare under the same parity frame?"
"The monitor is useful, but is this a reading, a test failure, or a decision input?"
"Two methods, roles, system variants, or AI workflows need fair comparison against the same architecture characteristics."
```

**First-minute use slice.** A product-family team must compare two architectures for substitutability, evidence reuse and latency, while preserving a safety constraint. Recover the workload, latency quantity and operating conditions of the criterion. A warm-start observation covers the warm start it measures. If the design also has an applicable bound of at most 10 ms extra for a cold start and at most 70 ms for a warm start throughout the required workload, the team can use the resulting 80 ms upper bound for a 100 ms limit. If starts may exceed that extra time, obtain evidence for the uncovered conditions. Check the test package against each changed interface for the separate evidence-reuse question. Each result keeps its subject, conditions and grounds. The bound settles the latency limit for the covered design. To compare both designs, obtain the grounds needed for each remaining criterion. For a configuration the team can commit to, establish that the results for the required criteria hold together there. For performance promised across operating modes or choices left to others, establish the requirement throughout those conditions.

This pattern frames architecture evaluation over declared criteria rows, Q-Bundle slots, candidates, bearers or selected structures. Use a parity frame when the receiving inference depends on comparable conditions. The optional record below uses a C.32.ACE-local form and introduces no new U-kind. Its program label establishes neither Method or MethodDescription membership, a WorkPlan, dated Work, nor an evaluation result. When measurement validity, comparison policy, a selection result, G.5 result declaration, publication, or architecture decision is current, use the definition and test for that claim.

Ordinary working move: select the declared criteria rows or Q-Bundle slots and bind the claim scope, relevant context slices and reference scheme, adding a plane, evaluation window or input projection when the evaluation or receiving inference depends on it, and establish parity for the variants when comparison depends on it. To identify a particular evaluation as `U.Work`, establish who performed it at the scale of the claim. A laboratory can be the evaluating System. Ground each claimed performer under A.13 and admit the occurrence under A.15.1. For a claim about a particular operator, establish that operator's contribution. Add `evaluationWorkAttributionRefs` only when the program or receiving use represents precise assignment-bound attribution; missing or failed F.6 attribution alone leaves the Work intact while its independent A.13/A.15.1 grounds hold. Any A.6.1 operation application is an additional relation, not a substitute for the Method enacted by the Work. Return the typed results established through their result patterns as feedback for comparison or the next synthesis pass.

The first useful result explains how a bounded architecture evaluation will obtain the result needed by the receiving use. An ordinary account can suffice; use `ArchitectureCharacteristicEvalProgram@Project` when a record helps preserve that framing. When a reusable way of evaluating is current, identify that separate `U.Method` under A.3.1; when a claim-bearing episteme describes that exact Method, test the same episteme for `U.MethodDescription` under A.3.2. A planned evaluation belongs to A.15.2, an actual dated evaluation to A.15.1, and each result to its measurement, comparison, evaluation, or assertion pattern. Use the record to frame readings of characteristics through rows, slots, candidates, or structures; it is not any of those neighboring objects.

For a first pass, make the evaluated rows or Q-Bundle slots, candidates or structures, purpose, operation, result form, receiving use and necessary conditions recoverable. Bind the claim scope, relevant context slices and reference scheme, including every declared selector. Include a plane, temporal window, input projection, parity frame or refresh condition when the evaluation or its use depends on it. A performed measurement retains its C.16 time stance; a dated Work occurrence retains its own extent. Add project-use, Method, MethodDescription, Work, operation-application and typed-result references only for those current claims.

```text
ArchitectureCharacteristicEvalProgram@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureEvalProgramProjectUseRelationRef?: U.RelationRef governed by the exact eval-program-use or work-use pattern
  claimScopeRef: U.EntityRef referencing one U.ClaimScope
  selectedContextSliceRefs:
  effectiveReferenceScheme:
  referencePlane?: when interpretation depends on it
  evaluationWindow?: when the evaluation or receiving use depends on time
  inputProjectionRefs?: when selected projections are used
  evaluatedCriteriaSetRef?: when evaluating a row from this set
  evaluatedCriteriaRowRefs?: the evaluated rows from that set
  evaluatedQBundleSlotRefs?: the evaluated slots from C.25
  evaluatedCandidateRefs?:
  evaluatedBearerOrSelectedStructureRefs:
  evalPurpose: characterizeCurrentArchitecture | compareCandidates | monitorEvolution | prepareSelection | triggerNextSynthesis
  evalQuestion:
  parityFrameRef?: when the receiving inference depends on comparable conditions
  evalScope: singleCriterion | coupledCriteria | qBundleSlice | variantPortfolio | holisticUseSlice
  evalOperation: measurement | simulation | benchmark | scenarioWalkthrough | test | monitor | expertReview | evidenceAudit | analyticalDerivation
  triggerMode: onePass | batchComparison | continual | onChange | manualOnDemand
  resultForm: reading | band | rank | dominanceRelation | tradeoffFront | qualitativeState | evidenceFinding
  runContext: designTime | laboratory | pipeline | production | workReview | decisionPrep
  measurementOrObservationMethodRefs?: when the evaluation relies on measurement or observation
  methodDescriptionRefs?:
  evaluationWorkRefs?: FinSet(U.EntityRef constrained to U.Work)
  evaluationWorkAttributionRefs?: FinSet(U.RelationRef constrained to obtaining performedUnderAssignment relations)
  evaluationOperationApplicationRefs?: subject-pattern relation or A.6.1 application references
  evaluationResultRefs?: typed result references accepted under the definition and test for each result
  uncertaintyAndMissingDataPolicy:
  proxyRisk: material risk, unresolved risk, or reason no material proxy risk was identified
  protectedCounterCharacteristicRefs?: when a loss needs protection
  comparisonPolicyRef?:
  receivingUseRef:
  refreshOrRetireCondition:
```

Here `@Project` is a compatibility and retrieval cue only. It supplies no project entity, composite-work identity, context, authority, viewpoint, or parthood. A program local to one project names both the composite `U.Work` in `projectWorkOccurrenceRef` and the obtaining program-use relation in `architectureEvalProgramProjectUseRelationRef`; either field alone is insufficient. `evalOperation` states the intended operation family in the program record, not a run or application. Each `evaluationWorkRef` names one independently identified `U.Work` occurrence whose performers have A.13 cores and which A.15.1 admits independently. `evaluationWorkAttributionRefs` are optional and appear only when the record or receiving use represents precise assignment-bound attribution; any present ref resolves through F.6 to the same obtaining A.13 assignment, and its absence or failure alone leaves independently admitted Work intact. If that same finding questions a premise consumed by Work admission, recheck the premise and dependent conclusions. Any A.6.1 application binding and each typed result remain under the applicable patterns. A program, Method, MethodDescription, Work occurrence, operation application, assignment, attribution, and result never substitute for one another.

What goes wrong if C.32.ACE is missed: a project has architecture-characteristic rows but treats a test, monitor, dashboard, or source-side "fitness function" as the criterion or as the decision. The team may then reject useful losing variants as errors, optimize one indicator, or choose a candidate without fair comparison.

What C.32.ACE buys in practice: eval work is framed as typed evaluation over declared architecture criteria. A losing candidate can add knowledge about the solution space, while an error remains a failure against an expectation that causes unplanned rework.

The result identifies the candidates, bearers or structures, the conditions of evaluation, the intended result form and its receiving use. A comparative inference retains its parity conditions. An actual result is established separately under the rule for its result kind.

If neither an applicable C.32.ACS criterion nor a declared C.25 slot supplies what is to be evaluated, establish that criterion first. For measurement validity, composite-quality modeling, explicit comparison, selection, publication, evidence, assurance or an architecture decision, use the pattern governing that result.

Common exits by claim kind:

- `C.32.HCS` and `C.32.ACS` when the evaluation still needs a criterion. A declared `C.25` Q-Bundle slot can already supply it.
- `C.16` for measurement validity, readings, units, uncertainty, or comparability claims.
- `C.25` for Q-Bundles and composite quality families.
- `E.13` when an eval result or dashboard starts replacing the declared architecture concern.
- `C.32` for candidate synthesis, `C.32.MLAO` for residual input, and `E.23` for repeated improvement feedback.
- `A.19.CPM` for explicit comparison, `A.19.SelectorMechanism` for set-returning selection, `C.11` for local choice, and `G.5` for selected-set result declaration. For publication, use E.24.PUB for the occurrence and audience availability, and E.17 when a source-backed face and source return are needed.
- The subject rule for an evidence claim's required support; `A.10` when its source-to-use account needs recovery or replay, and `B.3` for a named assurance claim.
- `C.32.PAD` for project decision.

