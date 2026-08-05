---
chunk_kind: "child"
pattern_id: "C.24"
pattern_title: "Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
section_id: "C.24:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.24/C.24__015_rationale.md"
commit_sha: "3dbce51436bfd718bf49cb0356eebce70c4fc015"
heading_path:
  - "C.24 — Agentic Tool-Use and Call Planning (C.Agent-Tools-CAL)"
  - "C.24:10 — Rationale"
line_start: 52960
line_end: 52968
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

### C.24:10 - Rationale

`C.24` exists because tool-use systems fail in a distinctive way: they can look adaptive while actually hiding route choice, budget burn, stop conditions, and replan logic inside one opaque execution chain. A separate planning calculus is therefore necessary so that tool use remains auditable, replayable, and governable before the first irreversible call is made.

Source-use relation and source-currentness for this rationale: these rows are current-practice pressure and BLP-neighbour alignment, not a standalone `SoTA-Echoing` table. A current tool-use or agentic-loop source becomes load-bearing only when it changes one `CallPlan`, `CheckpointReturn`, budget, stop or replan condition, BLP waiver, or relation row.

- Contemporary tool-use systems in agential roles work best when planning, feedback, and replanning stay explicit rather than collapsing into one brittle script. The practical implication is to publish one `U.WorkPlan` whose planned steps select exact Methods, cite route-description epistemes separately when current, and carry stop or replan triggers before execution.
- Post-2015 search, optimization, and agentic systems also show that bounded probing is useful but dangerous when it silently becomes commitment. The safeguard here is the explicit `CheckpointReturn` plus visible commit trigger and one explicit split between planned budget envelope and burned actual budget.
- Scaling-first practice favors general, learnable methods over fragile hand-tuned tactics when assurance and cost remain comparable. The practical implication is not blind optimism but disciplined BLP: when a narrow heuristic wins, record the waiver, expiry, and re-evaluation window.
