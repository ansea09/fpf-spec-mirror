---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:18"
section_title: "Import Collision and Alias Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__019_import-collision-and-alias-discipline.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:18 — Import Collision and Alias Discipline"
line_start: 64498
line_end: 64508
dependencies:
  - "A.16.0"
  - "A.6.2-A.6.4"
  - "A.7"
  - "C.2.1"
  - "C.2.2a"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.17.2"
  - "E.18"
  - "E.7"
  - "F.9"
  - "F.9.1"
  - "U.MultiViewDescribing"
keywords:
  - "alias discipline"
  - "engineering/management/research bundles"
  - "governance"
  - "import discipline"
  - "reusable viewpoint family"
  - "viewpoint bundle"
---

### E.17.1:18 - Import Collision and Alias Discipline

#### E.17.1:18.1 - Family id is not a synonym bag
A `ViewFamilyId` does not mean that all member viewpoints are interchangeable labels for one concern. It means that a reviewed family of viewpoints is intended to recur together. Authors should therefore resist the common drift where one convenient bundle name begins to substitute for all of its members.

#### E.17.1:18.2 - Import collision rule
When two imported bundles contribute viewpoints with overlapping lexical names, the publication should preserve the originating viewpoint ids and bundle provenance rather than silently merging the members. Bundle reuse is admissible only if collisions remain inspectable.

#### E.17.1:18.3 - Alias boundary
Local teaching aliases may be added for readability, but the alias must dock to explicit member viewpoints and must not erase bundle provenance. If the alias starts doing bundle-selection work by itself, it is making an unsupported bundle-selection claim and should be replaced by explicit member references.

