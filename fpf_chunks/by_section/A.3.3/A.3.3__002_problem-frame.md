---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__002_problem-frame.md"
commit_sha: "9fba9529833b4e288fa149878b22a9ee44e1886f"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:1 — Problem frame"
line_start: 8990
line_end: 9016
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

### A.3.3:1 - Problem frame

Use this pattern when a project needs one reusable claim about **how the state of an exact EntityOfConcern can change**: a state space, a transition law, an observation relation, and the conditions under which prediction, simulation, calibration, conformance, drift, or gating claims may be relied on.

Use it when the working question is:

* which EntityOfConcern has changing state, distinguishing an obtaining assignment occurrence from a separately identified A.2.5 assignment-state relation when that distinction is current;
* which characteristics and local meanings define the state space;
* which transition law states how those coordinates evolve;
* which observations or work-derived traces can be compared with the law;
* over which operating region, claim scope, qualification window, parameter regime, or scale band the claim applies; and
* whether a prediction can be used for comparison, gating, assurance, planning, or control.

A passive System can be the changing entity. When an agency, dated Work, or F.6 attribution claim is current, establish its basis independently.

**Primary governed object.** A.3.3 examines one already identified claim-bearing `U.Episteme` candidate and judges whether that same individual belongs to the dependent kind `U.Dynamics`. Positive membership requires its exact C.2.1 `EntityOfConcern` to be the thing whose state is modelled and its ClaimGraph, interpreted under its effective `U.ReferenceScheme`, to declare both a state space and a state-transition law for that subject. The same episteme retains its C.2.1 identity.

**E.24.UK settlement.** `U.Dynamics` remains a dependent durable U-kind under `U.Episteme`. It is the reusable state-space and transition-law episteme. Components such as `stateSpace`, `transitionLaw`, `observationRelation`, and `calibrationOrParameterSource` remain ClaimGraph content or references inside the dynamics episteme unless another governing pattern independently identifies one of them.

**First useful move.** In one ordinary sentence, name the exact changing subject, the state coordinates and their meanings, the rule that relates earlier and later state, where that rule applies, and the applicable stop conditions. If that is enough for the current comparison, stop. Add observation, calibration, evidence, temporal, mathematical-lens, assurance, or gate machinery only when the proposed receiving use needs it. Before making a prediction, conformance, or gate-use claim, name the observation relation and exact applicability window; if either is unavailable, stop that stronger use.

**What goes wrong if missed.** Procedure text becomes "the dynamics", telemetry becomes a law, one observed run becomes a prediction, a dashboard becomes a state space, a description or selected graph is mistaken for the dynamics episteme, or a simulation becomes permission to act.

**What this buys in practice.** Practitioners can compare predictions with traces, decide whether stale predictions may still be used, separate Methods and MethodDescriptions from laws of change, and decide where characteristic, scope, temporal, mathematical-lens, evidence, assurance, or gate patterns must take over.

**Not this pattern when.** If the source only states a semantic way of doing, use `A.3.1`. If one episteme substantively describes that admitted Method, use `A.3.2`. If the question is an independently selected organization of exact constituents and obtaining relations, use `A.22`. If the source states one actual bounded change established by the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification, use `A.3.4`. A possible, predicted, simulated, or probable transition remains claim content. If it states planned work or dated work, use `A.15.2` or `A.15.1`. If it states a mechanism algebra, use `A.6.1` and `E.20`. If it states only freshness, rhythm, inertia, delay, window, or currentness as a positive temporal aspect, use `C.27.TA`; if it states adequacy or supported use of an authored temporal claim, use `C.27`. If it states only evidence or assurance, use `A.10` or `B.3`.

