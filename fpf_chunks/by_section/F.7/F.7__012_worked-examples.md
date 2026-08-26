---
chunk_kind: "child"
pattern_id: "F.7"
pattern_title: "Concept-Set Table"
section_id: "F.7:11"
section_title: "Worked examples"
source_path: "FPF-Spec.md"
output_path: "by_section/F.7/F.7__012_worked-examples.md"
commit_sha: "d064720b072b822cbb2f1d41e555cf08e2904f11"
heading_path:
  - "F.7 — Concept-Set Table"
  - "F.7:11 — Worked examples"
line_start: 92592
line_end: 92621
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

### F.7:11 - Worked examples

#### F.7:11.1 - Actor wording across BPMN and PROV

| Comparison or use | Exact entries | Relation | Boundary | Basis | Conclusion |
| --- | --- | --- | --- | --- | --- |
| Choose a plain-language heading for a teaching paragraph | BPMN **Participant** claim; PROV **Agent** claim | No identity asserted; any F.9 relation must be established for the exact claims | PROV agents include software and organisations; BPMN participants have model-specific structure | Source passages and F.0.1 | The word **party** may be used as an explanatory umbrella only in this paragraph if the sentences retain each source’s distinct claim. |

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

