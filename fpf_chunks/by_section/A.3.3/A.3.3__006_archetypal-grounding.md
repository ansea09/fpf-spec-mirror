---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:5"
section_title: "Archetypal Grounding"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__006_archetypal-grounding.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:5 — Archetypal Grounding"
line_start: 9145
line_end: 9175
dependencies:
  - "A.1.1"
  - "A.10"
  - "A.15.1"
  - "A.15.2"
  - "A.19"
  - "A.2.6"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.1"
  - "A.3.2"
  - "A.3.4"
  - "A.6.1"
  - "B.1.5"
  - "B.3"
  - "C.16"
  - "C.2.1"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "F.18"
  - "F.19"
  - "U.ClaimScope"
  - "U.Mechanism"
  - "U.Method"
  - "U.MethodDescription"
  - "U.Transformation"
  - "U.Work"
  - "U.WorkPlan"
keywords:
  - "calibration"
  - "dynamics"
  - "observation relation"
  - "prediction"
  - "simulation"
  - "state space"
  - "transition law"
---

### A.3.3:5 - Archetypal Grounding

#### A.3.3:5.1 - Reactor control

A reactor team models temperature and concentration under a nonlinear ODE with disturbances. One claim-bearing reactor-model episteme is `U.Dynamics`. Its ClaimGraph declares the nonlinear ODE as `transitionLaw`, the exact temperature-and-concentration state space as `stateSpace`, the observation relation, disturbances, and the operating region and applicability window, or cites exact references that supply those declarations. The control policy is `U.Method`; a claim-bearing episteme represented by the controller code may be `U.MethodDescription` only when it passes A.3.2 for that Method, while the code representation, dated controller runs, and mechanism claims stay with their governing patterns. Thermocouple readings become evidence only through `A.10` or the direct evidence pattern.

Side-by-side split:

| Filled question | `U.Dynamics` value | `U.Transformation` value |
| --- | --- | --- |
| EntityOfConcern | exact reactor temperature-and-concentration state subject interpreted under the declared scheme and operating-region claim | the exact catalyst bed as changed referent for one actual regeneration occurrence |
| Core relation | state-space coordinates plus nonlinear transition-law claim graph, observation relation, disturbances, operating region, and applicability window | exact catalyst bed; maintenance temporal extent and regeneration boundary; boundary conditions; actual fouling, flow, pressure, and catalyst-condition facts before, during, and after that boundary; continuity or reidentification rule for the bed and this one occurrence |
| Use | possible, predicted, simulated, or probable state change; conformance, drift, and gate input only when the receiving use's required conditions are satisfied (§4.6) | actual bounded-change claim on the recovered subject-side occurrence basis |
| Kept outside | method, controller code, dated runs, evidence, and gate authority | reusable law of state change, method description, work occurrence, evidence relation, and permission to act |

#### A.3.3:5.2 - Reliability and operations

A service platform models backlog, arrival rate, and incident recovery with a queueing or birth-death model. The model can predict whether an SLO is feasible, but the service promise remains `U.PromiseContent`, and release or gate use needs the gate pattern.

#### A.3.3:5.3 - Evolutionary architecture

An architecture group tracks latency, coupling, operational cost, and change lead time across releases. An episteme about that architecture can be `U.Dynamics` when its `ClaimGraph` declares a state space over those characteristics and a discrete-time transition map as the transition law. Architecture moves, selected structures, and views stay with architecture patterns; work occurrences and measurements stay with work and evidence patterns.

#### A.3.3:5.4 - Knowledge dynamics

A claim portfolio uses belief, evidence weight, source currentness, and contestability as state coordinates. An episteme declaring a Bayesian or likelihood update as the transition law over that claim-state space is `U.Dynamics`. The studies, reviews, and source records are evidence values.

#### A.3.3:5.5 - Natural physical evolution

A `U.Dynamics` episteme can model the Moon's motion around Earth using an orbital state space and transition law.

