---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__006_archetypal-grounding.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:5 — Archetypal Grounding"
line_start: 6716
line_end: 6737
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.20"
  - "A.21"
  - "A.3.1"
  - "A.3.2"
  - "A.6.1"
  - "B.3"
  - "B.4"
  - "C.2.P.DR"
  - "C.27"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
  - "U.Mechanism"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "model"
  - "simulation"
  - "state evolution"
  - "state space"
---

### A.3.3:5 - Archetypal Grounding

#### A.3.3:5.1 - Reactor control

A reactor team models temperature and concentration under a nonlinear ODE with disturbances. The ODE, state space, observation relation, and operating region are `U.Dynamics`. The control policy is `U.Method`; the controller code is `U.MethodDescription` unless a dated run or mechanism claim is current. Thermocouple readings become evidence only through `A.10` or the direct evidence pattern.

#### A.3.3:5.2 - Reliability and operations

A service platform models backlog, arrival rate, and incident recovery with a queueing or birth-death model. The model can predict whether an SLO is feasible, but the service promise remains `U.PromiseContent`, and release or gate use needs the gate pattern.

#### A.3.3:5.3 - Evolutionary architecture

An architecture group tracks latency, coupling, operational cost, and change lead time across releases. A discrete-time transition map over those characteristics can be `U.Dynamics`. Architecture moves, selected structures, and views stay with architecture patterns; work occurrences and measurements stay with work and evidence patterns.

#### A.3.3:5.4 - Knowledge dynamics

A claim portfolio uses belief, evidence weight, source currentness, and contestability as state coordinates. A Bayesian or likelihood update is a dynamics episteme over claim state. The studies, reviews, and source records are evidence values; the dynamics model does not make a claim true by itself.

#### A.3.3:5.5 - Natural physical evolution

The Moon orbiting Earth can be modeled as `U.Dynamics` without pretending that the Moon enacts a method or performs governed work. A role assignment such as satellite classification may be well-formed, but it does not create method-work alignment.

