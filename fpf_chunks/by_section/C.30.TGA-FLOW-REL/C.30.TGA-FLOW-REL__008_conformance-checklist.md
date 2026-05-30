---
chunk_kind: "child"
pattern_id: "C.30.TGA-FLOW-REL"
pattern_title: "Architecture/TGA Flow-Structure Relation"
section_id: "C.30.TGA-FLOW-REL:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TGA-FLOW-REL/C.30.TGA-FLOW-REL__008_conformance-checklist.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.30.TGA-FLOW-REL — Architecture/TGA Flow-Structure Relation"
  - "C.30.TGA-FLOW-REL:7 — Conformance Checklist"
line_start: 52916
line_end: 52930
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
  - "E.10"
  - "E.17"
  - "E.17.0"
  - "E.18"
  - "F.18"
  - "G.6"
keywords:
  - "ArchitectureFlowStructureRelation@TGA"
  - "FlowTransductionStructure"
  - "TGA graph support"
  - "architecture flow relation"
  - "graph/path/crossing"
---

### C.30.TGA-FLOW-REL:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-TGA-FLOW-1 E.18 object.** | The relation names the E.18 graph, path, slice, crossing, or flow valuation object it uses. | Add the exact E.18 reference or use C.30/C.30.ASV without TGA relation. |
| **CC-TGA-FLOW-2 Architecture locus.** | The relation names the architecture description or architecture structural view it relates to. | Add `architectureDescriptionRef` or `architectureStructuralViewRef`, or keep the graph claim inside E.18 only. |
| **CC-TGA-FLOW-3 Functional/flow separation.** | Functional structure and flow/transduction structure remain separate unless a correspondence is declared. | Add `FunctionFlowRelationNote` or remove the functional-architecture claim from the graph sentence. |
| **CC-TGA-FLOW-4 No TGA architecture takeover.** | The TGA graph is not treated as generic architecture ontology or all architecture structure kinds. | Assign generic architecture-description claims to C.30 and keep this pattern to flow/transduction structure. |
| **CC-TGA-FLOW-5 No work overread.** | A graph/path/slice is not treated as work occurrence or work result. | Assign the work claim to A.15 or the governing work-result pattern. |
| **CC-TGA-FLOW-6 No evidence/assurance/gate overread.** | The relation is not used as evidence sufficiency, assurance claim, gate decision, or release permission without exact evidence, assurance, gate, or release pattern application. | Assign the live claim to A.10/G.6, B.3, A.20/A.21, or release loci as live. |
| **CC-TGA-FLOW-7 Causal and mathematical boundaries.** | Causal/intervention and mathematical-lens claims are assigned to C.28 and C.29. | Apply those governing patterns or narrow the relation's admissible use. |
| **CC-TGA-FLOW-8 Pin and scalarization boundary.** | Edition/context/plane pins and no-hidden-scalarization claims remain E.18-governed. | Add E.18 pin/set-return references or remove the comparison/selection claim. |
| **CC-TGA-FLOW-9 Source return.** | Extracted, generated, coarsened, or partial graphs state source-return conditions when hidden distinctions affect action. | Add source-return condition or narrow the admissible use. |
| **CC-TGA-FLOW-10 Useful action.** | The repair leaves a surviving move: name graph/path/crossing relation, add correspondence, return to source, assign the live claim to an exact governing pattern, or stop. | Restore that move, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |

