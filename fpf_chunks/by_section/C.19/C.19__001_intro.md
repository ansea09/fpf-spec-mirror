---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__001_intro.md"
commit_sha: "3f6e02840fe3a22427aed590f9688a9c8f6bf5c8"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:intro — Intro"
line_start: 60672
line_end: 60684
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
  - "C.19"
  - "C.22.PFR"
  - "C.24"
  - "C.28"
  - "C.32"
  - "C.32.P2S"
  - "C.35"
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

**Intent.** State and test exploration and exploitation policy over still-live candidate pools so frontier treatment, graduation, narrowing, and sunset treatment stay explicit and auditable. A C.19 result governs pool treatment only; `C.19:4.4` routes a question that has moved to another operation or result.

C.19 states policy over a live pool. It does not generate candidates; use §4.4 when the next result requires another operation.


