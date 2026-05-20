---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — describedEntity‑retargeting morphism"
section_id: "A.6.4:9"
section_title: "Mini-checklist (for use)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__010_mini-checklist-for-use.md"
commit_sha: "LOCAL_TEST"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — describedEntity‑retargeting morphism"
  - "A.6.4:9 — Mini-checklist (for use)"
line_start: 11957
line_end: 11978
dependencies:
  - "A.1"
  - "A.6.2"
  - "C.2"
  - "C.2.1"
  - "E.18"
  - "E.TGA"
  - "F.9"
  - "U.EpistemeSlotGraph"
  - "U.EpistemicRetargeting"
keywords:
  - "KindBridge"
  - "SquareLaw-retargeting"
  - "StructuralReinterpretation"
  - "describedEntity shift"
  - "retargeting"
  - "subject retargeting"
---

### A.6.4:9 - Mini-checklist (for use)

When you think you need "retargeting" in FPF, ask:

1. **Does `describedEntityRef` change?**
   If no, this is Viewing (A.6.3), not Retargeting.

2. **Is there a `KindBridge` between source and receiving entities?**
   If not, add or select the bridge in Part F, or revise the Intension instead of treating the relation as retargeting.

3. **What invariant are you preserving?**
   Write it down in KD-CAL/LOG-CAL terms. If you cannot, retargeting is underspecified.

4. **How do `GroundingHolonRef`, context, and viewpoint behave?**
   State whether they stay the same, move along Bridges, or are out of scope.

5. **Can the operation be factored as Mechanism + pure retargeting?**
   If the step needs computation such as FFT or model fitting, separate the Mechanism from the EpistemicRetargeting.

6. **What remains admissible for the reader?**
   State the remaining reader action, and name source-bearing reopen or a neighboring pattern when the bridge, invariant, or source support is insufficient for the intended use.

