---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__006_solution.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:4 — Solution"
line_start: 78264
line_end: 78347
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.22.CGUS"
  - "A.3.4"
  - "A.6.3.NAR"
  - "B.3"
  - "C.29"
  - "C.30.TFS-REL"
  - "C.32.P2S"
  - "E.17"
  - "E.18"
  - "E.18.1"
  - "E.18.2"
  - "E.23"
  - "G.11"
keywords:
---

### E.18.3:4 - Solution

Select `ConstraintGovernedTransformationFlowUnfoldingStructure@Context <: U.Structure` as the E.18 transformation-flow specialization of `ConstraintGovernedUnfoldingStructure@Context`.

```text
ConstraintGovernedTransformationFlowUnfoldingStructure@Context:
  kind: U.Structure
  unfoldingStructureRef:
  boundedContextRef:
  transformedEntityOrConcernRef:
  transformationLoci[]:
  adjacentGovernedLoci[]:
  transferOrDependencyRelations[]:
  pathOrPathSliceRefs[]:
  crossingRefs[]:
  guardRefs[]:
  flowValuationRef?:
  methodWorkLinkageRef?:
  evidenceOrAssuranceLinkageRef?:
  architectureUseRef?:
  narrativeOrPublicationUseRef?:
  preservedTransformationStructure:
  lostOrHiddenTransformationStructure:
  nonAdmissibleOverreads:
  returnToGoverningPatternCondition:
  stopOrReopenCondition:
```

The record is admitted only when the substrate is bounded transformation-flow structure. `A.3.4` governs each atomic bounded transformation claim. `E.18` governs the compound structure over transformations, crossings, path slices, guards, valuations, and structure-positioned loci. This pattern governs the narrower `U.Structure` specialization that says how the current transformation-flow structure unfolds toward next uses without becoming those uses.

`methodWorkLinkageRef?` may point to one `MethodWorkUnfoldingLinkage@Context` when the method-work relation itself must stay inspectable. If only a method, method description, work plan, work-entry readiness, or performed-work claim is current, point directly to the A.3 or A.15 governing record instead of creating a linkage record.

`pathOrPathSliceRefs[]` does not make the structure a chain. A transformation-flow unfolding structure may branch, join, cycle, expose partial orders, or keep several guarded continuations live. A path slice is one selected traversal for explanation, comparison, or local review.

#### E.18.3:4.0a - Field Glosses

The record is a transformation-flow `U.Structure` specialization. Fields that point outside transformation-flow name adjacent governed loci; they do not transfer authority into E.18.3.

| Field | What this slot names | Not this | Direct exit when stronger claim is current |
| --- | --- | --- | --- |
| `unfoldingStructureRef` | the A.22.CGUS structure record or local CGUS block being specialized | not a route card or workflow title | `A.22.CGUS` for the generic structure |
| `transformedEntityOrConcernRef` | entity or concern whose transformation-flow unfolding is organized | not the carrier, diagram, or method description | direct pattern for that EntityOfConcern |
| `transformationLoci[]` | selected positions in the E.18 transformation-flow structure | not a performed sequence | `E.18` and `A.3.4` |
| `adjacentGovernedLoci[]` | method, work, evidence, architecture, publication, or refresh positions adjacent to the flow | not claims governed by E.18.3 itself | direct governing pattern for each adjacent locus |
| `transferOrDependencyRelations[]` | flow relations or dependencies among loci | not proof that a work order is feasible | `E.18`, `A.6.0`, `A.6.5`, or C.29 when a lens is current |
| `pathOrPathSliceRefs[]` | selected traversal or local slice through the flow | not the whole topology and not a project procedure | `DemonstrativeUnfoldingSlice@Context`, E.18, or A.15 family as current |
| `crossingRefs[]` | boundary-crossing positions in the selected flow | not gate passage | `A.20`, `A.21`, or E.18 crossing discipline |
| `guardRefs[]` | conditions that permit or block a continuation | not evidence or assurance by itself | `A.20`, `A.21`, `A.10`, or `B.3` as current |
| `flowValuationRef?` | valuation over the selected flow relation | not an architecture score or decision | E.18 valuation discipline; comparison or decision patterns when current |
| `methodWorkLinkageRef?` | optional A.15-owned relation record for method and work linkage | not work authorization | `A.15` and A.15 child patterns |
| `architectureUseRef?` | optional C.32.P2S or C.30.TFS-REL architecture-use relation | not architecture decision or description | `C.32.P2S`, `C.30`, `C.30.TFS-REL`, `C.32.PAD`, or `C.30.AD` |
| `preservedTransformationStructure` | transformation-flow structure kept by the unfolding use | not the complete structure in a source description, source-use record, or observed system | `C.33` or `C.34` when preservation adequacy is current |
| `lostOrHiddenTransformationStructure` | transformation-flow structure omitted, coarsened, or not recoverable | not a failure by itself | return to E.18, C.33, C.34, or the receiving governing pattern for omitted or coarsened structure |
| `nonAdmissibleOverreads` | blocked stronger readings for this flow use | not a catalogue of unrelated mistakes | direct pattern needed for the blocked claim |
| `returnToGoverningPatternCondition` | condition that sends the next claim to the direct pattern | not a local mini-ontology of reopening | receiving governing pattern named by value |
| `stopOrReopenCondition` | condition to stop at a description or reopen the smallest affected relation | not a `G.11` refresh unless currentness is the claim | `G.11` only for currentness or decay; direct governing pattern otherwise |

#### E.18.3:4.1 - Adjacent Locus Rule

An adjacent governed locus can be present in the unfolding structure, but its stronger claim remains outside this pattern.

| Adjacent locus | Present in E.18.3 as | Direct governing pattern for stronger claim |
| --- | --- | --- |
| Method selection or method relation | locus, dependency, or linkage ref | `A.3.1`, `A.3.2`, `B.1.5`, local method patterns |
| Work planning or work occurrence | locus, readiness dependency, or work linkage ref | A.15 family, especially `A.15.2`, `A.15.5`, `A.15.1` |
| Evidence, assurance, or gate | evidence or gate linkage ref, crossing, guard, or readiness condition | `A.10`, `B.3`, `A.20`, `A.21`, `G.6` |
| Architecture use | architecture-use ref over the current transformation-flow structure when it is used inside an architecture claim | `C.30`, `C.30.TFS-REL`, `C.32.P2S`, `C.32.PAD` |
| Narrative or publication use | demonstrative slice, view, publication, or rendering ref | `A.6.3.NAR`, `E.17`, `E.17.0` |
| Currentness or slice-local refresh | path-slice currentness or refresh trigger | `G.11` for currentness; `E.18` for slice-local flow refresh |

#### E.18.3:4.2 - Demonstrative Slice Rule

A path slice, flow card, worked example, replay, or first-use explanation is a `DemonstrativeUnfoldingSlice@Context` when it teaches or demonstrates an admissible traversal. It must state included loci, omitted branches, loop compression, traversal rule, and return condition when those affect use.

Do not infer that the demonstrated order is the project work order. If work order is current, open the work plan or method-description pattern.

Do not infer that the demonstrated path is the whole transformation-flow topology. If the underlying flow has branches, joins, cycles, alternatives, or partial orders, name what the slice omits or compresses before relying on it for comparison, architecture, evidence, or work planning.

A path slice or flow card can still be useful before work starts. Use it as a slot-filling scaffold: each visible step should either fill a transformation locus, crossing, guard, valuation, preserved/lost transformation-structure field, adjacent-governing-pattern exit, stop condition, or return condition, or else be rejected as a teaching-only position. This keeps attention on the objects being planned while the team is still discovering constraints. The slice is not ready to guide method, work, evidence, gate, architecture, or publication claims until the receiving direct governing pattern has admitted that claim.

#### E.18.3:4.3 - Boundary

This `U.Structure` specialization is not a second transformation ontology, workflow, method, work plan, performed work, mathematical graph, publication, evidence relation, gate decision, architecture decision, or architecture description. It is a transformation-flow structure over transformation loci plus the exit map to the direct patterns that govern those stronger claims.

