---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:7"
section_title: "Embodiment and dissipation (reporting scheme)"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__008_embodiment-and-dissipation-reporting-scheme.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:7 — Embodiment and dissipation (reporting scheme)"
line_start: 30060
line_end: 30074
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

### B.1.6:7 - Embodiment and dissipation (reporting scheme)

Every Work vector **MAY** be split into two projections, both defined on the **same basis** and the **same boundary/time window**:

* **Embodied\_B(q)** — the part of Work retained **inside** B as *state change* of produced holons (e.g., latent heat stored, material incorporated, committed data).
* **Dissipated\_B(q)** — the part of Work irreversibly exported beyond B (e.g., heat loss, scrap, discarded packets).

By norm:

```
Work_B(q) = Embodied_B(q) + Dissipated_B(q)
```

This split is **informative**, not a second algebra: Γ\_work always folds the **total** Work; the split is attached in the **Boundary Ledger** for transparency.

