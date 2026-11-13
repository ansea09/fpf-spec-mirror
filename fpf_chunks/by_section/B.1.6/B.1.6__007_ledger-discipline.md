---
chunk_kind: "child"
pattern_id: "B.1.6"
pattern_title: "Work-Resource Aggregation"
section_id: "B.1.6:4"
section_title: "Ledger Discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/B.1.6/B.1.6__007_ledger-discipline.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "B.1.6 — Work-Resource Aggregation"
  - "B.1.6:4 — Ledger Discipline"
line_start: 44938
line_end: 44957
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

### B.1.6:4 - Ledger Discipline

A ledger can organize the grounds needed to reconstruct the aggregation. Whether using a ledger or another representation, retain for each resource component:

- resource Characteristic, Scale, applicable Unit, polarity when relevant, and accounting boundary;
- the measured or estimated subject, time window, and included Work occurrence, non-Work carrier phase or other admitted accounting subject to which the value applies;
- the attribution basis: C.16 measurement Work and its result episteme for a claimed performed measurement, or the source values, model and conditions for an estimated or derived value, including the calibration and uncertainty basis needed for its use;
- every A.15.1 Work-part relation used by the ledger, every C.27.TA overlap fact used by it, and any current non-Work carrier `PhaseOf`, each independently established by its subject pattern;
- whether component values include the same resource use, stock portion or attributed contribution, and the justified allocation or deduplication rule where they do;
- any conversions, normalizations or imputations used, with the operative methods and rules;
- the operative aggregation rule, its edition when the result or use depends on it, and the aggregation Work occurrence when that dated occurrence is asserted or required;
- the typed aggregation result and its statement, with a separately identified C.2.1 result episteme when the receiving claim or use needs one; and
- sources and derivations needed to justify the result; A.10/G.6 accounts under the conditions in §2; G.11 currentness when it affects use; and the admissible use, stop or reopen condition, with any guard justified by F.19's plausible-reader test.

Keep visible which values are measured, estimated or planned, and which normalization, conversion or allocation has been applied. These descriptions can overlap: an estimated value may result from an indirect measurement. Its basis determines the claim.

A planned value does not become a measurement result or performed-work resource use. A citation to a meter or invoice does not establish the measurement Work; a ledger row does not establish Work parthood or overlap.

Use `PortionOf` only for a resource portion with its A.14 measure and additivity basis. Use `PhaseOf` only for a proper temporal restriction of one unchanged non-Work carrier after its identity rule and interval conditions hold. For Work, use A.15.1 `TemporalPartOf_work`, `EpisodeOf_work`, `OperationalPartOf_work`, or another admitted Work-part relation only between independently admitted Work participants after its predicate passes. Route interval overlap through C.27.TA. Use retry or resumption only through a locally declared species with the needed participant meanings, predicate, identity, cardinality, and applicability; otherwise keep separately identified occurrences. Belonging to a collection, common timestamps, shared identifiers, a phase label, or co-listing in the ledger establishes none of those relations.

