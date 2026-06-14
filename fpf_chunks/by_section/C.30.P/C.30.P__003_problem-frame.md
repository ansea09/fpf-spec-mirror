---
chunk_kind: "child"
pattern_id: "C.30.P"
pattern_title: "Architecture and Structure Precision Restoration"
section_id: "C.30.P:1"
section_title: "Problem frame"
source_path: "FPF-Spec.md"
output_path: "by_section/C.30.P/C.30.P__003_problem-frame.md"
commit_sha: "7c617d5d0fa1abf94a21bac2dd909f68ed514249"
heading_path:
  - "C.30.P — Architecture and Structure Precision Restoration"
  - "C.30.P:1 — Problem frame"
line_start: 54150
line_end: 54171
dependencies:
  - "A.10"
  - "A.15"
  - "A.20"
  - "A.21"
  - "A.22"
  - "A.6.F"
  - "A.6.P"
  - "B.3"
  - "C.11"
  - "C.16"
  - "C.16.P"
  - "C.2.P"
  - "C.25"
  - "C.28"
  - "C.29"
  - "C.30"
  - "C.30.ASV"
  - "C.30.ILC"
  - "C.30.LCA"
  - "C.30.TFS-REL"
  - "E.10"
  - "E.10.ARCH"
  - "E.11"
  - "E.17"
  - "E.8"
keywords:
---

### C.30.P:1 - Problem frame

Working engineers often say "architecture" or "structure" while pointing at a useful artifact: a diagram, model, graph, table, dashboard, ADR, code-agent relation graph, neural-network architecture-operation diagram, benchmark result, or source document. Ordinary speech is acceptable; FPF-governed prose is not. If the artifact is named by a source label such as `block`, `layer`, `expert`, `cache`, `router`, or `gate`, use `C.30.STRAT` before assigning the recovered use locally.

The repair question is:

> Which selected structure, architecture relation, architecture-description use, structural-view use, source-return relation, or neighboring claim does the wording name, and which FPF pattern governs that claim?

The architecture or structure use under repair may be:

- selected structure under `A.22`;
- an `ArchitectureOf@Context` claim under `C.30`, a thin architecture-description bridge under `C.30`, or the full architecture-description mechanism under `C.30.AD`;
- an `ArchitectureStructuralView@Context` or named `C.30.*` subcase;
- a publication, view, face, `PublicationUnit`, carrier, dashboard, ADR, source document, or source-return relation under `C.2.P` or `E.17`;
- a relation construction under `A.6.P`;
- a function or functionality-kind use under `A.6.F`;
- a mathematical-lens use claim under `C.29`;
- a characteristic, scale, score, coordinate, threshold, or quality-coordinate claim under `C.16.P` or `C.16`;
- a Q-bundle or quality-characterization claim under `C.16.Q`, `C.25`, or `E.21`;
- an evidence, assurance, gate, work, decision, causal-use, release, or method claim under its governing pattern;
- ordinary prose with no FPF-governed use being made.

