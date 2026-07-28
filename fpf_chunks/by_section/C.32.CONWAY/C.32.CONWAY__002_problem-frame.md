---
chunk_kind: "child"
pattern_id: "C.32.CONWAY"
pattern_title: "Architecture-Influence and Transformed-Architecture Correspondence"
section_id: "C.32.CONWAY:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.CONWAY/C.32.CONWAY__002_problem-frame.md"
commit_sha: "17edd955485f60cafb16159c7d90e20f4ad21844"
heading_path:
  - "C.32.CONWAY — Architecture-Influence and Transformed-Architecture Correspondence"
  - "C.32.CONWAY:1 — Problem frame"
line_start: 64667
line_end: 64838
dependencies:
  - "A.10"
  - "A.12"
  - "A.15.1"
  - "A.19.CPM"
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
  - "G.5"
keywords:
---

### C.32.CONWAY:1 - Problem frame

Use this pattern when one architecture, selected structure, Work arrangement, communication structure, constraint, or candidate-synthesis result influences the candidate architecture of a changed referent, and the practitioner must decide what to change on either side without mistaking influence for action.

Plain cue: **compare an architecture that influences the change with the architecture being changed**.

Primary working reader: an architect or architecture-responsible practitioner who must compare one independently typed influence source with the architecture of the changed referent and prepare candidate changes without turning either architecture into an actor.

Typical entry situations include:

- a desired product architecture cannot be produced and verified by the current manufacturing and certification arrangements;
- chosen service boundaries still force every delivery team to coordinate every release;
- a method family is proposed for changing documents, but the assigned review roles and evidence structure do not fit what the project must produce;
- an AI-agent toolchain is intended for Work on project products, but its control and evidence boundaries do not fit the changed product architecture; or
- the project needs a source-side, transformed-side, joint, or bounded-mismatch inverse-Conway candidate rather than another diagram of the desired target.

A clean-looking target architecture can still be unbuildable or unproducible, untestable, hard to maintain or evolve, or hard to certify. Existing production, communication, approval, control, evidence, and operating arrangements can constrain the candidate and shift coordination into shared releases, approvals, evidence reconciliation, or exception handling. Treat each such arrangement as an independently typed influence source and recover its direct influence relation when that relation is asserted; the source architecture does not act, and mirroring alone does not establish architecture adequacy.


Start with the domain action: a manufacturing system builds a product, a compiler compiles a program, a service team changes a service, a clinical team treats a patient, or an instructional system teaches a learner. Identify the changed referent first. Only then name an acting system, role assignment, and dated Work when those facts are current. Separately name the architecture or other source that influences the candidate and the exact relation by which it does so.

**First-minute use slice.** A product-family team wants independently replaceable field modules. It identifies the changed referent as the product-family module boundary, the source as one `ArchitectureOf@ManufacturingAndCertification` with a batch line and shared evidence responsibility, and the transformed side as `ArchitectureOf@ProductFamily` with its current field-module boundary structure. No direct architecture-influence kind or predicate has yet been recovered, so the team keeps the pairing as a provisional independent-change pressure with `missing-governor`. It prepares source-side, transformed-side, joint, and bounded-mismatch candidates without naming an actor, role, or Work occurrence. Those facts are added separately only if a later claim needs them.

The primary working object is a local candidate-synthesis frame. When one exact architecture-influence or correspondence relation already obtains, C.32.CONWAY also owns one reusable `ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context` episteme about that exact occurrence. The frame, row, changing system, Work, changed referent, architecture claims, candidate palette, and any network that later cites the row remain different objects.

What goes wrong if this pattern is missed: an architecture, organization chart, method family, toolchain, communication structure, or network record is called the transformer and silently receives agency, role, Work, or participation in the change. Or the reverse happens: real performer and Work facts disappear behind a vague claim that one architecture shaped another.

What this buys in practice: the practitioner can prepare architecture candidates while preserving four independent questions—what changed, who acted or performed Work, which sources influenced the candidate, and which exact architecture pair the current correspondence row concerns.

Ordinary working move:

1. name the changed referent and exact changing relation when one is being claimed;
2. name exact acting and performance facts only when current;
3. name each influence source with its kind and direct influence relation;
4. select one pair consisting of an influence-source architecture and a transformed architecture;
5. prepare source-side change, transformed-side change, joint change, or bounded mismatch candidates.

Adoption test: a reader can tell which exact case passes, which does not, what the practitioner changes next, and whether the result is only local synthesis material or a reusable exact pair row.

Not this pattern when the current work is only bounded-change identification, role or Work attribution, module-interface repair, mathematical structural similarity, local choice, or an architecture decision. Use the direct governing pattern and return here only when one pair of an influence-source architecture and a transformed architecture changes candidate synthesis.

Common exits by claim kind:

- `A.3.4` or `A.3.4.P` for the bounded change and changed referent.
- `A.12`, `A.15.1`, and direct role-relation and Work-relation owners for acting system, role assignment, dated Work, and work-to-change facts.
- `A.6.M` for module-interface repair.
- `C.32.ACS` for current architecture-characteristic criteria rows and `C.25` for any composite Q-Bundle and exact slot used by the trade-off.
- `C.29` and the project-selected structural-equivalence pattern for structural similarity.
- `A.19.CPM` for explicit comparison and `A.19.SelectorMechanism` for set-returning selection.
- `G.5` for selected-set publication; `C.18` and `C.19` for archive, front, or pool-treatment policy.
- `C.11` for fixed local choice and `C.32.PAD` for a project architecture decision.

The first useful output is `ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project`. It is a working record for candidate synthesis, not an acting entity, exact relation occurrence, architecture decision, or structural-equivalence claim.

For a first pass, fill only the bounded context, synthesis question, independently identified changed referent, source and transformed architecture refs, one selected structure on each side, either the current governed characteristic refs or plain provisional characteristic heads, the applicable candidate-form heads, and the next governing pattern. Assert an influence row only when its direct relation is current; otherwise keep one explicit provisional pressure in `provisionalArchitectureCharacteristicHeads[]` and its exact return. The first-minute case above can be filled as follows:

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project:
  boundedContextRef: ProductFamilyModuleChange@2026Q3
  synthesisQuestion: which source-side, product-side, joint, or bounded-mismatch change can support independently replaceable field modules?
  changedReferentRef: ProductFamilyFieldModuleBoundary@2026Q3
  influenceSourceSelectedStructureMap[]:
    - influenceSourceArchitectureRef: ArchitectureOf@ManufacturingAndCertification
      structureKindRef: BatchAndEvidenceResponsibilityStructure
      selectedStructureRef: BatchLineSharedEvidenceStructure@Current
      contributionToCandidatePressure: may prevent independent field-module replacement
      architectureCharacteristicPressure: provisional independent-change pressure
      governingPatternRef: A.22
      sourceReturnCondition: missing-governor — recover the direct architecture-influence kind and predicate
  transformedArchitectureRef: ArchitectureOf@ProductFamily
  transformedHolonRef: ProductFamily@Current
  transformedSelectedStructureMap[]:
    - structureKindRef: ModuleBoundaryStructure
      selectedStructureRef: FieldModuleBoundaryStructure@Current
      requiredArchitectureRole: permit independent field-module replacement
      architectureCharacteristicPressure: provisional independent-change pressure
      governingPatternRef: A.22
  correspondenceClaims[]:
    - correspondenceId: BatchEvidence-to-FieldModulePressure
      influenceSourceArchitectureRef: ArchitectureOf@ManufacturingAndCertification
      transformedArchitectureRef: ArchitectureOf@ProductFamily
      influenceSourceSelectedStructureRef: BatchLineSharedEvidenceStructure@Current
      transformedSelectedStructureRef: FieldModuleBoundaryStructure@Current
      correspondenceUse: prepare candidates; no exact pair row asserted
      pressureDirection: batch and evidence arrangements may constrain module independence
      provisionalArchitectureCharacteristicHeads[]: independent change for field modules
      receivingPatternRef: C.32.ACS
      sourceReturnCondition: missing-governor — recover the direct influence kind and predicate
  candidateArchitectureConfigurations[]:
    - candidateRef: SourceSideChange@CellAndEvidenceRoles
    - candidateRef: TransformedSideChange@FieldModuleBoundary
    - candidateRef: JointChange@CellEvidenceAndModuleBoundary
    - candidateRef: BoundedMismatch@ExplicitExceptionCost
  evolutionWindowRef: ProductFamilyModuleChange@2026Q3
  nextGoverningPatternRef: C.32.ACS
```

This sparse frame asserts no influence occurrence and no exact pair row. The four candidate refs are first-pass heads, not comparison-ready configurations. Add acting-system, role-assignment, dated-Work, exact-pair-row, C.29, network, publication, comparison-ready gain/loss/preservation, and any additional source-return fields only when the corresponding claim becomes current; adding them refines this frame without changing its changed referent, architecture pair, or provisional pressure. The complete extension schema is:

```text
ArchitectureInfluenceTransformedArchitectureCorrespondenceFrame@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  architectureCorrespondenceFrameProjectUseRelationRef?: U.RelationRef governed by the exact synthesis-use or work-use pattern
  boundedContextRef:
  synthesisQuestion:
  changedReferentRef:
  exactChangingRelationRef?: separately governed U.RelationRef
  performerRows[]?:
    actingSystemRef: U.SystemRef
    roleAssignmentRef?: U.RoleAssignmentRef, required when a role is claimed
    workOccurrenceRef?: U.WorkRef, required when performance is claimed
    performedUnderAssignmentRelationRef?: U.RelationRef, required with workOccurrenceRef
    actorSideOrWorkToChangeRelationRefs[]: exact U.RelationRef values required by the current claim
  influenceSourceRows[]?: asserted influence facts only
    influenceSourceRef:
    influenceSourceKindRef:
    exactInfluenceRelationRef: U.RelationRef
    influenceGoverningPatternRef:
  influenceSourceSelectedStructureMap[]?:
    influenceSourceArchitectureRef?: ArchitectureOf@Context
    structureKindRef:
    selectedStructureRef:
    contributionToCandidatePressure:
    architectureCharacteristicPressure:
    governingPatternRef:
    sourceReturnCondition?:
  transformedArchitectureRef: ArchitectureOf@Context
  transformedHolonRef: transformedArchitectureRef.describedHolonRef
  transformedSelectedStructureMap[]:
    structureKindRef:
    selectedStructureRef?:
    requiredArchitectureRole:
    architectureCharacteristicPressure:
    governingPatternRef:
    sourceReturnCondition?:
  evolutionWindowRef:
  architecturePairRowRefs[]?: ArchitectureInfluenceTransformedArchitectureCorrespondenceRow@Context refs
  correspondenceClaims[]?: synthesis-local compound claims that have not yet met the exact-row assertion threshold
    correspondenceId:
    influenceSourceArchitectureRef?:
    transformedArchitectureRef:
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
    receivingPatternRef:
    sourceReturnCondition:
  candidateArchitectureConfigurations[]:
    candidateRef:
    influenceSourceSideChange?:
    transformedArchitectureChange?:
    coordinationChange?:
    expectedArchitectureGain?:
    knownArchitectureLoss?:
    evolutionWindowRef?:
    receivingPatternRef?:
    sourceReturnCondition?:
    stopOrEscalationCondition?:
  c29LensOrStructuralEquivalenceRef?:
  nextGoverningPatternRef:
```

The two project-use fields are unchanged. `@Project` remains a compatibility and retrieval cue only. If the frame is used in one actual project, `projectWorkOccurrenceRef` names the exact composite `U.Work` and `architectureCorrespondenceFrameProjectUseRelationRef` names the direct relation by which that Work uses the frame. The frame, synthesis Work, candidates, architecture claims, and project Work remain distinct.

`TransformerTransformedArchitectureCorrespondenceFrame@Project` and the former title “Transformer and Transformed Architecture Correspondence” are lineage and search cues only. They do not name the current Tech object, make any named value an actor, or establish an actor, role, Work, or participation fact.

