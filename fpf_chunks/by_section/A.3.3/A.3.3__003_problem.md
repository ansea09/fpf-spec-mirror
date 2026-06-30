---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__003_problem.md"
commit_sha: "e264bfb1cdeecdfe1b7407deba14165475c20ac7"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:2 — Problem"
line_start: 6859
line_end: 6868
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

### A.3.3:2 - Problem

Without a first-class `U.Dynamics`, state-change claims collapse into nearby but different claims:

1. **Recipe becomes law.** Teams put procedure text, a control diagram, a workflow diagram, or a method description where a state-transition law should be.
2. **Trace becomes law.** Dated work logs, telemetry, and incident sequences are treated as if past events defined what must happen.
3. **Dashboard becomes state space.** Metric lists appear without characteristics, units, scales, topology, geometry, invariants, or operating region.
4. **Prediction becomes authority.** A model output is used for a gate, release, safety, or work decision without freshness, non-expansiveness, commutation, observation, or assurance conditions.
5. **Domain vocabulary blocks transfer.** Physics, control, finance, reliability, operations, knowledge dynamics, and architecture all talk about change differently; FPF needs one kernel pattern that preserves their differences without inventing separate ontologies.

