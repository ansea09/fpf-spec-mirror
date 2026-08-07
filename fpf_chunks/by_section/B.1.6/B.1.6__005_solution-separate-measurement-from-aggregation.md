---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:2"
section_title: "Solution — separate measurement from aggregation"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__005_solution-separate-measurement-from-aggregation.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:2 — Solution — separate measurement from aggregation"
line_start: 36866
line_end: 36925
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
  - "C.16 measurement work/result episteme"
  - "Scale/Unit"
  - "aggregation work"
  - "allocation/deduplication"
  - "dated work set"
  - "edition-pinned aggregation policy"
  - "provenance"
  - "resource Characteristic"
  - "typed aggregation result"
  - "typed input"
  - "uncertainty"
  - "work parthood/phase/overlap"
  - "work-resource aggregation"
---

### B.1.6:2 - Solution — separate measurement from aggregation

Start with one direct sentence:

> Dated aggregation work `W_agg` applied policy `P` to the exact C.16 resource-result epistemes for work set `W_set`, under declared work-part/overlap relations and accounting boundary `B`, and obtained aggregation result `R_agg`; C.2.1 episteme `E_agg` states that result and A.10/G.6 record its provenance.

If any referenced resource value lacks its resource Characteristic, measurement work, result episteme, Scale/Unit, uncertainty when current, or provenance, it is not repaired by adding a ledger row.

`WorkResourceAggregation@Context` is a descriptive account for one aggregation claim:

```text
WorkResourceAggregation@Context:
  aggregationConcernRef
  boundedContextRef
  accountingBoundaryAndTimeWindowRefs
  aggregatedWorkOccurrenceRefs
  workPartPhaseOrOverlapRelationRefs
  resourceCharacteristicRefs
  measurementWorkRefs
  measurementResultEpistemeRefs
  aggregationMethodRef
  aggregationOperationDeclarationRef?
  aggregationPolicyRef
  conversionOrNormalizationRefs?
  aggregationWorkRef
  aggregationResultRef
  aggregationResultEpistemeRef
  provenancePathRefs
  admissibleUse
  nonAdmissibleOverread
```

These are separately governed objects, not fields that create one another:

- a **resource Characteristic** says which quantity or property is accounted for;
- **measurement work** and a **C.16 measurement-result episteme** supply each attributed resource value, Scale, Unit, uncertainty, model, calibration, and time stance;
- the **aggregation policy** declares inclusion, conversion, weighting, missing-value, partition, overlap, and deduplication rules;
- **aggregation work** is dated `U.Work` with performer, method, actual inputs through direct relations or A.6.1 bindings, resources, and temporal extent;
- the **B.1.6 aggregation result** is the typed total, vector, interval, or bounded estimate obtained under that policy and work set;
- a distinct **C.2.1 aggregation-result episteme** states the result, work set, policy, boundary, time window, qualifications, and uncertainty; and
- **A.10/G.6 provenance** makes the measurement sources, transformations, aggregation work, and result episteme replayable.

A ledger, dashboard, policy, profile, clause, citation, or graph edge may represent or cite this chain. None establishes work occurrence, actual participation, measurement, aggregation, or result identity by presence.

#### B.1.6:2.1 - Direct Owner Map

| Current claim | Direct owner |
| --- | --- |
| Resource Characteristic, Scale, Unit, measurement model/calibration, measurement work and result | `C.16` plus A.15.1/A.6.1 for work and bindings |
| Dated aggregation work, performer, method enactment, and actual inputs | `A.15.1` and `A.6.1` |
| Work temporal part, episode, operational part, partition, overlap, retry, resumption, or later occurrence | `A.15.1` and the exact Work relation owner; use `B.1.4` only to aggregate already recovered temporal relations |
| Proper temporal restriction of another enduring carrier | that carrier's direct identity owner plus `A.14` `PhaseOf`; never a substitute for Work relations |
| Overlap, shared-stock, boundary, and deduplication facts | exact stock, resource-use, boundary, work-overlap, or accounting relation owner |
| Aggregation policy and typed aggregation result | `B.1.6` |
| Measurement-result and aggregation-result epistemes | `C.2.1`; A.15.PROD only when their inception through work matters |
| Source recovery and provenance | `A.10` and `G.6`; `E.17` for publication |
| Edition currentness | `G.11` |
| Planned work or resource readiness | `A.15.2` or `A.15.5`, never a measured aggregation result |
| Transformation, whole reidentification, assurance, comparison, or decision | its direct A.3.4, B.2, B.3, A.19, C.11, or other exact governor |

