---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 61949
line_end: 61960
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.0"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "A.7"
  - "B.3"
  - "C.16"
  - "C.2.P"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "F.18"
  - "G.6"
keywords:
  - "architecture structural view"
  - "architecture-to-transformation-flow relation"
  - "candidate architecture input"
  - "functional behavior"
  - "selected structure"
  - "transformation-flow structure"
---

### C.30.TFS-REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-architecture** | The E.18 selected transformation-flow structure is called the whole architecture. | Use C.30 for the grounded architecture claim, selected architecture-relevant structure, or conditional architecture description, and keep this relation only for the transformation-flow relation. |
| **Graph-description-as-functional-architecture** | A graph-shaped mathematical description or diagram is treated as the functional architecture itself. | Split functional structure, selected transformation-flow structure, mathematical description, and publication face; add correspondence when needed. |
| **Flow-as-work-log** | Path or slice wording is treated as work occurrence. | Assign occurrence or result claims to A.15 or P2W and keep E.18 to selected structure, path, slice, or valuation. |
| **Crossing-as-gate-result** | A crossing relation is treated as gate passage. | Assign gate-decision claims to A.21 and keep crossing relation under E.18. |
| **Valuation-as-score** | A flow valuation is used as a generic architecture score. | State E.18 valuation and set-return discipline; assign measurement, characterization, selection, or candidate-set claims to `C.16` or an admitted governing pattern when those claims are being made. |
| **Generated relation-graph proof** | A code-agent relation graph or probe output is used as proof of architecture understanding or safety. | Recover the source publication or codebase edition, extraction or probe locus, relation observation class selected from {observed, inferred, unknown}, hidden structure, and evidence or assurance pattern governing the claim applications. |
| **Prompt-data-tool flow as authority proof** | A prompt, data, or tool-flow diagram is treated as permission for tool action or proof that authority is safe. | Keep the diagram as a transformation-flow relation or E.18.2 mathematical description. A path from untrusted content to tool action is governed by `SecurityTrustBoundaryStructure`, C.24, E.16, A.20, or A.21 when those claim kinds are being made. |

