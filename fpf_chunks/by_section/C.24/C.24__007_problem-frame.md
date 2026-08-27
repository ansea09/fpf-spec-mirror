---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__007_problem-frame.md"
commit_sha: "322625be006f38158e4e7d600f662558f03df77a"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:1 — Problem frame"
line_start: 52309
line_end: 52314
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.1"
  - "A.15.2"
  - "A.15.7"
  - "B.1.6"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.18"
  - "C.19"
  - "C.19.1"
  - "C.2.1"
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

### C.24:1 - Problem frame

Tool-using Systems may plan across web services, local programs, instruments, robots, or human-operated routes. The implementation may be an LLM agent, a search system, a conventional planner, or a fixed program. The planning problem is the same: turn a fixed action or option into an ordered and bounded route without hiding route grounding, budget, or stop logic.

A local system-role kind or assignment is recorded only when that separate fact matters. When planning, revision, or a call is claimed as performed Work, the admitted System, dated Work, Method, interval, and applicable attribution facts remain recoverable through `A.15.1`, `A.2.1`, and `F.6`.

