---
chunk_kind: "child"
pattern_id: "G.2"
pattern_title: "SoTA Harvester & Synthesis"
section_id: "G.2:8"
section_title: "Common Anti‑Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/G.2/G.2__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "ec66cbef9f337bca279d86e825db0947f90e2598"
heading_path:
  - "G.2 — SoTA Harvester & Synthesis"
  - "G.2:8 — Common Anti‑Patterns and How to Avoid Them"
line_start: 76884
line_end: 76905
dependencies:
  - "A.10"
  - "A.19.DECLARED-SUBSTRATE-INTERPRETIVE-VIEW"
  - "A.6.P"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.21"
  - "E.10"
  - "E.19"
  - "E.8"
  - "F.17"
  - "F.9"
  - "G.0"
  - "G.1"
  - "G.10"
  - "G.11"
  - "G.13"
  - "G.3-G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "BridgeMatrix"
  - "DeclaredSubstrateAtlasView"
  - "FlowRecord"
  - "GammaEpistSynthId"
  - "SoTA Synthesis Pack@CG-Frame"
  - "SoTA harvest"
  - "SoTAPaletteDescription"
  - "Tradition"
  - "TraditionAtlasView"
  - "TypedSetViews"
  - "palette-first"
  - "synthesis"
---

### G.2:8 - Common Anti‑Patterns and How to Avoid Them

* **AP‑G2‑1: “One true SoTA score.”**
  **Avoid:** selecting a single unqualified scalar metric as “the” SoTA.
  **Do instead:** represent evaluation constructs as families/variants; keep partial orders set‑returning (delegated).

* **AP‑G2‑2: Fusion without explicit alignment proof.**
  **Avoid:** merging rival `Tradition` claims into one statement “by common sense.”
  **Do instead:** preserve parallel Claim Sheets; if consolidation is required, publish explicit alignment proof or keep a divergence record.

* **AP‑G2‑3: Hidden protocol drift.**
  **Avoid:** changing the harvesting protocol (inclusion criteria, windowing, screening rubric) without pins.
  **Do instead:** pin harvesting policy/profile ids and treat changes as RSCR‑relevant.

* **AP‑G2‑4: Unanchored pedagogy.**
  **Avoid:** micro‑examples without carriers (they become folklore).
  **Do instead:** bind micro‑examples to A.10 anchors and declare `entityOfConcern`.

* **AP‑G2‑5: Atlas by default.**
  **Avoid:** writing as if every tradition comparison or NQD/OEE note needs `TraditionAtlasView`, or as if atlas wording renames the palette itself.
  **Do instead:** keep the base palette and derived front, archive, or shortlist explicit; use atlas form only when several declared views or interpretive qualifiers must be held together, and prefer thinner `DeclaredSubstrateInterpretiveView` when that is enough.

