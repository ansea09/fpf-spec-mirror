---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 60096
line_end: 60108
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.4"
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
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.P2S"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.17.0"
  - "E.18"
  - "E.18.2"
  - "E.18.3"
  - "E.18.NET"
  - "E.24.PUB"
  - "F.18"
  - "G.6"
keywords:
---

### C.30.TFS-REL:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Structure-as-architecture** | The E.18 selected transformation-flow structure is called the whole architecture. | Use C.30 for the actual architecture relation, selected structure, or bounded claim; C.30.AD for description; keep this record only for the transformation-flow use. |
| **Unnamed network as architecture bearer** | A connected network or its graph is assigned maintainability, capability, responsibility, agency, production, required effect, or actual transformation without one containing holon/relation or explicit participating holons. | Select the named-containing-holon or explicit inter-holon branch, restore every characteristic to a named bearer, and keep graph/record outside architecture identity. |
| **Graph-description-as-functional-architecture** | A graph-shaped mathematical description or diagram is treated as functional architecture, functional element, or actual change. | Split functional claim, selected TFS, actual transformation, mathematical description, representation, and publication; add correspondence when needed. |
| **Flow-as-work-log** | Path or slice wording is treated as Work occurrence. | Assign occurrence or result claims to A.15 or P2W and keep E.18 to selected structure, path, slice, or valuation. |
| **Crossing-as-gate-result** | A crossing relation is treated as gate passage. | Assign gate-decision claims to A.21 and keep crossing relation under E.18. |
| **Valuation-as-score** | A flow valuation is used as a generic architecture score. | State E.18 valuation and set-return discipline; assign measurement, characterization, selection, or candidate-set claims to `C.16` or an admitted governing pattern. |
| **Generated relation-graph proof** | A code-agent relation graph or probe output is used as proof of architecture understanding or safety. | Recover source publication/codebase edition, extraction/probe locus, observation class from {observed, inferred, unknown}, unexplored regions, hidden structure, and direct evidence or assurance application. |
| **Prompt-data-tool flow as authority proof** | A prompt, data, or tool-flow diagram is treated as permission for tool action or proof that authority is safe. | Keep it as a transformation-flow use or E.18.2 mathematical description. Route a selected `SecurityTrustBoundaryStructure` view through C.30.ASV; route agentic tool-use and call planning to `C.24`, autonomy-budget enforcement to `E.16`, and gate or release claims to `A.20` or `A.21` when those exact claim kinds are being made. |

