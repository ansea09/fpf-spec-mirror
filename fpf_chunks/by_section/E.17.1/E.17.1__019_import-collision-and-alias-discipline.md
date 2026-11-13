---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:18"
section_title: "Import Collision and Alias Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__019_import-collision-and-alias-discipline.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:18 — Import Collision and Alias Discipline"
line_start: 113553
line_end: 113563
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

### E.17.1:18 - Import Collision and Alias Discipline

#### E.17.1:18.1 - A family designator is not a synonym bag
An ordinary family designator does not mean that all member viewpoints are interchangeable labels for one concern. One declaration states that this reviewed family of viewpoints is intended to recur together. Authors should keep the family designator distinct from each member.

#### E.17.1:18.2 - Import collision rule
When two imported bundles contribute viewpoints with overlapping lexical names, preserve the originating viewpoint designators and catalogue provenance rather than silently merging the members. Inspectable collisions make provenance adequate; they do not show that the local senses correspond or that either member may substitute for the other.

#### E.17.1:18.3 - Alias boundary
Local teaching aliases may be added for readability, but the alias must identify the member viewpoints it denotes and must not erase bundle provenance. If the alias alone is used to select the bundle, the selection is unsupported. The project should replace the alias in that use with explicit member references.

