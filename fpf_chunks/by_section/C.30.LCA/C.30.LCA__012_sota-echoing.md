---
chunk_kind: "child"
pattern_id: "C.30.LCA"
pattern_title: "Control Structure View Adequacy (LCA)"
section_id: "C.30.LCA:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.LCA/C.30.LCA__012_sota-echoing.md"
commit_sha: "2e112078bb209e5e3a511c3bd1aa6b1b2e299efe"
heading_path:
  - "C.30.LCA — Control Structure View Adequacy (LCA)"
  - "C.30.LCA:11 — SoTA-Echoing"
line_start: 52504
line_end: 52512
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
  - "C.30.ASV"
  - "C.30.TGA-FLOW-REL"
  - "E.18"
  - "G.6"
keywords:
  - "control layer"
  - "control-structure view"
  - "controller/plant"
  - "layered control architecture"
  - "proof overread"
  - "rate band"
  - "supervisor loop"
---

### C.30.LCA:11 - SoTA-Echoing

| SoTA/practice anchor | What it supports | FPF adoption stance | Practitioner implication |
|---|---|---|---|
| Layered and multi-rate control architecture practice, with Matni/Ames/Doyle used here as lineage and practice basis for quantitative layered multi-rate control rather than as current proof by itself. | Planner, controller/regulator, observer, plant, supervisor, rate separation, and feedback relations are recognizable control-structure-view content. | Adopt and adapt: use the practice vocabulary to start or check a control-structure view, then assign stability, safety, timing, evidence, assurance, and gate claims to their governing FPF patterns. | A control-stack diagram can start a view record; it cannot close stability, safety, or evidence review. |
| Feedback-control and cyber-physical systems practice. | Observation, actuation, plant dynamics, disturbances, and externality boundaries matter for control adequacy. | Adopt: keep boundary fields visible in the control view and assign dynamics/timing claims out. | If timing or plant behavior matters, open `C.27` or `A.3.3` instead of adding more claim force to the LCA sentence. |
| ISO/IEC/IEEE 42010 architecture-description practice. | Architecture descriptions use viewpoints and views over concerns, and several views may describe one architecture. | Adopt and adapt: bind `ControlStructureView@Context` to `DescriptionContext` and `ArchitectureOf@Context`. | A control view is a view under a declared concern, not the architecture itself. |
| FPF `B.2.5` supervisor-subholon feedback-loop material. | Supervisor-subholon relations are already useful FPF pattern material for feedback-loop recognition. | Reuse with boundary: cite `B.2.5` for the relation, not for proof. | A supervisor loop becomes inspectable without becoming evidence, assurance, or gate authority. |

