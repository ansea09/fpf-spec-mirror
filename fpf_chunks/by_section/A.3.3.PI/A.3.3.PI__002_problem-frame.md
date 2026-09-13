---
chunk_kind: "child"
pattern_id: "A.3.3.PI"
pattern_title: "Retain the Information Needed for Prediction"
section_id: "A.3.3.PI:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3.PI/A.3.3.PI__002_problem-frame.md"
commit_sha: "bbfb5347013400e9a895fa4b0f66992e931c0ece"
heading_path:
  - "A.3.3.PI — Retain the Information Needed for Prediction"
  - "A.3.3.PI:1 — Problem frame"
line_start: 10067
line_end: 10078
dependencies:
  - "A.3.3"
  - "A.3.3.CC"
  - "A.3.3.TR"
  - "B.5.FM"
  - "B.5.MPC.R"
  - "C.11.DUA"
  - "C.16"
  - "C.29.1"
keywords:
---

### A.3.3.PI:1 - Problem frame

Use this pattern when a description of the present leaves a future result unresolved, or when you want to simplify a predictive account without losing an answer that matters. A total can hide components that change at different rates. A current readout can merge situations whose next outcomes have different probabilities. A summary adequate for the next output can lose information needed two steps later.

**First useful move.** Find two admitted situations that the proposed description treats as the same. Apply the supplied change rule under the same inputs and compare the future result needed by the question. If one kilogram of substance A becomes half a kilogram after treatment, while one kilogram of substance B becomes a quarter, the description “one kilogram remains” cannot determine the next total. It can still supply the range from a quarter to half a kilogram.

The Method constructs information sufficient for a stated prediction: additional state values, a usable history, a distribution over possible states or a bound that settles the question. Its result can also identify which missing distinction would change the answer. It connects the state, transition and observation contributions recognized by A.3.3.

The elementary cases require arithmetic, equations and conditional probabilities. More demanding models need their subject-specific estimation, reduction or computational Methods. The common task is to choose and use the retained information with the prediction it supports.

When an available prediction or bound already settles the working question, use it. When the missing contribution is a rule of change, A.3.3.TR helps construct that rule. The present Method applies when the retained information and the desired prediction need to be reconciled.

