---
chunk_kind: "child"
pattern_id: "C.29.BB"
pattern_title: "Construct a Balance across a Boundary"
section_id: "C.29.BB:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.29.BB/C.29.BB__002_problem-frame.md"
commit_sha: "8581bcf6502498b53aaa9fd42ed925a1371c08d1"
heading_path:
  - "C.29.BB — Construct a Balance across a Boundary"
  - "C.29.BB:1 — Problem frame"
line_start: 64624
line_end: 64635
dependencies:
  - "A.3.3.TR"
  - "C.11.DUA"
  - "C.29.1"
  - "C.29.2"
  - "E.18.2"
keywords:
---

### C.29.BB:1 - Problem frame

Use this pattern when a total changes and you need to construct the relation between that change, transfers across a chosen boundary, and creation or removal within it. The difficulty may be choosing what belongs inside, combining accounts for parts, or understanding why a balance changes after the boundary is redrawn.

Two tanks can gain less liquid than their external inflow minus outflow suggests because some liquid remains in their connecting line. A job moving between two stages changes their separate counts while leaving the total unfinished count unchanged. A computation can introduce a discrepancy if two cells use different amounts for their shared transfer.

The Method constructs a balance for a chosen additive quantity over a specified interval and collection of parts. Its first result can be a predicted total, a bound, a missing-transfer question, or a computational update that preserves the supplied balance. The construction may describe a physical region, a defined population or a mathematical partition; identify which one answers the working question.

The reader needs the quantity's meaning and enough arithmetic to combine amounts with signs. A physical application also needs the relevant storage and transfer laws. A rate or field calculation needs the calculus used by that model.

If a complete, applicable balance already answers the question, use it. This pattern is useful when the balance itself must be built or revised. Detailed transport laws, reaction models and numerical solvers remain contributions of their respective subject Methods.

