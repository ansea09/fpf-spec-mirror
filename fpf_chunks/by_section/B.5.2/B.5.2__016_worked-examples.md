---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:15"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__016_worked-examples.md"
commit_sha: "e2457cb64712832c1652450aaa143636078c85b1"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:15 — Worked Examples"
line_start: 41286
line_end: 41327
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

### B.5.2:15 - Worked Examples

#### B.5.2:15.1 - Service degradation diagnosis

A service team notices recurring latency spikes during one operating window. The prompt species is `AnomalyStatement`: *why does latency spike in the evening batch window despite unchanged nominal load?*

The candidate set includes:

- queue saturation in one downstream dependency,
- a time-window interaction with backup traffic,
- and a recent mechanism regression in cache invalidation.

The backup-interaction conjecture is preferred because its timing fits the existing observations and it remains consistent with known mechanisms; the other two candidates remain live. Isolating backup traffic and comparing latency against prior windows is a possible discriminator. When that probe is obtainable and its expected contribution justifies its cost and delay, it can be selected as separate work. The conjecture itself records no observation from that unperformed probe.

Now keep the same observations and rival set but make the probe window unavailable. The qualified conjecture and its uncertainty remain; if the available comparison cannot select a winner, defer that selection. No new test, waiver or study proposal is needed just to finish the present abductive result.

In both variants, suppose an existing operational qualification independently supports a bounded diversion to a spare instance for this traffic and interval, with sufficient capacity and actual permission, across all three remaining causes. C.11 can support that service response on the available basis. Diverting traffic does not identify the cause; a causal claim about the mechanism still needs the appropriate C.28 support. If that operational basis is absent, do not infer a justified diversion from conjecture plausibility.

#### B.5.2:15.2 - Opportunity-driven materials inquiry

A research group sees an opportunity rather than a failure: a new fabrication method appears to create a micro-structure with useful thermal behavior. The prompt species is `OpportunityCuePrompt` rather than anomaly.

Candidate hypotheses include:

- the effect is caused by surface geometry,
- it is caused by composition gradients,
- or it is an effect of one measurement regime.

The geometry explanation is the prime conjecture because it fits more of the initial observations and suggests a clearer discriminating experiment. Keep the composition and measurement rivals visible. The possible experiment can inform a separate research choice; its description neither funds it nor makes it mandatory. Long-horizon research can be worthwhile on its own declared contribution, without treating the conjecture as an established thermal-performance result.

#### B.5.2:15.3 - Probe-driven theory repair

A theory-maintenance group identifies a probe-worthy mismatch between two accepted claims. The prompt species is `ProbeCuePrompt`: *what changed assumption would allow these two claims to coexist without contradiction?*

The candidate set includes:

- hidden scope restriction on the first claim,
- mistaken invariance assumption in the second,
- and a more general missing mediating construct.

The selected prime hypothesis is the mediating construct, but the scope-restriction candidate remains stored as a live rival because it could still outperform if later deductions fail. This example illustrates why `B.5.2` tracks the rival set rather than only the currently favored conjecture.

