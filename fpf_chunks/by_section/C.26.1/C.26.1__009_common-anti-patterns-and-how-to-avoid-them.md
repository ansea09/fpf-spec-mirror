---
chunk_kind: "child"
pattern_id: "C.26.1"
pattern_title: "Probe-Coupled Boundary Interaction"
section_id: "C.26.1:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.1/C.26.1__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.26.1 — Probe-Coupled Boundary Interaction"
  - "C.26.1:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 54711
line_end: 54720
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15"
  - "A.6"
  - "A.6.B"
  - "A.6.P"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.26"
  - "C.26.2"
  - "C.26.3"
  - "F.9"
keywords:
  - "API read"
  - "bridge result"
  - "dashboard as instrument"
  - "evidence window"
  - "export loss"
  - "passive read"
  - "probe-coupled boundary"
  - "survey"
  - "workshop as state-changing interaction"
---

### C.26.1:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Symptom | Repair |
| --- | --- | --- |
| Every interaction is QL | Any message, meeting, or API call is called probe-coupled. | Require a false passive-read, export, comparison, or optimization use. |
| Causal action mistaken for probe | A deployment or command changes the world, and QL is invoked. | Use intervention or work-governing patterns unless the action is being used as a readout of the state it changes. |
| Bridge loss alone | Export loses local meaning, but no state-changing probe is live. | Use `F.9` with loss notes. |
| Context-word drift | *Context* hides source-local meaning, a selected model-use organization, ClaimScope, a probe frame, or a measurement setup. | Name the actual value. Retain *bounded context* only when using the established DDD term. |
| Relation token leakage | `coupledBy(...)` appears as if already ratified. | Keep it as local drafting form or apply `A.6.P` and `F.18`. |

