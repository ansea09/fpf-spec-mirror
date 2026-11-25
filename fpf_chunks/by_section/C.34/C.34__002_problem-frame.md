---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
section_id: "C.34:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__002_problem-frame.md"
commit_sha: "423f9d3fef92bafec7b092b910e8ce056a0f607d"
heading_path:
  - "C.34 — Assess Structural Correspondence for Architecture Use (Equivalence and Morphisms)"
  - "C.34:1 — Problem frame"
line_start: 85262
line_end: 85314
dependencies:
  - "A.22"
  - "A.6.3.NAR"
  - "A.6.M"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.18"
  - "F.15"
  - "F.9"
keywords:
  - "directionality"
  - "equivalence"
  - "lost structure"
  - "mapping mode"
  - "morphism"
  - "preserved structure"
  - "scope"
  - "structural correspondence"
---

### C.34:1 - Problem frame

Use this pattern when two descriptions, views, models, generated outputs, or realized observations that carry or describe selected structure are being treated as same enough for architecture work and the practitioner must say what selected structure is preserved, what is lost, and which use the correspondence licenses.

Primary working reader: an architect, reviewer, or model-assisted practitioner comparing views, descriptions, source models, generated graphs, candidate architectures, realized structures, abstraction levels, coarsened models, or transformed models.

Typical entry phrases:

```text
"These two diagrams look equivalent; what relation is preserved?"
"The model query and the architecture view should correspond; what was lost in projection?"
"The generated graph matches the module graph; is the semantic relation the same?"
"This candidate preserves dataflow but changes control authority."
"The neural architecture replacement keeps shape but changes routing and memory placement."
"The narrative order preserves the architecture trade-off; what selected source structure is still same enough for this use?"
```

The first useful result explains which correspondence supports the intended architecture use. An ordinary account can suffice; reuse an adequate existing account. `StructuralPreservationAdequacyNote@Context` is an optional working form:

```text
StructuralPreservationAdequacyNote@Context:
  selectedSourceStructureRefs:
  selectedTargetStructureRefs:
  architectureClaimRef?:
  mappingMode:
    exactEquivalence | isomorphism | homomorphism | correspondence |
    projection | abstraction | coarsening | simulationRelation |
    nearSameness | declaredOther
  preservedRelationsOrConstraints:
  preservedInvariantsOrCompositions?:
  lostStructure?:
  relationTypeSemantics?:
  relationObservationClass?:
  directionality:
  scopeOrScaleWindow?:
  lensUseOutputRef?:
  correspondenceRecordRef?:
  constraintGovernedUnfoldingStructureRefs?:
  admissibleUse:
  nonAdmissibleUse?:
  preservationLossReturnCondition?:
  nextClaimOrRuleRef?:
  receivingClaimKind?:
```

After using C.34, another practitioner can recover the claimed correspondence, preserved structure, direction and scope, any loss or uncertainty that limits reliance, and the use it supports.

What C.34 buys in practice: the practitioner can say "same enough for this use" without implying stronger equivalence. The pattern makes sameness conditional on preserved relation, declared loss, and receiving use.

Name the conclusion you want to carry from one model to the other. Identify what makes it true in the first. Look for that relation, or a rule from which it follows, in the second.

For a current claim limited to mathematical-lens use, generic bridge translation, measurement, structural view adequacy, architecture-description correspondence, candidate synthesis, decision, evidence, assurance, gate, release, or work authorization, use the pattern that defines or tests it. Use C.34 only for the architecture-specific preservation claim.

