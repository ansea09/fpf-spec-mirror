---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:4"
section_title: "Ledger Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__007_ledger-discipline.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:4 — Ledger Discipline"
line_start: 37040
line_end: 37057
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
- work-parthood, phase, partition, or overlap relations independently established by their direct owners;
- shared resource, meter, person, tool, stock, data, port, or time-window overlap and the exact deduplication rule;
- conversions, normalizations, imputations, and their declared method/policy refs;
- the aggregation policy edition and actual aggregation work occurrence;
- aggregation result and distinct C.2.1 result episteme; and
- A.10/G.6 source and provenance refs, G.11 currentness when current, admissible use, unsupported overread, and reopen condition.

Measured, estimated, normalized, converted, allocated, and planned values remain visibly different. A planned value does not become a measurement result or performed-work resource use. A citation to a meter or invoice does not establish the measurement work; a ledger row does not establish work parthood or overlap.

Use `PortionOf` only for an exact resource portion, `PhaseOf` only for an exact temporal/work phase, and the direct work-parthood or work-overlap relation for work occurrences. `MemberOf`, common timestamps, shared identifiers, or co-listing in the ledger do not establish any of those relations.

