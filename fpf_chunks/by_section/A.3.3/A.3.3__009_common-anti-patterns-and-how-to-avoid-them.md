---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__009_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "646b41f84ffef4918ad9bdb34e7b450f0c4903ee"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 8635
line_end: 8646
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

### A.3.3:8 - Common Anti-Patterns and How to Avoid Them

| Anti-pattern | Repair |
| --- | --- |
| "The procedure is the dynamics." | Put the semantic way of doing in `U.Method`; identify the claim-bearing episteme that the procedure text represents as `U.MethodDescription` only when it passes A.3.2; keep representation and publication separate; and put the state-space/law episteme in `U.Dynamics`. |
| "Telemetry is the dynamics." | Keep telemetry as a separately identified observation or source record `O`; include exact Work-side facts `W` only when Work is actually current, then derive `trace(W, O, D)` through the declared observation relation and compare it with the law. |
| "The dashboard is our state space." | Recover characteristics, units, scales, comparability relations, operating region, and invariants. |
| "The simulation approved the release." | Keep simulation as prediction; use `A.20`, `A.21`, `A.10`, or `B.3` for gate, evidence, and assurance claims. |
| "The model works everywhere." | State the applicability window and lowering condition; use `C.27.TA` for currentness and `C.29` for transfer. |
| "A workflow diagram proves the dynamics." | Recover whether the diagram describes a method, method description, work plan, dated work occurrence, selected transformation-flow structure, evidence relation, mechanism, or transition-law claim graph. |
| "A learned predictor is the law." | State training domain, observation relation, uncertainty, error policy, and applicability window before using prediction. |

