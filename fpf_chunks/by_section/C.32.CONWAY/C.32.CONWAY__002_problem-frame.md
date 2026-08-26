---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__002_problem-frame.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:1 — Problem frame"
line_start: 62675
line_end: 62858
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.19.CPM"
  - "A.2.1"
  - "A.22"
  - "A.3.4"
  - "A.3.4.P"
  - "A.6.P.WMR"
  - "A.6.RCD"
  - "A.6.REL"
  - "B.3"
  - "C.11"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ACS"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.PAD"
  - "E.18"
  - "E.18.NET"
  - "F.6"
  - "G.5"
  - "U.Structure"
keywords:
---

### C.32.CONWAY:1 - Problem frame

Use this pattern when one architecture-side source — recovered as an exact described holon, selected `U.Structure`, and either an obtaining C.30 `ArchitectureRelation` or truthful modal `ArchitectureClaim` — or another independently typed Work arrangement, communication structure, constraint, or candidate-synthesis result influences the candidate architecture of a changed referent, and the practitioner must decide what to change on either side without mistaking influence for action.

Plain cue: **compare an architecture that influences the change with the architecture being changed**.

Primary working reader: an architect or architecture-responsible practitioner who must compare one independently typed influence source with the current or modal architecture content of the changed referent and prepare candidate changes without turning an `ArchitectureRelation`, selected structure, claim, or architecture-bearing holon into an actor.

Typical entry situations include:

- a desired product architecture cannot be produced and verified by the current manufacturing and certification arrangements;
- chosen service boundaries still force every delivery team to coordinate every release;
- a method family is proposed for changing documents, but the assigned review roles and evidence structure do not fit what the project must produce;
- an AI-agent toolchain is intended for Work on project products, but its control and evidence boundaries do not fit the changed product architecture; or
- the project needs a source-side, transformed-side, joint, or bounded-mismatch inverse-Conway candidate rather than another diagram of the desired target.

A clean-looking target architecture can still be unbuildable or unproducible, untestable, hard to maintain or evolve, or hard to certify. Existing production, communication, approval, control, evidence, and operating arrangements can constrain the candidate and shift coordination into shared releases, approvals, evidence reconciliation, or exception handling. Treat each such arrangement as an independently typed influence source and recover its direct influence relation when that relation is asserted; the source architecture does not act, and mirroring alone does not establish architecture adequacy.


Start with the domain action: a manufacturing system builds a product, a compiler compiles a program, a service team changes a service, a clinical team treats a patient, or an instructional system teaches a learner. Identify the changed referent first. Only then name an acting system, exact system-role assignment, and dated Work when those facts are current. Separately name the architecture or other source that influences the candidate and the exact relation by which it does so.

**First-minute use slice.** A product-family team wants independently replaceable field modules. It identifies the changed referent as `ProductFamilyFieldModuleBoundary@2026Q3`. The influence side is the obtaining C.30 `ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)`; the transformed side is the obtaining C.30 `ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)`. The exact holons and selected `U.Structure` participants remain visible, and any desired replacement structure stays only in a separate `ArchitectureClaim`. No direct architecture-influence kind or predicate has yet been recovered, so the team keeps the pairing as a provisional independent-change pressure with `missing-governor`. It prepares source-side, transformed-side, joint, and bounded-mismatch candidates without naming an acting system, system-role assignment, Work occurrence, or actual transformation. Those facts are added separately only if a later claim needs them.

The primary working object is a local candidate-synthesis frame. It can pair actual architecture sides through exact obtaining C.30 `ArchitectureRelation` refs or carry candidate, required, desired, or expected structure only through separately identified `ArchitectureClaim` refs. When one exact architecture-influence or correspondence relation already obtains between two actual architecture sides, C.32.CONWAY is also the pattern for one reusable `ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context` episteme about that exact occurrence. The frame, row, architecture relations, claims, selected structures, changing system, Work, actual transformation, changed referent, candidate palette, and any network that later cites the row remain different objects.

What goes wrong if this pattern is missed: an architecture, organization chart, method family, toolchain, communication structure, or network record is called the transformer and silently receives agency, a system-role kind or assignment, Work, or participation in the change. Or the reverse happens: real performer and Work facts disappear behind a vague claim that one architecture shaped another.

What this buys in practice: the practitioner can prepare architecture candidates while preserving four independent questions—what changed, who acted or performed Work, which sources influenced the candidate, and which exact architecture pair the current correspondence row concerns.

Ordinary working move:

1. name the changed referent and, only when actual change is claimed, the independently admitted `U.Transformation`; keep every actor-side or Work-to-change relation separate;
2. name exact acting and performance facts only when current;
3. name each influence source with its kind and direct influence relation;
4. for an exact reusable row, select one pair of obtaining C.30 `ArchitectureRelation` occurrences and keep each holon and selected-structure participant visible; when either side is only candidate, required, desired, or expected, keep the pair in the frame with its exact `ArchitectureClaim` instead;
5. prepare source-side change, transformed-side change, joint change, or bounded mismatch candidates.

Adoption test: a reader can tell which exact case passes, which does not, what the practitioner changes next, and whether the result is only local synthesis material or a reusable exact pair row.

Not this pattern when the current work is only bounded-change identification, system-role assignment or Work attribution, module-interface repair, mathematical structural similarity, local choice, or an architecture decision. Use the subject pattern and return here only when one pair of an influence-source architecture and a transformed architecture changes candidate synthesis.

Common exits by claim kind:

- `A.3.4` or `A.3.4.P` for the bounded change and changed referent.
- `A.12` for acting-side externalization, `A.2.1` for the exact system-role-assignment occurrence, `A.15.1` for dated Work and distributed performers, `F.6` for `performedUnderAssignment(W, RA)` and its actual-performer projection, and the pattern that defines any direct actor-side or Work-to-change relation needed by the current use.
- `A.6.M` for module-interface repair.
- `C.32.ACS` for current architecture-characteristic criteria rows and `C.25` for any composite Q-Bundle and exact slot used by the trade-off.
- `C.29` and the project-selected structural-equivalence pattern for structural similarity.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for selected-set result declaration; `E.17` for a source-backed publication face and source return; `E.24.PUB` for the publication occurrence and audience availability; `C.18` and `C.19` for archive, front, or pool-treatment policy.
- `C.11` for fixed local choice and `C.32.PAD` for a project architecture decision.

The first useful output is `ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project`. It is a working record for candidate synthesis, not an acting entity, exact relation occurrence, architecture decision, or structural-equivalence claim.

For a first pass, fill only the synthesis question, intended correspondence use, ClaimScope when it changes the claim, independently identified changed referent, source-side and transformed-side exact holon and selected-structure refs, and either an obtaining C.30 `ArchitectureRelation` ref or a truthful modal `ArchitectureClaim` ref for each side. Add architecture-characteristic criteria refs or plain provisional heads, applicable candidate-form heads, evidence and the evolution window, and the next pattern. Assert an influence row only when its direct relation is current and both architecture sides are obtaining C.30 occurrences; otherwise keep one explicit provisional pressure in `provisionalArchitectureCharacteristicHeads[]` and its exact return. The first-minute case above can be filled as follows:

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project:
  intendedCorrespondenceUse: prepare architecture candidates for independent field-module replacement
  claimScopeRef?: product-family module-change architecture claims
  synthesisQuestion: which source-side, product-side, joint, or bounded-mismatch change can support independently replaceable field modules?
  changedReferentRef: ProductFamilyFieldModuleBoundary@2026Q3
  influenceSourceSelectedStructureMap[]:
    - influenceSourceHolonRef: ManufacturingCertificationSystem@Plant-A
      influenceSourceArchitectureRelationRef: C.30 ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)
      influenceSourceArchitectureClaimRef?: omitted — the obtaining relation and current structure are enough for this use
      structureKindRef: BatchAndEvidenceResponsibilityStructure
      selectedStructureRef: BatchLineSharedEvidenceStructure@Current
      contributionToCandidatePressure: may prevent independent field-module replacement
      architectureCharacteristicPressure: provisional independent-change pressure
      relationFunctionClaimRef: C.30 plus A.22
      sourceReturnCondition: missing-governor — recover the direct architecture-influence kind and predicate
  transformedHolonRef: ProductFamily@Current
  transformedArchitectureRelationRef: C.30 ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)
  transformedArchitectureClaimRef?: omitted — the obtaining relation and current structure are enough for this use
  transformedSelectedStructureMap[]:
    - structureKindRef: ModuleBoundaryStructure
      selectedStructureRef: FieldModuleBoundaryStructure@Current
      requiredStructureContribution: permit independent field-module replacement
      architectureCharacteristicPressure: provisional independent-change pressure
      relationFunctionClaimRef: C.30 plus A.22
  correspondenceClaims[]:
    - correspondenceId: BatchEvidence-to-FieldModulePressure
      influenceSourceArchitectureRelationRef: C.30 ArchitectureRelation(ManufacturingCertificationSystem@Plant-A, BatchLineSharedEvidenceStructure@Current)
      transformedArchitectureRelationRef: C.30 ArchitectureRelation(ProductFamily@Current, FieldModuleBoundaryStructure@Current)
      influenceSourceSelectedStructureRef: BatchLineSharedEvidenceStructure@Current
      transformedSelectedStructureRef: FieldModuleBoundaryStructure@Current
      correspondenceUse: prepare candidates; no exact pair row asserted
      pressureDirection: batch and evidence arrangements may constrain module independence
      provisionalArchitectureCharacteristicHeads[]: independent change for field modules
      receivingUsePatternLocator: C.32.ACS
      sourceReturnCondition: missing-governor — recover the direct influence kind and predicate
  candidateArchitectureConfigurations[]:
    - candidateRef: SourceSideChange@CellAndEvidenceStructures
    - candidateRef: TransformedSideChange@FieldModuleBoundary
    - candidateRef: JointChange@CellEvidenceAndModuleBoundary
    - candidateRef: BoundedMismatch@ExplicitExceptionCost
  evolutionWindowRef: ProductFamilyModuleChange@2026Q3
  evidenceRefs?: current batch-line evidence-structure and field-module boundary records
  nextQuestionPatternLocator: C.32.ACS
```

This sparse frame asserts no influence occurrence and no exact pair row. The four candidate refs are first-pass heads, not comparison-ready configurations. Add acting-system, exact system-role-assignment, dated-Work, exact-pair-row, C.29, network, publication, comparison-ready gain, loss, and preservation, and any additional source-return fields only when the corresponding claim becomes current; adding them refines this frame without changing its changed referent, architecture pair, or provisional pressure. The complete extension schema is:

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureCorrespondenceFrameProjectUseRelationRef?: U.RelationRef defined by the exact synthesis-use or work-use pattern
  synthesisQuestion:
  intendedCorrespondenceUse:
  claimScopeRef?: U.ClaimScope
  changedReferentRef:
  actualTransformationRef?: U.EntityRef constrained to U.Transformation, only when A.3.4 independently admits the bounded change of changedReferentRef
  performerRows[]?:
    actingSystemRef: U.EntityRef constrained to U.System; for performance, this must equal actingSystemRoleAssignmentRef.HolderSystemSlot
    actingSystemRoleAssignmentRef?: U.RelationRef constrained to U.SystemRoleAssignment, required when an obtaining assignment is claimed and whenever performance is attributed under assignment
    workOccurrenceRef?: U.EntityRef constrained to U.Work, required when performance is claimed
    performedUnderAssignmentRelationRef?: U.RelationRef governed by F.6, required with workOccurrenceRef
    actorSideOrWorkToChangeRelationRefs[]: exact U.RelationRef values required by the current claim
  influenceSourceRows[]?: asserted influence facts only
    influenceSourceRef:
    influenceSourceKindRef:
    exactInfluenceRelationRef: U.RelationRef
    influencePatternLocator:
  influenceSourceSelectedStructureMap[]?:
    influenceSourceHolonRef:
    influenceSourceArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
    influenceSourceArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for actual, candidate, required, desired, or expected content not carried by an obtaining relation
    structureKindRef:
    selectedStructureRef:
    contributionToCandidatePressure:
    architectureCharacteristicPressure:
    relationFunctionClaimRef:
    sourceReturnCondition?:
  transformedHolonRef:
  transformedArchitectureRelationRef?: exact obtaining C.30 ArchitectureRelation ref
  transformedArchitectureClaimRef?: exact C.30 ArchitectureClaimRef for actual, candidate, required, desired, or expected content not carried by an obtaining relation
  transformedSelectedStructureMap[]:
    structureKindRef:
    selectedStructureRef?:
    requiredStructureContribution:
    architectureCharacteristicPressure:
    relationFunctionClaimRef:
    sourceReturnCondition?:
  evolutionWindowRef:
  evidenceRefs?:
  architecturePairRowRefs[]?: ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context refs
  correspondenceClaims[]?: synthesis-local compound claims that have not yet met the exact-row assertion threshold
    correspondenceId:
    influenceSourceArchitectureRelationRef?:
    influenceSourceArchitectureClaimRef?:
    transformedArchitectureRelationRef?:
    transformedArchitectureClaimRef?:
    influenceSourceSelectedStructureRef?:
    transformedSelectedStructureRef:
    correspondenceUse:
    pressureDirection:
    affectedArchitectureCharacteristicRefs[]?: current C.32.ACS criteria-row refs; exact C.25 Q-Bundle slot refs when composite
    provisionalArchitectureCharacteristicHeads[]?: plain discovery cues pending C.32.ACS/C.25; never criteria refs
    expectedArchitectureGain?:
    knownArchitectureLoss?:
    preservedStructure?:
    lostOrHiddenStructure?:
    receivingUsePatternLocator:
    sourceReturnCondition:
  candidateArchitectureConfigurations[]:
    candidateRef:
    influenceSourceSideChange?:
    transformedArchitectureChange?:
    coordinationChange?:
    expectedArchitectureGain?:
    knownArchitectureLoss?:
    evolutionWindowRef?:
    receivingUsePatternLocator?:
    sourceReturnCondition?:
    stopOrEscalationCondition?:
  c29LensOrStructuralEquivalenceRef?:
  nextQuestionPatternLocator:
```

Project-local use keeps two separate fields. `@Project` remains a compatibility and retrieval cue only. If the frame is used in one actual project, `projectWorkOccurrenceRef` names the exact composite `U.Work` and `architectureCorrespondenceFrameProjectUseRelationRef` names the direct relation by which that Work uses the frame. The frame, synthesis Work, candidates, architecture relations, claims, selected structures, and project Work remain distinct. An `ArchitectureRelation` ref is affirmative only for an independently obtaining C.30 occurrence; candidate, required, desired, or expected architecture content stays in an `ArchitectureClaim` and cannot enter an exact pair row as though it already obtained.

`TransformerTransformedArchitectureCorrespondenceFrame@Project` and the former title “Transformer and Transformed Architecture Correspondence” are lineage and search cues only. They do not name the current Tech object, make any named value an actor, or establish an acting-system, system-role-kind, assignment, Work, or participation fact.

