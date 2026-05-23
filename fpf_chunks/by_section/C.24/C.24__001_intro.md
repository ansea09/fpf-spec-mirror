---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
section_id: "C.24:intro"
section_title: "Intro"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__001_intro.md"
commit_sha: "04dd733fb18b66d3a640d11758e0af22ea253fd8"
heading_path:
  - "C.24 — Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
  - "C.24:intro — Intro"
line_start: 42833
line_end: 42848
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

## C.24 - Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)

> **Type:** Calculus (C)
> **Status:** Stable
> **Normativity:** Normative

**Plain-name.** Agentic tool-use and call planning.

**Intent.** Govern admissible tool-call planning and replanning under explicit budget, assurance, and policy while keeping upstream choice, pool policy, planning, and execution distinct.

**Instantiates / Refines Pillars.** `E.2` `P-3` Scalable Formality, `P-7` Pragmatic Utility, `P-10` Open-Ended Evolution, `P-11` SoTA Alignment, and the Bitter-Lesson Preference: prefer scalable, general methods that benefit from more data or compute over fragile hand-tuned heuristics when assurance and cost stay comparable.

**Depends on.** A-kernel (`A.1–A.15`) for holonic basics and Role-Method-Work separation; `B.3` Trust & Assurance (`F–G–R` with CL penalties); `E.3/E.5` (precedence and Guard-Rails); `C.5` `Resrc-CAL`; `C.18` `NQD-CAL` (candidate generation and declared set surfaces); `C.19` `E/E-LOG` (explore-exploit policies); optional `Compose-CAL` and `KD-CAL` where available.

**Coordinates with.** `U.WorkPlan` and `U.PromiseContent` bindings (acceptance gates), Working-Model publication discipline per `B.3`, and Evidence/Provenance (`G.6`).

