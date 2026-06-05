---
chunk_kind: "child"
pattern_id: "E.17"
pattern_title: "Multi‑View Publication Kit"
section_id: "E.17:14"
section_title: "Minimal authoring template (Part E)"
source_path: "FPF-Spec.md"
output_path: "by_section/E.17/E.17__015_minimal-authoring-template-part-e.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "E.17 — Multi‑View Publication Kit"
  - "E.17:14 — Minimal authoring template (Part E)"
line_start: 63341
line_end: 63345
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

### E.17:14 - Minimal authoring template (Part E)

**Header:** `MVPK v⟨edition⟩ — Σ = {PlainView ⪯ TechCard ⪯ InteropCard, AssuranceLane ⟂}`
**For each arrow `f`:** emit `{Emit_s(f) | s ∈ Σ}` (or use the plain aliases `{PlainView(f), TechCard(f), …}`) with: **PublicationScope**, ViewpointId, pins, CHR and CG references, SCR ids, Bridge+CL ids (if crossing), and—if composite—machine‑checkable witnesses that `Emit_s(g∘f) = Emit_s(g)∘Emit_s(f)` **and** for each `s ⪯ t` the naturality square `PromoteView[s→t]_Y ∘ Emit_s(f) = Emit_t(f) ∘ PromoteView[s→t]_X`.

