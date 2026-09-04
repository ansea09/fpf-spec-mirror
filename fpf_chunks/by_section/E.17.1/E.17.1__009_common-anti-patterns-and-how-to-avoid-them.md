---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
section_id: "E.17.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "d7a7123459d158c6d5f0d304d6170c4aa69af71b"
heading_path:
  - "E.17.1 — Viewpoint Bundle Library - Reusable Viewpoint Reference Bundles"
  - "E.17.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 82119
line_end: 82127
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

### E.17.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Publication-face hijack** | A family designator is reused as a publication-face name or document type. | `CC-VBL-5` keeps the ordinary designator distinct from a publication face, form, carrier, viewpoint reference, or exact member. |
| **Bundle equals view collection** | A folder or report pack is called a viewpoint bundle even though no exact `U.ViewpointRef` values resolve to admitted `U.Viewpoint` epistemes. | `E.17.1` defines the bundle as a declared family of exact viewpoint references, not a file grouping. |
| **Silent local drift** | A local project keeps the old family designator but swaps in different viewpoints. | `CC-VBL-6` requires another catalogue edition or family declaration when member references, targets, family meaning, or compatibility constraints change. |
| **Namespace collapse** | Engineering and publication viewpoint designators are mixed as if they were one lexical namespace. | The solution keeps the designator namespaces distinct and requires explicit attribution. |

