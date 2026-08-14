---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__011_rationale.md"
commit_sha: "7205ce8cea50eb778520a026373b2b7bcbc43fbb"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:10 — Rationale"
line_start: 70596
line_end: 70601
dependencies:
  - "A.6.RCD"
  - "A.6.REL"
  - "C.32.ADR"
  - "C.32.PAD"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.24.PUB"
  - "E.4"
  - "E.4.DPF"
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:10 - Rationale

Framework authors do need a recurring set of framework-specific questions, so removing every PFAD locator would make the entry harder to discover. They do not need a separate PFAD relation or record: `E.9` already carries one bounded answer, alternatives, rationale, consequences, action, and reopen condition. Direct assertions preserve the selected initial pattern relations without making their representation authoritative.

PFAD is therefore a profile by practical question and content, not a new ontological kind or a second stage.

