---
chunk_kind: "child"
pattern_id: "C.30.TFS-REL"
pattern_title: "Architecture Transformation-Flow Structure Relation"
section_id: "C.30.TFS-REL:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.TFS-REL/C.30.TFS-REL__008_conformance-checklist.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.30.TFS-REL — Architecture Transformation-Flow Structure Relation"
  - "C.30.TFS-REL:7 — Conformance Checklist"
line_start: 60113
line_end: 60131
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

### C.30.TFS-REL:7 - Conformance Checklist

| ID | Requirement | Failed-check repair |
| --- | --- | --- |
| **CC-C30TFR-1 Flow-structure object.** | The record names the exact E.18 TFS, E.18.NET network, path, slice, crossing, or flow valuation object it uses. | Add the exact E.18 or E.18.NET reference named by value, or use C.30 or C.30.ASV without this record. |
| **CC-C30TFR-2 Architecture locus.** | The record names an actual `ArchitectureRelation`, exact selected architecture structure, exact `ArchitectureStructuralView` or `ArchitectureDescription` episteme, or bounded `ArchitectureClaim`. | Add the exact architecture relation/structure/episteme/claim as the selected use requires; otherwise keep the TFS or network claim with E.18 or E.18.NET, the mathematical-description claim with E.18.2, or the math-lens-use claim with C.29. |
| **CC-C30TFR-3 Functional, required, flow, and actual-change separation.** | Required/desired behavior and effect remain claim content; selected TFS remains structure; an `actualTransformationRef` appears only with the complete A.3.4 changed-referent, boundary, conditions, before/during/after, and continuity/reidentification basis. Functional and flow structure co-reference is explicit rather than assumed. | Repair through `FunctionTransformationFlowRelationNote`; split the required claim, selected structure, and actual transformation; add correspondence or positive selected-structure co-reference only when its predicate is governed. |
| **CC-C30TFR-4 No architecture takeover.** | The selected transformation-flow structure, network, mathematical description, or use record is not treated as generic architecture ontology or all architecture structure kinds. | Assign actual architecture relations, selected architecture-relevant structures, bounded claims, or description use to C.30/C.30.AD and keep this pattern to the architecture-to-transformation-flow trace. |
| **CC-C30TFR-4a Network architecture branch.** | A network use selects exactly one branch. The containing branch has one exact holon and actual architecture relation whose selected structure is the exact network. The inter-holon branch has at least two exact holons, exactly the actual architecture relations and bounded claims this question uses, no containing fields, and `noNetworkBearerHolonAsserted=true`; a singular participant ref never implies a containing architecture. | Complete one branch, remove or reroute a conflicting architecture-side ref, add a participant only when the current question relies on it, or keep the network claim under E.18.NET without architecture use. |
| **CC-C30TFR-4b Named characteristic bearer and representation boundary.** | Every architecture characteristic claimed or used remains on an exact named holon, actual architecture relation, selected structure, view/description episteme, bounded claim, or other governed bearer; no graph, representation, mathematical description, publication, or network record becomes that bearer. | Name the exact bearer under C.30 or its direct owner; demote the visible object to representation, description, or publication use. |
| **CC-C30TFR-4c Member-local, unfolding, and row-reference boundary.** | Every path, slice, crossing, valuation, required effect, or actual transformation named with a network remains bound to its exact owning member TFS and local positions, participants, or bindings; a network-aware unfolding selects the same network through its E.18.3 locator; every `NetworkCrossFlowRelationRowRef` resolves exactly one row in a current record for that network without replacing the obtaining relation occurrence. | Restore the member-local binding or network-locator match; repair or remove a row locator that resolves zero or several rows or points to another network; keep occurrence truth with its direct governor. |
| **CC-C30TFR-5 No Work overread.** | A selected TFS, network, path, or slice is not treated as Work occurrence or work result. | Assign the Work claim to A.15 or the governing work-result pattern. |
| **CC-C30TFR-6 No evidence, assurance, or gate overread.** | The record is not used as evidence sufficiency, assurance claim, gate decision, or release permission without the direct governing application. | Assign the claim being made to A.10, G.6, B.3, A.20, A.21, or the release locus named by value. |
| **CC-C30TFR-7 Causal and mathematical boundaries.** | Causal or intervention claims and mathematical-lens claims are assigned to C.28 and C.29. | Apply those governing patterns or narrow the record's admissible use. |
| **CC-C30TFR-8 Pin and scalarization boundary.** | Edition, context, and plane pins plus no-hidden-scalarization claims remain E.18-governed. | Add E.18 pin and set-return references or remove the comparison or selection claim. |
| **CC-C30TFR-9 Hidden relation return.** | Extracted, generated, coarsened, or partial relation graphs or flow diagrams state the source publication or edition, extraction or probe locus, relation observation class, unexplored regions, and hidden relation-structure return condition when hidden distinctions affect action. | Add the missing relation-structure fields or narrow the admissible use. |
| **CC-C30TFR-10 Useful action.** | The repair leaves a remaining use: name the selected TFS, path, or crossing; choose the containing or inter-holon branch for a selected network; add correspondence; return to source; assign the claim being made to a governing pattern; or stop. | Restore that use, or classify the phrase as reduced-use cue, quote-only wording, blocked transfer, or incomplete rewrite. |
| **CC-C30TFR-11 Lowering and currentness.** | The record states the smallest changed locus when E.18 TFS semantics or pins, E.18.NET network identity or relations, selected network branch or architecture loci, a relied-on row locator, relation observation class, correspondence, hidden relation-structure return, or related governing boundary changes. | Update the affected TFS/network reference, branch, architecture locus, or row locator; narrow admissible use; keep subject claims with their direct owners; lower the record; or block architecture-to-transformation-flow use. |

