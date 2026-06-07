---
chunk_kind: "child"
pattern_id: "C.26.3"
pattern_title: "Viability-Envelope Boundary Regulation"
section_id: "C.26.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.26.3/C.26.3__012_sota-echoing.md"
commit_sha: "18497f0808242ab7c1a31cb5c94898e9f6b6879d"
heading_path:
  - "C.26.3 — Viability-Envelope Boundary Regulation"
  - "C.26.3:11 — SoTA-Echoing"
line_start: 47234
line_end: 47252
dependencies:
  - "A.10"
  - "A.15"
  - "A.19"
  - "A.3"
  - "A.6"
  - "B.3"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.25"
  - "C.26"
  - "C.26.1"
  - "C.26.2"
  - "U.Dynamics"
keywords:
  - "allostasis"
  - "boundary regulation"
  - "failure mode"
  - "homeostasis"
  - "metric-induced distortion"
  - "quality bundle"
  - "sensor/probe/actuator split"
  - "service viability"
  - "viability envelope"
---

### C.26.3:11 - SoTA-Echoing

| Pattern claim | Practice source | Pattern implication | Adoption stance |
| --- | --- | --- | --- |
| Viability maintenance is not fixed-value homeostasis only; stability can be relational, variational, dynamic, allostatic, metastable, and resilient. | [Conceptual foundations of physiological regulation incorporating the free energy principle and self-organized criticality](https://www.sciencedirect.com/science/article/pii/S0149763423004281). | Use viability envelopes and stability-through-change; reject one-scalar optimization and "all architecture is homeostasis." | Adapt as architecture-facing envelope discipline. |
| Action and perception are coupled under partial observability and cost. | [Active inference as a theory of sentient behavior](https://www.sciencedirect.com/science/article/pii/S0301051123002612). | Treat sensors, probes, dashboards, and actuators as part of the envelope relation when they change behavior or viability. | Adapt for measurement-as-action and planning cost. |
| Active-inference engineering already appears in energy/building control under privacy, partial observability, evolving conditions, and abrupt changes. | [Active Inference for Energy Control and Planning in Smart Buildings and Communities](https://arxiv.org/abs/2503.18161). | Use engineering examples cautiously: they show the kind of control problem, not settled FPF doctrine. | Use as emerging engineering anchor. |
| Boundaries can be statistical/computational descriptions of what a system can measure, model, and affect. | [The Computational Boundary of a Self](https://philpapers.org/rec/LEVTCB-3) and [The Markov blankets of life](https://philarchive.org/rec/KIRTMB). | Name boundary conditions and information constraints without reifying a boundary substance. | Adapt with map-territory caution. |
| Excess Bayesian / active-embodied inference shows the cost of moving sensor, body, instrument, or access point to obtain a discriminating observation. | [Connecting the free energy principle with quantum cognition](https://www.frontiersin.org/articles/10.3389/fnbot.2022.910161/full). | Treat probe placement, access placement, and observation cost as part of viability-envelope work when they change the decision. | Adapt for probe/action cost, not as a replacement for ordinary Bayesian or active-inference routes. |
| Platform and software engineering already treats many quality concerns as trade-off bundles. | Reliability, incident, platform, compliance, energy, support, operator-load practice, and [Google SRE SLO / error-budget practice](https://sre.google/workbook/implementing-slos/), coordinated with `C.25`. | Make the quality bundle explicit and state actuator authority, latency, adaptation cost, and failure mode. | Adopt through FPF quality-bundle routes. |

Worked-slice discipline from these rows:

- state the envelope before importing source terminology;
- translate source terms into selected structures, `ArchitectureOf@Context` relations, architecture descriptions, structural views, or exact C.30 subcases;
- keep sensors, probes, actuators, and metrics distinct;
- state adaptation cost and failure mode;
- apply ordinary quality and measurement patterns to one-scalar quality concerns.

