---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:13"
section_title: "Bundle Anatomy and Member Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__014_bundle-anatomy-and-member-discipline.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:13 — Bundle Anatomy and Member Discipline"
line_start: 113383
line_end: 113420
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

### E.17.1:13 - Bundle Anatomy and Member Discipline

A viewpoint-bundle library becomes thin and reusable only when the bundle stays stable while the member viewpoints remain explicit enough to review independently. The bundle must be coherent as a family and clear about each member.

#### E.17.1:13.1 - What a viewpoint member should make explicit

Each `U.ViewpointRef` member inside a reusable bundle resolves to one viewpoint episteme edition whose claim content makes explicit at least:

- the **concern family** it brings into focus,
- **stakeholder or audience referents** only when they change the concerns,
- the **target-kind criterion** it carries and the compatibility condition under which this family can reuse it,
- the **independently admitted episteme kinds** whose membership rules allow candidates under that viewpoint,
- any **bundle-specific conformance notes** later users must retain, plus a reference that resolves to the comparison claim or F.9 Bridge when either has independently been established; a note or reference creates no correspondence.

`E.17.1` does not redefine the internals of `U.Viewpoint`. It states what must remain visible if a viewpoint is to be reused as part of a bundle rather than as an undocumented local label.

#### E.17.1:13.2 - Bundle-level coherence

A shared prefix does not make a coherent bundle. A coherent bundle should answer a recognizable family-level question, such as:

- *which engineering concerns are standard for holon description?*
- *which governance perspectives are required for a service review?*
- *which research-method viewpoints recur across inquiry reports?*

If the member viewpoints do not share that family-level purpose, the result is not one bundle but an uncurated catalogue fragment.

#### E.17.1:13.3 - Thin bundles, rich annexes

`E.17.1` allows bundles to stay thin. Projects may link to companion material by references that resolve to the annex assets under their applicable schemes. State the local role of each reference. Examples include:

- lexical discipline notes,
- bridge overlays,
- A.16 move-publication notes,
- worked examples,
- or SoTA references

This preserves a stable declaration claim block while letting the reuse package carry enough teaching material and review guidance.

