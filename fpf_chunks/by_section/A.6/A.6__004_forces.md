---
chunk_kind: "child"
pattern_id: "A.6"
pattern_title: "Signature Stack & Boundary Discipline"
section_id: "A.6:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6/A.6__004_forces.md"
commit_sha: "b22b6993b3e94f7896d5dc1cd011af7bc3f49b0d"
heading_path:
  - "A.6 — Signature Stack & Boundary Discipline"
  - "A.6:3 — Forces"
line_start: 6993
line_end: 7004
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.20"
  - "A.21"
  - "A.6"
  - "A.6.0"
  - "A.6.1"
  - "A.6.3"
  - "A.6.B"
  - "A.6.P"
  - "A.7"
  - "B.3"
  - "C.26"
  - "C.26.1"
  - "C.28"
  - "E.10"
  - "E.10.D2"
  - "E.17"
  - "E.17.0"
  - "E.17.EFP"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "U.EpistemicViewing"
  - "U.Mechanism"
  - "U.MultiViewDescribing"
  - "U.Signature"
  - "U.View"
  - "U.Viewpoint"
  - "U.Work"
keywords:
  - "A.6.B L/A/D/E claims"
  - "Confuses deontics with mathematical admissibility"
  - "Rewrite as declarative predicate"
  - "authority-wording split"
  - "boundary"
  - "boundary claim-classification fields"
  - "in invariants"
  - "probe/order/frame/export/state-reading claims"
  - "promise/commitment/API/policy wording"
  - "reference predicate IDs from CC when needed"
  - "register-backed status boundary"
  - "signature stack"
  - "undermines auditability"
  - "“MUST” appears inside Definition: blocks"
---

### A.6:3 - Forces

| Force                                        | Tension                                                                                                                                                            |
| -------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Modularity vs expressiveness**             | A stable boundary must be abstract, but users want operational detail “in the same doc”.                                                                           |
| **Truth vs governance**                      | Definitions/invariants (“is”, “iff”, “∀”) vs permissions/obligations (“MUST/SHOULD/MAY”).                                                                          |
| **Design‑time clarity vs run‑time evidence** | What can be checked statically vs what requires executing work and observing traces.                                                                               |
| **View vs viewpoint discipline**             | Views are projections; viewpoints are accountable stances. Dropping viewpoint loses architecture accountability (ISO‑style discipline is already encoded in MVPK). |
| **Local meaning vs cross‑context reuse**     | Boundaries should be local to a bounded context; reuse must be explicit (Bridges/CL), not hidden.                                                                  |
| **Evolvability vs auditability**             | Evolving interfaces requires change; auditors require stable evidence trails.                                                                                      |
| **Human readability vs formal precision**    | Plain explanations vs tech‑register constraints; both must remain aligned.                                                                                         |

