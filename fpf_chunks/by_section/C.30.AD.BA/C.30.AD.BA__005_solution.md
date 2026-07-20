---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__005_solution.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:2 — Solution"
line_start: 58703
line_end: 58754
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.27"
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
  - "E.17.1"
  - "E.17.2"
  - "E.24.PUB"
  - "F.18"
keywords:
---

### C.30.AD.BA:2 - Solution

Use a `BuiltAssetArchitectureDescriptionUseCard@Project` for the first controlled slice:

```text
BuiltAssetArchitectureDescriptionUseCard@Project:
  architectureClaimRef: ArchitectureOf@ContextRef
  describedHolonRef:
  boundedContextRef:
  builtAssetKindCue:
    facility | plant | bridge | campusBuilding |
    infrastructureAsset | productAsset | otherDeclared
  selectedStructureRefs:
  structureKindRefs:
  architectureStructuralViewRefs:
  referenceDesignationRefs?
  assetInformationRefs?
  digitalTwinViewRefs?
  publicationOrExchangeRefs?
  correspondenceRefs?
  sourceReturnCondition?
  DesignRunTagRefs?
  admissibleUse:
  nonAdmissibleUse:
  firstNeighborPatternApplication?
```

`@Project` guard: in this card name, `@Project` marks a project-side use card for first-pass built-asset architecture-description triage. It is not `U.Project`, not a bounded context, not project authority, and not a part-whole relation. If one of those claims is current, use the governing project, context, authority, or part-whole pattern named by value.

Expand to `BuiltAssetArchitectureDescription@Context` only when durable description use is current:

```text
BuiltAssetArchitectureDescription@Context:
  architectureDescriptionRef: ArchitectureDescription@ContextRef
  architectureClaimRef: ArchitectureOf@ContextRef
  describedBuiltAssetRef: U.HolonRef
  boundedContextRef: U.BoundedContextRef
  viewSetRefs:
  referenceDesignationSchemeRefs:
  assetInformationModelRefs:
  digitalTwinDescriptionRefs:
  exchangeOrPublicationRefs:
  sourceEpistemeRefs:
  correspondenceRefs:
  sourceReturnCondition:
  currentnessOrEditionBoundary:
  admissibleUse:
  nonAdmissibleUse:
```

`BuiltAssetArchitectureDescription@Context` is a specialization of `ArchitectureDescription@Context`. It is a Description episteme about `ArchitectureOf@Context`; it is not the built asset and not the architecture itself.

