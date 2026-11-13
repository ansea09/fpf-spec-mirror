---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__001_intro.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:intro — Intro"
line_start: 63902
line_end: 63912
dependencies:
  - "A.10"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
  - "C.11.CRC"
  - "C.16"
  - "C.17"
  - "C.18"
  - "C.24"
  - "E.10.LRN"
  - "E.17"
  - "E.24.PUB"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "already-live candidate pool"
  - "audience availability"
  - "change trigger"
  - "explore-exploit"
  - "governing lens"
  - "keep frontier"
  - "narrow to subset"
  - "pool-policy result"
  - "publication face"
  - "publication occurrence"
  - "selector-facing declaration"
  - "sunset line"
  - "widen"
---

## C.19 - Explore-Exploit Live-Pool Governor

> **Type:** C-pattern
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Explore-exploit governor.

**Intent.** State and test exploration and exploitation policy over live candidate pools so frontier treatment, graduation, narrowing, and sunset treatment stay explicit and auditable. A C.19 result governs pool treatment only. C.19 does not generate candidates; use `C.19:4.4` when the next result requires another operation.


