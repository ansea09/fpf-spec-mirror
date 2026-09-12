---
chunk_kind: "child"
pattern_id: "B.5"
pattern_title: "Canonical Reasoning Cycle"
section_id: "B.5:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5/B.5__002_problem-frame.md"
commit_sha: "4865bcb9123ba04cb2a433c95bf6401be20fe8cb"
heading_path:
  - "B.5 — Canonical Reasoning Cycle"
  - "B.5:1 — Problem frame"
line_start: 41062
line_end: 41073
dependencies:
  - "A.10"
  - "B.5.1"
  - "B.5.2"
  - "B.5.4"
  - "C.29"
keywords:
---

### B.5:1 - Problem frame

Use this pattern when an engineer or researcher has a question, surprising result or promising construction, but the next useful contribution is unclear. They may need to formulate a better question, construct something, prove a claim, explain an observation, or test a consequence. Reasoning is the broader activity; this pattern governs the choice and connection of those contributions in an inquiry.

**First useful move.** State what you want to understand or make possible. Ask whether an available result already answers that question. If it does not, name the missing result and try one operation that could obtain it. Return what that operation established and the next question, if one remains.

For example: “We need the highest component temperature, but our model reports a mean. Two states with the same mean can have different maxima. Next, determine which temperature differences this arrangement admits.” This already redirects the inquiry before another model fit.

The practical gain is a useful answer or a better-founded next question. A correct answer to an inadequate formulation can otherwise consume the inquiry's effort.

Use a known calculation, proof, observation or qualified Method directly when it already answers the question. A separate cycle description adds nothing in that case. Detailed mathematical techniques, physical modeling and domain validation remain with their disciplines.

