---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:4"
section_title: "Solution - one catalogue episteme with local bundle declarations"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__005_solution-one-catalogue-episteme-with-local-bundle-declarations.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:4 — Solution - one catalogue episteme with local bundle declarations"
line_start: 113199
line_end: 113309
dependencies:
  - "A.16.0"
  - "A.22"
  - "A.6.2-A.6.4"
  - "A.6.3.RT"
  - "A.6.3.RT.OE"
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

`E.17.1` defines a reusable form for one ordinary C.2.1 catalogue episteme L whose local bundle declarations package `U.ViewpointRef` values resolving to E.17.0 viewpoint episteme editions. L, a declaration claim block within L, its ordinary family designator, each reference, each viewpoint designator, and P remain distinct. Neither the catalogue nor a declaration redefines viewpoint identity or membership, grants `U.View` membership, or creates publication forms and carriers.

#### E.17.1:4.1 - Core role

A conforming viewpoint-bundle library makes three things explicit:

- **which family is being named,** by an ordinary family designator interpreted under `R_L`;
- **which `U.ViewpointRef` members resolve to the viewpoint episteme editions packaged by that family;**
- **which target-kind compatibility condition and catalogue-edition discipline constrain the family.**

This lets `MultiViewDescribing` import a finite viewpoint family from a stable catalogue `U.Episteme` instead of restating it ad hoc in every local description family.

#### E.17.1:4.2 - Reuse an admitted catalogue; open full constitution only when needed

**Existing-catalogue route.** Resolve the already admitted catalogue edition L, retrieve the local declaration by its family designator under L's effective `R_L`, and resolve only the member references needed now. Do not reconstruct L's complete C.2.1 constitution merely to import an admitted edition.

Open the complete constitution below for the affected catalogue edition when authoring or admitting a new L, when the identity of L or its edition, or the resolution of a reference, is disputed, or when a named later use needs the catalogue's ClaimGraph, subject, or scheme as inspectable premises. Reuse an existing check while that edition, its effective scheme, and the relied-on premises stay unchanged. The complete constitution has three participants:

- `G_L : NonemptyClaimContent` is the catalogue's complete interpreted claim content (`ClaimGraph`), stating its scope, local family declarations, referenced viewpoint editions, target-kind compatibility conditions, and edition-change rule.
- `K_L` is the catalogue subject: the independently identified finite C.13 collection of already admitted viewpoint episteme editions whose recurring reuse groupings L describes. Its collection identity, members, obtaining membership relations, and identity rule are established before L. Neither the catalogue nor a declaration creates them.
- `R_L : EpistemeInterpretationScheme` is the effective rule collection under which the catalogue's ordinary library, edition, and family designators resolve; each `U.ViewpointRef` resolves to P; target-kind criteria and compatibility claims are interpreted; and reference, omission, provenance, and edition-change rules are read. C.2.1:4.1.2 supplies both ranges; the catalogue requires the full content and rule coverage stated here.

An eligible replacement for `R_L` must also resolve the catalogue’s designators and interpret its criteria. Range membership alone supplies neither result. A missing rule leaves the affected retrieval or compatibility judgement unresolved. Each referenced P retains its own effective scheme and E.17.0 membership. Resolving its reference under `R_L` does not transfer the catalogue's scheme to P.

`EpistemeConstitutionRelation(G_L, K_L, R_L)` must obtain. The participant-determined triple `<G_L, K_L, R_L>` identifies catalogue episteme L. If a proposed catalogue has only a file, label, list, or card but lacks an identifiable `K_L` or an effective `R_L`, stop. L has not yet been constituted.

`G_L` makes at least these claims recoverable:

- one ordinary library designator and one ordinary edition designator interpreted under `R_L`;
- a finite set of local family-declaration claim blocks, each retrievable inside `G_L` by one ordinary family designator interpreted under `R_L`;
- the `U.ViewpointRef` members and target-kind compatibility claim for each declaration; and
- only maintenance claims currently needed, using the branch that matches the present claim:
  - for a current maintenance-System claim, cite the admitted maintenance `U.System`; cite a local system-role kind and its independently evaluated classification only when that classification is current;
  - for actual maintenance Work, recover the actual performer through A.13 and let A.15.1 independently admit the dated `U.Work`. Add F.6 only when the catalogue claim or receiving use expressly relies on precise assignment-bound attribution through the same obtaining A.13 assignment. F.6 identifies neither assignment nor performer. Missing or failed F.6 alone leaves independently admitted Work intact. A short catalogue claim may omit identifiers its bounded use does not need;
  - for current maintenance responsibility, cite its direct admitted predicate and actual participants or return the missing governor; assignment establishes no responsibility; and
  - for prospective maintenance guidance, retain only the change-control note, intended maintenance condition or `U.WorkPlan`, and scope tag; this content asserts no performed Work, current assignment, or responsibility.

The catalogue entry cites these values. Their definitions or constraints come from elsewhere, and the entry creates none of them.

Library, edition, and family designators are lexical values under `R_L`, not local ValueKinds, public U-kinds, episteme identity discriminators, or entities by spelling. A local family declaration is claim content in `G_L`, not by itself a separate entity or episteme. Its compact locator `<editionDesignator(L), familyDesignator>` is a retrieval aid under `R_L`; it does not replace L's C.2.1 identity.

If a receiving use needs one declaration as a separately identified episteme, constitute that new episteme independently under C.2.1 rather than inferring it from a row.

Normative constraints:

1. Within one `G_L`, every family designator **SHALL** retrieve exactly one local declaration claim block under `R_L`.
2. A catalogue **SHALL NOT** define new kernel episteme kinds, id kinds, reference kinds, or publication-face/form kinds merely to type its fields.
3. A catalogue **MAY** be a core FPF catalogue or an organization-local extension when the same constitution, resolution, and family-declaration discipline remains recoverable.

#### E.17.1:4.3 - Local bundle declaration and its ordinary family designator

A bundle declaration is a bounded claim block inside `G_L`. It states one finite, non-empty recurring family of `U.ViewpointRef` values resolving to members of catalogue subject `K_L`. Under `R_L`, each reference resolves to one viewpoint episteme edition P already admitted to `U.Viewpoint` membership under E.17.0. The declaration neither admits P nor changes P's C.2.1 identity.

Its minimum claim content is:

- one ordinary `familyDesignator`, unique within `G_L` under `R_L`;
- one target-kind compatibility condition: either the by-value criterion used for this family or a reference that resolves to the ClaimGraph defining or constraining the admitted target kind. If member viewpoints use different fixed target-kind criteria, the declaration states the compatibility rule rather than inventing a common superclass token;
- `viewpointRefs`, one finite non-empty set of `U.ViewpointRef` values;
- optional references that resolve under their applicable schemes to archetypal-grounding examples or sections, with their intended recognition use stated;
- optional alignment claims naming the source and relation when a correspondence is asserted; and
- optional references that resolve under their applicable schemes to annex assets, each with its local role such as lexical note, Bridge material, A.16 move-publication note, example, or SoTA companion.

The family designator retrieves the declaration claim block inside L. A member `U.ViewpointRef` resolves to its P edition, and any reader-facing viewpoint token is only P's designator. The family designator, declaration claim block, reference, viewpoint designator, P, and L are distinct. No token, list position, prefix, alias, or member spelling substitutes for an episteme or reference.

The compatibility condition neither selects an actual EntityOfConcern for a describing use nor supplies or changes any member P's fixed target-kind criterion. Those claims remain in P and E.17.0 conformance.

A bundle is not a bundle of views, files, forms, carriers, or publication occurrences. If a receiving use needs an A.22 structure among the member viewpoints, it separately recovers obtaining relations and selects that structure. Declaration adjacency or order is not structure.

Changing the member-reference set, family meaning, compatibility condition, or the interpretation supplied by `R_L` changes `G_L` or the effective scheme and therefore identifies another catalogue episteme. Repackaging, annex layout, publication form, carrier, or audience does not reidentify unchanged L or any unchanged member viewpoint episteme.

#### E.17.1:4.4 - Import discipline into `MultiViewDescribing`

When you name a family designator for a describing use, resolve catalogue edition L and its effective `R_L`, retrieve the designated declaration inside `G_L`, then name the imported reference subset `Sigma`. If L or the declaration is not already recoverable, use §4.2 to establish `<G_L, K_L, R_L>` before import:

- `Sigma` is a subset of that declaration's `viewpointRefs` in L;
- every member is a `U.ViewpointRef` resolving to one admitted viewpoint episteme edition P;
- every candidate episteme E used under a member is independently identified under C.2.1 and is a `U.View` only when `EpistemeViewpointConformanceRelation(E,P)` obtains; and
- every one-viewpoint selection for one describing use carries a single `viewpointRef`; importing the family neither selects P for that use nor establishes conformance.

A local subset names catalogue edition L, the source family designator, and the member references actually used, and identifies omitted members as unused or intentionally excluded.

A multi-library use preserves each `<editionDesignator(L), familyDesignator>` source and member provenance rather than flattening everything into one unnamed family. If one use selects several viewpoints, it constructs their C.13 collection with membership. It does not overload one reference or infer a new family from adjacency.

Construction, identity viewing, transformation, declaration membership, selection, naming, rendering, or publication grants neither `U.Viewpoint` nor `U.View` membership.

A local overlay may add didactic or publication material without changing L. Changing a member viewpoint's meaning, the reference target, membership set, or family meaning requires a new local catalogue edition carrying the revised or new family declaration rather than silent mutation under the inherited family designator.

#### E.17.1:4.5 - Guard and naming discipline

- A viewpoint bundle is a family of **viewpoints**, not a bundle of views or documents.
- The family designator is an ordinary lexical value under `R_L`, not a local id kind, publication-face/form kind, reference, or entity.
- Engineering viewpoint designators and publication viewpoint designators may coexist, but their namespaces **SHALL** remain disambiguated.
- Bundle semantics come from the viewpoint episteme editions resolved by its member references, not from the spelling pattern of the family designator.

#### E.17.1:4.6 - Publication and representation stay outside the bundle

A published library is the same selected C.2.1 episteme edition participating in E.24.PUB relations:

- `PublicationExpressionRelation` relates that selected edition, one independently identified expression, and one bounded-use declaration;
- `PublicationExpressionBearingRelation` relates one independently identified physical or digital carrier to that expression;
- `PublicationFormConformanceRelation` relates the expression to any selected reusable publication form whose rules it satisfies; and
- `EpistemePublicationRelation` relates the selected edition, audience declaration, bounded-use declaration, expression, and carrier for one maximal continuous availability interval.

When form-mediated expression and bearing are claimed, retain E.24.PUB's corresponding relations with the same expression as witness. A change of exact publication need not interrupt broader availability of the library through its permitted expressions and carriers.

Changing a participant or restoring availability after a gap yields another publication occurrence under E.24.PUB; it does not reidentify unchanged L or any member viewpoint.

Rendering, printing, or uploading is separate system-performed `U.Work`. For a diagram or catalogue rendering, recover the correspondence between its elements and independently identified declarations or viewpoint epistemes. Use A.6.3.RT/A.6.3.RT.OE when constructing an expression or changing its representation scheme. Add C.29 when choosing or using a mathematical representation raises an inference or transfer question. Publication, representation, form, carrier, or rendering grants no viewpoint or view membership and makes no represented world-side relation obtain.

