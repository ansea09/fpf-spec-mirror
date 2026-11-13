---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:2"
section_title: "Solution — separate measurement from aggregation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__005_solution-separate-measurement-from-aggregation.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:2 — Solution — separate measurement from aggregation"
line_start: 44857
line_end: 44926
dependencies:
  - "A.1"
  - "A.10"
  - "A.14"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1"
  - "B.1.4"
  - "B.1.6"
  - "B.2"
  - "B.2-family"
  - "B.2.P"
  - "C.13"
  - "C.16"
  - "C.2.1"
  - "C.27"
  - "C.29"
  - "E.17"
  - "G.11"
  - "G.6"
keywords:
---

### B.1.6:2 - Solution — separate measurement from aggregation

Start with the resource question and the values needed to answer it. State the result:

> Under rule `P`, the resource values attributed to the included subjects `S` within accounting boundary `B` and time window `T` yield typed result `R`, with the stated qualifications. The result statement identifies those inputs and grounds.

A sufficient ordinary sentence or table can state this claim. Stop when it answers the receiving resource question with the required basis. If a needed input or relation remains unresolved, keep the dependent result or use unresolved while retaining supported components or a sufficient narrower result.

For each input, retain its subject, resource Characteristic, Scale, applicable Unit, attribution basis and uncertainty relevant to the use. A claimed performed measurement retains its C.16 Work and result; an estimated or derived value retains the source values, model and conditions that warrant it. A ledger row supplies no missing basis merely by displaying the value.

`WorkResourceAggregation@Context` is one possible descriptive outline for the aggregation claim. Use it when that organization helps the receiving use; ordinary prose or another adequate representation can carry the same content. Fields marked `?` are included when the corresponding claim or use needs them; the conditions below govern their required content:

```text
WorkResourceAggregation@Context:
  aggregationConcernRef
  claimScopeRef?: U.ClaimScope
  accountingBoundaryRefs
  timeWindowRefs
  includedSubjectRefs
  aggregatedWorkOccurrenceRefs?
  resourceUseRelationRefs?
  workPartOrOverlapRelationRefs?
  nonWorkCarrierPhaseRelationRefs?
  resourceCharacteristicRefs
  resourceValueBasisRefs
  measurementWorkRefs?
  measurementResultEpistemeRefs?
  aggregationMethodRef?
  aggregationOperationDeclarationRef?
  aggregationPolicyRef
  conversionOrNormalizationRefs?
  aggregationWorkRef?
  aggregationResultRef
  aggregationResultEpistemeRef?
  provenancePathRefs?
  admissibleUse
  stopOrReturnCondition
  nonAdmissibleOverread?
```

`stopOrReturnCondition` states when to stop or return to another pattern. Include `nonAdmissibleOverread?` only when it passes F.19's plausible-reader test. `groundedNonAdmissibleOverread?` is an alias for that same optional value.

Recover the following content for the claims made and the use being proposed:

- a **resource Characteristic** says which quantity or property is accounted for;
- each **resource value** retains its attribution basis: a claimed performed measurement has C.16 measurement Work and a measurement-result episteme; an estimated or derived value keeps its source values, model and conditions. Retain Scale, applicable Unit, time stance, and the calibration and uncertainty basis needed for the use;
- the **aggregation policy** states the inclusion rule and output kind, together with the conversion, normalization, weighting, missing-value, allocation, uncertainty and overlap rules needed to interpret or justify this result. Identify the policy edition when the result or its use depends on that edition;
- when the claim asserts **dated aggregation Work**, or the receiving use needs that occurrence, A.13 identifies its performer and A.15.1 independently admits it as `U.Work`. If assignment-bound attribution is also needed, F.6 checks that relation separately. The Method, inputs through direct relations or A.6.1 bindings, resources and temporal extent retain their grounds;
- the **B.1.6 aggregation result** is the typed total, vector, interval or bounded estimate warranted by the input values, included accounting subjects and operative rules;
- the **result statement** conveys the result, included subjects, rule, boundary, time basis, qualifications and relevant uncertainty. When the receiving claim or use needs a claim-bearing episteme, identify it through C.2.1 by its claim content, EntityOfConcern and effective ReferenceScheme. Keep the resource value, claim content, episteme and expression distinct; and
- keep the **source basis** recoverable: the measurement or estimate sources, operative rules and derivations needed to justify the result. Use A.10 when source-to-use reliance must be replayable, and G.6 when that chain needs a stable address for citation, replay, audit or refresh. Apply G.11 when currentness affects the use.

A ledger or other representation may describe this account. Establish each Work, participation, measurement, part/overlap or result-identity claim on which the proposed use depends under its predicate; an adequate existing representation can then carry the warranted result.

#### B.1.6:2.1 - Subject Pattern Map

| Claim | Subject pattern |
| --- | --- |
| Resource Characteristic, Scale, applicable Unit and value-attribution basis | `C.16` for measurement and derived value attribution; for a claimed measurement Work, A.13 identifies its performer and A.15.1 independently admits the occurrence. Add F.6 when assignment-bound attribution is needed, and A.6.1 for bindings when used. |
| Dated aggregation Work and performer | A.13 identifies the performer, then A.15.1 independently admits the Work. Add F.6 only if the result must also identify the assignment under which the Work was performed. Method enactment and inputs remain separately governed, including A.6.1 bindings when used. |
| Work temporal part, episode, operational part, partition, overlap, retry, resumption, or later occurrence | `A.15.1` and the Work relation pattern; use `B.1.4` only to aggregate already recovered temporal relations |
| Proper temporal restriction of another enduring carrier | that carrier's identity pattern plus `A.14` `PhaseOf`; never a substitute for Work relations |
| Overlap, shared-stock, boundary, and deduplication facts | C.27.TA for interval overlap; the stock, resource-use, boundary, or accounting relation pattern for the other fact |
| Aggregation policy and typed aggregation result | `B.1.6` |
| Measurement-result and aggregation-result epistemes | `C.2.1`; A.15.PROD only when their inception through work matters |
| Source recovery, replayable reliance, provenance or publication | Recover the sources needed for the claim. Use `A.10` for a needed replayable source-to-use reliance account, `G.6` for a needed stable address of that chain, and `E.17` for a publication question. |
| Edition currentness | `G.11` |
| Planned work or resource readiness | `A.15.2` or `A.15.5`, never a measured aggregation result |
| Transformation, whole reidentification, assurance, comparison, or decision | the applicable A.3.4, B.2, B.3, A.19, C.11, or other pattern for that claim |

