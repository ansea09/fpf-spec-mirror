---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
section_id: "C.24:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__009_forces.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.24 — Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
  - "C.24:3 — Forces"
line_start: 42903
line_end: 42911
dependencies:
  - "A.1"
  - "A.15"
  - "B.3"
  - "C.11"
  - "C.18"
  - "C.19"
  - "C.28"
  - "C.5"
  - "E.2"
  - "E.3"
  - "E.5"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
  - "U.WorkPlan"
keywords:
  - "BLP tolerances"
  - "CallGraph"
  - "CallPlan"
  - "CallRouteDescription"
  - "CheckpointReturn"
  - "agential tool use"
  - "budget and harm gates"
  - "enactment budget"
  - "route-vs-plan-vs-work distinction"
  - "stop/replan condition"
  - "tool-call budget"
---

### C.24:3 - Forces

| Force                                    | Tension                                                                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **General methods vs. hand-craft**       | Scalable, model-centric search ↔ short-term wins of bespoke scripts (guarded by **Bitter-Lesson Preference**).        |
| **Assurance vs. Autonomy**               | F-G-R gates & CL penalties ↔ system latitude to sequence calls and learn online.                                       |
| **Exploration vs. Delivery**             | Exploration share for illumination ↔ delivery SLAs and cost ceilings (E/E-LOG policy).                                |
| **Route vs. plan vs. execution**         | `U.MethodDescription` ↔ `U.WorkPlan` ↔ `U.Work` ↔ service promises (`U.PromiseContent`).                              |

