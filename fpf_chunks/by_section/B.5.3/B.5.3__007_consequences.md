---
chunk_kind: "child"
pattern_id: "B.5.3"
pattern_title: "Role-Projection Bridge"
section_id: "B.5.3:6"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.3/B.5.3__007_consequences.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "B.5.3 — Role-Projection Bridge"
  - "B.5.3:6 — Consequences"
line_start: 33901
line_end: 33909
dependencies:
  - "A.2"
  - "C.3"
keywords:
  - "concept bridge"
  - "domain-specific vocabulary"
  - "mapping"
  - "terminology"
---

### B.5.3:6 - **Consequences**

| Benefits | Trade-offs / Mitigations |
| :--- | :--- |
| **Semantic Richness and Precision:** The pattern allows domain-specific constraints and rules to be formally integrated into the model, enabling much more powerful automated checking and reasoning. | **Increased Modeling Granularity:** It introduces a layer of indirection (`Entity → Role → U.Type`) that modelers must learn. *Mitigation:* Tooling can automate much of this, suggesting relevant roles based on the context or domain. |
| **Multi-Domain Integration:** The pattern provides a clean and robust mechanism for a single model to incorporate concepts from multiple, diverse domains without conflict. | - |
| **Preserves a Lean Kernel:** The FPF kernel remains small and universal, with all domain-specific complexity handled in a modular, plug-in fashion via `Role` libraries. | - |
| **Enhanced Traceability and Clarity:** The roles an entity plays are explicit assertions. This makes the model's intent clear and auditable. | - |

