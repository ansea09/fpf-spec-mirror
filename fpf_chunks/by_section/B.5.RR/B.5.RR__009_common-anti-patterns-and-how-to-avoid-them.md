---
chunk_kind: "child"
pattern_id: "B.5.RR"
pattern_title: "Revise Reasoning After a Premise or Question Changes"
section_id: "B.5.RR:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.RR/B.5.RR__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "4ddaf71557d4159e988cc61d2bd3088bfc1d2803"
heading_path:
  - "B.5.RR — Revise Reasoning After a Premise or Question Changes"
  - "B.5.RR:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 44942
line_end: 44951
dependencies:
  - "B.5"
  - "B.5.MPC.R"
  - "B.5.RA"
  - "B.5.RC"
  - "C.11.DUA"
keywords:
---

### B.5.RR:8 - Common Anti-Patterns and How to Avoid Them

| Observed failure in revision | Why it matters | Repair |
| --- | --- | --- |
| Replace a number while retaining the old question | The calculation still solves for the former unknown. | Restate the givens and requested result before choosing the computation. |
| Treat the loss of one argument as a refutation | A different sufficient argument may remain. | Examine its premises and derive the conclusion or its negation separately. |
| Count two dependent arguments as independent | Both can fail with their shared prerequisite. | Follow the common premise through both uses. |
| Preserve a conclusion through circular repetition | The retained statements supply no starting support. | Recover a grounded argument or leave the conclusion unresolved. |
| Repair the whole report to answer a small change | Unaffected results are needlessly reproduced. | Compare affected repair with a fresh sufficient answer and choose the useful scope. |

