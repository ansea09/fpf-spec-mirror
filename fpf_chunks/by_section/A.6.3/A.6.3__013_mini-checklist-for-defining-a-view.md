---
chunk_kind: "child"
pattern_id: "A.6.3"
pattern_title: "U.EpistemicViewing — EntityOfConcern-preserving morphism"
section_id: "A.6.3:9"
section_title: "Mini-checklist (for defining a view)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3/A.6.3__013_mini-checklist-for-defining-a-view.md"
commit_sha: "d6af871b3e4e47c952d800a2a418c0634f180aaf"
heading_path:
  - "A.6.3 — U.EpistemicViewing — EntityOfConcern-preserving morphism"
  - "A.6.3:9 — Mini-checklist (for defining a view)"
line_start: 12518
line_end: 12540
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
keywords:
---

### A.6.3:9 - Mini-checklist (for defining a view)

When you introduce a new “view” in FPF, check:
1. **Same EntityOfConcern?**
   Does `entityOfConcernRef` stay the same? If not, this is **Retargeting**, not Viewing.

2. **Which slots move?**
   Have you listed exactly which SlotKinds you read/write, and shown that `EntityOfConcernSlot` is read‑only?

3. **Conservative?**
   Can you explain, in your discipline’s terms, why the view does not introduce new claims about the same EntityOfConcern?

4. **Profile?**
   Is this a self‑contained projection (`U.DirectEpistemicViewing`) or does it depend on a `CorrespondenceModel` (`U.CorrespondenceEpistemicViewing`)?

5. **Context & viewpoint?**
   Have you stated:
   * the EntityOfConcernClass for `EntityOfConcernSlot`,
   * the contexts/ReferencePlanes you assume,
   * and the viewpoint bundle (if any) you operate under?

If all answers are crisp and the invariants EV-0...EV-6 are satisfied, the pattern is a good candidate for `U.EpistemicViewing`.

