---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:8"
section_title: "Common Anti-Patterns and How to Avoid Them"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__013_common-anti-patterns-and-how-to-avoid-them.md"
commit_sha: "353d59d1c2167344cfff99cadbf413c587c14a66"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:8 — Common Anti-Patterns and How to Avoid Them"
line_start: 53670
line_end: 53680
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

### C.24:8 - Common Anti-Patterns and How to Avoid Them

- **Planning the whole tool lifecycle.** Keep candidate generation, selection, execution, scoring, and publication outside C.24.
- **Route description as Method.** Recover the Method or keep the route in probe state.
- **Plan as execution.** Put actual burn and call facts in Work-side results and the trace.
- **BLP slogan as comparison.** Use C.19.1's probe and any selected comparison; keep a waiver separate or return no scale claim or no scale-based preference.
- **Catch-all policy or profile ref.** Cite the actual PoolPolicyResult, EmitterPolicy, C.19.1 result, B.3 result, or domain-defined constraint, or omit the branch.
- **Confidence threshold as assurance.** Use a direct condition and cite B.3 only for a named assurance use.
- **Executable adaptation by implication.** Store the binding in a route description; identify any executable adaptation independently.
- **Successful probe as commitment.** Require a checkpoint with a commit trigger.

