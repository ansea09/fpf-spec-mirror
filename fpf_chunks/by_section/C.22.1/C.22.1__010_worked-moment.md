---
chunk_kind: "child"
pattern_id: "C.22.1"
pattern_title: "Task-family adaptation signature"
section_id: "C.22.1:9"
section_title: "Worked moment"
source_path: "FPF-Spec.md"
output_path: "by_section/C.22.1/C.22.1__010_worked-moment.md"
commit_sha: "9fa2a3596dab58d282d736bcf413cdda4286db0a"
heading_path:
  - "C.22.1 — Task-family adaptation signature"
  - "C.22.1:9 — Worked moment"
line_start: 62859
line_end: 62868
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

### C.22.1:9 - Worked moment

Consider two research setups, A and B, adapting to the same catalyst-search family. This is an illustrative comparison. The declared threshold is at least 80 accepted predictions out of the same 100 held-out cases under a fixed validation rule. Both start with the same training corpus and no prior exposure to those held-out cases. Time starts when adaptation begins; the budget counts all adaptation and evaluation calls. The rule checks threshold attainment at the end of each round.

A first meets the rule after 2 hours and 120 calls; B after 6 hours and 480 calls. Both finish at 85/100. The signatures therefore distinguish acquisition time and cost despite equal final scores. They report first observed attainment at the declared checkpoints, without claiming an unobserved earlier crossing.

On a named adjacent family, the same before/after test gives A 60/100 then 70/100 and B 60/100 then 60/100. That supports A's observed 10-percentage-point transfer gain on this test and no observed gain for B on it; it does not settle all neighboring families. Retention beyond the measured run is untested, and no durable-specialization claim is made. If A also claims corridor entry, it names the prior repertoire and the repeatable solution class absent from that baseline; the faster threshold alone does not supply this evidence.

The comparison can finish with these bounded claims. If A's prior exposure later proves different, reopen the equal-exposure comparison while retaining the observed histories. A later retention claim needs its own window and observations. A selector may use the signature under its applicable rule; the signature alone chooses neither setup.

