---
chunk_kind: "child"
pattern_id: "A.6.4"
pattern_title: "U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
section_id: "A.6.4:9"
section_title: "Mini-checklist (for use)"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.4/A.6.4__013_mini-checklist-for-use.md"
commit_sha: "10cd224cef9c92043fb6821e165decd6ea05073f"
heading_path:
  - "A.6.4 — U.EpistemicRetargeting — EntityOfConcern retargeting morphism"
  - "A.6.4:9 — Mini-checklist (for use)"
line_start: 13273
line_end: 13294
dependencies:
  - "A.6.2"
  - "A.6.3"
  - "A.6.5"
  - "A.7"
  - "C.2"
  - "C.2.1"
  - "C.3"
  - "E.10.D2"
  - "E.18"
  - "F.9"
keywords:
---

### A.6.4:9 - Mini-checklist (for use)

When you think you need "retargeting" in FPF, ask:

1. **Does `entityOfConcernRef` change?**
   If no, this is Viewing (A.6.3), not Retargeting.

2. **Is there a `KindBridge` between source and receiving entities?**
   If not, add or select the bridge in Part F, or revise the EntityOfConcern instead of treating the relation as retargeting.

3. **What invariant are you preserving?**
   Write it down in KD-CAL/LOG-CAL terms. If you cannot, retargeting is underspecified.

4. **How do `GroundingHolonRef`, context, and viewpoint behave?**
   State whether they stay the same, move along Bridges, or are out of scope.

5. **Can the operation be factored as Mechanism + pure retargeting?**
   If the step needs computation such as FFT or model fitting, separate the Mechanism from the EpistemicRetargeting.

6. **What remains admissible for the reader?**
   State the remaining reader action, and name source-bearing reopen or a neighboring pattern when the bridge, invariant, or source/bridge/invariant witness is insufficient for the intended use.

