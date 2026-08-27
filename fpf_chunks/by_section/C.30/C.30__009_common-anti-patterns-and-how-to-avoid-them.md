---
chunk_kind: "child"
pattern_id: "C.30"
pattern_title: "Grounded Architecture and Selected-Structure Adequacy"
section_id: "C.30:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30/C.30__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "C.30 — Grounded Architecture and Selected-Structure Adequacy"
  - "C.30:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 58109
line_end: 58123
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
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
  - "C.18"
  - "C.19"
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
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.1"
  - "E.17.2"
  - "E.18"
  - "E.24.PUB"
  - "F.18"
  - "G.5"
  - "G.6"
keywords:
  - "ArchitectureOf@Context"
  - "architecture claim"
  - "architecture question card"
  - "architecture-description boundary"
  - "artifact-as-architecture guard"
  - "candidate architecture use"
  - "grounded architecture"
  - "selected structure"
---

### C.30:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| **Architecture-as-document** | A document, diagram, table, generated relation graph, or dashboard is treated as the architecture or as what makes `ArchitectureRelation` obtain. | Recover the representation and publication objects, exact claim episteme, selected structure, and actual direct relation separately; a carrier creates none of their subject-side facts. |
| **Publication-unit architecture drift** | One publication unit mixes architecture description, evidence claim, gate decision state, decision note, and work authorization under one architecture heading. | Name the exact `ArchitectureRelation` or modal `ArchitectureClaim` content, keep description, view, and publication objects separate, and use the applicable patterns for evidence, gate, decision, and work claims. The publication heading creates no selected structure or subject-side relation. |
| **Module-diagram takeover** | Architecture is reduced to module structure or interface relation. | Recover the structure kind, use `C.30.ASV`, and use the module-and-interface repair pattern when the full module claim is current. |
| **Tool-model lock-in** | A notation or tool model becomes the source of architecture truth. | Recover FPF architecture claim, structures, views, correspondence, and source-return condition. |
| **Evidence laundering** | A published architecture description is used as evidence sufficiency. | Assign the evidence relation or evidence claim to `A.10` or `G.6`; C.30 keeps only the architecture claim, selected-structure, and conditional architecture-description-use boundary; the evidence relation stays with the evidence pattern. |
| **Assurance or safety overread** | Architecture description or LCA diagram is used as assurance or safety case. | Use `B.3`, `A.10`, `G.6`, `C.30.LCA`, or the exact safety or gate pattern according to the claim being made. |
| **Risk color as architecture decision** | A red, yellow, or green risk cell, risk matrix, or maturity score decides the architecture move or resource-allocation priority. | Recover the structure kind under consideration, affected scope, loss, hazard or threat path, source or grounding relation, characteristic scale, comparator, and gate pattern; use the applicable patterns for architecture adequacy, evidence sufficiency, causal proof, assurance proof, resource-allocation reason, and gate-passage claims. |
| **Causal slogan** | Architecture property is said to cause a quality without a bounded claim or independently admitted relation grounding. | Start with `ArchitectureStructuralCharacteristicQBundleClaimLine`; apply C.28 or the applicable evidence, causal-use, or assurance pattern, or use `ArchitectureCharacteristicQBundleClaim` when a durable bounded claim is needed. Name a direct relation only after its defining pattern identifies the participants and its predicate is satisfied. |
| **Architecture-operation overread** | Replacing a block, module, layer, protocol, cache, memory path, or flow relation is treated as improvement by label alone. | Apply `C.30.STRAT` to source labels, then recover the changed structure kind, preserved structure, lost structure, source relation, affected characteristic, and pattern for any decision or evidence claim. |
| **Sterile compliance rewrite** | The text becomes well typed but no longer helps the practitioner act. | Restore a concrete next architecture move, a retainable `ArchitectureQuestionCard@Project` when needed, or the applicable pattern for the separate claim. |

