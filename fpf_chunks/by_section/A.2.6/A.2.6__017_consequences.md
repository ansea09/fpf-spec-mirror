---
chunk_kind: "child"
pattern_id: "A.2.6"
pattern_title: "Unified Scope Mechanism (USM): Context Slices & Scopes"
section_id: "A.2.6:11.1"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/A.2.6/A.2.6__017_consequences.md"
commit_sha: "b0368ed8d883c04d0b261b03f46c28e23d790dc5"
heading_path:
  - "A.2.6 — Unified Scope Mechanism (USM): Context Slices & Scopes"
  - "A.2.6:11.1 — Consequences"
line_start: 4620
line_end: 4623
dependencies:
  - "A.1.1"
  - "A.2.2"
  - "A.2.3"
  - "B.3"
keywords:
  - "& guard style)"
  - "ClaimScope (G)"
  - "WorkScope"
  - "applicability"
  - "scope"
  - "set-valued"
---

### A.2.6:11.1 - Consequences

A correct USM use makes scope checks reproducible: every membership claim points to a slice, every cross-context reuse names the Bridge and CL loss, and every widening or narrowing changes the declared scope rather than the word around it. The cost is explicitness: a project must name context versions, environment selectors, and `Γ_time` before a guard can admit the claim, work, or publication use.

