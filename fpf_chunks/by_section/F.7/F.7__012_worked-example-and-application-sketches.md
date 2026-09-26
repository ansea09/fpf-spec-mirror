---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Display Source-Local Comparisons in a Concept-Set Table"
section_id: "F.7:11"
section_title: "Worked example and application sketches"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__012_worked-example-and-application-sketches.md"
commit_sha: "7bba05916e6e8ad42f868ed3aad0a7644fe0c354"
heading_path:
  - "F.7 — Display Source-Local Comparisons in a Concept-Set Table"
  - "F.7:11 — Worked example and application sketches"
line_start: 104613
line_end: 104644
dependencies:
  - "A.6.9"
  - "B.3"
  - "C.16"
  - "E.10.D1"
  - "F.0.1"
  - "F.1"
  - "F.17"
  - "F.2"
  - "F.3"
  - "F.4"
  - "F.5"
  - "F.6"
  - "F.9"
keywords:
  - "comparison surface"
  - "direction"
  - "evidence"
  - "exact local claim"
  - "loss"
  - "obtaining relation"
  - "optional SchemeSenseCell"
  - "receiving use"
---

### F.7:11 - Worked example and application sketches

Section 11.1 supplies exact source bases for one contrast row. Sections 11.2–11.5 show further applications; complete their source-local claims, relations and evidence before treating them as finished tables.

#### F.7:11.1 - Actor wording across BPMN and PROV

| Comparison or use | Exact entries | Relation | Boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Choose a plain-language heading for a teaching paragraph | BPMN 2.0.2 §9.3.1 `Participant`: a Collaboration element representing a PartnerEntity, PartnerRole, or both. PROV-O, 30 April 2013, §3.1 `prov:Agent`: something responsible for an activity, an entity's existence, or another agent's activity. | None asserted; this is a contrast row. | BPMN's representation within a Collaboration and PROV's responsibility meaning remain distinct. | [BPMN 2.0.2 §9.3.1, p. 113](https://www.omg.org/spec/BPMN/2.0.2/PDF#page=143); [PROV-O §3.1](https://www.w3.org/TR/2013/REC-prov-o-20130430/#description-starting-point-terms); each term is interpreted within that cited source scheme. | Use **Parties in the comparison** as this paragraph's heading, then retain the two source-specific sentences. This explanatory heading asserts no common kind, identity or substitutability. |

#### F.7:11.2 - Runtime occurrence comparison

| Comparison or use | Exact entries | Relation | Boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Report selected PLC task runs as provenance activities | IEC task-execution claim; PROV Activity claim | A stated source-local semantic or representation relation, direction IEC → PROV, when actually established | PROV omits scan-cycle and scheduling semantics | F.9 or the direct representation pattern plus evidence | Report only the covered occurrence facts; do not infer that every PROV Activity is an IEC task run. |

Performed-Work attribution remains an A.15.1 and F.6 claim about actual Work and system-role assignment. The table supplies neither.

#### F.7:11.3 - Measured value and target

| Comparison or use | Exact entries | Relation | Boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Judge an observed service characteristic against a target | SOSA observation and its result; ISO quantity value if used; ITIL service target | Measurement, scale, and unit relations; F.9 only for a genuine local-meaning relation | Composite KPI, sampling, and unit limits | C.16, A.10, B.3, and F.12 | Compare only the named characteristic, population, and window with adequate evidence. |

#### F.7:11.4 - Class inclusion and FCA order

A contrast row may show OWL class inclusion, FPF subtype, and FCA concept order together while stating that FCA order is not class inclusion. A positive relation between the first two is still a separate claim with its own semantics and evidence.

#### F.7:11.5 - *Role* trigger word

Show NIST RBAC **role** as a permission grouping and a local system-role-kind claim as a kind whose instances are Systems. Mark them **distinct subjects**. Use E.10.ROLE to recover other uses such as relation participation or signature position; do not assign them one `senseFamily` merely because the spelling matches.

