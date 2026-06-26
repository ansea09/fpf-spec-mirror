---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__007_bias-annotation.md"
commit_sha: "f1d0f9319cf1f93129b7691a328a281022252c4e"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:6 — Bias-Annotation"
line_start: 64016
line_end: 64021
dependencies:
  - "C.32.ADR"
  - "C.32.PAD"
  - "C.33"
  - "C.34"
  - "C.35"
  - "E.17"
  - "E.19"
  - "E.21"
  - "E.23"
  - "E.4"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:6 - Bias-Annotation

The main drift is carrier-first decision making: a team starts from ADR headings, a status field, or a template and assumes that filling the file has made the decision. The repair is to fill the decision relation first and publish a projection second.

The second drift is child-pattern duplication: PFAD can become a local restatement of generic decision practice. The repair is to keep only the framework-specific slots live and return generic decision work to `E.9`, `C.32.PAD`, and `C.32.ADR`.

