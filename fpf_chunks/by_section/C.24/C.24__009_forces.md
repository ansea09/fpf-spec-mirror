---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__009_forces.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:3 — Forces"
line_start: 52690
line_end: 52698
dependencies:
  - "A.1"
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.5"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.24"
  - "C.28"
  - "C.5"
  - "E.10.MOVE"
  - "E.11.PUR"
  - "E.23"
  - "E.3"
  - "E.5"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
  - "U.WorkPlan"
keywords:
---

### C.24:3 - Forces

| Force                                    | Tension                                                                                                                 |
| ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| **General methods vs. bespoke local heuristics**       | Scalable, model-centric search ↔ short-term wins of bespoke scripts (guarded by **Bitter-Lesson Preference**).        |
| **Assurance vs. Autonomy**               | F-G-R gates & CL penalties ↔ system latitude to sequence calls and learn online.                                       |
| **Exploration vs. Delivery**             | Exploration share for illumination ↔ delivery SLAs and cost ceilings (E/E-LOG policy).                                |
| **Method vs. route vs. plan vs. execution** | exact `U.Method` ↔ separate `U.MethodDescription` ↔ `U.WorkPlan` ↔ dated `U.Work` ↔ service promises (`U.PromiseContent`). |

