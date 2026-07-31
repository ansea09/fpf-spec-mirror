---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:10"
section_title: "Rationale"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__011_rationale.md"
commit_sha: "373c87917e92123cfa039e24c42a1f122b54fb66"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:10 — Rationale"
line_start: 66250
line_end: 66257
dependencies:
  - "A.10"
  - "A.15"
  - "A.21"
  - "B.3"
  - "C.16"
  - "C.25"
  - "C.29"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.32.ADA"
  - "C.32.P2S"
  - "C.32.PAD"
  - "E.11.PUR"
  - "E.17"
  - "E.24.PUB"
  - "E.8"
keywords:
  - "ADR projection"
  - "ArchitectureDecisionDescription@Project"
  - "ArchitectureDecisionRecordProjection@Project"
  - "architecture decision record"
  - "consequences"
  - "method-use instruction"
  - "publication boundary"
  - "rationale"
  - "section function"
  - "supersession"
---

### C.32.ADR:10 - Rationale

ADR practice is valuable when it makes architectural decisions communicable and revisitable. It becomes weak when a record is treated as the decision itself or when a template substitutes for decision work.

C.32.ADR therefore uses the record as a projection. The decision relation is made in `C.32.PAD`; the record publishes a decision description for a declared reader. This preserves the strongest ADR practice, small and updateable records, while adding FPF kind control for architecture descriptions, method descriptions, evidence, assurance, gate, publication, and performed work.

The pattern also generalizes ADR practice beyond software by using section functions rather than software-specific carrier assumptions. A record can be a Markdown file, engineering memo, or certification rationale if it projects the decision description and keeps receiving claims with their governing patterns.

