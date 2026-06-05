---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "eaafd3a43b9173706e1f8388a3bc94c6445397e4"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 51790
line_end: 51804
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.3"
  - "A.6.F"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.2.1"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.P"
  - "C.30.STRAT"
  - "C.30.TGA-FLOW-REL"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "grounded architecture"
  - "selected structure"
---

### C.30:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Architecture-as-document** | The document, diagram, table, generated relation graph, or dashboard is called the architecture. | Recover carrier, publication, description, or view relation and name `ArchitectureOf@Context` only when selected structure is live. |
| **Publication-unit architecture drift** | One publication unit mixes architecture description, evidence claim, gate decision state, decision note, and work authority under one architecture heading. | Name the source architecture description or view, split evidence claims, gate decision state, decision note, and work authority to exact governing patterns, and keep the publication face subordinate to E.17 and MVPK. A publication heading is not an architecture claim, and a section title is not evidence, gate, decision, or work authority. |
| **Module-diagram takeover** | Architecture is reduced to module structure or interface relation. | Recover structure kind and use `C.30.ASV`; assign full module repair to the exact module-and-interface repair pattern when that claim kind is live. |
| **Tool-model lock-in** | A notation or tool model becomes the source of architecture truth. | Recover FPF architecture claim, structures, views, correspondence, and source-return condition. |
| **Evidence laundering** | A published architecture description is used as evidence sufficiency. | Assign the evidence-path relation or evidence claim to `A.10` or `G.6`; C.30 keeps only the architecture claim, selected-structure, and conditional architecture-description-use boundary; evidence-path relation stays with the evidence pattern. |
| **Assurance or safety overread** | Architecture description or LCA diagram is used as assurance or safety case. | Assign the live claim to `B.3`, `A.10`, `G.6`, `C.30.LCA`, and live safety patterns or gate patterns. |
| **Risk color as architecture decision** | A red, yellow, or green risk cell, risk matrix, or maturity score decides the architecture move or resource-allocation priority. | Recover the live structure kind, affected scope, loss, hazard, or threat path, source relation or grounding relation, characteristic scale, comparator, and gate pattern; do not treat ordinal risk color as architecture adequacy, evidence sufficiency, causal proof, assurance proof, resource-allocation reason, or gate passage. |
| **Causal slogan** | Architecture property is said to cause a quality without a declared relation grounding. | Start with `ArchitectureStructuralCharacteristicQBundleRelationLine`; open `C.28`, evidence-path, causal-use, or assurance claim, or `ArchitectureCharacteristicQBundleRelationRecord` only when that stronger evidence, causal-use, assurance, or full relation claim is live. |
| **Architecture-operation overread** | Replacing a block, module, layer, protocol, cache, memory path, or flow relation is treated as improvement by label alone. | Apply `C.30.STRAT` to source labels, then recover changed structure kind, preserved structure, lost structure, source relation, affected characteristic, and decision or evidence governing pattern. |
| **Sterile compliance rewrite** | The text becomes well typed but no longer helps the practitioner act. | Restore `ArchitectureQuestionCard@Project`, a concrete next architecture move, or a named exact governing pattern application. |

