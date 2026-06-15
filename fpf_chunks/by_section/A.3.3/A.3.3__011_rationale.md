---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__011_rationale.md"
commit_sha: "c092a1f2299d88d42db012f3184aeff205c13219"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:10 — Rationale"
line_start: 7001
line_end: 7006
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

### A.3.3:10 - Rationale

FPF needs `U.Dynamics` because many practical questions are not about what an agent should do, but about how a state changes when the world evolves, a model is simulated, evidence arrives, a resource pool fluctuates, or an architecture changes. Those questions need a law of change, not a procedure, not a work log, and not a promise.

The pattern is deliberately broad because state-change reasoning appears in physics, control, software operations, reliability, strategy, architecture, and knowledge work. The shared kernel is not a universal notation. It is the distinction between state-space, transition law, observation relation, applicability window, and related governed claim families such as method, work, transformation, evidence, assurance, and gate use.

