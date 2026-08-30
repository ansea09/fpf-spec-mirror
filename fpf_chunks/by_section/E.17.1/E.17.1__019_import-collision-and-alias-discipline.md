---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:18"
section_title: "Import Collision and Alias Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__019_import-collision-and-alias-discipline.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:18 — Import Collision and Alias Discipline"
line_start: 81922
line_end: 81932
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

### E.17.1:18 - Import Collision and Alias Discipline

#### E.17.1:18.1 - A family designator is not a synonym bag
An ordinary family designator does not mean that all member viewpoints are interchangeable labels for one concern. It means that one declaration claim block says a reviewed family of viewpoints is intended to recur together. Authors should therefore resist the drift where one convenient designator begins to substitute for all of its members.

#### E.17.1:18.2 - Import collision rule
When two imported bundles contribute viewpoints with overlapping lexical names, preserve the originating viewpoint designators and exact catalogue provenance rather than silently merging the members. Inspectable collisions make provenance adequate; they do not show that the local senses correspond or that either member may substitute for the other.

#### E.17.1:18.3 - Alias boundary
Local teaching aliases may be added for readability, but the alias must dock to explicit member viewpoints and must not erase bundle provenance. If the alias starts doing bundle-selection work by itself, it is making an unsupported bundle-selection claim and should be replaced by explicit member references.

