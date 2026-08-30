---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:3"
section_title: "Forces"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__004_forces.md"
commit_sha: "8bb4989c9be7fa4b33f0bb7537e4611676ee3087"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:3 — Forces"
line_start: 66177
line_end: 66187
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

### C.32.ADR:3 - Forces

| Force | Tension |
|---|---|
| Reader economy | The record should be short enough to use, but not so short that decision content disappears. |
| Section variation | ADR templates and engineering memos differ, while the decision functions must remain recoverable. |
| Publication and decision separation | The record publishes a description of the decision; it does not become the decision relation. |
| Architecture and method coupling | A record often needs to cite both target structures and required developer methods. |
| Evolution | Supersession, violation detection, and update conditions must be visible without making the record a governance system. |
| Cross-domain use | Software ADR practice must generalize to other holon kinds without importing software-only assumptions. |

