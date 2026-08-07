---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:14"
section_title: "Import, Subset, and Multi-Bundle Coordination"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__015_import-subset-and-multi-bundle-coordination.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:14 — Import, Subset, and Multi-Bundle Coordination"
line_start: 79935
line_end: 79977
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

### E.17.1:14 - Import, Subset, and Multi-Bundle Coordination

The value of viewpoint bundles appears most clearly when they are imported, subsetted, and coordinated across several reused families. Those cases need explicit discipline so that a local project does not quietly mutate what it claims to be reusing.

#### E.17.1:14.1 - Subset selection

A `MultiViewDescribing` use may legitimately import only a subset of a bundle's viewpoint references. When it does so, it should declare:

- which ordinary family designator is the source,
- which viewpoint members are actually in local use,
- and whether the omitted members are simply unused or are intentionally excluded because the local scope does not require them.

The local family must not speak as if it had imported the whole bundle while silently dropping inconvenient viewpoints.

#### E.17.1:14.2 - Local overlays vs new bundles

A local project often wants a small adaptation: one extra concern note, one narrower stakeholder emphasis, one local naming convention. `E.17.1` prefers explicit overlays or new editions over silent mutation.

A practical rule is:

- if the local project selects a subset or adds only didactic/publication material, keep exact catalogue edition L and its declaration unchanged and declare the local subset or annex; do not treat the overlay as declaration content;
- if the local project changes viewpoint membership or meaning, publish a new local catalogue edition or a new family declaration.

This is how bundle reuse remains trustworthy across organizations.

#### E.17.1:14.3 - Multi-bundle coordination: provenance first, comparison separately

Many real description families need more than one bundle, for example:

- one engineering viewpoint family,
- one safety or assurance family,
- and one governance or publication-oriented family.

Preserve the exact provenance of every imported `U.ViewpointRef` and resolved P as `<editionDesignator(L), familyDesignator, member reference>`. That tuple answers where a member came from. It establishes no semantic sameness, difference, correspondence, translation, substitution, or admissible comparison by itself.

If the compared meanings are interpreted under one exact effective reference scheme, identify the exact P editions or claim subgraphs being compared, state the exact comparison predicate, polarity, scope, and participants, and apply the pattern that defines that predicate. If no direct semantic predicate is current, report only the observable lexical or structural contrast—members, omissions, order, target criteria, or claim-shape differences—and do not call it correspondence.

If the comparison crosses effective schemes or semantic contexts, first resolve the two exact F.17 `SchemeSenseCell` endpoints. Use F.9 only when its direct Bridge predicate is actually satisfied. Then state the proposed comparison or reuse separately as one bounded C.2.1 use claim about that exact Bridge with `<u,d,r,t>` and polarity, and recover the exact A.10 reliance disposition or the B.3 assurance branch when its threshold is met. Without the exact cells, obtaining Bridge, bounded-use claim, and required reliance path, stop at lexical or structural contrast. Catalogue provenance remains useful in every branch, but never substitutes for any of them.

#### E.17.1:14.4 - Engineering vs publication families

Some contexts need both engineering viewpoints and publication viewpoints. `E.17.1` permits both, but it does not allow one family designator to erase the distinction. A family that imports both kinds must keep the namespaces and catalogue origins explicit so that authors do not confuse *how the holon is being understood* with *how a publication face/form chooses to expose that understanding*.

