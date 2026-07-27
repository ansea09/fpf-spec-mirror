---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__008_conformance-checklist.md"
commit_sha: "1f413fcd23f4ea26956a45d67dde57bb233f6ad9"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:7 — Conformance Checklist"
line_start: 62076
line_end: 62091
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

### C.30.TFS-REL:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30TFR-1 E.18 object.** | The relation names the E.18 selected transformation-flow structure, path, slice, crossing, or flow valuation object it uses. | Add the E.18 object reference named by value or use C.30 or C.30.ASV without this relation. |
| **CC-C30TFR-2 Architecture locus.** | The relation names `ArchitectureOf@Context`, selected architecture-relevant structure, architecture structural view, or conditional `ArchitectureDescription@Context` use it relates to. | Add `architectureClaimRef`, `selectedArchitectureStructureRefs`, `architectureStructuralViewRef`, or `architectureDescriptionRef` when durable description use is being made; otherwise keep the selected-structure claim inside E.18, the mathematical-description claim inside E.18.2, or the math-lens-use claim inside C.29. |
| **CC-C30TFR-3 Functional and flow separation.** | Functional structure and transformation-flow structure remain separate unless correspondence or positive selected-structure co-reference is declared. | Add `FunctionTransformationFlowRelationNote`, add the co-reference check, or remove the functional-architecture claim from the flow sentence. |
| **CC-C30TFR-4 No architecture takeover.** | The selected transformation-flow structure or its mathematical description is not treated as generic architecture ontology or all architecture structure kinds. | Assign grounded architecture claims, selected architecture-relevant structures, or conditional architecture-description use to C.30 and keep this pattern to the architecture-to-transformation-flow relation. |
| **CC-C30TFR-5 No work overread.** | A selected structure, path, or slice is not treated as work occurrence or work result. | Assign the work claim to A.15 or the governing work-result pattern. |
| **CC-C30TFR-6 No evidence, assurance, or gate overread.** | The relation is not used as evidence sufficiency, assurance claim, gate decision, or release permission without evidence named by value, assurance, gate, or release pattern application. | Assign the claim being made to A.10, G.6, B.3, A.20, A.21, or the release locus named by value when a release claim is being made. |
| **CC-C30TFR-7 Causal and mathematical boundaries.** | Causal or intervention claims and mathematical-lens claims are assigned to C.28 and C.29. | Apply those governing patterns or narrow the relation's admissible use. |
| **CC-C30TFR-8 Pin and scalarization boundary.** | Edition, context, and plane pins plus no-hidden-scalarization claims remain E.18-governed. | Add E.18 pin and set-return references or remove the comparison or selection claim. |
| **CC-C30TFR-9 Hidden relation return.** | Extracted, generated, coarsened, or partial relation graphs or flow diagrams state the source publication or edition, extraction or probe locus, relation observation class, unexplored regions, and hidden relation-structure return condition when hidden distinctions affect action. | Add the missing relation-structure fields or narrow the admissible use. |
| **CC-C30TFR-10 Useful action.** | The repair leaves a remaining use: name selected structure, path, or crossing relation; add correspondence; return to source; assign the claim being made to a governing pattern; or stop. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-C30TFR-11 Lowering and currentness.** | The relation states the smallest changed locus when E.18 semantics or pins, relation observation class, architecture locus, correspondence, hidden relation-structure return, or related governing boundary changes. | Update the affected reference, narrow admissible use, keep the selected-structure claim inside E.18, keep the mathematical-description claim inside E.18.2, keep math-lens use inside C.29, apply the governing pattern to the non-flow claim, lower the relation, or block architecture-to-transformation-flow use. |

