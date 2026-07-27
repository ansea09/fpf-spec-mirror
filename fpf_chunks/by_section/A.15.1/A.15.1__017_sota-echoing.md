---
chunk_kind: "child"
pattern_id: "A.15.1"
pattern_title: "U.Work"
section_id: "A.15.1:13.1"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.15.1/A.15.1__017_sota-echoing.md"
commit_sha: "60caecb4751fb2a3623a1faaca757d29a19acff9"
heading_path:
  - "A.15.1 — U.Work"
  - "A.15.1:13.1 — SoTA-Echoing"
line_start: 24784
line_end: 24795
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
  - "F.6"
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
  - "actual performer U.System"
  - "admitted U.Work kind"
  - "containing system"
  - "covering U.RoleAssignment"
  - "enacted method"
  - "optional direct bindings and resource use"
  - "performedUnderAssignment"
  - "separate result or consequence"
  - "temporal extent"
  - "world-side dated occurrence"
---

### A.15.1:13.1 - SoTA-Echoing

**SoTA alignment rule.** A source tradition counts here only when it preserves the local separations: `U.Work` is the admitted kind; one Work individual is a world-side dated occurrence; each actual performer is an admitted `U.System`; the exact obtaining `U.RoleAssignment` states the role under which that system performs; and an assertion or description about the occurrence is a separate `U.Episteme`. The occurrence has exact method, temporal, and containing-system relations; work-to-referent, binding, and resource-use relations are added only when they independently obtain. Neighboring change, evaluation, evidence, production, delivery, and acceptance claims remain separate. Historical occurrence modeling is used as lineage only when a current practice still needs those distinctions.

| Source tradition | Current source reference and source maturity | Local invariant adopted | Shortcut rejected |
| --- | --- | --- | --- |
| Occurrent and 4D occurrence ontology | ISO/IEC 21838-2:2021 / BFO 2020; BORO-style extensionalism used as historical lineage for identity criteria. | `U.Work` admits dated occurrence holons; each Work individual has its own temporal extent and participates in separately obtaining occurrence relations, while assertions and records about it remain separate epistemes. Parts, retries, resumptions, and overlaps stay explicit. | Treating a method factor, diagram, role label, log entry, or record schema as the performed occurrence. |
| Object-centric event logging and process mining | OCEL 2.0 Specification (2024) and object-centric process-mining practice. | Event records can enter an evidence or provenance relation for work only after they designate independently grounded Work individuals and make actual performer systems, covering role assignments, enacted method, temporal extent, and containing system recoverable, together with any involved-object, binding, resource-use, interpretation, or policy relation on which the receiving claim relies. | Treating telemetry or event rows alone as Work occurrences or as membership evidence for `U.Work`. |
| Observability and telemetry practice | OpenTelemetry Specification 1.58.0 and current traces, metrics, and logs practice. | Telemetry can support, replay, measure, or diagnose a claim about work, but the occurrence still needs its actual performer system, covering assignment, enacted method, temporal extent, and containing system. It needs an affected-referent, binding, or resource-use fact only when the receiving claim relies on that independently obtaining relation. | Counting trace, metric, or log existence as the performed work, a result, or dominance evidence without the governing evidence, comparison, or archive relation. |
| Provenance and evidence-provenance practice | W3C PROV mature recommendation plus 2024 PROV-O/BFO alignment work. | Assertions or descriptions about Work cite exact evidence-provenance relations and currentness notes without letting evidence, assurance, gate, or provenance claims replace the occurrence. | Using a provenance relation, assurance statement, or gate result as if it were the performed work. |
| Temporal-interval and aggregation practice | Interval-algebra lineage plus current operations-management use of utilization, lead-time, and resource-ledger roll-ups. | A.15.1 supplies exact Work intervals, parts, and performed resource-use facts; `B.1.4` governs temporal aggregation and `B.1.6` governs work-resource aggregation, each with its exact policy and admissible use. | Mixing union, hull, parent cost, child cost, and ordinal comparison on the Work object without a recovered Part B aggregation claim. |

