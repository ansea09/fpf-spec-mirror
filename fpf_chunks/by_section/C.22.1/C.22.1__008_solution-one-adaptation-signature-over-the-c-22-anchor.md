---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:7"
section_title: "Solution — one adaptation signature over the C.22 anchor"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__008_solution-one-adaptation-signature-over-the-c-22-anchor.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:7 — Solution — one adaptation signature over the C.22 anchor"
line_start: 62449
line_end: 62468
dependencies:
  - "A.15"
  - "C.19.1"
  - "C.22"
  - "C.22.1"
  - "C.24"
  - "E.10"
  - "E.16"
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
- Bind the adaptation signature to the declared `TaskFamilyRef` or `TaskSignature` and work target. Reuse an existing account when it supplies the needed fields and grounds.
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
- Anchor these fields to the same work target and work-measure threshold semantics declared by `C.22`. State the time origin, budget boundary and threshold-observation rule. If the threshold was not reached or the available history cannot establish its first crossing, say so and retain the observed limit; do not invent a crossing time or cost.
- `C.22` continues to carry the declared task-family anchor, task typing, and baseline `TaskSignature`. `C.22.1` narrows the adaptation-signature question to threshold timing, reuse, downside, and corridor-entry disclosure over that existing anchor.

