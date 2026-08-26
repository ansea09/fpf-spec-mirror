---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:15"
section_title: "Conformance checklist"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__016_conformance-checklist.md"
commit_sha: "563f4c8e06a319cbd375b66cdbb2df27a5f8b9ef"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:15 — Conformance checklist"
line_start: 49979
line_end: 49986
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

### C.22.1:15 - Conformance checklist

- `CC-C22.1-1` An adaptation signature **SHALL** bind to one declared `TaskFamily` or `TaskSignature`, one work target, and one work-measure threshold target rather than one generic improvement story.
- `CC-C22.1-2` An adaptation signature **SHALL** publish `timeToThreshold`, `budgetToThreshold`, and `priorExposureDeclaration`; if threshold was not reached, the signature **SHALL** say so explicitly instead of implying success.
- `CC-C22.1-3` Any declared transfer, retention, post-threshold-efficiency, downside, corridor-entry, or stepping-stone claim **SHALL** be explicit by value with the target, baseline, evidence source, or evidence locus named, not left as narrative garnish.
- `CC-C22.1-4` This pattern may refine specialization timing and reuse claims over the declared `C.22` anchor, but it **SHALL NOT** redefine acceptance-gate thresholds, task-family attachment, or selector/parity law governed by another FPF pattern.
- `CC-C22.1-5` Downstream selector/parity pattern applications **SHALL** cite or consume the same published adaptation-signature field set rather than silently redefining threshold, prior-exposure, transfer, retention, downside, or corridor-entry terms.

