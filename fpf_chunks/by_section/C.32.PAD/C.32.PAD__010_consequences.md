---
chunk_kind: "child"
pattern_id: "C.32.PAD"
pattern_title: "Project Architecture Decision After Candidate Synthesis"
section_id: "C.32.PAD:9"
section_title: "Consequences"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.PAD/C.32.PAD__010_consequences.md"
commit_sha: "b999972c4b60e6cef7206f9bbd777423e6525ec5"
heading_path:
  - "C.32.PAD — Project Architecture Decision After Candidate Synthesis"
  - "C.32.PAD:9 — Consequences"
line_start: 66342
line_end: 66350
dependencies:
  - "A.10"
  - "A.15"
  - "A.15.6"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.2"
  - "A.2.1"
  - "A.21"
  - "B.2"
  - "B.2.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.TFS-REL"
  - "C.31"
  - "C.31.ASAP"
  - "C.32"
  - "C.32.ACE"
  - "C.32.ACS"
  - "C.32.ADA"
  - "C.32.ADR"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "C.32.P2S"
  - "E.11.PUR"
  - "E.17"
  - "E.18.NET"
  - "E.24.PUB"
  - "E.8"
  - "G.5"
keywords:
  - "ArchitectureDecisionRelation@Project"
  - "accepted loss"
  - "affected selected structure"
  - "architect-developer split"
  - "architecture-characteristic trade-off"
  - "method-use instruction"
  - "project architecture decision"
  - "reopen condition"
  - "selected architecture option"
---

### C.32.PAD:9 - Consequences

| Consequence | Benefit | Cost |
|---|---|---|
| The architecture decision relation to exact composite project work is explicit before publication. | ADRs, design memos, and governance files can describe a recoverable decision rather than inventing one. | The architect performs decision work before publication work. |
| Structure and method are coupled without collapsing. | Developers can see both intended architecture structures and required methods. | The decision record needs enough detail to avoid empty method instructions. |
| Trade-offs and accepted losses are recorded. | Later teams can reopen the decision under changed characteristics instead of guessing the original rationale. | Decisions may look less tidy because loss is visible. |
| Architect-developer split is stated. | Team refinement can proceed without losing source return. | Architecture governance must maintain split and reopen conditions. |

