---
chunk_kind: "child"
pattern_id: "C.34"
pattern_title: "Structural Correspondence, Equivalence, and Morphism Adequacy"
section_id: "C.34:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.34/C.34__002_problem-frame.md"
commit_sha: "f7c7e93f137a4691b390d46046428434e847099d"
heading_path:
  - "C.34 — Structural Correspondence, Equivalence, and Morphism Adequacy"
  - "C.34:1 — Problem frame"
line_start: 62147
line_end: 62198
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

Use this pattern when two structure-bearing objects are being treated as the same enough for architecture work and the practitioner must say what selected structure is preserved, what is lost, and which use the correspondence licenses.

Primary working reader: an architect, reviewer, or model-assisted practitioner comparing views, descriptions, source models, generated graphs, candidate architectures, realized structures, abstraction levels, coarsened models, or transformed models.

Typical entry phrases:

```text
"These two diagrams look equivalent; what relation is actually preserved?"
"The model query and the architecture view should correspond; what was lost in projection?"
"The generated graph matches the module graph; is the semantic relation the same?"
"This candidate preserves dataflow but changes control authority."
"The neural architecture replacement keeps shape but changes routing and memory placement."
"The narrative order preserves the architecture trade-off; what source structure is still same enough for this use?"
```

The first useful output is `StructuralPreservationAdequacyNote@Context`:

```text
StructuralPreservationAdequacyNote@Context:
  sourceStructureRefs:
  targetStructureRefs:
  architectureClaimRef?:
  mappingMode:
    exactEquivalence | isomorphism | homomorphism | correspondence |
    projection | abstraction | coarsening | simulationRelation |
    nearSameness | declaredOther
  preservedRelationsOrConstraints:
  preservedInvariantsOrCompositions?:
  lostStructure:
  relationTypeSemantics?:
  sourceObservationClass?:
  directionality:
  scopeOrScaleWindow?:
  lensUseOutputRef?:
  correspondenceRecordRef?:
  admissibleUse:
  nonAdmissibleUse:
  sourceReturnCondition:
  receivingOwnerOrPatternRef:
  receivingClaimKind:
```

Adoption test: after using C.34, another practitioner can tell which mapping mode is being claimed, which structure is preserved, which structure is lost, whether the relation is directional or scoped, and which downstream claim is licensed.

What C.34 buys in practice: the practitioner can say "same enough for this use" without smuggling in stronger equivalence. The pattern makes sameness conditional on preserved relation, declared loss, and receiving use.

Ordinary working move: put the source and target structures side by side, circle the relation or constraint that must survive, name the relation that does not survive, and choose the weakest mapping word that still supports the next use.

Not this pattern when the current claim is only mathematical-lens use, generic bridge translation, measurement, structural view adequacy, architecture-description correspondence, candidate synthesis, decision, evidence, assurance, gate, release, or work authorization. Use the direct owner and keep C.34 only for the architecture-specific preservation claim.

