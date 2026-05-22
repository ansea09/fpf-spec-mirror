---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:4"
section_title: "Solution - U.ViewpointBundleLibrary"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__005_solution-u-viewpointbundlelibrary.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:4 — Solution - U.ViewpointBundleLibrary"
line_start: 55836
line_end: 55896
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

`E.17.1` introduces `U.ViewpointBundleLibrary` as the reusable catalogue object for reusable viewpoint families. The library is a catalogue object: it packages named bundles of `U.Viewpoint` values and related metadata, but it does not define new kernel episteme kinds, new surfaces, or new publication carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** via `ViewFamilyId`;
- **which `U.Viewpoint` values belong to that family;**
- **under what entity-of-interest class and edition discipline** the family is valid.

This lets `U.MultiViewDescribing` import a finite viewpoint family from a stable catalogue object instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - `U.ViewpointBundleLibrary` (library object)

A `U.ViewpointBundleLibrary` is a catalogue of viewpoint bundles with at least:

- `libraryId : LibraryId`
- `editionId : EditionId`
- `bundles : FinSet(U.ViewpointBundle)`
- optional governance metadata such as responsibility role assignment, change-control note, or scope tags

Normative constraints:

1. Within one library edition, each `ViewFamilyId` **SHALL** be unique.
2. Libraries **SHALL NOT** define new kernel episteme kinds or surface kinds.
3. Libraries **MAY** be specialized as core FPF libraries or organization-local extensions that preserve the same bundle discipline.

#### E.17.1:4.3 - `U.ViewpointBundle` and `ViewFamilyId`

A `U.ViewpointBundle` is a finite, non-empty family of compatible `U.Viewpoint` values packaged for reuse.

Minimal structure:

- `viewFamilyId : ViewFamilyId`
- `EoIClassSpec <: U.Entity`
- `viewpoints : FinSet(U.Viewpoint)`
- optional `ArchetypalCards : FinSet(U.ArchetypalGroundingRef)`
- optional `AlignmentNotes` for ISO 42010 or domain-standard correspondences
- optional typed annex references for lexical, bridge, routing, example, or SoTA support material

`ViewFamilyId` names the bundle. It does **not** name a `U.View`, a publication face, or a file-system surface.

#### E.17.1:4.4 - Import discipline into `U.MultiViewDescribing`

When a `U.MultiViewDescribing[EoIClass]` family declares a `ViewFamilyId`:

- its finite viewpoint family `Sigma` **SHALL** be a subset of the referenced bundle's `viewpoints`;
- every D/S episteme in the family **SHALL** use `viewpointRef` values drawn from that imported family;
- every associated `U.View` **SHALL** preserve viewpoint attribution rather than silently retyping or relabeling the imported viewpoints.

If more than one bundle is used, the family shall make the partition explicit rather than relying on unnamed mixture.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- `ViewFamilyId` is a lexical family id, not a surface kind.
- Engineering viewpoint ids and publication viewpoint ids may coexist, but they **SHALL** remain disambiguated.
- Bundle semantics come from the owned `U.Viewpoint` definitions, not from the spelling pattern of the family id.

