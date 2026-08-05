---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__012_sota-echoing.md"
commit_sha: "6709213844a26981daf25510ac99ffb7fa53b017"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:11 — SoTA-Echoing"
line_start: 62478
line_end: 62487
dependencies:
  - "A.10"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.3.3"
  - "B.2.5"
  - "B.3"
  - "C.27"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.STRAT"
  - "C.30.TFS-REL"
  - "E.17.0"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller and plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:11 - SoTA-Echoing

| SoTA and practice source | What it contributes | FPF adoption stance | Practitioner implication |
| --- | --- | --- | --- |
| Anderson, Doyle, Low, and Matni, "System Level Synthesis" (Annual Reviews in Control, 2019). | Structured controller-synthesis practice treats closed-loop responses, constraints, locality, and distributed implementation as explicit synthesis variables and implementation relations rather than as a box-and-arrow guarantee. | Adopt and adapt: use SLS as current control-structure pressure for explicit role, relation, locality, rate, and implementation-boundary fields; do not import SLS proof claims into C.30.LCA. | A distributed-control diagram can start a control-structure description; stability or robust-performance claims are governed by dynamics or control-proof patterns. |
| Ames, Coogan, Egerstedt, Notomista, Sreenath, and Tabuada, "Control Barrier Functions: Theory and Applications" (ECC, 2019). | Safety-critical control separates a controller structure from a safety property and the mathematical certificate or enforcement method used for that property. | Adopt and adapt: keep safety wording visible as a neighboring safety or proof claim, not as control-view adequacy. | When a sentence says the supervisor/controller makes the plant safe, keep the control description and assign safety to the direct safety, dynamics, evidence, or assurance pattern. |
| Rawlings, Mayne, and Diehl, *Model Predictive Control: Theory, Computation, and Design*, 2nd ed. (2017). | Planner/regulator, receding horizon, constraint, update period, and model-boundary distinctions are current MPC structure cues. | Adopt as control vocabulary: recover roles, rates, model boundaries, and constraints; route temporal/rate claims to `C.27.TA`, authored temporal adequacy to `C.27`, and dynamics to `A.3.3`. | A multi-rate or MPC-style note names rate bands and model boundaries before claiming adequacy. |
| Leveson and Thomas, *STPA Handbook* (2018), as systems-theoretic safety-control practice. | Safety analysis treats unsafe control actions, feedback, process models, constraints, and losses as control-structure-relevant distinctions. | Adopt and adapt: allow safety-loss control-structure notes, while keeping safety-case verdicts and evidence sufficiency outside C.30.LCA. | A loss-control diagram can organize the description; it does not close the safety case. |
| FPF `C.2.1`, `A.22`, `C.30`, `C.30.AD`, `E.17.0`, and `C.30.ASV`. | These patterns separate exact selected control structure, architecture relation/claim, description episteme, viewpoint episteme, conformance occurrence, and described/controlled holon. | Bind `ControlStructureView` to one selected `U.Structure` and exact viewpoint conformance; recover every control relation through its direct pattern. | A control view can coordinate several relations without becoming the architecture, relation occurrence, or proof. |

