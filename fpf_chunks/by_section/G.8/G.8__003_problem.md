---
chunk_kind: "child"
pattern_id: "G.8"
pattern_title: "Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
section_id: "G.8:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/G.8/G.8__003_problem.md"
commit_sha: "4ce2f7202e12c5c519a3466f5e07fe0b92e78a44"
heading_path:
  - "G.8 — Package Method-Family Admissibility Rules and Maturity Ladders (SoS-LOG)"
  - "G.8:2 — Problem"
line_start: 128493
line_end: 128500
dependencies:
  - "A.10"
  - "A.21"
  - "B.3"
  - "C.18"
  - "C.19"
  - "C.22"
  - "C.23"
  - "E.10"
  - "E.17"
  - "E.18"
  - "E.5.2"
  - "F.17"
  - "F.8"
  - "F.9"
  - "G.10"
  - "G.11"
  - "G.4"
  - "G.5"
  - "G.6"
  - "G.7"
  - "G.Core"
keywords:
  - "SoS-LOG"
  - "admissibility ledger"
  - "rule ids"
  - "tri-state {pass"
---

### G.8:2 - Problem

1. **Selector needs a stable input artefact.** `G.5` cannot consume “maturity narratives” and scattered SoS‑LOG snippets without re‑authoring semantics or inventing implicit defaults.
2. **Thresholds leak into LOG.** Numeric gates embedded directly into rule text or ladder rungs blur the boundary between LOG decisions (`C.23`) and Acceptance thresholds (`G.4`).
3. **Auditability is brittle.** Decisions (`pass/degrade/abstain`) lack stable, citable links to evidence paths (`G.6`) and crossing pins (Bridge/CL/Φ policy ids as required for the stated use), so later re‑checks and RSCR become ad‑hoc.
4. **Telemetry contaminates decision semantics.** Undeclared use of QD/OEE/illumination signals in dominance, or a changed definition edition, can alter outcomes without making the new basis visible.
5. **Refresh is under‑specified.** Bundle evolution (rules, ladders, pins, policies, editions) must be RSCR‑addressable via typed trigger kinds, not by free‑text “reasons”.

