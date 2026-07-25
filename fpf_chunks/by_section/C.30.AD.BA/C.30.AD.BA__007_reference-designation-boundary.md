---
chunk_kind: "child"
pattern_id: "C.30.AD.BA"
pattern_title: "Built-Asset Architecture Description and Reference Designation"
section_id: "C.30.AD.BA:4"
section_title: "Reference Designation Boundary"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.AD.BA/C.30.AD.BA__007_reference-designation-boundary.md"
commit_sha: "3bc659a6f866071f629bf41fc2dd41f2518e579a"
heading_path:
  - "C.30.AD.BA — Built-Asset Architecture Description and Reference Designation"
  - "C.30.AD.BA:4 — Reference Designation Boundary"
line_start: 59533
line_end: 59552
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

### C.30.AD.BA:4 - Reference Designation Boundary

A reference designation helps identify an object across aspect-sensitive descriptions. It does not prove that the functional object, product object, location object, property object, and activity-side object are one FPF entity in all uses. Recover the designation relation first:

```text
BuiltAssetReferenceDesignationUse@Context:
  designationRef:
  designationSchemeRef:
  designatedEntityRef:
  aspectOrViewRef:
  architectureClaimRef:
  selectedStructureRef?:
  correspondenceRefs?:
  sourceReturnCondition?:
  admissibleUse:
  nonAdmissibleUse:
```

Use the designation to coordinate descriptions. Do not use the designation code as part-whole proof, function proof, evidence sufficiency, assurance, gate passage, or decision authority by appearance.

