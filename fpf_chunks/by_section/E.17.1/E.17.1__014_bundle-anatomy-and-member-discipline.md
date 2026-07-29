---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:13"
section_title: "Bundle Anatomy and Member Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__014_bundle-anatomy-and-member-discipline.md"
commit_sha: "bcbdb7fd94b80006d23a673827f4f660453b2501"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:13 — Bundle Anatomy and Member Discipline"
line_start: 78148
line_end: 78185
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

### E.17.1:13 - Bundle Anatomy and Member Discipline

A viewpoint-bundle library becomes thin and reusable only when the bundle itself stays stable while the member viewpoints remain explicit enough to review independently. The bundle therefore has two simultaneous obligations: coherence at the family level and clarity at the member level.

#### E.17.1:13.1 - What a viewpoint member should make explicit

Each member `U.Viewpoint` inside a reusable bundle should make explicit at least:

- the **concern family** it brings into focus,
- the **stakeholder families** for whom that concern matters,
- the **entity of concern class** for which it is admissible,
- the **allowed description and specification-useification kinds** that usually realize it,
- and any **bundle-specific conformance or correspondence notes** that later view families should preserve.

`E.17.1` does not redefine the internals of `U.Viewpoint`. It states what must remain visible if a viewpoint is to be reused as part of a bundle rather than as an undocumented local label.

#### E.17.1:13.2 - Bundle-level coherence

A bundle is not just a bag of viewpoints with one shared prefix. A coherent bundle should answer a recognizable family-level question, such as:

- *which engineering concerns are standard for holon description?*
- *which governance perspectives are required for a service review?*
- *which research-method viewpoints recur across inquiry reports?*

If the member viewpoints do not share that family-level purpose, the result is not one bundle but an uncurated catalogue fragment.

#### E.17.1:13.3 - Thin bundles, rich annexes

`E.17.1` intentionally allows bundles to stay thin. Rich companion material such as:

- lexical discipline notes,
- bridge overlays,
- A.16 move-publication notes,
- worked examples,
- or SoTA references

may live in typed annex manifests. This preserves a stable bundle core while still letting reuse packages carry enough didactic material and review help.

