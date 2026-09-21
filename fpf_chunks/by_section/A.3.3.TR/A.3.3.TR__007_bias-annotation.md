---
chunk_kind: "child"
pattern_id: "A.3.3.TR"
pattern_title: "Construct a Rule for State Change"
section_id: "A.3.3.TR:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.TR/A.3.3.TR__007_bias-annotation.md"
commit_sha: "31f4cb0b7f8000e0115098b50b44f80c8c36a671"
heading_path:
  - "A.3.3.TR — Construct a Rule for State Change"
  - "A.3.3.TR:6 — Bias-Annotation"
line_start: 10012
line_end: 10017
dependencies:
  - "A.22.CGUS"
  - "A.3.3"
  - "A.3.3.CC"
  - "B.5.FM"
  - "B.5.MPC"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
keywords:
---

### A.3.3.TR:6 - Bias-Annotation

The continuous example uses an ideal Newtonian model with supplied masses, forces and constraints. Its simplicity makes the common construction visible; another phenomenon needs its own interaction account. The concurrent example assumes atomic reads and writes and makes interleaving observable at that scale. Choose the granularity from the interactions and intermediate effects that can change the answer.

Finite examples can make complete exploration look inexpensive. Large state sets and continuous systems may require abstraction, symbolic reasoning, approximation or a less detailed conclusion. The Method permits a useful conditional result before that larger work.

