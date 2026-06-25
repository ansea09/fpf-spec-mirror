---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__005_solution.md"
commit_sha: "792091cf6f89f21f3423d75c72238bb0982777f2"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:2 — Solution"
line_start: 31561
line_end: 31617
dependencies:
  - "A.1.1"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "B.1"
  - "B.1.6"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.18"
  - "E.18.2"
keywords:
---

### B.1.4:2 - Solution

Recover a `ContextTemporalAggregation@Context` before using the aggregate:

```text
ContextTemporalAggregation@Context:
  aggregationConcernRef
  aggregatedEntityOfConcernRef
  boundedContextRef
  aggregationMode: contextualOrder | temporalPhase | declaredMixedUse
  orderedRelationRefs?
  phaseRelationRefs?
  orderSpecRef?
  timeWindowRef?
  carrierIdentityRef?
  independenceOrJoinConditionRefs?
  coverageAndNonOverlapConditionRefs?
  boundaryCrossingRelationRefs?
  relatedMethodRefs?
  relatedMethodDescriptionRefs?
  relatedWorkOccurrenceRefs?
  relatedWorkResourceAggregationRefs?
  relatedTransformationRefs?
  relatedWholeReidentificationRefs?
  evidenceOrSourceRefs
  admissibleUse
  nonAdmissibleOverread
  strongerSourceReturnCondition
```

Use the record as a small typed relation, not as a new durable `U.Level`, `U.Boundary`, `U.Interaction`, or generic process object.

#### B.1.4:2.1 - Two Aggregation Modes

| Mode | Current object | Required relation discipline | Typical use |
| --- | --- | --- | --- |
| Contextual order aggregation | A bounded set of relation positions whose order, partial order, or join structure changes meaning. | `OrderSpec`, ordered relation refs, join or independence conditions, and a bounded context. | Ordered method relation, order-bound argument chain, staged construction description, controlled sequence. |
| Temporal phase aggregation | One carrier considered through phases or time slices. | Carrier identity, `PhaseOf` or phase relation refs, `TimeWindow`, coverage, and non-overlap conditions. | Asset history, revision history, experimental run phases, dated evidence window. |

If one source phrase mixes both modes, split the record. A method may have an ordered relation structure, and the work that enacts it may also have dated phases, but those are different claims.

#### B.1.4:2.2 - Direct Owner Map

| Current claim | Direct owner |
| --- | --- |
| Method as semantic way of doing | `A.3.1` |
| Method description, SOP, algorithm text, simulator configuration, or formal expression | `A.3.2`, with publication owners when publication use is current |
| Work plan | `A.15.2` |
| Dated work occurrence, performed episode, or evidence that work happened | `A.15.1` |
| Work-resource roll-up, spent resource, cost, effort, energy, material, or comparable ledger | `B.1.6` |
| Phase relation, portion relation, membership, or parthood | `A.14`, `B.1`, and `C.13` as appropriate |
| Holon delimitation or boundary-crossing relation | `A.1`, `B.1`, `A.12`, `A.3.4`, or the direct relation owner named by value |
| Bounded change under conditions | `A.3.4` |
| Whole reidentification, emergence-family wording, MHT, MET, MFT, synergy, or metric-mirage wording | Use `B.2.P` to test whether a whole-reidentification problem is current. If it remains current, use `B.2`, `B.2.2`, `B.2.3`, `B.2.4`, or `B.2.5` according to the recovered whole, emergence, autonomy, capability, or supervisor relation claim. |
| Architecture structural view or selected structure | `C.30.ASV`, `A.22`, or the architecture owner named by value |
| Mathematical order, graph, algebraic notation, graph path, or morphism used as expression | Use `C.29` when mathematical-lens adequacy, preserved structure, lost structure, payoff, or stop condition is being evaluated. Use `E.18` when the selected transformation-flow structure is current. Use `E.18.2` when the mathematical expression of that selected structure is current. |

