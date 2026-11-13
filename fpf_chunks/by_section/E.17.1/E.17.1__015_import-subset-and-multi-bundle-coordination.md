---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:14"
section_title: "Import, Subset, and Multi-Bundle Coordination"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__015_import-subset-and-multi-bundle-coordination.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:14 — Import, Subset, and Multi-Bundle Coordination"
line_start: 113421
line_end: 113465
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

### E.17.1:14 - Import, Subset, and Multi-Bundle Coordination

Importing a family, selecting a subset and coordinating several families show why viewpoint bundles are useful. Make each choice explicit so that other users can tell what the project has reused and what it has changed.

#### E.17.1:14.1 - Subset selection

A `MultiViewDescribing` use may import only a subset of a bundle's viewpoint references. When it does so, it should declare:

- which ordinary family designator is the source,
- which viewpoint members are in local use,
- and whether the omitted members are unused or are intentionally excluded because the local scope does not require them.

The local family must not speak as if it had imported the whole bundle while silently dropping inconvenient viewpoints.

#### E.17.1:14.2 - Local overlays vs new bundles

A local project often wants a small adaptation: one extra concern note, one narrower stakeholder emphasis, one local naming convention. `E.17.1` prefers explicit overlays or new editions over silent mutation.

A practical rule is:

- if the local project selects a subset or adds only didactic/publication material, keep catalogue edition L and its declaration unchanged and declare the local subset or annex; do not treat the overlay as declaration content;
- if the local project changes viewpoint membership or meaning, publish a new local catalogue edition carrying the revised or new family declaration.

#### E.17.1:14.3 - Multi-bundle coordination: provenance first, comparison separately

Many description families need more than one bundle, for example:

- one engineering viewpoint family,
- one safety or assurance family,
- and one governance or publication-oriented family.

Preserve the provenance of every imported `U.ViewpointRef` and resolved P as `<editionDesignator(L), familyDesignator, member reference>`. That tuple identifies where each member came from. It establishes no semantic sameness, difference, correspondence, translation, substitution, or admissible comparison by itself.

Identify the P editions or claim subgraphs being compared, the comparison predicate, polarity, scope and participants. Recover how each source interprets the values used by that predicate, then apply its subject method. Different schemes may require a representation or quantity conversion without requiring a semantic Bridge. If the material supports only a lexical or structural contrast (such as members, omissions, order, target criteria or claim-shape differences), state that limited result.

When the comparison or proposed reuse depends on a semantic relation between distinct local senses, resolve their F.17 `SchemeSenseCell` endpoints and establish the F.9 Bridge. State the proposed use separately as one bounded C.2.1 claim about that Bridge with `<u,d,r,t>` and polarity.

For reliance on an affirmative claim, retain the same-use A.10 provenance. Ordinary reliance requires `RelianceDisposition=pass`; when a named assurance claim is current, require its B.3 result with `disposition=supported-for-use` for that bounded use.

If a required meaning, correspondence or reliance ground is missing, withhold the dependent conclusion and retain the supported contrast or exact inquiry. Catalogue provenance identifies the sources in every branch.

#### E.17.1:14.4 - Engineering vs publication families

Some contexts need both engineering viewpoints and publication viewpoints. A shared family designator must preserve the distinction between engineering and publication viewpoints. A family that imports both kinds must keep the namespaces and catalogue origins explicit so that authors can distinguish *how the holon is being understood* from *how a publication face/form chooses to expose that understanding*.

