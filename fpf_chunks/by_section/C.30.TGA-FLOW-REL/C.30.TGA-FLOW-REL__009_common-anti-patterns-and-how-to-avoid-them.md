---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture-TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "21e2101c100964de121c37408b37563ee0cdbf8c"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture-TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 54423
line_end: 54434
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureFlowStructureRelation@TGA"
  - "FlowTransductionStructure"
  - "TGA graph relation"
  - "architecture flow relation"
  - "graph/path/crossing"
---

### C.30.TGA-FLOW-REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Graph-as-architecture** | The E.18 graph is called the architecture. | Use C.30 for the grounded architecture claim, selected architecture-relevant structure, or conditional architecture description, and keep this relation only for flow or transduction structure. |
| **Graph-as-functional-architecture** | A TGA graph is treated as the functional architecture itself. | Split functional structure from flow or transduction structure and add correspondence. |
| **Flow-as-work-log** | Path or slice wording is treated as work occurrence. | Assign occurrence or result claims to A.15 or P2W and keep TGA as graph or path relation. |
| **Crossing-as-gate-result** | A crossing relation is treated as gate passage. | Assign gate-decision claims to A.21 and keep crossing relation under E.18. |
| **Valuation-as-score** | A flow valuation is used as a generic architecture score. | State E.18 valuation and set-return discipline; assign measurement, characterization, selection, or candidate-set claims to `C.16` or an admitted governing pattern when those claims are being made. |
| **Generated relation-graph proof** | A code-agent relation graph or probe output is used as proof of architecture understanding or safety. | Recover source, source observation class selected from {observed, inferred, unknown}, hidden structure, and evidence or assurance pattern governing the claim applications. |
| **Prompt-data-tool flow as authority proof** | A prompt, data, or tool-flow graph is treated as permission for tool action or proof that authority is safe. | Keep the graph as a flow relation. A path from untrusted content to tool action is governed by `SecurityTrustBoundaryStructure`, C.24, E.16, A.20, or A.21 when those claim kinds are being made. |

