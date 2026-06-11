---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB — Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:6"
section_title: "Conformance checklist  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__007_conformance-checklist-normative.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "E.17.2 — TEVB — Typical Engineering Viewpoints Bundle"
  - "E.17.2:6 — Conformance checklist  (normative)"
line_start: 63765
line_end: 63805
dependencies:
  - "A.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "E.TGA"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:6 - Conformance checklist  *(normative)*

**CC‑TEVB‑1 (Bundle identity).**
Any artefact claiming to be “TEVB engineering viewpoints” MUST:

* refer to `viewFamilyId = VF.TEVB.ENG`,
* have `EntityOfConcernClassSpec = {h : U.Holon | HolonKind(h) ∈ {System, Episteme}}`,
* enumerate `viewpoints = {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}` and no others.

**CC‑TEVB‑2 (Viewpoint definition).**
Each `VP.*` viewpoint MUST be a well‑formed `U.Viewpoint` per E.17.0:

* `viewpointId` equal to one of the four engineering IDs,
* `EntityOfConcernClassSpec` equal to the bundle’s,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` explicitly declared.

**CC‑TEVB‑3 (DescriptionContext completeness).**
Every Description episteme or specification-use case participating in a TEVB‑managed multi‑view family for a holon MUST have a `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩` with:

* `EntityOfConcernRef` referencing a `U.System` or `U.Episteme`,
* `ViewpointRef ∈ {VP.Functional, VP.Procedural, VP.RoleEnactor, VP.ModuleInterface}`,
* `BoundedContextRef` pointing to the engineering context (E.10.D1).

Capability, Method, procedure/control, role-structure, structural-architecture, module, interface, and allocation terms in those descriptions are viewpoint concern/content unless the text explicitly declares an A.6.4 retargeting, KindBridge, and species-extension rule that changes `EntityOfConcernRef`.

**CC‑TEVB‑4 (Separation from PublicationVPs).**
`VP.*` identifiers from TEVB are engineering-viewpoint ids. They do not serve as MVPK publication-side viewpoint ids. Publication-side viewpoints live in MVPK and may **correspond** to TEVB engineering viewpoints through `CorrespondenceModel`, but they are separate symbols.

**CC‑TEVB‑5 (No Role coordinate in EntityOfConcern and Description-episteme boundary or specification use).**
TEVB-aligned descriptions and specification-use cases MAY reference `U.RoleEnactor` families in `StakeholderFamilies` but SHALL NOT add `Role` or `RoleEnactor` as characteristics in Description episteme or specification-use case signatures beyond what A.7 and E.10.D2 already provides. Role semantics stay in RoleEnactment patterns; TEVB just selects concerns.

**CC‑TEVB‑6 (Alignment with consumer viewpoint maps).**
When a pattern defines engineering viewpoint families named “Functional”, “Procedural”, “Role‑Enactor (Device‑Structure)”, or “Module‑Interface” over the same `EntityOfConcernClass` and claims TEVB alignment (for example, E.TGA E.18:5.12 viewpoint map), it MUST bind them to TEVB viewpoints as follows:

* “Functional” → `VP.Functional`,
* “Procedural” → `VP.Procedural`,
* “Role‑Enactor (Device‑Structure)” → `VP.RoleEnactor`,
* “Module‑Interface” → `VP.ModuleInterface`.

Any deviation MUST be explicitly documented as a species‑level extension and MUST NOT reuse `VF.TEVB.ENG`.

