---
chunk_kind: "child"
pattern_id: "E.17.1"
pattern_title: "U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
section_id: "E.17.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17.1/E.17.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "c859eed90b5ca9d0f717a1ffb13a841a3b52c016"
heading_path:
  - "E.17.1 — U.ViewpointBundleLibrary - Reusable Viewpoint Bundles"
  - "E.17.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 72409
line_end: 72417
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

### E.17.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | What it looks like | How FPF prevents it |
|---|---|---|
| **Publication-face hijack** | A `ViewFamilyId` is reused as a publication-face name or document type. | `CC-VBL-3` keeps family ids lexical and bundle-local. |
| **Bundle equals view collection** | A folder or report pack is called a viewpoint bundle even though no `U.Viewpoint` family is declared. | `E.17.1` defines the bundle as a declared family of viewpoints, not a file grouping. |
| **Silent local drift** | A local project keeps the old family id but swaps in different viewpoints. | `CC-VBL-5` requires editioning for semantic or membership change. |
| **Namespace collapse** | Engineering viewpoint ids and publication viewpoint ids are mixed as if they were one namespace. | The solution keeps id spaces distinct and requires explicit attribution. |

