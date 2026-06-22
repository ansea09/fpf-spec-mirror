---
chunk_kind: "child"
pattern_id: "B.1.2"
pattern_title: "System Aggregation and Holon Delimitation"
section_id: "B.1.2:4"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.2/B.1.2__006_solution.md"
commit_sha: "9b6d71cff42a9ac45e46a2be2d9450f766868bc4"
heading_path:
  - "B.1.2 — System Aggregation and Holon Delimitation"
  - "B.1.2:4 — Solution"
line_start: 30821
line_end: 30897
dependencies:
  - "A.1"
  - "A.12"
  - "A.14"
  - "A.15.1"
  - "A.19"
  - "A.22"
  - "A.3.4"
  - "A.6.5"
  - "A.6.F"
  - "A.6.M"
  - "B.1"
  - "C.13"
  - "C.16"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.AD.BA"
keywords:
---

### B.1.2:4 - Solution

Use B.1.2 to recover a system aggregation relation and its delimitation discipline.

#### B.1.2:4.1 - System Aggregation Relation

```text
SystemAggregationRelation@Context:
  candidateSystemWholeRef: U.System
  boundedContextRef:
  identityOrRecognitionRule:
  componentRelationRefs?
  portionRelationRefs?
  phaseRelationRefs?
  memberRelationRefs?
  holonDelimitationRelationRef:
  externalBoundaryCrossingRelationRefs?
  internalizedBoundaryCrossingRelationRefs?
  functionalElementRefs?
  moduleOrBearerAllocationRefs?
  wholeLevelCharacteristicRefs?
  constructionBasisRef?
  evidenceRelationRefs?
  mathLensOrRepresentationRef?
```

This relation is not a U-kind and not the system itself. It states which relations must be named before a system aggregation claim is relied on.

#### B.1.2:4.2 - Delimitation And Boundary-Crossing

Use `HolonDelimitationRelation@Context` for the current system delimitation: identity rule, included parts, excluded environment, selected structure, and context boundary conditions.

Use `HolonBoundaryCrossingRelation@Context` or a direct owner for relations that cross that delimitation: material flow, energy flow, signal, control, measurement, source use, publication use, evidence relation, transformation, probe relation, supply relation, commitment relation, A.6.C contract-language unpacking, or coupling.

Do not recast crossing relations as parthood merely because the relation is important.

#### B.1.2:4.3 - Boundary-Interface Compatibility Check

When a system aggregate exposes or hides crossing relations, record the compatibility choice:

```text
BoundaryInterfaceCompatibilityCheck@Context:
  systemAggregationRelationRef:
  crossingRelationRef:
  compatibilityDecision: expose | namespace | internalize | exclude | useDirectOwner
  ownerPatternRef:
  evidenceRelationRef?
```

This check is a system-aggregation aid, not a new ontology. It prevents silent loss of external obligations and unmanaged endpoint explosion.

#### B.1.2:4.4 - Whole-Level Characteristics

Roll up system-level characteristics only after the relation and scale are selected.

Useful families include:

- additive quantities such as mass, cost, energy stock, or material amount;
- limiting quantities such as pressure rating, weakest connector, safety class, or availability bottleneck;
- logical or capability claims such as emergency-stop availability or vulnerability exposure;
- architecture characteristics that depend on selected structure.

Use `C.16`, `A.19`, and `C.29` when characteristic space, scale, threshold, or mathematical lens is relied on for the current claim. Use B.2 when redundancy, closure, or coordination creates or reveals a whole that must be reidentified.

#### B.1.2:4.5 - Functional Elements And Bearers

A functional element in a functional view is not automatically a system part.

Recover separately:

- functional behavior or functional element under `A.6.F`;
- physical, organizational, software, or operational bearer under `A.6.M`, A.14, C.13, and architecture owners;
- allocation or correspondence between function and bearer;
- system aggregation only when bearer parthood is independently admitted.

One bearer may realize several functions. One function may require several bearers. This is allocation and correspondence before it is part-whole.

