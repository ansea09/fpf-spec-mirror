---
chunk_kind: "child"
pattern_id: "C.32.ADA"
pattern_title: "Architecture Decision Adequacy Scales"
section_id: "C.32.ADA:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADA/C.32.ADA__005_solution.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.32.ADA — Architecture Decision Adequacy Scales"
  - "C.32.ADA:4 — Solution"
line_start: 84832
line_end: 84943
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

Evaluate the complete coordinate set for one declared use without averaging its values. Identify the blocking weaknesses and the repair that can make the intended use adequate. Retain a sufficient result; select further improvement when its useful contribution warrants the work.

#### C.32.ADA:4.1 - Shared value meanings

Use the same ordinal value domain and labels as `E.21`. ADA specializes what counts as expression for architecture-decision adequacy; it does not create a second scale.

| Value | Label | Architecture-decision adequacy meaning |
|---:|---|---|
| `0` | `absent` | The coordinate is not expressed for the declared architecture-decision use. |
| `1` | `namedOnly` | The coordinate is named or implied, but cannot support reliance, action, evaluation, or repair. |
| `2` | `partiallyExpressedForDeclaredUse` | The coordinate is present but incomplete, fragile, misplaced, or too narrow for the declared use. |
| `3` | `sufficientlyExpressedForDeclaredUse` | The coordinate can support the declared use in the current project, with limits visible. |
| `4` | `wellExpressedForDeclaredUse` | The coordinate has clear refs, boundaries, source-return, and repair path for likely project changes. |
| `5` | `exceptionallyExpressedForDeclaredUse` | The intended readers can recover the coordinate, its grounds and the choices left to them with minimal effort throughout the declared use. Where the use extends to another team, later situation or kind of holon, the expression supports that transfer and preserves relevant neighbouring coordinates. |

Values are ordinal content evaluations. They are not measures, averages, votes, maturity ladder names, evidence weights, assurance levels, gate statuses, or implementation approval.

The result-bearing coordinate row uses the E.21 label domain with an architecture-decision coordinate:

| Coordinate | Value | Label | ShortRationale |
|---|---:|---|---|
| `<ADA coordinate>` | `<0..5>` | `<E.21 label>` | `<for 1..4, why the lower adjacent value would understate the expressed content and the higher adjacent value would overstate it; for 0, why 1 would overstate it and what would raise or reopen; for 5, what makes 4 too weak and what would lower or reopen>` |

`5` is not required for every use. Stop conditions are declared before evaluation. A lower diagnostic floor may be used for exploration or internal discussion, but it does not make the decision ready for developer work, implementation commitment, or governance enforcement.

#### C.32.ADA:4.2 - Complete coordinate set

Evaluate every coordinate. If a coordinate is not live, mark it `notTriggered` only with a short reason grounded in the declared use. An established absence of required content can warrant a low value; an unperformed check or unavailable basis leaves the dependent value unestablished. Name that missing judgement, retain supported coordinate results and keep the complete evaluation as draft until its required basis is available. Do not use `notTriggered` to conceal that gap.

Assess each statement at the source needed for the decision. An omission in a memo can make the memo unusable for its audience. It leaves open whether the governing decision contains the missing provision. To judge transfer to another team, identify which information and help that team would have and which choices it must recover. Reuse adequate evidence for that coordinate and its stated use. Claim that another team actually succeeded only when its performance is evidenced.

| Coordinate | What is evaluated | Repair when weak |
|---|---|---|
| `BoundedDecisionQuestionRecoverability` | Decision subject, described holon, exact `U.ClaimScope`, relevant A.2.6 `U.ContextSlice` membership, effective reference scheme, applicable plane, any time qualification required by the decision or use, status, and decision question can be recovered; a selected `BoundedModelUseStructure` is named only when it independently changes interpretation. | Repair the missing decision-subject, scope, slice, or model-use-structure assertion using `C.32.PAD`, A.2.6, or A.1.1. |
| `CandidateBasisAndSelectionTraceability` | Candidate palette, residual frame, comparison, selection, selected set, or reason no candidate-set question is live is recoverable. | Repair the missing candidate, comparison, or selection assertion using the applicable content in `C.32`, `C.32.MLAO`, `A.19.CPM`, `A.19.SelectorMechanism`, `G.5`, or `C.11`. |
| `AffectedStructureAndDescriptionAdequacy` | Affected selected structures, views, architecture descriptions, correspondence, structural-information lens uses, and source-return are recoverable. | Repair the missing structure, description, correspondence, or lens-use assertion using `C.30`, `C.30.ASV`, `C.30.AD`, `A.6.F`, `A.6.M`, or `C.29`. |
| `ArchitectureCharacteristicTradeoffAdequacy` | Architecture characteristics, criteria rows, Q-Bundles, eval readings, accepted losses, and guardrails are explicit. | Repair the missing characteristic, criterion, reading, loss, or guardrail assertion using `C.32.ACS`, `C.32.HCS`, `C.25`, `C.32.ACE`, `C.16`, `C.31`, or `C.31.ASAP`. |
| `MethodAndWorkDockingAdequacy` | Method-use instructions identify what a future performer must be able and authorized to do, the conditions to start and the expected effects on structure. Name the intended System when readiness depends on its identity. For performed work, identify the acting System and the extent of its Work. Actual Work retains its obtaining A.13 assignment basis even when the record omits separate assignment fields. Explicit assignment refs and F.6 are added for precise assignment-bound attribution; responsibility remains independently governed. | Repair the missing MethodDescription, Method, A.13 performer basis, A.15.1 Work fact, optional assignment species and F.6 attribution, responsibility predicate or missing governor, readiness, or expected-effect assertion using `A.15`, `A.15.1`, `A.15.2`, `A.15.5`, `E.8`, `E.11.PUR`, `A.6.RCD`, or `C.24`. |
| `ArchitectDeveloperSplitAdequacy` | Structures fixed by the decision, refinement left open to developers, holon-transition or BOSC-triggered boundary refs, and source-return condition are explicit. | Repair the split or claim-kind assertion using `C.32.PAD`, `A.15`, or `B.2.P`; use `B.2` only when whole reidentification is triggered. |
| `PublicationProjectionAdequacy` | ADR-like or other publication projection carries the needed section functions for the declared readers. | Use `C.32.ADR` for the needed projection and `E.24.PUB` for the publication occurrence, form, carrier, audience and availability; add `E.17` when a source-backed face and source return are needed. |
| `EvidenceEvalAndGateExitAdequacy` | Eval, evidence, assurance, gate, or institutional-governance assertions are named only when live, with their exact predicates and subject-pattern locators. | Repair the assertion using `C.32.ACE`, `C.16`, `A.10`, `B.3`, `A.21`, or the named institutional-governance content. |
| `EvolutionAndReopenConditionAdequacy` | Reopen, supersession, stronger-source return, and changed-context triggers are clear. | Repair the reopen, supersession, archive/front, improvement, or source-currentness assertion using `C.32.PAD`, `C.32.FAIL`, `C.18`, `C.19`, or `E.23`. |
| `TransformerTransformedCorrespondenceAdequacy` | Required correspondence between a separately typed influence-source architecture and the transformed-side architecture is recoverable when the decision depends on it. Keep a modal or unresolved synthesis frame distinct from an exact row about an obtaining influence occurrence under `C.32.CONWAY`. | Use `C.32.CONWAY` to repair the correspondence frame or exact pair row. Use `A.15`, `A.3.4`, `A.3.4.P`, or `E.18` only for a separately current Method/Work, actual-change, or flow-structure claim. |
| `NonOverreadAndSubjectAssertionAdequacy` | The decision, description, publication, Method, eval, evidence, assurance and gate claims retain their distinct meanings and applicable definitions or tests. Exact predicate or ClaimGraph identity is needed when the claim or intended reliance depends on it. | Repair the overread, relation, wording, or name using `A.7`, `A.6.P`, `E.10`, `F.18`, or the subject pattern for the unresolved question. |
| `ConsequenceAndRepairGuidanceAdequacy` | Consequences, accepted losses, weak coordinates, and next repair instructions are actionable for the declared use. | Repair the missing consequence, projection function, or coordinate assertion using PAD, ADR, or the coordinate-specific subject pattern. |

#### C.32.ADA:4.3 - Use-specific stop conditions

Declare the use before scoring. Common uses:

| Declared use | Ordinary stop condition |
|---|---|
| Internal architecture discussion | Every triggered coordinate is evaluated; `0 absent` coordinates block reliance, and values below `3 sufficientlyExpressedForDeclaredUse` name the patterns or sources that must be repaired. |
| Ready for architecture review | No triggered coordinate below `3 sufficientlyExpressedForDeclaredUse`; candidate basis, trade-off, affected structures, work split, and reopen condition are strong enough for reviewers to inspect by value. |
| Ready for developer work or implementation commitment | Every triggered coordinate is at least `4 wellExpressedForDeclaredUse`. Establish that the versions, operating conditions, permissions and choices on which those findings depend can hold together for the implementer’s work. A qualified end-to-end result can supply this ground for the conditions it covers. When operating conditions or choices remain open, establish that the instructions work across the required combinations or that authorized participants can adapt in time with the information available. A lower diagnostic floor can serve a separately declared diagnostic use. |
| Ready for ADR-like publication | Publication projection, section functions, status, source-return, and supersession are at least `4 wellExpressedForDeclaredUse`; if the record will guide developer work, use the developer-work floor too. |
| Ready for governance enforcement | Every triggered coordinate is at least `4 wellExpressedForDeclaredUse`; enforcement status requires a separate current gate, evidence-use, assurance, or governance result. |

Use these as ordinary defaults. A project can declare stricter stop conditions. It must not weaken a triggered coordinate by hiding it under an average, and it must not call a diagnostic result ready for developer work or governance enforcement.

#### C.32.ADA:4.4 - Small complete evaluation slice

This slice additionally records a dated evaluation and precise assignment-bound attribution. `ArchitectureReviewService-4` has the A.13 performer basis for decision-adequacy evaluation. A.15.1 independently admits `DecisionAdequacyEvaluationWork-12`, performed from 10:00 to 10:20 on 2026-08-12, enacting `DecisionAdequacyEvaluationMethod-2` within `ProjectArchitectureReviewService-4 : U.System`. The obtaining `ArchitectureReviewerAssignment-6` is of the declared species `ArchitectureReviewerAssignment`, has that recovered performer as holder and covers the Work. The separate F.6 relation uses that same obtaining A.13 assignment. These are the grounds for the Work and attribution fields below; the coordinate result is a separate episteme.

```text
ArchitectureDecisionAdequacyEvaluation@OrderFlow:
  declaredUse: readyForDeveloperWork
  claimScopeRef: OrderFlow developer-work readiness for the named decision and release slice
  selectedContextSliceRefs: OrderFlow service, named product-family release, and current developer-work window slices
  effectiveReferenceScheme: OrderFlow architecture decision scheme edition 4
  referencePlane: selected architecture and developer-work commitment
  evaluationWindow: review session 2026-08-12, 10:00–10:20
  decisionQuestionInputProjectionRef: PAD decision relation plus its declared-use and source-return fields
  evaluatorSystemRef: ArchitectureReviewService-4
  evaluatorAssignmentSpeciesRef: ArchitectureReviewerAssignment
  evaluatorAssignmentOccurrenceRef: ArchitectureReviewerAssignment-6
  evaluationWorkRef: DecisionAdequacyEvaluationWork-12
  evaluationPerformedUnderAssignmentRef: performedUnderAssignment(DecisionAdequacyEvaluationWork-12, ArchitectureReviewerAssignment-6)
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

In this example the implementers can recover the governing grounds, but have to reconcile parts of the record for the same release. The rows identify that work where it affects a rating. For a question confined to this release, excellent expression can be established within this release.

| Coordinate | Value | Label | Short rationale and repair |
|---|---:|---|---|
| `BoundedDecisionQuestionRecoverability` | `4` | `wellExpressedForDeclaredUse` | The subject, question, release window and status are explicit. The reader must consult the referenced window to distinguish this release from the next. Put the effective window beside the decision if that removes a recurrent lookup. |
| `CandidateBasisAndSelectionTraceability` | `4` | `wellExpressedForDeclaredUse` | The record identifies the palette and the selected option. To recover why this option was chosen for this release, the reader follows the palette reference and matches the selected comparison row. |
| `AffectedStructureAndDescriptionAdequacy` | `4` | `wellExpressedForDeclaredUse` | The module and information views show the affected structures. The reader must match their scope references to find where they concern the same interface in this release. |
| `ArchitectureCharacteristicTradeoffAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Substitutability gain and latency loss support a bounded reading of the trade-off, so `2` understates what is usable; incomplete guardrail eval rows prevent `4`. Repair through `C.32.ACS`, `C.32.ACE`, `C.25`, and `C.16`. |
| `MethodAndWorkDockingAdequacy` | `2` | `partiallyExpressedForDeclaredUse` | The directive to use events and the assignment-bound attribution requirement give more content than `1 namedOnly`. The implementers still need the Method, required capabilities and readiness conditions for the intended change. This record also claims that implementation Work was performed under `ServiceTeamAssignment`. Recover that actual Work and its A.13/A.15.1 grounds. For the additional assignment-bound claim, establish the species, obtaining assignment and F.6 attribution. Future instructions may identify the assignment to be secured before implementation. |
| `ArchitectDeveloperSplitAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | The acting Systems and fixed-versus-open Work split are clear enough for a bounded local reading, so `2` understates them; the missing source-return threshold for schema refinement prevents `4`. Repair that PAD boundary. If responsibility is claimed, cite its direct predicate, participants, applicability, and identity or return the missing governor; use B.2.P or B.2 only when the corresponding level or whole question is current. |
| `PublicationProjectionAdequacy` | `5` | `exceptionallyExpressedForDeclaredUse` | The ADR supplies the functions its readers need. Its link opens the effective decision for this release directly. In this use the implementer can recover the governing status with minimal effort. |
| `EvidenceEvalAndGateExitAdequacy` | `3` | `sufficientlyExpressedForDeclaredUse` | Named evaluation and gate continuation conditions give a usable bounded next step, so `2` understates them; their instructions do not yet make the required commitment checks recoverable, preventing `4`. Repair the triggered assertions through `C.32.ACE`, `C.16`, `A.10`, `B.3`, or `A.21`. |
| `EvolutionAndReopenConditionAdequacy` | `4` | `wellExpressedForDeclaredUse` | The record identifies latency and schema-version pressure as reasons to reopen. The guardrail lists triggers by revision. The reader must match the order-flow release and discard the superseded threshold to recover the applicable trigger. |
| `TransformerTransformedCorrespondenceAdequacy` | `notTriggered` | — | The OrderFlow decision in this slice does not rely on the locally mentioned toolchain/product-structure correspondence. Keep that observation as a cue; reopen this coordinate and use `C.32.CONWAY` if the correspondence becomes decision-relevant. |
| `NonOverreadAndSubjectAssertionAdequacy` | `4` | `wellExpressedForDeclaredUse` | The decision, ADR, Method, evaluation and gate state distinct claims. The implementer must match a decision entry to a separately indexed gate entry to establish which governs the next implementation step. |
| `ConsequenceAndRepairGuidanceAdequacy` | `4` | `wellExpressedForDeclaredUse` | The record identifies the affected choices and where to repair them. The reader uses the coordinate table and linked instructions together to locate the applicable action. |

**PAD adequate, ADR weak.** A fixture architecture decision relation can reach `4 wellExpressedForDeclaredUse` on every triggered PAD, Method, work-split, trade-off, and reopen coordinate while the trade-study memo omits status and supersession. ADA identifies only the missing publication-projection assertion and cites `C.32.ADR`; it does not rewrite the PAD relation.

**ADR readable, PAD weak.** A Markdown ADR can have clear headings, status, context, decision, and consequences while the project relation lacks candidate basis, affected selected structures, and Method/Work docking. ADA identifies those missing assertions and cites `C.32.PAD`, `C.32`, and `A.15` as their subject-pattern locators; template completeness does not make the architecture decision adequate.

