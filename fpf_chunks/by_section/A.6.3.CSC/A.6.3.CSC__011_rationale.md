---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__011_rationale.md"
commit_sha: "b74ecf2b633a2315086198e4aab07c2b61257c27"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:10 — Rationale"
line_start: 11920
line_end: 11927
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "C.26"
  - "C.26.1"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
  - "coarsened rendering"
  - "controlled semantic coarsening"
  - "dashboard tile"
  - "lookup handle"
  - "narrower admissible use"
  - "non-admissible downstream use"
  - "redaction"
  - "reopen trigger"
  - "source-bearing episteme or source publication"
  - "state-representation shortcut"
---

### A.6.3.CSC:10 - Rationale

Controlled coarsening is useful because FPF work often needs cheap readable forms. It is risky because cheap readable forms often travel farther than their admissible use. The pattern therefore does not ban coarsened renderings; it makes the source-to-rendering relation explicit enough that later users know when to stop, reopen, or hand off to another governing FPF pattern or `authoritySourceRef` destination.

This pattern is narrower than a general simplification pattern. It applies only when the coarsened rendering remains tied to a source-bearing side and carries a narrower-use card.

The core memory aid is simple: a coarsened rendering may help interpretation, but it must not become the source-bearing side it was derived from. It may expose or cite the source-bearing side or the project-side FPF kind and reference named by value that carries the requested admissibility; that exposed source or value remains the admissibility source, not the coarsened rendering's readable face. If admissibility is missing, a repair request, source-gap note, or reopen note may guide only future repair or return to source; it does not backdate the coarsened rendering into source relation.

