---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Contextual and Temporal Aggregation"
section_id: "B.1.4:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__005_solution.md"
commit_sha: "434e17ec848bb7f49e6da99dfc268effb2b5b9af"
heading_path:
  - "B.1.4 — Contextual and Temporal Aggregation"
  - "B.1.4:2 — Solution"
line_start: 37003
line_end: 37063
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
  - "C.2.1"
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
  includedPositionRefs?
  includedPhaseRefs?
  claimScopeRef?: U.ClaimScope
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
  stopOrReturnCondition
  groundedNonAdmissibleOverread?
  strongerSourceReturnCondition
```

Use the record as a small typed relation, not as a new durable `U.Level`, `U.Boundary`, `U.Interaction`, or generic process object.

#### B.1.4:2.1 - Two Aggregation Modes

| Mode | Current object | Required relation discipline | Typical use |
| --- | --- | --- | --- |
| Contextual order aggregation | An exact set of relation positions whose order, partial order, or join structure changes meaning for the stated use. | Included positions, `OrderSpec`, ordered relation refs, join or independence conditions, and ClaimScope when needed. | Ordered method relation, order-bound argument chain, staged construction description, controlled sequence. |
| Temporal phase aggregation | One enduring carrier considered through exact proper phases or time slices. | Carrier identity rule, included phases, `PhaseOf` or another direct phase relation, `TimeWindow`, coverage, and non-overlap conditions. For an unchanged episteme, the complete C.2.1 identity triple stays fixed. | Asset history, proper restriction of one unchanged episteme, experimental-carrier phases, dated evidence window. Distinct episteme editions first require C.2.1 identities and an independently obtaining edition relation. |

If one source phrase mixes both modes, split the record. A Method may have an ordered relation structure; the Work that enacts it may have exact A.15.1 temporal parts, episodes, operational parts, or separate occurrences, while C.27.TA supplies any independently declared overlap or other interval relation the receiving use aggregates. Those are different claims, and generic `PhaseOf` does not replace the Work or temporal relations.

#### B.1.4:2.2 - Where Stronger Claims Go

| Current claim | Pattern to use |
| --- | --- |
| Method as semantic way of doing | `A.3.1` |
| Method description, SOP, algorithm text, simulator configuration, or formal expression | `A.3.2`, with publication owners when publication use is current |
| Work plan | `A.15.2` |
| Dated work occurrence, performed episode, or evidence that work happened | `A.15.1` |
| Work-resource roll-up, spent resource, cost, effort, energy, material, or comparable ledger | `B.1.6` |
| Episteme identity and historical continuity between distinct epistemes | `C.2.1`; aggregate only exact identities and an already obtaining `EpistemeEditionRelation` when the bounded use needs their chronology |
| Proper `PhaseOf`, portion, membership, or other parthood relation for a non-Work carrier | `A.14`, `B.1`, and `C.13` as appropriate; Work temporal and part relations remain with `A.15.1` |
| Holon delimitation or boundary-crossing relation | `A.1`, `B.1`, `A.12`, `A.3.4`, or the pattern that defines the exact relation |
| Bounded change under conditions | `A.3.4` |
| Whole reidentification, emergence-family wording, MHT, MET, MFT, synergy, or metric-mirage wording | Use `B.2.P` to test whether a whole-reidentification problem is current. If it remains current, use `B.2`, `B.2.2`, `B.2.3`, `B.2.4`, or `B.2.5` according to the recovered whole, emergence, autonomy, capability, or supervisor relation claim. |
| Architecture structural view or selected structure | `C.30.ASV`, `A.22`, or the pattern that defines or tests the architecture claim |
| Mathematical order, graph, algebraic notation, graph path, or morphism used as expression | Use `C.29` when mathematical-lens adequacy, preserved structure, lost structure, payoff, or stop condition is being evaluated. Use `E.18` when the selected transformation-flow structure is current. Use `E.18.2` when the mathematical expression of that selected structure is current. |

