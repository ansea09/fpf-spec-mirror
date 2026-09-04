---
chunk_kind: "child"
pattern_id: "A.3.3"
pattern_title: "U.Dynamics: State-Space and Transition-Law Episteme"
section_id: "A.3.3:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/A.3.3/A.3.3__012_sota-echoing.md"
commit_sha: "9a9c1b14df894386c664cf49a9ccbbd4a4063100"
heading_path:
  - "A.3.3 — U.Dynamics: State-Space and Transition-Law Episteme"
  - "A.3.3:11 — SoTA-Echoing"
line_start: 9254
line_end: 9265
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

### A.3.3:11 - SoTA-Echoing

| Source line | Source refs | Adopt, adapt, or reject | Effect in this pattern |
| --- | --- | --- | --- |
| Current constructor-theory and process-theory work | Gogioso, Wang-Mascianica, Waseem, Scandolo, and Coecke, "Constructor Theory as Process Theory", EPTCS 397, 2023, arXiv:2401.05364; Deutsch and Marletto, "Constructor theory of time", arXiv:2505.08692v3, revised 2026-06-05. | Adapt: dynamics, transformations, tasks, and processes are kept close without collapsing law, method, mechanism, and work. | `U.Dynamics` remains a law-of-change episteme; `A.3.4` admits an actual transformation only from the exact changed referent, temporal or formal boundary, boundary conditions, actual subject facts, and continuity or reidentification; possible, predicted, simulated, or probable change and every work or authority claim remain separate. |
| Current data-driven predictive-control work | de Jong, Breschi, Schoukens, and Lazar, "Koopman Data-Driven Predictive Control with Robust Stability and Recursive Feasibility Guarantees", arXiv:2405.01292; Shang, Cortes, and Zheng, "On the Exponential Stability of Koopman Model Predictive Control", arXiv:2511.02008. | Adopt: prediction, lifted state, stability, recursive feasibility, and prediction error need explicit state-space, model, horizon, and constraint declarations. | `stateSpace`, `transitionLaw`, `applicabilityWindow`, `constraintsOrInvariants`, and prediction-use conditions are mandatory before comparison or gate use. |
| Current stochastic predictive-control work | Knaup and Tsiotras, "Recursively Feasible Stochastic Model Predictive Control for Time-Varying Linear Systems Subject to Unbounded Disturbances", arXiv:2410.11107. | Adopt: stochasticity, unbounded disturbances, time variation, feasibility, and chance constraints must not be hidden behind one model label. | `stochasticity`, `inputsOrDisturbances`, tolerance policy, and applicability window are explicit fields. |
| Current digital-twin validation pressure | Russell Bernal, Petterson, Alarcon Granadeno, Murphy, Mason, and Cleland-Huang, "Validating Terrain Models in Digital Twins for Trustworthy sUAS Operations", arXiv:2508.16104. | Adapt: model validation depends on operational context, observation limits, granularity, uncertainty, and real-world use conditions. | Observation relation, evidence relation, operating region, and source-currentness condition remain separate from the dynamics law. |
| Historical state-space, declarative, and imperative contrasts | Classical state-space control, early declarative programming, workflow slogans, and process-model slogans. | Reject as current SoTA by themselves; retain only as lineage and recognition cues. | The pattern repairs by FPF kind, state-space declaration, and slot relation rather than by programming-paradigm or process-slogan labels. |

Lower current use of this pattern when current work on process theory, predictive control, hybrid systems, stochastic dynamics, digital twins, causal dynamics, learned world models, graph representations, equivalence representations, or FPF's own characteristic-space, temporal, mathematical-lens, transformation, work, evidence, and gate patterns changes the governing distinction.

