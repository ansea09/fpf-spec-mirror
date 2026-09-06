---
chunk_kind: "child"
pattern_id: "E.23"
pattern_title: "Quality Improvement Loop Method"
section_id: "E.23:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/E.23/E.23__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "43c46859c3926a371fa60cfb1c76aefa19f9eaf9"
heading_path:
  - "E.23 — Quality Improvement Loop Method"
  - "E.23:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 90421
line_end: 90437
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

### E.23:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
|---|---|
| **Checklist closed, quality improved.** Discharge count replaces re-evaluation. | Re-evaluate the changed object and apply `CC-E23-4` when dated Work is asserted. |
| **Loop result without evaluation form.** The loop says the object improved but retains no evidence in the declared evaluation form. | Restore that result form and evidence basis, then apply `CC-E23-4` to any dated Work claim. |
| **Agentic retry as method law.** Repetition continues without a scale-qualified predicted evaluation-result change. | Add `ExpectedEvaluationResultChange@Context`, cost and risk, trade-offs, and a stop or switch condition. |
| **Operation-family creep.** Verification, memory, supervision, or search is added everywhere. | Keep only operations that can change the evaluation result enough to justify cost. |
| **Goodharted pass.** Visible values rise while protected qualities worsen, or a non-`5` value is treated as a defect to be fixed by more apparatus. | Use trade-off inspection; apply `E.13` when the visible value is replacing the intended value; reject, delete, split, relocate, or hold dominated changes; continue searching for substantive content improvement when the improvement aim is still open; record `stay at current value` only when the `LoopEvaluationEvidenceBasis@Context` shows that no non-dominated content improvement remains. |
| **Lexical substitution closure.** A trigger word disappears, but the replacement narrows, widens, or changes the object kind; for example a graph-shaped method or workflow cue becomes a work sequence without a selected ontology decision. | Reopen the row, recover the pre-repair and post-repair kind through `E.10`, `F.19`, `F.18`, or the subject pattern, and leave the repair blocking if the kind cannot be preserved or explicitly changed by accepted decision. |
| **Maturity-ceiling stop.** All-`5` is treated as end of development. | Close this loop locally and record reopen conditions. |
| **SoTA citation as self-assignment.** Sources are cited as proof of frontier quality. | State source contributions and re-evaluate the composed result. |
| **Loop engineering as ontology.** A fashionable source phrase is treated as a new Core kind or as proof that all repeated activity is one improvement loop. | Use the phrase only as an entry cue; recover object version and evaluation, or use its subject pattern for the live claim. Common exits are work, gates, evolutionary retention and publication, source use, refresh, transformation-flow, and DPF subject patterns. |
| **Proposal as performance.** A selected proposal or `continue` decision is treated as if the repair happened. | Apply `CC-E23-13`: keep selection epistemic until separate Work and an obtaining result or change relation exist. |
| **Cycle as Work or context.** A record, dashboard, retry label, or visible arrow cycle is treated as enduring Work or ambient context. | Apply `CC-E23-14`: recover the conditional structure only when needed, and identify each asserted performed pass separately. |
| **Finding as actual Problem.** A low coordinate, floor miss, or loop-entry need is treated as a Problem occurrence. | Keep the finding epistemic; cite C.22.PFR only when one actual condition and one criterion-applicability occurrence make the temporally identified `ProblematicForRelation` obtain. |

