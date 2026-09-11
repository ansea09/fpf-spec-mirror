---
chunk_kind: "child"
pattern_id: "B.5.4"
pattern_title: "Recognize a Reusable Concept in a Concrete Situation"
section_id: "B.5.4:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.4/B.5.4__006_archetypal-grounding.md"
commit_sha: "cda9087f48e0bce2c5f9d5f4389e7e025c7678f5"
heading_path:
  - "B.5.4 — Recognize a Reusable Concept in a Concrete Situation"
  - "B.5.4:5 — Archetypal Grounding"
line_start: 42094
line_end: 42111
dependencies:
  - "A.7.1"
  - "B.5"
  - "C.29"
  - "C.3"
keywords:
---

### B.5.4:5 - Archetypal Grounding

#### B.5.4:5.1 - Glare from water

You want to reduce glare in an image. Identify air, water, a selected interface patch, incoming light and the direction from that patch to the camera. Draw the local normal and incidence plane. For unpolarized illumination of a smooth dielectric interface at Brewster incidence, reflected light is polarized perpendicular to that plane. Rotating a linear polarizer before the camera changes the transmitted reflected contribution. This is the domain relation supplied by [Feynman, I.33, §33-4](https://www.feynmanlectures.caltech.edu/I_33.html#Ch33-S4).

The interpretation tells you what to adjust. Moving the viewpoint changes incidence; ripples change local normals, so a single planar sketch may need several patches. Inspect a changed view and determine whether the proposed adjustment still follows.

#### B.5.4:5.2 - Recognize a conflict relation before colouring a graph

A laboratory must place three tests in two simultaneous-run slots. Its operating conditions say that A and B need the same exclusive fixture throughout a run; B and C need the same exclusive power unit; A and C can run together. There are no other constraints in this constructed case.

Represent tests by vertices and a pairwise inability to share a slot by an edge. The observations supply edges AB and BC. The construction in [B.5:5.1][fpf-b5-5-1-ref] produces slots {A,C} and {B}; reading the result back means that neither exclusive resource is double-booked.

Now change the conditions: A and C also require the same observer throughout a run. This adds edge AC. The triangle needs three slots under these conditions; two-colouring no longer supplies an arrangement.

Consider instead three tests with independent fixtures whose shared resource is a 5 A supply. Each draws 2 A. Any pair can run together, but all three exceed the supply's capacity. A graph with no pairwise conflict edges loses that group constraint. Retain the currents and the slot-wise capacity inequality when constructing the arrangement.

