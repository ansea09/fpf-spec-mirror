---
chunk_kind: "child"
pattern_id: "C.28.MR"
pattern_title: "Derive an Intervention Consequence by Mechanism Replacement"
section_id: "C.28.MR:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.28.MR/C.28.MR__002_problem-frame.md"
commit_sha: "a4048aafca7f550ddc5dc880c9b488e9c8401434"
heading_path:
  - "C.28.MR — Derive an Intervention Consequence by Mechanism Replacement"
  - "C.28.MR:1 — Problem frame"
line_start: 63897
line_end: 63906
dependencies:
  - "A.3.3.TR"
  - "B.5.MPC"
  - "B.5.RR"
  - "C.28"
  - "C.29.1"
keywords:
---

### C.28.MR:1 - Problem frame

Use this pattern when a causal model is available and the working question asks what follows if a mechanism is replaced: a controller uses a different rule, a variable is held at a chosen value, or an action occurs at a specified event. The model may be small enough to calculate by hand.

The subject is the intervention query in that model. The Method constructs the modified model and derives the requested value, distribution, contrast or bound under its assumptions. The practitioner needs the subject meaning of the variables and enough mathematical or computational help to solve the relevant equations.

**First useful move.** Point to the equation that represents the proposed change. Replace that equation and re-evaluate the variables needed for the question. If a display merely reports voltage, changing its displayed number leaves the supply equation in place. Changing the supply command instead changes the voltage and the current through the retained load equation.

Use an adequate existing derivation directly. Observational reporting can finish without this transformation. If only an observed joint distribution is available, recover a causal-model assumption or an identification result through C.28 before claiming a particular intervention consequence. Identifying an effect from data is a separate task from deriving it in a supplied model.

