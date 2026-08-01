---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:4"
section_title: "Ledger Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__007_ledger-discipline.md"
commit_sha: "1eb56cd0cfd6dccad65143e03d28509373bd8dd5"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:4 — Ledger Discipline"
line_start: 37032
line_end: 37049
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

### B.1.6:4 - Ledger Discipline

The ledger is a replay surface, not the aggregation's ontic owner. For every resource component it records:

- resource Characteristic, Scale, Unit, polarity when relevant, and accounting boundary;
- exact measured or estimated subject, time window, and work occurrence to which the value applies;
- C.16 measurement work and measurement-result episteme, including model, calibration, uncertainty, and provenance refs when current;
- exact A.15.1 Work-temporal, episode, operational-part, partition, or overlap relations—and any separately current non-Work carrier `PhaseOf`—independently established by their direct owners;
- shared resource, meter, person, tool, stock, data, port, or time-window overlap and the exact deduplication rule;
- conversions, normalizations, imputations, and their declared method/policy refs;
- the aggregation policy edition and actual aggregation work occurrence;
- aggregation result and distinct C.2.1 result episteme; and
- A.10/G.6 source and provenance refs, G.11 currentness when current, admissible use, unsupported overread, and reopen condition.

Measured, estimated, normalized, converted, allocated, and planned values remain visibly different. A planned value does not become a measurement result or performed-work resource use. A citation to a meter or invoice does not establish the measurement work; a ledger row does not establish work parthood or overlap.

Use `PortionOf` only for an exact resource portion with its A.14 measure and additivity basis. Use `PhaseOf` only for a proper temporal restriction of one unchanged non-Work carrier after its direct identity rule and interval conditions hold. For Work, use A.15.1 `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, another admitted Work-part relation, overlap, retry, resumption, or a separately identified occurrence according to its exact predicate. `MemberOf`, common timestamps, shared identifiers, a phase label, or co-listing in the ledger establishes none of those relations.

