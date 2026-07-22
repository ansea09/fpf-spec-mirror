---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:13.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__017_sota-echoing.md"
commit_sha: "0990ff1d1ccee4587b8f7e16e7a725a8edbe66b4"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:13.1 — SoTA-Echoing"
line_start: 24698
line_end: 24709
dependencies:
  - "A.1"
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.15.4"
  - "A.15.5"
  - "A.15.PROD"
  - "A.2"
  - "A.2.1"
  - "A.2.2"
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
  - "E.10.ARCH"
  - "E.17"
  - "U.Capability"
  - "U.Method"
  - "U.MethodDescription"
  - "U.ReferenceScheme"
  - "U.Role"
  - "U.RoleAssignment"
  - "U.System"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "U.Work admitted kind"
  - "actual binding"
  - "affected referent"
  - "enactsMethod"
  - "episode"
  - "no automatic transformation"
  - "occurrence assertion and record separation"
  - "overlap"
  - "performed resource-use fact"
  - "performedBy"
  - "retry"
  - "work continuity"
  - "work part"
  - "world-side dated occurrence"
---

### A.15.1:13.1 - SoTA-Echoing

**SoTA alignment rule.** A source tradition counts here only when it preserves the local three-way distinction: `U.Work` as the admitted kind, one Work individual as a world-side dated occurrence, and an assertion or description about that occurrence as a separate `U.Episteme`. The occurrence stands in exact performer, method, temporal, affected-referent, binding, containing-system, and resource-use relations, while neighboring change, evaluation, evidence, production, delivery, and acceptance claims remain separate. Historical occurrence modeling is used as lineage only when a current practice still needs that distinction.

| Source tradition | Current source reference and source maturity | Local invariant adopted | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021 / BFO 2020; BORO-style extensionalism used as historical lineage for identity criteria. | `U.Work` admits dated occurrence holons; each Work individual has its own temporal extent and participates in separately obtaining occurrence relations, while assertions and records about it remain separate epistemes. Parts, retries, resumptions, and overlaps stay explicit. | Treating a method factor, diagram, role label, log entry, or record schema as the performed occurrence. |
| Object-centric event logging and process mining | OCEL 2.0 Specification (2024) and object-centric process-mining practice. | Event records can enter an evidence or provenance relation for work only after they designate independently grounded Work individuals and make involved objects, performer or role assignment, enacted method, temporal extent, affected referent, and exact interpretation or policy references needed by the receiving claim recoverable. | Treating telemetry or event rows alone as Work occurrences or as membership evidence for `U.Work`. |
| Observability and telemetry practice | OpenTelemetry Specification 1.58.0 and current traces, metrics, and logs practice. | Telemetry can support, replay, measure, or diagnose a claim about work, but the occurrence still needs performer assignment, enacted method, temporal extent, affected referent, bindings, and resource-use facts. | Counting trace, metric, or log existence as the performed work, a result, or dominance evidence without the governing evidence, comparison, or archive relation. |
| Provenance and evidence-provenance practice | W3C PROV mature recommendation plus 2024 PROV-O/BFO alignment work. | Assertions or descriptions about Work cite exact evidence-provenance relations and currentness notes without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | A.15.1 supplies exact Work intervals, parts, and performed resource-use facts; `B.1.4` governs temporal aggregation and `B.1.6` governs work-resource aggregation, each with its exact policy and admissible use. | Mixing union, hull, parent cost, child cost, and ordinal comparison on the Work object without a recovered Part B aggregation claim. |

