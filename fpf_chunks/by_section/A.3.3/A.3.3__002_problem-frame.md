---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__002_problem-frame.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:1 — Problem frame"
line_start: 6828
line_end: 6851
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
  - "A.3.4"
  - "A.6.1"
  - "B.3"
  - "C.2.P.DR"
  - "C.27"
  - "C.27.TA"
  - "C.29"
  - "E.10"
  - "E.10.ARCH"
  - "E.20"
  - "F.18"
  - "U.BoundedContext"
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

### A.3.3:1 - Problem frame

Use this pattern when a project needs one reusable model of **how state changes** in a bounded context: a state space, a transition law, an observation relation, and the conditions under which prediction, simulation, calibration, conformance, drift, or gating claims are warranted.

Use it when the working question is:

* which holon, episteme, system-in-role, claim, service, resource bundle, architecture, or other EntityOfConcern has changing state;
* which characteristics define the state space;
* which transition law states how those coordinates evolve;
* which observations or work-derived traces can be compared with the law;
* whether a prediction can be used for comparison, gating, assurance, planning, or control.

**Primary EntityOfConcern.** The `EntityOfConcern` is `U.Dynamics`: an `U.Episteme` that specifies a state space and a state-transition law for one or more EntitiesOfConcern in a bounded context.

**E.24.UK settlement.** `U.Dynamics` is retained as a dependent durable U-kind under the `U.Episteme` settlement. Its durable value is the reusable state-space and transition-law episteme for changing state in a bounded context. It is not a root change kind, not the changed EntityOfConcern, not a work occurrence, and not a flow structure; components such as `stateSpace`, `transitionLaw`, `observationRelation`, and `calibrationOrParameterSource` remain slots or claim graphs inside the dynamics episteme unless another governing pattern makes one of them separately addressable.

**First useful move.** Name the changing EntityOfConcern, the bounded context, the state-space characteristics, the transition law, the observation relation, and the applicability window. If these cannot be named, the current claim is not yet ready for prediction, conformance, or gate use.

**What goes wrong if missed.** Procedure text becomes "the dynamics", telemetry becomes a law, one observed run becomes a prediction, a dashboard becomes a state space, or a simulation becomes permission to act.

**What this buys in practice.** Practitioners can compare predictions with traces, decide whether stale predictions may still be used, separate methods from laws of change, and decide where mathematical-lens, temporal, evidence, assurance, or gate patterns must take over.

**Not this pattern when.** If the source only states a semantic way of doing, use `A.3.1`. If it states an episteme describing that way, use `A.3.2`. If it states bounded transformation under conditions, use `A.3.4`. If it states planned work or dated work, use `A.15.2` or `A.15.1`. If it states a mechanism algebra, use `A.6.1` and `E.20`. If it states only freshness, rhythm, inertia, delay, window, or currentness as a positive temporal aspect, use `C.27.TA`; if it states adequacy or supported use of an authored temporal claim, use `C.27`. If it states only evidence or assurance, use `A.10` or `B.3`.

