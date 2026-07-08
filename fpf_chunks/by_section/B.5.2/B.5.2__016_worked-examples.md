---
chunk_kind: "child"
pattern_id: "B.5.2"
pattern_title: "Abductive Loop"
section_id: "B.5.2:15"
section_title: "Worked Examples"
source_path: "FPF-Spec.md"
output_path: "by_section/B.5.2/B.5.2__016_worked-examples.md"
commit_sha: "c927fef1dac0f4d5f8ca93deef8a52de75e3f77b"
heading_path:
  - "B.5.2 — Abductive Loop"
  - "B.5.2:15 — Worked Examples"
line_start: 36190
line_end: 36227
dependencies:
  - "A.10"
  - "A.16"
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

The prime hypothesis is not selected because it sounds most familiar. It is selected because it best fits the observed window, remains consistent with known mechanism declarations, and generates a concrete next probe: isolate backup traffic and compare the latency shape against prior windows. The resulting conjecture becomes an `L0` hypothesis with one explicit evidence-acquisition relation.

#### B.5.2:15.2 - Opportunity-driven materials inquiry

A research group sees an opportunity rather than a failure: a new fabrication method appears to create a micro-structure with useful thermal behavior. The prompt species is `OpportunityCuePrompt` rather than anomaly.

Candidate hypotheses include:

- the effect is caused by surface geometry,
- it is caused by composition gradients,
- or it is an effect of one measurement regime.

The selected prime hypothesis is the geometry explanation because it explains more of the initial observations and yields a cleaner discriminating experiment. The loop shows why opportunity-driven abduction still needs rival tracking; without it, attractive novelty language would substitute for hypothesis discipline.

#### B.5.2:15.3 - Probe-driven theory repair

A theory-maintenance group identifies a probe-worthy mismatch between two accepted claims. The prompt species is `ProbeCuePrompt`: *what changed assumption would allow these two claims to coexist without contradiction?*

The candidate set includes:

- hidden scope restriction on the first claim,
- mistaken invariance assumption in the second,
- and a more general missing mediating construct.

The selected prime hypothesis is the mediating construct, but the scope-restriction candidate remains stored as a live rival because it could still outperform if later deductions fail. This example illustrates why `B.5.2` tracks the rival set rather than only the currently favored conjecture.

