---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__002_problem-frame.md"
commit_sha: "1e57ccda08ebbb9d49b7b2190bc2740b72075a13"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:1 — Problem frame"
line_start: 74199
line_end: 74210
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:1 - Problem frame

Use this pattern when you need to relate a total's change over an interval to transfers across a boundary and creation or removal within it. The difficulty may be choosing what belongs inside, combining accounts for parts, or understanding why a balance changes after the boundary is redrawn.

Two tanks can gain less liquid than their external inflow minus outflow suggests because some liquid remains in their connecting line. A job moving between two stages changes their separate counts while leaving the total unfinished count unchanged. A computation can introduce a discrepancy if two cells use different amounts for their shared transfer.

The Method constructs a balance for an additive quantity over an interval and collection of parts. Its first result can be a predicted total, a bound, a missing-transfer question, or a computational update that preserves the supplied balance. The construction may describe a physical region, a defined population or a mathematical partition; identify which one answers the working question.

The reader needs the quantity's meaning and enough arithmetic to combine amounts with signs. A physical application also needs storage and transfer laws. A rate or field calculation needs the calculus used by that model.

If a balance already answers the question, use it. This pattern is useful when the balance itself must be built or revised. Detailed transport laws, reaction models and numerical solvers remain contributions of their respective subject Methods.

