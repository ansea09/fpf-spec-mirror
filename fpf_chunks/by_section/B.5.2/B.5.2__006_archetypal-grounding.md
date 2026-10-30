---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Generate and Compare Candidate Explanations (Abductive Loop)"
section_id: "B.5.2:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__006_archetypal-grounding.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "B.5.2 — Generate and Compare Candidate Explanations (Abductive Loop)"
  - "B.5.2:5 — Archetypal Grounding"
line_start: 49538
line_end: 49545
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

**Tell.** Abduction develops a candidate conjecture from a typed prompt through explicit rival generation and plausibility comparison.

**Show (System).** An operations team sees a recurring latency spike that existing explanations do not cover. They publish an `AnomalyStatement`, compare rival causes against current telemetry and mechanism knowledge, and retain a qualified prime conjecture. They name a possible discriminating probe without assigning a maturity level or committing the service team to an experiment.

**Show (Episteme).** A research group notices that two accepted results no longer fit together under one framing. It publishes a `ProbeCuePrompt`, enumerates several rival explanatory reframings, rejects the ones that fail scope fit or would not generate decisive probes, and advances one candidate explanation as the next working hypothesis.

