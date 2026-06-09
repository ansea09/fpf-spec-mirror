---
chunk_kind: "child"
pattern_id: "C.26"
pattern_title: "Quantum-Like Modeling Lens"
section_id: "C.26:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26/C.26__003_problem.md"
commit_sha: "093d30e806a1466e24032733eb020bb5a5f585cc"
heading_path:
  - "C.26 — Quantum-Like Modeling Lens"
  - "C.26:2 — Problem"
line_start: 46015
line_end: 46022
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.3"
  - "A.6"
  - "A.6.3.CSC"
  - "A.6.3.RT"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.26.1"
  - "C.26.1-C.26.3"
  - "C.26.2"
  - "C.26.3"
  - "E.8"
  - "E.9"
  - "F.9"
keywords:
  - "QL-NQ"
  - "QL-lite"
  - "incompatible probes"
  - "instrument update"
  - "minimal admissible output"
  - "order effect"
  - "probe frame"
  - "quantum-like"
  - "source-loss coarsening"
  - "state export"
---

### C.26:2 - Problem

Without this pattern, teams make five recurring mistakes.

They treat a probe as a neutral read when the probe changes later answers or behavior. They combine two posterior-looking outputs as if both came from one shared sample space. They export a team state, dashboard value, or context-map result as if it were a faithful-enough export for the intended use. They compress a large state representation for speed and then reuse the shortcut outside its admissible-use scope. They let words such as `quantum`, `entanglement`, `collapse`, or `field` import ontology that the model never earned.

The result is not merely loose wording. The team may approve a release from a dashboard whose publication and operational use changed the work it was supposed to report, average incompatible risk estimates, copy a local decision into another bounded context after the bridge lost the live coordination, or claim a speed gain because the representation was low-bit, linear, symbolic, or compressed without naming the loss.

