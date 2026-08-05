---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:14"
section_title: "Import, Subset, and Multi-Bundle Coordination"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__015_import-subset-and-multi-bundle-coordination.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:14 — Import, Subset, and Multi-Bundle Coordination"
line_start: 79751
line_end: 79789
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

### E.17.1:14 - Import, Subset, and Multi-Bundle Coordination

The value of viewpoint bundles appears most clearly when they are imported, subsetted, and coordinated across several reused families. Those cases need explicit discipline so that a local project does not quietly mutate what it claims to be reusing.

#### E.17.1:14.1 - Subset selection

A `MultiViewDescribing` use may legitimately import only a subset of a bundle's viewpoint references. When it does so, it should declare:

- which `ViewFamilyId` is the source,
- which viewpoint members are actually in local use,
- and whether the omitted members are simply unused or are intentionally excluded because the local scope does not require them.

The local family must not speak as if it had imported the whole bundle while silently dropping inconvenient viewpoints.

#### E.17.1:14.2 - Local overlays vs new bundles

A local project often wants a small adaptation: one extra concern note, one narrower stakeholder emphasis, one local naming convention. `E.17.1` prefers explicit overlays or new editions over silent mutation.

A practical rule is:

- if the local project selects a subset or adds only didactic/publication material, keep the exact imported bundle edition unchanged and declare the local subset or annex; do not treat the overlay as bundle content;
- if the local project changes viewpoint membership or meaning, publish a new local bundle or a new edition.

This is how bundle reuse remains trustworthy across organizations.

#### E.17.1:14.3 - Multi-bundle coordination

Many real description families need more than one bundle, for example:

- one engineering viewpoint family,
- one safety or assurance family,
- and one governance or publication-oriented family.

In such cases, `E.17.1` expects the family to preserve the provenance of each exact member reference and resolved viewpoint episteme P rather than flattening everything into one unnamed `Sigma`. Cross-family correspondence names each participating exact `U.ViewpointRef` or resolved P together with its exact source bundle edition and `ViewFamilyId` provenance; the corresponding `VP.*` token may remain only as a readable designator.

#### E.17.1:14.4 - Engineering vs publication families

Some contexts need both engineering viewpoints and publication viewpoints. `E.17.1` permits both, but it does not allow one family id to erase the distinction. A family that imports both kinds must keep the namespaces and bundle origins explicit so that authors do not confuse *how the holon is being understood* with *how a publication face/form chooses to expose that understanding*.

