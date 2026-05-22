---
chunk_kind: "child"
pattern_id: "B.5.2.1"
pattern_title: "Creative Abduction with NQD"
section_id: "B.5.2.1:9"
section_title: "Context‑Level KPIs (optional, informative)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2.1/B.5.2.1__011_context-level-kpis-optional-informative.md"
commit_sha: "725f0b7b372754cda3f6f4e15184215da568fc4d"
heading_path:
  - "B.5.2.1 — Creative Abduction with NQD"
  - "B.5.2.1:9 — Context‑Level KPIs (optional, informative)"
line_start: 32601
line_end: 32610
dependencies:
  - "A.17"
  - "A.18"
  - "B.4"
  - "B.5"
  - "B.5.2"
  - "C.11"
  - "C.17"
  - "C.18"
  - "C.19"
  - "G.5"
keywords:
  - "Creativity-CHR"
  - "DecisionSubject note"
  - "E/E-LOG"
  - "NQD binding"
  - "Novelty@context"
  - "Q-front"
  - "creative abduction"
  - "declared Q components"
  - "retained exploration/archive evidence"
  - "Γ_nqd.generate"
  - "ΔDiversity_P"
---

### B.5.2.1:9 - Context‑Level KPIs (optional, informative)

Contexts *may* monitor these—*not* as gates, but to improve practice:

1. **Generativity (Gv).** Fraction of abductive cycles whose selected candidate reaches **L1/L2** within policy windows (time‑to‑L1; time‑to‑evidence). (Maps onto state transitions driven by **B.5**.)
2. **Frontier‑Hit Rate (FHR).** % of cycles where the chosen candidate lies on the **Pareto front** over the declared `DominanceSet` at selection time; track novelty/diversity contribution separately as archive, tie-break, or policy-promoted evidence.
3. Coverage Gain (ΔI, report). Change in the *illumination summary* (coverage map/%filled cells) per cycle (how much of the descriptor space is now “lit”).
4. **Exploration Cost Ratio (ECR).** Compute/time spent in NQD‑Generate divided by downstream Shape/Evidence cost saved (tracks whether the pattern pays for itself).
5. **Refutation Learning Yield (RLY).** Among *refuted* candidates, % that added new coverage or raised SurpriseScore—turning “failures” into map‑building.

