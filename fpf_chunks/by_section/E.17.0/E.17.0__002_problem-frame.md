---
chunk_kind: "child"
pattern_id: "E.17.0"
pattern_title: "Viewpoint and View Recognition for Multi-View Describing"
section_id: "E.17.0:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.0/E.17.0__002_problem-frame.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "E.17.0 — Viewpoint and View Recognition for Multi-View Describing"
  - "E.17.0:1 — Problem frame"
line_start: 81482
line_end: 81499
dependencies:
  - "A.22"
  - "A.6.3"
  - "A.6.5"
  - "C.13"
  - "C.2.1"
  - "C.29"
  - "E.10.D2"
  - "E.17"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
keywords:
---

### E.17.0:1 - Problem frame

An engineer may have several claim-bearing epistemes about one system, method, structure, work occurrence, or another exact entity. A functional description, safety description, maintenance description, and allocation description may serve different concerns. One episteme may also be constructed from another by a query or projection, rendered in several forms, published several times, or compared with another view.

Those uses involve different objects and relations:

1. the exact EntityOfConcern of each episteme;
2. the episteme itself, identified under C.2.1;
3. an exact `U.Viewpoint` episteme carrying fixed concerns and conformance rules;
4. an obtaining `EpistemeViewpointConformanceRelation` occurrence;
5. dependent `U.View` membership of the same episteme individual;
6. an optional A.6.3 viewing relation recording how one episteme was constructed from another;
7. an optional viewpoint selected for one current describing use when it changes what that use reads or checks or may conclude;
8. exact correspondence relations and epistemes that assert or describe them;
9. publication occurrences, forms, carriers, and representations.

The list is an orientation, not a form to fill. Ordinary positive recognition needs items 1 through 5; a negative test stops without an obtaining conformance occurrence or `U.View` membership. Construction, selection, correspondence, and publication stay outside unless the receiving use calls for them.

