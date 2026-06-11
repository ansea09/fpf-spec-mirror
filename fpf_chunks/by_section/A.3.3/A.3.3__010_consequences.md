---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__010_consequences.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:9 — Consequences"
line_start: 6789
line_end: 6807
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

### A.3.3:9 - Consequences

| Benefit | Cost or caution |
| --- | --- |
| Prediction, simulation, conformance, drift, and calibration claims become reviewable. | The project must name state-space characteristics and observation relations rather than relying on dashboard labels. |
| Methods, method descriptions, mechanisms, work, and dynamics stop substituting for each other. | Source labels like `process` and `model` often need `E.10.ARCH` recovery before typed assignment. |
| Gate and release use becomes safer because prediction needs freshness or a stated mathematical condition. | Some attractive predictions become inadmissible until observation or proof is supplied. |
| Dynamics can cover physical, organizational, epistemic, software, architectural, and resource examples under one FPF kind. | Domain-specific laws still need their own notation, assumptions, and evidence disciplines. |
| Mathematical-lens transfer is visible rather than hidden inside equations. | `C.29` may be needed when the dynamics model crosses contexts, scales, or representation regimes. |

#### A.3.3:9.1 - Quick use cards

* **Dynamics predicts.** It is a state-space and transition-law episteme.
* **Work reveals.** Measurements, logs, and actuals belong to work, evidence, or source values.
* **Method guides.** A method may use dynamics, but dynamics is not the method.
* **State space first.** No state-space characteristics, no reviewable dynamics claim.
* **Observation matters.** A law without observation relation cannot be compared with traces.
* **Prediction is not authority.** Gate and release claims need their governing patterns.

