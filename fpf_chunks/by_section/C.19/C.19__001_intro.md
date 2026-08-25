---
chunk_kind: "child"
pattern_id: "C.19"
pattern_title: "Explore-Exploit Live-Pool Governor"
section_id: "C.19:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.19/C.19__001_intro.md"
commit_sha: "2124f3a0ea03125a5bf495c2ef99f5fbb4c73571"
heading_path:
  - "C.19 — Explore-Exploit Live-Pool Governor"
  - "C.19:intro — Intro"
line_start: 48263
line_end: 48278
dependencies:
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "B.3"
  - "C.11"
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

**Export relation.** `C.19` defines no generation operation. Use it to state and test live-pool treatment records over candidate pools, fronts, archive regions, family regions, and cultural live pools.

**Depends on.** `C.18` for archive and front stewardship, `C.16` for characteristic and measurement claims, `A.19.CPM` and `A.19.SelectorMechanism` for comparison and selection kernels, `B.3` for assurance-sensitive confidence claims, and `G.5` for ordinary selector and default tokens.

**Coordinates with.** `C.17` for compatible characteristic results and `G.9` for parity comparison. `C.19:4.4` names the exact next-pattern coordination when the live question changes.

