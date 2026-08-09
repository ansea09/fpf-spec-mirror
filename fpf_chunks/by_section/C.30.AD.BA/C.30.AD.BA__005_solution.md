---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__005_solution.md"
commit_sha: "036c056e98c38522172c6b7b3ad08214281cc4e4"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:2 — Solution"
line_start: 60694
line_end: 60842
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.5"
  - "A.2.8.PER"
  - "A.2.9"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
  - "A.6.F"
  - "A.6.M"
  - "A.6.P"
  - "A.6.RCD"
  - "A.6.REL"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.27.TA"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.17"
  - "E.17.0"
  - "E.24.PUB"
  - "F.18"
  - "G.11"
keywords:
---

### C.30.AD.BA:2 - Solution

Start with one intended architecture use, not with the available tool outputs. Name the exact built asset and recover the actual subject-relation occurrences and exact selected A.22 structures that matter. Cite an obtaining `ArchitectureRelation` only when its C.30 predicate holds; otherwise keep required, desired, expected, candidate, negative, or unresolved content in a bounded `ArchitectureClaim`.

Constitute each architecture description under C.2.1 about exactly one EntityOfConcern: the built asset, one obtaining `ArchitectureRelation` occurrence, or one exact selected structure. Keep its exact ClaimGraph and effective `U.ReferenceScheme` recoverable. The same episteme is a `U.View` only while a separately identified E.17.0 conformance relation to one exact viewpoint episteme obtains. Then recover reference designation, model exchange, source use, representation, publication, and currentness through their own objects and relations.

For a first controlled use, record only the references needed to make the next architecture move:

```text
BuiltAssetArchitectureDescriptionUse@Project:
  projectWorkOccurrenceRef?: U.EntityRef constrained to U.Work
  builtAssetDescriptionProjectUseRelationRef?: U.RelationRef governed by the exact description-use or work-use pattern
  architectureDescriptionRef: U.EpistemeRef constrained to ArchitectureDescription
  descriptionClaimGraphRef: U.ClaimGraphRef
  descriptionEntityOfConcernRef:
    exactly one builtAssetRef |
      ArchitectureRelation occurrence ref |
      selected U.Structure ref
  effectiveReferenceScheme: U.ReferenceScheme, byValue
  builtAssetRef: U.HolonRef
  architectureRelationOccurrenceRefs?: FinSet(U.RelationRef)
  architectureClaimRefs?: FinSet(U.EpistemeRef)
  selectedStructureRefs: FinSet(U.StructureRef)
  architectureStructuralViewRefs?: FinSet(U.EpistemeRef constrained to ArchitectureStructuralView)
  viewpointConformanceRelationRefs?: FinSet(EpistemeViewpointConformanceRelationRef)
  claimScope?: U.ClaimScope, byValue
  architectureConcernRefs?: FinSet(U.EpistemeRef)
  modelUseStructureRef?: U.StructureRef
  empiricalGroundingRelationRefs?: FinSet(U.RelationRef)
  referenceDesignationRelationRefs?: FinSet(U.RelationRef)
  assetInformationDescriptionRefs?: FinSet(U.EpistemeRef)
  digitalTwinDescriptionRefs?: FinSet(U.EpistemeRef)
  designRunSeparationUse?: BuiltAssetDesignRunSeparationUse, byValue
  sourceToUsePathRefs?: FinSet(U.RelationRef)
  sourceReturnCondition?:
  representationRefs?: FinSet(U.EntityRef)
  publicationOccurrenceRefs?: FinSet(EpistemePublicationRelationRef)
  publicationFormRefs?: FinSet(U.EntityRef)
  carrierRefs?: FinSet(U.EntityRef)
  descriptionFreshnessClaimRefs?: FinSet(U.EpistemeRef)
  publicationCurrentnessRelationRefs?: FinSet(U.RelationRef)
  admissibleUse:
  nextGoverningPatternApplicationRef:
  nonAdmissibleUse:
```

This is a project-side use record, not a description identity constructor or a new root kind. `@Project` is a compatibility and retrieval cue and establishes no project entity, Work occurrence, authority, context, viewpoint, parthood, or use relation. When the use is genuinely local to one actual project, `projectWorkOccurrenceRef` identifies the exact composite `U.Work`, and `builtAssetDescriptionProjectUseRelationRef` identifies the separately governed obtaining relation by which this description use concerns that Work. Otherwise both remain absent.

`architectureDescriptionRef` resolves to one exact C.2.1 episteme whose identity is the cited ClaimGraph, one exact `descriptionEntityOfConcernRef`, and effective reference scheme. If that EntityOfConcern is the built asset, it is exactly `builtAssetRef`. If it is an architecture-relation occurrence or selected structure, its exact participants or selection trace recover `builtAssetRef` without deriving identity from an optional architecture claim. `architectureClaimRefs` carry bounded claim content or trace only.

Every value in `architectureStructuralViewRefs` identifies an exact description episteme admitted as `U.View` only through an independently obtaining `EpistemeViewpointConformanceRelation` to one exact viewpoint. It can be the same episteme as `architectureDescriptionRef` only when that description's one EntityOfConcern is the selected structure required by C.30.ASV; otherwise it is a separately identified description episteme connected through an explicit description-set use or correspondence claim or independently obtaining relation. A multi-view use can cite several such description/view epistemes; the use record, collection, file, bundle, list order, or publication creates neither their identities nor their conformance.

`claimScope`, architecture concern, empirical grounding, and `modelUseStructureRef` remain neighboring qualifiers or relations. A DDD-style bounded-model-use structure appears only when that independently selected structure changes interpretation or selection for this use. It replaces none of the asset, relation, structure, description, scheme, scope, grounding, viewpoint, Work, or project-use objects and is absent from base identity.

Use `sourceToUsePathRefs` when a model publication, exchange, measurement description, or other named expression enters the present architecture use. Use a source-return condition only when stronger use of a derivative or reused description must return to that named source or governing pattern. Keep a diagram or model as representation, and keep publication occurrence, form, and carrier separate. Use `G.11` when description freshness, publication currentness, edition, telemetry freshness, model decay, or synchronization currentness is the claim; none establishes architecture adequacy or empirical grounding by itself.

When ISO 19650 discipline is invoked, cite the exact published part and edition rather than an unversioned series label. At the `2026-07-31` source check, ISO lists `ISO 19650-1:2018`, Edition 1, and `ISO 19650-3:2020`, Edition 1, as published editions last confirmed in 2024 and now to be revised, with draft successors under development. The current transfer is therefore exact and bounded: Part 1 contributes whole-life information-management discipline for exchanging, recording, versioning, and organizing information; Part 3 contributes the operational-phase management process and information exchanges. Record the exact standard source and edition in the source-to-use path, the used model or information edition, the reference date and validity window through the currentness loci, the refresh or source-return condition, and `admissibleUse` and `nonAdmissibleUse`. A draft or later edition does not silently replace the cited source. ISO 19650 practice contributes information-management discipline, not FPF ontology, subject-relation truth, architecture adequacy, evidence sufficiency, assurance, Work occurrence, or authority.

#### C.30.AD.BA:2.1 - Recover the selected structures before combining views

For every included view, state the exact candidate description episteme, its selected-structure EntityOfConcern, the architecture concern for which it is used, the exact viewpoint episteme, and the obtaining E.17.0 conformance occurrence. A geometry or coordination model can expose several structures, but the file boundary does not select one structure or grant view membership on the engineer's behalf.

| Encountered description | First recover | Architecture-description use |
| --- | --- | --- |
| Spatial model | Spatial containment, placement, access, or separation structure under its direct relation pattern. | Cite the exact description episteme, selected structure, viewpoint, and conformance occurrence for the exact built asset. |
| Functional or flow model | Required or desired effect claims, functional structure, selected transformation-flow structure, ports, and interfaces under `A.6.F`, `E.18`, or `C.30.TFS-REL`; an actual transformation only under A.3.4. | Keep required content, selected flow organization, actual change, and the description/view use distinct; record correspondence or positive co-reference only when its direct predicate obtains. |
| Product or equipment model | Module claim or admitted module relation, component, interface, allocation, or placement relations under `A.6.M` and their direct governing patterns. | Keep the physical asset parts distinct from the description elements, representations, and publications that refer to them. |
| Control or operational model | Exact selected control structure under `C.30.LCA`, together with direct control, measurement, Work, and currentness relations. | Cite the control description/view without treating live values, a dashboard, or the LCA diagram as architecture adequacy or proof. |
| Cost, schedule, operation, maintenance, sustainability, or energy view | The exact description episteme and selected structure; then any measurement-result episteme for a claimed Characteristic under `C.16`, operation or maintenance Work under `A.15`, positive temporal aspect under `C.27.TA` or action-guiding temporal claim under `C.27`, causal use of an intervention, maintenance action, simulation, telemetry change, or claimed effect under `C.28`, and evidence, reliance, or assurance under `A.10` or `B.3`. | Keep the description or view, measured Characteristic, Work, temporal aspect or claim, causal-use question and verdict, currentness boundary, evidence, and assurance distinct; cite its source-to-use path and `G.11` validity or reopen condition. |

This last row is a distinct recognition-and-routing branch, not a new auxiliary-view kind and not a claim that every such description is an architecture structural view. Admit one as `U.View` only through the same exact selected-structure EntityOfConcern, viewpoint, and independently obtaining E.17.0 conformance required of every other view; return each embedded claim to the owner named in the row.

A single IFC publication may carry source descriptions for several rows. Conversely, one selected structure may be the EntityOfConcern of several descriptions and may be represented or published several times. `C.30.AD.BA` therefore keys each use to exact description identity, selected structure, view conformance, built-asset trace, and declared use rather than to a file, platform, package, or view count.

#### C.30.AD.BA:2.2 - Recover a reference designation as a relation

A reference designation is useful because it makes information about an entity retrievable under an explicit structuring and designation scheme. First recover the exact designation or reference relation through its direct representation/reference/naming owner. `C.30.AD.BA` records only its built-asset architecture-description use; a code, field, repeated string, list row, or the record below neither admits a relation kind nor makes an occurrence obtain. If no current direct owner supplies the needed relation, keep the designation use as bounded C.2.1 claim content; apply `A.6.RCD` only when a named repeated receiving use genuinely needs a reusable predicate definition or admitted direct relation.

```text
BuiltAssetReferenceDesignationUse:
  designationValue: local designation value, byValue
  referenceDesignationScheme: U.ReferenceScheme, byValue
  designatedEntityRef: U.EntityRef
  selectedAspectStructureRef: U.StructureRef
  designationOrReferenceRelationRef?: U.RelationRef
  qualificationWindow:
  correspondingEntityRef?: U.EntityRef
  correspondenceClaimOrRelationRef?: U.EpistemeRef | U.RelationRef
  admissibleUse:
  nonAdmissibleUse:
```

`selectedAspectStructureRef` names the exact structure in which the designation is interpreted, such as a functional, product, location, or declared local structure. It is not a free aspect label. `designatedEntityRef` names the entity designated in that structure. The direct relation ref is affirmative only when its own owner admits that kind and the occurrence independently obtains. If a design object and a realized component both need to be retrieved, name the two entities and a bounded correspondence claim or independently obtaining correspondence relation rather than letting one code silently collapse them.

The designation use permits retrieval and cross-description coordination. Part-whole, function, location, identity across aspects, and evidence claims still come from their direct relations or claim owners. Repeated appearance of the same designation expression is insufficient to merge referents when the scheme, selected structure, local sense, or qualification window differs.

#### C.30.AD.BA:2.3 - Keep exchange checking distinct from architecture evaluation

An IFC exchange or another machine-readable model is a representation and publication of one or more epistemes. Its schema relations can preserve valuable source structure. Before using it as architecture-description content:

1. identify every source episteme used, its representation, and the publication occurrence, form, and carrier;
2. recover the exact actual subject-relation occurrences and A.22 selected structures represented by the relation data being used;
3. record the source-to-use path into the exact architecture description or view episteme;
4. state the admissible architecture use and any lost, inferred, unknown, stale, or unavailable relation content.

A computer-interpretable exchange specification can evaluate whether declared information is present and shaped as specified. That evaluation concerns the exchange description or publication. It does not make schema relation data obtain in the built asset, constitute a selected structure, grant `U.View` membership, establish description truth, or show that the selected architecture is adequate for the asset's functions, constraints, or architectural characteristics. Apply the architecture, characteristic-evaluation, evidence, and assurance patterns for those claims.

#### C.30.AD.BA:2.4 - Keep a digital-twin description coupled without merging its objects

The phrase *digital twin* can cover a model episteme, software system, sensor systems, telemetry epistemes, simulation methods, operational Work, interfaces, representations, and publications. Recover each current object by its direct kind and relation. `C.30.AD.BA` uses only the exact descriptions and views that contribute to the built asset's architecture-description use.

When one declared architecture-description use crosses design-side and run-side material, fill the optional local carrier named by `designRunSeparationUse`:

```text
BuiltAssetDesignRunSeparationUse:
  designSideDescriptionRefs: FinSet(U.EpistemeRef)
  runSideDescriptionRefs: FinSet(U.EpistemeRef)
  designSideWorkOccurrenceRefs?: FinSet(U.EntityRef constrained to U.Work)
  runSideWorkOccurrenceRefs?: FinSet(U.EntityRef constrained to U.Work)
  telemetryEpistemeRefs?: FinSet(U.EpistemeRef)
  sourceToUsePathRefs: FinSet(U.RelationRef)
  descriptionFreshnessClaimRefs?: FinSet(U.EpistemeRef)
  publicationCurrentnessRelationRefs?: FinSet(U.RelationRef)
  designToRealizationCorrespondenceClaimOrRelationRefs?:
    FinSet(U.EpistemeRef | U.RelationRef)
  directCouplingRelationRefs?: FinSet(U.RelationRef)
  actualTransformationRefs?: FinSet(U.EntityRef constrained to U.Transformation)
  classificationBasis:
  admissibleCrossLifecycleUse:
  blockedMerge:
```

This is a by-value classifier for one built-asset description use, not a new FPF kind, a generic tag, or a relation constructor. `designSideDescriptionRefs` cite exact epistemes used for intended, required, proposed, or design-state material; `runSideDescriptionRefs` cite exact as-built, observed, operating, inspection, or maintenance-state epistemes. The classification is local to the declared use, not intrinsic to an episteme. If one publication carries both, identify the exact description or ClaimGraph loci before classifying them; the publication boundary does not perform the split.

Every referenced object and relation keeps its direct owner. C.2.1 governs description identity; `A.15` governs each exact `U.Work`; `G.11` governs freshness, currentness, and decay; the exact source-use owner governs each source path; the direct correspondence or coupling owner governs an affirmative relation; and `A.10` or `B.3` governs reliance or assurance. `C.28` governs a causal use of telemetry, simulation, maintenance, or a claimed physical or energy change; `C.27` continues to govern the temporal adequacy of the change statement. A.3.4 governs an actual physical transformation only when the exact changed referent, boundary, conditions, before/during/after facts, and continuity or reidentification basis are complete. A required or desired effect, live value, simulation result, control-view row, or local design/run classification is not that actual transformation. The local carrier owns only which already identified references participate on each side of this one cross-lifecycle use. Its nested source and currentness refs must resolve to the same exact refs cited by the enclosing use record, not duplicate or replace them. When an exact side, source path, Work occurrence, currentness boundary, or required direct relation cannot be recovered, state that gap in `blockedMerge` and narrow or block the cross-lifecycle use.

| Local anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Design/run collapse | A design description, realized asset description, telemetry episteme, operation or maintenance Work, and physical change are treated as one because a platform links or displays them together. | Fill `BuiltAssetDesignRunSeparationUse` with the exact side-specific descriptions, Work, sources, and currentness refs; cite correspondence, coupling, or transformation only under its direct owner, or block the merged use. |
| Lifecycle view merge | Original design, as-built model, operation record, maintenance Work, and an alleged transformation are merged because one dashboard presents them as one lifecycle view. | Keep each existing object and relation reference explicit; actual change enters only through A.3.4, and identity, parthood, evidence, assurance, or architecture adequacy is never inferred from co-display. |

The twin's coupling to the asset establishes neither parthood nor identity between the digital and physical objects. Connection, synchronization, rendering, bundling, and publication also establish neither architecture relation, selected structure, description truth, empirical grounding, view membership, evidence sufficiency, assurance, gate passage, Work, nor project-use relation.

A green twin, dashboard, exchange result, or release screen is therefore a cue, not gate passage. `A.21` becomes current only when an actual `OperationalGate(profile)` consumes declared `GateCheckRef`s and publishes `GateDecision` plus `DecisionLogRef`; if that relation is absent, keep the display as a cue and route any evidence, work-entry readiness, assurance, Work, or neighboring claim to `A.10`, `A.15.5`, `B.3`, `A.15.1`, or its exact direct governor. Even `GateDecision=pass` establishes neither release, readiness, permission, authorization, nor performed Work.

Recover the release-looking claim before routing it. An actual release action is one exact `A.15.1` `U.Work` occurrence; work-entry readiness is `A.15.5`; a non-prohibition, granted permission, permission exercise, non-violation, or permission conflict is `A.2.8.PER`; an instituting or revoking grant act is `A.2.9`. A further claim that a subject was released needs its named subject predicate and participants; if they cannot be recovered, keep the display as a cue and return `A.6.RCD missing-governor`. No current model, source, gate result, dashboard, or the word *authorized* supplies one of these relations by appearance.

**Currentness and smallest reopen.** When a decisive input changes, reopen only the built-asset description-use locus and conclusion that depend on it. A changed asset or selected structure reopens the dependent description identity, built-asset trace, or structural-view use; changed view conformance reopens that one view admission; a changed designation scheme, referent, or qualification window reopens only its `BuiltAssetReferenceDesignationUse`; a changed source, model, publication, or telemetry edition or freshness/fidelity boundary reopens its exact source-to-use or currentness locus; changed design/run classification, cited Work, source/currentness ref, correspondence, coupling, or transformation reopens only the affected `BuiltAssetDesignRunSeparationUse` and dependent admissible cross-lifecycle use; and a changed project-use relation or direct governor reopens only that exact relation reference and dependent admissible-use conclusion. Update the affected description, designation, design/run, or currentness locus; when the required input cannot be recovered, narrow or block only that use while unrelated views, descriptions, designations, and uses stay closed.

