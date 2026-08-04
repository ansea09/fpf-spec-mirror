---
chunk_kind: "child"
pattern_id: "E.4.PFAD"
pattern_title: "Principle-Framework Architecture Decision"
section_id: "E.4.PFAD:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/E.4.PFAD/E.4.PFAD__002_problem-frame.md"
commit_sha: "7ba40a95a967ca5c69afc63aeca381e6adedc8da"
heading_path:
  - "E.4.PFAD — Principle-Framework Architecture Decision"
  - "E.4.PFAD:1 — Problem frame"
line_start: 70213
line_end: 70220
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
  - "E.4.DPF.DA"
  - "E.4.PFR"
  - "E.9"
  - "F.18"
  - "G.11"
  - "G.2"
keywords:
---

### E.4.PFAD:1 - Problem frame

Use this pattern when a framework author or steward must decide the architecture of one FPF-grounded domain principle framework or local practice framework: its purpose, selected pattern set, relation structure, publication or access carrier, dependency boundary, names, source basis, quality route, and currentness route.

Primary `EntityOfConcern`: `PrincipleFrameworkArchitectureDecision@Context`, a framework-local architecture decision relation with explicit slots. The first useful output is a filled decision relation, not an ADR document and not the realized framework itself.

Use this pattern only when the decision has framework-specific obligations beyond generic architecture-decision practice. If the decision only needs ordinary decision rationale or ordinary project architecture decision slots, use `E.9`, `C.32.PAD`, and `C.32.ADR` directly.

