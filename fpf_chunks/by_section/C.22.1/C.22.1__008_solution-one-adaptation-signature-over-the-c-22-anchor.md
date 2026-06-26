---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:7"
section_title: "Solution — one adaptation signature over the C.22 anchor"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__008_solution-one-adaptation-signature-over-the-c-22-anchor.md"
commit_sha: "40b232f11ed950ed34082273c57ff4f6c45b7f06"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:7 — Solution — one adaptation signature over the C.22 anchor"
line_start: 46537
line_end: 46556
dependencies:
  - "A.15"
  - "C.19.1"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "E.10"
  - "E.16"
  - "E.19"
  - "E.22"
  - "E.23"
  - "G.11"
  - "G.5"
  - "G.9"
keywords:
  - "adaptation signature"
  - "budget-to-threshold"
  - "corridor entry"
  - "downside field"
  - "prior exposure"
  - "retention"
  - "stepping stone"
  - "task-family specialization"
  - "time-to-threshold"
  - "transfer"
---

### C.22.1:7 - Solution — one adaptation signature over the `C.22` anchor

- Use one shared adaptation-signature field set for this question. `G.5`, `G.9`, and later notes may cite or consume it, but they should not silently rename threshold, prior-exposure, transfer, downside, or corridor-entry terms.
- When specialization is the live adaptation question, publish one adaptation signature bound to the declared `TaskFamilyRef` or `TaskSignature`, not one generic improvement claim.
- The signature should expose at least:
  - `thresholdTarget`
  - `timeToThreshold`
  - `budgetToThreshold`
  - `postThresholdEfficiency?`
  - `priorExposureDeclaration`
  - `transferTarget?`
  - `transferGain?`
  - `retentionWindow?`
  - `downsideEffect?`
  - `corridorEntryBaseline?`
  - `corridorEntryEvidence?`
  - `steppingStoneEvidence?`
- These fields stay anchored to the same work target and work-measure threshold semantics already declared by `C.22`, so adaptation is typed as movement toward usable specialization rather than as an ungrounded growth story.
- `C.22` continues to carry the declared task-family anchor, task typing, and baseline `TaskSignature`. `C.22.1` narrows the adaptation-signature question to threshold timing, reuse, downside, and corridor-entry disclosure over that existing anchor.

