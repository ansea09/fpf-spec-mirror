---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "cb17c555f343780e31e5fea236a74adc69295736"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 6795
line_end: 6806
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

### A.3.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The procedure is the dynamics." | Put the semantic way of doing in `U.Method`, the procedure text in `U.MethodDescription`, and the law of state change in `U.Dynamics`. |
| "Telemetry is the dynamics." | Treat telemetry as evidence or source material; derive `trace(W, D)` and compare it with the declared law. |
| "The dashboard is our state space." | Recover characteristics, units, scales, comparability relations, operating region, and invariants. |
| "The simulation approved the release." | Keep simulation as prediction; use `A.20`, `A.21`, `A.10`, or `B.3` for gate, evidence, and assurance claims. |
| "The model works everywhere." | State the applicability window and lowering condition; use `C.27.TA` for currentness and `C.29` for transfer. |
| "A workflow diagram proves the dynamics." | Recover whether the diagram describes a method, method description, work plan, dated work occurrence, selected transformation-flow structure, evidence relation, mechanism, or transition-law claim graph. |
| "A learned predictor is the law." | State training domain, observation relation, uncertainty, error policy, and applicability window before using prediction. |

