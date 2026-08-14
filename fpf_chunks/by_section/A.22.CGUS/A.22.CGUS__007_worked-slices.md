---
chunk_kind: "child"
pattern_id: "A.22.CGUS"
pattern_title: "Constraint-Governed Unfolding Structure"
section_id: "A.22.CGUS:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/A.22.CGUS/A.22.CGUS__007_worked-slices.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "A.22.CGUS — Constraint-Governed Unfolding Structure"
  - "A.22.CGUS:5 — Worked Slices"
line_start: 35023
line_end: 35092
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "B.3.5"
  - "B.5.2"
  - "C.13"
  - "C.18"
  - "C.19"
  - "C.2.P.DR"
  - "C.3"
  - "C.32.P2S"
  - "C.33"
  - "C.35"
  - "E.10.MOVE"
  - "E.11"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.3"
  - "E.18.NET"
  - "E.18.NET-conforming"
  - "E.23"
  - "E.24.PUB"
  - "F.17"
  - "G.11"
  - "G.5"
keywords:
---

### A.22.CGUS:5 - Worked Slices

**Architecture P2S slice.** A team starts with architecture-relevant problem pressure. The selected unfolding structure may include independently identified problem-side epistemes, unknown-structure and candidate-structure claims, selected structures, architecture characteristics, one exact `ArchitectureDecisionRelation@Project` occurrence defined by `C.32.PAD`, one exact `ArchitectureUnfoldingStructureUse@Project` occurrence defined by `C.32.P2S`, actual-structure feedback relations, and reconsideration conditions. The P2S card can describe those objects and relations, but it creates none of them. Unknown, candidate, selected, or expected structures remain epistemic claim content until their world-side obtaining basis is independently recovered; planned or performed realization Work remains with the A.15 family, and actual structure remains under A.22 and the exact relation definitions used.

**Abductive search slice.** An inquiry starts from an abductive prompt and a cue set selected for the search. The unfolding structure may relate rival hypotheses, plausibility constraints, hypothesis-generation positions, evidence-return relations, and downstream tests. The structure is not evidence; evidence appears only when an evidence pattern defines or constrains the claim.

**Improvement-loop slice.** A pattern version has an evaluation frame and current evaluation result. The unfolding structure may relate E.22 `CandidateImprovementProposalRow@Context` values, protected tradeoffs, scale-qualified E.23 `ExpectedEvaluationResultChange@Context` predictions, one `ImprovementLoopDecisionValue`, and re-evaluation. The loop is not improvement by shape; `E.23` governs repeated improvement only after the object version, evaluation frame, proposal rows, expected result changes, loop decision, and stop or return boundaries are recoverable.

**First-entry seed slice.** A README entry says "develop or review architecture." That line may seed an entry unfolding among problem-side records, candidate first subject-qualified records, bounded results or blockers, and next readable outputs. The README line is a seed description, not the project's unfolding structure and not a universal FPF route.

**Field-filled scaffold slice.** A team has a visible card sequence `problem pressure -> candidate options -> evaluate -> repair`. At first this is an ordinary C.2.1 episteme whose EntityOfConcern is the cooling-design question and whose ClaimContent states proposed positions and continuations plus the unresolved A.22 coordinates. After the exact basis below is recoverable, the team may select one CGUS and separately create a demonstrative slice over it:

```text
selectedCGUSRef: ArchitectureCandidateSynthesisAndImprovementStructure@Cooling-v2
selectedConstituentRefs[]:
  - ProblemCard@Cooling-v2, independently identified as a C.2.1 episteme
  - EvaluationResult@thermal-margin-v1, independently identified by its exact evaluation assertion and defining `ClaimGraph`
  - CurrentModulePlacementStructure@Cooling-v2, independently selected under A.22
  - RepairProposalEpisteme@Cooling-v2, independently identified under C.2.1 as the current proposal claim
  - ReturnConditionEpisteme@Cooling-v2, independently identified under C.2.1 as the current return-condition claim
selectedObtainingRelationOccurrenceRefs[]:
  - CandidateEvaluatedByResult@Cooling-v2, only after an exact defining ClaimGraph supplies the relation predicate and current facts satisfy it
  - ProposalChangesCandidate@Cooling-v2, only after the exact relation predicate and current facts establish that occurrence
  - ResultConstrainsDecision@Cooling-v2, only after the exact relation predicate and current facts establish that occurrence
relationSignatureRefs[]: CandidateEvaluatedByResult; ProposalChangesCandidate; ResultConstrainsDecision, each resolved to an exact direct declaration before use
appliedConstraintClaimRefs[]:
  - ThermalMarginConstraint
  - ServiceAccessConstraint
  - AcceptedLossBoundary
  - MaintainableCoolingPathInvariant
guardedContinuationRows[]:
  - RepairAdmissionGuard with its exact condition claim, required selected relation occurrences, and repair-candidate continuation
namedSelectionUseFrame:
  questionOrAction: decide whether accept-candidate and repair-candidate continuations remain admissible
  forbiddenOverread: no displayed order, authorization, performed Work, or architecture decision follows from the card
positionLocatorRows[]:
  - <selectedCGUSRef, PressurePositionSlotSpec, ProblemCard@Cooling-v2>
  - <selectedCGUSRef, EvaluationResultPositionSlotSpec, EvaluationResult@thermal-margin-v1>
  - <selectedCGUSRef, CandidateStructurePositionSlotSpec, CurrentModulePlacementStructure@Cooling-v2>
  - <selectedCGUSRef, RepairProposalPositionSlotSpec, RepairProposalEpisteme@Cooling-v2>
  - <selectedCGUSRef, ReturnPositionSlotSpec, ReturnConditionEpisteme@Cooling-v2>
preservedStructureRefs[]: CandidateAlternativeStructure; RepairLocalityStructure
structureInformationAdequacyNoteRefs[]: TeachingSliceAdequacyNote@Cooling-v2 under C.33, recording omitted rejected-candidate detail and its declared-use effect
admissibleNextFormKindRefs[]: U.Structure for a C.32 candidate-palette update; U.Episteme for an E.22 proposal; exact decision-relation kind only under C.32.PAD
stopCondition: stop stronger candidate-set or evaluation use when the selected relation occurrences or constraints are no longer recoverable
reconsiderationConditions[]:
  - conditionClaimRef: exact claim that a new candidate appears
    affectedStructureRef: ArchitectureCandidateSynthesisAndImprovementStructure@Cooling-v2
    nextQuestion: does the C.32 candidate-structure selection change?
    relevantPatternRef?: C.32, because it constrains candidate-structure selection
  - conditionClaimRef: exact claim that the evaluated object version changed
    affectedStructureRef: ArchitectureCandidateSynthesisAndImprovementStructure@Cooling-v2
    nextQuestion: does the E.23 improvement evaluation change?
    relevantPatternRef?: E.23, because it supplies the improvement-evaluation test
```

The visible chain helps planning because each filled locator makes the current constituent recoverable. It neither makes the project follow that order nor creates a WorkPlan, Work occurrence, relation, decision, or CGUS by table completion. The block becomes an admitted CGUS basis only after every listed relation declaration resolves, every selected occurrence independently obtains, and the A.22 constraints and use frame are current; otherwise the completely filled display remains a provisional episteme and identifies the exact missing relation definition, current occurrence, stronger claim, or concrete contribution.

**Local relation repair slice.** Later `EvaluationResult@thermal-margin-v2` becomes the current result for the same cooling candidate. Keep the candidate set, structure positions, service-access constraint, maintainable-cooling-path invariant, and reconsideration boundaries. Replace only the referenced `CandidateEvaluatedByResult` relation instance, then re-evaluate `RepairAdmissionGuard` against its exact constraint assertion and defining `ClaimGraph`. If the new result does not satisfy the guard, remove `repair candidate` from the admissible next forms and update the demonstrative slice that showed that branch; the unrelated `accept candidate` continuation remains live. A changed result therefore repairs one relation and its dependent guard before it changes a wider graph.

**Schema-completion proxy failure.** A team counts filled CGUS fields and adds weakly used references until the completion count rises. Update effort then grows, practitioners stop repairing changed relation instances, and wrong next-form choices increase. The count describes field population only; it does not establish recoverability, currentness, or practical value. Remove references without a receiving use, evaluate whether practitioners recover the correct live alternatives and smallest repair, and use `E.13` when field completion is substituting for those outcomes.

**Reference-currentness slice.** A SoTA pack relies on telemetry and admitted publication editions that can decay. CGUS may relate the current reference set, edition-shift relations, decay triggers, possible deprecation or reship records, and a reconsideration boundary. The structure is not the currentness claim; the currentness assertions and defining or constraining `ClaimGraph` located through `G.11` remain separate.

**Physical-modeling slice.** A team models a physical system or another governed EntityOfConcern whose behavior depends on component relations, conservation-like constraints, operating modes, calibration data, and analysis goals. CGUS may relate the model structure, admitted measured data, mode-change relations, compiler boundary, solver boundary, surrogate-substitution relation, and returns to calibration or model-discovery work. In a digital-twin case, the physical entity, digital model, measured-data history, simulation outputs, services, and bidirectional correspondence relations keep their exact kinds and relations. A simulation run, generated code, exchange package, AI-assisted model edit, calibration result, and digital-twin publication remain separate results. Acausal modeling is useful here because it shows that relations and constraints can be stated before a calculation direction is chosen; `C.29`, `G.11`, `E.23`, evidence patterns, and domain DPF patterns supply the stronger mathematical, currentness, evaluation, evidence, or domain-validity rules when those claims are made.

**Formal-expression boundary slice.** A team expresses part of the cooling CGUS as a DCR graph or constraint-solver model to check whether the `repair candidate` branch is reachable under `RepairAdmissionGuard`. The expression preserves selected positions, dependency relations, and the guard. It loses neighboring subject assertions, their reconsideration conditions, C.33 adequacy notes, and any relation not encoded in the chosen formalism. Record that preservation and loss under `C.29`, use the output only for the declared reachability question, and reconsider the selected CGUS before selecting the next form. Satisfiability or reachability does not establish that the expression is the CGUS, prescribe performed-work order, prove architecture adequacy, or authorize work.

**Method-to-work boundary slice.** A selected CGUS may include exact already-obtaining relations among one admitted `U.Method`, an independently identified C.2.1 episteme, `U.WorkPlan`, readiness claim, dated `U.Work`, actual `U.Transformation`, production or inception claim, evidence, assurance, and gate result. Intended realization, a plan seed, display order, imperative grammar, or a relation to expected structure does not make the episteme a `U.MethodDescription`: A.3.2 membership requires that the episteme's exact EntityOfConcern be one admitted Method and that its ClaimContent contain at least one substantive way-of-doing claim. The structure selects only relations and assertions whose defining or constraining `ClaimGraph` sources are located through A.3, A.15, A.3.4, A.15.PROD, A.10, B.3, A.20, or A.21 as applicable; it authorizes and performs nothing.

