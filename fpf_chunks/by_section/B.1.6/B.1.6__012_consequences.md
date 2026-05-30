---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Γ\\_work — Work as Spent Resource"
section_id: "B.1.6:11"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__012_consequences.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "B.1.6 — Γ\\_work — Work as Spent Resource"
  - "B.1.6:11 — Consequences"
line_start: 30695
line_end: 30710
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

### B.1.6:11 - Consequences

**Benefits**

* **Audit‑ready costing:** A single definition of Work makes multi‑scale totals consistent and comparable.
* **Separation of concerns:** Control‑flow (Γ\_method) never contaminates cost accounting (Γ\_work).
* **Cross‑scale reliability:** Partition/time additivity gives predictable roll‑ups from parts and phases.
* **Safety by design:** WLNK gates reveal feasibility limits early; emergence is explicit via MHT.

**Trade‑offs / mitigations**

* **Boundary modelling effort:** Requires explicit ports and stock deltas. *Mitigation:* use A.14 templates for common boundary patterns.
* **Vector heterogeneity:** Mixed units can be hard to read. *Mitigation:* keep vectors typed; add equivalence maps only when justified in `M_spec`.
* **Independence discipline:** Shared stocks complicate additivity. *Mitigation:* elevate stock accounting to the parent boundary per CC‑B1.6.7.


