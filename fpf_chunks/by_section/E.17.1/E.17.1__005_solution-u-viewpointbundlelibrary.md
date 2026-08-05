---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:4"
section_title: "Solution - U.ViewpointBundleLibrary"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__005_solution-u-viewpointbundlelibrary.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:4 — Solution - U.ViewpointBundleLibrary"
line_start: 79524
line_end: 79601
dependencies:
  - "A.16.0"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.13"
  - "C.2.1"
  - "C.2.2a"
  - "C.29"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "E.7"
  - "F.9"
  - "F.9.1"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:4 - Solution - `U.ViewpointBundleLibrary`

`E.17.1` governs `U.ViewpointBundleLibrary` as one reusable C.2.1 catalogue episteme whose named bundles package exact `U.ViewpointRef` values resolving to exact E.17.0 viewpoint episteme editions. Library, bundle, family id, reference, designator, and P remain distinct. Neither a library nor bundle redefines viewpoint identity or membership, grants `U.View` membership, or creates publication forms and carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** via `ViewFamilyId`;
- **which `U.ViewpointRef` members resolve to the exact viewpoint episteme editions packaged by that family;**
- **under what entity of concern class and edition discipline** the family is valid.

This lets `MultiViewDescribing` import a finite viewpoint family from a stable catalogue `U.Episteme` instead of restating it ad hoc in every local description family.

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

A `U.ViewpointBundle` is a finite, non-empty family of governed `U.ViewpointRef` values packaged for reuse. Every reference resolves to one exact viewpoint episteme edition that has already gained `U.Viewpoint` membership under E.17.0. The bundle neither admits P nor changes P's C.2.1 identity.

Minimal structure:

- `viewFamilyId : ViewFamilyId`;
- `EntityOfConcernClassSpec <: U.Entity`, used only as the compatibility constraint for the targets admitted by the member viewpoints;
- `viewpointRefs : FinSet(U.ViewpointRef)`;
- optional `ArchetypalCards : FinSet(U.ArchetypalGroundingRef)`;
- optional `AlignmentNotes` for exact ISO 42010 or domain-standard correspondence claims; and
- optional typed annex references for lexical, bridge, A.16 move-publication, example, or SoTA companion material.

`ViewFamilyId` designates the bundle. A member `U.ViewpointRef` resolves an exact P, and any `ViewpointId` exposed for readers is only P's designator. The family id, reference, designator, and episteme are distinct; no token, list position, prefix, alias, or member spelling substitutes for P.

The bundle constraint does not select an actual EntityOfConcern, supply P's fixed target-kind criterion, or judge a candidate episteme. Those claims remain in exact P and E.17.0 conformance. A bundle is not a bundle of views, files, forms, carriers, or publication occurrences. If a receiving use needs an A.22 structure among the member viewpoints, it separately recovers exact obtaining relations and selects that structure; bundle adjacency or order is not structure.

Changing the member-reference set, family meaning, or compatibility constraint requires another bundle edition. Repackaging, annex layout, publication form, carrier, or audience does not reidentify any unchanged member viewpoint episteme.

#### E.17.1:4.4 - Import discipline into `MultiViewDescribing`

When a describing use declares a `ViewFamilyId`, it identifies the exact library and bundle edition and then names the exact imported reference subset `Sigma`:

- `Sigma` is a subset of that exact bundle edition's `viewpointRefs`;
- every member is an exact `U.ViewpointRef` resolving to one admitted viewpoint episteme edition P;
- every candidate episteme E used under a member is independently identified under C.2.1 and is a `U.View` only when `EpistemeViewpointConformanceRelation(E,P)` obtains; and
- every actual one-viewpoint selection for one describing use carries one singular `viewpointRef`; importing the family neither selects P for that use nor establishes conformance.

A local subset names both the source `ViewFamilyId` and the member references actually used, while keeping omitted members visible as unused or intentionally excluded. A multi-bundle use preserves each exact source bundle edition and member provenance rather than flattening everything into one unnamed family. If one use selects several viewpoints, it constructs their exact governed C.13 collection; it does not overload one reference or infer a new family from adjacency.

Construction, identity viewing, transformation, bundle membership, selection, naming, rendering, or publication grants neither `U.Viewpoint` nor `U.View` membership. A local overlay may add didactic or publication material without changing the imported bundle. Changing a member viewpoint's meaning, the reference target, membership set, or family meaning requires a new local bundle or edition rather than silent mutation under the inherited id.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- `ViewFamilyId` is a lexical family id, not a publication-face/form kind.
- Engineering viewpoint ids and publication viewpoint ids may coexist, but they **SHALL** remain disambiguated.
- Bundle semantics come from the exact viewpoint episteme editions resolved by its member references, not from the spelling pattern of the family id.

#### E.17.1:4.6 - Publication and representation stay outside the bundle

A published library is the same selected C.2.1 episteme edition participating in exact E.24.PUB relations:

- `PublicationFormExpressionRelation` relates that selected edition, one exact publication form, and one exact bounded-use declaration;
- `PublicationFormBearingRelation` relates one exact `U.PresentationCarrier` and that form; and
- `EpistemePublicationRelation` relates the selected edition, audience declaration, bounded-use declaration, form, and carrier for one maximal continuous availability interval.

Changing a participant or restoring availability after a gap yields another publication occurrence under E.24.PUB; it does not reidentify an unchanged library, bundle, or member viewpoint. Rendering, printing, or uploading is separate system-performed `U.Work`. C.29 representation is separately governed when a diagram or catalogue rendering corresponds to independently recovered bundle objects. Publication, representation, form, carrier, or rendering grants no viewpoint or View membership and makes no world-side subject relation obtain.

