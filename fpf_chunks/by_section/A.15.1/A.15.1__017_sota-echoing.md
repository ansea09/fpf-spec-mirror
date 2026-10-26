---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work: Dated Performed Work Occurrence"
section_id: "A.15.1:13.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__017_sota-echoing.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "A.15.1 — U.Work: Dated Performed Work Occurrence"
  - "A.15.1:13.1 — SoTA-Echoing"
line_start: 29451
line_end: 29462
dependencies:
  - "A.1"
  - "A.10"
  - "A.13"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.6"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.4"
  - "B.1.6"
  - "B.3"
  - "C.2.1"
  - "C.27.TA"
  - "C.32.P2S"
  - "E.10"
  - "E.10.ROLE"
  - "E.17"
  - "F.6"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.WorkPlan"
keywords:
  - "A.13-qualified actual performer U.System"
  - "F.6 only after admission for precise assignment-bound attribution"
  - "conditional agency profile"
  - "containing System"
  - "enacted Method"
  - "exact performance history"
  - "independent U.Work admission"
  - "optional direct bindings and resource use"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:13.1 - SoTA-Echoing


| Source tradition | Source reference and contribution | FPF use | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021, BFO 2020, and BORO-style extensionalism are mature identity lineage, not a newly published operational practice. | `U.Work` admits dated occurrence holons; each Work individual has its own temporal extent and participates in separately obtaining occurrence relations, while assertions and records about it remain separate epistemes. Parts, retries, resumptions, and overlaps stay explicit. | Treating a Method factor, diagram, system-role label, log entry, or record schema as the performed occurrence. |
| Object-centric event logging and process mining | The [OCEL 2.0 semantic specification](https://www.ocel-standard.org/specification/overview/) remains the semantic basis; the [OCEL 2.1 revision](https://www.ocel-standard.org/specification/formats/bundled/) adds a compact single-file CSV serialization and a bundled format using CSV or Parquet tables. | Event records can support Work claims only when they designate independently grounded candidate actions and make every actual performer's A.13 basis, enacted Method, temporal extent, local containing-system relation, and any relied-on object, binding, resource-use, interpretation, or policy relation recoverable. Any precise assignment-bound attribution remains a separate later F.6 result. A serialization revision changes neither Work identity nor these admission conditions. | Treating telemetry or event rows alone as Work occurrences or as membership evidence for `U.Work`. |
| Observability and telemetry practice | [OpenTelemetry Specification 1.60.0](https://opentelemetry.io/docs/specs/otel/) for trace, metric and log representation. | Telemetry can support, replay, measure, or diagnose a claim about Work, but the occurrence still needs every actual performer's A.13 basis, independently grounded history, enacted Method, temporal extent, and local containing-system relation. Add F.6 only for a separately claimed precise assignment-bound attribution, and add another enactment, affected-referent, binding, or resource-use fact only when the receiving claim uses it. | Counting trace, metric, or log existence as the performed Work, a result, or dominance evidence without the direct evidence, comparison, or archive relation. |
| Provenance and evidence-provenance practice | W3C PROV is a mature recommendation; the [2025 PROV-O and BFO alignment](https://pmc.ncbi.nlm.nih.gov/articles/PMC11833102/) is a later interoperability contribution. | Assertions or descriptions about Work cite the evidence-provenance relations and currentness notes their use needs without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed Work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | A.15.1 supplies identified Work intervals, parts, and performed resource-use facts; use `B.1.4` for temporal aggregation and `B.1.6` for work-resource aggregation, each with its stated policy and admissible use. | Mixing union, hull, parent cost, child cost, and ordinal comparison on the Work object without a recovered Part B aggregation claim. |


