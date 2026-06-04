---
chunk_kind: "child"
pattern_id: "E.22"
pattern_title: "Improvement-Oriented Quality-Read Question Framing"
section_id: "E.22:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.22/E.22__011_rationale.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "E.22 — Improvement-Oriented Quality-Read Question Framing"
  - "E.22:10 — Rationale"
line_start: 68597
line_end: 68610
dependencies:
  - "A.19.ECS"
  - "C.17-C.19"
  - "C.25"
  - "E.10"
  - "E.19"
  - "E.2.DA"
  - "E.21"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.22:10 - Rationale

Feedback and review improve an object only when the desired condition, current condition, and next action are distinguishable. If the requested desired condition is merely "acceptable", the reviewer should not be expected to design the best feasible version. If the requested desired condition is "exceptional where feasible", a floor-only blocker pass is under-scoped.

There is no neutral "just read this" in an FPF quality context. The local act in this pattern is an improvement-oriented quality read under a named object-under-improvement evaluation. The frame states what the reader is reading for, and the result states what the object-under-improvement evaluation saw, which candidate improvement proposal follows from that read, and which next admissible move remains only a hypothesis unless another exact pattern receives it.

This is also why `E.22` connects naturally to `E.23` and OEE/NQD. Improvement loops need proposals before changes; OEE/NQD often needs a bounded proposal portfolio before generation, candidate-pool policy, front or archive insertion, selected-set publication, parity, and refresh. `E.22` supplies the evaluative proposal shape. It does not govern the repeated loop, candidate generator, pool policy, selector result, parity result, or refresh plan.

`GQM` discipline gives the same lesson for measurement: questions must follow from the goal. A quality read whose goal is not declared will answer the reviewer's implicit question rather than the requester's intended question.

Multi-coordinate and multi-scale evaluations also need trade-off control. Raising one coordinate can harm another, and a scalar or hidden total order can hide that loss. Therefore `exceptionalImprovementRead` is paired with `paretoTradeoffRead` whenever the proposed changes may affect protected qualities.

`E.22` is deliberately small. It does not define quality coordinates, scales, rubrics, review profiles, OEE/NQD archive semantics, selector results, parity reports, refresh plans, decisions, or work plans. It makes the question to the object-under-improvement evaluation explicit enough that the object-under-improvement evaluation can produce the right kind of answer and the next admissible move can be assigned without overclaim.

