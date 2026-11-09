---
chunk_kind: "child"
pattern_id: "B.1.4"
pattern_title: "Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
section_id: "B.1.4:2"
section_title: "Solution"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.4/B.1.4__005_solution.md"
commit_sha: "b223469ecafb9735c1d9bac220671e3336618339"
heading_path:
  - "B.1.4 — Specify Order-Sensitive or Temporal Aggregation (Γ_ctx, Γ_time)"
  - "B.1.4:2 — Solution"
line_start: 41956
line_end: 42030
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
  - "B.2"
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

Start with the receiving question and the result it needs. An already adequate aggregation rule and ordinary explanation can be used directly.

1. **Recover the inputs and relations.** Identify the included positions, values, intervals or phases and the objects they concern. Keep their identity and relations grounded in the subject facts and applicable rules. For a temporal input, recover its bearer, temporal reference and exact interval; relate different references only through a justified conversion.
2. **Choose the combining rule and result.** State the operation and what it returns: for example, an ordered relation structure, a combined value, the union of covered intervals or their elapsed span. Supply the order, join, independence, coverage and overlap conditions that this operation actually uses. If the rule needed by the question is missing, retain that gap rather than naming an unsupported aggregate.
3. **Obtain the requested result.** A specification can be sufficient when the task asks how the aggregation is to be performed. When a computed result is needed, apply the selected operation and interpret its result under those conditions. Distinguish an order structure from the result of applying the operations it represents. Section :5 shows why the same inputs can support different warranted results.
4. **Bound the use and stop.** State the supported use and any condition whose failure or uncertainty changes it. Narrow the result or leave the affected conclusion unresolved when its required basis is missing. Use another pattern when a distinct claim needs that pattern's contribution. Stop with the sufficient ordinary answer.

When the receiving use needs an inspectable account, reuse an adequate account or materialize a `ContextTemporalAggregation@Context` record. It describes the independently established inputs, rule and result; it does not establish their subject facts:

```text
ContextTemporalAggregation@Context:
  aggregationConcernRef
  aggregatedEntityOfConcernRef
  aggregationMode: contextualOrder | temporalAggregation
  combiningRuleOrOperator
  resultOrResultSpecification
  includedPositionRefs?
  includedIntervalRefs?
  includedPhaseRefs?
  claimScopeRef?: U.ClaimScope
  orderedRelationRefs?
  temporalRelationRefs?
  phaseRelationRefs?
  orderSpecRef?
  temporalReference?
  timeWindowRef?
  carrierIdentityRefs?
  independenceOrJoinConditionRefs?
  coverageAndOverlapPolicyRefs?
  boundaryCrossingRelationRefs?
  relatedMethodRefs?
  relatedMethodDescriptionRefs?
  relatedWorkOccurrenceRefs?
  relatedWorkResourceAggregationRefs?
  relatedTransformationRefs?
  relatedWholeReidentificationRefs?
  evidenceOrSourceRefs?
  admissibleUse
  stopOrReturnCondition?
  nonAdmissibleOverread?
  strongerSourceReturnCondition?
```

The aggregation concern is the receiving question; the EntityOfConcern is the independently identified subject of the aggregation claim. Included inputs retain their own bearers and identities. Add each optional value when it changes that claim or its use. Facts and evidence needed to warrant the result remain necessary whether or not a reference field is written.

`stopOrReturnCondition?` states an action-changing limit; `strongerSourceReturnCondition?` is used only for a distinct stronger claim that the receiving work needs. Include `nonAdmissibleOverread?` only when it passes F.19's plausible-reader test; `groundedNonAdmissibleOverread?` is an alias for that same optional value.

#### B.1.4:2.1 - Two Aggregation Modes

| Mode | Current object | Required relation discipline | Typical use |
| --- | --- | --- | --- |
| Contextual order aggregation | Exact positions and relation facts whose order, partial order or join structure matters to the stated use. | Included inputs, combining rule and required result, `OrderSpec`, ordered relation refs, join or independence conditions when used, and ClaimScope when needed. | Ordered method relation, order-bound argument chain, staged construction description, controlled sequence. |
| Temporal aggregation | Exact interval or time-indexed facts about named bearers or occurrences. | Input identities and temporal relations, temporal reference or justified conversion, `TimeWindow`, combining rule, coverage and overlap policy. The proper-phase profile additionally requires one continuing carrier and the direct phase relation. | Work-interval union or elapsed span, asset phases, observation windows, or chronology over exact episteme identities. For proper phases of one episteme, its complete C.2.1 identity triple stays fixed; distinct editions require their own identities and any claimed edition relation. |

When a use combines order and temporal claims, distinguish what each contributes and state the correspondence on which the joint result relies; one sufficient account may contain both. A Method may have an ordered relation structure. Work that enacts it may have exact A.15.1 temporal parts, episodes, operational parts or separate occurrences, while C.27.TA supplies any independently declared overlap or other interval relation. Aggregate those actual inputs under the chosen rule. Use `PhaseOf` only for the proper-phase profile of one enduring carrier, not as a substitute for Work or temporal relations.

#### B.1.4:2.2 - Where Stronger Claims Go

| Current claim | Pattern to use |
| --- | --- |
| Method as semantic way of doing | `A.3.1` |
| Method-description membership or a description-use question | `A.3.2` defines membership and description boundaries. For SOPs, code or simulator configurations, use A.3.2 when the question is whether the identified episteme has an admitted Method as its exact EntityOfConcern and makes a substantive claim about it as a way of doing; representation form alone does not select the branch. Use the applicable subject or publication pattern for another claim. |
| Work plan | `A.15.2` |
| Dated work occurrence, performed episode, or evidence that work happened | `A.15.1` |
| Work-resource roll-up, spent resource, cost, effort, energy, material, or comparable ledger | `B.1.6` |
| Episteme identity and historical continuity between distinct epistemes | `C.2.1`; aggregate only exact identities and an already obtaining `EpistemeEditionRelation` when the bounded use needs their chronology |
| Proper `PhaseOf`, portion, membership, or other parthood relation for a non-Work carrier | `A.14`, `B.1`, and `C.13` as appropriate; Work temporal and part relations remain with `A.15.1` |
| Holon delimitation or boundary-crossing relation | `A.1`, `B.1`, `A.12`, `A.3.4`, or the pattern that defines the exact relation |
| Bounded change under conditions | `A.3.4` |
| Whole reidentification, emergence-family wording, MHT, MET, MFT, synergy, or metric-mirage wording | Use `B.2.P` when emergence-family wording hides the claim kind. If a whole-reidentification question remains, including one raised by an autonomy or capability change, use `B.2`; `B.2.2` and `B.2.3` handle System and Episteme result recognition, and `B.2.4` is the capability/functioning decision bridge. Use `B.2.5` separately for an exact two-sided supervisor-subholon feedback claim, whether or not whole reidentification is current. |
| Architecture structural view or selected structure | `C.30.ASV`, `A.22`, or the pattern that defines or tests the architecture claim |
| Mathematical order, graph, algebraic notation, graph path or morphism used as expression | Use the applicable mathematical or subject rule directly when it supplies the result. Use `C.29` for a separate unresolved representation-choice, transfer or reliance question. Use `E.18` when its selected transformation-flow structure is the subject, and `E.18.2` for a mathematical description of that TFS or a selected TFS network. |

