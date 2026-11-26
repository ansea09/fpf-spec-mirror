---
chunk_kind: "child"
pattern_id: "C.29.3"
pattern_title: "Computational Realization"
section_id: "C.29.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.3/C.29.3__002_problem-frame.md"
commit_sha: "9d38fbfe4ce5b72d8fe05e839cbca0025a5b31cf"
heading_path:
  - "C.29.3 — Computational Realization"
  - "C.29.3:1 — Problem frame"
line_start: 74319
line_end: 74330
dependencies:
  - "A.3.3"
  - "A.6.1"
  - "B.5.MPC"
  - "C.16"
  - "C.29.2"
keywords:
---

### C.29.3:1 - Problem frame

**Use this when** a computation is available, but the proposed executing arrangement has not yet been connected to its inputs, operations and interpretable results. A motor interface may accept a different number from the one calculated. A circuit may produce a voltage whose scale differs from the input scale. At a second entrance, issuing copies of the original passes can defeat a room's admission limit.

Start with the result the arrangement must deliver. For an input or history covered by the order, explain how the system is prepared, which actions perform the computation and how its result is read. Compare that result with what the recipient needs. An operating law can establish the comparison over its whole range. A particular input can expose a failure, such as a command outside the interface's range.

The first result is a realization design under stated conditions, an interpreted result from an execution, or a failed connection with a proposed correction. The method helps construct and use that connection. The engineering of a circuit, controller, physical apparatus or administrative arrangement supplies the mechanisms that perform the computation.

The reader should understand the intended computation and be able to obtain explanations of the system's operations. The examples supply their arithmetic, elementary electrical account and card rules. More demanding uses need the corresponding knowledge of hardware, numerical methods, physical models or concurrent operation.

Use an adequate existing implementation when its inputs, behavior and result interpretation already meet the receiving need. Use C.29.2 when the computational procedure itself must be constructed. Use B.5.MPC when the open question also concerns which physical account and mathematical question can answer the original problem.

