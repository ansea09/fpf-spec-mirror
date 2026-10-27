---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:8"
section_title: "Corridor, transfer, and durability discipline"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__009_corridor-transfer-and-durability-discipline.md"
commit_sha: "c475118bc1c11d2921b14f74c876e69c24ced3ea"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:8 — Corridor, transfer, and durability discipline"
line_start: 62469
line_end: 62480
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

### C.22.1:8 - Corridor, transfer, and durability discipline

- If the adaptation claim depends on entering a new solution corridor, publish the `corridorEntryBaseline` first: the prior repertoire, baseline set, or comparison family relative to which corridor entry is being claimed.
- State `corridorEntryEvidence` that supports the claimed difference from that baseline, such as a reproducible solution class, a stable descriptor shift or a supported stepping-stone sequence. Name what distinguishes the corridor; an unfamiliar sample alone does not establish entry.
- If a stepping stone mattered, publish the stepping-stone evidence as part of the adaptation signature rather than treating it as retrospective color.
- Corridor or stepping-stone notes do not replace the work-measure threshold account; they explain why the adaptation path matters, not whether the threshold was actually reached.
- A fast threshold result is not yet enough to claim durable specialization.
- If transfer to a neighboring task family is claimed, name the transfer target and the observed gain explicitly.
- If retention is claimed, name the reuse or retention window rather than letting durability hide inside one isolated run.
- If specialization harms neighboring task families, narrows reusable competence, or creates de-specialization cost, publish that in `downsideEffect?` rather than telling only the upside story.
- If post-threshold performance matters to later exploitation, publish `postThresholdEfficiency?` so the claim is not trapped at the threshold-crossing moment only.

