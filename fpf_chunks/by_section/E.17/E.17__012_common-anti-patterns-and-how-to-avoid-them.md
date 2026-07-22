---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:10"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__012_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:10 — Common Anti-Patterns and How to Avoid Them"
line_start: 78373
line_end: 78385
dependencies:
  - "A.15.4"
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.17.AUD"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.8"
  - "F.9"
  - "F.9.1"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemicViewing"
  - "U.MultiViewDescribing"
keywords:
---

### E.17:10 - Common Anti-Patterns and How to Avoid Them

1. **“Presentation logic” as semantics.**
    *Fix:* Move any logic to `Describe_EoC_DescEp`, an exact specification-use or episteme-refinement gate, CG‑Spec, or KD‑CAL; keep views declarative; publication adds **zero** claims.
2. **Publishing only view objects.**
    *Fix:* MVPK **acts on arrows**. Always emit views for `g∘f`, not just for `ViewObj_s(X)`, `ViewObj_s(Y)`, and `ViewObj_s(Z)`.
3. **Unpinned numbers.**
    *Fix:* Reject card; supply **pins** plus CG and CHR references.
4. **Viewpointless views.**
    *Fix:* Define Viewpoint; attach concerns + conformance; re‑emit.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` can refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

