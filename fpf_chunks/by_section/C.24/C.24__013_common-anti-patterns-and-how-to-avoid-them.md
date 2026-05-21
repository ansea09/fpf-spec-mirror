---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
section_id: "C.24:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "eb2832093c1e482d5fdd4985c3d2011ab240b429"
heading_path:
  - "C.24 — Agentic Tool‑Use & Call‑Planning (C.Agent‑Tools‑CAL)"
  - "C.24:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 42191
line_end: 42198
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

### C.24:8 - Common Anti-Patterns and How to Avoid Them

- **Treating route description as plan.** Avoid by keeping callable logic in `ATC.CallRouteDescription` and keeping `ATC.CallPlan` as one `U.WorkPlan` that cites it.
- **Treating planning as execution.** Avoid by publishing actual burn only through `CheckpointReturn`, `Work`, and `CallGraph`, not inside the plan surface.
- **Burning enactment budget while the live question is still upstream choice or pool policy.** Avoid by rerouting unresolved fixed-option choice to `C.11` and unresolved live-pool governance to `C.19` before building one call plan.
- **Counting a successful probe as committed rollout.** Avoid by publishing one `CheckpointReturn` with a visible commit trigger instead of smuggling rollout through a positive scout result.
- **Hiding stop conditions or replan triggers.** Avoid by making them part of the public plan surface rather than one private implementer intuition.

