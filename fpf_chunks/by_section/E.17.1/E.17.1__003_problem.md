---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__003_problem.md"
commit_sha: "56440a9f2e252d7fd462f43470a433dd03413e19"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:2 — Problem"
line_start: 82021
line_end: 82035
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

### E.17.1:2 - Problem

Without a viewpoint-bundle library pattern:

1. **Each domain invents local viewpoint families.**
   Similar families reappear under slightly different labels, but no stable catalogue `U.Episteme` records whether the underlying viewpoints are actually the same.
2. **Viewpoint identity drifts.**
   A family called `functional`, `capability`, or `operational` may differ only lexically, or may differ semantically, but there is no disciplined place to tell which is which.
3. **`MultiViewDescribing` cannot reuse a family cleanly.**
   Every instance must restate its finite viewpoint family locally instead of importing an existing bundle.
4. **Reusable viewpoint-library practice remains external.**
   FPF lacks a native place where reusable viewpoint families can be expressed as reviewable catalogue content without importing a standard's ontology.
5. **Reader-facing labels leak into semantics.**
   Authors reuse the same name for viewpoints, views, publication faces, or folders, and the boundary between EntityOfConcern and Description episteme becomes unclear.

