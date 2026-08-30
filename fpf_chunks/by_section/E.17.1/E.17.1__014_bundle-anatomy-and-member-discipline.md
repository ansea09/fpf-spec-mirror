---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:13"
section_title: "Bundle Anatomy and Member Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__014_bundle-anatomy-and-member-discipline.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:13 — Bundle Anatomy and Member Discipline"
line_start: 81754
line_end: 81791
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

### E.17.1:13 - Bundle Anatomy and Member Discipline

A viewpoint-bundle library becomes thin and reusable only when the bundle itself stays stable while the member viewpoints remain explicit enough to review independently. The bundle therefore has two simultaneous obligations: coherence at the family level and clarity at the member level.

#### E.17.1:13.1 - What a viewpoint member should make explicit

Each `U.ViewpointRef` member inside a reusable bundle resolves to one exact viewpoint episteme edition whose claim content makes explicit at least:

- the **concern family** it brings into focus,
- exact **stakeholder or audience referents** only when they change the concerns,
- the exact **target-kind criterion** it carries and the compatibility condition under which this family can reuse it,
- the **independently admitted episteme kinds** whose exact membership rules allow candidates under that viewpoint,
- any **bundle-specific conformance notes** later users must retain, plus an exact reference that resolves to the comparison claim or F.9 Bridge when either has independently been established; a note or reference creates no correspondence.

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

may be linked through references that resolve under their applicable schemes to exact annex assets, with each reference's local role stated. This preserves a stable declaration claim block while still letting reuse packages carry enough didactic material and review help.

