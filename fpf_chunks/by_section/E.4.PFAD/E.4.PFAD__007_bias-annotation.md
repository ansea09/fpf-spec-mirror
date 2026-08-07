---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:6"
section_title: "Bias-Annotation"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__007_bias-annotation.md"
commit_sha: "b7ec5a0b1dfa4bdae4cf055188219e89cef61a63"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:6 — Bias-Annotation"
line_start: 70321
line_end: 70328
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

### E.4.PFAD:6 - Bias-Annotation

The first drift is form-first decision making: a team starts from a schema, row, ADR heading, or status field and assumes that filling it has settled the architecture. Start from the reader's problem, alternatives, downstream-used boundary, and practical consequence instead.

The second drift is machinery-first entry: proposal, dependency, quality, naming, and publication apparatus appears before the reader knows whether a framework decision is needed. Keep that apparatus conditional on its own receiving use.

The third drift is relation-by-representation: a table row or reference list is treated as the relation it records. State the relation directly; add a representation only when a named maintenance or checking use needs it.

