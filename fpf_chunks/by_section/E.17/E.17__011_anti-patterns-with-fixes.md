---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:10"
section_title: "Anti‑patterns (with fixes)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__011_anti-patterns-with-fixes.md"
commit_sha: "e3fedf42dc7cb5d12905913b5a0b0e951ed7d254"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:10 — Anti‑patterns (with fixes)"
line_start: 63296
line_end: 63308
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.9"
  - "A.7"
  - "C.2.P"
  - "E.10"
  - "E.10.D2"
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

### E.17:10 - Anti‑patterns (with fixes)

1. **“Presentation logic” as semantics.**
    *Fix:* Move any logic to `Describe_EoC_DescEp`, an exact specification-use or episteme-refinement gate, CG‑Spec, or KD‑CAL; keep views declarative; publication adds **zero** claims.
2. **Publishing only view objects.**
    *Fix:* MVPK **acts on arrows**. Always emit views for `g∘f`, not just for `ViewObj_s(X)`, `ViewObj_s(Y)`, and `ViewObj_s(Z)`.
3. **Unpinned numbers.**
    *Fix:* Reject card; supply **pins** plus CG and CHR references.
4. **Viewpointless views.**
    *Fix:* Define Viewpoint; attach concerns + conformance; re‑emit.
5. **`InteropCard` equivalent to `TechCard` duplication.**
    *Fix:* `InteropCard` may refine typing or shape but cannot contradict `TechCard` (reindexing monotone).

