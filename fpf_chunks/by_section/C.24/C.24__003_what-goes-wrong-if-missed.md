---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:0.1"
section_title: "What goes wrong if missed"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__003_what-goes-wrong-if-missed.md"
commit_sha: "5801dc610c657ac7b1efee349b18e80ce6d7df6f"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:0.1 — What goes wrong if missed"
line_start: 51246
line_end: 51252
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.28"
  - "C.5"
  - "E.17"
  - "E.23"
  - "E.24.PUB"
  - "G.5"
  - "G.6"
  - "G.9"
  - "U.PromiseContent"
keywords:
---

### C.24:0.1 - What goes wrong if missed

- a route is scheduled by an opaque heuristic, so nobody can see which budget is being burned or what should stop it;
- unresolved choice or pool-policy work is smuggled into a plan;
- a route description is mistaken for a Method, a plan for performed Work, or a successful probe for committed rollout; and
- replanning loses the decision that made the route admissible in the first place.

