---
chunk_kind: "child"
pattern_id: "A.11"
pattern_title: "Ontological Parsimony (C‑5)"
section_id: "A.11:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.11/A.11__006_archetypal-grounding.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "A.11 — Ontological Parsimony (C‑5)"
  - "A.11:5 — Archetypal Grounding"
line_start: 18871
line_end: 18880
dependencies:
  - "A.11"
  - "U.Type"
keywords:
  - "Occam's razor"
  - "essential concepts"
  - "minimalism"
  - "simplicity"
---

### A.11:5 - Archetypal Grounding

| Gate    | **Rejected candidate** (why)                                                                                                                                                                               | **Accepted approach**           |
| ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------- |
| **G‑1** | `U.CoolantPump` – expressible as `U.System:Pump` + `CoolingCirculatorRole`.                                                                                                                                | Composition via Role.           |
| **G‑2** | `U.Actuator` vs existing `U.Transformer` (90 % overlap).                                                                                                                                                   | Retain broader `U.Transformer`. |
| **G‑3** | `U.MiscellaneousObject` – name signals no function.                                                                                                                                                        | Reject; unclear purpose.        |
| **G‑4** | `U.SmallPart` – boundary depends on subjective size.                                                                                                                                                       | Reject; fails crisp test.       |
| —       | **`U.ProvenanceChain`** – required to record immutable evidence lineage; cannot be composed; functionally named; crisp membership rule (*“ordered list of Evidence Graph Ref with forward integrity hash”*). | Accepted, timer started.        |

