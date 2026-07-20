---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__007_worked-slices.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:5 — Worked Slices"
line_start: 81483
line_end: 81522
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.30.TFS-REL"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.23"
  - "G.11"
  - "G.5"
keywords:
---

### E.18.3:5 - Worked Slices

**Minimal first use.** In the candidate-set repair situation, name `CandidateSetComparisonBasis@Review-2026-07` and its kind, then describe candidate `ReferenceEditionChangePosition`, `ComparisonRecalculationPosition`, and the proposed dependency `ComparisonDependsOnAdmittedEdition`. Keep the result as a `ProvisionalUnfoldingDemonstrationDescription@Context` with return descriptions pointing to G.11 and A.19. This already prevents a stale-edition comparison from looking current without asserting typed positions or a relation instance prematurely. Admit the full E.18.3 structure only when the exact dependency and every required admission coordinate are recoverable.

**P2W carry-through.** Accepted problem-side records may name distinctions, constraints, and unresolved relation positions that jointly guide later method selection, planning, work, interpretation, and return. `E.18.3` can relate those positions to candidate governing-pattern positions through exact connection kinds and supporting relations. It does not authorize launch or performed work, and it does not replace E.18.1 carry-through.

**Transformation-flow mini-example.** A team has a flow card "admitted reference-publication edition changes -> recalculate comparison -> update candidate set -> decide whether to repair." E.18.3 admits only the transformation-flow slice:

```text
transformedEntityRef: CandidateSetComparisonBasis@Review-2026-07
transformedEntityKindRef: U.Episteme
transformationPositionRefs[]: ReferenceEditionChangePosition; ComparisonRecalculationPosition; CandidateSetUpdatePosition; DecisionRepairPosition
governingPatternPositionRelationRefs[]: G2SourceUseBasisConnection; G11CurrentnessBasisConnection; A19ComparisonResultConnection; C18RetainedSetResultConnection; C32PADRepairReturnConnection
dependencyRelationReferenceEpistemeRefs[]: ComparisonDependsOnAdmittedEdition; CandidateSetUpdateDependsOnComparison
pathIds[]: CandidateSetRepairFlow
pathSliceIds[]: EditionChangeToDecisionRepairSlice
demonstrativeSliceRefs[]: DemonstrativeUnfoldingSlice@CandidateSetRepairTeaching
guardRelationReferenceEpistemeRefs[]: EditionAdmissionGuard; ComparisonBasisChangeGuard
preservedTransformationStructureRefs[]: EditionToComparisonDependencyStructure; ComparisonToCandidateSetDependencyStructure
structureInformationAdequacyNoteRefs[]: CandidateSetRepairTeachingOmissionNote under C.33, naming omitted comparison branches and return
governingPatternReturnBoundaryRefs[]: return to G.11 for currentness; A.19 for comparison; C.18 for retained-set stewardship; C.32.PAD for decision repair
stopBoundaryRef: stop stronger use when any named position or supporting relation is no longer recoverable
```

Before those typed positions, exact relation references, C.33 omission note, and returns are recoverable, the flow card remains a provisional demonstration description. The block above is admitted only after they are recoverable; its `demonstrativeSliceRefs[]` then names a separate post-admission slice.

**Local edition-relation repair.** `G.11` admits `ReferencePublicationEdition@v2`, while `ComparisonDependsOnAdmittedEdition` still references v1. Keep the transformed entity, flow positions, path ids, preserved structures, and all return boundaries. Replace the stale relation value ref, then re-evaluate `EditionAdmissionGuard`. Reopen the A.19 comparison position only if the admitted comparison basis changed; reopen the C.18 retained-set position only if the comparison result changed; reach C.32.PAD only if that retained-set change affects the current decision. The edition change therefore propagates through exact dependent relations instead of reopening the whole flow by proximity.

**Connected-box proxy failure.** A team reports that every flow-card box is connected and adds low-value edges until path coverage reaches its target. The relation count rises, but guards no longer distinguish admissible alternatives, stale dependencies remain unrepaired, and wrong governing-pattern returns increase. Edge count and path coverage describe the expression only; they do not establish current, useful transformation-flow structure. Remove edges without a declared structural function or subject use, evaluate whether practitioners select the correct guarded continuation and smallest repair, and use `E.13` when display coverage substitutes for those outcomes.

**Architecture P2S projection.** A P2S flow card includes architecture-relevant problem pressure, selected or unknown structures, synthesis positions, and actual-structure feedback relations. If one slice is transformation-flow structure, `E.18.3` names that slice and its exact connections. Architecture use remains with `C.32.P2S` and `C.30.TFS-REL`; an architecture decision remains with `C.32.PAD`.

**Physical workpiece transformation.** A heat-treatment structure concerns `GearBlank@Lot-14`, admitted as a project `U.Holon`, and relates load, soak, quench, and hardness-evaluation positions. `QuenchAdmittedAfterSoakRange` is an exact guard relation; furnace loading and quenching remain planned or performed work under A.15, and the hardness result remains under its evaluation and evidence patterns. A flow card can expose guarded alternatives before execution without claiming that the work occurred.

**Clinical transformation planning.** A treatment-adjustment structure concerns `Patient@Case-17`, admitted as a `U.System`, and relates assessment, intervention-candidate, contraindication-guard, observed-state, and return positions. The structure can show that one observed state changes which intervention remains admissible. It does not authorize treatment, establish evidence sufficiency, replace clinical judgement, or claim that an intervention occurred; those claims remain with their clinical DPF, work, evidence, and gate patterns.

**Formal flow-expression boundary.** A team expresses the candidate-set repair slice as a directed graph or DCR model to ask whether `DecisionRepairPosition` is reachable after `EditionAdmissionGuard`. The expression preserves selected dependency and guard topology plus the queried path. It loses subject-use authority, direct governing-pattern connections, C.33 omission notes, and currentness semantics unless those are separately mapped. Use `E.18.2` for the mathematical description and `C.29` for its admissibility and loss. A positive reachability result does not establish currentness, retained-set validity, decision repair, work order, or the identity of the whole E.18.3 structure.

**Reference-currentness repair.** A path slice can depend on an admitted publication edition, a `G.2` source-use relation, a source pack, or a telemetry window. E.18 governs slice-local flow refresh. `G.11` governs source currentness, decay, edition shift, deprecation, reship, and no-change claims. Connect those positions through exact E.18.3 relations without creating a combined currentness-refresh value.

