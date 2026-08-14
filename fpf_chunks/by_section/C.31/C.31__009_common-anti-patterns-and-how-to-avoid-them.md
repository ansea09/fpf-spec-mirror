---
chunk_kind: "child"
pattern_id: "C.31"
pattern_title: "Modularity and Reusable Structure Characteristics"
section_id: "C.31:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.31/C.31__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "C.31 — Modularity and Reusable Structure Characteristics"
  - "C.31:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 63538
line_end: 63548
dependencies:
  - "A.10"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.6.M"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.31"
  - "C.31.ASAP"
  - "C.31.RSA"
  - "C.32"
  - "C.32.P2S"
  - "G.5"
keywords:
  - "ModularityVectorLite"
  - "bespoke residue"
  - "cohesion"
  - "coupling"
  - "evidence reuse"
  - "interface variation"
  - "modularity characteristics"
  - "reusable-structure characteristics"
  - "substitutability"
---

### C.31:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| `ScalarModularityScore` | A single score claims architecture quality. | Replace with `ModularityVectorLite`, disclosed scoring basis and subject pattern, or report-only boundary. |
| `UntypedMeasureList` | A table of heads appears without characteristic, scale, declared measurement basis, or repair action. | Classify heads and create C.16-compatible cards only where the recovered claim needs them. |
| `MeasurementBeforeRepair` | The practitioner is asked for full measurement before one useful move exists. | Start with three characteristics under evaluation and repair direction. |
| `OpenInterfaceEqualsModular` | Interface publication is treated as modularity. | Apply relation repair through A.6.M and characterize only the interface or substitutability head under evaluation. |
| `ComplexityAsOneCharacteristic` | Algorithmic cost, graph-connectivity cost, policy and approval cost, evidence-maintenance cost, and cognitive cost are averaged. | Keep residual heads claim-scoped and apply lens or measurement patterns when those uses are being made. |
| `ProxyBecomesValue` | A report-only proxy becomes a beyond-local-repair claim. | State forbidden use and use the subject pattern before relying on that claim. |

