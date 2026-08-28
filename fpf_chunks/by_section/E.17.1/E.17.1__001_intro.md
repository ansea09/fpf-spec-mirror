---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__001_intro.md"
commit_sha: "72222c13cc1bba009f1ee1f1aca47654db8e5716"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:intro — Intro"
line_start: 80574
line_end: 80605
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

## E.17.1 - Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Tech-name.** `ViewpointBundleLibrary` (pattern and catalogue form, not a U-kind).

**Plain-name.** Viewpoint bundle library.

**Use this when.** The same coherent family of already admitted viewpoint editions recurs across projects, schools, or publication uses, and users need one editioned catalogue from which exact viewpoint references can be imported without restating or reidentifying the viewpoints.

**First action.** Resolve one already admitted catalogue edition L and its family designator, retrieve the local declaration, and resolve only the `U.ViewpointRef` members needed now. If L or the declaration is new, missing, or disputed, use §4.2 to recover `<G_L, K_L, R_L>` and verify L's C.2.1 constitution for that edition; reuse that result while the edition, effective scheme, and relied-on premises stay unchanged.

**First useful result.** One exact catalogue edition L, one ordinary family designator retrieving a local declaration claim block, and one finite non-empty member set of `U.ViewpointRef` values that each resolve to an exact E.17.0 viewpoint episteme edition. L retains its C.2.1 identity; the compact locator `<editionDesignator(L), familyDesignator>` aids retrieval under `R_L` but is neither L's identity nor a separate bundle kind or entity.

**Ordinary stop.** Stop when exact L, the declaration, and the needed reference subset are recoverable. Do not reconstruct L's constitution, instantiate every member, select an A.22 structure, prove conformance, or publish the catalogue merely to import an admitted family.

**Admission boundary.** E.24.UK admits `U.Viewpoint` and `U.View`; it does not admit `U.ViewpointBundleLibrary` or `U.ViewpointBundle`. E.17.1 therefore defines an ordinary catalogue-episteme form and local bundle declarations in its claim content. The historical filename remains a discovery locator only and grants no kind membership.

**Do not use this when.** One describing use merely selects one viewpoint or a small one-off set that has no recurring family-level purpose. Keep the exact references local; a bundle adds no conformance, membership, structure, publication, or correspondence merely by collecting them.

**What changes in practice.** Authors reuse exact references and preserve their bundle provenance; reviewers can detect silent member substitution, alias collision, and package-driven membership claims.



**Builds on.**
`A.6.2-A.6.4` (episteme morphism classes), A.6.5 relation-declaration slot discipline, `A.7`, `E.7`, `E.10`, `E.10.D1`, `E.10.D2`, and `E.17.0 MultiViewDescribing`.

**Used by.**
`E.17.2` (TEVB engineering viewpoint bundles), `E.18:5.12`, and domain-specific viewpoint families for architecture, governance, safety, research, or assurance.

