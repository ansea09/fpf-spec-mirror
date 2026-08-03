---
chunk_kind: "child"
pattern_id: "A.6.3.CSC"
pattern_title: "Controlled Semantic Coarsening"
section_id: "A.6.3.CSC:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/A.6.3.CSC/A.6.3.CSC__011_rationale.md"
commit_sha: "9dd9215969126625d449a40e8ca4d1df9ac903f8"
heading_path:
  - "A.6.3.CSC — Controlled Semantic Coarsening"
  - "A.6.3.CSC:10 — Rationale"
line_start: 13936
line_end: 13943
dependencies:
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.6.3"
  - "A.6.3.CR"
  - "A.6.3.NAR"
  - "A.6.3.RT"
  - "A.6.4"
  - "A.6.P"
  - "C.2.1"
  - "C.26"
  - "C.26.1"
  - "C.33"
  - "E.10"
  - "E.17.EFP"
  - "E.17.ID.CR"
  - "E.19"
  - "E.24.PUB"
  - "E.8"
  - "F.18"
  - "F.9"
  - "F.9.1"
keywords:
---

### A.6.3.CSC:10 - Rationale

Controlled coarsening is useful because FPF work often needs cheap readable forms. It is risky because cheap readable forms often travel farther than their admissible use. The pattern therefore does not ban coarsened renderings; it makes the source-to-rendering relation explicit enough that later users know when to stop, reopen, or hand off to another governing FPF pattern or `authoritySourceRef` destination.

This pattern is narrower than a general simplification pattern. It applies only when the coarsened rendering remains tied to a source-bearing side and carries a narrower-use card.

The core memory aid is simple: exact coarsened episteme `Y` may help interpretation, but it must not become exact source episteme `X`. A publication occurrence, form, carrier, source set, model, graph, or evidence set may expose or be designated by an endpoint but cannot replace one. If admissibility is missing, a repair or return note guides only future work and does not backdate `Y` into source relation or authority.

