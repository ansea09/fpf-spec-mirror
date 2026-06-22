---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 57829
line_end: 57839
dependencies:
keywords:
---

### C.31:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ScalarModularityScore` | A single score claims architecture quality. | Replace with `ModularityVectorLite`, disclosed scoring basis and governing pattern, or report-only boundary. |
| `UntypedMeasureList` | A table of heads appears without characteristic, scale, declared measurement basis, or repair action. | Classify heads and create C.16-compatible cards only where the recovered claim needs them. |
| `MeasurementBeforeRepair` | The practitioner is asked for full measurement before one useful move exists. | Start with three characteristics under evaluation and repair direction. |
| `OpenInterfaceEqualsModular` | Interface publication is treated as modularity. | Apply relation repair through A.6.M and characterize only the interface or substitutability head under evaluation. |
| `ComplexityAsOneCharacteristic` | Algorithmic cost, graph-connectivity cost, policy and approval cost, evidence-maintenance cost, and cognitive cost are averaged. | Keep residual heads claim-scoped and apply lens or measurement patterns when those uses are being made. |
| `ProxyBecomesValue` | A report-only proxy becomes a beyond-local-repair claim. | State forbidden use and use the governing pattern before relying on that claim. |

