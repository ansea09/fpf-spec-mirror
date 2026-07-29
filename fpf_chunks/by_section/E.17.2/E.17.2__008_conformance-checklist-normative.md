---
chunk_kind: "child"
pattern_id: "E.17.2"
pattern_title: "TEVB - Typical Engineering Viewpoints Bundle"
section_id: "E.17.2:6"
section_title: "Conformance checklist  (normative)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.2/E.17.2__008_conformance-checklist-normative.md"
commit_sha: "2ada413629b846ef308222d16489a82cb5b40a71"
heading_path:
  - "E.17.2 — TEVB - Typical Engineering Viewpoints Bundle"
  - "E.17.2:6 — Conformance checklist  (normative)"
line_start: 79040
line_end: 79080
dependencies:
  - "A.1"
  - "A.15"
  - "A.2"
  - "A.2.1"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.18"
  - "F.18"
  - "U.MultiViewDescribing"
  - "U.ViewpointBundleLibrary"
keywords:
---

### E.17.2:6 - Conformance checklist  *(normative)*

**CC‑TEVB‑1 (Bundle identity).**
Any artefact claiming to be “TEVB engineering viewpoints” must:

* refer to `viewFamilyId = VF.TEVB.ENG`,
* have `EntityOfConcernClassSpec = {h : U.Holon | HolonKind(h) ∈ {System, Episteme}}`,
* enumerate `viewpoints = {VP.Functional, VP.Procedural, VP.AllocationResponsibility, VP.ModuleInterface}` and no others.

**CC‑TEVB‑2 (Viewpoint definition).**
Each `VP.*` viewpoint must be a well‑formed `U.Viewpoint` per E.17.0:

* `viewpointId` equal to one of the four engineering IDs,
* `EntityOfConcernClassSpec` equal to the bundle’s,
* `StakeholderFamilies`, `Concerns`, `AllowedEpistemeKinds`, `ConformanceRules` explicitly declared.

**CC‑TEVB‑3 (DescriptionContext completeness).**
Every Description episteme or specification-use case participating in a TEVB‑managed multi‑view family for a holon must have a `DescriptionContext = ⟨EntityOfConcernRef, BoundedContextRef, ViewpointRef⟩` with:

* `EntityOfConcernRef` referencing a `U.System` or `U.Episteme`,
* `ViewpointRef ∈ {VP.Functional, VP.Procedural, VP.AllocationResponsibility, VP.ModuleInterface}`,
* `BoundedContextRef` pointing to the engineering context (E.10.D1).

Capability, Method, procedure terms, control-logic terms, role-structure, structural-architecture, module, interface, and allocation terms in those descriptions are viewpoint concern and content unless the text explicitly declares an A.6.4 retargeting, KindBridge, and species-extension rule that changes `EntityOfConcernRef`.

**CC‑TEVB‑4 (Separation from PublicationVPs).**
`VP.*` identifiers from TEVB are engineering-viewpoint ids. They do not serve as MVPK publication-side viewpoint ids. Publication-side viewpoints are governed in MVPK and may **correspond** to TEVB engineering viewpoints through `CorrespondenceModel`, but they are separate symbols.

**CC‑TEVB‑5 (No Role coordinate in EntityOfConcern and Description-episteme boundary or specification use).**
TEVB-aligned descriptions and specification-use cases may reference stakeholder or audience families in `StakeholderFamilies`, and may use `VP.AllocationResponsibility` as the viewpoint id, but they must not add `Role`, `RoleAssignment`, or a `AllocationResponsibility` value as a characteristic in Description episteme or specification-use case signatures beyond what A.7, C.2.1, and E.10.D2 already provide. Work-facing role and holder claims stay in `A.2`, `A.2.1`, `A.15`, and Part F; TEVB just selects concerns.

**CC‑TEVB‑6 (Alignment with consumer viewpoint maps).**
When a pattern defines engineering viewpoint families named “Functional”, “Procedural”, “Allocation‑Responsibility (Device‑Structure)”, or “Module‑Interface” over the same `EntityOfConcernClass` and claims TEVB alignment (for example, the `E.18:5.12` transformation-flow viewpoint-family map), it must bind them to TEVB viewpoints as follows:

* “Functional” → `VP.Functional`,
* “Procedural” → `VP.Procedural`,
* “Allocation‑Responsibility (Device‑Structure)” → `VP.AllocationResponsibility`,
* “Module‑Interface” → `VP.ModuleInterface`.

Any deviation must be explicitly documented as a species‑level extension and must not reuse `VF.TEVB.ENG`.

