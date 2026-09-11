---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__006_archetypal-grounding.md"
commit_sha: "ef9ded2cb965193aa2484c84f06d65770439cef8"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:5 — Archetypal Grounding"
line_start: 41215
line_end: 41222
dependencies:
  - "A.10"
  - "A.16"
  - "A.22.CGUS"
  - "A.6.P"
  - "B.3.3"
  - "B.4.1"
  - "B.5"
  - "B.5.2.0"
keywords:
  - "abduction"
  - "candidate hypotheses"
  - "explanatory prompt"
  - "origin trace"
  - "plausibility filters"
  - "route-to-hypothesis"
---

### B.5.2:5 - Archetypal Grounding

**Tell.** Abduction is not "a flash of insight." It is the governed passage from a typed prompt to a candidate conjecture through explicit rival generation and plausibility comparison.

**Show (System).** An operations team sees a recurring latency spike that existing explanations do not cover. They publish an `AnomalyStatement`, compare rival causes against current telemetry and mechanism knowledge, and retain a qualified prime conjecture. They name a possible discriminating probe without assigning a maturity level or committing the service team to an experiment.

**Show (Episteme).** A research group notices that two accepted results no longer fit together under one framing. It publishes a `ProbeCuePrompt`, enumerates several rival explanatory reframings, rejects the ones that fail scope fit or would not generate decisive probes, and advances one candidate explanation as the next working hypothesis.

