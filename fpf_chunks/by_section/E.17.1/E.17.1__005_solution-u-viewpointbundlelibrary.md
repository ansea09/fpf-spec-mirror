---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:4"
section_title: "Solution - U.ViewpointBundleLibrary"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__005_solution-u-viewpointbundlelibrary.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:4 — Solution - U.ViewpointBundleLibrary"
line_start: 69067
line_end: 69127
dependencies:
  - "A.16.0"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.7"
  - "F.9"
  - "F.9.1"
  - "U.MultiViewDescribing"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:4 - Solution - `U.ViewpointBundleLibrary`

`E.17.1` introduces `U.ViewpointBundleLibrary` as the reusable catalogue `U.Episteme` for reusable viewpoint families. The library is an episteme-record species: it packages named bundles of `U.Viewpoint` values and related metadata, but it does not define new kernel episteme kinds, new publication forms, or new publication carriers. A published library is a `U.EpistemePublication`, `PublicationUnit`, publication form, face, or carrier only through the usual E.17 publication relation positions.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** via `ViewFamilyId`;
- **which `U.Viewpoint` values belong to that family;**
- **under what entity of concern class and edition discipline** the family is valid.

This lets `U.MultiViewDescribing` import a finite viewpoint family from a stable catalogue `U.Episteme` instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - `U.ViewpointBundleLibrary` (catalogue episteme)

A `U.ViewpointBundleLibrary` is a catalogue `U.Episteme` of viewpoint bundles with at least:

- `libraryId : LibraryId`
- `editionId : EditionId`
- `bundles : FinSet(U.ViewpointBundle)`
- optional governance metadata such as responsibility role assignment, change-control note, or scope tags

Normative constraints:

1. Within one library edition, each `ViewFamilyId` **SHALL** be unique.
2. Libraries **SHALL NOT** define new kernel episteme kinds or publication-face/form kinds.
3. Libraries **MAY** be specialized as core FPF libraries or organization-local extensions that preserve the same bundle discipline.

#### E.17.1:4.3 - `U.ViewpointBundle` and `ViewFamilyId`

A `U.ViewpointBundle` is a finite, non-empty family of compatible `U.Viewpoint` values packaged for reuse.

Minimal structure:

- `viewFamilyId : ViewFamilyId`
- `EntityOfConcernClassSpec <: U.Entity`
- `viewpoints : FinSet(U.Viewpoint)`
- optional `ArchetypalCards : FinSet(U.ArchetypalGroundingRef)`
- optional `AlignmentNotes` for ISO 42010 or domain-standard correspondences
- optional typed annex references for lexical, bridge, A.16 move-publication, example, or SoTA companion material

`ViewFamilyId` names the bundle. It does **not** name a `U.View`, a publication face, or a file-system carrier.

#### E.17.1:4.4 - Import discipline into `U.MultiViewDescribing`

When a `U.MultiViewDescribing[EntityOfConcernClass]` family declares a `ViewFamilyId`:

- its finite viewpoint family `Sigma` **SHALL** be a subset of the referenced bundle's `viewpoints`;
- every Description episteme or specification-use case in the family **SHALL** use `viewpointRef` values drawn from that imported family;
- every associated `U.View` **SHALL** preserve viewpoint attribution rather than silently retyping or relabeling the imported viewpoints.

If more than one bundle is used, the family shall make the partition explicit rather than relying on unnamed mixture.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- `ViewFamilyId` is a lexical family id, not a publication-face/form kind.
- Engineering viewpoint ids and publication viewpoint ids may coexist, but they **SHALL** remain disambiguated.
- Bundle semantics come from the owned `U.Viewpoint` definitions, not from the spelling pattern of the family id.

