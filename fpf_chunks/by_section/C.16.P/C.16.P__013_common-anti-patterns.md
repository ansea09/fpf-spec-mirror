---
chunk_kind: "child"
pattern_id: "C.16.P"
pattern_title: "Characteristic and Scale Precision Restoration"
section_id: "C.16.P:10"
section_title: "Common anti-patterns"
source_path: "FPF-Spec.md"
output_path: "by_section/C.16.P/C.16.P__013_common-anti-patterns.md"
commit_sha: "a0c90e3bbfcc0285893cc5bb9d4a88fcd224f00e"
heading_path:
  - "C.16.P — Characteristic and Scale Precision Restoration"
  - "C.16.P:10 — Common anti-patterns"
line_start: 40813
line_end: 40823
dependencies:
  - "A.10"
  - "A.15"
  - "A.17"
  - "A.18"
  - "A.19"
  - "A.19.ECS"
  - "A.20"
  - "A.21"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.Q"
  - "C.25"
  - "C.28"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.21"
  - "F.18"
  - "G.0"
  - "G.5"
  - "G.9"
keywords:
---

### C.16.P:10 - Common anti-patterns

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Metric-as-evidence | A metric is treated as evidence, proof, gate input, or decision authority without exact evidence, gate, decision, and measurement construction. | Recover characteristic and scale construction, then apply `A.10` or exact evidence, gate, or decision pattern if that claim is live. |
| Score-as-gate | A score is treated as gate passage, readiness, release, or decision. | Recover scale, threshold rule or reference, comparison reference or comparator set, and exact gate, decision, or release pattern. |
| Axis-as-ontology | Axis or dimension is treated as if it already named a characteristic or factor. | Recover `Characteristic`, coordinate, latent factor, mathematical lens, structural aspect, or ordinary prose. |
| Strong-without-scale | Strong or weak modifies a claim without scale, characteristic, or comparison reference or comparator set. | Write the exact characteristic and scale or demote to ordinary prose. |
| Indicator-as-indicated-characteristic | Indicator wording hides the indicated characteristic or proxy relation. | Name indicator role, indicated characteristic or claim, and proxy-distortion risk. |
| Characterization repair copied everywhere | Receiving patterns keep their own `metric`, `score`, or `strong` trigger lists. | Keep one thin cue and send hidden construction to `C.16.P`. |

