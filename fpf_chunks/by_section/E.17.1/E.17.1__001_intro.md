---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__001_intro.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:intro — Intro"
line_start: 79453
line_end: 79476
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

## E.17.1 - `U.ViewpointBundleLibrary` - Reusable Viewpoint Bundles

> **Type:** Architectural (A)
> **Status:** Stable
> **Normativity:** Normative unless marked informative

**Plain-name.** Viewpoint bundle library.

**Use this when.** The same coherent family of already admitted viewpoint editions recurs across projects, schools, or publication uses, and users need one editioned catalogue from which exact viewpoint references can be imported without restating or reidentifying the viewpoints.

**First useful result.** One exact library edition, one `ViewFamilyId`, and one finite non-empty set of `U.ViewpointRef` values that each resolve to an exact E.17.0 viewpoint episteme edition.

**Do not use this when.** One describing use merely selects one viewpoint or a small one-off set that has no recurring family-level purpose. Keep the exact references local; a bundle adds no conformance, membership, structure, publication, or correspondence merely by collecting them.

**What changes in practice.** Authors reuse governed references and preserve their bundle provenance; reviewers can detect silent member substitution, alias collision, and package-driven membership claims.



**Builds on.**
`A.6.2-A.6.4` (episteme morphism classes), `A.6.5 U.RelationSlotDiscipline`, `A.7`, `E.7`, `E.10`, `E.10.D1`, `E.10.D2`, and `E.17.0 MultiViewDescribing`.

**Used by.**
`E.17.2` (TEVB engineering viewpoint bundles), `E.18:5.12`, and domain-specific viewpoint families for architecture, governance, safety, research, or assurance.

