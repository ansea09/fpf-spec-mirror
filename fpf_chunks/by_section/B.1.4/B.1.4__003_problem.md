---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
section_id: "B.1.4:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__003_problem.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "B.1.4 — Contextual & Temporal Aggregation (Γ\\_ctx & Γ\\_time)"
  - "B.1.4:2 — Problem"
line_start: 28852
line_end: 28861
dependencies:
  - "A.12"
  - "A.14"
  - "A.15"
  - "B.1"
  - "B.1.1"
keywords:
  - "composition"
  - "order-sensitive"
  - "temporal aggregation"
  - "time-series"
---

### B.1.4:2 - Problem

Forcing sequential or temporal phenomena through the default, order‑indifferent Γ leads to recurring failures:

1. **Semantic erasure:** Treating `SerialStepOf` as if it were structural parthood flattens workflows; swapping steps silently changes meaning.
2. **Causal paradoxes:** Aggregating time slices as if they were unordered parts lets effects precede causes, or hides missing epochs.
3. **Locality violations:** Hidden shared state between “parallel” branches breaks reproducibility; independent branches were not actually independent.
4. **DesignRunTag conflation:** Mixing design‑time plans and run‑time histories in one fold produces “chimeras” that neither simulate nor audit reality.


