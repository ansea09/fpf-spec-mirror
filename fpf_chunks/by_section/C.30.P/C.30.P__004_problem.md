---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Clarify Architecture and Structure Wording (Precision Restoration)"
section_id: "C.30.P:2"
section_title: "Problem"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__004_problem.md"
commit_sha: "61a9542aa8479024cdd174c024079d2a6a15f16d"
heading_path:
  - "C.30.P — Clarify Architecture and Structure Wording (Precision Restoration)"
  - "C.30.P:2 — Problem"
line_start: 68000
line_end: 68010
dependencies:
  - "A.10"
  - "A.15"
  - "A.19.CPM"
  - "A.19.SelectorMechanism"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.18"
  - "C.19"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.AD"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "C.32"
  - "C.32.CONWAY"
  - "C.32.FAIL"
  - "C.32.MLAO"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
  - "G.5"
keywords:
  - "architecture description"
  - "architecture wording"
  - "diagram"
  - "model"
  - "precision restoration"
  - "structural view"
  - "structure wording"
---

### C.30.P:2 - Problem

How can FPF repair architecture or structure wording without:

- creating `U.Architecture`;
- treating architecture and structure as one fused kind;
- treating a description, view, diagram, graph, dashboard, source, ADR, model, or publication as the architecture itself;
- assigning all function, flow, module-interface, signature, control, evidence, assurance, gate, decision, work, quality, mathematical-lens, or source claims to architecture;

- duplicating first-stage repair lists inside `A.22`, `C.30`, `C.30.ASV`, and every named `C.30.*` subpattern?

