---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__005_solution.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:4 — Solution"
line_start: 67154
line_end: 67257
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.19"
  - "A.2.1"
  - "A.2.6"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.13"
  - "E.17"
  - "E.21"
  - "E.22"
  - "E.24.PUB"
keywords:
  - "ArchitectureDecisionAdequacyEvaluation@Project"
  - "E.21 labels"
  - "architecture decision adequacy"
  - "complete coordinate set"
  - "declared use"
  - "method docking"
  - "no average"
  - "publication projection"
  - "repair target"
---

### C.32.ADA:4 - Solution

Create `ArchitectureDecisionAdequacyEvaluation@Project` for one declared use. Evaluate the complete coordinate set. Do not average coordinate values. Use the weakest live coordinate to choose the next repair.

#### C.32.ADA:4.1 - Shared value meanings

Use the same ordinal value domain and labels as `E.21`. ADA specializes what counts as expression for architecture-decision adequacy; it does not create a second scale.

| Value | Label | Architecture-decision adequacy meaning |
|---:|---|---|
| `0` | `absent` | The coordinate is not expressed for the declared architecture-decision use. |
| `1` | `namedOnly` | The coordinate is named or implied, but cannot support reliance, action, evaluation, or repair. |
| `2` | `partiallyExpressedForDeclaredUse` | The coordinate is present but incomplete, fragile, misplaced, or too narrow for the declared use. |
| `3` | `sufficientlyExpressedForDeclaredUse` | The coordinate can support the declared use in the current project, with limits visible. |
| `4` | `wellExpressedForDeclaredUse` | The coordinate has clear refs, boundaries, source-return, and repair path for likely project changes. |
| `5` | `exceptionallyExpressedForDeclaredUse` | The coordinate is well expressed and transferable across another team, later slice, or adjacent holon kind with minimal recovery work and no hidden neighbor loss. |

Values are ordinal content evaluations. They are not measures, averages, votes, maturity ladder names, evidence weights, assurance levels, gate statuses, or implementation approval.

The result-bearing coordinate row uses the E.21 label domain with an architecture-decision coordinate:

| Coordinate | Value | Label | ShortRationale |
|---|---:|---|---|
| `<ADA coordinate>` | `<0..5>` | `<E.21 label>` | `<why the lower adjacent value would understate the expressed content; why the higher adjacent value would overstate it, or for 5 what makes 4 too weak and what would lower or reopen>` |

`5` is not required for every use. Stop conditions are declared before evaluation. A lower diagnostic floor may be used for exploration or internal discussion, but it does not make the decision ready for developer work, implementation commitment, or governance enforcement.

#### C.32.ADA:4.2 - Complete coordinate set

Evaluate every coordinate. If a coordinate is not live, mark it `notTriggered` only with a short reason grounded in the declared use.

| Coordinate | What is evaluated | Repair when weak |
|---|---|---|
| `BoundedDecisionQuestionRecoverability` | Decision subject, described holon, exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme and plane, evaluation window, status, and decision question can be recovered; a selected `BoundedModelUseStructure` is named only when it independently changes interpretation. | Return to `C.32.PAD`, A.2.6, or A.1.1 for the exact missing decision-subject, scope, slice, or model-use-structure content. |
| `CandidateBasisAndSelectionTraceability` | Candidate palette, residual frame, comparison, selection, selected set, or reason no candidate-set question is live is recoverable. | Return to `C.32`, `C.32.MLAO`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, or `C.11`. |
| `AffectedStructureAndDescriptionAdequacy` | Affected selected structures, views, architecture descriptions, correspondence, structural-information lens uses, and source-return are recoverable. | Return to `C.30`, `C.30.ASV`, `C.30.AD`, `A.6.F`, `A.6.M`, or `C.29`. |
| `ArchitectureCharacteristicTradeoffAdequacy` | Architecture characteristics, criteria rows, Q-Bundles, eval readings, accepted losses, and guardrails are explicit. | Return to `C.32.ACS`, `C.32.HCS`, `C.25`, `C.32.ACE`, `C.16`, `C.31`, or `C.31.ASAP`. |
| `MethodAndWorkDockingAdequacy` | Method-use instructions, responsible roles, work boundaries, readiness, and expected structure effects are usable. | Return to `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `E.8`, `E.11.PUR`, or `C.24`. |
| `ArchitectDeveloperSplitAdequacy` | Architect-owned structures, developer-owned refinement, holon-transition or BOSC-triggered boundary refs, and source-return condition are explicit. | Return to `C.32.PAD`, `A.15`, `B.2.P` for claim-kind recovery, and `B.2` when whole reidentification is triggered. |
| `PublicationProjectionAdequacy` | ADR-like or other publication projection carries the needed section functions for the declared readers. | Return to `C.32.ADR`, `E.17`, or `E.24.PUB`. |
| `EvidenceEvalAndGateExitAdequacy` | Eval, evidence, assurance, gate, or governance exits are named only when live and routed to governing patterns. | Return to `C.32.ACE`, `C.16`, `A.10`, `B.3`, `A.21`, or local governance pattern. |
| `EvolutionAndReopenConditionAdequacy` | Reopen, supersession, stronger-source return, and changed-context triggers are clear. | Return to `C.32.PAD`, `C.32.FAIL`, `C.18`, `C.19`, `E.23`, or source-currentness pattern. |
| `TransformerTransformedCorrespondenceAdequacy` | Required correspondence between transformer-side and transformed-side structures is present when the decision depends on it. | Return to `C.32.CONWAY`, `A.15`, `A.3.4`, `A.3.4.P`, or `E.18`. |
| `NonOverreadAndReceivingPatternAdequacy` | The decision, description, publication, method, eval, evidence, assurance, and gate claims are kept with their governing patterns. | Return to `A.7`, `A.6.P`, `E.10`, `F.18`, or the exact receiving pattern. |
| `ConsequenceAndRepairGuidanceAdequacy` | Consequences, accepted losses, weak coordinates, and next repair instructions are actionable for the declared use. | Return to PAD consequence rows, ADR section functions, or the coordinate-specific repair pattern. |

#### C.32.ADA:4.3 - Use-specific stop conditions

Declare the use before scoring. Common uses:

| Declared use | Ordinary stop condition |
|---|---|
| Internal architecture discussion | Every triggered coordinate is evaluated; `0 absent` coordinates block reliance, and values below `3 sufficientlyExpressedForDeclaredUse` carry repair owners. |
| Ready for architecture review | No triggered coordinate below `3 sufficientlyExpressedForDeclaredUse`; candidate basis, trade-off, affected structures, work split, and reopen condition are strong enough for reviewers to inspect by value. |
| Ready for developer work or implementation commitment | Every triggered coordinate is at least `4 wellExpressedForDeclaredUse` unless a governing project decision explicitly declares a lower diagnostic floor and says the result is not an implementation commitment. |
| Ready for ADR-like publication | Publication projection, section functions, status, source-return, and supersession are at least `4 wellExpressedForDeclaredUse`; if the record will guide developer work, use the developer-work floor too. |
| Ready for governance enforcement | Every triggered coordinate is at least `4 wellExpressedForDeclaredUse`; the gate, evidence, assurance, or governance pattern still owns enforcement status. |

Use these as ordinary defaults. A project can declare stricter stop conditions. It must not weaken a triggered coordinate by hiding it under an average, and it must not call a diagnostic result ready for developer work or governance enforcement.

#### C.32.ADA:4.4 - Small complete evaluation slice

```text
ArchitectureDecisionAdequacyEvaluation@OrderFlow:
  declaredUse: readyForDeveloperWork
  claimScopeRef: OrderFlow developer-work readiness for the named decision and release slice
  selectedContextSliceRefs: OrderFlow service, named product-family release, and current developer-work window slices
  effectiveReferenceScheme: OrderFlow architecture decision scheme edition 4
  referencePlane: selected architecture and developer-work commitment
  evaluationWindow: review session 2026-07-31
  decisionQuestionInputProjectionRef: PAD decision relation plus its declared-use and source-return fields
  evaluatorSystemRef: ArchitectureReviewService-4
  evaluatorRoleAssignmentRef: ArchitectureReviewerAssignment-6
  evaluationWorkOccurrenceRef: DecisionAdequacyEvaluationWork-12
  adequacyResultEpistemeRef: DecisionAdequacyResult-12
  architectureDecisionRelationRef: PAD:order-flow-event-integration
  architectureDecisionRecordProjectionRef: ADR:order-flow-event-integration
  noAveragePolicy: true
  stopCondition: every triggered coordinate >= 4 wellExpressedForDeclaredUse
  strongestBlockingCoordinates:
    - MethodAndWorkDockingAdequacy
    - ArchitectureCharacteristicTradeoffAdequacy
  result: repairBeforeUse
```

| Coordinate | Value | Label | Short rationale and repair |
|---|---:|---|---|
| `BoundedDecisionQuestionRecoverability` | `4` | `wellExpressedForDeclaredUse` | Subject, holon, exact claim scope and selected slices, scheme and plane, window, status, and question are clear; `5` would need transfer evidence across another product-family slice. |
| `CandidateBasisAndSelectionTraceability` | `4` | `wellExpressedForDeclaredUse` | Candidate palette and selected option are cited; `5` would need another team to replay the selection without local recovery. |
| `AffectedStructureAndDescriptionAdequacy` | `4` | `wellExpressedForDeclaredUse` | Module and information structures plus C.30.ASV refs are usable; `5` would need a worked cross-team source-return case. |
| `ArchitectureCharacteristicTradeoffAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Substitutability gain and latency loss are named, but guardrail eval rows are incomplete; repair through `C.32.ACS`, `C.32.ACE`, `C.25`, and `C.16`. |
| `MethodAndWorkDockingAdequacy` | `2` | `partiallyExpressedForDeclaredUse` | The ADR says "use events" but lacks method description, responsible role, readiness exit, and expected structure effect; repair through PAD and `A.15`. |
| `ArchitectDeveloperSplitAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Architect-owned event boundary is clear, but developer-owned schema refinement lacks source-return threshold; repair through PAD and, if level pressure is real, `B.2.P` or `B.2`. |
| `PublicationProjectionAdequacy` | `4` | `wellExpressedForDeclaredUse` | ADR section functions are mapped; `5` would need a replayed package-update or supersession case. |
| `EvidenceEvalAndGateExitAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Eval and gate exits are named but not replayable enough for developer commitment; repair through `C.32.ACE`, `C.16`, `A.10`, `B.3`, or `A.21` as triggered. |
| `EvolutionAndReopenConditionAdequacy` | `4` | `wellExpressedForDeclaredUse` | Reopen triggers cover latency and schema-version pressure; `5` would need an executed supersession slice. |
| `TransformerTransformedCorrespondenceAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Toolchain and product-structure correspondence is locally stated; repair through `C.32.CONWAY` if it becomes load-bearing for work organization. |
| `NonOverreadAndReceivingPatternAdequacy` | `4` | `wellExpressedForDeclaredUse` | Decision, ADR, method, eval, and gate claims are routed to owners; `5` would need a near-miss showing avoided overread. |
| `ConsequenceAndRepairGuidanceAdequacy` | `4` | `wellExpressedForDeclaredUse` | Consequences and repair loci are actionable; `5` would need transfer evidence across another holon kind. |

**PAD adequate, ADR weak.** A fixture architecture decision relation can reach `4 wellExpressedForDeclaredUse` on every triggered PAD, method, work-split, trade-off, and reopen coordinate while the trade-study memo omits status and supersession. ADA returns only the publication projection to `C.32.ADR`; it does not rewrite the PAD relation.

**ADR readable, PAD weak.** A Markdown ADR can have clear headings, status, context, decision, and consequences while the project relation lacks candidate basis, affected selected structures, and method docking. ADA returns the decision relation to `C.32.PAD`, `C.32`, and `A.15`; template completeness does not make the architecture decision adequate.

