---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Generate and Compare Candidate Explanations (Abductive Loop)"
section_id: "B.5.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__006_archetypal-grounding.md"
commit_sha: "e307edbd91c04c1d85661bd309b9944fac251937"
heading_path:
  - "B.5.2 — Generate and Compare Candidate Explanations (Abductive Loop)"
  - "B.5.2:5 — Archetypal Grounding"
line_start: 49683
line_end: 49690
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
  - "C.28.CM"
keywords:
---

### B.5.2:5 - Archetypal Grounding

**Tell.** Abduction develops candidate conjectures from an admissible prompt through generation, consideration of serious alternatives and plausibility comparison.

**Show (System).** An operations team sees a recurring latency spike that existing explanations do not cover. They publish an `AnomalyStatement`, compare rival causes against current telemetry and mechanism knowledge, and retain a qualified prime conjecture. They name a possible discriminating probe.

**Show (Episteme).** A research group notices that two accepted results no longer fit together under one framing. It publishes a `ProbeCuePrompt`, enumerates several rival explanatory reframings, rejects the ones that fail scope fit or yield no interpretable implication, deduction or possible discriminating contrast, and advances one candidate explanation as the next working hypothesis.

