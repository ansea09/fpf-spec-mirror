---
chunk_kind: "child"
pattern_id: "B.2.5"
pattern_title: "Supervisor-Subholon Feedback Loop"
section_id: "B.2.5:11"
section_title: "SoTA-Echoing"
source_path: "FPF-Spec.md"
output_path: "by_section/B.2.5/B.2.5__012_sota-echoing.md"
commit_sha: "20c8a0a53eda448bd9d019c860be4517a6e822cc"
heading_path:
  - "B.2.5 — Supervisor-Subholon Feedback Loop"
  - "B.2.5:11 — SoTA-Echoing"
line_start: 31649
line_end: 31657
dependencies:
  - "A.1"
  - "A.12"
  - "A.15"
  - "A.2"
  - "A.3"
  - "A.7"
  - "B.2"
  - "C.30.LCA"
keywords:
  - "control architecture"
  - "feedback loop"
  - "layered control"
  - "stability"
  - "supervisor"
---

### B.2.5:11 - SoTA-Echoing

| SoTA/practice anchor | What it informs | FPF adoption stance | Practitioner implication |
|---|---|---|---|
| Layered and multi-rate control architecture practice, with Matni/Ames/Doyle used here as lineage and practice lineage for layered multi-rate control rather than as current proof by itself. | Supervisor, plant, controller, planner, observer, feedback, and rate separation are useful relation cues for supervisor-subholon loop recovery. | Adopt and adapt: keep supervisor-subholon loop recognition, then assign stability, timing, safety, evidence, assurance, and gate claims to their governing patterns. | A loop diagram starts the relation record; dynamics, timing, and safety claims still need their own pattern. |
| Cyber-physical systems and feedback-control practice. | Shared medium limits, observation channels, actuation, delay, disturbance, and plant dynamics affect whether a loop is adequate. | Adopt: require loop closure and medium visibility; assign reusable dynamics claims to `A.3.3`. | If communication delay matters, it is not solved by the B.2.5 label. |
| Organizational policy and review practice. | Supervisory relations can be enacted through policies, review boards, reports, and publication channels. | Adapt: model the acting systems/practices and publication/source or reliance relations explicitly. | A committee or review practice may supervise; a published note does not act by itself. |
| FPF architecture-description discipline under `C.30` and `C.30.LCA`. | A supervisor loop can be one relation inside a control-structure view. | Reuse: `B.2.5` supplies relation recovery; `C.30.LCA` supplies view recovery. | Use the pattern that governs the claim kind being made, then add the related pattern only when a second claim being made is present. |

