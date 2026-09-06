---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:4"
section_title: "Solution - one catalogue episteme with local bundle declarations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__005_solution-one-catalogue-episteme-with-local-bundle-declarations.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:4 — Solution - one catalogue episteme with local bundle declarations"
line_start: 82066
line_end: 82161
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
---

### E.17.1:4 - Solution - one catalogue episteme with local bundle declarations

`E.17.1` defines a reusable form for one ordinary C.2.1 catalogue episteme L whose local bundle declarations package exact `U.ViewpointRef` values resolving to exact E.17.0 viewpoint episteme editions. L, a declaration claim block within L, its ordinary family designator, each reference, each viewpoint designator, and P remain distinct. Neither the catalogue nor a declaration redefines viewpoint identity or membership, grants `U.View` membership, or creates publication forms and carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** via an ordinary family designator interpreted under exact `R_L`;
- **which `U.ViewpointRef` members resolve to the exact viewpoint episteme editions packaged by that family;**
- **which exact target-kind compatibility condition and catalogue-edition discipline constrain the family.**

This lets `MultiViewDescribing` import a finite viewpoint family from a stable catalogue `U.Episteme` instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - Reuse an admitted catalogue; open full constitution only when needed

**Existing-catalogue route.** Resolve the already admitted catalogue edition L, retrieve the local declaration by its family designator under L's effective `R_L`, and resolve only the member references needed now. Do not reconstruct L's complete C.2.1 constitution merely to import an admitted edition.

Open the complete constitution below for the affected catalogue edition when authoring or admitting a new L, when L or edition identity or reference resolution is disputed, or when a named later use needs the catalogue's ClaimGraph, subject, or scheme as inspectable premises. Reuse an existing check while that edition, its effective scheme, and the relied-on premises stay unchanged:

- `G_L` is the exact `U.ClaimGraph` that states the catalogue scope, the local family declarations, the referenced viewpoint editions, their target-kind compatibility conditions, and the edition-change rule;
- `K_L` is the exact catalogue subject: the independently identified finite C.13 collection of already admitted viewpoint episteme editions whose recurring reuse groupings L describes. Its collection identity, exact members, obtaining membership relations, and identity rule are established before L; neither the catalogue nor a declaration creates them; and
- `R_L : U.ReferenceScheme` is the exact effective scheme under which the catalogue's ordinary library, edition, and family designators resolve; each `U.ViewpointRef` resolves to exact P; target-kind criteria and compatibility claims are interpreted; and reference, omission, provenance, and edition-change rules are read.

`EpistemeConstitutionRelation(G_L, K_L, R_L)` must obtain. The participant-determined triple `<G_L, K_L, R_L>` identifies exact catalogue episteme L. If a proposed catalogue has only a file, label, list, or card but no truthful exact `K_L` or effective `R_L`, stop: L has not yet been constituted.

`G_L` makes at least these claims recoverable:

- one ordinary library designator and one ordinary edition designator interpreted under `R_L`;
- a finite set of local family-declaration claim blocks, each retrievable inside `G_L` by one ordinary family designator interpreted under `R_L`;
- the exact `U.ViewpointRef` members and target-kind compatibility claim for each declaration; and
- only maintenance claims currently needed, using the branch that matches the present claim:
  - for a current maintenance-System claim, cite the admitted maintenance `U.System`; cite an exact local system-role kind and its independently evaluated classification only when that classification is current;
  - for actual maintenance Work, recover the exact actual performer through A.13 and let A.15.1 independently admit the dated `U.Work`; add F.6 only when the catalogue claim or receiving use expressly consumes precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer, missing or failed F.6 leaves the Work intact, and a short catalogue claim may omit identifiers its bounded use does not need;
  - for current maintenance responsibility, cite its direct admitted predicate and actual participants or return the exact missing governor; assignment establishes no responsibility; and
  - for prospective maintenance guidance, retain only the change-control note, intended maintenance condition or `U.WorkPlan`, and scope tag; this content asserts no performed Work, current assignment, or responsibility.

The catalogue entry only cites these values, which are defined or constrained elsewhere and creates none of them.

Library, edition, and family designators are lexical values under `R_L`, not local ValueKinds, public U-kinds, episteme identity discriminators, or entities by spelling. A local family declaration is claim content in `G_L`, not automatically a separate entity or episteme. Its compact locator `<editionDesignator(L), familyDesignator>` is a retrieval aid under `R_L`; it does not replace L's C.2.1 identity. If a receiving use truly needs one declaration as a separately identified episteme, constitute that new episteme independently under C.2.1 rather than inferring it from a row.

Normative constraints:

1. Within one exact `G_L`, every family designator **SHALL** retrieve exactly one local declaration claim block under `R_L`.
2. A catalogue **SHALL NOT** define new kernel episteme kinds, id kinds, reference kinds, or publication-face/form kinds merely to type its fields.
3. A catalogue **MAY** be a core FPF catalogue or an organization-local extension when the same constitution, resolution, and family-declaration discipline remains recoverable.

#### E.17.1:4.3 - Local bundle declaration and its ordinary family designator

A bundle declaration is a bounded claim block inside exact `G_L`. It states one finite, non-empty recurring family of exact `U.ViewpointRef` values drawn from exact catalogue subject `K_L`. Every reference resolves under `R_L` to one exact viewpoint episteme edition P that has already gained `U.Viewpoint` membership under E.17.0. The declaration neither admits P nor changes P's C.2.1 identity.

Its minimum claim content is:

- one ordinary `familyDesignator`, unique within exact `G_L` under `R_L`;
- one exact target-kind compatibility condition: either the by-value criterion actually used for this family or a reference that resolves to the exact ClaimGraph defining or constraining the admitted target kind; if member viewpoints use different fixed target-kind criteria, the declaration states the exact compatibility rule rather than inventing a common superclass token;
- `viewpointRefs`, one finite non-empty set of exact `U.ViewpointRef` values;
- optional references that resolve under their applicable schemes to exact archetypal-grounding examples or sections, with their intended recognition use stated;
- optional alignment claims naming the exact source and relation when a real correspondence is asserted; and
- optional references that resolve under their applicable schemes to exact annex assets, each with its local role such as lexical note, Bridge material, A.16 move-publication note, example, or SoTA companion.

The family designator retrieves the declaration claim block inside exact L. A member `U.ViewpointRef` resolves exact P, and any reader-facing viewpoint token is only P's designator. The family designator, declaration claim block, reference, viewpoint designator, P, and L are distinct; no token, list position, prefix, alias, or member spelling substitutes for an exact episteme or reference.

The compatibility condition neither selects an actual EntityOfConcern for a describing use nor supplies or changes any member P's fixed target-kind criterion. Those claims remain in exact P and E.17.0 conformance. A bundle is not a bundle of views, files, forms, carriers, or publication occurrences. If a receiving use needs an A.22 structure among the member viewpoints, it separately recovers exact obtaining relations and selects that structure; declaration adjacency or order is not structure.

Changing the member-reference set, family meaning, compatibility condition, or the interpretation supplied by `R_L` changes `G_L` or the effective scheme and therefore identifies another catalogue episteme. Repackaging, annex layout, publication form, carrier, or audience does not reidentify unchanged L or any unchanged member viewpoint episteme.

#### E.17.1:4.4 - Import discipline into `MultiViewDescribing`

When a describing use names a family designator, it resolves exact catalogue edition L and its effective `R_L`, retrieves the declaration claim block designated inside `G_L`, and then names the exact imported reference subset `Sigma`. If exact L or the declaration is not already recoverable, use §4.2 to establish `<G_L, K_L, R_L>` before import:

- `Sigma` is a subset of that declaration's `viewpointRefs` in exact L;
- every member is an exact `U.ViewpointRef` resolving to one admitted viewpoint episteme edition P;
- every candidate episteme E used under a member is independently identified under C.2.1 and is a `U.View` only when `EpistemeViewpointConformanceRelation(E,P)` obtains; and
- every actual one-viewpoint selection for one describing use carries one singular `viewpointRef`; importing the family neither selects P for that use nor establishes conformance.

A local subset names exact catalogue edition L, the source family designator, and the member references actually used, while keeping omitted members visible as unused or intentionally excluded. A multi-library use preserves each exact `<editionDesignator(L), familyDesignator>` source and member provenance rather than flattening everything into one unnamed family. If one use selects several viewpoints, it constructs their C.13 collection with exact membership; it does not overload one reference or infer a new family from adjacency.

Construction, identity viewing, transformation, declaration membership, selection, naming, rendering, or publication grants neither `U.Viewpoint` nor `U.View` membership. A local overlay may add didactic or publication material without changing exact L. Changing a member viewpoint's meaning, the reference target, membership set, or family meaning requires a new local catalogue edition or family declaration rather than silent mutation under the inherited family designator.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- The family designator is an ordinary lexical value under `R_L`, not a local id kind, publication-face/form kind, reference, or entity.
- Engineering viewpoint designators and publication viewpoint designators may coexist, but their namespaces **SHALL** remain disambiguated.
- Bundle semantics come from the exact viewpoint episteme editions resolved by its member references, not from the spelling pattern of the family designator.

#### E.17.1:4.6 - Publication and representation stay outside the bundle

A published library is the same selected C.2.1 episteme edition participating in exact E.24.PUB relations:

- `PublicationFormExpressionRelation` relates that selected edition, one exact publication form, and one exact bounded-use declaration;
- `PublicationFormBearingRelation` relates one exact `U.PresentationCarrier` and that form; and
- `EpistemePublicationRelation` relates the selected edition, audience declaration, bounded-use declaration, form, and carrier for one maximal continuous availability interval.

Changing a participant or restoring availability after a gap yields another publication occurrence under E.24.PUB; it does not reidentify unchanged L or any member viewpoint. Rendering, printing, or uploading is separate system-performed `U.Work`. C.29 applies when a diagram or catalogue rendering represents independently recovered declarations or viewpoint epistemes. Publication, representation, form, carrier, or rendering grants no viewpoint or view membership and makes no represented world-side relation obtain.

