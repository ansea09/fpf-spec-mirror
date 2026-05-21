---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:9"
section_title: "Archetypal grounding (System / Episteme)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__010_archetypal-grounding-system-episteme.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:9 — Archetypal grounding (System / Episteme)"
line_start: 29607
line_end: 29618
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "A.15.1"
  - "B.1"
  - "B.1.2"
  - "B.1.4"
  - "B.1.5"
  - "C.5"
keywords:
  - "Resrc-CAL"
  - "cost"
  - "energy consumption"
  - "resource aggregation"
  - "work"
---

### B.1.6:9 - Archetypal grounding (System / Episteme)

| Facet                       | **U.System — Assembling a heat‑treated frame**                                                                      | **U.Episteme — Training and publishing a model**                                                                                     |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| **Boundary**                | The enclosure boundary of the frame workstation; ports for electricity, gas, material in/out.                       | The boundary of the knowledge publication unit: data ingress, model-publication egress, compute energy ingress.                                 |
| **Work definition**         | Electricity and fuel inflows minus outflows minus Δstock of materials and thermal content retained in the frame.    | Energy spent (compute) + data‑read deltas; Embodied work includes the stored parameters (as committed bytes) and archived SCRs. |
| **Embodied vs Dissipated**  | Embodied: material incorporated, latent heat retained; Dissipated: heat loss, scrap.                                | Embodied: parameter file written, proof carriers; Dissipated: energy to heat, discarded intermediate data.                          |
| **Additivity across parts** | Ports on furnace, press, conveyor are `Bᵢ`; total frame‑level Work is Σ over `Bᵢ`.                                  | Data‑read over dataset shards are `Bᵢ`; total training Work adds per‑shard deltas.                                                   |
| **Time slicing**            | Heat → dwell → quench phases are `PhaseOf`; Work adds: Σ over phases.                                               | Epochs are `PhaseOf`; Work adds across epochs.                                                                                       |
| **WLNK**                    | Gas supply cap limits feasible heat cycles (critical input); if redundancy is added (dual supply), model it as MHT. | Storage bandwidth caps data‑read; adding a cache hierarchy is MHT (new structural capability), not “free” efficiency.                |


