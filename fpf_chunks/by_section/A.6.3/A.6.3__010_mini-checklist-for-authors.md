---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — describedEntity‑preserving morphism"
section_id: "A.6.3:9"
section_title: "Mini‑checklist (for authors)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__010_mini-checklist-for-authors.md"
commit_sha: "16cd31387cff04ab6b0feef22717f82ac54efa8f"
heading_path:
  - "A.6.3 — U.EpistemicViewing — describedEntity‑preserving morphism"
  - "A.6.3:9 — Mini‑checklist (for authors)"
line_start: 10244
line_end: 10266
dependencies:
  - "A.6.0"
  - "A.6.2"
  - "A.6.5"
  - "A.7"
  - "B.5.3"
  - "C.2"
  - "C.2.1"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.TGA"
  - "U.EffectFreeEpistemicMorphing"
  - "U.EpistemeSlotGraph"
  - "U.MultiViewDescribing"
  - "U.RelationSlotDiscipline"
  - "U.Signature"
keywords:
  - "ClaimGraph"
  - "CorrespondenceModel"
  - "Direct vs Correspondence Viewing"
  - "EpistemicViewing"
  - "RepresentationScheme"
  - "Viewpoint"
  - "describedEntity preservation"
  - "displayed fibration"
  - "episteme"
  - "optics"
  - "view"
---

### A.6.3:9 - Mini‑checklist (for authors)

When you introduce a new “view” in FPF, check:
1. **Same described entity?**
   Does `describedEntityRef` stay the same? If not, this is **Retargeting**, not Viewing.

2. **Which slots move?**
   Have you listed exactly which SlotKinds you read/write, and shown that `DescribedEntitySlot` is read‑only?

3. **Conservative?**
   Can you explain, in your discipline’s terms, why the view does not introduce new claims about the same entity?

4. **Profile?**
   Is this a self‑contained projection (`U.DirectEpistemicViewing`) or does it depend on a `CorrespondenceModel` (`U.CorrespondenceEpistemicViewing`)?

5. **Context & viewpoint?**
   Have you stated:
   * the EoIClass for `DescribedEntitySlot`,
   * the contexts/ReferencePlanes you assume,
   * and the viewpoint bundle (if any) you operate under?

If all answers are crisp and the invariants EV-0...EV-6 are satisfied, the pattern is a good candidate for `U.EpistemicViewing`.

