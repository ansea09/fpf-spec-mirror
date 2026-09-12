---
chunk_kind: "child"
pattern_id: "C.29.1"
pattern_title: "Mathematical Result Transfer"
section_id: "C.29.1:7"
section_title: "Conformance Checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.1/C.29.1__008_conformance-checklist.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "C.29.1 — Mathematical Result Transfer"
  - "C.29.1:7 — Conformance Checklist"
line_start: 60042
line_end: 60058
dependencies:
  - "A.3.3"
  - "A.6.3.RT"
  - "B.5"
  - "B.5.MPC"
  - "C.29"
keywords:
---

### C.29.1:7 - Conformance Checklist

These checks concern a claimed use of mathematical transfer. Recognition of a promising representation starts the work; the comparison and argument establish what conclusion it supports. Select the checks that apply to the claimed use.

| ID | Check and action |
|---|---|
| CC-C29.1-1 | The account SHALL state the receiving question and direction of use. If the same result is used as both a bound and a source action, explain the additional source witness for the latter. |
| CC-C29.1-2 | The transfer argument SHALL identify the source inputs, relevant operations and premises, including operation conditions that affect the conclusion. Recover a missing source rule before relying on its transfer. |
| CC-C29.1-3 | The account SHALL define the correspondence on the domain used by the conclusion and explain the meaning of its relevant values. A conclusion outside the represented domain needs a further argument. |
| CC-C29.1-4 | An exact operation-transfer claim SHALL be supported by the comparison in C.29.1:4.3 over its stated domain. Include availability or return conditions when the receiving use depends on them. |
| CC-C29.1-5 | An answer defined through a merged representation SHALL have the representative-independence argument in C.29.1:4.4, or be qualified as a bound or set of possible answers. A conflicting permitted pair requires repair of that proposed answer. |
| CC-C29.1-6 | A bound or approximation claim SHALL explain why it covers the allowed cases, the direction of its inequality and the subsequent error propagation needed by the receiving use. |
| CC-C29.1-7 | A returned receiving solution claimed to be feasible in the source SHALL identify an allowed source counterpart with the stated properties. A relaxation optimum alone supplies no such counterpart. |
| CC-C29.1-8 | The returned conclusion SHALL retain its answer-changing assumptions and distinguish the result obtained from the further work still needed. A physical application includes the physical premises; a changed premise reopens the dependent comparison. |

A complete argument about a mathematical model establishes its stated conditional consequence. Confidence that an observed system satisfies the premises, or that an implementation performs the operation, comes from the corresponding subject work.

