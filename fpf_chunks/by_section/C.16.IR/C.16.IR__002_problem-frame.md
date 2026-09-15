---
chunk_kind: "child"
pattern_id: "C.16.IR"
pattern_title: "Determine What an Indication Can Resolve"
section_id: "C.16.IR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.IR/C.16.IR__002_problem-frame.md"
commit_sha: "98777b284b6a41fa3481a1230a16182d0f323c2a"
heading_path:
  - "C.16.IR — Determine What an Indication Can Resolve"
  - "C.16.IR:1 — Problem frame"
line_start: 52876
line_end: 52887
dependencies:
  - "A.3.3.PI"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.16.MR"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### C.16.IR:1 - Problem frame

Use this pattern when an available measurement relation leaves open what can be inferred from an indication. A loaded voltmeter reading can fit several source voltages. A saturated sensor can establish that a quantity exceeds one threshold while leaving a higher threshold unresolved. A stored counter remainder can correspond to several event counts.

**First useful move.** Try to construct two cases that fit the same indication and stated conditions but give different answers to the receiving question. If an ideal instrument reports the square of a signed displacement, a reading of 9 square metres fits both +3 and -3 metres. It determines the magnitude but leaves the direction unresolved. Restricting displacement to nonnegative values would resolve that difference only when the subject conditions support the restriction.

The Method determines what the indication resolves under the available relation, domain and uncertainty assumptions. Its result can be a value, a compatible range, a settled comparison, two remaining alternatives or an incompatibility among the premises. C.16 supplies the subject, Characteristic, Scale, performed measurement and result meanings. C.16.MR constructs a missing measurement relation.

The examples require elementary equations, inequalities and integer remainders. More difficult relations can require subject-specific inverse methods, probability models or validated numerical computation.

Apply an already suitable conversion or analysis function directly when it supplies the answer with adequate uncertainty. Use this construction when ambiguity, omitted influences or the meaning of a computed range can change that answer.

