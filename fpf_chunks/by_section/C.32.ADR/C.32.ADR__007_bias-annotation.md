---
chunk_kind: "child"
pattern_id: "C.32.ADR"
pattern_title: "Architecture Decision Record Projection"
section_id: "C.32.ADR:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/C.32.ADR/C.32.ADR__007_bias-annotation.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "C.32.ADR — Architecture Decision Record Projection"
  - "C.32.ADR:6 — Bias-Annotation"
line_start: 61006
line_end: 61016
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

### C.32.ADR:6 - Bias-Annotation

| Risk handled | How C.32.ADR handles it |
|---|---|
| Template-first writing | The record starts from a PAD decision relation and section functions, not from a blank template. |
| Publication-as-decision drift | The ADR projection cites the decision relation and remains a publication object. |
| Architecture-copy drift | Architecture descriptions are cited through `C.30.AD`; the record carries only decision-relevant references. |
| Method prose drift | Method-use instruction is typed through `A.15`, `E.8`, or `E.11.PUR` when live. |
| History loss | Status and supersession are record functions; old records stay recoverable unless governed archival policy says otherwise. |
| Software-only overread | ADR-like projection is generalized by section function and reader use, not by software tool convention. |

