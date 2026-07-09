---
chunk_kind: "child"
pattern_id: "E.18.3"
pattern_title: "Constraint-Governed Transformation-Flow Unfolding Structure"
section_id: "E.18.3:5"
section_title: "Worked Slices"
source_path: "FPF-Spec.md"
output_path: "by_section/E.18.3/E.18.3__007_worked-slices.md"
commit_sha: "d77339d7056433de3ee55ad863860ee4b3006f6f"
heading_path:
  - "E.18.3 — Constraint-Governed Transformation-Flow Unfolding Structure"
  - "E.18.3:5 — Worked Slices"
line_start: 78348
line_end: 78371
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

### E.18.3:5 - Worked Slices

**P2W carry-through.** Accepted problem-side records may name distinctions, constraints, and unresolved loci that jointly guide the next FPF use. `E.18.3` can organize the transformation-flow structure among those records, candidate governing-pattern loci, and possible next uses such as pattern-use recommendations, method-selection frames, work-planning seeds, evaluation-refresh frames, or return-to-governing-pattern requests. It does not authorize launch or performed work.

**Transformation-flow mini-example.** A team has a flow card "admitted reference-publication edition changes -> recalculate comparison -> update candidate set -> decide whether to repair." E.18.3 admits only the transformation-flow slice:

```text
transformedEntityOrConcernRef: candidate-set comparison basis
transformationLoci[]: admitted reference-publication edition change; comparison recalculation; retained candidate-set update; repair-decision locus
adjacentGovernedLoci[]: G.2 source-use record or source pack; G.11 source-currentness relation; A.19 comparison relation; C.18 retained-set record; C.32.PAD decision-repair relation
transferOrDependencyRelations[]: comparison basis depends on the admitted reference-publication edition; retained candidate-set update depends on accepted comparison
pathOrPathSliceRefs[]: one teaching slice from edition change to repair decision
guardRefs[]: stop if the changed reference-publication edition is not admitted through the G.2 source-use record or source pack; return if comparison basis changes
preservedTransformationStructure: dependency from admitted reference-publication edition to comparison basis and retained-set update
lostOrHiddenTransformationStructure: alternative comparison branches not shown in the teaching slice
returnToGoverningPatternCondition: G.11 for currentness, A.19 for comparison, C.18 for retained set, C.32.PAD for decision repair
```

The flow card remains a demonstrative slice until those loci and exits are named.

**Architecture P2S projection.** A P2S flow card includes architecture-relevant problem pressure, selected or unknown structures, synthesis loci, and feedback. If a slice inside it is transformation-flow, `E.18.3` names that transformation-flow structure. The architecture use remains with `C.32.P2S` and `C.30.TFS-REL`; the decision remains with `C.32.PAD`.

**Reference-currentness repair.** A path slice relies on an admitted reference-publication edition, a `G.2` source-use record, a source pack, or a telemetry window. If the flow slice itself must be refreshed, E.18 keeps the slice-local refresh boundary. If the claim is source-currentness relation, decay, edition shift, deprecation, reship, or no-change, `G.11` governs it.

