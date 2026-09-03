---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:5"
section_title: "Aggregation Rules"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__008_aggregation-rules.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:5 — Aggregation Rules"
line_start: 38013
line_end: 38044
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
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
  - "F.6"
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

### B.1.6:5 - Aggregation Rules

**Typed resource basis.** Aggregate only values whose resource Characteristic, Scale, Unit, subject, and accounting boundary are compatible under the declared policy. Joules, hours, kilograms, currency, bytes, and attention do not become one scalar by co-location.

**Measurement before aggregation.** Each measured input points to exact C.16 measurement work and one measurement-result episteme. Raw meter output, indication, resource stock, attributed value, aggregation input, and later efficiency verdict remain distinct.

**Exact Work set.** Name every dated Work occurrence included. Parent–child, `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, and other admitted Work-part relations must already obtain between exact Work participants under A.15.1 or their direct subject patterns. Any overlap fact comes through its exact C.27.TA temporal declaration. A Method, plan, epoch or phase label, invoice period, or dashboard grouping does not establish the Work set.

**Exact policy.** The aggregation policy states inclusion/exclusion, conversion, normalization, weighting, missing-value treatment, boundary allocation, uncertainty treatment, overlap/deduplication, and output kind. A policy declaration is not aggregation work or a result.

**Overlap and shared stocks.** Addition is admissible only for disjoint partitions or after an exact policy handles overlap. Shared people, tools, meters, inventories, datasets, ports, and time windows require the direct shared-use/overlap fact and a justified allocation or deduplication rule.

**Aggregation work and result.** Use A.13 to identify the actual performer and A.15.1 to admit the dated aggregation Work independently. If the aggregation account must also identify the assignment under which the Work was performed, check that relation separately through F.6. Keep the Method, actual bindings, resources, and time separate. State the B.1.6 result as a typed total, vector, interval, or bounded estimate under the named policy and Work set; then state it in a distinct C.2.1 episteme.

**Uncertainty and provenance.** Propagate measurement uncertainty and model/conversion uncertainty according to the exact aggregation policy. Use A.10/G.6 paths to record the established work, measurements, policy application, transformations, result, and sources.

**Plan/result separation.** Keep expected use from a method description or WorkPlan as planned and resource readiness under A.15.5. Use A.15.1 and the measurement or aggregation predicates for performed Work and measured results.

**Efficiency and yield.** A ratio or yield claim names its input resource results, exact output/domain result, measurement bases, aggregation work, and comparison policy. It does not use a generic output-result relation. Apparent free gain remains a measurement, accounting-boundary, substitution, or whole-reidentification question until its subject pattern is recovered.

#### B.1.6:5.1 - Compact Obligation Rows

| Obligation | What must be named |
| --- | --- |
| Resource input | Resource Characteristic, Scale/Unit, subject, C.16 measurement work/result episteme, uncertainty, time, and provenance |
| Work set | Dated Work occurrences, every A.15.1 Work-part relation used by this aggregation, and every C.27.TA overlap fact it uses; any non-Work carrier phase keeps its own identity rule and `PhaseOf` relation |
| Policy | Edition, inclusion, conversions, weights, missing values, boundary allocation, uncertainty, overlap/deduplication, and output kind |
| Aggregation execution | Actual performer identified through A.13; dated `U.Work` independently admitted through A.15.1; a separate F.6 check when the result must also identify the assignment under which the Work was performed; separate Method, resources, and actual direct/A.6.1 bindings |
| Aggregation result | Typed result, work set, policy, boundary, window, qualifications, and distinct C.2.1 episteme |
| Provenance/currentness | A.10/G.6 paths and G.11 result when currentness affects use |
| Later use | Exact receiving work and direct premise/reference/argument/decision-use relation |

