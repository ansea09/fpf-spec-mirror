---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:13.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__017_sota-echoing.md"
commit_sha: "89fcd508edbf9a49dc956955a42884fbca43f88c"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:13.1 — SoTA-Echoing"
line_start: 22915
line_end: 22926
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
  - "A.3.1"
  - "A.3.2"
  - "B.1"
  - "B.1.6"
  - "B.3"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ARCH"
  - "E.17"
  - "U.BoundedContext"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "EpisodeOf_work"
  - "TemporalPartOf_work"
  - "actuals"
  - "concurrent work part"
  - "operational work part"
  - "performed enactment"
  - "trace"
  - "work occurrence"
---

### A.15.1:13.1 - SoTA-Echoing

**SoTA alignment rule.** A source tradition counts here only when it preserves the local `U.Work` distinction: dated occurrence, role-assigned performer, enacted method, `methodDescriptionRef` when current, time window, affected referent, resources, outcome, and evidence-provenance relation. Historical occurrence modeling is used as lineage only when a current standard or current practice still needs the same distinction.

| Source tradition | Current source reference and source maturity | Local invariant adopted | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021 / BFO 2020; BORO-style extensionalism used as historical lineage for identity criteria. | `U.Work` is an occurrence with temporal extent and occurrence references; parts, retries, resumptions, and overlaps stay explicit. | Treating a method factor, diagram, role label, or log entry as proof of a performed occurrence. |
| Object-centric event logging and process mining | OCEL 2.0 Specification (2024) and object-centric process-mining practice. | Event records can enter an evidence or provenance relation for work only after they are bound to involved objects, performer or role-assignment relation, method, time window, context, and affected referent. | Treating telemetry or event rows alone as `U.Work`. |
| Observability and telemetry practice | OpenTelemetry Specification 1.58.0 and current traces, metrics, and logs practice. | Telemetry is an evidence relation or archive input. It can replay, measure, or diagnose a work occurrence, but the occurrence still needs performer, method, context, time window, affected referent, resources, and outcome. | Counting trace, metric, or log existence as the performed work or as dominance evidence without the governing comparison or archive policy. |
| Provenance and evidence-provenance practice | W3C PROV mature recommendation plus 2024 PROV-O/BFO alignment work. | Work records state evidence-provenance relation references and currentness notes without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | Roll-ups require declared `Gamma_time`, `Gamma_work`, and overlap policy; partial order and overlap are not hidden in step labels. | Mixing union, hull, parent cost, child cost, and ordinal comparison without a declared policy. |

