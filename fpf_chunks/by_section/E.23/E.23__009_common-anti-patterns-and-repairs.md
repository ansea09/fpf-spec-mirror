---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:8"
section_title: "Common anti-patterns and repairs"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__009_common-anti-patterns-and-repairs.md"
commit_sha: "4b75b56c13f5d61be5238fdbc7c20af5c6f89df7"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:8 — Common anti-patterns and repairs"
line_start: 85120
line_end: 85133
dependencies:
  - "A.19.ECS"
  - "A.22.CGUS"
  - "C.17-C.19"
  - "C.32.P2S"
  - "E.2.DA"
  - "E.21"
  - "E.22"
  - "E.23"
  - "E.9.DA"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
---

### E.23:8 - Common anti-patterns and repairs

| Anti-pattern | Repair |
|---|---|
| **Checklist closed, quality improved.** Discharge count replaces re-evaluation. | Re-evaluate the changed object. |
| **Loop result without evaluation form.** The loop says the object improved but records only prose, applied rows, or values without the named evaluation's evidence basis. | Re-run the object-under-improvement evaluation in its declared result-row shape. |
| **Agentic retry as method law.** Repetition continues without a scale-qualified predicted evaluation-result change. | Add `ExpectedEvaluationResultChange@Context`, cost and risk, trade-offs, and a stop or switch condition. |
| **Operation-family creep.** Verification, memory, supervision, or search is added everywhere. | Keep only operations that can change the evaluation result enough to justify cost. |
| **Goodharted pass.** Visible values rise while protected qualities worsen, or a non-`5` value is treated as a defect to be fixed by more apparatus. | Use trade-off inspection; apply `E.13` when the visible value is replacing the intended value; reject, delete, split, relocate, or hold dominated changes; continue searching for substantive content improvement when the improvement aim is still open; record `stay at current value` only when the `LoopEvaluationEvidenceBasis@Context` shows that no non-dominated content improvement remains. |
| **Lexical substitution closure.** A trigger word disappears, but the replacement narrows, widens, or changes the object kind; for example a graph-shaped method or workflow cue becomes a work sequence without a selected ontology decision. | Reopen the row, recover the pre-repair and post-repair kind through `E.10`, `F.19`, `F.18`, or the governing pattern, and leave the repair blocking if the kind cannot be preserved or explicitly changed by accepted decision. |
| **Maturity-ceiling stop.** All-`5` is treated as end of development. | Close this loop locally and record reopen conditions. |
| **SoTA citation as self-assignment.** Sources are cited as proof of frontier quality. | State source contributions and re-evaluate the composed result. |
| **Loop engineering as ontology.** A fashionable source phrase is treated as a new Core kind or as proof that all repeated activity is one improvement loop. | Use the phrase only as an entry cue; recover object version and evaluation, or send the live claim to its direct governing pattern. Common exits are work, gates, evolutionary retention and publication, source use, refresh, transformation-flow, and DPF governing patterns. |

