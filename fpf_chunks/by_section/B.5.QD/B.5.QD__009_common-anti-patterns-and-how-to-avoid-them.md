---
chunk_kind: "child"
pattern_id: "B.5.QD"
pattern_title: "Develop a New Question from a Result or Construction"
section_id: "B.5.QD:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.QD/B.5.QD__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "3e9ea496420256ac09257c024b3120fcbc762b81"
heading_path:
  - "B.5.QD — Develop a New Question from a Result or Construction"
  - "B.5.QD:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 44973
line_end: 44983
dependencies:
  - "B.5.MPC"
  - "B.5.RA"
  - "B.5.RR"
  - "C.11.DUA"
  - "C.39"
  - "C.40"
  - "E.10.INT"
keywords:
---

### B.5.QD:8 - Common Anti-Patterns and How to Avoid Them

| Failure | Repair |
|---|---|
| Appending exceptions until a refuted claim survives, while losing the original use. | Follow the counterexample's failed relation; formulate the condition or obstruction that helps answer the working question. |
| Treating a failed lemma as a refutation of the main conjecture. | Recover which argument used the lemma and what remains undecided; investigate an alternative step where useful. |
| Generating many syntactic variants and counting them as progress. | Work a variation that changes an available construction, an answer or a useful distinction. |
| Asking for a unique prediction from information shared by physically different continuations. | Exhibit the differing cases; obtain sufficient state information or return a useful bound. |
| Discarding a successful operation after it gives the requested number. | Recover its relation to inputs and outputs when another use could benefit, as with cumulative totals. |
| Making proof of eventual usefulness a prerequisite for exploration. | Identify the nearer inquiry or construction the question can enable and compare that contribution with its present cost. |

